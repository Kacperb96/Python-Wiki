# Zestaw ćwiczeń praktycznych — 20. Performance i optymalizacja

W tym folderze bardzo ważne jest nie tylko „napisać szybszy kod”, ale przede wszystkim umieć uzasadnić, co i dlaczego przyspieszyłeś.

## Poziom 1 — myślenie o wydajności

1. Wyjaśnij własnymi słowami, czym różni się benchmark od profilowania.
2. Podaj przykład przedwczesnej optymalizacji.
3. Wyjaśnij różnicę między CPU-bound i I/O-bound.
4. Wskaż przykład problemu, gdzie algorytm jest ważniejszy niż mikrosztuczki.
5. Opisz, czemu „wydaje mi się, że to wolne” nie wystarcza.

## Poziom 2 — benchmarki

6. Porównaj dwa sposoby zbudowania tej samej listy.
7. Porównaj ręczną pętlę i list comprehension.
8. Zmierz dwa sposoby łączenia tekstu.
9. Zrób kilka powtórzeń pomiaru i porównaj wyniki.
10. Opisz, jakie czynniki mogą zafałszować benchmark.

## Poziom 3 — CPU vs I/O

11. Podaj 5 przykładów zadań CPU-bound.
12. Podaj 5 przykładów zadań I/O-bound.
13. Opisz, kiedy wątki mogą pomóc.
14. Opisz, kiedy procesy mogą pomóc.
15. Wybierz jeden problem i sklasyfikuj go jako CPU-bound albo I/O-bound z uzasadnieniem.

## Poziom 4 — profilowanie

16. Napisz mały program z jednym oczywistym wąskim gardłem.
17. Wskaż, który fragment chciałbyś profilować jako pierwszy.
18. Opisz, czym różni się zgadywanie od profilowania.
19. Podaj przykład kodu, który wygląda groźnie, ale nie jest realnym hot spotem.
20. Zrób checklistę: co sprawdzasz przed optymalizacją.

## Poziom 5 — algorytmy i struktury danych

21. Porównaj wyszukiwanie w liście i w secie.
22. Opisz, czemu zła struktura danych może zabić wydajność.
23. Wskaż przypadek, gdzie `dict` jest lepszy niż lista rekordów.
24. Opisz przykład, w którym zmiana algorytmu daje większy zysk niż mikrooptymalizacja składni.
25. Znajdź fragment kodu, gdzie da się poprawić złożoność rozwiązania.

## Poziom 6 — streaming i pamięć

26. Opisz różnicę między wczytaniem wszystkiego do listy a iteracją po generatorze.
27. Pokaż przykład przetwarzania pliku linia po linii.
28. Wyjaśnij, kiedy streaming ma sens.
29. Opisz, czemu pełne wczytanie danych czasem jest błędem architektonicznym, a nie tylko wydajnościowym.
30. Podaj przykład oszczędzania pamięci przez zmianę modelu przetwarzania.

## Poziom 7 — decyzje optymalizacyjne

31. Opisz sytuację, w której nie warto jeszcze optymalizować.
32. Opisz sytuację, w której optymalizacja jest już obowiązkowa.
33. Porównaj koszt utrzymania bardzo sprytnego kodu z jego zyskiem wydajnościowym.
34. Zbuduj małą strategię optymalizacji dla projektu, który ma spowolnienie.
35. Wypisz 5 zasad zdrowego podejścia do performance.

## Zadanie końcowe

36. Weź mały program albo moduł i zrób mini analizę wydajności:

- co mierzyć,
- czy problem jest CPU czy I/O,
- gdzie może być hot spot,
- czy problem dotyczy pamięci,
- czy warto użyć streamingu,
- jaka byłaby pierwsza sensowna poprawka,
- czego na pewno byś jeszcze nie optymalizował.
