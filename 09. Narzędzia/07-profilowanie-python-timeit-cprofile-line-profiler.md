# Profilowanie w Pythonie — `timeit`, `cProfile`, `line_profiler`

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co profilować kod](#po-co-profilować-kod)
3. [Nie zgaduj — mierz](#nie-zgaduj--mierz)
4. [`timeit`](#timeit)
5. [Kiedy używać `timeit`](#kiedy-używać-timeit)
6. [`cProfile`](#cprofile)
7. [Kiedy używać `cProfile`](#kiedy-używać-cprofile)
8. [`line_profiler`](#line_profiler)
9. [Kiedy używać `line_profiler`](#kiedy-używać-line_profiler)
10. [Różnica między timingiem a profilowaniem](#różnica-między-timingiem-a-profilowaniem)
11. [Typowe pułapki wydajnościowe](#typowe-pułapki-wydajnościowe)
12. [Jak czytać wyniki profilera](#jak-czytać-wyniki-profilera)
13. [Typowe błędy początkujących](#typowe-błędy-początkujących)
14. [Praktyczne przykłady](#praktyczne-przykłady)
15. [Dobre praktyki](#dobre-praktyki)
16. [Podsumowanie](#podsumowanie)
17. [Mini ściąga](#mini-ściąga)
18. [Ćwiczenia](#ćwiczenia)
19. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Profilowanie to mierzenie wydajności kodu.

Najważniejsza zasada:

**nie zgaduj, co jest wolne — zmierz to.**

Bardzo często intuicja programisty jest błędna i optymalizuje nie to miejsce, które naprawdę spowalnia program.

W Pythonie podstawowe narzędzia to:

- `timeit`
- `cProfile`
- `line_profiler`

---

## Po co profilować kod

Bo profilowanie pomaga odpowiedzieć:

- która funkcja jest wolna,
- ile razy została wywołana,
- która linia zużywa najwięcej czasu,
- czy optymalizacja naprawdę coś poprawiła.

---

## Nie zgaduj — mierz

To jedna z najważniejszych profesjonalnych zasad.

Bez pomiaru łatwo:

- optymalizować nieistotne miejsce,
- tracić czas,
- komplikować kod bez realnego zysku.

---

## `timeit`

`timeit` służy do mierzenia czasu małych fragmentów kodu.

Przykład:

```python
import timeit

wynik = timeit.timeit("sum(range(100))", number=10000)
print(wynik)
```

---

## Kiedy używać `timeit`

Gdy:

- porównujesz dwa małe rozwiązania,
- chcesz sprawdzić, który zapis jest szybszy,
- mierzysz mały fragment kodu.

To narzędzie dobre do mikrobenchmarków.

---

## `cProfile`

`cProfile` profiluje wykonanie programu lub funkcji.

Pokazuje:

- które funkcje ile czasu zajmują,
- ile razy były wywołane,
- gdzie są główne koszty.

Przykład:

```python
import cProfile

def policz():
    return sum(range(100000))

cProfile.run("policz()")
```

---

## Kiedy używać `cProfile`

Gdy:

- chcesz zobaczyć ogólny obraz wydajności,
- analizujesz większy fragment programu,
- szukasz wolnych funkcji.

---

## `line_profiler`

`line_profiler` mierzy czas na poziomie pojedynczych linii kodu.

To bardzo przydatne, gdy wiesz już, która funkcja jest wolna, i chcesz znaleźć dokładnie które linie są problemem.

To narzędzie nie jest wbudowane standardowo, ale jest bardzo znane i praktyczne.

---

## Kiedy używać `line_profiler`

Gdy:

- `cProfile` wskazał podejrzaną funkcję,
- chcesz zejść o poziom niżej,
- potrzebujesz bardzo precyzyjnej analizy.

---

## Różnica między timingiem a profilowaniem

### Timing

Mierzy czas wykonania fragmentu kodu.

### Profilowanie

Rozkłada ten czas na części i pokazuje, gdzie znika.

---

## Typowe pułapki wydajnościowe

- optymalizacja zbyt wcześnie,
- brak pomiaru przed i po zmianie,
- skupianie się na małych detalach zamiast dużych wąskich gardeł,
- ignorowanie złożoności algorytmicznej.

---

## Jak czytać wyniki profilera

Najważniejsze pytania:

- które funkcje zużywają najwięcej czasu,
- które funkcje są wywoływane bardzo często,
- czy koszt leży w jednej funkcji, czy rozkłada się na wiele.

---

## Typowe błędy początkujących

- mylenie `timeit` z pełnym profilerem,
- brak powtarzalnych pomiarów,
- porównywanie wyników bez kontroli środowiska,
- skupienie na mikrooptymalizacji zamiast na ważnych problemach.

---

## Praktyczne przykłady

### `timeit`

```python
import timeit

print(timeit.timeit("x * x", setup="x=10", number=1000000))
```

### `cProfile`

```python
import cProfile

def licz():
    for _ in range(10000):
        sum(range(100))

cProfile.run("licz()")
```

---

## Dobre praktyki

- najpierw sprawdź, czy naprawdę masz problem z wydajnością,
- zacznij od `cProfile`, gdy problem jest większy,
- używaj `timeit` do małych porównań,
- optymalizuj dopiero po pomiarze,
- po każdej zmianie mierz ponownie.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- `timeit` mierzy czas małych fragmentów,
- `cProfile` pokazuje koszt funkcji w większym obrazie,
- `line_profiler` pozwala zejść do poziomu linii,
- dobra optymalizacja zaczyna się od pomiaru.

---

## Mini ściąga

```python
import timeit
timeit.timeit("kod", number=1000)
```

```python
import cProfile
cProfile.run("funkcja()")
```

---

## Ćwiczenia

### Ćwiczenie 1

Zmierz `timeit`, ile trwa `sum(range(100))`.

### Ćwiczenie 2

Uruchom prostą funkcję przez `cProfile`.

### Ćwiczenie 3

Porównaj dwa sposoby tworzenia listy i zmierz je.

---

## Przykładowe rozwiązania

```python
import timeit
print(timeit.timeit("sum(range(100))", number=10000))
```
