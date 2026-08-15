# Zestaw ćwiczeń praktycznych — 08. Przydatne libki

W tym folderze szczególnie ważne jest porównywanie dwóch stylów rozwiązania:

- wersji ręcznej,
- wersji z użyciem biblioteki.

Dlatego przy wielu zadaniach warto zrobić oba warianty i odpowiedzieć sobie:

- które rozwiązanie jest krótsze,
- które jest czytelniejsze,
- które byłoby lepsze w prawdziwym projekcie.

## Poziom 1 — `re`

1. Znajdź pierwszą liczbę w tekście.
2. Znajdź wszystkie liczby w tekście.
3. Sprawdź, czy string ma format `ABC-123`.
4. Zamień wszystkie cyfry na `*`.
5. Wyciągnij rok, miesiąc i dzień z daty.
6. Wyciągnij wszystkie adresy e-mail z tekstu.
7. Sprawdź, czy hasło zawiera przynajmniej jedną cyfrę.
8. Rozbij tekst po wielu białych znakach przez `re.split()`.
9. Użyj grup nazwanych do wyciągnięcia danych z prostego logu.
10. Zastąp wiele spacji jedną spacją.
11. Dla 3 wybranych problemów pokaż też wersję bez regexu i porównaj, która jest lepsza.

## Poziom 2 — `itertools`

12. Połącz kilka list przez `chain()`.
13. Pobierz pierwsze 10 elementów z `count()`.
14. Wygeneruj wszystkie pary z dwóch list przez `product()`.
15. Wygeneruj wszystkie kombinacje 2-elementowe.
16. Użyj `groupby()` na posortowanych danych.
17. Użyj `cycle()` do powtarzania małego wzorca.
18. Użyj `islice()` do wycięcia fragmentu iteratora.
19. Wygeneruj wszystkie permutacje trzech liter.
20. Użyj `zip_longest()` na listach różnej długości.
21. Zbuduj mały pipeline iteratorów z `chain()` i `filter()`.
22. Dla 3 zadań pokaż też prostą wersję na pętli i porównaj czytelność.

## Poziom 3 — `functools`

23. Użyj `partial()` do utworzenia funkcji `kwadrat`.
24. Użyj `reduce()` do policzenia sumy listy.
25. Napisz dekorator z `wraps`.
26. Dodaj `lru_cache` do funkcji Fibonacciego.
27. Użyj `cached_property` w małej klasie.
28. Napisz funkcję z `singledispatch`, która inaczej obsługuje `int` i `str`.
29. Użyj `partial()` do wstępnego ustawienia argumentu funkcji logującej.
30. Porównaj funkcję z cache i bez cache na małym przykładzie.
31. Użyj `reduce()` do połączenia listy stringów w jeden napis.
32. Pokaż różnicę między dekoratorem z `wraps` i bez `wraps`.
33. Wskaż 3 przypadki, gdzie zwykła funkcja lub `sum()` są lepsze niż `partial()` albo `reduce()`.

## Poziom 4 — `collections`

34. Użyj `Counter` do policzenia słów w tekście.
35. Użyj `defaultdict(list)` do grupowania rekordów.
36. Użyj `deque` do zbudowania kolejki.
37. Użyj `ChainMap` do nałożenia dwóch konfiguracji.
38. Użyj `namedtuple` do opisu punktu lub użytkownika.
39. Użyj `Counter.most_common()` do znalezienia najczęstszych elementów.
40. Użyj `deque` jako stosu i jako kolejki.
41. Użyj `defaultdict(int)` do liczenia wystąpień.
42. Pokaż prosty przykład `OrderedDict` albo wyjaśnij, czemu dziś bywa mniej potrzebny.
43. Napisz mały przykład z `ChainMap`, gdzie jedna konfiguracja nadpisuje drugą.
44. Dla 3 przypadków pokaż, jak wyglądałoby ręczne rozwiązanie zwykłym `dict` lub `list`.

## Poziom 5 — `typing`

45. Dodaj typy do kilku prostych funkcji.
46. Utwórz `TypedDict` dla obiektu JSON użytkownika.
47. Użyj `Literal` dla trybu `dev/prod`.
48. Użyj `Optional` albo `X | None` w funkcji zwracającej brak wyniku.
49. Użyj `list[str]` albo `List[str]` w adnotacji listy.
50. Zdefiniuj alias typu dla listy rekordów.
51. Napisz funkcję generyczną przyjmującą listę elementów tego samego typu.
52. Dodaj typowanie do słownika konfiguracji.
53. Użyj `Protocol` albo opisz prosty przypadek, gdzie interfejs po zachowaniu ma sens.
54. Oznacz callback przyjmujący funkcję przez `Callable`.
55. Dla 3 funkcji opisz, co konkretnie dają typy ponad sam kod bez adnotacji.

## Poziom 6 — `dataclasses`

56. Zbuduj `dataclass` `User` z kilkoma polami.
57. Dodaj `default_factory` do listy tagów.
58. Dodaj `__post_init__` z prostą walidacją.
59. Użyj `repr` dataclass i zobacz, jak wygląda wynik.
60. Użyj `eq=True` i porównaj dwa obiekty.
61. Dodaj pole opcjonalne z domyślną wartością `None`.
62. Zbuduj `dataclass` `Product` z metodą liczącą cenę brutto.
63. Użyj `asdict()` do zamiany obiektu na słownik.
64. Użyj `frozen=True` i zobacz, co się stanie przy próbie zmiany pola.
65. Porównaj prostą klasę ręczną i klasę opartą o `dataclass`.
66. Dla 3 przykładów odpowiedz, czy lepsza będzie `dataclass`, zwykły `dict`, czy zwykła klasa.

## Poziom 7 — zadania przekrojowe

67. Napisz parser prostych logów:
- użyj `re` do wyciągnięcia pól,
- `dataclass` do modelu danych,
- `typing` do opisania funkcji.

68. Zgrupuj wpisy po poziomie logowania przez `defaultdict(list)`.
69. Policz najczęstsze komunikaty przez `Counter`.
70. Użyj `itertools` do przetworzenia wielu kolekcji wpisów w jeden strumień.
71. Dodaj cache do kosztownej funkcji analitycznej przez `lru_cache`.
72. Zbuduj mały system konfiguracji oparty o `ChainMap` i `TypedDict`.
73. Zbuduj prostą analizę zamówień, gdzie część rozwiązań piszesz ręcznie, a część przez standardową bibliotekę, i porównujesz oba style.
74. Weź 5 problemów z tego folderu i dla każdego dopisz jedno zdanie: „dlaczego tutaj używam biblioteki zamiast zwykłej pętli/prostego kodu”.

## Zadanie końcowe

75. Zbuduj mini moduł przetwarzania zamówień lub logów, w którym połączysz co najmniej 4 biblioteki z tego folderu.

Minimalne wymagania:

- walidacja lub ekstrakcja tekstu przez `re`,
- grupowanie danych przez `defaultdict`,
- analiza częstości przez `Counter`,
- typowanie funkcji,
- `dataclass` dla modelu danych,
- przynajmniej jeden sensowny element z `itertools` albo `functools`.

Na końcu opisz:

- gdzie biblioteki uprościły kod,
- gdzie zwykły Python byłby czytelniejszy,
- którego narzędzia użyłeś z największą korzyścią,
- gdzie najłatwiej byłoby przesadzić ze „sprytnym” kodem.
