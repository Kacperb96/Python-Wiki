# Contract tests w Pythonie

## O co chodzi

Contract tests sprawdzają, czy dwie strony integracji nadal zgadzają się co do kontraktu.

Kontrakt może dotyczyć np.:

- kształtu requestu,
- kształtu odpowiedzi,
- nazw pól,
- typów danych,
- znaczenia kodów błędów,
- zachowania klient-serwer.

To bardzo ważne przy systemach, które komunikują się ze sobą przez API albo inne jawne interfejsy.

## Najprostsza intuicja

Unit test pyta:

- czy moja logika działa?

Integracja pyta:

- czy kilka elementów razem działa?

Contract test pyta:

- czy obie strony nadal rozumieją interfejs tak samo?

To subtelna, ale bardzo ważna różnica.

## Po co contract tests

Bo nawet jeśli Twój kod lokalnie działa, to możesz mieć problem, jeśli:

- inny system zmienił format odpowiedzi,
- pole zostało przemianowane,
- opcjonalne pole przestało być opcjonalne,
- klient zakłada coś, czego serwer już nie gwarantuje.

W takich przypadkach często nie chodzi o błąd algorytmu, tylko o pęknięcie kontraktu między systemami.

## Przykład intuicyjny

Masz klienta, który oczekuje odpowiedzi:

```json
{
  "user_id": 1,
  "name": "Anna"
}
```

A serwer po zmianie zaczyna zwracać:

```json
{
  "id": 1,
  "full_name": "Anna"
}
```

Oba systemy osobno mogą działać poprawnie. Ale ich kontrakt już się rozjechał.

## Kiedy contract tests mają sens

Szczególnie gdy:

- masz integrację między usługami,
- rozwijasz klienta API i serwer niezależnie,
- ważny jest stabilny kształt danych,
- chcesz szybko wykryć pęknięcie interfejsu.

## Contract test vs zwykły test integracyjny

### Test integracyjny

Sprawdza współpracę w obrębie jednego systemu lub bezpośrednio połączonych elementów.

### Contract test

Chroni jawny kontrakt na granicy dwóch systemów lub komponentów.

Czyli bardziej chodzi o zgodność interfejsu niż o pełen przepływ logiki wewnętrznej.

## Co może być kontraktem

Nie tylko JSON odpowiedzi.

Kontraktem może być też:

- kolejka wiadomości,
- payload eventu,
- schema danych,
- wynik endpointu,
- znaczenie statusów i błędów.

## Realistyczny contract drift 1: zmiana nazwy pola

Klient oczekuje:

```json
{
  "payment_status": "paid"
}
```

Provider zaczyna zwracać:

```json
{
  "status": "paid"
}
```

Skutek:

- klient lokalnie może mieć zielone unit testy,
- ale integracja zacznie się sypać.

To klasyczny contract drift.

## Realistyczny contract drift 2: opcjonalne pole przestało być opcjonalne

Stary kontrakt:

```json
{
  "user_id": 1,
  "email": null
}
```

Nowy kontrakt po zmianie serwera:

- `email` jest zawsze stringiem,
- albo pole w ogóle znika,
- albo klient zaczyna zakładać, że zawsze istnieje.

Takie zmiany potrafią być bardzo zdradliwe, bo nie zawsze wywalają się od razu w najbardziej oczywistym miejscu.

## Realistyczny contract drift 3: zmiana znaczenia pola

Jeszcze trudniejszy przypadek:

- pole nadal nazywa się tak samo,
- typ nadal wygląda podobnie,
- ale zmienia się jego semantyka.

Przykład:

- dawniej `amount` oznaczało kwotę brutto,
- teraz oznacza kwotę netto.

To jeszcze bardziej pokazuje, że kontrakt to nie tylko nazwy pól, ale też ich znaczenie.

## Mini case study

Masz klienta płatności, który oczekuje pola:

- `payment_status`

Provider albo wewnętrzny serwis zmienia je na:

- `status`

Jeśli nie masz contract testu, problem może wyjść dopiero później, np. na produkcji.

Jeśli masz contract test, rozjazd kontraktu jest widoczny od razu.

## Kiedy nie przesadzać

Nie każda lokalna funkcja potrzebuje "contract testów".

Ten poziom ma sens wtedy, gdy naprawdę istnieje jawna granica między komponentami albo systemami.

## Typowe błędy początkujących

- mylenie contract tests z każdym testem API,
- brak rozróżnienia, co jest wewnętrznym detalem, a co kontraktem,
- zbyt ogólne testy, które nie chronią ważnych pól i znaczeń,
- zakładanie, że integracja "na pewno się nie zmieni".

## Szybka ściąga

- contract test chroni zgodność interfejsu między dwiema stronami,
- jest bardzo ważny przy API i integracjach,
- wykrywa pęknięcie kontraktu, nawet gdy systemy osobno wydają się działać,
- nie zastępuje unitów, integracji ani E2E.

## Ćwiczenia

1. Podaj przykład kontraktu w API.
2. Opisz przypadek, gdzie pole JSON zostało zmienione i contract test mógłby to wykryć.
3. Wyjaśnij różnicę między integracją a contract testem.
4. Zaprojektuj prosty contract test dla odpowiedzi endpointu.
5. Wskaż 3 sytuacje, gdzie contract test daje realną wartość.

## Najważniejsze do zapamiętania

- Contract tests chronią granice między systemami lub komponentami.
- Najważniejsza jest zgodność kształtu i znaczenia interfejsu.
- To bardzo praktyczne przy API i integracjach.
- Rozjazd kontraktu potrafi zepsuć system mimo przechodzących testów lokalnych.
- Dobrze zaprojektowany contract test daje szybki sygnał o niebezpiecznej zmianie interfejsu.
