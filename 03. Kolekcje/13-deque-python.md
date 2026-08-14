# deque w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `deque`](#czym-jest-deque)
3. [Skąd importować `deque`](#skad-importowac-deque)
4. [Dlaczego `deque` istnieje, skoro jest lista](#dlaczego-deque-istnieje-skoro-jest-lista)
5. [Tworzenie `deque`](#tworzenie-deque)
6. [Dodawanie elementów](#dodawanie-elementow)
7. [`appendleft()`](#appendleft)
8. [Usuwanie elementów](#usuwanie-elementow)
9. [`popleft()`](#popleft)
10. [`deque` jako kolejka FIFO](#deque-jako-kolejka-fifo)
11. [`deque` jako stos LIFO](#deque-jako-stos-lifo)
12. [`extend()` i `extendleft()`](#extend-i-extendleft)
13. [Ważna pułapka `extendleft()`](#wazna-pulapka-extendleft)
14. [`rotate()`](#rotate)
15. [Ograniczona długość `maxlen`](#ograniczona-dlugosc-maxlen)
16. [Złożoność operacji](#zlozonosc-operacji)
17. [Kiedy używać `deque`](#kiedy-uzywac-deque)
18. [Kiedy lista jest lepsza](#kiedy-lista-jest-lepsza)
19. [Typowe błędy początkujących](#typowe-bledy-poczatkujacych)
20. [Praktyczne przykłady](#praktyczne-przyklady)
21. [Dobre praktyki](#dobre-praktyki)
22. [Podsumowanie](#podsumowanie)
23. [Mini ściąga](#mini-sciaga)
24. [Ćwiczenia](#cwiczenia)
25. [Przykładowe rozwiązania](#przykladowe-rozwiazania)

---

## Wprowadzenie

`deque` to bardzo przydatna struktura danych z modułu `collections`.

Nazwa pochodzi od:

**double-ended queue**

czyli kolejki dwustronnej.

Najważniejsza idea:

**możesz sprawnie dodawać i usuwać elementy z obu końców.**

To brzmi niepozornie, ale w praktyce bywa dużo lepsze od listy.

---

## Czym jest `deque`

To kolejka dwustronna.

Przykład:

```python
from collections import deque

d = deque([1, 2, 3])
print(d)
```

Wynik:

```python
deque([1, 2, 3])
```

`deque` wygląda podobnie do listy, ale ma trochę inne zastosowanie.

---

## Skąd importować `deque`

```python
from collections import deque
```

---

## Dlaczego `deque` istnieje, skoro jest lista

Lista jest świetna, gdy:

- dodajesz na koniec przez `append()`,
- usuwasz z końca przez `pop()`,
- chcesz często indeksować elementy.

Ale jeśli często robisz:

```python
lista.insert(0, x)
lista.pop(0)
```

to lista nie jest do tego najlepszym narzędziem.

`deque` został stworzony właśnie po to, żeby wygodnie pracować z początkiem i końcem kolekcji.

---

## Tworzenie `deque`

```python
from collections import deque

d = deque([1, 2, 3])
print(d)
```

Wynik:

```python
deque([1, 2, 3])
```

Pusta kolejka:

```python
d = deque()
print(d)
```

Wynik:

```python
deque([])
```

---

## Dodawanie elementów

### Na koniec

```python
from collections import deque

d = deque([1, 2, 3])
d.append(4)
print(d)
```

Wynik:

```python
deque([1, 2, 3, 4])
```

### Na początek

```python
d.appendleft(0)
print(d)
```

Wynik:

```python
deque([0, 1, 2, 3, 4])
```

---

## `appendleft()`

Dodaje element na lewy koniec.

```python
from collections import deque

d = deque([2, 3, 4])
d.appendleft(1)
print(d)
```

Wynik:

```python
deque([1, 2, 3, 4])
```

To jedna z najważniejszych metod `deque`.

---

## Usuwanie elementów

### Z końca

```python
from collections import deque

d = deque([1, 2, 3])
print(d.pop())
print(d)
```

Wynik:

```python
3
deque([1, 2])
```

### Z początku

```python
print(d.popleft())
print(d)
```

Wynik:

```python
1
deque([2])
```

---

## `popleft()`

To odpowiednik `pop(0)` dla listy, ale dużo bardziej naturalny dla kolejki.

```python
from collections import deque

d = deque([10, 20, 30])
print(d.popleft())
print(d)
```

Wynik:

```python
10
deque([20, 30])
```

---

## `deque` jako kolejka FIFO

FIFO oznacza:

**first in, first out**

czyli pierwszy dodany wychodzi pierwszy.

```python
from collections import deque

kolejka = deque()
kolejka.append("A")
kolejka.append("B")
kolejka.append("C")

print(kolejka.popleft())
print(kolejka.popleft())
print(kolejka)
```

Wynik:

```python
A
B
deque(['C'])
```

To klasyczne zastosowanie `deque`.

---

## `deque` jako stos LIFO

LIFO oznacza:

**last in, first out**

czyli ostatni dodany wychodzi pierwszy.

```python
from collections import deque

stos = deque()
stos.append("A")
stos.append("B")
stos.append("C")

print(stos.pop())
print(stos.pop())
print(stos)
```

Wynik:

```python
C
B
deque(['A'])
```

---

## `extend()` i `extendleft()`

### `extend()`

Dodaje wiele elementów na koniec.

```python
from collections import deque

d = deque([1, 2, 3])
d.extend([4, 5])
print(d)
```

Wynik:

```python
deque([1, 2, 3, 4, 5])
```

### `extendleft()`

Dodaje wiele elementów na początek.

```python
d = deque([3, 4])
d.extendleft([2, 1])
print(d)
```

Wynik:

```python
deque([1, 2, 3, 4])
```

I tu pojawia się pułapka.

---

## Ważna pułapka `extendleft()`

`extendleft()` dodaje elementy kolejno na lewą stronę, więc finalnie kolejność jest odwrócona względem wejściowej iteracji.

```python
from collections import deque

d = deque([10])
d.extendleft([1, 2, 3])
print(d)
```

Wynik:

```python
deque([3, 2, 1, 10])
```

Wiele osób spodziewa się:

```python
deque([1, 2, 3, 10])
```

ale to nie ten mechanizm.

---

## `rotate()`

Przesuwa elementy cyklicznie.

### Obrót w prawo

```python
from collections import deque

d = deque([1, 2, 3, 4])
d.rotate(1)
print(d)
```

Wynik:

```python
deque([4, 1, 2, 3])
```

### Obrót w lewo

```python
d.rotate(-2)
print(d)
```

Wynik:

```python
deque([2, 3, 4, 1])
```

To przydaje się na przykład przy cyklicznych buforach albo prostych algorytmach kolejkowych.

---

## Ograniczona długość `maxlen`

Możesz stworzyć `deque`, które pamięta tylko ostatnie `N` elementów.

```python
from collections import deque

historia = deque(maxlen=3)
historia.append("A")
historia.append("B")
historia.append("C")
print(historia)

historia.append("D")
print(historia)
```

Wynik:

```python
deque(['A', 'B', 'C'], maxlen=3)
deque(['B', 'C', 'D'], maxlen=3)
```

Najstarszy element wypada automatycznie.

To świetne do:

- historii ostatnich akcji,
- buforów,
- ostatnich logów,
- ruchomego okna.

---

## Złożoność operacji

Najważniejsze praktycznie:

- `append()` i `pop()` na końcu są szybkie,
- `appendleft()` i `popleft()` na początku też są szybkie,
- `deque` jest dużo lepsze od listy do operacji na początku.

Nie traktuj jednak `deque` jako zamiennika listy do wszystkiego.

---

## Kiedy używać `deque`

Używaj `deque`, gdy:

- budujesz kolejkę,
- budujesz stos,
- często dodajesz lub usuwasz elementy z obu końców,
- potrzebujesz bufora o stałej długości,
- pracujesz na historii ostatnich zdarzeń.

---

## Kiedy lista jest lepsza

Lista bywa lepsza, gdy:

- potrzebujesz częstego indeksowania,
- chcesz sortować dane,
- pracujesz głównie na końcu kolekcji,
- chcesz prostszy, bardziej powszechny typ danych.

---

## Typowe błędy początkujących

### 1. Używanie listy jako kolejki z `pop(0)`

Da się, ale `deque` jest do tego lepsze.

### 2. Niezrozumienie `extendleft()`

Wynikowa kolejność może zaskoczyć.

### 3. Traktowanie `deque` jak zwykłej listy do wszystkiego

To narzędzie do konkretnych zastosowań.

### 4. Zapominanie o `maxlen`

A to jedna z najfajniejszych funkcji `deque`.

---

## Praktyczne przykłady

### Prosta kolejka zadań

```python
from collections import deque

zadania = deque(["mail", "raport", "backup"])

while zadania:
    aktualne = zadania.popleft()
    print(f"Realizuje: {aktualne}")
```

Wynik:

```python
Realizuje: mail
Realizuje: raport
Realizuje: backup
```

### Historia ostatnich 5 działań

```python
from collections import deque

historia = deque(maxlen=5)

for krok in range(1, 8):
    historia.append(f"akcja-{krok}")

print(historia)
```

Wynik:

```python
deque(['akcja-3', 'akcja-4', 'akcja-5', 'akcja-6', 'akcja-7'], maxlen=5)
```

---

## Dobre praktyki

- Używaj `deque` do kolejki i historii zdarzeń.
- Używaj `popleft()` zamiast `pop(0)` na liście.
- Pamiętaj o pułapce `extendleft()`.
- Rozważ `maxlen`, gdy interesuje Cię tylko ostatnie `N` elementów.
- Nie zamieniaj listy na `deque` bez powodu.

---

## Podsumowanie

`deque` to kolejka dwustronna z modułu `collections`.

Najbardziej przydaje się wtedy, gdy:

- dodajesz i usuwasz z obu końców,
- budujesz FIFO albo LIFO,
- potrzebujesz bufora o stałej długości.

Najważniejsze do zapamiętania:

**`deque` nie jest “lepszą listą”, tylko narzędziem do trochę innych zadań.**

---

## Mini ściąga

```python
from collections import deque

d = deque([1, 2, 3])
d.append(4)
d.appendleft(0)
d.pop()
d.popleft()
d.rotate(1)

historia = deque(maxlen=5)
```

---

## Ćwiczenia

1. Zbuduj kolejkę FIFO przez `deque`.
2. Zbuduj stos LIFO przez `deque`.
3. Pokaż różnicę między `append()` i `appendleft()`.
4. Pokaż pułapkę `extendleft()`.
5. Zbuduj historię ostatnich 3 działań przez `deque(maxlen=3)`.

---

## Przykładowe rozwiązania

```python
from collections import deque

kolejka = deque()
kolejka.append("A")
kolejka.append("B")
kolejka.append("C")

print(kolejka.popleft())
print(kolejka)
```

```python
from collections import deque

historia = deque(maxlen=3)

for i in range(5):
    historia.append(i)

print(historia)
```
