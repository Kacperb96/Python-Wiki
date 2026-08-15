# Case study: moduł orders w architekturze event-driven

## Po co ten plik

Ten plik spina cały folder 25 w jedną praktyczną całość.

Nie chodzi tu już o pojedyncze definicje, tylko o odpowiedź na pytanie:

- jak kolejki, retry, idempotencja, eventual consistency i outbox spotykają się w jednym realnym module?

## Mini system

Załóżmy backend sklepu internetowego z modułem `orders`.

Po utworzeniu zamówienia system powinien:

- zapisać zamówienie,
- wysłać mail potwierdzający,
- naliczyć punkty lojalnościowe,
- zaktualizować CRM,
- opublikować event dla innych usług,
- nie blokować użytkownika długim requestem.

## Najważniejsza decyzja architektoniczna

Nie wszystko powinno dziać się synchronicznie.

Trzeba świadomie rozdzielić:

- co jest krytyczne dla odpowiedzi użytkownika,
- co może wydarzyć się później,
- które skutki uboczne są odwracalne,
- które operacje są bardzo wrażliwe na duble.

## Prosty podział odpowiedzialności

### Synchronicznie w requestcie

- walidacja wejścia,
- zapis zamówienia,
- zwrot odpowiedzi do klienta,
- zapis rekordu do outboxa.

### Asynchronicznie później

- mail,
- CRM,
- analityka,
- notyfikacje poboczne,
- część zadań raportowych.

To bardzo częsty rozsądny model.

## Flow krok po kroku

### Krok 1: klient składa zamówienie

```http
POST /orders
```

Backend robi:

1. waliduje payload,
2. zapisuje `orders`,
3. zapisuje rekord `order.created` do outboxa,
4. commit,
5. zwraca odpowiedź.

### Przykładowa odpowiedź

```json
{
  "order_id": 101,
  "status": "created"
}
```

Najważniejsze:

- użytkownik nie czeka na mail, CRM i inne poboczne efekty.

## Krok 2: publisher czyta outbox

Osobny proces bierze rekordy z outboxa i publikuje event, np.:

```text
order.created
```

Dalej event może trafić do:

- systemu mailowego,
- systemu lojalnościowego,
- CRM,
- analityki.

## Krok 3: wiele consumerów robi swoje

Każdy consumer odpowiada za swój fragment pracy.

### Consumer A

- wysyła mail.

### Consumer B

- nalicza punkty.

### Consumer C

- aktualizuje CRM.

To bardzo ważne, bo każdy z tych skutków może mieć inne ryzyko i inne zasady retry.

## Gdzie pojawia się eventual consistency

W tym modelu przez chwilę możesz mieć taki stan:

- zamówienie już istnieje,
- mail jeszcze nie wyszedł,
- CRM jeszcze nie wie,
- punkty jeszcze nie są naliczone.

To nie musi być błąd.

To może być normalny stan przejściowy dobrze zaprojektowanego systemu.

## Gdzie grożą duble

To kluczowe pytanie.

Duble mogą pojawić się w miejscach takich jak:

- publisher opublikuje event drugi raz,
- consumer dostanie tę samą wiadomość ponownie,
- worker zrobi retry po timeoutcie,
- proces padnie po wykonaniu skutku ubocznego, ale przed potwierdzeniem.

## Operacje mniej groźne przy dubelkach

### Wysyłka maila

Dubel jest nieprzyjemny, ale zwykle mniej krytyczny niż błąd finansowy.

### Aktualizacja read modelu lub cache

Często bywa względnie łatwa do zaprojektowania idempotentnie.

## Operacje bardziej groźne przy dubelkach

### Naliczanie punktów

Jeśli event wykona się dwa razy, klient dostaje za dużo punktów.

### Obciążenie płatności

Tu brak idempotencji bywa bardzo niebezpieczny.

## Idempotencja w tym module

### Mail

Możesz akceptować małe ryzyko dubla albo dodać prostą ochronę.

### Punkty lojalnościowe

Lepiej użyć `operation_id` albo `event_id` i zapisywać, że dane naliczenie już zostało wykonane.

### CRM

Często trzeba zakładać, że integracja może dostać ten sam komunikat dwa razy.

## Minimalna symulacja myślowa

