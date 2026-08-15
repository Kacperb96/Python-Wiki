# Testy i debugowanie systemu messagingowego python

## Po co ten plik

Teoria o brokerach, retry i eventach jest potrzebna, ale prawdziwe zrozumienie przychodzi dopiero wtedy, gdy widzisz:

- co testować,
- jak wygląda awaria,
- skąd biorą się duble,
- czemu kolejka ma lag,
- jak odróżnić stan przejściowy od realnego błędu.

Ten plik spina folder 25 od strony jakości i utrzymania.

## Co testować unitowo

Unit testy powinny sprawdzać małe, ważne reguły.

Przykłady:

- czy decyzja retry/no retry działa poprawnie,
- czy funkcja idempotencji rozpoznaje dubel,
- czy payload eventu ma poprawne pola,
- czy consumer odrzuca brakujące dane,
- czy klucz deduplikacji działa tak, jak oczekujesz.

### Przykład

```python
processed = {"evt-1"}


def should_process(event_id: str) -> bool:
    return event_id not in processed


print(should_process("evt-1"))
print(should_process("evt-2"))
```

Output:

```text
False
True
```

## Co testować integracyjnie

Integracja jest tu bardzo ważna, bo problem zwykle leży między komponentami.

Przykłady:

- zapis rekordu + zapis outboxa,
- publisher czyta outbox i publikuje event,
- consumer odbiera event i wykonuje skutek uboczny,
- retry nie robi podwójnej szkody,
- worker po błędzie poprawnie wraca do kolejki lub ścieżki błędów.

## Co testować E2E

E2E zostaw dla kilku najważniejszych przepływów.

Dobre przykłady:

- użytkownik składa zamówienie i finalnie dostaje mail,
- punkty lojalnościowe naliczają się dokładnie raz,
- awaria integracji CRM nie blokuje utworzenia zamówienia,
- event z outboxa finalnie trafia do konsumenta.

## Co jest trudne w testowaniu messagingu

Najtrudniejsze są rzeczy takie jak:

- opóźnienie,
- kolejność zdarzeń,
- duble,
- częściowe sukcesy,
- retry po awarii pośredniej.

To oznacza, że nie wystarczy tylko przetestować "happy path".

## Mini case study: znikający event

Objaw:

- zamówienie jest w bazie,
- ale CRM nigdy się o nim nie dowiedział.

### Pierwsze hipotezy

- event nie trafił do outboxa,
- outbox ma rekord, ale publisher go nie wypchnął,
- broker przyjął event, ale consumer go nie przetworzył,
- consumer padł i nie zrobił retry,
- monitorowanie nie wykryło zaległości.

### Co sprawdzić

1. czy rekord jest w `orders`,
2. czy jest odpowiadający rekord w outboxie,
3. czy rekord outboxa jest oznaczony jako opublikowany,
4. czy broker widział wiadomość,
5. czy consumer dostał i potwierdził komunikat,
6. czy były retry albo błędy po drodze.

To bardzo klasyczna ścieżka debugowania.

## Mini case study: dubel maila

Objaw:

- użytkownik dostaje dwa identyczne maile.

### Możliwe przyczyny

- worker wykonał task dwa razy,
- broker dostarczył wiadomość ponownie,
- publisher opublikował event drugi raz,
- brak deduplikacji po stronie consumer.

### Najważniejsza lekcja

To nie musi oznaczać, że broker jest zepsuty.

To bardzo często oznacza, że system nie był przygotowany na normalny scenariusz wielokrotnego dostarczenia.

## Mini case study: lag kolejki

Objaw:

- zamówienia są tworzone poprawnie,
- ale maile i CRM aktualizują się dopiero po kilkunastu minutach.

### Co to może znaczyć

- consumerzy nie nadążają,
- jest za mało workerów,
- jedno zadanie jest za ciężkie,
- retry zapycha kolejkę,
- zewnętrzna integracja działa wolno,
- publisher lub consumer ma problemy z wydajnością.

### Co warto zmierzyć

- liczbę oczekujących wiadomości,
- wiek najstarszej wiadomości,
- czas przetwarzania jednego zadania,
- liczbę retry,
- liczbę błędów na consumerze,
- opóźnienie między `created_at` eventu a jego przetworzeniem.

