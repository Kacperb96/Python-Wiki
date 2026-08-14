# Zestaw ćwiczeń praktycznych — 11. Narzędzie profesjonalisty

## Poziom 1 — konfiguracja projektu

1. Utwórz minimalny `pyproject.toml`.
2. Dodaj `requires-python`.
3. Dodaj zależności runtime.
4. Dodaj grupę `dev`.

## Poziom 2 — linting i formatowanie

5. Dodaj konfigurację `ruff`.
6. Dodaj konfigurację `black`.
7. Dodaj konfigurację `isort`.
8. Przygotuj plik z błędami stylu i opisz, które narzędzie co wykryje.
9. Ustal jednolitą długość linii dla narzędzi.

## Poziom 3 — jakość i automatyzacja

10. Dodaj konfigurację `mypy`.
11. Dodaj minimalny `.pre-commit-config.yaml`.
12. Zaprojektuj prosty `Makefile` z targetami `test`, `lint`, `format`.
13. Wyjaśnij, co powinno trafiać do CI, a co do local pre-commit.

## Poziom 4 — workflow projektu

14. Napisz minimalny workflow GitHub Actions dla projektu Python.
15. Zaprojektuj lokalny workflow:
   - format,
   - lint,
   - typecheck,
   - test.
16. Rozpisz różnicę między `poetry`, `uv`, `pip` i `venv` dla małego projektu.
17. Opisz, kiedy `tox` ma sens.
18. Opisz, kiedy `nox` ma sens.

## Zadanie końcowe

19. Zaprojektuj kompletny profesjonalny setup dla małego projektu:
   - `pyproject.toml`,
   - `ruff`,
   - `black`,
   - `mypy`,
   - `pre-commit`,
   - `Makefile`,
   - GitHub Actions,
   - opis lokalnego workflow developera.
