# Zestaw ćwiczeń praktycznych — 10. Testowanie

Ćwiczenia są ułożone od prostych do bardziej dojrzałych.

Najlepiej robić je warstwowo.

Nie przeskakuj od razu do mocków i `hypothesis`, jeśli nie czujesz jeszcze zwykłego `pytest`.

---

## Poziom 1 — pierwsze testy w `pytest`

1. Napisz funkcję `dodaj(a, b)` i test sprawdzający kilka prostych przypadków.
2. Napisz funkcję `jest_parzysta(n)` i przetestuj liczby parzyste oraz nieparzyste.
3. Napisz funkcję `powitaj(imie)` i sprawdź, czy zwraca poprawny napis.
4. Napisz test dla funkcji `pole_prostokata(a, b)`.
5. Napisz test dla funkcji `czy_pelnoletni(wiek)`.
6. Zgrupuj kilka testów w jednym pliku `test_utils.py`.
7. Uruchom `pytest` dla jednego pliku testowego.
8. Uruchom `pytest -q` i porównaj output ze zwykłym `pytest`.

---

## Poziom 2 — przypadki błędne i wyjątki

9. Napisz funkcję `bezpieczne_dzielenie(a, b)`, która rzuca `ZeroDivisionError`, i przetestuj ten wyjątek.
10. Napisz funkcję `parse_int(tekst)` i przetestuj przypadek poprawny oraz błędny.
11. Napisz test dla pustego stringa w funkcji `normalizuj_imie()`.
12. Napisz test dla wartości granicznych, np. `wiek = 17`, `18`, `19`.
13. Napisz test dla funkcji, która ma zwrócić `None` w szczególnej sytuacji.
14. Dodaj test, który upewnia się, że błędne dane wejściowe są odrzucone.

---

## Poziom 3 — lepsze użycie `pytest`

15. Użyj `@pytest.mark.parametrize`, żeby przetestować kilka przypadków funkcji `dodaj()`.
16. Użyj `@pytest.mark.parametrize`, żeby przetestować funkcję `jest_parzysta()` dla wielu danych.
17. Napisz fixture `user_data`, która zwraca przykładowy słownik użytkownika.
18. Użyj tej samej fixture w co najmniej dwóch testach.
19. Napisz fixture przygotowującą listę produktów.
20. Zrób fixture z `yield`, która tworzy zasób i go sprząta.
21. Umieść wspólną fixture w `conftest.py`.
22. Napisz test parametryzowany dla kilku błędnych danych wejściowych.

---

## Poziom 4 — organizacja testów

23. Rozdziel testy jednostkowe i integracyjne do osobnych plików.
24. Zrób małą strukturę katalogu `tests/unit` i `tests/integration`.
25. Napisz test jednostkowy dla czystej logiki funkcji.
26. Napisz prosty test integracyjny dla funkcji zapisującej dane do pliku i potem je odczytującej.
27. Zastanów się i opisz, dlaczego jeden test jest jednostkowy, a drugi integracyjny.
28. Dodaj czytelne nazwy testów tak, by od razu było wiadomo, co sprawdzają.

---

## Poziom 5 — mocking

29. Zamockuj funkcję wysyłającą mail.
30. Zamockuj klienta HTTP, który normalnie pobiera dane z API.
31. Zamockuj repozytorium w prostym serwisie biznesowym.
32. Sprawdź, czy mock został wywołany z odpowiednimi argumentami.
33. Użyj `return_value`, żeby sterować wynikiem mocka.
34. Użyj `side_effect`, żeby zasymulować wyjątek.
35. Zamockuj klasę tworzoną wewnątrz testowanej funkcji.
36. Napisz przykład złego patchowania i popraw go tak, by patchować we właściwym miejscu.

---

## Poziom 6 — coverage

37. Uruchom `coverage run -m pytest` dla małego projektu.
38. Wygeneruj raport przez `coverage report`.
39. Sprawdź, które linie kodu nie są pokryte testami.
40. Dopisz brakujące testy dla jednej krytycznej funkcji.
41. Porównaj coverage przed i po dopisaniu testów.
42. Sprawdź, czy wyższy coverage rzeczywiście oznacza lepsze testy w Twoim przykładzie.
43. Zastanów się, które linie są niepokryte dlatego, że kod ma słaby design.

---

## Poziom 7 — `hypothesis`

44. Napisz prosty test property-based dla dodawania.
45. Napisz test właściwości: odwrócenie listy dwa razy daje oryginał.
46. Napisz test właściwości: `sorted(xs)` ma tę samą długość co `xs`.
47. Napisz test property-based dla funkcji normalizującej tekst.
48. Wymyśl własną sensowną właściwość dla funkcji z projektu.
49. Celowo napisz błędną funkcję i zobacz, czy `hypothesis` znajdzie kontrprzykład.
50. Opisz własnymi słowami, czym różni się zwykły test od testu opartego na właściwości.

---

## Poziom 8 — scenariusze bardziej realistyczne

51. Napisz test dla serwisu, który korzysta z walidatora i repozytorium.
52. Napisz test dla funkcji, która pobiera dane, przetwarza je i zwraca wynik końcowy.
53. Napisz test poprawnego scenariusza i osobny test scenariusza błędnego dla tej samej operacji.
54. Przetestuj funkcję, która zależy od bieżącego czasu albo losowości, izolując tę zależność.
55. Napisz test dla logiki zamówienia: poprawny zakup, pusty koszyk, brak produktu.
56. Uporządkuj nazwy testów tak, by były czytelną dokumentacją zachowania systemu.

---

## Zadanie końcowe

57. Weź mały projekt z repo i zbuduj dla niego sensowny pakiet testów obejmujący:

- testy jednostkowe,
- testy wyjątków,
- testy parametryzowane,
- fixture,
- mocking zależności,
- coverage,
- przynajmniej 1 test property-based.

58. Opisz krótko:

- co testujesz jednostkowo,
- co integracyjnie,
- co zamockowałeś,
- czego nadal nie testujesz i dlaczego.

---

## Jak pracować z tym zestawem

Najlepiej:

1. zrób 8-12 zadań z poziomów 1-3,
2. pokaż rozwiązania,
3. dopiero potem przejdź do mocków i coverage,
4. `hypothesis` zostaw na moment, w którym zwykłe testy są już naturalne.

W testowaniu jakość myślenia jest ważniejsza niż liczba napisanych asercji.
