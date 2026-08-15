# `collections` w Pythonie

## Wprowadzenie

`collections` to moduł z wyspecjalizowanymi strukturami danych.

Pomaga pisać kod:

- krócej,
- czytelniej,
- bardziej idiomatycznie,
- bez ręcznego budowania typowych wzorców.

To jeden z najbardziej praktycznych modułów w codziennej pracy.

## Kiedy `collections` ma sens

Używaj go, gdy potrzebujesz:

- liczenia wystąpień,
- słownika z wartościami domyślnymi,
- wydajnej kolejki,
- lekkiego rekordu danych,
- połączenia kilku warstw konfiguracji.

## Kiedy zwykły `dict` albo `list` wystarczą

Nie każde zadanie wymaga specjalnej struktury.

Jeśli masz bardzo prosty przypadek, zwykły `dict` albo `list` bywają najlepsze. `collections` ma sens wtedy, gdy realnie usuwa powtarzalny kod albo daje wyraźną przewagę semantyczną.

## `Counter`

Liczy wystąpienia elementów.

```python
from collections import Counter

counter = Counter(["a", "b", "a", "c", "a"])
print(counter)
print(counter["a"])
```

Output:

```python
Counter({'a': 3, 'b': 1, 'c': 1})
3
```

### Kiedy wybrać `Counter`

- analiza częstości,
- liczenie słów,
- liczenie znaków,
- ranking najczęstszych elementów.

### Kiedy zwykły `dict` wystarczy

Jeśli liczysz dosłownie 2-3 rzeczy w jednorazowym prostym kodzie, ręczne liczenie też może być OK. W praktyce jednak `Counter` często jest po prostu lepszy.

## `defaultdict`

Pozwala ustawić domyślny typ wartości.

```python
from collections import defaultdict

d = defaultdict(list)
d["owoce"].append("jablko")
print(d)
```

Output:

```python
defaultdict(<class 'list'>, {'owoce': ['jablko']})
```

### Kiedy wybrać `defaultdict`

- grupowanie rekordów,
- liczenie wystąpień,
- budowanie map klucz -> lista wartości.

### Porównanie ze zwykłym `dict`

Zwykły `dict` wymaga częściej kodu w stylu:

```python
if key not in data:
    data[key] = []
```

`defaultdict` usuwa ten boilerplate.

## `deque`

Dwukierunkowa kolejka.

```python
from collections import deque

q = deque([1, 2, 3])
q.append(4)
q.appendleft(0)
print(q)
```

Output:

```python
deque([0, 1, 2, 3, 4])
```

### Kiedy wybrać `deque`

- kolejka FIFO,
- stos,
- operacje z obu końców,
- przesuwające się okno danych.

### Kiedy zwykła lista jest gorsza

Lista nie jest dobrym wyborem, gdy często usuwasz elementy z początku.

## `namedtuple`

Lekki rekord z nazwanymi polami.

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(2, 3)
print(p.x, p.y)
```

Output:

```python
2 3
```

### Kiedy ma sens

- prosty lekki rekord,
- starszy kod,
- sytuacje, gdzie nie potrzebujesz pełnej `dataclass`.

### Kiedy lepsza jest `dataclass`

Jeśli chcesz:

- łatwiejszą rozbudowę,
- domyślne wartości,
- `__post_init__`,
- wyraźniejsze modelowanie danych,

to `dataclass` bywa lepszym wyborem.

## `OrderedDict`

Historycznie był ważniejszy, bo zwykły `dict` nie gwarantował kolejności.

Dziś zwykły `dict` w nowoczesnym Pythonie zachowuje kolejność wstawiania, więc `OrderedDict` jest mniej potrzebny, ale nadal można go spotkać w starszym kodzie i niektórych wyspecjalizowanych przypadkach.

## `ChainMap`

Pozwala traktować kilka słowników jak jedną logiczną całość.

```python
from collections import ChainMap

base = {"host": "localhost", "port": 8000}
override = {"port": 9000}
config = ChainMap(override, base)

print(config["host"])
print(config["port"])
```

Output:

```python
localhost
9000
```

### Kiedy wybrać `ChainMap`

- konfiguracja z kilku warstw,
- domyślne wartości + nadpisania,
- wiele słowników widzianych jako jedna całość.

### Kiedy wystarczy zwykłe scalanie

Jeśli robisz jednorazowe złączenie dwóch małych słowników, zwykłe `a | b` albo `merged = {**a, **b}` też może wystarczyć.

## `collections` vs ręczny kod

### Gdy biblioteka wygrywa

- `Counter` zamiast ręcznego liczenia,
- `defaultdict(list)` zamiast ciągłego sprawdzania kluczy,
- `deque` zamiast listy jako kolejki,
- `ChainMap` przy kilku warstwach konfiguracji.

### Gdy prosty kod wygrywa

- mały jednorazowy `dict`,
- prosta lista bez intensywnych operacji z początku,
- zwykła krotka lub `dict`, jeśli nie potrzebujesz specjalnej semantyki.

## Typowe błędy początkujących

- ręczne zliczanie tam, gdzie `Counter` jest oczywistszy,
- używanie listy jako kolejki,
- nadużywanie specjalnych struktur bez potrzeby,
- brak świadomości, że `defaultdict` tworzy wartości automatycznie,
- używanie `namedtuple`, gdy `dataclass` byłaby czytelniejsza.

## Mini scenariusz praktyczny

Masz listę zamówień i chcesz:

- policzyć najczęstsze produkty,
- pogrupować zamówienia po kliencie,
- mieć kolejkę zadań,
- połączyć config domyślny z lokalnym.

To jest dokładnie teren, na którym `collections` robi ogromną różnicę względem ręcznego kodu.

## Dobre praktyki

- dobieraj strukturę do problemu,
- nie wymyślaj ręcznie tego, co standardowa biblioteka robi lepiej,
- wybieraj strukturę, która czytelnie komunikuje zamiar,
- nie używaj specjalnej struktury bez realnej korzyści.

## Szybka ściąga

Najczęściej przydatne:

- `Counter` — liczenie,
- `defaultdict` — domyślne wartości,
- `deque` — kolejka/stos,
- `namedtuple` — lekki rekord,
- `ChainMap` — widok na kilka słowników.

## Ćwiczenia

1. Policz słowa przez `Counter` i ręcznie, a potem porównaj.
2. Zgrupuj rekordy przez `defaultdict(list)`.
3. Zbuduj kolejkę przez `deque`.
4. Nałóż konfiguracje przez `ChainMap`.
5. Porównaj `namedtuple` i `dataclass` na prostym modelu danych.

## Najważniejsze do zapamiętania

- `collections` daje bardzo praktyczne struktury danych do codziennego kodu.
- `Counter`, `defaultdict` i `deque` to jedne z najbardziej użytecznych narzędzi modułu.
- Specjalna struktura ma sens wtedy, gdy usuwa boilerplate lub poprawia semantykę.
- Nie każde zadanie wymaga `collections`.
- Dobra struktura danych często upraszcza cały kod bardziej niż „sprytna” logika.
