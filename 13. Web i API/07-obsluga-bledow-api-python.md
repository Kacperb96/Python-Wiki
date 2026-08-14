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
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczne przykłady](#praktyczne-przykłady)
11. [Dobre praktyki](#dobre-praktyki)
12. [Podsumowanie](#podsumowanie)
13. [Mini ściąga](#mini-ściąga)
14. [Ćwiczenia](#ćwiczenia)
15. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

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

---

## Błąd klienta vs błąd serwera

To podstawowe rozróżnienie.

Błąd klienta:

- złe dane,
- brak autoryzacji,
- brak zasobu.

Błąd serwera:

- nieoczekiwana awaria,
- błąd integracji,
- błąd infrastruktury.

---

## Status codes przy błędach

Najczęściej:

- `400 Bad Request`
- `401 Unauthorized`
- `403 Forbidden`
- `404 Not Found`
- `409 Conflict`
- `422 Unprocessable Entity`
- `500 Internal Server Error`

---

## Czytelny format odpowiedzi błędu

Dobrze, gdy błędy mają przewidywalny kształt.

Na przykład:

- kod błędu,
- komunikat,
- szczegóły,
- ewentualnie identyfikator zdarzenia.

---

## Walidacja i błędy wejścia

Błędy walidacji powinny być czytelne i pomocne.

Klient powinien dostać informację:

- które pole jest błędne,
- co było oczekiwane.

---

## Logowanie błędów

Nie każdy błąd trzeba pokazywać klientowi w pełnym szczególe.

Ale serwer powinien:

- logować problem,
- zachować kontekst,
- nie ujawniać zbędnych sekretów w odpowiedzi.

---

## Błędy domenowe

Niektóre błędy nie są techniczne, tylko biznesowe.

Na przykład:

- brak dostępnego limitu,
- próba wykonania niedozwolonej operacji,
- konflikt stanu zasobu.

One też powinny mieć sensowną reprezentację HTTP.

---

## Typowe błędy początkujących

- wszędzie `500`,
- brak spójnego formatu błędów,
- zbyt lakoniczne albo zbyt techniczne komunikaty,
- ujawnianie zbyt wielu szczegółów wewnętrznych klientowi.

---

## Praktyczne przykłady

### Błąd klienta

Request bez wymaganego pola powinien zwrócić błąd walidacji, a nie `500`.

### Błąd domenowy

Próba kupna produktu niedostępnego w magazynie nie jest awarią serwera, tylko przewidywalnym błędem biznesowym.

---

## Dobre praktyki

- rozróżniaj błędy klienta i serwera,
- utrzymuj spójny format odpowiedzi błędów,
- loguj szczegóły po stronie serwera,
- klientowi pokazuj tyle, ile trzeba, ale nie za dużo.

---

## Podsumowanie

Obsługa błędów API to ważna część kontraktu aplikacji.

Dobrze zaprojektowane błędy bardzo poprawiają jakość integracji i utrzymania systemu.

---

## Mini ściąga

Najważniejsze:

- `4xx` zwykle oznaczają problem po stronie klienta,
- `5xx` zwykle oznaczają problem po stronie serwera,
- błędy powinny być spójne i czytelne,
- nie ujawniaj niepotrzebnych szczegółów wewnętrznych.

---

## Ćwiczenia

1. Wyjaśnij różnicę między `4xx` i `5xx`.
2. Podaj przykład błędu walidacji.
3. Podaj przykład błędu domenowego.
4. Wyjaśnij, po co logować błędy po stronie serwera.
5. Wyjaśnij, czemu nie każdy problem powinien kończyć się `500`.

---

## Przykładowe rozwiązania

### 1. `4xx` vs `5xx`

`4xx` zwykle oznaczają błąd klienta, a `5xx` problem po stronie serwera.

### 2. Walidacja

Brak wymaganego pola `email` w request body.

### 3. Domena

Próba złożenia zamówienia na niedostępny produkt.

### 4. Po co logować

Żeby móc diagnozować problemy bez ujawniania całych szczegółów klientowi.

### 5. Czemu nie `500`

Bo wiele błędów jest przewidywalnych i powinno mieć bardziej precyzyjny status.
