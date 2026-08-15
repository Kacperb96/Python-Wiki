# Outbox pattern python

## O czym jest ten rozdział

Outbox pattern to jeden z najważniejszych wzorców łączących bazę danych z publikowaniem wiadomości albo eventów.

Problem, który rozwiązuje, jest bardzo praktyczny.

Masz flow:

1. zapisujesz stan biznesowy w bazie,
2. chcesz opublikować event do brokera.

I od razu pojawia się niebezpieczne pytanie:

- co jeśli baza się zapisała, ale event nie został wysłany?
- albo odwrotnie: event poszedł, ale stan nie został poprawnie utrwalony?

To właśnie miejsce, gdzie outbox pattern robi ogromną różnicę.

## Najprostsza intuicja problemu

Załóżmy, że po utworzeniu zamówienia chcesz opublikować event `order.created`.

Naiwny kod myślowy:

1. `INSERT INTO orders ...`
2. `publish("order.created")`

Brzmi niewinnie.

Ale co jeśli między tymi dwoma krokami:

- aplikacja padnie,
- broker chwilowo nie działa,
- połączenie sieciowe pęknie,
- event nie dojdzie?

Wtedy masz stan w bazie bez odpowiadającego mu eventu.

Albo odwrotny problem:

- event został opublikowany,
- ale transakcja z bazą finalnie się nie utrwaliła.

Wtedy inne systemy dowiedziały się o czymś, co formalnie nie istnieje.

## Najprostsza intuicja outbox pattern

Outbox pattern mówi w uproszczeniu:

- nie publikuj eventu bezpośrednio jako osobnego, luźnego kroku,
- zapisz go najpierw do tabeli outbox w tej samej transakcji co główny stan biznesowy,
- osobny proces później bezpiecznie publikuje wiadomości z outboxa do brokera.

To jest klucz.

## Jak to wygląda krok po kroku

### Krok 1

W jednej transakcji zapisujesz:

- rekord biznesowy,
- rekord eventu w tabeli outbox.

### Krok 2

Transakcja się commit-uje.

### Krok 3

Osobny publisher czyta nieopublikowane rekordy z outboxa.

### Krok 4

Publikuje je do brokera.

### Krok 5

Oznacza je jako wysłane.

## Najważniejsza korzyść

Masz gwarancję, że:

- jeśli stan biznesowy został utrwalony,
- to odpowiadający mu event też jest zapisany lokalnie i nie zniknie przez chwilową awarię publishowania.

To ogromna poprawa niezawodności.

## Przykład tabeli outbox

Przykładowe pola:

- `id`
- `event_type`
- `aggregate_type`
- `aggregate_id`
- `payload`
- `created_at`
- `published_at`
- `status`

Najprostsza intuicja:

- outbox to lokalna kolejka oczekujących wiadomości oparta o bazę.

## Mini case study: order created

Masz flow tworzenia zamówienia.

### Naiwny wariant

1. tworzysz `orders`,
2. próbujesz wysłać `order.created` do brokera.

Ryzyko:

- brak spójności między bazą i messagingiem.

### Wariant z outboxem

W jednej transakcji:

1. tworzysz `orders`,
2. zapisujesz rekord `order.created` do `outbox`.

Potem osobny proces publikuje event.

W efekcie:

- nie tracisz informacji o potrzebie publikacji,
- nawet jeśli broker chwilowo nie działa.

## Minimalna symulacja w Pythonie

```python
orders = []
outbox = []


def create_order(order_id: int):
    orders.append({"id": order_id, "status": "created"})
    outbox.append({
        "event_type": "order.created",
        "aggregate_id": order_id,
        "published": False,
    })


def publish_pending_events():
    for event in outbox:
        if not event["published"]:
            print(f"publishing {event['event_type']} for {event['aggregate_id']}")
            event["published"] = True


create_order(101)
print(orders)
print(outbox)
publish_pending_events()
print(outbox)
```

Output:

```text
[{'id': 101, 'status': 'created'}]
[{'event_type': 'order.created', 'aggregate_id': 101, 'published': False}]
publishing order.created for 101
[{'event_type': 'order.created', 'aggregate_id': 101, 'published': True}]
```

To oczywiście model uproszczony, ale świetnie buduje intuicję.

## Outbox nie eliminuje dubli automatycznie

To ważne.

Jeśli publisher padnie po opublikowaniu eventu, ale przed oznaczeniem go jako wysłany, event może zostać opublikowany ponownie.

