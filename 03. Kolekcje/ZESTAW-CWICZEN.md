# Zestaw ćwiczeń praktycznych — 03. Kolekcje

Ten zestaw jest ułożony warstwowo.

Najpierw ćwiczysz podstawowe operacje, potem przechodzisz do mutowalności, kopiowania, comprehension i generatorów, a na końcu do bardziej zaawansowanych kolekcji z `collections`.

## Jak pracować z zadaniami

Najlepszy tryb pracy:

1. najpierw spróbuj sam,
2. potem uruchom kod na małych danych,
3. sprawdź edge case:
   - pusta lista,
   - brakujący klucz,
   - duplikaty,
   - wartości `0`, `""`, `None`,
4. dopiero na końcu porównaj z materiałem.

## Poziom 1 — listy, tuple, dict, set

1. Utwórz listę 10 liczb i wypisz:
   - pierwszy element,
   - ostatni element,
   - trzy pierwsze elementy,
   - elementy od indeksu `2` do `6`,
   - elementy co drugi.
2. Dodaj element do listy przez `append()`, potem przez `insert()`, a na końcu usuń jeden element przez `remove()` i jeden przez `pop()`.
3. Posortuj listę rosnąco i malejąco. Pokaż różnicę między `sort()` i `sorted()`.
4. Utwórz krotkę z danymi użytkownika i rozpakuj ją do osobnych zmiennych.
5. Zbuduj tuple jednoelementowe i pokaż różnicę między `(5)` a `(5,)`.
6. Utwórz słownik użytkownika i wypisz:
   - wszystkie klucze,
   - wszystkie wartości,
   - wszystkie pary klucz-wartość.
7. Dodaj nowy klucz do słownika, zmień istniejący i usuń wybrany klucz.
8. Utwórz dwa zbiory i pokaż:
   - sumę,
   - część wspólną,
   - różnicę,
   - różnicę symetryczną.
9. Usuń duplikaty z listy przy pomocy `set`, a potem zastanów się, co stało się z kolejnością.
10. Napisz funkcję, która przyjmuje listę i zwraca słownik z informacją:
   - ile jest elementów,
   - jaki jest pierwszy element,
   - jaki jest ostatni element,
   - czy lista zawiera duplikaty.

## Poziom 2 — mutowalność i kopiowanie

11. Pokaż na przykładzie, że przypisanie `b = a` nie tworzy kopii listy.
12. Zrób płytką kopię listy trzema sposobami:
   - `copy()`,
   - slicing,
   - `list(...)`.
13. Pokaż, że przy liście zagnieżdżonej płytka kopia nadal współdzieli wewnętrzne listy.
14. Napraw poprzedni przykład przez `copy.deepcopy()`.
15. Napisz przykład pokazujący różnicę między mutowalnością listy i niemutowalnością tuple.
16. Pokaż pułapkę z domyślnym argumentem funkcji będącym pustą listą.
17. Zbuduj macierz `3x3` błędnym sposobem przez `[[0] * 3] * 3`, zmień jeden element i opisz, co się stało.
18. Zbuduj tę samą macierz poprawnie.

## Poziom 3 — comprehensions

19. Zbuduj listę kwadratów liczb od `1` do `20` przez list comprehension.
20. Zbuduj listę tylko liczb parzystych od `1` do `30`.
21. Z listy słów zbuduj listę ich długości.
22. Z listy słów wybierz tylko te, których długość jest większa niż `5`.
23. Zbuduj listę etykiet `["parzysta", "nieparzysta", ...]` dla liczb od `1` do `10`.
24. Utwórz słownik `{liczba: liczba**2}` dla liczb od `1` do `10`.
25. Utwórz słownik tylko dla liczb parzystych.
26. Z napisu utwórz zbiór unikalnych liter przez set comprehension.
27. Przepisz krótki kod z pętlą `for` na comprehension, a potem oceń, czy nowa wersja jest czytelniejsza.

## Poziom 4 — zagnieżdżone comprehensions i generatory

28. Napisz nested comprehension tworzące macierz `3x3`.
29. Spłaszcz listę zagnieżdżoną `[[1, 2], [3, 4], [5, 6]]` do jednej listy.
30. Zbuduj listę wszystkich par `(x, y)` dla `x` i `y` z zakresu `0..2`.
31. Z tej listy par wybierz tylko te, dla których `x != y`.
32. Utwórz generator expression dla kwadratów liczb od `1` do `10`.
33. Przejdź po generatorze w pętli `for`.
34. Pokaż, że po zużyciu generatora drugi raz nie zwraca już danych.
35. Użyj generator expression razem z:
   - `sum()`,
   - `max()`,
   - `any()`,
   - `all()`.
36. Porównaj na małym przykładzie list comprehension i generator expression:
   - co zwraca `print(...)`,
   - czy można przejść po wyniku wiele razy,
   - czy dane są tworzone od razu.

