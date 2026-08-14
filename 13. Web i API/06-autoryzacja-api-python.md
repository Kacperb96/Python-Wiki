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
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczne przykłady](#praktyczne-przykłady)
11. [Dobre praktyki](#dobre-praktyki)
12. [Podsumowanie](#podsumowanie)
13. [Mini ściąga](#mini-ściąga)
14. [Ćwiczenia](#ćwiczenia)
15. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

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

---

## Tokeny i nagłówek `Authorization`

W praktyce często spotkasz:

- token dostępu,
- nagłówek `Authorization`,
- schemat `Bearer`.

To bardzo powszechny wzorzec w API.

---

## Podstawowy przepływ

W uproszczeniu:

1. użytkownik się loguje,
2. dostaje token,
3. klient wysyła token w kolejnych requestach,
4. serwer sprawdza token,
5. serwer sprawdza uprawnienia.

---

## Uprawnienia i role

Sam fakt zalogowania nie zawsze wystarcza.

Często trzeba jeszcze rozróżniać:

- zwykłego użytkownika,
- moderatora,
- administratora.

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

---

## Typowe błędy początkujących

- mylenie `401` i `403`,
- brak testów uprawnień,
- sprawdzanie tylko "czy token istnieje", zamiast "czy naprawdę daje dostęp",
- rozlewanie logiki bezpieczeństwa po całym kodzie bez jednego wzorca.

---

## Praktyczne przykłady

### Chroniony endpoint

Mentalnie:

- endpoint wymaga aktualnego użytkownika,
- zależność pobiera użytkownika z tokenu,
- jeśli to się nie uda, endpoint nie powinien działać.

### Rola administratora

Nie każdy zalogowany użytkownik powinien móc usuwać innych użytkowników.

---

## Dobre praktyki

- rozróżniaj autentykację i autoryzację,
- jasno modeluj role i uprawnienia,
- trzymaj logikę bezpieczeństwa w przewidywalnych miejscach,
- testuj scenariusze braku dostępu.

---

## Podsumowanie

Autoryzacja API to jeden z kluczowych filarów bezpiecznego backendu.

Nie chodzi tylko o token, ale o poprawny model dostępu do zasobów.

---

## Mini ściąga

Najważniejsze:

- autentykacja mówi, kim jesteś,
- autoryzacja mówi, co możesz zrobić,
- `401` i `403` to nie to samo,
- tokeny i role to częsty wzorzec pracy z API.

---

## Ćwiczenia

1. Wyjaśnij różnicę między autentykacją a autoryzacją.
2. Wyjaśnij, kiedy użyć `401`.
3. Wyjaśnij, kiedy użyć `403`.
4. Podaj przykład endpointu tylko dla admina.
5. Wyjaśnij, czemu sama obecność tokenu nie wystarcza.

---

## Przykładowe rozwiązania

### 1. Różnica

Autentykacja identyfikuje użytkownika, a autoryzacja sprawdza jego uprawnienia.

### 2. `401`

Gdy brak poprawnej autentykacji, np. brak lub zły token.

### 3. `403`

Gdy użytkownik jest rozpoznany, ale nie ma prawa wykonać operacji.

### 4. Admin

Na przykład endpoint usuwający użytkownika z systemu.

### 5. Czemu token nie wystarcza

Bo trzeba jeszcze ustalić, czy ten użytkownik ma dostęp do danego zasobu lub operacji.
