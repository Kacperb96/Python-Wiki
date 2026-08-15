# HTTP i REST w Pythonie — podstawy

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest HTTP](#czym-jest-http)
3. [Request i response](#request-i-response)
4. [Metody HTTP](#metody-http)
5. [Status codes](#status-codes)
6. [Nagłówki](#nagłówki)
7. [JSON w API](#json-w-api)
8. [Czym jest REST](#czym-jest-rest)
9. [Endpointy i zasoby](#endpointy-i-zasoby)
10. [Idempotencja i semantyka metod](#idempotencja-i-semantyka-metod)
11. [Przykład requestu i odpowiedzi](#przykład-requestu-i-odpowiedzi)
12. [Typowe błędy początkujących](#typowe-błędy-początkujących)
13. [Praktyczna ściąga](#praktyczna-ściąga)
14. [Ćwiczenia](#ćwiczenia)
15. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

Jeśli chcesz budować nowoczesne aplikacje backendowe, musisz dobrze rozumieć HTTP i podstawy REST.

To fundament pracy z:

- API,
- frontendem,
- mikroserwisami,
- integracjami zewnętrznymi.

---

## Czym jest HTTP

HTTP to protokół komunikacji między klientem a serwerem.

Najprostszy model:

- klient wysyła żądanie,
- serwer odsyła odpowiedź.

Klientem może być:

- przeglądarka,
- frontend,
- skrypt Python,
- aplikacja mobilna,
- inna usługa backendowa.

---

## Request i response

### Request

Request zwykle zawiera:

- metodę,
- adres URL,
- nagłówki,
- opcjonalne body.

### Response

Response zwykle zawiera:

- status code,
- nagłówki,
- body z danymi.

To jest absolutna podstawa czytania i projektowania API.

---

## Metody HTTP

Najważniejsze:

- `GET` pobieranie danych,
- `POST` tworzenie zasobu,
- `PUT` pełna aktualizacja,
- `PATCH` częściowa aktualizacja,
- `DELETE` usuwanie.

Bardzo ważne:

metoda HTTP nie powinna być przypadkowa.

To część kontraktu API.

---

## Status codes

Najczęściej spotkasz:

- `200 OK`,
- `201 Created`,
- `204 No Content`,
- `400 Bad Request`,
- `401 Unauthorized`,
- `403 Forbidden`,
- `404 Not Found`,
- `422 Unprocessable Entity`,
- `500 Internal Server Error`.

Kod statusu mówi klientowi, jak zakończyło się żądanie.

---

## Nagłówki

Nagłówki przenoszą dodatkowe informacje.

Przykłady:

- `Content-Type`,
- `Authorization`,
- `Accept`.

Są bardzo ważne przy:

- autoryzacji,
- formacie danych,
- cachowaniu,
- negocjacji treści.

---

## JSON w API

Najczęściej dane w API są przesyłane jako JSON.

Przykład:

```json
{"id": 1, "name": "Anna"}
```

To praktyczny standard w wielu aplikacjach webowych.

---

## Czym jest REST

REST to styl projektowania API oparty na zasobach i przewidywalnych regułach HTTP.

W praktyce najczęściej oznacza:

- sensowne endpointy,
- poprawne metody HTTP,
- czytelne statusy,
- stateless communication,
- myślenie w kategoriach zasobów.

---

## Endpointy i zasoby

Przykłady:

- `GET /users`
- `GET /users/1`
- `POST /users`
- `PATCH /users/1`
- `DELETE /users/1`

Tu zasobem są użytkownicy.

To dużo bardziej przewidywalne niż np. chaotyczne ścieżki w stylu:

- `/getAllUsers`
- `/createUserNow`
- `/removeUserById`

---

## Idempotencja i semantyka metod

To ważne pojęcie.

Idempotentna operacja to taka, której wielokrotne wykonanie daje ten sam efekt końcowy.

W praktyce często:

- `GET` jest bezpieczny i nie powinien zmieniać stanu,
- `PUT` bywa idempotentny,
- `DELETE` też zwykle projektuje się jako idempotentny,
- `POST` zwykle nie jest idempotentny.

To ważne dla klientów, retry i sensownego modelu API.

---

## Przykład requestu i odpowiedzi

Request:

```http
POST /users HTTP/1.1
Host: api.example.com
Content-Type: application/json
Authorization: Bearer TOKEN

{"name": "Anna", "email": "anna@example.com"}
```

Przykładowa odpowiedź:

```http
HTTP/1.1 201 Created
Content-Type: application/json

{"id": 1, "name": "Anna", "email": "anna@example.com"}
```

Jak to czytać:

- klient tworzy nowy zasób,
- serwer zwraca `201 Created`,
- odpowiedź zawiera reprezentację nowo utworzonego użytkownika.

---

## Typowe błędy początkujących

- traktowanie metod HTTP jak rzeczy wymiennej,
- złe używanie status codes,
- projektowanie endpointów bardziej pod funkcje niż pod zasoby,
- brak konsekwencji w adresach i semantyce,
- brak rozróżnienia między błędem klienta a błędem serwera.

---

## Praktyczna ściąga

### Najczęstsze mapowanie

- `GET /users` -> lista,
- `GET /users/{id}` -> jeden zasób,
- `POST /users` -> utworzenie,
- `PATCH /users/{id}` -> częściowa zmiana,
- `DELETE /users/{id}` -> usunięcie.

### Najczęstsze statusy

- `200`,
- `201`,
- `204`,
- `400`,
- `401`,
- `403`,
- `404`,
- `422`,
- `500`.

---

## Ćwiczenia

1. Rozpisz REST endpointy dla `users`.
2. Rozpisz REST endpointy dla `orders`.
3. Dobierz metodę HTTP dla pobrania, utworzenia, aktualizacji i usunięcia.
4. Dopasuj status code do kilku scenariuszy.
5. Wyjaśnij różnicę między `PUT` i `PATCH`.
6. Wyjaśnij własnymi słowami, czemu `GET` nie powinien zmieniać danych.

---

## Najważniejsze do zapamiętania

- HTTP to kontrakt między klientem a serwerem.
- Metoda HTTP i status code mają znaczenie semantyczne.
- REST najczęściej projektuje API wokół zasobów.
- JSON to najczęstszy format danych w nowoczesnym API.
- Dobre API jest przewidywalne dla klienta, a nie tylko „działa”.
