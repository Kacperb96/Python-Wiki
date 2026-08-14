# `typing` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co używać `typing`](#po-co-używać-typing)
3. [Adnotacje typów](#adnotacje-typów)
4. [Typy podstawowe](#typy-podstawowe)
5. [`list[str]`, `dict[str, int]` i nowoczesna składnia](#liststr-dictstr-int-i-nowoczesna-składnia)
6. [`Optional` i `Union`](#optional-i-union)
7. [`Any`](#any)
8. [`Callable`](#callable)
9. [`TypeAlias` i `Literal`](#typealias-i-literal)
10. [`TypedDict`](#typeddict)
11. [Typowe błędy początkujących](#typowe-błędy-początkujących)
12. [Praktyczne przykłady](#praktyczne-przykłady)
13. [Dobre praktyki](#dobre-praktyki)
14. [Podsumowanie](#podsumowanie)
15. [Mini ściąga](#mini-ściąga)
16. [Ćwiczenia](#ćwiczenia)
17. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`typing` wspiera statyczne typowanie w Pythonie.

Python nadal pozostaje językiem dynamicznym, ale adnotacje typów pomagają:

- czytać kod,
- łapać błędy wcześniej,
- lepiej wspierać IDE,
- ułatwiać utrzymanie większych projektów.

---

## Po co używać `typing`

Typy poprawiają komunikację między ludźmi i narzędziami.

Kod z dobrymi adnotacjami zwykle łatwiej zrozumieć i bezpieczniej rozwijać.

---

## Adnotacje typów

```python
def dodaj(a: int, b: int) -> int:
    return a + b
```

To nie wymusza typów w czasie działania samo z siebie, ale daje informacje narzędziom i programistom.

Przykład:

```python
print(dodaj(2, 3))
```

Wynik:

```python
5
```

---

## Typy podstawowe

Najczęstsze:

- `int`
- `str`
- `float`
- `bool`
- `list`
- `dict`

Przykład:

```python
imie: str = "Anna"
wiek: int = 30
```

---

## `list[str]`, `dict[str, int]` i nowoczesna składnia

Nowoczesny zapis:

```python
def przetworz(dane: list[str]) -> dict[str, int]:
    return {x: len(x) for x in dane}
```

To obecnie zwykle czytelniejsza forma niż starsze `List[str]` i `Dict[str, int]`.

Przykład:

```python
print(przetworz(["Ala", "Python"]))
```

Wynik:

```python
{'Ala': 3, 'Python': 6}
```

---

## `Optional` i `Union`

`Optional[str]` oznacza zwykle `str | None`.

```python
def znajdz() -> str | None:
    return None
```

To znaczy, że funkcja może zwrócić tekst albo brak wyniku.

`Union` oznacza kilka możliwych typów.

W nowoczesnym Pythonie często używa się składni z `|`.

---

## `Any`

`Any` oznacza brak konkretnej kontroli typu.

Jest przydatne czasem, ale nadużywane osłabia sens typowania.

---

## `Callable`

Do opisu funkcji przekazywanych jako argument:

```python
from typing import Callable

def uruchom(f: Callable[[int], int], x: int) -> int:
    return f(x)
```

Przykład:

```python
print(uruchom(lambda x: x * 2, 5))
```

Wynik:

```python
10
```

---

## `TypeAlias` i `Literal`

`TypeAlias` pomaga nazwać złożony typ.

`Literal` pozwala ograniczyć wartości do konkretnych wariantów.

```python
from typing import Literal, TypeAlias

UserId: TypeAlias = int

def ustaw_tryb(tryb: Literal["dev", "prod"]) -> None:
    print(tryb)
```

Przykład:

```python
ustaw_tryb("dev")
```

Wynik:

```python
dev
```

---

## `TypedDict`

Do opisu słowników o znanej strukturze.

```python
from typing import TypedDict

class User(TypedDict):
    name: str
    age: int
```

To bardzo przydatne przy danych JSON-like.

Przykład użycia:

```python
user: User = {"name": "Anna", "age": 30}
print(user["name"])
```

Wynik:

```python
Anna
```

---

## Typowe błędy początkujących

- mylenie adnotacji typów z walidacją runtime,
- używanie `Any` wszędzie,
- przesadne komplikowanie typów w prostym kodzie,
- brak aktualizacji adnotacji po zmianach logiki.

### 5. Traktowanie typowania jako celu samego w sobie

Typy mają pomagać w czytelności i bezpieczeństwie, a nie robić kod bardziej ciężkim niż potrzeba.

---

## Praktyczne przykłady

### Funkcja z listą napisów

```python
def policz_litery(slowa: list[str]) -> dict[str, int]:
    return {slowo: len(slowo) for slowo in slowa}
```

Przykład użycia:

```python
print(policz_litery(["kot", "pies"]))
```

Wynik:

```python
{'kot': 3, 'pies': 4}
```

### `TypedDict`

```python
from typing import TypedDict

class Product(TypedDict):
    name: str
    price: float
```

To jest szczególnie wygodne, gdy pracujesz na danych podobnych do JSON-a.

---

## Dobre praktyki

- typuj publiczne API funkcji i klas,
- nie komplikuj adnotacji bardziej niż to potrzebne,
- preferuj nowoczesną składnię typów,
- używaj `TypedDict` i `dataclass` tam, gdzie poprawia to czytelność danych.

Praktyczna zasada:

zacznij od prostych typów funkcji i zwracanych wartości. Nie próbuj od razu typować wszystkiego w najbardziej zaawansowany sposób.

---

## Podsumowanie

`typing` nie zmienia Pythona w język statyczny, ale znacząco poprawia jakość większego kodu.

Największa wartość to czytelność, lepsze narzędzia i wcześniejsze wykrywanie problemów.

Najważniejsze do zapamiętania:

- adnotacje typów nie są tym samym co walidacja w runtime,
- dobrze opisane typy pomagają ludziom i narzędziom,
- `TypedDict`, `Literal` i `Callable` rozwiązują bardzo praktyczne problemy.

---

## Mini ściąga

```python
def hello(name: str) -> str:
    return f"Hi {name}"
```

Najważniejsze:

- `a: int` opisuje typ,
- `-> str` opisuje typ zwracany,
- `str | None` oznacza opcjonalność,
- `Callable` opisuje funkcję,
- `TypedDict` opisuje strukturę słownika.

---

## Ćwiczenia

1. Dodaj typy do funkcji sumującej dwie liczby.
2. Opisz funkcję przyjmującą listę napisów.
3. Zwróć typ opcjonalny `str | None`.
4. Zdefiniuj `TypedDict` dla użytkownika.
5. Użyj `Literal` dla trybu pracy aplikacji.

---

## Przykładowe rozwiązania

### 1. Dodawanie

```python
def dodaj(a: int, b: int) -> int:
    return a + b
```

### 2. Lista napisów

```python
def polacz(slowa: list[str]) -> str:
    return " ".join(slowa)
```

### 3. Opcjonalny wynik

```python
def znajdz_user(user_id: int) -> str | None:
    return None
```

### 4. `TypedDict`

```python
from typing import TypedDict

class User(TypedDict):
    name: str
    age: int
```

### 5. `Literal`

```python
from typing import Literal

def ustaw_tryb(tryb: Literal["dev", "prod"]) -> None:
    print(tryb)
```
