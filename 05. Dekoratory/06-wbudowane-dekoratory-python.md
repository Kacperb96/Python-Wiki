# Wbudowane dekoratory w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [`@property`](#property)
3. [`@staticmethod`](#staticmethod)
4. [`@classmethod`](#classmethod)
5. [`@functools.lru_cache`](#functoolslru_cache)
6. [Dlaczego te dekoratory są tak ważne](#dlaczego-te-dekoratory-są-tak-ważne)
7. [Typowe zastosowania](#typowe-zastosowania)
8. [Typowe błędy początkujących](#typowe-błędy-początkujących)
9. [Praktyczne przykłady](#praktyczne-przykłady)
10. [Dobre praktyki](#dobre-praktyki)
11. [Podsumowanie](#podsumowanie)
12. [Mini ściąga](#mini-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

W Pythonie są dekoratory, które spotyka się bardzo często i trzeba je znać praktycznie obowiązkowo.

Najważniejsze z nich to:

- `@property`
- `@staticmethod`
- `@classmethod`
- `@functools.lru_cache`

Każdy z nich rozwiązuje trochę inny problem.

---

## `@property`

Pozwala używać metody jak atrybutu.

Przykład:

```python
class Konto:
    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo
```

Teraz:

```python
k = Konto(100)
print(k.saldo)
```

bez nawiasów.

Można też dodać setter:

```python
    @saldo.setter
    def saldo(self, wartosc):
        if wartosc < 0:
            raise ValueError("Saldo nie moze byc ujemne")
        self._saldo = wartosc
```

---

## `@staticmethod`

To metoda, która należy logicznie do klasy, ale nie potrzebuje:

- `self`
- ani `cls`

Przykład:

```python
class Matematyka:
    @staticmethod
    def dodaj(a, b):
        return a + b
```

Użycie:

```python
Matematyka.dodaj(2, 3)
```

---

## `@classmethod`

To metoda, która dostaje klasę jako pierwszy argument.

Najczęściej nazywa się on `cls`.

Przykład:

```python
class Osoba:
    gatunek = "czlowiek"

    @classmethod
    def pokaz_gatunek(cls):
        return cls.gatunek
```

`classmethod` często służy też jako alternatywny konstruktor.

---

## `@functools.lru_cache`

To dekorator do cache’owania wyników funkcji.

Import:

```python
from functools import lru_cache
```

Przykład:

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

To bardzo przyspiesza powtarzalne obliczenia.

---

## Dlaczego te dekoratory są tak ważne

Bo pojawiają się bardzo często:

- `@property` w OOP,
- `@staticmethod` i `@classmethod` w klasach,
- `@lru_cache` w optymalizacji.

To praktyczny zestaw obowiązkowy.

---

## Typowe zastosowania

### `@property`

- walidacja danych,
- kontrolowany dostęp do atrybutów.

### `@staticmethod`

- funkcje pomocnicze logicznie związane z klasą.

### `@classmethod`

- alternatywne konstruktory,
- operacje na klasie, nie na instancji.

### `@lru_cache`

- memoizacja,
- przyspieszanie czystych funkcji.

---

## Typowe błędy początkujących

- mylenie `@staticmethod` i `@classmethod`,
- używanie `@staticmethod`, gdy zwykła funkcja poza klasą byłaby lepsza,
- używanie `@property` bez realnej potrzeby,
- używanie `@lru_cache` dla funkcji zależnych od zmiennego stanu.

---

## Praktyczne przykłady

```python
class Temperatura:
    def __init__(self, c):
        self._c = c

    @property
    def celsjusz(self):
        return self._c

    @staticmethod
    def c_na_f(c):
        return c * 9 / 5 + 32

    @classmethod
    def zera(cls):
        return cls(0)
```

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def silnia(n):
    if n <= 1:
        return 1
    return n * silnia(n - 1)
```

---

## Dobre praktyki

- `@property` używaj do sensownej kontroli dostępu,
- `@classmethod` traktuj jako narzędzie pracy z klasą,
- `@staticmethod` stosuj wtedy, gdy metoda logicznie należy do klasy,
- `@lru_cache` używaj do funkcji deterministycznych.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- `@property` robi z metody atrybut,
- `@staticmethod` nie dostaje ani `self`, ani `cls`,
- `@classmethod` dostaje klasę,
- `@lru_cache` cache’uje wyniki funkcji.

---

## Mini ściąga

```python
@property
@staticmethod
@classmethod
@lru_cache(maxsize=None)
```

---

## Ćwiczenia

### Ćwiczenie 1

Utwórz klasę z `@property`.

### Ćwiczenie 2

Dodaj `@staticmethod`.

### Ćwiczenie 3

Dodaj `@classmethod` jako alternatywny konstruktor.

### Ćwiczenie 4

Użyj `@lru_cache` do funkcji Fibonacciego.

---

## Przykładowe rozwiązania

```python
from functools import lru_cache

class A:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x
```
