# Iteratory i generatory w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest iteracja](#czym-jest-iteracja)
3. [Iterable, iterator i iterowanie](#iterable-iterator-i-iterowanie)
4. [Protokół iteratora](#protokół-iteratora)
5. [`iter()` i `next()`](#iter-i-next)
6. [Jak działa pętla `for`](#jak-działa-pętla-for)
7. [Czym jest generator](#czym-jest-generator)
8. [`yield`](#yield)
9. [Generator a zwykła funkcja](#generator-a-zwykła-funkcja)
10. [Generator expression](#generator-expression)
11. [`yield from`](#yield-from)
12. [Generatory strumieni danych](#generatory-strumieni-danych)
13. [Pipeline generatorów](#pipeline-generatorów)
14. [Pamięć i wydajność](#pamięć-i-wydajność)
15. [Kiedy używać iteratora](#kiedy-używać-iteratora)
16. [Kiedy używać generatora](#kiedy-używać-generatora)
17. [Typowe błędy początkujących](#typowe-błędy-początkujących)
18. [Praktyczne przykłady](#praktyczne-przykłady)
19. [Dobre praktyki](#dobre-praktyki)
20. [Podsumowanie](#podsumowanie)
21. [Mini ściąga](#mini-ściąga)
22. [Ćwiczenia](#ćwiczenia)
23. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Iteratory i generatory to jeden z najważniejszych „głębszych” tematów w Pythonie.

To właśnie one stoją za:

- pętlą `for`,
- generator expressions,
- pracą na dużych danych,
- leniwym obliczaniem,
- strumieniowym przetwarzaniem danych.

Jeśli dobrze zrozumiesz iteratory i generatory, dużo łatwiej będzie Ci pisać:

- wydajniejszy kod,
- kod oszczędzający pamięć,
- eleganckie przetwarzanie danych krok po kroku.

---

## Czym jest iteracja

Iteracja to przechodzenie po elementach jeden po drugim.

Przykład:

```python
for x in [10, 20, 30]:
    print(x)
```

Na pierwszy rzut oka to wygląda prosto.

Ale pod spodem Python używa specjalnego mechanizmu iteratorów.

---

## Iterable, iterator i iterowanie

To trzy powiązane pojęcia:

### Iterable

To obiekt, po którym można iterować.

Na przykład:

- lista,
- tuple,
- string,
- zbiór,
- słownik,
- plik.

### Iterator

To obiekt, który:

- pamięta aktualną pozycję,
- umie zwracać kolejne elementy.

### Iterowanie

To proces pobierania kolejnych elementów z iteratora.

---

## Protokół iteratora

Iterator w Pythonie opiera się na dwóch kluczowych metodach:

- `__iter__()`
- `__next__()`

Najprościej:

- `__iter__()` zwraca iterator,
- `__next__()` daje kolejny element albo zgłasza `StopIteration`.

To właśnie jest protokół iteratora.

---

## `iter()` i `next()`

Przykład:

```python
lista = [10, 20, 30]
it = iter(lista)

print(next(it))
print(next(it))
print(next(it))
```

Po ostatnim elemencie:

```python
next(it)
```

da błąd:

```python
StopIteration
```

---

## Jak działa pętla `for`

Pętla:

```python
for x in dane:
    print(x)
```

robi mniej więcej:

1. `it = iter(dane)`
2. bierze kolejne `next(it)`
3. kończy, gdy pojawi się `StopIteration`

To bardzo ważne do zrozumienia całej idei generatorów.

---

## Czym jest generator

Generator to specjalny rodzaj iteratora.

Najprościej:

generator produkuje wartości po jednej, wtedy gdy są potrzebne.

Nie tworzy wszystkiego od razu.

To daje:

- oszczędność pamięci,
- leniwe obliczanie,
- wygodne przetwarzanie strumieni danych.

---

## `yield`

`yield` to słowo kluczowe, które zamienia zwykłą funkcję w generator.

Przykład:

```python
def liczby():
    yield 1
    yield 2
    yield 3
```

Wywołanie:

```python
g = liczby()
print(g)
```

zwraca generator, a nie gotową listę.

---

## Generator a zwykła funkcja

### Zwykła funkcja

```python
def f():
    return 10
```

Kończy się od razu po `return`.

### Generator

```python
def g():
    yield 10
```

Wstrzymuje się na `yield` i może później wznowić działanie.

---

## Generator expression

To krótki zapis generatora:

```python
g = (x ** 2 for x in range(5))
```

To podobne do list comprehension, ale używa nawiasów `()`, a nie `[]`.

Nie tworzy całej listy od razu.

---

## `yield from`

`yield from` pozwala delegować generowanie do innego iteratora lub generatora.

Przykład:

```python
def wew():
    yield 1
    yield 2

def zew():
    yield from wew()
    yield 3
```

To wygodniejszy zapis niż ręczne:

```python
for x in wew():
    yield x
```

---

## Generatory strumieni danych

To bardzo praktyczne zastosowanie.

Możesz mieć generator, który przetwarza dane kawałek po kawałku:

- linie z pliku,
- rekordy z API,
- wielki zbiór danych,
- nieskończony ciąg.

Przykład:

```python
def czytaj_linie(sciezka):
    with open(sciezka, "r") as plik:
        for linia in plik:
            yield linia.strip()
```

To pozwala czytać dane strumieniowo.

---

## Pipeline generatorów

Generatory można łączyć w etapy:

```python
def liczby():
    for x in range(10):
        yield x

def parzyste(dane):
    for x in dane:
        if x % 2 == 0:
            yield x

def kwadraty(dane):
    for x in dane:
        yield x ** 2
```

Potem:

```python
wynik = kwadraty(parzyste(liczby()))
for x in wynik:
    print(x)
```

To bardzo elegancki model pracy na strumieniu danych.

---

## Pamięć i wydajność

Lista:

- tworzy wszystkie elementy od razu,
- zajmuje pamięć na cały wynik.

Generator:

- tworzy elementy po jednej sztuce,
- zwykle zużywa mniej pamięci.

To szczególnie ważne przy dużych danych.

---

## Kiedy używać iteratora

Iterator przydaje się, gdy:

- chcesz kontrolować ręcznie przechodzenie po danych,
- pracujesz z `next()`,
- budujesz własny obiekt iterowalny.

---

## Kiedy używać generatora

Generator przydaje się, gdy:

- chcesz przetwarzać dane leniwie,
- dane są duże,
- chcesz stworzyć strumień wyników,
- nie potrzebujesz wszystkiego naraz.

---

## Typowe błędy początkujących

- mylenie iterable z iteratorem,
- zapominanie, że iterator się zużywa,
- oczekiwanie, że generator działa jak lista,
- brak zrozumienia `StopIteration`,
- niepotrzebne zamienianie wszystkiego na listę.

---

## Praktyczne przykłady

### Ręczna iteracja

```python
lista = [1, 2, 3]
it = iter(lista)

print(next(it))
print(next(it))
```

### Generator

```python
def odliczanie(n):
    while n > 0:
        yield n
        n -= 1
```

### `yield from`

```python
def a():
    yield from [1, 2, 3]
    yield 4
```

---

## Dobre praktyki

- używaj generatorów do dużych lub strumieniowych danych,
- pamiętaj, że generator jest jednorazowy,
- nie komplikuj iteratorów, jeśli zwykła pętla wystarczy,
- używaj `yield from`, gdy delegujesz iterację dalej.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- iterator wspiera `__iter__()` i `__next__()`,
- `for` działa na iteratorach,
- generator to specjalny iterator tworzony przez `yield`,
- `yield from` upraszcza delegowanie,
- generatory są świetne do leniwego i oszczędnego przetwarzania danych.

---

## Mini ściąga

```python
it = iter([1, 2, 3])
next(it)
```

```python
def gen():
    yield 1
    yield 2
```

```python
(x for x in range(10))
```

```python
yield from inny_generator()
```

---

## Ćwiczenia

### Ćwiczenie 1

Utwórz iterator dla listy i pobierz dwa pierwsze elementy przez `next()`.

### Ćwiczenie 2

Napisz generator wypisujący liczby od 1 do `n`.

### Ćwiczenie 3

Napisz generator zwracający tylko liczby parzyste z zakresu.

### Ćwiczenie 4

Użyj `yield from`, by połączyć dwa źródła danych.

---

## Przykładowe rozwiązania

### Ćwiczenie 1

```python
it = iter([10, 20, 30])
print(next(it))
print(next(it))
```

### Ćwiczenie 2

```python
def liczby(n):
    for x in range(1, n + 1):
        yield x
```

### Ćwiczenie 3

```python
def parzyste(n):
    for x in range(n + 1):
        if x % 2 == 0:
            yield x
```

### Ćwiczenie 4

```python
def oba():
    yield from [1, 2, 3]
    yield from [4, 5]
```