## Lag: bardzo ważna intuicja

W systemie messagingowym nie wystarczy wiedzieć, że wiadomość "kiedyś zostanie obsłużona".

Trzeba wiedzieć także:

- jak długo czeka,
- czy consumer nadąża,
- czy backlog rośnie,
- czy opóźnienie jest akceptowalne biznesowo.

## Flaky testy w messagingu

To bardzo częsty problem.

### Przykład 1: test zależny od czasu

Test zakłada, że worker wykona zadanie w dokładnie określonym krótkim czasie.

Raz przechodzi, raz nie.

Lepsze podejście:

- testować semantykę, nie wyścig z zegarem,
- kontrolować czas lub symulować krok procesu,
- nie robić testów "czekaj 2 sekundy i zobacz" jako głównego modelu jakości.

### Przykład 2: współdzielony stan kolejki

Jeden test zostawia wiadomość w kolejce, a drugi czyta ją przypadkiem jako własną.

Lepsze podejście:

- izolować środowisko testowe,
- czyścić kolejki i stan deduplikacji,
- używać jawnych fixture i setupów.

## Contract drift w eventach

To bardzo ważny temat.

Załóżmy, że event `order.created` miał payload:

```json
{
  "order_id": 101,
  "user_id": 42,
  "total_amount": 199.99
}
```

A potem publisher zaczyna wysyłać:

```json
{
  "id": 101,
  "customer_id": 42,
  "amount": 199.99
}
```

Jeśli consumer oczekuje starego kontraktu:

- zacznie się sypać,
- albo co gorsza: będzie działał źle po cichu.

Tu testy kontraktu eventów są bardzo cenne.

## Co logować w produkcji

Dobrze logować:

- `event_id`,
- typ eventu,
- moment publikacji,
- moment odbioru,
- liczbę retry,
- błąd i typ błędu,
- decyzję o `ack` albo odrzuceniu,
- powód odłożenia do ścieżki błędów.

Nie logować bezmyślnie wrażliwych payloadów, jeśli zawierają sekrety lub dane prywatne.

## Przydatne metryki

Najbardziej praktyczne metryki to często:

- liczba wiadomości oczekujących,
- wiek najstarszej wiadomości,
- liczba wiadomości przetwarzanych na sekundę,
- liczba błędów per consumer,
- liczba retry,
- czas od publikacji do przetworzenia,
- liczba wiadomości w ścieżce błędów.

## Szybka checklista debugowania

Gdy coś nie działa w systemie messagingowym, sprawdź po kolei:

1. czy zdarzenie lub task w ogóle zostały utworzone,
2. czy zostały zapisane w outboxie lub opublikowane,
3. czy broker lub kolejka mają backlog,
4. czy consumer działa i potwierdza wiadomości,
5. czy retry nie zapętla problemu,
6. czy consumer jest idempotentny,
7. czy payload eventu nadal zgadza się z oczekiwaniem odbiorcy,
8. czy opóźnienie jest stanem przejściowym czy realną awarią.

## Co ten plik pokazuje

Najważniejsza lekcja:

- messaging to nie tylko publikacja wiadomości,
- to także testowanie kontraktów, deduplikacji, retry, opóźnień i odporności na częściowe awarie.

## Najważniejsze do zapamiętania

- System messagingowy trzeba testować warstwowo: unit, integracja, kilka E2E.
- Lagi i duble to normalne klasy problemów, nie egzotyczne wyjątki.
- Event może zniknąć logicznie na wielu etapach drogi i trzeba umieć zawężać miejsce awarii.
- Idempotencja, kontrakty eventów i monitoring backlogu są krytyczne.
- Dobre logi i metryki robią gigantyczną różnicę w debugowaniu systemu rozproszonego.

## Ćwiczenia

1. Rozpisz checklistę debugowania problemu "event nie dotarł do consumer".
2. Podaj trzy źródła dubli wiadomości.
3. Zaprojektuj dwa testy integracyjne dla outbox pattern.
4. Opisz flaky test związany z workerem i pokaż, jak byś go ustabilizował.
5. Wypisz pięć metryk, które monitorowałbyś dla kolejki maili.
