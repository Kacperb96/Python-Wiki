# `functools` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co używać `functools`](#po-co-używać-functools)
3. [`partial`](#partial)
4. [`reduce`](#reduce)
5. [Dekoratory z `wraps`](#dekoratory-z-wraps)
6. [`lru_cache`](#lru_cache)
7. [`cached_property`](#cached_property)
8. [`cmp_to_key`](#cmp_to_key)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczne przykłady](#praktyczne-przykłady)
11. [Dobre praktyki](#dobre-praktyki)
12. [Podsumowanie](#podsumowanie)
13. [Mini ściąga](#mini-ściąga)
14. [Ćwiczenia](#ćwiczenia)
15. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`functools` zawiera narzędzia wspierające pracę z funkcjami i dekoratorami.

Nie każdy element tego modułu jest używany codziennie, ale kilka z nich jest bardzo praktycznych.

---

## Po co używać `functools`

Najczęstsze zastosowania:

- częściowe wiązanie argumentów,
- cache wyników funkcji,
- poprawne pisanie dekoratorów,
- redukcja sekwencji do jednej wartości.

---

## `partial`

Pozwala stworzyć nową funkcję z częścią argumentów już ustawioną.

```python
from functools import partial

def potega(x, y):
    return x ** y

kwadrat = partial(potega, y=2)
print(kwadrat(5))
```

---

## `reduce`

Redukuje sekwencję do jednej wartości.

```python
from functools import reduce

wynik = reduce(lambda a, b: a + b, [1, 2, 3, 4])
print(wynik)
```

W praktyce często czytelniejsze bywa zwykłe `sum()`, ale warto znać ideę.

---

## Dekoratory z `wraps`

Jeśli piszesz dekorator, używaj `wraps`.

```python
from functools import wraps

def moj_dekorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("start")
        return func(*args, **kwargs)
    return wrapper
```

To zachowuje metadane funkcji, np. nazwę i docstring.

---

## `lru_cache`

Bardzo praktyczny cache wyników funkcji.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(30))
```

To potrafi dramatycznie przyspieszyć niektóre obliczenia.

---

## `cached_property`

Pozwala obliczyć wartość raz i potem ją zapamiętać na instancji.

```python
from functools import cached_property

class Raport:
    @cached_property
    def wynik(self):
        print("licze")
        return 42
```

---

## `cmp_to_key`

Pomaga zamienić starszy styl porównywania na klucz do sortowania.

Jest mniej codzienny, ale spotykany w starszym kodzie i specjalnych przypadkach.

---

## Typowe błędy początkujących

- brak `wraps` w dekoratorach,
- nadużywanie `reduce`, gdy prostsza funkcja wbudowana wystarcza,
- używanie `lru_cache` dla funkcji z efektami ubocznymi,
- brak rozumienia, że cache może zużywać pamięć.

---

## Praktyczne przykłady

### Cache dla drogiego obliczenia

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def policz(x):
    print("licze", x)
    return x * x

print(policz(5))
print(policz(5))
```

### Dekorator logujący

```python
from functools import wraps

def loguj(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Wywolanie {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

---

## Dobre praktyki

- `wraps` traktuj jako standard przy dekoratorach,
- `lru_cache` stosuj do czystych funkcji,
- `partial` używaj tam, gdzie poprawia czytelność,
- nie komplikuj prostych przypadków funkcjonalnych na siłę.

---

## Podsumowanie

`functools` daje kilka bardzo wartościowych narzędzi do bardziej dojrzałego stylu pracy z funkcjami.

Najczęściej naprawdę przydają się:

- `wraps`,
- `lru_cache`,
- `partial`.

---

## Mini ściąga

```python
from functools import partial, wraps, lru_cache
```

Najważniejsze:

- `partial()` ustawia część argumentów,
- `wraps` zachowuje metadane funkcji,
- `lru_cache` cache'uje wyniki funkcji,
- `reduce` redukuje sekwencję do jednej wartości.

---

## Ćwiczenia

1. Utwórz funkcję `kwadrat` przez `partial`.
2. Policz sumę listy przez `reduce`.
3. Napisz prosty dekorator z `wraps`.
4. Zastosuj `lru_cache` do funkcji Fibonacciego.
5. Użyj `cached_property` w klasie.

---

## Przykładowe rozwiązania

### 1. `partial`

```python
from functools import partial

def potega(x, y):
    return x ** y

kwadrat = partial(potega, y=2)
print(kwadrat(4))
```

### 2. `reduce`

```python
from functools import reduce

print(reduce(lambda a, b: a + b, [1, 2, 3]))
```

### 3. Dekorator

```python
from functools import wraps

def dekorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

### 4. Fibonacci

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

### 5. `cached_property`

```python
from functools import cached_property

class A:
    @cached_property
    def x(self):
        return 123
```
