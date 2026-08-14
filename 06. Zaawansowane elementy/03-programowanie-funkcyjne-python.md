# Programowanie funkcyjne w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest programowanie funkcyjne](#czym-jest-programowanie-funkcyjne)
3. [Funkcje wysokiego rzędu](#funkcje-wysokiego-rzędu)
4. [`map`](#map)
5. [`filter`](#filter)
6. [`reduce`](#reduce)
7. [Lambdy](#lambdy)
8. [`functools.partial`](#functoolspartial)
9. [`functools.singledispatch`](#functoolssingledispatch)
10. [Programowanie funkcyjne a Pythonic style](#programowanie-funkcyjne-a-pythonic-style)
11. [Kiedy to podejście ma sens](#kiedy-to-podejście-ma-sens)
12. [Kiedy przeszkadza](#kiedy-przeszkadza)
13. [Typowe błędy początkujących](#typowe-błędy-początkujących)
14. [Praktyczne przykłady](#praktyczne-przykłady)
15. [Dobre praktyki](#dobre-praktyki)
16. [Podsumowanie](#podsumowanie)
17. [Mini ściąga](#mini-ściąga)
18. [Ćwiczenia](#ćwiczenia)
19. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Python nie jest „czysto funkcyjnym” językiem, ale ma bardzo dużo narzędzi inspirowanych programowaniem funkcyjnym.

Najważniejsze z nich to:

- funkcje wysokiego rzędu,
- `map`,
- `filter`,
- `reduce`,
- lambdy,
- `partial`,
- `singledispatch`.

To bardzo przydatny zestaw, ale trzeba umieć używać go z wyczuciem.

---

## Czym jest programowanie funkcyjne

Najprościej:

to styl, w którym:

- funkcje są traktowane jak wartości,
- dane często się przekształca krok po kroku,
- unika się zbędnych efektów ubocznych,
- logika bywa budowana przez składanie funkcji.

Python łączy to podejście z innymi stylami.

---

## Funkcje wysokiego rzędu

To funkcje, które:

- przyjmują inne funkcje,
  lub
- zwracają inne funkcje.

Przykład:

```python
def zastosuj(f, x):
    return f(x)
```

To fundament programowania funkcyjnego w Pythonie.

---

## `map`

`map` stosuje funkcję do każdego elementu.

```python
liczby = [1, 2, 3, 4]
wynik = map(lambda x: x * 2, liczby)
print(list(wynik))
```

To można też zapisać czytelniej przez comprehension:

```python
[x * 2 for x in liczby]
```

Dlatego w Pythonie `map` nie zawsze jest domyślnym wyborem.

---

## `filter`

`filter` zostawia tylko elementy spełniające warunek.

```python
liczby = [1, 2, 3, 4, 5]
wynik = filter(lambda x: x % 2 == 0, liczby)
print(list(wynik))
```

Alternatywa:

```python
[x for x in liczby if x % 2 == 0]
```

---

## `reduce`

`reduce` pochodzi z `functools`.

Redukuje wiele elementów do jednej wartości.

```python
from functools import reduce

liczby = [1, 2, 3, 4]
wynik = reduce(lambda a, b: a + b, liczby)
print(wynik)
```

To działa jak składanie elementów krok po kroku.

---

## Lambdy

Lambda to mała anonimowa funkcja.

```python
lambda x: x * 2
```

Przydaje się wtedy, gdy potrzebujesz krótkiej funkcji „na miejscu”.

Ale jeśli logika robi się większa, zwykłe `def` jest czytelniejsze.

---

## `functools.partial`

`partial` pozwala „zamrozić” część argumentów funkcji.

```python
from functools import partial

def potega(a, b):
    return a ** b

kwadrat = partial(potega, b=2)
print(kwadrat(5))
```

To bardzo praktyczne.

---

## `functools.singledispatch`

To mechanizm pozwalający definiować różne wersje funkcji zależnie od typu pierwszego argumentu.

Przykład idei:

```python
from functools import singledispatch

@singledispatch
def pokaz(x):
    print("Domyslnie:", x)
```

Potem można rejestrować wersje dla konkretnych typów.

To bardzo elegancki sposób na prosty polimorfizm funkcyjny.

---

## Programowanie funkcyjne a Pythonic style

W Pythonie bardzo ważna jest czytelność.

Dlatego:

- czasem `map` i `filter` są świetne,
- a czasem lepsza będzie comprehension,
- czasem `reduce` jest elegancki,
- a czasem zwykła pętla jest bardziej zrozumiała.

Nie chodzi o „czystą doktrynę”, tylko o dobry kod.

---

## Kiedy to podejście ma sens

Gdy:

- transformujesz dane,
- przetwarzasz kolekcje,
- chcesz składać małe funkcje,
- zależy Ci na czystej logice bez efektów ubocznych.

---

## Kiedy przeszkadza

Gdy:

- kod robi się zbyt abstrakcyjny,
- lambdy są zbyt rozbudowane,
- `reduce` utrudnia czytanie,
- kilka prostych linii pętli byłoby jaśniejsze.

---

## Typowe błędy początkujących

- nadużywanie lambd,
- używanie `reduce`, gdzie `sum()` byłoby lepsze,
- ignorowanie tego, że `map` i `filter` zwracają iteratory,
- pisanie kodu „funkcyjnego” kosztem czytelności.

---

## Praktyczne przykłady

### `map`

```python
liczby = [1, 2, 3]
print(list(map(lambda x: x * 10, liczby)))
```

### `filter`

```python
print(list(filter(lambda x: x > 0, [-2, -1, 0, 1, 2])))
```

### `reduce`

```python
from functools import reduce
print(reduce(lambda a, b: a + b, [1, 2, 3, 4]))
```

### `partial`

```python
from functools import partial

def dodaj(a, b):
    return a + b

dodaj5 = partial(dodaj, 5)
print(dodaj5(10))
```

### `singledispatch`

```python
from functools import singledispatch

@singledispatch
def opisz(x):
    print("Nieznany typ")

@opisz.register
def _(x: int):
    print("Liczba:", x)
```

---

## Dobre praktyki

- wybieraj rozwiązanie najbardziej czytelne,
- lambdy stosuj do naprawdę krótkich rzeczy,
- pamiętaj, że comprehension w Pythonie bardzo często wygrywa z `map` i `filter`,
- używaj `partial`, gdy naprawdę upraszcza kod,
- `singledispatch` stosuj tam, gdzie daje realną elegancję.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- Python wspiera wiele narzędzi programowania funkcyjnego,
- najważniejsze to `map`, `filter`, `reduce`, lambdy, `partial`, `singledispatch`,
- trzeba używać ich świadomie i z naciskiem na czytelność.

---

## Mini ściąga

```python
map(f, dane)
filter(f, dane)
reduce(f, dane)
lambda x: ...
partial(f, ...)
@singledispatch
```

---

## Ćwiczenia

### Ćwiczenie 1

Użyj `map`, by podwoić liczby.

### Ćwiczenie 2

Użyj `filter`, by zostawić tylko dodatnie liczby.

### Ćwiczenie 3

Użyj `reduce`, by policzyć iloczyn listy.

### Ćwiczenie 4

Użyj `partial`, by stworzyć funkcję dodającą 10.

---

## Przykładowe rozwiązania

```python
list(map(lambda x: x * 2, [1, 2, 3]))
```

```python
list(filter(lambda x: x > 0, [-2, 0, 3]))
```

```python
from functools import reduce
reduce(lambda a, b: a * b, [1, 2, 3, 4])
```
