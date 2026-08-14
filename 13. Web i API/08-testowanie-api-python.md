# Testowanie API w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co testować API](#po-co-testować-api)
3. [Co testować w API](#co-testować-w-api)
4. [Status code i body odpowiedzi](#status-code-i-body-odpowiedzi)
5. [Scenariusze pozytywne i negatywne](#scenariusze-pozytywne-i-negatywne)
6. [Walidacja danych wejściowych](#walidacja-danych-wejściowych)
7. [Autoryzacja i uprawnienia](#autoryzacja-i-uprawnienia)
8. [Warstwa HTTP vs logika biznesowa](#warstwa-http-vs-logika-biznesowa)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczne przykłady](#praktyczne-przykłady)
11. [Dobre praktyki](#dobre-praktyki)
12. [Podsumowanie](#podsumowanie)
13. [Mini ściąga](#mini-ściąga)
14. [Ćwiczenia](#ćwiczenia)
15. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Testy API są bardzo ważne, bo sprawdzają kontrakt między klientem a serwerem.

To nie tylko testowanie funkcji, ale też zachowania warstwy HTTP.

---

## Po co testować API

Bo API musi zachowywać się przewidywalnie dla:

- frontendu,
- innych usług,
- partnerów integracyjnych,
- testów automatycznych.

---

## Co testować w API

Najczęściej:

- status code,
- strukturę body,
- walidację wejścia,
- błędy,
- autoryzację,
- podstawowe scenariusze biznesowe.

---

## Status code i body odpowiedzi

To absolutne minimum.

Test powinien sprawdzać nie tylko, że endpoint "odpowiedział", ale że zrobił to poprawnie:

- `200`, `201`, `404`, `422` itd.,
- poprawny JSON,
- potrzebne pola.

---

## Scenariusze pozytywne i negatywne

Pozytywne:

- poprawne dane,
- poprawna autoryzacja,
- oczekiwany wynik.

Negatywne:

- brak danych,
- błędny format,
- brak uprawnień,
- brak zasobu.

---

## Walidacja danych wejściowych

API powinno odrzucać błędne dane na wejściu.

To bardzo ważny obszar testów.

---

## Autoryzacja i uprawnienia

Nie wystarczy sprawdzić "czy działa".

Trzeba też sprawdzić:

- kto może wykonać daną operację,
- co dzieje się bez tokenu,
- co dzieje się z błędnym tokenem.

---

## Warstwa HTTP vs logika biznesowa

Nie wszystko trzeba testować wyłącznie przez API.

Dobrze rozdzielać:

- testy endpointów,
- testy logiki biznesowej,
- testy integracyjne.

---

## Typowe błędy początkujących

- testowanie tylko "happy path",
- brak sprawdzania kodów błędów,
- ignorowanie walidacji wejścia,
- mieszanie zbyt wielu odpowiedzialności w jednym teście.

---

## Praktyczne przykłady

### Pozytywny test

Sprawdza, że:

- `POST /users` zwraca `201`,
- odpowiedź zawiera `id`,
- dane zostały zapisane.

### Negatywny test

Sprawdza, że:

- brak wymaganego pola kończy się błędem walidacji.

---

## Dobre praktyki

- testuj statusy i treść odpowiedzi,
- pokrywaj scenariusze negatywne,
- trzymaj testy czytelne i jednoznaczne,
- nie testuj wszystkiego wyłącznie przez HTTP, jeśli logikę można sensownie testować niżej.

---

## Podsumowanie

Testowanie API to ważna część profesjonalnego backendu.

Dobre testy API dają bezpieczeństwo refaktoryzacji i stabilność integracji.

---

## Mini ściąga

Najważniejsze:

- sprawdzaj status code,
- sprawdzaj body odpowiedzi,
- testuj błędne dane,
- testuj autoryzację,
- rozdzielaj poziomy testów.

---

## Ćwiczenia

1. Wypisz 3 rzeczy, które warto sprawdzać w teście endpointu.
2. Podaj przykład scenariusza negatywnego.
3. Wyjaśnij, po co testować brak autoryzacji.
4. Wyjaśnij różnicę między testem endpointu a testem logiki biznesowej.
5. Wskaż ryzyko testowania tylko "happy path".

---

## Przykładowe rozwiązania

### 1. 3 rzeczy

- status code,
- struktura JSON,
- poprawność danych w odpowiedzi.

### 2. Negatywny scenariusz

Wysłanie requestu bez wymaganego pola.

### 3. Brak autoryzacji

Żeby upewnić się, że nieuprawniony klient nie ma dostępu do chronionych zasobów.

### 4. Różnica

Test endpointu sprawdza warstwę HTTP, a test logiki biznesowej sprawdza reguły aplikacji bez koniecznego udziału HTTP.

### 5. Ryzyko

Można przeoczyć błędy w walidacji, obsłudze wyjątków i uprawnieniach.