```python
outbox = []
processed_events = set()


def create_order(order_id: int):
    outbox.append({"event_id": f"evt-{order_id}", "type": "order.created", "order_id": order_id})


def process_loyalty_event(event: dict):
    event_id = event["event_id"]
    if event_id in processed_events:
        return "already processed"

    processed_events.add(event_id)
    return f"points added for order {event['order_id']}"


create_order(101)
event = outbox[0]
print(process_loyalty_event(event))
print(process_loyalty_event(event))
```

Output:

```text
points added for order 101
already processed
```

To dobrze pokazuje sens idempotencji konsumera.

## Retry w tym module

Retry ma sens tam, gdzie błąd jest przejściowy.

### Dobry kandydat

- chwilowy timeout CRM,
- chwilowy problem z providerem maili,
- chwilowe niedostępne API zewnętrzne.

### Zły kandydat na bezmyślne retry

- zły payload,
- nieistniejące zamówienie,
- logika, która zawsze kończy się błędem biznesowym.

## Before/after: słabszy i dojrzalszy flow

### Słabszy flow

- zapis do bazy,
- natychmiastowa wysyłka maila,
- natychmiastowy CRM,
- natychmiastowe punkty,
- wszystko w jednym requestcie.

Problemy:

- długi request,
- duża kruchość,
- jedna awaria psuje wszystko,
- trudniejsza skalowalność.

### Dojrzalszy flow

- zapis do bazy,
- zapis do outboxa,
- odpowiedź dla użytkownika,
- późniejsza publikacja eventu,
- niezależni consumerzy,
- retry i idempotencja tam, gdzie trzeba.

To dużo dojrzalszy model dla większego systemu.

## Większy case study: mail się spóźnia, ale zamówienie istnieje

Objaw:

- użytkownik widzi zamówienie,
- ale nie dostał jeszcze maila.

Czy to bug?

Nie zawsze.

Najpierw trzeba sprawdzić:

- czy event jest w outboxie,
- czy został opublikowany,
- czy consumer mailowy ma lag,
- czy provider maili ma problem.

To bardzo typowy przykład eventual consistency w praktyce.

## Większy case study: punkty naliczone dwa razy

Objaw:

- klient dostał 200 punktów zamiast 100.

Pierwsze hipotezy:

- consumer nie jest idempotentny,
- event został dostarczony więcej niż raz,
- retry zadziałało po częściowym sukcesie,
- system nie zapisuje `processed_event_id`.

To bardzo typowy błąd w systemach event-driven.

## Jak dobrać poziomy testów do tego modułu

### Unit

Testuj:

- logikę idempotencji,
- decyzję retry vs no retry,
- budowanie payloadu eventu,
- walidację przejść stanu.

### Integration

Testuj:

- zapis `orders` + outbox,
- publikację zaległych eventów,
- poprawne przetworzenie eventu przez consumer,
- brak podwójnego skutku dla tego samego `event_id`.

### E2E

Testuj:

- użytkownik składa zamówienie i finalnie dostaje mail,
- punkty są naliczane raz,
- awaria jednego consumer nie blokuje głównego flow zamówienia.

## Co ten case study pokazuje

Najważniejsza lekcja:

- messaging to nie jest tylko "wrzuć task do kolejki",
- to cały model pracy ze stanem, opóźnieniem, dubelkami i niezawodnością.

I właśnie dlatego retry, idempotencja, eventual consistency i outbox muszą być rozumiane razem, a nie osobno.

## Najważniejsze do zapamiętania

- W dojrzałym module event-driven nie wszystko dzieje się w requestcie.
- Zapis stanu i zamiar publikacji eventu warto spinać outboxem.
- Consumerzy muszą być projektowani pod możliwość dubli.
- Eventual consistency oznacza, że część skutków pojawia się później.
- Najgroźniejsze skutki dubli pojawiają się tam, gdzie system zmienia stan biznesowy albo pieniądze.

## Ćwiczenia

1. Rozpisz własną wersję flow `create_order` z eventami i workerami.
2. Wskaż, które operacje w tym module są najbardziej wrażliwe na duble.
3. Zaprojektuj prosty mechanizm idempotencji dla naliczania punktów.
4. Opisz, które elementy flow zostawiłbyś synchronicznie, a które asynchronicznie.
5. Wypisz trzy metryki, które chciałbyś widzieć dla tego modułu.