## Poziom 5 — protokoły kolekcji i własne iterowalne obiekty

37. Sprawdź przez `isinstance`, czy:
   - lista jest `Iterable`,
   - string jest `Sequence`,
   - dict jest `Mapping`,
   - set jest `Sequence`.
38. Napisz klasę, która przechowuje listę liczb i implementuje `__iter__()`.
39. Rozszerz ją o `__len__()`.
40. Rozszerz ją o `__getitem__()`, aby działało indeksowanie.
41. Dodaj `__contains__()`, aby działało `in`.
42. Napisz klasę `Oceny`, która pozwala:
   - iterować po ocenach,
   - policzyć liczbę ocen przez `len()`,
   - pobrać ocenę po indeksie.

## Poziom 6 — `Counter`, `defaultdict`, `deque`, `ChainMap`, `namedtuple`

43. Użyj `Counter` do policzenia liter w napisie.
44. Użyj `Counter.most_common()` do znalezienia 3 najczęstszych słów w tekście.
45. Napisz ręczne liczenie wystąpień przez zwykły słownik i porównaj z `Counter`.
46. Użyj `defaultdict(list)` do grupowania produktów po kategorii.
47. Użyj `defaultdict(set)` do grupowania unikalnych tagów po kategorii.
48. Użyj `defaultdict(int)` do policzenia ocen lub znaków w tekście.
49. Użyj `deque` jako kolejki FIFO.
50. Użyj `deque` jako stosu LIFO.
51. Zbuduj historię ostatnich 5 działań przez `deque(maxlen=5)`.
52. Pokaż pułapkę `extendleft()` i opisz kolejność dodawania.
53. Użyj `ChainMap` do połączenia konfiguracji:
   - domyślnej,
   - użytkownika,
   - lokalnej.
54. Pokaż, że zapis do `ChainMap` trafia do pierwszego słownika.
55. Utwórz `namedtuple` opisujący punkt 2D lub użytkownika i pokaż:
   - dostęp po nazwie pola,
   - dostęp po indeksie,
   - `_asdict()`,
   - `_replace()`.

## Poziom 7 — praktyka projektowa

56. Napisz funkcję, która przyjmuje listę słowników i zwraca listę unikalnych wartości wybranego pola.
57. Napisz funkcję grupującą rekordy po kluczu i liczącą ich liczbę.
58. Zaimplementuj prostą kolejkę zadań przez `deque`.
59. Zbuduj analizator koszyka zakupowego:
   - lista produktów,
   - liczność produktów,
   - unikalne produkty,
   - grupowanie po kategorii.
60. Zbuduj prostą analizę tekstu:
   - liczba słów,
   - liczba unikalnych słów,
   - top 10 najczęstszych słów,
   - podział słów po długości.

---

## Poziom 8 — zadania przekrojowe

61. Zbuduj porównanie trzech sposobów reprezentacji tych samych danych:
   - lista krotek,
   - lista słowników,
   - słownik słowników,
   i opisz plusy oraz minusy każdego podejścia.
62. Napisz program, który analizuje tekst i korzysta jednocześnie z:
   - `split()`,
   - `set`,
   - `Counter`,
   - `sorted()`.
63. Zbuduj prosty system ocen uczniów:
   - słownik uczniów,
   - listy ocen,
   - średnie,
   - ranking przez `sorted()`,
   - wykrycie braków danych.
64. Zrób mini menedżer historii operacji:
   - przechowuje ostatnie 10 działań w `deque`,
   - liczy typy działań przez `Counter`,
   - grupuje działania po kategorii przez `defaultdict(list)`.
65. Napisz klasę własnej kolekcji, która:
   - przechowuje rekordy,
   - wspiera iterację,
   - wspiera `len()`,
   - wspiera odczyt po indeksie,
   - ma czytelne `__repr__()`.

## Zadanie końcowe

66. Zbuduj mini system analizy logów tekstowych:
   - wczytuje listę wpisów,
   - grupuje po poziomie logu,
   - liczy częstotliwości,
   - przechowuje ostatnie `N` wpisów,
   - korzysta z `Counter`, `defaultdict`, `deque`, comprehension i generatorów.

67. Zbuduj mini system “magazyn danych”, który:
   - przechowuje produkty w słownikach,
   - grupuje je po kategorii,
   - liczy częstotliwość tagów,
   - wykrywa duplikaty,
   - używa `set`, `dict`, `Counter`, `defaultdict`, `sorted()` i comprehension.

## Jak ocenić, czy umiesz ten folder

Jeśli potrafisz bez większego stresu rozwiązać zadania do poziomu 5, to masz już naprawdę porządne podstawy.

Jeśli robisz też poziom 6 i zadania przekrojowe, to folder `03` masz opanowany solidnie, a nie tylko “na czuja”.
