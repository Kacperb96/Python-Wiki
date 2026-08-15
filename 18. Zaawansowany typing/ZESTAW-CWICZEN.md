# Zestaw ćwiczeń praktycznych — 18. Zaawansowany typing

W tym folderze szczególnie ważne jest nie tylko "napisać adnotację", ale też rozumieć, jaki problem ona rozwiązuje.

## Poziom 1 — `Protocol`

1. Zdefiniuj prosty `Protocol` dla obiektu z metodą `send()`.
2. Napisz dwie klasy spełniające ten sam `Protocol` bez wspólnego dziedziczenia.
3. Wyjaśnij własnymi słowami różnicę między `Protocol` a zwykłą klasą bazową.
4. Podaj przykład, gdzie duck typing i `Protocol` dobrze się uzupełniają.
5. Pokaż przypadek, gdzie `Protocol` poprawia czytelność serwisu przyjmującego zależność.

## Poziom 2 — `TypeVar` i generyki

6. Napisz funkcję `identity`, która zwraca dokładnie ten sam typ, który dostaje.
7. Napisz generyczną funkcję zwracającą pierwszy element listy.
8. Zbuduj prostą generyczną klasę `Box[T]`.
9. Wyjaśnij, dlaczego `TypeVar` daje więcej niż zwykłe `Any`.
10. Pokaż przykład funkcji, która bez generyka traci informację o typie wyniku.

## Poziom 3 — variance

11. Wyjaśnij własnymi słowami, czym jest covariance.
12. Wyjaśnij własnymi słowami, czym jest contravariance.
13. Podaj intuicyjny przykład z typami `Animal`, `Dog`, `Cat`.
14. Opisz, czemu ten temat pojawia się częściej przy kolekcjach, callbackach i interfejsach.
15. Wskaż, dlaczego variance bywa trudna i kiedy wystarczy rozumieć ją intuicyjnie.

## Poziom 4 — `ParamSpec`

16. Napisz dekorator logujący, który zachowuje sygnaturę dekorowanej funkcji.
17. Pokaż, co tracisz, gdy typujesz dekorator zbyt ogólnie przez `Callable[..., Any]`.
18. Wyjaśnij, po co istnieje `ParamSpec`.
19. Dodaj dekorator mierzący czas wykonania i zachowujący typy argumentów.
20. Porównaj dekorator źle i dobrze opisany typami.

## Poziom 5 — `TypeGuard`

21. Napisz funkcję sprawdzającą, czy lista zawiera wyłącznie stringi.
22. Oznacz ją jako `TypeGuard[list[str]]`.
23. Pokaż, jak po takim checku typ wejścia staje się węższy.
24. Wyjaśnij różnicę między zwykłym `bool` a `TypeGuard`.
25. Opisz przypadek, gdzie własny checker typu poprawia czytelność kodu.

## Poziom 6 — `@overload`

26. Napisz funkcję, która dla wejścia `int` zwraca `int`, a dla `str` zwraca `str`.
27. Dodaj do niej przeciążenia przez `@overload`.
28. Wyjaśnij, kiedy `@overload` daje realną wartość.
29. Podaj przykład, gdzie `Union` jest zbyt mało precyzyjne.
30. Porównaj prostą funkcję z `Union` i wersję z `@overload`.

## Poziom 7 — `mypy` i `pyright`

31. Wybierz mały moduł i dodaj do niego typy.
32. Wyobraź sobie, jakie błędy mógłby tam wykryć checker typów.
33. Opisz, czym różni się błąd runtime od błędu wychwyconego statycznie.
34. Zaprojektuj prostą strategię wprowadzania typów do istniejącego projektu.
35. Wypisz 5 zasad rozsądnego używania `mypy` lub `pyright`.

## Poziom 8 — zadania przekrojowe

36. Zbuduj prosty system powiadomień, gdzie serwis zależy od `Protocol` zamiast konkretnej klasy.
37. Użyj generycznej klasy do opisu kontenera danych.
38. Dodaj dekorator z `ParamSpec`.
39. Dodaj własny checker z `TypeGuard`.
40. Wybierz jedno miejsce, gdzie `@overload` poprawia precyzję API.

## Zadanie końcowe

41. Zbuduj mały moduł z zaawansowanym typingiem, który zawiera:

- `Protocol`,
- co najmniej jedną funkcję generyczną,
- dekorator z `ParamSpec`,
- checker z `TypeGuard`,
- jedno sensowne użycie `@overload`.

Na końcu opisz:

- które typy rzeczywiście poprawiły projekt,
- które były najtrudniejsze do zrozumienia,
- gdzie najłatwiej przesadzić z komplikowaniem adnotacji.
