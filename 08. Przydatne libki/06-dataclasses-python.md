# `dataclasses` w Pythonie

## Wprowadzenie

`dataclasses` upraszczają tworzenie klas, które głównie przechowują dane.

Zamiast ręcznie pisać dużo powtarzalnego kodu, możesz użyć dekoratora `@dataclass`.

To jedno z najbardziej praktycznych narzędzi nowoczesnego Pythona do modelowania prostych obiektów danych.

## Kiedy `dataclass` ma sens

`dataclass` jest świetna, gdy:

- klasa ma głównie pola danych,
- chcesz prosty konstruktor,
- chcesz automatyczny `repr`,
- chcesz porównywanie obiektów po wartościach,
- modelujesz DTO, config, rekord, value object.

## Kiedy zwykła klasa albo `dict` są lepsze

### Zwykła klasa

Lepsza, gdy klasa ma dużo własnego zachowania i mało danych.

### `dict`

Może wystarczyć, gdy dane są jednorazowe, bardzo luźne i nie potrzebujesz wyraźnego modelu.

`dataclass` ma sens wtedy, gdy chcesz nazwać strukturę danych i nadać jej porządną formę.

## Najprostsza dataclass

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

u = User("Anna", 30)
print(u)
```

Output:

```python
User(name='Anna', age=30)
```

## Automatycznie generowane metody

`@dataclass` domyślnie generuje m.in.:

- `__init__`,
- `__repr__`,
- `__eq__`.

```python
print(User("Anna", 30) == User("Anna", 30))
```

Output:

```python
True
```

## Wartości domyślne

```python
from dataclasses import dataclass

@dataclass
class Config:
    debug: bool = False
    port: int = 8000

print(Config())
```

Output:

```python
Config(debug=False, port=8000)
```

## `field()` i `default_factory`

To bardzo ważne przy mutowalnych wartościach domyślnych.

```python
from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    tags: list[str] = field(default_factory=list)
```

Każda instancja dostaje własną listę `tags`.

## `__post_init__`

Służy do dodatkowej logiki po utworzeniu obiektu.

```python
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("price nie moze byc ujemne")

print(Product("Kawa", 12.5))
```

Output:

```python
Product(name='Kawa', price=12.5)
```

## `frozen=True`

Tworzy dataclass bardziej niemutowalną.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int
```

To przydatne np. dla obiektów konfiguracyjnych albo value objects.

## `dataclass` vs zwykła klasa

### Gdy `dataclass` wygrywa

- model użytkownika,
- rekord zamówienia,
- wynik parsera,
- prosty config,
- obiekt danych z lekką walidacją.

### Gdy zwykła klasa wygrywa

- obiekt z bogatym zachowaniem,
- klasa zarządzająca procesem,
- serwis, który ma dużo metod i zależności.

### Gdy `dict` wystarczy

- bardzo prosty tymczasowy payload,
- krótki eksperyment,
- jednorazowa struktura bez potrzeby modelowania.

## `dataclass` a czytelność

Duża zaleta `dataclass` polega na tym, że od razu widać model danych.

Porównaj:

### Luźny `dict`

```python
user = {"name": "Anna", "age": 30}
```

### Jawny model

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
```

Drugi wariant zwykle lepiej komunikuje intencję w większym kodzie.

## Typowe błędy początkujących

- używanie mutowalnej wartości domyślnej bez `default_factory`,
- wciskanie `dataclass` do klas, które mają głównie zachowanie,
- brak walidacji w `__post_init__`, gdy dane tego wymagają,
- mylenie `dataclass` z pełnym OOP lub z ORM-em,
- używanie `dict` wszędzie, nawet gdy model danych już się prosi o nazwany typ.

## Mini scenariusz praktyczny

Masz parser logów albo moduł zamówień. Każdy wpis ma kilka pól: datę, poziom, komunikat, użytkownika.

`dataclass` świetnie nadaje się do reprezentowania takiego rekordu. Jest czytelniej niż na słownikach i lżej niż w rozbudowanym OOP.

## Dobre praktyki

- używaj `dataclass` dla obiektów danych,
- stosuj `default_factory` dla list i słowników,
- używaj `__post_init__`, gdy potrzebna jest lekka walidacja,
- nie wciskaj `dataclass` do każdej klasy,
- wybieraj model, który najlepiej komunikuje intencję.

## Szybka ściąga

Najczęściej przydatne:

- `@dataclass`,
- `field(default_factory=...)`,
- `__post_init__`,
- `frozen=True`.

## Ćwiczenia

1. Zrób `User` jako `dataclass`.
2. Dodaj listę tagów przez `default_factory`.
3. Dodaj walidację ceny w `__post_init__`.
4. Porównaj `dict`, zwykłą klasę i `dataclass` dla tego samego modelu.
5. Opisz 3 sytuacje, gdzie `dataclass` ma sens i 2, gdzie nie ma.

## Najważniejsze do zapamiętania

- `dataclass` upraszcza modelowanie klas przechowujących dane.
- Daje ogromnie dużo za małą ilość kodu.
- `default_factory` jest ważne przy mutowalnych polach.
- `dataclass` nie zastępuje każdej klasy i nie jest rozwiązaniem na wszystko.
- Najlepiej sprawdza się tam, gdzie dane są ważniejsze niż zachowanie.
