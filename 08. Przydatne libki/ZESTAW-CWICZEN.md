# Zestaw ćwiczeń praktycznych — 08. Przydatne libki

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

## Poziom 2 — `itertools`

11. Połącz kilka list przez `chain()`.
12. Pobierz pierwsze 10 elementów z `count()`.
13. Wygeneruj wszystkie pary z dwóch list przez `product()`.
14. Wygeneruj wszystkie kombinacje 2-elementowe.
15. Użyj `groupby()` na posortowanych danych.
16. Użyj `cycle()` do powtarzania małego wzorca.
17. Użyj `islice()` do wycięcia fragmentu iteratora.
18. Wygeneruj wszystkie permutacje trzech liter.
19. Użyj `zip_longest()` na listach różnej długości.
20. Zbuduj mały pipeline iteratorów z `chain()` i `filter()`.

## Poziom 3 — `functools`

21. Użyj `partial()` do utworzenia funkcji `kwadrat`.
22. Użyj `reduce()` do policzenia sumy listy.
23. Napisz dekorator z `wraps`.
24. Dodaj `lru_cache` do funkcji Fibonacciego.
25. Użyj `cached_property` w małej klasie.
26. Napisz funkcję z `singledispatch`, która inaczej obsługuje `int` i `str`.
27. Użyj `partial()` do wstępnego ustawienia argumentu funkcji logującej.
28. Porównaj funkcję z cache i bez cache na małym przykładzie.
29. Użyj `reduce()` do połączenia listy stringów w jeden napis.
30. Pokaż różnicę między dekoratorem z `wraps` i bez `wraps`.

## Poziom 4 — `collections`

31. Użyj `Counter` do policzenia słów w tekście.
32. Użyj `defaultdict(list)` do grupowania rekordów.
33. Użyj `deque` do zbudowania kolejki.
34. Użyj `ChainMap` do nałożenia dwóch konfiguracji.
35. Użyj `namedtuple` do opisu punktu lub użytkownika.
36. Użyj `Counter.most_common()` do znalezienia najczęstszych elementów.
37. Użyj `deque` jako stosu i jako kolejki.
38. Użyj `defaultdict(int)` do liczenia wystąpień.
39. Pokaż prosty przykład `OrderedDict` albo wyjaśnij, czemu dziś bywa mniej potrzebny.
40. Napisz mały przykład z `ChainMap`, gdzie jedna konfiguracja nadpisuje drugą.

## Poziom 5 — `typing`

41. Dodaj typy do kilku prostych funkcji.
42. Utwórz `TypedDict` dla obiektu JSON użytkownika.
43. Użyj `Literal` dla trybu `dev/prod`.
44. Użyj `Optional` albo `X | None` w funkcji zwracającej brak wyniku.
45. Użyj `list[str]` albo `List[str]` w adnotacji listy.
46. Zdefiniuj alias typu dla listy rekordów.
47. Napisz funkcję generyczną przyjmującą listę elementów tego samego typu.
48. Dodaj typowanie do słownika konfiguracji.
49. Użyj `Protocol` albo opisz prosty przypadek, gdzie interfejs po zachowaniu ma sens.
50. Oznacz callback przyjmujący funkcję przez `Callable`.

## Poziom 6 — `dataclasses`

51. Zbuduj `dataclass` `User` z kilkoma polami.
52. Dodaj `default_factory` do listy tagów.
53. Dodaj `__post_init__` z prostą walidacją.
54. Użyj `repr` dataclass i zobacz, jak wygląda wynik.
55. Użyj `eq=True` i porównaj dwa obiekty.
56. Dodaj pole opcjonalne z domyślną wartością `None`.
57. Zbuduj `dataclass` `Product` z metodą liczącą cenę brutto.
58. Użyj `asdict()` do zamiany obiektu na słownik.
59. Użyj `frozen=True` i zobacz, co się stanie przy próbie zmiany pola.
60. Porównaj prostą klasę ręczną i klasę opartą o `dataclass`.

## Poziom 7 — zadania przekrojowe

61. Napisz parser prostych logów:
użyj `re` do wyciągnięcia pól i `dataclass` do modelu danych.
62. Zgrupuj wpisy po poziomie logowania przez `defaultdict(list)`.
63. Policz najczęstsze komunikaty przez `Counter`.
64. Użyj `typing` do opisania funkcji parsera.
65. Użyj `itertools` do przetworzenia wielu kolekcji wpisów w jeden strumień.
66. Dodaj cache do kosztownej funkcji analitycznej przez `lru_cache`.
67. Zbuduj mały system konfiguracji oparty o `ChainMap` i `TypedDict`.

## Zadanie końcowe

68. Zbuduj mini moduł przetwarzania zamówień:

- walidacja tekstu przez `re`,
- grupowanie danych przez `defaultdict`,
- analiza częstości przez `Counter`,
- typowanie funkcji,
- `dataclass` dla modelu danych,
- `cached_property` albo `partial` w sensownym miejscu.

Pokaż przy tym, że rozumiesz:

- kiedy regex ma sens, a kiedy wystarczy prostsza metoda,
- kiedy iterator z `itertools` daje wartość,
- jak `functools` upraszcza kod,
- po co istnieje `typing`,
- czemu `dataclass` przyspiesza modelowanie danych.
