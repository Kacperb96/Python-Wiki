# `functools.wraps` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co istnieje `wraps`](#po-co-istnieje-wraps)
3. [Problem bez `wraps`](#problem-bez-wraps)
4. [Jak działa `wraps`](#jak-działa-wraps)
5. [Podstawowy wzorzec użycia](#podstawowy-wzorzec-użycia)
6. [Jakie metadane zachowuje](#jakie-metadane-zachowuje)
7. [`__name__`, `__doc__`, introspekcja](#__name____doc__-introspekcja)
8. [Dlaczego to ważne w praktyce](#dlaczego-to-ważne-w-praktyce)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczne przykłady](#praktyczne-przykłady)
11. [Dobre praktyki](#dobre-praktyki)
12. [Podsumowanie](#podsumowanie)
13. [Mini ściąga](#mini-ściąga)
14. [Ćwiczenia](#ćwiczenia)
15. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Kiedy piszesz dekorator, bardzo łatwo przypadkiem „zgubić” informacje o dekorowanej funkcji.

Bez dodatkowej pomocy wrapper staje się nową funkcją i Python widzi właśnie jego, a nie oryginał.

To psuje:

- nazwę funkcji,
- docstring,
- część introspekcji,
- narzędzia debugujące i dokumentujące.

Właśnie dlatego istnieje `functools.wraps`.

---

## Po co istnieje `wraps`

`wraps` służy do zachowania metadanych oryginalnej funkcji.

Najprościej:

dekorowany wrapper ma dalej wyglądać jak oryginalna funkcja.

---

## Problem bez `wraps`

Przykład:

```python
def dekorator(f):
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper
```

Jeśli udekorujesz funkcję, to:

```python
print(funkcja.__name__)
```

może pokazać:

```python
wrapper
```

zamiast właściwej nazwy.

---

## Jak działa `wraps`

`wraps` kopiuje ważne metadane z oryginalnej funkcji do wrappera.

Import:

```python
from functools import wraps
```

---

## Podstawowy wzorzec użycia

```python
from functools import wraps

def dekorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper
```

To najczęściej właśnie tak powinien wyglądać dekorator.

---

## Jakie metadane zachowuje

Między innymi:

- `__name__`
- `__doc__`
- `__module__`

oraz ustawia `__wrapped__`.

---

## `__name__`, `__doc__`, introspekcja

Przykład:

```python
from functools import wraps

def dekorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper
```

To pomaga, gdy:

- sprawdzasz `help()`,
- generujesz dokumentację,
- używasz frameworków,
- debugujesz.

---

## Dlaczego to ważne w praktyce

W prawdziwych projektach brak `wraps` może powodować bardzo mylące sytuacje.

Na przykład:

- logi pokazują złą nazwę funkcji,
- dokumentacja widzi `wrapper`,
- testy lub frameworki mają gorsze informacje o funkcji.

---

## Typowe błędy początkujących

- brak `@wraps(f)`,
- mylenie `wraps` z dekoratorem użytkownika,
- zakładanie, że Python zrobi to automatycznie.

---

## Praktyczne przykłady

```python
from functools import wraps

def loguj(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print("Wywolanie:", f.__name__)
        return f(*args, **kwargs)
    return wrapper

@loguj
def hello():
    """Przykladowa funkcja."""
    print("Hello")
```

---

## Dobre praktyki

- prawie zawsze używaj `wraps` w dekoratorach funkcyjnych,
- traktuj to jako domyślny nawyk,
- szczególnie pilnuj tego w kodzie bibliotecznym i frameworkowym.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- `functools.wraps` zachowuje metadane funkcji,
- jest bardzo ważny w poprawnych dekoratorach,
- bez niego wrapper „przykrywa” tożsamość oryginalnej funkcji.

---

## Mini ściąga

```python
from functools import wraps

def dekorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper
```

---

## Ćwiczenia

### Ćwiczenie 1

Napisz dekorator bez `wraps` i sprawdź `__name__`.

### Ćwiczenie 2

Dodaj `wraps` i porównaj wynik.

---

## Przykładowe rozwiązania

```python
from functools import wraps

def dekorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper
```
