# Zestaw ćwiczeń praktycznych — 09. Narzędzia

## Poziom 1 — środowisko i zależności

1. Utwórz nowe środowisko wirtualne dla małego projektu.
2. Aktywuj środowisko i sprawdź ścieżkę do aktywnego Pythona.
3. Zainstaluj jedną bibliotekę do środowiska i wypisz jej wersję.
4. Wyjaśnij własnymi słowami różnicę między systemowym Pythonem a `venv`.
5. Przygotuj listę zależności dla projektu.
6. Zainstaluj bibliotekę z określoną wersją.
7. Wygeneruj plik z zależnościami projektu.
8. Odtwórz środowisko z pliku zależności.

## Poziom 2 — pip i zarządzanie projektem

9. Sprawdź listę zainstalowanych pakietów w środowisku.
10. Odinstaluj wybraną bibliotekę.
11. Zainstaluj pakiet lokalnie tylko dla projektu.
12. Sprawdź, która wersja pakietu jest aktualnie używana.
13. Napisz krótki opis tego, po co projektowi potrzebny jest plik zależności.
14. Rozdziel zależności „runtime” i narzędziowe na dwóch przykładach.
15. Wyjaśnij, co może pójść źle, gdy dwóch programistów używa innych wersji pakietów.

## Poziom 3 — git i porządek repo

16. Zainicjalizuj małe repo testowe i wykonaj pierwszy commit.
17. Dodaj `.gitignore` dla środowiska wirtualnego i plików tymczasowych.
18. Sprawdź różnicę między plikiem śledzonym i nieśledzonym.
19. Zobacz status repo po kilku zmianach.
20. Dodaj plik do repo i wykonaj drugi commit z sensownym komunikatem.
21. Napisz 3 przykłady dobrych nazw commitów.
22. Utwórz osobny branch testowy.
23. Wyjaśnij, po co programiście Python przydaje się git nawet w małych projektach.

## Poziom 4 — dokumentacja i czytelność

24. Napisz krótkie `README` dla prostego projektu.
25. Dodaj docstringi do 3 funkcji.
26. Opisz moduł i jego przeznaczenie.
27. Napisz docstring dla klasy i jednej metody.
28. Dodaj opis argumentów i wartości zwracanej w docstringu.
29. Napisz krótki przykład użycia funkcji w docstringu.
30. Popraw nieczytelny opis funkcji tak, aby ktoś nowy zrozumiał jej przeznaczenie.

## Poziom 5 — logging

31. Skonfiguruj `logging` na poziomie `INFO`.
32. Zaloguj komunikat `DEBUG`, `INFO`, `WARNING`, `ERROR`.
33. Zaloguj wyjątek przez `logging.exception()`.
34. Zapisz logi do pliku.
35. Dodaj do formatu loga czas i poziom logowania.
36. Napisz małą funkcję, która loguje rozpoczęcie i zakończenie działania.
37. Pokaż różnicę między `print()` i `logging` na prostym przykładzie.
38. Dodaj logger modułowy przez `logging.getLogger(__name__)`.

## Poziom 6 — debugowanie

39. Wstaw `breakpoint()` do małej funkcji i przejdź przez nią krok po kroku.
40. Użyj `pdb` do sprawdzenia wartości zmiennej w problematycznym miejscu.
41. Zasymuluj błąd logiczny i znajdź go przez debugowanie.
42. Użyj `p` albo `pp` w debuggerze do wypisania stanu danych.
43. Sprawdź stos wywołań w debuggerze.
44. Porównaj debugowanie przez `print()` i przez `breakpoint()`.
45. Napisz krótko, kiedy `breakpoint()` daje większą wartość niż dodatkowe logi.

## Poziom 7 — profilowanie

46. Porównaj dwa proste sposoby wykonania tej samej operacji przez `timeit`.
47. Sprawdź, czy comprehension jest szybsze od zwykłej pętli w prostym przypadku.
48. Użyj `cProfile` do sprawdzenia, która funkcja jest najwolniejsza.
49. Zmierz czas działania fragmentu kodu przed i po małej poprawce.
50. Napisz przykład, w którym nie warto optymalizować bez wcześniejszego pomiaru.
51. Wyjaśnij różnicę między debugowaniem a profilowaniem.

## Poziom 8 — subprocess

52. Napisz skrypt uruchamiający prostą komendę przez `subprocess.run()`.
53. Przechwyć `stdout` z procesu i wypisz wynik.
54. Przechwyć `stderr` z procesu i zobacz, jak wygląda błąd.
55. Dodaj `check=True` i sprawdź zachowanie przy nieudanej komendzie.
56. Dodaj `timeout`.
57. Uruchom komendę z argumentami przekazanymi jako lista.
58. Napisz funkcję pomocniczą do bezpiecznego uruchamiania komend.
59. Wyjaśnij, czemu składanie jednej dużej komendy tekstowej bywa mniej bezpieczne niż przekazanie listy argumentów.

## Poziom 9 — zadania przekrojowe

60. Zbuduj mały projekt CLI z własnym `venv`, `README` i `.gitignore`.
61. Dodaj logowanie do tego projektu.
62. Celowo wprowadź błąd i zdebuguj go przez `breakpoint()`.
63. Zmierz czas działania wybranego fragmentu przez `timeit` albo `cProfile`.
64. Uruchom pomocniczą komendę systemową przez `subprocess` i zapisz wynik do loga.
65. Przygotuj instrukcję uruchomienia projektu od zera dla innej osoby.
66. Zrób małe repo testowe pokazujące sensowny przepływ: zmiana -> commit -> log -> debug -> pomiar.

## Zadanie końcowe

67. Zbuduj małe narzędzie CLI do analizy pliku:

- ma `README`,
- używa `logging`,
- da się je debugować,
- działa z wirtualnego środowiska,
- ma uporządkowane zależności,
- odpala zewnętrzną komendę pomocniczą przez `subprocess`,
- potrafi zmierzyć czas działania wybranego fragmentu.

Pokaż przy tym, że rozumiesz:

- po co istnieje `venv`,
- jak zarządzać zależnościami,
- jak utrzymywać porządek w repo,
- kiedy używać logowania,
- jak znaleźć błąd,
- jak mierzyć wydajność zamiast zgadywać,
- jak bezpiecznie uruchamiać zewnętrzne procesy.
