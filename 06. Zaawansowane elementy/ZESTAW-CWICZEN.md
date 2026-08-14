# Zestaw ćwiczeń praktycznych — 06. Zaawansowane elementy

## Poziom 1 — iterowalne obiekty, iteratory i `yield`

1. Napisz generator zwracający liczby od `1` do `n`.
2. Napisz generator zwracający tylko liczby parzyste z podanego zakresu.
3. Napisz generator zwracający kolejne kwadraty liczb.
4. Napisz własny iterator klasy `Licznik`, który iteruje od `start` do `end`.
5. Napisz funkcję, która przyjmuje iterator i wypisuje wszystkie jego elementy.
6. Pokaż różnicę między obiektem iterowalnym a iteratorem na prostym przykładzie.
7. Użyj `next()` ręcznie na iteratorze listy.
8. Pokaż, co się dzieje, gdy iterator się skończy.

## Poziom 2 — generatory w praktyce

9. Napisz generator zwracający słowa z listy jedno po drugim.
10. Napisz generator filtrujący tylko dodatnie liczby.
11. Napisz generator, który dla każdej liczby zwraca jej sześcian.
12. Połącz kilka generatorów w prosty pipeline danych.
13. Napisz generator zwracający liczby Fibonacciego do określonego limitu.
14. Napisz generator, który czyta dane partiami z listy po `n` elementów.
15. Pokaż na przykładzie, że generator „zużywa się” po przejściu iteracji.
16. Porównaj listę składana i generator expression dla tego samego przypadku.

## Poziom 3 — context managery

17. Użyj `with open(...)` do bezpiecznej pracy z plikiem.
18. Napisz własny context manager klasowy, który wypisuje `start` i `koniec`.
19. Napisz context manager, który mierzy czas wykonania bloku `with`.
20. Napisz context manager do tymczasowej zmiany flagi konfiguracyjnej.
21. Napisz context manager, który przechwytuje wyjątek i wypisuje komunikat.
22. Zbuduj context manager, który zapisuje moment wejścia i wyjścia z bloku.
23. Napisz wersję context managera opartą o `contextlib.contextmanager`.
24. Porównaj klasowy context manager i wersję generatorową.

## Poziom 4 — programowanie funkcyjne

25. Użyj `map()` do przekształcenia listy liczb na ich kwadraty.
26. Użyj `filter()` do odfiltrowania tylko dodatnich liczb.
27. Użyj `reduce()` do policzenia sumy albo iloczynu listy liczb.
28. Porównaj czytelność wersji z `map()` i zwykłej pętli.
29. Napisz funkcję korzystającą z `lambda` jako krótkiego callbacka.
30. Użyj `sorted(..., key=...)` i wyjaśnij, jaką rolę pełni przekazana funkcja.
31. Napisz mały przykład z `any()` i `all()`.
32. Rozwiąż ten sam problem funkcyjnie i imperatywnie, a potem porównaj style.

## Poziom 5 — deskryptory

33. Napisz prosty deskryptor, który loguje odczyt atrybutu.
34. Napisz deskryptor walidujący, że przypisana liczba jest dodatnia.
35. Użyj tego deskryptora w klasie `Product`.
36. Napisz drugi deskryptor walidujący minimalną długość napisu.
37. Dodaj deskryptor do klasy `User`, aby pilnował poprawności pola `email` lub `name`.
38. Pokaż, kiedy wywołuje się `__get__`, `__set__` i `__delete__`.
39. Napisz prosty deskryptor przechowujący dane pod ukrytą nazwą atrybutu.
40. Wyjaśnij na własnym przykładzie, po co w ogóle używać deskryptora zamiast zwykłego `@property`.

## Poziom 6 — `__slots__`

41. Napisz klasę z `__slots__` i spróbuj przypisać do niej nowy atrybut spoza slotów.
42. Porównaj klasę zwykłą i klasę z `__slots__` pod kątem tego, jakie atrybuty można dodawać.
43. Napisz klasę `Point` z `__slots__ = ("x", "y")`.
44. Sprawdź, czy instancja klasy ze slotami ma `__dict__`.
45. Dodaj do klasy ze slotami metodę i pokaż, że metody nadal działają normalnie.
46. Spróbuj połączyć `__slots__` z dziedziczeniem w prostym przykładzie.

## Poziom 7 — pamięć, referencje i model obiektów

47. Pokaż na przykładzie, że dwie zmienne mogą wskazywać na tę samą listę.
48. Zademonstruj różnicę między kopiowaniem referencji a tworzeniem nowej listy.
49. Pokaż różnicę między `==` i `is` na mutowalnych i niemutowalnych obiektach.
50. Napisz mały eksperyment pokazujący, że zmiana listy przez jedną referencję jest widoczna przez drugą.
51. Porównaj pamięciowo listę i generator dla większego zbioru danych.
52. Pokaż prosty przykład, kiedy generator jest lepszy od listy pod względem pamięci.
53. Pokaż prosty przykład, kiedy lista jest wygodniejsza niż generator.
54. Wyjaśnij na własnym przykładzie pojęcie mutowalności.

## Poziom 8 — zadania przekrojowe

55. Zbuduj pipeline danych:
generator źródłowy, filtr i transformacja.
56. Do pipeline’u dodaj context manager mierzący czas.
57. Użyj deskryptora w klasie opisującej rekord przetwarzanych danych.
58. Napisz mini system logowania wejścia i wyjścia z sekcji krytycznej przez `with`.
59. Zbuduj iterator klasowy i generator rozwiązujące ten sam problem, a potem porównaj oba podejścia.
60. Zrób przykład, w którym `map()`, generator i zwykła pętla dają ten sam wynik.

## Zadanie końcowe

61. Zbuduj mini pipeline przetwarzania danych:

- generator źródłowy,
- filtr,
- transformacja,
- context manager mierzący czas,
- walidacja przez deskryptor w klasie modelującej rekord,
- porównanie wersji listowej i generatorowej.

Pokaż przy tym, że rozumiesz:

- czym różni się iterator od generatora,
- po co używa się `with`,
- kiedy styl funkcyjny ma sens,
- co robi deskryptor,
- kiedy `__slots__` może być przydatne,
- jak referencje i mutowalność wpływają na zachowanie programu.
