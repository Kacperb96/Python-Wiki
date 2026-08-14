# Magic Methods w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym są magic methods](#czym-są-magic-methods)
3. [Dlaczego są ważne](#dlaczego-są-ważne)
4. [`__str__`](#__str__)
5. [`__repr__`](#__repr__)
6. [Różnica między `__str__` i `__repr__`](#różnica-między-__str__-i-__repr__)
7. [`__len__`](#__len__)
8. [`__getitem__`](#__getitem__)
9. [`__setitem__`](#__setitem__)
10. [`__contains__`](#__contains__)
11. [`__eq__`](#__eq__)
12. [`__hash__`](#__hash__)
13. [Jak Python używa magic methods](#jak-python-używa-magic-methods)
14. [Własne obiekty zachowujące się jak kolekcje](#własne-obiekty-zachowujące-się-jak-kolekcje)
15. [Spójność `__eq__` i `__hash__`](#spójność-__eq__-i-__hash__)
16. [Typowe błędy początkujących](#typowe-błędy-początkujących)
17. [Praktyczne przykłady](#praktyczne-przykłady)
18. [Dobre praktyki](#dobre-praktyki)
19. [Podsumowanie](#podsumowanie)
20. [Mini ściąga](#mini-ściąga)
21. [Ćwiczenia](#ćwiczenia)
22. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Magic methods, nazywane też czasem dunder methods, to metody specjalne w Pythonie.

Nazywają się tak, bo mają postać:

```python
__nazwa__
```

To dzięki nim Twoje obiekty mogą zachowywać się jak wbudowane typy.

Na przykład:

- ładnie się wypisywać,
- działać z `len()`,
- wspierać indeksowanie,
- wspierać `in`,
- porównywać się przez `==`,
- działać jako klucze słownika.

---

## Czym są magic methods

To specjalne metody, które Python wywołuje automatycznie w określonych sytuacjach.

Przykład:

```python
len(obiekt)
```

powoduje użycie:

```python
obiekt.__len__()
```

---

## Dlaczego są ważne

Bo pozwalają tworzyć klasy, które są:

- wygodne w użyciu,
- bardziej naturalne,
- zgodne ze stylem Pythona.

Dzięki nim własna klasa może zachowywać się jak:

- lista,
- słownik,
- tekst,
- liczba,
- rekord danych.

---

## `__str__`

Służy do czytelnego tekstowego przedstawienia obiektu dla użytkownika.

Przykład:

```python
class Osoba:
    def __init__(self, imie):
        self.imie = imie

    def __str__(self):
        return f"Osoba: {self.imie}"
```

Teraz:

```python
print(Osoba("Ania"))
```

da czytelny wynik.

Output:

```python
Osoba: Ania
```

---

## `__repr__`

Służy do bardziej technicznego przedstawienia obiektu.

Przykład:

```python
class Osoba:
    def __init__(self, imie):
        self.imie = imie

    def __repr__(self):
        return f"Osoba(imie={self.imie!r})"
```

```python
print(Osoba("Ania"))
```

Output:

```python
Osoba(imie='Ania')
```

---

## Różnica między `__str__` i `__repr__`

### `__str__`

- dla użytkownika,
- bardziej przyjazne,
- bardziej "ludzkie".

### `__repr__`

- dla programisty,
- bardziej techniczne,
- przydatne przy debugowaniu.

Jeśli nie ma `__str__`, Python często używa `__repr__`.

To znaczy:

- `__str__` jest bardziej dla człowieka,
- `__repr__` bardziej dla programisty i debugowania.

---

## `__len__`

Pozwala obsługiwać:

```python
len(obiekt)
```

Przykład:

```python
class MojaLista:
    def __init__(self, dane):
        self.dane = dane

    def __len__(self):
        return len(self.dane)
```

```python
print(len(MojaLista([1, 2, 3])))
```

Output:

```python
3
```

---

## `__getitem__`

Pozwala obsługiwać:

```python
obiekt[index]
```

Przykład:

```python
class MojaLista:
    def __init__(self, dane):
        self.dane = dane

    def __getitem__(self, index):
        return self.dane[index]
```

To wspiera też często slicing.

```python
lista = MojaLista([10, 20, 30])
print(lista[1])
```

Output:

```python
20
```

---

## `__setitem__`

Pozwala obsługiwać:

```python
obiekt[index] = wartosc
```

Przykład:

```python
class MojaLista:
    def __init__(self, dane):
        self.dane = list(dane)

    def __setitem__(self, index, value):
        self.dane[index] = value
```

```python
lista = MojaLista([1, 2, 3])
lista[0] = 99
print(lista.dane)
```

Output:

```python
[99, 2, 3]
```

---

## `__contains__`

Pozwala kontrolować działanie:

```python
x in obiekt
```

Przykład:

```python
class MojaLista:
    def __init__(self, dane):
        self.dane = dane

    def __contains__(self, item):
        return item in self.dane
```

```python
lista = MojaLista([1, 2, 3])
print(2 in lista)
print(5 in lista)
```

Output:

```python
True
False
```

---

## `__eq__`

Definiuje porównanie:

```python
a == b
```

Przykład:

```python
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

```python
print(Punkt(1, 2) == Punkt(1, 2))
```

Output:

```python
True
```

---

## `__hash__`

Odpowiada za hashowanie obiektu.

To ważne, jeśli obiekt ma być:

- kluczem słownika,
- elementem zbioru.

Przykład:

```python
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Punkt) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))
```

```python
punkty = {Punkt(1, 2), Punkt(1, 2)}
print(len(punkty))
```

Output:

```python
1
```

---

## Jak Python używa magic methods

Przykłady:

- `print(obj)` -> `__str__`
- `repr(obj)` -> `__repr__`
- `len(obj)` -> `__len__`
- `obj[i]` -> `__getitem__`
- `obj[i] = x` -> `__setitem__`
- `x in obj` -> `__contains__`
- `a == b` -> `__eq__`
- `hash(obj)` -> `__hash__`

To właśnie dzięki temu dobrze napisane obiekty zachowują się naturalnie i "po pythonowemu".

---

## Własne obiekty zachowujące się jak kolekcje

To bardzo ważne zastosowanie.

Jeśli zaimplementujesz odpowiednie magic methods, Twoja klasa może wyglądać dla użytkownika jak lista albo mapa.

---

## Spójność `__eq__` i `__hash__`

To bardzo ważne.

Jeśli dwa obiekty są równe przez `==`, to ich hash też powinien być taki sam.

Inaczej słowniki i zbiory mogą działać niepoprawnie.

---

## Typowe błędy początkujących

### 1. Mylenie `__str__` i `__repr__`

### 2. Pisanie `__eq__` bez sprawdzenia typu `other`

### 3. Implementacja `__eq__` bez przemyślenia `__hash__`

### 4. Oczekiwanie, że magic methods trzeba wywoływać ręcznie

Zwykle Python robi to sam.

### 5. Brak sprawdzenia typu `other` w `__eq__`

To może prowadzić do dziwnych błędów przy porównaniu z innym obiektem.

---

## Praktyczne przykłady

### Ładne wypisywanie

```python
class Ksiazka:
    def __init__(self, tytul):
        self.tytul = tytul

    def __str__(self):
        return f"Ksiazka: {self.tytul}"
```

```python
print(Ksiazka("Python"))
```

Output:

```python
Ksiazka: Python
```

### Własna kolekcja

```python
class Pudelko:
    def __init__(self, dane):
        self.dane = list(dane)

    def __len__(self):
        return len(self.dane)

    def __getitem__(self, index):
        return self.dane[index]
```

```python
p = Pudelko(["a", "b", "c"])
print(len(p))
print(p[0])
```

Output:

```python
3
a
```

### Porównywanie punktów

```python
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Punkt) and self.x == other.x and self.y == other.y
```

```python
print(Punkt(1, 1) == Punkt(1, 1))
```

Output:

```python
True
```

---

## Dobre praktyki

### Implementuj tylko te magic methods, które naprawdę mają sens

### Dbaj o spójność zachowania

### `__repr__` rób pomocne w debugowaniu

### Jeśli definiujesz `__eq__`, przemyśl też `__hash__`

Praktyczna zasada:

najpierw zastanów się, jakie zachowanie obiektu byłoby naturalne dla użytkownika klasy, a dopiero potem dobieraj magic methods.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- magic methods to specjalne metody automatycznie używane przez Pythona,
- dzięki nim własne klasy mogą działać bardziej naturalnie,
- `__str__`, `__repr__`, `__len__`, `__getitem__`, `__setitem__`, `__contains__`, `__eq__`, `__hash__` należą do najważniejszych.

Najważniejsze do zapamiętania:

- `__str__` i `__repr__` wpływają na wypisywanie,
- `__len__` daje `len()`,
- `__getitem__` daje indeksowanie,
- `__contains__` daje `in`,
- `__eq__` i `__hash__` wpływają na porównanie i użycie w zbiorach lub słownikach.

---

## Mini ściąga

```python
__str__
__repr__
__len__
__getitem__
__setitem__
__contains__
__eq__
__hash__
```

---

## Ćwiczenia

### Ćwiczenie 1

Utwórz klasę z `__str__`.

### Ćwiczenie 2

Utwórz klasę wspierającą `len()`.

### Ćwiczenie 3

Utwórz klasę wspierającą indeksowanie.

### Ćwiczenie 4

Utwórz klasę `Punkt` z `__eq__`.

---

## Przykładowe rozwiązania

### Ćwiczenie 1

```python
class Produkt:
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def __str__(self):
        return f"Produkt: {self.nazwa}"
```

### Ćwiczenie 2

```python
class Dane:
    def __init__(self, elementy):
        self.elementy = elementy

    def __len__(self):
        return len(self.elementy)
```

### Ćwiczenie 3

```python
class Dane:
    def __init__(self, elementy):
        self.elementy = elementy

    def __getitem__(self, index):
        return self.elementy[index]
```

### Ćwiczenie 4

```python
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Punkt) and self.x == other.x and self.y == other.y
```
