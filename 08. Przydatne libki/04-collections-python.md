# `collections` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co używać `collections`](#po-co-używać-collections)
3. [`Counter`](#counter)
4. [`defaultdict`](#defaultdict)
5. [`deque`](#deque)
6. [`namedtuple`](#namedtuple)
7. [`OrderedDict`](#ordereddict)
8. [`ChainMap`](#chainmap)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczne przykłady](#praktyczne-przykłady)
11. [Dobre praktyki](#dobre-praktyki)
12. [Podsumowanie](#podsumowanie)
13. [Mini ściąga](#mini-ściąga)
14. [Ćwiczenia](#ćwiczenia)
15. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`collections` to moduł z wyspecjalizowanymi strukturami danych.

Pomaga pisać kod krócej, czytelniej i bardziej idiomatycznie.

To jeden z najbardziej praktycznych modułów w codziennej pracy.

---

## Po co używać `collections`

Zamiast samodzielnie budować typowe wzorce, możesz użyć gotowych narzędzi:

- liczenie elementów,
- słowniki z wartościami domyślnymi,
- wydajne kolejki,
- lekkie rekordy danych.

---

## `Counter`

Liczy wystąpienia elementów.

```python
from collections import Counter

licznik = Counter(["a", "b", "a", "c", "a"])
print(licznik)
print(licznik["a"])
```

To świetne do prostych analiz danych.

Wynik:

```python
Counter({'a': 3, 'b': 1, 'c': 1})
3
```

---

## `defaultdict`

Pozwala ustawić domyślny typ wartości.

```python
from collections import defaultdict

d = defaultdict(list)
d["owoce"].append("jablko")
print(d)
```

Nie musisz wcześniej sprawdzać, czy klucz istnieje.

Wynik:

```python
defaultdict(<class 'list'>, {'owoce': ['jablko']})
```

---

## `deque`

Dwukierunkowa kolejka.

```python
from collections import deque

q = deque([1, 2, 3])
q.append(4)
q.appendleft(0)
print(q)
```

Jest bardzo wydajna przy dodawaniu i usuwaniu z obu końców.

Wynik:

```python
deque([0, 1, 2, 3, 4])
```

---

## `namedtuple`

Lekki rekord z nazwanymi polami.

```python
from collections import namedtuple

Punkt = namedtuple("Punkt", ["x", "y"])
p = Punkt(2, 3)
print(p.x, p.y)
```

Wynik:

```python
2 3
```

To starszy, ale nadal spotykany wzorzec.

---

## `OrderedDict`

Historycznie słownik zachowujący kolejność.

Dziś zwykły `dict` w nowoczesnym Pythonie zachowuje kolejność wstawiania, więc `OrderedDict` jest mniej potrzebny, ale nadal pojawia się w niektórych przypadkach i starszym kodzie.

---

## `ChainMap`

Pozwala traktować kilka słowników jak jedną logiczną całość.

```python
from collections import ChainMap

a = {"x": 1}
b = {"y": 2}

c = ChainMap(a, b)
print(c["x"])
print(c["y"])
```

Wynik:

```python
1
2
```

---

## Typowe błędy początkujących

- ręczne zliczanie tam, gdzie `Counter` zrobi to prościej,
- używanie zwykłej listy zamiast `deque` jako kolejki,
- brak świadomości, że `defaultdict` tworzy domyślne wartości automatycznie,
- nadużywanie `namedtuple` tam, gdzie lepszy jest `dataclass`.

### 5. Używanie specjalnej struktury bez potrzeby

Nie każda sytuacja wymaga `Counter` albo `deque`. Czasem zwykły `dict` lub `list` w zupełności wystarczy.

---

## Praktyczne przykłady

### Najczęstsze słowa

```python
from collections import Counter

slowa = "ala ma kota ala ma psa ala".split()
print(Counter(slowa).most_common(2))
```

Wynik:

```python
[('ala', 3), ('ma', 2)]
```

### Grupowanie wartości

```python
from collections import defaultdict

grupy = defaultdict(list)

for nazwa, kategoria in [("jablko", "owoce"), ("marchew", "warzywa")]:
    grupy[kategoria].append(nazwa)

print(grupy)
```

Wynik:

```python
defaultdict(<class 'list'>, {'owoce': ['jablko'], 'warzywa': ['marchew']})
```

---

## Dobre praktyki

- wybieraj strukturę danych do problemu,
- `Counter` używaj do zliczeń,
- `defaultdict` do grupowania,
- `deque` do kolejek i buforów,
- nie komplikuj kodu, jeśli zwykły `dict` lub `list` już wystarczają.

Praktyczna zasada:

najpierw zapytaj: „jaki problem rozwiązuję?”, a dopiero potem wybierz strukturę z `collections`.

---

## Podsumowanie

`collections` daje bardzo praktyczne rozszerzenia podstawowych struktur danych.

To moduł, który naprawdę warto znać, bo często pozwala zamienić kilka linijek nieczytelnego kodu w jedną klarowną konstrukcję.

Najważniejsze do zapamiętania:

- `Counter` liczy,
- `defaultdict` upraszcza grupowanie,
- `deque` jest świetne do kolejek,
- `collections` często pozwala pisać krócej i czytelniej niż ręczne konstrukcje.

---

## Mini ściąga

```python
from collections import Counter, defaultdict, deque
```

Najważniejsze:

- `Counter` liczy,
- `defaultdict` daje domyślne wartości,
- `deque` działa dobrze jako kolejka,
- `namedtuple` tworzy lekki rekord.

---

## Ćwiczenia

1. Policz litery w napisie przez `Counter`.
2. Zgrupuj elementy listy według kategorii przez `defaultdict(list)`.
3. Zaimplementuj prostą kolejkę przez `deque`.
4. Utwórz `namedtuple` opisujący punkt.
5. Połącz dwa słowniki logicznie przez `ChainMap`.

---

## Przykładowe rozwiązania

### 1. Liczenie liter

```python
from collections import Counter

print(Counter("banan"))
```

### 2. Grupowanie

```python
from collections import defaultdict

d = defaultdict(list)
d["owoce"].append("banan")
print(d)
```

### 3. Kolejka

```python
from collections import deque

q = deque()
q.append("zadanie1")
print(q.popleft())
```

### 4. Punkt

```python
from collections import namedtuple

Punkt = namedtuple("Punkt", ["x", "y"])
print(Punkt(1, 2))
```

### 5. `ChainMap`

```python
from collections import ChainMap

cm = ChainMap({"x": 1}, {"y": 2})
print(cm["y"])
```