Czyli outbox rozwiązuje głównie problem spójności między bazą a publikacją, ale nadal trzeba myśleć o:

- idempotencji konsumenta,
- deduplikacji,
- retry publishera.

## Before/after

### Naiwny model

- zapis do bazy i publish są luźno powiązane,
- awaria pomiędzy nimi tworzy niespójność,
- zdarzenia mogą ginąć.

### Model z outboxem

- stan biznesowy i zamiar publikacji są zapisane razem,
- publikacja może wydarzyć się trochę później,
- system lepiej znosi awarie pośrednie.

## Kiedy outbox pattern ma sens

Outbox pattern ma sens szczególnie wtedy, gdy:

- publikujesz zdarzenia po zmianie stanu w bazie,
- architektura opiera się o eventy albo messaging,
- nie możesz sobie pozwolić na utratę ważnych eventów,
- chcesz zwiększyć niezawodność integracji między stanem lokalnym a brokerem.

## Kiedy outbox może być zbyt ciężki

Może być zbyt ciężki, gdy:

- system jest bardzo mały,
- publikacja eventów nie jest jeszcze krytyczna,
- nie masz jeszcze potrzeby pełnej niezawodności na tym poziomie,
- prostsze rozwiązanie naprawdę wystarcza.

Ale w systemach dojrzalszych to bardzo często jest wzorzec wart wdrożenia.

## Najczęstsze pułapki

### 1. Mylenie outboxa z pełną gwarancją exactly-once

Outbox nie daje magicznie "dokładnie raz".

Nadal trzeba myśleć o dubelkach i retry.

### 2. Brak procesu publikującego zaległe eventy

Sama tabela outbox nie wystarczy. Ktoś musi ją czytać i publikować.

### 3. Brak monitoringu zalegających rekordów

Jeśli outbox się zapełnia, a publisher nie nadąża, system zaczyna mieć coraz większy lag zdarzeń.

### 4. Trzymanie zbyt mało informacji w payloadzie eventu

Consumer musi dostać sensowny kontrakt danych.

### 5. Brak czyszczenia lub archiwizacji starych rekordów

Outbox też wymaga utrzymania operacyjnego.

## Mini case study: płatność i event

Masz flow:

- zamówienie zostaje oznaczone jako opłacone,
- system powinien opublikować `order.paid`.

Bez outboxa możesz mieć sytuację:

- status w bazie zmienił się na `paid`,
- ale event nie wyszedł,
- system wysyłki nie uruchomi dalszych działań.

Z outboxem:

- event przynajmniej jest zapisany lokalnie,
- publisher może go wypchnąć później,
- system ma dużo większą szansę dojścia do poprawnego stanu końcowego.

## Co Pythonowiec powinien rozumieć

Dobrze, żebyś umiał:

- rozpoznać problem "baza i broker to dwa różne światy",
- zrozumieć, czemu zwykłe `save + publish` jest ryzykowne,
- wiedzieć, że outbox wiąże stan i zamiar publikacji w jednej transakcji,
- pamiętać, że nadal trzeba projektować idempotencję po stronie konsumentów,
- myśleć o monitoringu i opóźnieniu publikacji.

## Output myślowy

### Bez outboxa

- system może gubić ważne eventy przy awarii pośredniej,
- spójność między bazą i messagingiem jest krucha.

### Z outboxem

- publikacja może być opóźniona,
- ale zamiar publikacji nie znika tak łatwo,
- system lepiej znosi błędy między bazą i brokerem.

## Najważniejsze do zapamiętania

- Outbox pattern łączy zapis stanu biznesowego i zapis eventu w jednej transakcji.
- Rozwiązuje ważny problem spójności między bazą i publikacją wiadomości.
- Nie eliminuje automatycznie dubli ani potrzeby idempotencji.
- Wymaga osobnego procesu publikującego oraz monitoringu.
- To jeden z najważniejszych wzorców przy dojrzalszym messagingu i event-driven architekturze.

## Ćwiczenia

1. Wyjaśnij własnymi słowami, jaki problem rozwiązuje outbox pattern.
2. Opisz, czemu zwykłe `save + publish` jest ryzykowne.
3. Rozpisz flow tworzenia zamówienia z outboxem krok po kroku.
4. Podaj dwa powody, dla których outbox nie zwalnia z idempotencji.
5. Zaprojektuj prostą tabelę outbox dla systemu zamówień.
