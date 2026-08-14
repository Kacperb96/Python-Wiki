# namedtuple w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `namedtuple`](#czym-jest-namedtuple)
3. [Skąd importować `namedtuple`](#skad-importowac-namedtuple)
4. [Po co używać `namedtuple`](#po-co-uzywac-namedtuple)
5. [Tuple a `namedtuple`](#tuple-a-namedtuple)
6. [Tworzenie `namedtuple`](#tworzenie-namedtuple)
7. [Dostęp do pól](#dostep-do-pol)
8. [Dostęp przez indeks](#dostep-przez-indeks)
9. [Niemutowalność `namedtuple`](#niemutowalnosc-namedtuple)
10. [Rozpakowywanie](#rozpakowywanie)
11. [`_asdict()`](#_asdict)
12. [`_replace()`](#_replace)
13. [`_fields`](#_fields)
14. [`namedtuple` a `dict`](#namedtuple-a-dict)
15. [`namedtuple` a `dataclass`](#namedtuple-a-dataclass)
16. [Kiedy używać `namedtuple`](#kiedy-uzywac-namedtuple)
17. [Typowe błędy początkujących](#typowe-bledy-poczatkujacych)
18. [Praktyczne przykłady](#praktyczne-przyklady)
19. [Dobre praktyki](#dobre-praktyki)
20. [Podsumowanie](#podsumowanie)
21. [Mini ściąga](#mini-sciaga)
22. [Ćwiczenia](#cwiczenia)
23. [Przykładowe rozwiązania](#przykladowe-rozwiazania)

---

## Wprowadzenie

`namedtuple` to wygodny sposób tworzenia krotek z nazwanymi polami.

Zwykła krotka:

```python
punkt = (10, 20)
```

działa, ale trzeba pamiętać:

- indeks `0` to `x`,
- indeks `1` to `y`.

`namedtuple` pozwala zapisać to czytelniej:

```python
punkt.x
punkt.y
```

To mała rzecz, ale czytelność bardzo rośnie.

---

## Czym jest `namedtuple`

To specjalny typ krotki z nazwami pól.

Łączy zalety:

- tuple,
- lekkiego rekordu danych,
- czytelnego dostępu po nazwach.

Najprościej:

**`namedtuple` to “tuple, której pola mają sensowne nazwy”.**

---

## Skąd importować `namedtuple`

```python
from collections import namedtuple
```

---

## Po co używać `namedtuple`

Bo poprawia czytelność bez rezygnowania z prostoty tuple.

Zamiast:

```python
osoba = ("Ania", 19, "Gdansk")
print(osoba[0])
print(osoba[1])
```

możesz mieć:

```python
print(osoba.imie)
print(osoba.wiek)
```

To jest dużo bardziej czytelne dla człowieka.

---

## Tuple a `namedtuple`

### Zwykła tuple

```python
punkt = (10, 20)
print(punkt[0])
print(punkt[1])
```

Wynik:

```python
10
20
```

### `namedtuple`

```python
from collections import namedtuple

Punkt = namedtuple("Punkt", ["x", "y"])
punkt = Punkt(10, 20)

print(punkt.x)
print(punkt.y)
```

Wynik:

```python
10
20
```

Wynik ten sam, ale druga wersja mówi dużo więcej o danych.

---

## Tworzenie `namedtuple`

```python
from collections import namedtuple

Punkt = namedtuple("Punkt", ["x", "y"])
p = Punkt(10, 20)
print(p)
```

Wynik:

```python
Punkt(x=10, y=20)
```

Można też przekazać pola jako string:

```python
Punkt = namedtuple("Punkt", "x y")
```

Najpierw tworzysz typ, a dopiero potem jego instancje.

---

## Dostęp do pól

```python
from collections import namedtuple

Uzytkownik = namedtuple("Uzytkownik", ["imie", "wiek", "miasto"])
u = Uzytkownik("Ania", 19, "Gdansk")

print(u.imie)
print(u.wiek)
print(u.miasto)
```

Wynik:

```python
Ania
19
Gdansk
```

To główna zaleta `namedtuple`.

---

## Dostęp przez indeks

`namedtuple` nadal jest tuple, więc indeksowanie też działa.

```python
print(u[0])
print(u[1])
print(u[2])
```

Wynik:

```python
Ania
19
Gdansk
```

Dzięki temu `namedtuple` zachowuje zgodność z krotkami.

---

## Niemutowalność `namedtuple`

`namedtuple` jest niemutowalne, tak jak zwykła tuple.

```python
from collections import namedtuple

Punkt = namedtuple("Punkt", ["x", "y"])
p = Punkt(10, 20)

# p.x = 99
```

Taki zapis skończy się błędem:

```python
AttributeError
```

To ważne, bo `namedtuple` nie służy do obiektów, które często zmieniasz.

---

## Rozpakowywanie

Możesz rozpakować `namedtuple` jak zwykłą krotkę.

```python
x, y = p
print(x)
print(y)
```

Wynik:

```python
10
20
```

---

## `_asdict()`

Pozwala zamienić `namedtuple` na słownik.

```python
print(u._asdict())
```

Wynik:

```python
{'imie': 'Ania', 'wiek': 19, 'miasto': 'Gdansk'}
```

To bardzo przydatne, gdy chcesz:

- zserializować dane,
- przekazać je dalej jako słownik,
- łatwo je wypisać.

---

## `_replace()`

Ponieważ `namedtuple` jest niemutowalne, nie zmieniasz go w miejscu.

Możesz jednak utworzyć nową wersję:

```python
nowy = u._replace(wiek=20)
print(u)
print(nowy)
```

Wynik:

```python
Uzytkownik(imie='Ania', wiek=19, miasto='Gdansk')
Uzytkownik(imie='Ania', wiek=20, miasto='Gdansk')
```

Stary obiekt zostaje bez zmian.

---

## `_fields`

Zwraca nazwy pól.

```python
print(u._fields)
```

Wynik:

```python
('imie', 'wiek', 'miasto')
```

To wygodne przy introspekcji albo prostym generowaniu opisów.

---

## `namedtuple` a `dict`

### `dict`

- mutowalny,
- bardzo elastyczny,
- może mieć dynamiczne klucze.

### `namedtuple`

- niemutowalny,
- ma stałą strukturę,
- pola są znane z góry,
- jest czytelniejszy niż tuple z indeksami.

Jeśli struktura danych jest stała, `namedtuple` bywa lepszy niż słownik.

---

## `namedtuple` a `dataclass`

`namedtuple` jest prostsze i lżejsze.

`dataclass` daje więcej:

- mutowalność lub niemutowalność do wyboru,
- typowanie,
- metody,
- wartości domyślne,
- łatwiejsze rozszerzanie.

W praktyce:

- `namedtuple` jest świetny do małych, lekkich rekordów,
- `dataclass` częściej wygrywa przy bardziej rozbudowanych modelach danych.

---

## Kiedy używać `namedtuple`

Używaj, gdy:

- masz małą, stałą strukturę danych,
- chcesz czytelności większej niż zwykła tuple,
- nie potrzebujesz mutowalności,
- chcesz coś lekkiego i prostego.

Przykłady:

- punkt 2D,
- rekord użytkownika,
- wynik funkcji,
- para współrzędnych,
- prosty obiekt konfiguracyjny.

---

## Typowe błędy początkujących

### 1. Mylenie klasy z instancją

Najpierw tworzysz typ:

```python
Punkt = namedtuple("Punkt", ["x", "y"])
```

Potem tworzysz obiekt:

```python
p = Punkt(10, 20)
```

### 2. Oczekiwanie mutowalności

`namedtuple` jest niemutowalne.

### 3. Nadużywanie `namedtuple` tam, gdzie lepszy byłby `dataclass`

Jeśli obiekt ma dużo logiki i zmian stanu, `namedtuple` nie jest najlepszym wyborem.

### 4. Używanie indeksów mimo nazw pól

Jeśli masz już `namedtuple`, zwykle lepiej czytać pola po nazwie.

---

## Praktyczne przykłady

### Punkt 2D

```python
from collections import namedtuple

Punkt = namedtuple("Punkt", ["x", "y"])
p = Punkt(3, 7)

print(p)
print(p.x)
print(p[1])
```

Wynik:

```python
Punkt(x=3, y=7)
3
7
```

### Dane użytkownika

```python
from collections import namedtuple

Uzytkownik = namedtuple("Uzytkownik", ["imie", "email"])
u = Uzytkownik("Jan", "jan@example.com")

print(u.email)
print(u._asdict())
```

Wynik:

```python
jan@example.com
{'imie': 'Jan', 'email': 'jan@example.com'}
```

---

## Dobre praktyki

- Używaj `namedtuple` do prostych, stałych rekordów.
- Czytaj pola po nazwie, nie po indeksie, jeśli zależy Ci na czytelności.
- Używaj `_replace()`, gdy chcesz “zmodyfikowaną kopię”.
- Jeśli obiekt ma rosnąć w złożoność, rozważ `dataclass`.

---

## Podsumowanie

`namedtuple` to lekka, czytelna wersja tuple z nazwanymi polami.

Najważniejsze rzeczy do zapamiętania:

- zachowuje się jak tuple,
- można czytać pola po nazwie,
- jest niemutowalne,
- świetnie nadaje się do małych rekordów danych.

---

## Mini ściąga

```python
from collections import namedtuple

Punkt = namedtuple("Punkt", ["x", "y"])
p = Punkt(10, 20)

print(p.x)
print(p[0])
print(p._asdict())
print(p._replace(x=99))
print(p._fields)
```

---

## Ćwiczenia

1. Utwórz `namedtuple` opisujący punkt 2D.
2. Utwórz `namedtuple` opisujący użytkownika.
3. Pokaż różnicę między dostępem po nazwie pola i po indeksie.
4. Użyj `_asdict()`.
5. Użyj `_replace()` do stworzenia nowego obiektu z jedną zmienioną wartością.

---

## Przykładowe rozwiązania

```python
from collections import namedtuple

Punkt = namedtuple("Punkt", ["x", "y"])
p = Punkt(5, 8)

print(p.x)
print(p.y)
print(p._asdict())
```

```python
from collections import namedtuple

Osoba = namedtuple("Osoba", ["imie", "wiek"])
o = Osoba("Ania", 19)
nowa = o._replace(wiek=20)

print(o)
print(nowa)
```
