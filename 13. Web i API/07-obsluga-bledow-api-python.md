# Obsługa błędów API w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co dobrze obsługiwać błędy w API](#po-co-dobrze-obsługiwać-błędy-w-api)
3. [Błąd klienta vs błąd serwera](#błąd-klienta-vs-błąd-serwera)
4. [Status codes przy błędach](#status-codes-przy-błędach)
5. [Czytelny format odpowiedzi błędu](#czytelny-format-odpowiedzi-błędu)
6. [Walidacja i błędy wejścia](#walidacja-i-błędy-wejścia)
7. [Logowanie błędów](#logowanie-błędów)
8. [Błędy domenowe](#błędy-domenowe)
9. [Przykład odpowiedzi błędu](#przykład-odpowiedzi-błędu)
10. [Typowe błędy początkujących](#typowe-błędy-początkujących)
11. [Praktyczna ściąga](#praktyczna-ściąga)
12. [Ćwiczenia](#ćwiczenia)
13. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

Dobre API nie tylko zwraca poprawne dane, ale też sensownie komunikuje błędy.

To bardzo ważne dla:

- frontendu,
- innych usług,
- debugowania,
- utrzymania systemu.

---

## Po co dobrze obsługiwać błędy w API

Bo klient API musi wiedzieć:

- co poszło nie tak,
- czy to jego błąd,
- czy może spróbować ponownie,
- czy problem leży po stronie serwera.

API z chaotycznymi błędami jest trudniejsze do integracji i dużo trudniejsze do utrzymania.

---

## Błąd klienta vs błąd serwera

To podstawowe rozróżnienie.

### Błąd klienta

- złe dane,
- brak autoryzacji,
- brak zasobu,
- złamane reguły wejścia.

### Błąd serwera

- nieoczekiwana awaria,
- błąd integracji,
- błąd infrastruktury,
- wewnętrzny wyjątek aplikacji.

To rozróżnienie powinno być widoczne i w statusach, i w sposobie logowania.

---

## Status codes przy błędach

Najczęściej:

- `400 Bad Request`,
- `401 Unauthorized`,
- `403 Forbidden`,
- `404 Not Found`,
- `409 Conflict`,
- `422 Unprocessable Entity`,
- `500 Internal Server Error`.

Nie każdy błąd to `500`.

Właśnie to jest jedna z najczęstszych słabości źle zaprojektowanego backendu.

---

## Czytelny format odpowiedzi błędu

Dobrze, gdy błędy mają przewidywalny kształt.

Na przykład:

- kod błędu,
- komunikat,
- szczegóły,
- ewentualnie identyfikator zdarzenia.

To pomaga klientom API pisać czytelniejszą obsługę błędów po swojej stronie.

---

## Walidacja i błędy wejścia

Błędy walidacji powinny być czytelne i pomocne.

Klient powinien dostać informację:

- które pole jest błędne,
- co było oczekiwane,
- czy problem dotyczy formatu, czy brakującej wartości.

To ważniejsze niż ogólny komunikat typu "bad request" bez szczegółów.

---

## Logowanie błędów

Nie każdy błąd trzeba pokazywać klientowi w pełnym szczególe.

Ale serwer powinien:

- logować problem,
- zachować kontekst,
- nie ujawniać zbędnych sekretów w odpowiedzi HTTP.

To ważna granica między diagnostyką wewnętrzną a kontraktem API.

---

## Błędy domenowe

Niektóre błędy nie są techniczne, tylko biznesowe.

Na przykład:

- brak dostępnego limitu,
- próba wykonania niedozwolonej operacji,
- konflikt stanu zasobu,
- zakup produktu niedostępnego w magazynie.

To nie jest awaria serwera.

To przewidywalna sytuacja biznesowa, która też powinna mieć sensowną reprezentację HTTP.

---

## Przykład odpowiedzi błędu

Przykład czytelnej odpowiedzi:

```json
{
  "error": {
    "code": "USER_NOT_FOUND",
    "message": "User with given id does not exist"
  }
}
```

Taka struktura jest dużo lepsza niż przypadkowe komunikaty zwracane raz tak, raz inaczej.

---

## Typowe błędy początkujących

- wszędzie `500`,
- brak spójnego formatu błędów,
- zbyt lakoniczne albo zbyt techniczne komunikaty,
- ujawnianie zbyt wielu szczegółów wewnętrznych klientowi,
- brak rozróżnienia błędu walidacyjnego od domenowego.

---

## Praktyczna ściąga

### Najważniejsze pytanie

Czy problem jest po stronie klienta, czy po stronie serwera?

### Częste statusy

- `400`, `401`, `403`, `404`, `409`, `422`, `500`.

### Dobra odpowiedź błędu powinna być

- spójna,
- czytelna,
- pomocna,
- bez ujawniania zbyt wielu sekretów.

---

## Ćwiczenia

1. Rozpisz kilka scenariuszy błędów klienta i serwera.
2. Dopasuj statusy HTTP do tych scenariuszy.
3. Zaprojektuj spójny format odpowiedzi błędu.
4. Opisz przykład błędu domenowego.
5. Wyjaśnij własnymi słowami, czemu nie każdy błąd powinien kończyć się `500`.
6. Zastanów się, jakich szczegółów nie warto pokazywać klientowi.

---

## Najważniejsze do zapamiętania

- Dobre API powinno sensownie komunikować błędy.
- Trzeba rozróżniać błąd klienta, domeny i serwera.
- Status code i format odpowiedzi błędu powinny być spójne.
- Serwer powinien logować więcej niż pokazuje klientowi.
- Chaos w błędach bardzo utrudnia integracje i utrzymanie systemu.
