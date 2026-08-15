# Zestaw ćwiczeń praktycznych — 13. Web i API

Ćwiczenia są ułożone od zrozumienia protokołu HTTP do zbudowania małego, sensownego API z walidacją, błędami i testami.

Najlepiej robić je po kolei.

---

## Poziom 1 — HTTP i REST

1. Rozpisz endpointy REST dla zasobu `users`.
2. Rozpisz endpointy REST dla zasobu `orders`.
3. Dobierz poprawne metody HTTP dla:

- listowania,
- pobierania jednego zasobu,
- tworzenia,
- pełnej aktualizacji,
- częściowej aktualizacji,
- usuwania.

4. Dobierz poprawne status codes do kilku scenariuszy:

- poprawne pobranie danych,
- utworzenie zasobu,
- brak zasobu,
- błędne dane wejściowe,
- brak autoryzacji.

5. Wyjaśnij własnymi słowami, czym różni się `PUT` od `PATCH`.
6. Wyjaśnij, czemu `GET` nie powinien służyć do zmiany danych.

---

## Poziom 2 — `Pydantic` i walidacja

7. Napisz model `UserCreate`.
8. Napisz model `ProductCreate`.
9. Zweryfikuj poprawne dane wejściowe dla modelu.
10. Zweryfikuj błędne dane wejściowe dla modelu.
11. Rozdziel model wejściowy i model wyjściowy dla tego samego zasobu.
12. Zaprojektuj osobny model do aktualizacji częściowej.
13. Opisz, jakie dane wejściowe API powinny być walidowane obowiązkowo.

---

## Poziom 3 — FastAPI basics

14. Napisz endpoint `GET /health`.
15. Napisz endpoint `GET /users/{user_id}`.
16. Napisz endpoint `POST /users` z modelem `Pydantic`.
17. Dodaj query parameter `limit`.
18. Dodaj odpowiedź JSON zawierającą listę użytkowników.
19. Dodaj prosty endpoint `DELETE /users/{user_id}`.
20. Uruchom aplikację i sprawdź odpowiedzi dla kilku endpointów.

---

## Poziom 4 — routing i struktura

21. Wydziel router `users`.
22. Wydziel router `orders`.
23. Dodaj prefix i tagi do obu routerów.
24. Połącz routery w `main.py`.
25. Zaprojektuj prosty podział plików dla małego API.
26. Wyjaśnij, czemu trzymanie wszystkiego w jednym pliku szybko staje się złym pomysłem.

---

## Poziom 5 — dependency injection

27. Napisz zależność `get_settings`.
28. Napisz zależność `get_current_user` w uproszczonej wersji.
29. Dodaj zależność do endpointu `GET /me`.
30. Zastanów się, które elementy backendu warto dostarczać przez `Depends`.
31. Wyjaśnij, czemu DI poprawia testowalność.

---

## Poziom 6 — autoryzacja i błędy

32. Zaprojektuj endpoint tylko dla zalogowanego użytkownika.
33. Zaprojektuj endpoint tylko dla administratora.
34. Dodaj obsługę scenariusza „zasób nie istnieje”.
35. Dodaj obsługę scenariusza „użytkownik nie ma dostępu”.
36. Zaprojektuj spójny format błędów API.
37. Rozpisz różnicę między `401` i `403`.
38. Opisz, jakich szczegółów błędu nie warto ujawniać klientowi.

---

## Poziom 7 — testowanie API

39. Napisz test dla poprawnego `GET /health`.
40. Napisz test dla poprawnego `POST /users`.
41. Napisz test dla błędnych danych wejściowych.
42. Napisz test dla braku autoryzacji.
43. Napisz test dla braku zasobu.
44. Napisz test sprawdzający strukturę JSON odpowiedzi.
45. Rozdziel testy pozytywne i negatywne tak, żeby były czytelne.

---

## Poziom 8 — myślenie backendowe

46. Zaprojektuj małe API do zarządzania zadaniami.
47. Rozpisz dla niego endpointy, modele wejściowe i modele wyjściowe.
48. Zdecyduj, które endpointy wymagają autoryzacji.
49. Zdecyduj, które błędy są walidacyjne, a które domenowe.
50. Zdecyduj, które scenariusze testowe są obowiązkowe.

---

## Zadanie końcowe

51. Zbuduj mini API do zarządzania zadaniami obejmujące:

- `GET /tasks`,
- `GET /tasks/{id}`,
- `POST /tasks`,
- `PATCH /tasks/{id}`,
- `DELETE /tasks/{id}`,
- modele `Pydantic`,
- routing,
- prostą autoryzację,
- spójną obsługę błędów,
- podstawowe testy endpointów.

52. Opisz krótko:

- jakie są zasoby,
- jakie są kontrakty wejścia i wyjścia,
- które endpointy są publiczne, a które prywatne,
- jakie błędy klient powinien dostać w najważniejszych scenariuszach.

---

## Jak pracować z tym zestawem

Najlepiej:

1. najpierw zrobić poziomy 1-3,
2. potem pokazać rozwiązania,
3. dopiero później przejść do DI, autoryzacji i testów,
4. zadanie końcowe potraktować jak pierwszy mini-backend.
