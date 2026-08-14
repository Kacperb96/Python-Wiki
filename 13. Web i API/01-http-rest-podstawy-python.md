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
11. [Typowe błędy początkujących](#typowe-błędy-początkujących)
12. [Praktyczne przykłady](#praktyczne-przykłady)
13. [Dobre praktyki](#dobre-praktyki)
14. [Podsumowanie](#podsumowanie)
15. [Mini ściąga](#mini-ściąga)
16. [Ćwiczenia](#ćwiczenia)
17. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

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
- aplikacja mobilna.

---

## Request i response

Request zwykle zawiera:

- metodę,
- adres URL,
- nagłówki,
- opcjonalne body.

Response zwykle zawiera:

- status code,
- nagłówki,
- body z danymi.

---

## Metody HTTP

Najważniejsze:

- `GET` pobieranie danych,
- `POST` tworzenie zasobu,
- `PUT` pełna aktualizacja,
- `PATCH` częściowa aktualizacja,
- `DELETE` usuwanie.

To absolutna podstawa pracy z API.

---

## Status codes

Najczęściej spotkasz:

- `200 OK`
- `201 Created`
- `204 No Content`
- `400 Bad Request`
- `401 Unauthorized`
- `403 Forbidden`
- `404 Not Found`
- `500 Internal Server Error`

Kod statusu mówi klientowi, jak zakończyło się żądanie.

---

## Nagłówki

Nagłówki przenoszą dodatkowe informacje.

Przykłady:

- `Content-Type`
- `Authorization`
- `Accept`

To bardzo ważne przy autoryzacji i formacie danych.

---

## JSON w API

Najczęściej dane w API są przesyłane jako JSON.

Przykład:

```json
{"id": 1, "name": "Anna"}
```

To dziś praktyczny standard w wielu aplikacjach webowych.

---

## Czym jest REST

REST to styl projektowania API oparty na zasobach i przewidywalnych regułach HTTP.

W praktyce najczęściej oznacza:

- sensowne endpointy,
- poprawne metody HTTP,
- czytelne statusy,
- stateless communication.

---

## Endpointy i zasoby

Przykłady:

- `GET /users`
- `GET /users/1`
- `POST /users`
- `DELETE /users/1`

Tu zasobem są użytkownicy.

---

## Idempotencja i semantyka metod

To ważne pojęcie.

W uproszczeniu:

- wielokrotne `GET` nie powinno zmieniać stanu,
- `DELETE` zwykle powinno być idempotentne,
- `POST` zwykle nie jest idempotentny.

To wpływa na poprawny projekt API.

---

## Typowe błędy początkujących

- używanie `POST` do wszystkiego,
- brak rozróżnienia `PUT` i `PATCH`,
- ignorowanie kodów statusu,
- słabe nazewnictwo endpointów,
- mieszanie akcji i zasobów w chaotyczny sposób.

---

## Praktyczne przykłady

### Pobranie listy użytkowników

```http
GET /users
```

### Utworzenie użytkownika

```http
POST /users
Content-Type: application/json

{"name": "Anna"}
```

### Odpowiedź

```http
201 Created
Content-Type: application/json

{"id": 1, "name": "Anna"}
```

---

## Dobre praktyki

- projektuj API wokół zasobów,
- dobieraj poprawne metody HTTP,
- używaj sensownych statusów,
- trzymaj spójny format odpowiedzi,
- rozdzielaj błędy klienta od błędów serwera.

---

## Podsumowanie

HTTP i REST to fundament nowoczesnych aplikacji backendowych.

Zanim wejdziesz głębiej w FastAPI, Django czy Flask, warto mieć te pojęcia naprawdę dobrze poukładane.

---

## Mini ściąga

Najważniejsze:

- `GET` pobiera,
- `POST` tworzy,
- `PUT` zastępuje,
- `PATCH` aktualizuje częściowo,
- `DELETE` usuwa,
- status code opisuje wynik żądania.

---

## Ćwiczenia

1. Wyjaśnij różnicę między requestem a response.
2. Wskaż, kiedy użyć `GET`, a kiedy `POST`.
3. Wskaż poprawny status dla utworzenia zasobu.
4. Zaprojektuj endpoint do pobrania jednego produktu.
5. Wyjaśnij, czym jest REST w prostych słowach.

---

## Przykładowe rozwiązania

### 1. Request vs response

Request to żądanie klienta, a response to odpowiedź serwera.

### 2. `GET` vs `POST`

`GET` służy do pobrania danych, a `POST` do utworzenia nowego zasobu.

### 3. Status tworzenia

Najczęściej `201 Created`.

### 4. Produkt

```http
GET /products/123
```

### 5. REST

To styl projektowania API, w którym operujesz na zasobach i poprawnie używasz mechanizmów HTTP.
