# Generator Expressions w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest generator expression](#czym-jest-generator-expression)
3. [Generator expression a list comprehension](#generator-expression-a-list-comprehension)
4. [Dlaczego generatory są ważne](#dlaczego-generatory-są-ważne)
5. [Podstawowa składnia](#podstawowa-składnia)
6. [Jak działa leniwe obliczanie](#jak-działa-leniwe-obliczanie)
7. [Zużywanie generatora](#zużywanie-generatora)
8. [Generator w `for`](#generator-w-for)
9. [Generator z `sum`, `max`, `min`, `any`, `all`](#generator-z-sum-max-min-any-all)
10. [Generator z warunkiem](#generator-z-warunkiem)
11. [Generator a pamięć](#generator-a-pamięć)
12. [Kiedy generator jest lepszy od listy](#kiedy-generator-jest-lepszy-od-listy)
13. [Kiedy lista jest lepsza od generatora](#kiedy-lista-jest-lepsza-od-generatora)
14. [Generator a funkcje generatorowe](#generator-a-funkcje-generatorowe)
15. [Typowe błędy początkujących](#typowe-błędy-początkujących)
16. [Praktyczne przykłady](#praktyczne-przykłady)
17. [Dobre praktyki](#dobre-praktyki)
18. [Podsumowanie](#podsumowanie)
19. [Mini ściąga](#mini-ściąga)
20. [Ćwiczenia](#ćwiczenia)
21. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Generator expressions są bardzo podobne do list comprehensions, ale działają inaczej.

Najważniejsza różnica jest taka:

- list comprehension tworzy całą listę od razu,
- generator expression tworzy elementy dopiero wtedy, gdy są potrzebne.

To nazywa się **leniwe obliczanie**.

Generatory są bardzo przydatne, gdy:

- pracujesz z dużą ilością danych,
- nie chcesz trzymać wszystkiego naraz w pamięci,
- potrzebujesz tylko przejść po elementach raz.

---

## Czym jest generator expression

To specjalny zapis podobny do comprehension, ale używający nawiasów okrągłych.

Przykład:

```python
gen = (x ** 2 for x in range(5))
print(gen)
```

To nie jest lista.
To generator.

### Porównanie

Lista:

```python
[x ** 2 for x in range(5)]
```

Generator:

```python
(x ** 2 for x in range(5))
```

---

## Generator expression a list comprehension

### List comprehension

```python
lista = [x ** 2 for x in range(5)]
print(lista)
```

Wynik:

```python
[0, 1, 4, 9, 16]
```

### Generator expression

```python
gen = (x ** 2 for x in range(5))
print(gen)
```

Wynik będzie wyglądał mniej więcej tak:

```python
<generator object ...>
```

To oznacza, że elementy nie zostały jeszcze policzone jako gotowa lista.

---

## Dlaczego generatory są ważne

Bo pozwalają oszczędzać pamięć.

Jeśli masz milion elementów:

```python
[x ** 2 for x in range(1_000_000)]
```

to tworzysz ogromną listę od razu.

A jeśli zrobisz:

```python
(x ** 2 for x in range(1_000_000))
```

to generator oblicza kolejne wartości dopiero wtedy, gdy ich potrzebujesz.

To bardzo ważne przy dużych danych.

---

## Podstawowa składnia

Schemat:

```python
(wyrazenie for element in kolekcja)
```

Przykład:

```python
gen = (x * 2 for x in [1, 2, 3, 4])
```

Można potem przejść po generatorze:

```python
for wartosc in gen:
    print(wartosc)
```

---

## Jak działa leniwe obliczanie

Generator nie produkuje wszystkich wyników od razu.

Zamiast tego:

1. pamięta przepis, jak policzyć kolejną wartość,
2. tworzy wartość dopiero, gdy ktoś o nią poprosi.

Przykład:

```python
gen = (x ** 2 for x in range(5))
print(next(gen))
print(next(gen))
print(next(gen))
```

Wynik:

```python
0
1
4
```

Każde `next(gen)` bierze kolejną wartość.

---

## Zużywanie generatora

To bardzo ważna cecha.

Generator działa jak strumień:

- bierzesz kolejne elementy,
- po przejściu nie możesz po prostu zacząć od nowa bez utworzenia nowego generatora.

Przykład:

```python
gen = (x for x in range(3))

print(list(gen))
print(list(gen))
```

Wynik:

```python
[0, 1, 2]
[]
```

Drugi raz generator jest już pusty, bo został zużyty.

---

## Generator w `for`

Najczęściej używa się generatora właśnie w pętli.

```python
gen = (x ** 2 for x in range(5))

for wartosc in gen:
    print(wartosc)
```

To bardzo naturalne zastosowanie.

---

## Generator z `sum`, `max`, `min`, `any`, `all`

Generatory świetnie współpracują z funkcjami, które pobierają iterowalne dane.

### `sum()`

```python
wynik = sum(x ** 2 for x in range(5))
print(wynik)
```

### `max()`

```python
najwieksza = max(x ** 2 for x in range(5))
print(najwieksza)
```

### `any()`

```python
czy_jest_parzysta = any(x % 2 == 0 for x in [1, 3, 5, 8])
print(czy_jest_parzysta)
```

### `all()`

```python
czy_wszystkie_dodatnie = all(x > 0 for x in [1, 2, 3])
print(czy_wszystkie_dodatnie)
```

To bardzo pythonowy styl.

---

## Generator z warunkiem

Można filtrować elementy tak jak w comprehension.

Przykład:

```python
gen = (x for x in range(10) if x % 2 == 0)
print(list(gen))
```

Wynik:

```python
[0, 2, 4, 6, 8]
```

---

## Generator a pamięć

To jedna z najważniejszych zalet generatorów.

### Lista

Trzyma wszystkie elementy naraz w pamięci.

### Generator

Tworzy elementy po jednym, gdy są potrzebne.

To oznacza, że generator bywa dużo lepszy dla:

- bardzo dużych danych,
- plików,
- strumieni,
- długich obliczeń.

---

## Kiedy generator jest lepszy od listy

Użyj generatora, gdy:

- nie potrzebujesz wszystkich wyników naraz,
- przechodzisz po danych tylko raz,
- dane mogą być duże,
- chcesz oszczędzić pamięć,
- przekazujesz wynik do `sum()`, `all()`, `any()`, `max()`, `min()`.

---

## Kiedy lista jest lepsza od generatora

Użyj listy, gdy:

- chcesz wielokrotnie używać wyników,
- potrzebujesz indeksowania,
- potrzebujesz długości przez `len()`,
- chcesz wypisać gotową kolekcję,
- chcesz sortować albo modyfikować wynik.

Generator nie nadaje się do wszystkiego.

---

## Generator a funkcje generatorowe

Generator expression to nie jedyny sposób tworzenia generatorów.

Można też pisać funkcje z `yield`.

Przykład:

```python
def liczby():
    for x in range(5):
        yield x
```

To już temat trochę obok, ale warto wiedzieć, że:

- generator expression to krótki zapis,
- funkcja generatorowa daje więcej możliwości przy bardziej złożonej logice.

---

## Typowe błędy początkujących

### 1. Oczekiwanie, że generator zachowuje się jak lista

Nie ma indeksów i nie działa tak samo.

### 2. Zapominanie, że generator się zużywa

Po jednym przejściu może być pusty.

### 3. Próba używania `len()` na generatorze

To nie działa tak jak dla listy.

### 4. Tworzenie generatora tam, gdzie potrzebna jest gotowa kolekcja

Czasem lista będzie po prostu lepsza.

### 5. Brak zrozumienia, czemu `print(gen)` nie pokazuje danych

Bo pokazuje obiekt generatora, a nie jego wszystkie elementy.

---

## Praktyczne przykłady

### Suma kwadratów

```python
wynik = sum(x ** 2 for x in range(1, 6))
print(wynik)
```

### Filtrowanie dodatnich liczb

```python
gen = (x for x in [-3, -1, 0, 2, 4] if x > 0)
print(list(gen))
```

### Sprawdzenie warunku

```python
czy_jest_ujemna = any(x < 0 for x in [1, 2, -3, 4])
print(czy_jest_ujemna)
```

### Wszystkie liczby parzyste

```python
gen = (x for x in range(20) if x % 2 == 0)

for liczba in gen:
    print(liczba)
```

---

## Dobre praktyki

### Używaj generatorów do jednorazowego przejścia po danych

To ich naturalne środowisko.

### Używaj generator expressions przy `sum()`, `any()`, `all()`

To bardzo elegancki i częsty wzorzec.

### Jeśli potrzebujesz wracać do wyników, użyj listy

Generator nie jest magazynem danych.

### Nie komplikuj

Jeśli generator expression robi się trudny do zrozumienia, wybierz prostsze rozwiązanie.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- generator expression używa `()`,
- tworzy wartości leniwie, a nie wszystkie naraz,
- oszczędza pamięć,
- dobrze współpracuje z `sum()`, `max()`, `min()`, `any()`, `all()`,
- zużywa się podczas iteracji,
- nie zastępuje listy w każdej sytuacji.

Jeśli dobrze opanujesz generatory, będziesz umiał pisać bardziej wydajny i bardziej elastyczny kod.

---

## Mini ściąga

### Podstawowy zapis

```python
(x ** 2 for x in range(5))
```

### Z warunkiem

```python
(x for x in liczby if x > 0)
```

### Zużycie generatora

```python
gen = (x for x in range(3))
next(gen)
```

### Z `sum()`

```python
sum(x ** 2 for x in range(5))
```

### Z `any()` i `all()`

```python
any(x < 0 for x in liczby)
all(x > 0 for x in liczby)
```

---

## Ćwiczenia

### Ćwiczenie 1

Utwórz generator kwadratów liczb od 1 do 10 i wypisz go jako listę.

### Ćwiczenie 2

Użyj generator expression z `sum()`, aby policzyć sumę liczb od 1 do 100.

### Ćwiczenie 3

Sprawdź przez `any()`, czy w liście jest liczba ujemna.

### Ćwiczenie 4

Sprawdź przez `all()`, czy wszystkie liczby są dodatnie.

### Ćwiczenie 5

Utwórz generator tylko dla liczb parzystych od 0 do 20.

---

## Przykładowe rozwiązania

### Ćwiczenie 1

```python
gen = (x ** 2 for x in range(1, 11))
print(list(gen))
```

### Ćwiczenie 2

```python
wynik = sum(x for x in range(1, 101))
print(wynik)
```

### Ćwiczenie 3

```python
liczby = [1, 2, -3, 4]
print(any(x < 0 for x in liczby))
```

### Ćwiczenie 4

```python
liczby = [1, 2, 3, 4]
print(all(x > 0 for x in liczby))
```

### Ćwiczenie 5

```python
gen = (x for x in range(21) if x % 2 == 0)
print(list(gen))
```

---

## Na koniec

Najlepiej uczyć się generator expressions przez porównywanie ich z list comprehensions.

Warto:

1. zrobić ten sam przykład jako listę,
2. potem jako generator,
3. sprawdzić różnicę w zachowaniu,
4. zobaczyć, kiedy generator się zużywa.

To bardzo szybko buduje intuicję, kiedy używać którego narzędzia.
