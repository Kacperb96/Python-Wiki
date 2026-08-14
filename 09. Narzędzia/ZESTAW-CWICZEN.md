# Zestaw ćwiczeń praktycznych — 09. Narzędzia

## Poziom 1 — środowisko i zależności

1. Utwórz nowe środowisko wirtualne dla małego projektu.
2. Zainstaluj jedną bibliotekę do środowiska i wypisz jej wersję.
3. Wyjaśnij własnymi słowami różnicę między systemowym Pythonem a `venv`.
4. Przygotuj listę zależności dla projektu.

## Poziom 2 — git i dokumentacja

5. Zainicjalizuj małe repo testowe i wykonaj pierwszy commit.
6. Dodaj `.gitignore` dla środowiska wirtualnego i plików tymczasowych.
7. Napisz krótkie `README` dla prostego projektu.
8. Dodaj docstringi do 3 funkcji.
9. Opisz moduł i jego przeznaczenie.

## Poziom 3 — logging i debugowanie

10. Skonfiguruj `logging` na poziomie `INFO`.
11. Zaloguj komunikat `DEBUG`, `INFO`, `WARNING`, `ERROR`.
12. Zaloguj wyjątek przez `logging.exception()`.
13. Wstaw `breakpoint()` do małej funkcji i przejdź przez nią krok po kroku.
14. Użyj `pdb` do sprawdzenia wartości zmiennej w problematycznym miejscu.

## Poziom 4 — profilowanie i subprocess

15. Porównaj dwa proste sposoby wykonania tej samej operacji przez `timeit`.
16. Użyj `cProfile` do sprawdzenia, która funkcja jest najwolniejsza.
17. Napisz skrypt uruchamiający prostą komendę przez `subprocess.run()`.
18. Przechwyć `stdout` z procesu i wypisz wynik.
19. Dodaj `check=True` i `timeout`.

## Zadanie końcowe

20. Zbuduj małe narzędzie CLI do analizy pliku:
   - ma `README`,
   - używa `logging`,
   - można je debugować,
   - da się uruchomić z wirtualnego środowiska,
   - odpala zewnętrzną komendę pomocniczą przez `subprocess`,
   - potrafi zmierzyć czas działania wybranego fragmentu.
