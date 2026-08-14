# Zestaw ćwiczeń praktycznych — 05. Dekoratory

## Poziom 1 — funkcje jako obiekty

1. Napisz funkcję `powitaj()`, przypisz ją do nowej zmiennej i wywołaj przez tę zmienną.
2. Napisz funkcję `wykonaj(f)`, która przyjmuje inną funkcję i ją uruchamia.
3. Utwórz dwie funkcje i włóż je do listy, a potem wywołaj każdą z nich w pętli.
4. Zbuduj słownik komend, w którym kluczem jest tekst, a wartością funkcja.
5. Napisz funkcję, która zwraca inną funkcję i sprawdź, że możesz ją później wywołać.
6. Napisz funkcję `operacja(a, b, f)`, która przyjmuje dwie liczby i funkcję wykonującą działanie.

## Poziom 2 — closures

7. Napisz closure, która pamięta prefiks i dokleja go do przekazanego tekstu.
8. Napisz closure liczące kolejne wywołania funkcji.
9. Napisz closure, która pamięta wartość startową i przy każdym wywołaniu ją zwiększa.
10. Napisz funkcję `generator_mnoznika(n)`, która zwraca funkcję mnożącą argument przez `n`.
11. Zrób closure, która zapamiętuje historię przekazanych napisów w liście.
12. Napisz closure filtrujące liczby większe od ustalonego progu.

## Poziom 3 — pierwszy dekorator

13. Napisz dekorator wypisujący komunikat przed uruchomieniem funkcji.
14. Rozszerz go tak, by wypisywał też komunikat po zakończeniu funkcji.
15. Udekoruj funkcję bez używania składni `@`, tylko przez ręczne przypisanie.
16. Napisz dekorator, który zlicza ile razy funkcja została wywołana.
17. Napisz dekorator logujący nazwę funkcji przez `f.__name__`.
18. Napisz dekorator mierzący czas wykonania funkcji.

## Poziom 4 — `*args`, `**kwargs` i zwracanie wyniku

19. Napisz dekorator działający na funkcji przyjmującej dowolną liczbę argumentów.
20. Napisz dekorator, który wypisuje argumenty pozycyjne i nazwane.
21. Napisz dekorator, który nie tylko wywołuje funkcję, ale też zwraca jej wynik.
22. Napisz dekorator blokujący wykonanie funkcji, jeśli pierwszy argument jest ujemny.
23. Udekoruj funkcję `dodaj(a, b)` i sprawdź, czy nadal poprawnie zwraca wynik.
24. Pokaż przykład błędnego dekoratora, który zapomina o `return wynik`.

## Poziom 5 — dekoratory z argumentami

25. Napisz dekorator `repeat(n)`, który uruchamia funkcję `n` razy.
26. Napisz dekorator `prefix(text)`, który wypisuje podany tekst przed funkcją.
27. Napisz dekorator `require_role(role)`, który symuluje sprawdzenie uprawnień.
28. Napisz dekorator `limit(max_calls)`, który pozwala wykonać funkcję tylko określoną liczbę razy.
29. Napisz dekorator `retry(times=3)`, który ponawia wykonanie funkcji po wyjątku.
30. Napisz dekorator z argumentem `debug=True/False`, który warunkowo loguje wywołanie.

## Poziom 6 — `functools.wraps`

31. Napisz dekorator bez `wraps` i sprawdź `__name__` udekorowanej funkcji.
32. Dodaj `@wraps` i porównaj efekt.
33. Sprawdź, co dzieje się z docstringiem funkcji bez `wraps` i z `wraps`.
34. Wypisz `__name__`, `__doc__` i `__module__` udekorowanej funkcji.
35. Napisz dekorator logujący, który poprawnie używa `wraps`.
36. Napisz dwa dekoratory: jeden poprawny z `wraps`, drugi celowo bez niego, i porównaj zachowanie.

## Poziom 7 — dekoratory klasowe i wbudowane

37. Napisz klasowy dekorator z `__call__`, który loguje wywołanie funkcji.
38. Napisz klasowy dekorator z licznikiem wywołań.
39. Pokaż prosty przykład użycia `@property`.
40. Pokaż prosty przykład użycia `@staticmethod`.
41. Pokaż prosty przykład użycia `@classmethod`.
42. Użyj `@functools.lru_cache` na funkcji rekurencyjnej i porównaj liczbę wywołań.

## Poziom 8 — praktyka i łączenie pomysłów

43. Napisz dekorator cache'ujący wyniki funkcji w zwykłym słowniku.
44. Napisz dekorator walidujący, że wszystkie liczby przekazane do funkcji są dodatnie.
45. Napisz dekorator, który zapisuje informację o wywołaniach do listy logów.
46. Zbuduj dekorator `timer`, a potem połącz go z dekoratorem `log_calls`.
47. Zrób dwa dekoratory i sprawdź, w jakiej kolejności działają po nałożeniu jeden na drugi.
48. Napisz funkcję udekorowaną kilkoma dekoratorami i wyjaśnij, co dzieje się krok po kroku.

## Poziom 9 — mini zadania projektowe

49. Zbuduj prosty system rejestracji komend, gdzie dekorator dodaje funkcję do słownika `commands`.
50. Zbuduj prosty dekorator `@route("/home")`, który zapisuje endpoint do słownika tras.
51. Napisz dekorator `@require_login`, który blokuje wykonanie funkcji bez ustawionej flagi `logged_in`.
52. Napisz dekorator `@validate_types`, który sprawdza typy wybranych argumentów.
53. Zbuduj dekorator `@memoize` i użyj go do przyspieszenia obliczania Fibonacciego.
54. Napisz dekorator `@audit`, który zapisuje nazwę funkcji, argumenty i wynik do listy wpisów.

## Zadanie końcowe

55. Zbuduj mini zestaw dekoratorów dla małej aplikacji:

- `@log_calls`
- `@measure_time`
- `@require_positive`
- `@cache_result`
- `@retry`

Użyj ich na kilku funkcjach i pokaż, że rozumiesz:

- kolejność dekoratorów,
- działanie wrappera,
- `*args, **kwargs`,
- `wraps`,
- skutki uboczne dekorowania,
- różnicę między dekoratorem prostym a dekoratorem z argumentami.
