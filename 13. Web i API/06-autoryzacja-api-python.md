# Autoryzacja API w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Autentykacja a autoryzacja](#autentykacja-a-autoryzacja)
3. [Po co chronić API](#po-co-chronić-api)
4. [Tokeny i nagłówek `Authorization`](#tokeny-i-nagłówek-authorization)
5. [Podstawowy przepływ](#podstawowy-przepływ)
6. [Uprawnienia i role](#uprawnienia-i-role)
7. [Typowe statusy błędów](#typowe-statusy-błędów)
8. [Autoryzacja a FastAPI](#autoryzacja-a-fastapi)
9. [Przykład mentalny chronionego endpointu](#przykład-mentalny-chronionego-endpointu)
10. [Typowe błędy początkujących](#typowe-błędy-początkujących)
11. [Praktyczna ściąga](#praktyczna-ściąga)
12. [Ćwiczenia](#ćwiczenia)
13. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

API bez sensownej autoryzacji bardzo szybko staje się problemem bezpieczeństwa.

Dlatego backendowy Pythonowiec musi rozumieć podstawowe mechanizmy kontroli dostępu.

---

## Autentykacja a autoryzacja

Autentykacja odpowiada na pytanie:

"kim jesteś?"

Autoryzacja odpowiada na pytanie:

"co wolno ci zrobić?"

To różne rzeczy, choć często działają razem.

---

## Po co chronić API

Bo nie każdy klient powinien mieć dostęp do:

- danych innych użytkowników,
- operacji administracyjnych,
- zasobów prywatnych,
- modyfikacji danych.

Brak sensownej autoryzacji bardzo szybko prowadzi do realnych problemów bezpieczeństwa.

---

## Tokeny i nagłówek `Authorization`

W praktyce często spotkasz:

- token dostępu,
- nagłówek `Authorization`,
- schemat `Bearer`.

Przykład:

```http
Authorization: Bearer TOKEN
```

To bardzo powszechny wzorzec w API.

---

## Podstawowy przepływ

W uproszczeniu:

1. użytkownik się loguje,
2. dostaje token,
3. klient wysyła token w kolejnych requestach,
4. serwer sprawdza token,
5. serwer sprawdza uprawnienia.

To prosty model, ale bardzo ważny do zrozumienia.

---

## Uprawnienia i role

Sam fakt zalogowania nie zawsze wystarcza.

Często trzeba jeszcze rozróżniać:

- zwykłego użytkownika,
- moderatora,
- administratora.

To właśnie już jest autoryzacja, a nie sama autentykacja.

---

## Typowe statusy błędów

Najczęściej:

- `401 Unauthorized` gdy brak poprawnej autentykacji,
- `403 Forbidden` gdy użytkownik jest znany, ale nie ma uprawnień.

To bardzo ważne rozróżnienie.

---

## Autoryzacja a FastAPI

W FastAPI bardzo często łączy się autoryzację z dependency injection.

Na przykład zależność może:

- odczytać token,
- zwalidować użytkownika,
- zwrócić aktualnego użytkownika endpointowi.

To bardzo naturalny wzorzec projektowy.

---

## Przykład mentalny chronionego endpointu

Mentalnie wygląda to tak:

- endpoint wymaga aktualnego użytkownika,
- zależność pobiera użytkownika z tokenu,
- jeśli to się nie uda, request kończy się błędem,
- jeśli użytkownik istnieje, można jeszcze sprawdzić rolę albo uprawnienia.

Przykład odpowiedzi przy braku tokenu może wyglądać tak:

```json
{"detail": "Not authenticated"}
```

Przy braku uprawnień np.:

```json
{"detail": "Not enough permissions"}
```

---

## Typowe błędy początkujących

- mylenie `401` i `403`,
- brak testów uprawnień,
- sprawdzanie tylko "czy token istnieje", zamiast "czy naprawdę daje dostęp",
- rozlewanie logiki bezpieczeństwa po całym kodzie bez jednego wzorca,
- zbyt uproszczone podejście typu "jak ktoś ma token, to wolno mu wszystko".

---

## Praktyczna ściąga

### Najważniejsze rozróżnienie

- autentykacja: kim jesteś,
- autoryzacja: co możesz zrobić.

### Najczęstsze statusy

- `401` -> brak poprawnej autentykacji,
- `403` -> brak uprawnień.

### Częsty wzorzec w FastAPI

- zależność `get_current_user`,
- zależność `require_admin`.

---

## Ćwiczenia

1. Wyjaśnij różnicę między autentykacją i autoryzacją.
2. Rozpisz prosty przepływ logowanie -> token -> kolejne requesty.
3. Opisz endpoint dostępny tylko dla zalogowanego użytkownika.
4. Opisz endpoint dostępny tylko dla administratora.
5. Dopasuj poprawnie `401` i `403` do scenariuszy.
6. Wyjaśnij własnymi słowami, czemu sama obecność tokenu to za mało.

---

## Najważniejsze do zapamiętania

- Autentykacja i autoryzacja to nie to samo.
- Token zwykle trafia do nagłówka `Authorization`.
- `401` i `403` oznaczają różne problemy.
- Dobre API musi sprawdzać nie tylko tożsamość, ale i uprawnienia.
- W FastAPI autoryzację bardzo często modeluje się przez zależności.
