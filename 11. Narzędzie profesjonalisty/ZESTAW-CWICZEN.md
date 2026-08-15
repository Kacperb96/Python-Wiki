# Zestaw ćwiczeń praktycznych — 11. Narzędzie profesjonalisty

Ćwiczenia są ułożone od najważniejszych podstaw workflow do bardziej dojrzałej automatyzacji.

Nie próbuj robić wszystkiego naraz.

Najpierw zrozum narzędzia jakości i konfigurację projektu, dopiero potem wchodź w pełną orkiestrację workflow.

---

## Poziom 1 — `pyproject.toml`

1. Utwórz minimalny `pyproject.toml` dla małego projektu.
2. Dodaj `requires-python`.
3. Dodaj nazwę, wersję i opis projektu.
4. Dodaj zależności runtime.
5. Dodaj sekcję zależności developerskich.
6. Wyjaśnij własnymi słowami, czemu `pyproject.toml` jest wygodniejszy niż porozrzucane ustawienia.

---

## Poziom 2 — linting i formatowanie

7. Dodaj minimalną konfigurację `ruff`.
8. Dodaj minimalną konfigurację `black`.
9. Dodaj konfigurację `isort` zgodną z `black`.
10. Przygotuj plik z nieużywanym importem i zobacz, co zgłosi `ruff`.
11. Przygotuj brzydko sformatowaną funkcję i zobacz, co zrobi `black`.
12. Przygotuj chaotyczny blok importów i uporządkuj go `isort` albo regułami importów w `ruff`.
13. Ustal wspólną długość linii dla narzędzi.

---

## Poziom 3 — typy i automatyczne checki

14. Dodaj podstawową konfigurację `mypy`.
15. Napisz funkcję z błędnym typem zwracanym i sprawdź, czy `mypy` to wykryje.
16. Napisz funkcję przyjmującą `int`, a wywołaj ją z `str`, i zobacz raport `mypy`.
17. Utwórz minimalny `.pre-commit-config.yaml`.
18. Dodaj do `pre-commit` `ruff` i prosty hook tekstowy.
19. Opisz, które checki warto odpalać lokalnie przed commitem, a które nie muszą lecieć za każdym razem.

---

## Poziom 4 — ergonomia projektu

20. Napisz prosty `Makefile` z targetami `test`, `lint`, `format`.
21. Dodaj target `typecheck`.
22. Dodaj target `check`, który uruchamia kilka narzędzi jakości.
23. Opisz, po co `Makefile` jest wygodny w projekcie zespołowym.
24. Zastanów się, które komendy naprawdę uruchamiasz najczęściej i warto je skrócić.

---

## Poziom 5 — zarządzanie zależnościami

25. Wyjaśnij różnicę między `pip` + `venv`, `poetry` i `uv`.
26. Opisz projekt, w którym `poetry` ma sens.
27. Opisz projekt, w którym `uv` ma sens.
28. Opisz projekt, w którym prosty `venv` + `pip` jest wystarczający.
29. Wskaż, dlaczego mieszanie kilku workflow zależności naraz robi bałagan.
30. Zapisz własny rekomendowany workflow dla małego projektu jednoosobowego.

---

## Poziom 6 — CI i automatyzacja zespołowa

31. Napisz minimalny workflow GitHub Actions dla projektu Python.
32. Dodaj w nim checkout repo, setup Pythona i uruchomienie testów.
33. Rozszerz workflow o `ruff`.
34. Rozszerz workflow o `mypy`.
35. Opisz, czemu CI powinno być spójne z lokalnym workflow.
36. Wyjaśnij, czemu czerwony pipeline trzeba traktować poważnie.

---

## Poziom 7 — `tox` i `nox`

37. Wyjaśnij, jaki problem rozwiązuje `tox`.
38. Wyjaśnij, jaki problem rozwiązuje `nox`.
39. Porównaj `tox` i `nox` własnymi słowami.
40. Wskaż projekt, gdzie `tox` ma sens.
41. Wskaż projekt, gdzie `nox` ma sens.
42. Wskaż projekt, gdzie oba mogą być nadmiarem.
43. Opisz, czemu te narzędzia nie zastępują testów, tylko organizują ich uruchamianie.

---

## Poziom 8 — myślenie projektowe

44. Zaprojektuj minimalny profesjonalny setup dla małego API w Pythonie.
45. Wybierz jedno podejście do zależności: `poetry`, `uv` albo `pip` + `venv`, i uzasadnij wybór.
46. Zdecyduj, czy w tym projekcie użyjesz `Makefile`.
47. Zdecyduj, czy użyjesz `pre-commit`.
48. Zdecyduj, czy użyjesz `mypy` w trybie lekkim czy mocniejszym.
49. Zdecyduj, czy od razu potrzebujesz `tox` albo `nox`.

---

## Zadanie końcowe

50. Zaprojektuj kompletny setup profesjonalnego małego projektu Python zawierający:

- `pyproject.toml`,
- `ruff`,
- `black`,
- `mypy`,
- `pre-commit`,
- `Makefile`,
- workflow GitHub Actions,
- opis lokalnego workflow developera.

51. Napisz krótkie uzasadnienie:

- czemu wybrałeś te narzędzia,
- czego świadomie nie dodajesz,
- które elementy są obowiązkowe, a które opcjonalne dla takiego projektu.

---

## Jak pracować z tym zestawem

Najlepiej:

1. najpierw zrób zadania 1-19,
2. potem pokaż rozwiązania,
3. dopiero później przejdź do CI, `tox` i `nox`,
4. na końcu zrób zadanie końcowe jako projektowy mini-audyt własnego workflow.
