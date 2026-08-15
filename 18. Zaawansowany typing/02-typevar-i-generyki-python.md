# `TypeVar` i generyki w Pythonie

## O co chodzi

`TypeVar` i generyki pozwalają opisywać zależność między typem wejścia a typem wyjścia.

To jest kluczowa różnica względem prostych adnotacji.

Czasem nie chcesz powiedzieć tylko:

- funkcja przyjmuje `Any`,
- funkcja zwraca `Any`.

Chcesz powiedzieć coś znacznie precyzyjniejszego:

- funkcja zwraca dokładnie ten sam typ, który dostała,
- klasa przechowuje element dowolnego typu, ale konsekwentnie jednego typu,
- metoda zachowuje informację o typie danych.

## Najprostsza intuicja

Jeśli `Any` mówi:

- może być cokolwiek,

to `TypeVar` często mówi:

- może być dowolny typ, ale musi być spójny w danym użyciu.

## Prosty przykład: `identity`

```python
from typing import TypeVar

T = TypeVar("T")


def identity(value: T) -> T:
    return value
```

Teraz:

- jeśli podasz `int`, wynik ma typ `int`,
- jeśli podasz `str`, wynik ma typ `str`.

To dużo lepsze niż `Any`.

## Przykład użycia

```python
print(identity(10))
print(identity("Python"))
```

Output:

```python
10
Python
```

## Dlaczego `Any` byłoby gorsze

Gdybyś napisał:

```python
from typing import Any


def identity(value: Any) -> Any:
    return value
```

checker typów traci precyzyjną informację o związku wejścia i wyjścia.

## Generyczna funkcja zwracająca pierwszy element

```python
from typing import TypeVar

T = TypeVar("T")


def first_item(items: list[T]) -> T:
    return items[0]
```

Jeśli lista jest `list[str]`, wynik ma typ `str`.

Jeśli lista jest `list[int]`, wynik ma typ `int`.

## Generyczna klasa

```python
from typing import Generic, TypeVar

T = TypeVar("T")


class Box(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

    def get(self) -> T:
        return self.value
```

Przykład:

```python
int_box = Box(123)
str_box = Box("hello")
print(int_box.get())
print(str_box.get())
```

Output:

```python
123
hello
```

## Kiedy generyki mają sens

Szczególnie gdy:

- kontener ma działać dla wielu typów,
- funkcja ma zachować typ wejścia,
- budujesz narzędzie lub API wielokrotnego użytku,
- zależy Ci na precyzji typów bez duplikacji kodu.

## Kiedy nie komplikować na siłę

Jeśli funkcja i tak logicznie działa tylko na `str` albo tylko na `int`, to nie trzeba na siłę robić generyka.

Generyki są dla przypadków naprawdę ogólnych.

## `TypeVar` ograniczony

Czasem chcesz powiedzieć, że typ nie może być zupełnie dowolny.

Przykład ideowy:

- tylko `str` albo `bytes`,
- tylko klasy dziedziczące po `BaseModel`,
- tylko obiekty z określonym interfejsem.

To już bardziej zaawansowane użycie, ale warto wiedzieć, że `TypeVar` może być także ograniczany.

## Typowe błędy początkujących

- używanie `Any` tam, gdzie potrzebny jest związek typów,
- robienie generyków dla rzeczy, które wcale nie są ogólne,
- zbyt wczesne komplikowanie projektu,
- brak zrozumienia, że generyk służy zachowaniu informacji o typie.

## Mini scenariusz praktyczny

Masz helpery, kolekcje, kontenery, repozytoria, wrappery na wyniki albo funkcje narzędziowe.

To bardzo częste miejsca, gdzie `TypeVar` i generyki realnie poprawiają jakość API.

## Szybka ściąga

- `TypeVar` opisuje spójny dowolny typ,
- generyki pozwalają zachować informacje o typie między wejściem a wyjściem,
- `Any` jest znacznie mniej precyzyjne,
- generyki mają sens tam, gdzie API naprawdę jest ogólne.

## Ćwiczenia

1. Napisz funkcję `identity` przez `TypeVar`.
2. Napisz funkcję zwracającą ostatni element listy z zachowaniem typu.
3. Zrób klasę `Box[T]`.
4. Porównaj wersję generyczną i wersję z `Any`.
5. Wskaż 3 miejsca w projekcie, gdzie generyki miałyby sens.

## Najważniejsze do zapamiętania

- `TypeVar` pomaga zachować związek między typami w API.
- Generyki są dużo lepsze niż `Any`, gdy chcesz zachować precyzję.
- Dobrze sprawdzają się w kontenerach i funkcjach narzędziowych.
- Nie warto robić generyków tam, gdzie problem nie jest naprawdę ogólny.
- Największa wartość generyków to lepsza informacja o typie bez duplikowania kodu.
