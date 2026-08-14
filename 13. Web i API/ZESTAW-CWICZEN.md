# Zestaw ćwiczeń praktycznych — 13. Web i API

## Poziom 1 — HTTP i REST

1. Rozpisz endpointy REST dla zasobu `users`.
2. Rozpisz endpointy REST dla zasobu `orders`.
3. Dobierz poprawne metody HTTP dla:
   - listowania,
   - tworzenia,
   - usuwania,
   - częściowej aktualizacji.
4. Dobierz poprawne status codes do kilku prostych scenariuszy.

## Poziom 2 — Pydantic i walidacja

5. Napisz model `UserCreate`.
6. Napisz model `ProductCreate`.
7. Zweryfikuj poprawne i błędne dane wejściowe.
8. Rozdziel model wejściowy i model wyjściowy dla tego samego zasobu.

## Poziom 3 — FastAPI basics

9. Napisz endpoint `GET /health`.
10. Napisz endpoint `GET /users/{user_id}`.
11. Napisz endpoint `POST /users` z modelem `Pydantic`.
12. Dodaj query parameter `limit`.

## Poziom 4 — routing i struktura

13. Wydziel router `users`.
14. Wydziel router `orders`.
15. Dodaj prefix i tagi do obu routerów.
16. Połącz routery w `main.py`.

## Poziom 5 — dependency injection i błędy

17. Napisz zależność `get_settings`.
18. Napisz zależność `get_current_user` w wersji uproszczonej.
19. Zaprojektuj spójny format błędów API.
20. Dodaj obsługę scenariusza „zasób nie istnieje”.
21. Dodaj obsługę scenariusza „użytkownik nie ma dostępu”.

## Poziom 6 — autoryzacja i testowanie

22. Zaprojektuj endpoint tylko dla zalogowanego użytkownika.
23. Zaprojektuj endpoint tylko dla administratora.
24. Napisz testy dla:
   - poprawnego żądania,
   - błędnych danych,
   - braku autoryzacji,
   - braku zasobu.

## Zadanie końcowe

25. Zbuduj mini API do zarządzania zadaniami:
   - `GET /tasks`
   - `GET /tasks/{id}`
   - `POST /tasks`
   - `PATCH /tasks/{id}`
   - `DELETE /tasks/{id}`
   - modele `Pydantic`,
   - routing,
   - prosta autoryzacja,
   - spójna obsługa błędów,
   - podstawowe testy endpointów.
