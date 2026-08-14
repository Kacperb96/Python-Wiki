# `dataclasses` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co używać `dataclasses`](#po-co-używać-dataclasses)
3. [Najprostsza dataclass](#najprostsza-dataclass)
4. [Automatycznie generowane metody](#automatycznie-generowane-metody)
5. [Wartości domyślne](#wartości-domyślne)
6. [`field()`](#field)
7. [`default_factory`](#default_factory)
8. [`__post_init__`](#post_init)
9. [`frozen=True`](#frozentrue)
10. [Dataclass a zwykła klasa](#dataclass-a-zwykła-klasa)
11. [Typowe błędy początkujących](#typowe-błędy-początkujących)
12. [Praktyczne przykłady](#praktyczne-przykłady)
13. [Dobre praktyki](#dobre-praktyki)
14. [Podsumowanie](#podsumowanie)
15. [Mini ściąga](#mini-ściąga)
16. [Ćwiczenia](#ćwiczenia)
17. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`dataclasses` upraszczają tworzenie klas, które głównie przechowują dane.

Zamiast ręcznie pisać dużo powtarzalnego kodu, możesz użyć dekoratora `@dataclass`.

---

## Po co używać `dataclasses`

`dataclass` jest przydatna, gdy:

- klasa ma głównie pola danych,
- chcesz mieć czytelny konstruktor,
- zależy ci na automatycznym `repr`,
- chcesz prostszy i krótszy kod.

---

## Najprostsza dataclass

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
```

Teraz możesz zrobić:

```python
u = User("Anna", 30)
print(u)
```

---

## Automatycznie generowane metody

`@dataclass` domyślnie generuje m.in.:

- `__init__`,
- `__repr__`,
- `__eq__`.

To oszczędza dużo powtarzalnej pracy.

---

## Wartości domyślne

```python
from dataclasses import dataclass

@dataclass
class Config:
    debug: bool = False
    port: int = 8000
```

---

## `field()`

`field()` daje więcej kontroli nad polem.

```python
from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    tags: list[str] = field(default_factory=list)
```

---

## `default_factory`

To bardzo ważne przy mutowalnych wartościach domyślnych.

Zamiast:

```python
tags = []
```

używaj:

```python
field(default_factory=list)
```

To zapobiega współdzieleniu tej samej listy między instancjami.

---

## `__post_init__`

Jeśli po utworzeniu obiektu chcesz zrobić dodatkową logikę:

```python
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("price nie moze byc ujemne")
```

---

## `frozen=True`

Tworzy dataclass bardziej niemutowalną.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int
```

To przydatne przy obiektach konfiguracyjnych i value objects.

---

## Dataclass a zwykła klasa

Dataclass nie zastępuje każdej klasy.

Najlepiej pasuje tam, gdzie dominują dane.

Jeśli klasa ma dużo niestandardowego zachowania, zwykła klasa może być lepsza.

---

## Typowe błędy początkujących

- używanie mutowalnych wartości domyślnych bez `default_factory`,
- traktowanie dataclass jak magicznego rozwiązania do wszystkiego,
- brak walidacji danych tam, gdzie jest potrzebna,
- zapominanie, że `frozen=True` ogranicza modyfikacje pól.

---

## Praktyczne przykłady

### Model użytkownika

```python
from dataclasses import dataclass

@dataclass
class User:
    username: str
    email: str
    active: bool = True
```

### Lista tagów

```python
from dataclasses import dataclass, field

@dataclass
class Article:
    title: str
    tags: list[str] = field(default_factory=list)
```

---

## Dobre praktyki

- używaj `dataclass`, gdy klasa głównie przechowuje dane,
- dla mutowalnych domyślnych wartości używaj `default_factory`,
- dodawaj typy pól,
- używaj `__post_init__` do prostych walidacji i inicjalizacji pośredniej.

---

## Podsumowanie

`dataclasses` znacząco upraszczają kod modeli danych.

To bardzo praktyczne narzędzie, które dobrze łączy się z `typing`.

---

## Mini ściąga

```python
from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    tags: list[str] = field(default_factory=list)
```

Najważniejsze:

- `@dataclass` generuje boilerplate,
- pola definiujesz jak zwykłe atrybuty,
- `field(default_factory=...)` jest ważne dla list i dictów,
- `__post_init__` pozwala dodać logikę po inicjalizacji.

---

## Ćwiczenia

1. Utwórz dataclass `User` z polami `name` i `age`.
2. Dodaj pole z wartością domyślną.
3. Dodaj listę tagów przez `default_factory`.
4. Dodaj walidację ceny przez `__post_init__`.
5. Utwórz niemutowalną dataclass punktu.

---

## Przykładowe rozwiązania

### 1. `User`

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
```

### 2. Wartość domyślna

```python
from dataclasses import dataclass

@dataclass
class Config:
    debug: bool = False
```

### 3. Tagi

```python
from dataclasses import dataclass, field

@dataclass
class Note:
    tags: list[str] = field(default_factory=list)
```

### 4. Walidacja

```python
from dataclasses import dataclass

@dataclass
class Product:
    price: float

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("zla cena")
```

### 5. Punkt

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int
```
