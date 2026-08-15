# `itertools` w Pythonie

## Wprowadzenie

`itertools` to moduł do pracy z iteratorami.

Pozwala pisać zwięzły i wydajny kod do:

- łączenia sekwencji,
- generowania kombinacji,
- budowania pipeline'ów danych,
- pracy leniwej bez tworzenia zbędnych list.

## Kiedy `itertools` ma sens

`itertools` przydaje się szczególnie, gdy:

- dane są przetwarzane etapami,
- nie chcesz ładować wszystkiego do pamięci,
- chcesz połączyć kilka iterowalnych źródeł,
- potrzebujesz kombinacji, permutacji lub iloczynu kartezjańskiego,
- pracujesz na strumieniu danych.

## Kiedy zwykły `for` jest lepszy

Jeśli zadanie jest bardzo proste, to zwykła pętla często wygrywa czytelnością.

To ważna zasada: `itertools` nie ma robić wrażenia, tylko upraszczać.

## Iteratory i leniwe przetwarzanie

Wiele narzędzi z `itertools` zwraca iterator, czyli elementy powstają dopiero wtedy, gdy są potrzebne.

To bywa korzystne pamięciowo.

## `chain()`

Łączy kilka iterowalnych źródeł.

```python
from itertools import chain

print(list(chain([1, 2], [3, 4], [5])))
```

Output:

```python
[1, 2, 3, 4, 5]
```

### Kiedy wybrać `chain()` zamiast `+`

Użyj `chain()`, gdy:

- źródeł jest dużo,
- są iteratorami,
- chcesz przetwarzać dane leniwie.

Jeśli masz dwie krótkie listy i chcesz po prostu nową listę, zwykłe `a + b` też może być całkiem dobre.

## `count()`

Nieskończony licznik.

```python
from itertools import count

for x in count(10, 2):
    print(x)
    if x >= 16:
        break
```

Output:

```python
10
12
14
16
```

## `cycle()`

Zapętla elementy w kółko.

```python
from itertools import cycle

for i, x in zip(range(5), cycle(["A", "B"])):
    print(x)
```

Output:

```python
A
B
A
B
A
```

## `repeat()`

Powtarza tę samą wartość.

```python
from itertools import repeat

print(list(repeat("ok", 3)))
```

Output:

```python
['ok', 'ok', 'ok']
```

## `islice()`

Wycina fragment iteratora.

```python
from itertools import islice

print(list(islice(range(100), 5, 10)))
```

Output:

```python
[5, 6, 7, 8, 9]
```

### Kiedy `islice()` ma sens

Gdy pracujesz z iteratorami i nie chcesz zamieniać ich całych na listę tylko po to, żeby pobrać fragment.

## `product()`, `permutations()`, `combinations()`

```python
from itertools import product, permutations, combinations

print(list(product([1, 2], ["a", "b"])))
print(list(permutations([1, 2, 3], 2)))
print(list(combinations([1, 2, 3], 2)))
```

To bardzo praktyczne narzędzia do generowania wariantów.

## `groupby()`

Grupuje kolejne elementy o tym samym kluczu.

```python
from itertools import groupby

data = [1, 1, 2, 2, 2, 3]
for key, group in groupby(data):
    print(key, list(group))
```

Output:

```python
1 [1, 1]
2 [2, 2, 2]
3 [3]
```

### Ważne

`groupby()` działa na kolejnych elementach, a nie jak SQL-owe globalne grupowanie.

Często przed użyciem trzeba dane posortować.

## `itertools` vs zwykła pętla

### Wersja z `chain()`

```python
from itertools import chain

for x in chain([1, 2], [3, 4], [5]):
    print(x)
```

### Wersja zwykła

```python
for seq in ([1, 2], [3, 4], [5]):
    for x in seq:
        print(x)
```

Obie są poprawne. `chain()` bywa czytelniejsze, jeśli naprawdę składasz wiele źródeł. Zwykły `for` bywa lepszy, jeśli chcesz maksymalnej oczywistości.

## Typowe błędy początkujących

- nieświadomość, że obiekty z `itertools` są iteratorami,
- wielokrotne zużywanie iteratora i zdziwienie, że „już nic nie ma”,
- używanie `groupby()` bez sortowania,
- zamienianie wszystkiego na `list()` bez potrzeby,
- używanie `itertools` tam, gdzie zwykła pętla byłaby prostsza.

## Mini scenariusz praktyczny

Masz trzy źródła wpisów logów i chcesz je przejść jednym strumieniem.

Tu `chain()` ma bardzo sensowny use case.

Masz też nieskończone źródło numerów albo chcesz pobrać tylko fragment iteratora. Tu `count()` i `islice()` robią świetną robotę.

## Dobre praktyki

- używaj `itertools`, gdy upraszcza kod albo oszczędza pamięć,
- nie komplikuj prostych zadań na siłę,
- pamiętaj, że iteratory są konsumowane,
- przy `groupby()` myśl o kolejności danych,
- wybieraj czytelność ponad „spryt”.

## Szybka ściąga

Najczęściej przydatne:

- `chain()` — łączy iterowalne źródła,
- `islice()` — wycina fragment iteratora,
- `count()` — nieskończony licznik,
- `product()` — iloczyn kartezjański,
- `combinations()` — kombinacje,
- `groupby()` — grupowanie kolejnych elementów.

## Ćwiczenia

1. Połącz trzy listy przez `chain()`.
2. Pobierz pierwsze 5 elementów z `count()`.
3. Wygeneruj wszystkie pary z dwóch list.
4. Pokaż działanie `groupby()` przed i po sortowaniu.
5. Napisz to samo zadanie raz z `itertools`, a raz zwykłą pętlą.

## Najważniejsze do zapamiętania

- `itertools` daje gotowe wzorce iteracyjne.
- Największą siłą jest leniwe przetwarzanie i gotowe kombinatoryczne narzędzia.
- `groupby()` grupuje kolejne elementy, nie wszystko globalnie.
- Nie każde zadanie wymaga `itertools`.
- Dobry użytek z `itertools` upraszcza kod, a nie go komplikuje.
