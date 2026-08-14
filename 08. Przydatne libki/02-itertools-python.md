# `itertools` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co używać `itertools`](#po-co-używać-itertools)
3. [Iteratory i leniwe przetwarzanie](#iteratory-i-leniwe-przetwarzanie)
4. [`count()`](#count)
5. [`cycle()`](#cycle)
6. [`repeat()`](#repeat)
7. [`chain()`](#chain)
8. [`islice()`](#islice)
9. [`product()`, `permutations()`, `combinations()`](#product-permutations-combinations)
10. [`groupby()`](#groupby)
11. [Typowe błędy początkujących](#typowe-błędy-początkujących)
12. [Praktyczne przykłady](#praktyczne-przykłady)
13. [Dobre praktyki](#dobre-praktyki)
14. [Podsumowanie](#podsumowanie)
15. [Mini ściąga](#mini-ściąga)
16. [Ćwiczenia](#ćwiczenia)
17. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`itertools` to moduł do pracy z iteratorami.

Pozwala pisać wydajny, zwięzły kod do:

- łączenia sekwencji,
- generowania kombinacji,
- cięcia iteratorów,
- budowania potoków danych.

---

## Po co używać `itertools`

`itertools` przydaje się, gdy chcesz:

- przetwarzać dane leniwie,
- uniknąć budowania niepotrzebnych list,
- korzystać z gotowych wzorców iteracyjnych.

---

## Iteratory i leniwe przetwarzanie

Wiele narzędzi z `itertools` zwraca iteratory.

To znaczy, że elementy powstają dopiero wtedy, gdy są potrzebne.

To często oszczędza pamięć.

---

## `count()`

Nieskończony licznik:

```python
from itertools import count

for x in count(10, 2):
    print(x)
    if x >= 16:
        break
```

---

## `cycle()`

Zapętla elementy:

```python
from itertools import cycle

for i, x in zip(range(5), cycle(["A", "B"])):
    print(x)
```

---

## `repeat()`

Powtarza wartość:

```python
from itertools import repeat

print(list(repeat("ok", 3)))
```

---

## `chain()`

Łączy iterowalne źródła:

```python
from itertools import chain

print(list(chain([1, 2], [3, 4], [5])))
```

---

## `islice()`

Wycina fragment iteratora:

```python
from itertools import islice

print(list(islice(range(100), 5, 10)))
```

---

## `product()`, `permutations()`, `combinations()`

To jedne z najpraktyczniejszych funkcji kombinatorycznych.

```python
from itertools import product, permutations, combinations

print(list(product([1, 2], ["a", "b"])))
print(list(permutations([1, 2, 3], 2)))
print(list(combinations([1, 2, 3], 2)))
```

---

## `groupby()`

Grupuje kolejne elementy o tym samym kluczu.

```python
from itertools import groupby

dane = [1, 1, 2, 2, 2, 3]
for klucz, grupa in groupby(dane):
    print(klucz, list(grupa))
```

Ważne: działa na kolejnych elementach, nie robi automatycznego grupowania jak SQL.

---

## Typowe błędy początkujących

- oczekiwanie, że iteratory można wielokrotnie konsumować bez odtwarzania,
- nieświadomość, że `groupby()` wymaga odpowiedniego uporządkowania danych,
- zamiana wszystkiego na listę bez potrzeby,
- używanie `itertools` tam, gdzie prosty `for` jest czytelniejszy.

---

## Praktyczne przykłady

### Wszystkie pary

```python
from itertools import product

for a, b in product([1, 2, 3], ["x", "y"]):
    print(a, b)
```

### Pierwsze 5 elementów iteratora

```python
from itertools import islice, count

print(list(islice(count(100), 5)))
```

---

## Dobre praktyki

- używaj `itertools`, gdy daje realne uproszczenie,
- pamiętaj o leniwej naturze iteratorów,
- przy `groupby()` sortuj dane, jeśli chcesz grupować po kluczu globalnie,
- nie komplikuj prostych zadań na siłę.

---

## Podsumowanie

`itertools` to bardzo mocny zestaw narzędzi do pracy z iteratorami.

W praktyce szczególnie często przydają się:

- `chain()`,
- `islice()`,
- `product()`,
- `combinations()`.

---

## Mini ściąga

```python
from itertools import chain, islice, product
```

Najważniejsze:

- `chain()` łączy,
- `islice()` wycina,
- `count()` liczy w nieskończoność,
- `product()` robi iloczyn kartezjański,
- `groupby()` grupuje kolejne elementy.

---

## Ćwiczenia

1. Połącz trzy listy w jeden iterator.
2. Pobierz pierwsze 10 liczb z `count()`.
3. Wygeneruj wszystkie pary z dwóch list.
4. Znajdź wszystkie kombinacje 2-elementowe.
5. Pogrupuj kolejne jednakowe liczby w liście.

---

## Przykładowe rozwiązania

### 1. Łączenie

```python
from itertools import chain

print(list(chain([1], [2, 3], [4])))
```

### 2. Pierwsze 10 liczb

```python
from itertools import count, islice

print(list(islice(count(1), 10)))
```

### 3. Pary

```python
from itertools import product

print(list(product([1, 2], ["a", "b"])))
```

### 4. Kombinacje

```python
from itertools import combinations

print(list(combinations([1, 2, 3], 2)))
```

### 5. Grupowanie

```python
from itertools import groupby

for k, g in groupby([1, 1, 2, 3, 3]):
    print(k, list(g))
```
