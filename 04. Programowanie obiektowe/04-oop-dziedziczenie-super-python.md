# Dziedziczenie i `super()` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest dziedziczenie](#czym-jest-dziedziczenie)
3. [Po co używać dziedziczenia](#po-co-używać-dziedziczenia)
4. [Klasa bazowa i klasa pochodna](#klasa-bazowa-i-klasa-pochodna)
5. [Podstawowa składnia dziedziczenia](#podstawowa-składnia-dziedziczenia)
6. [Dziedziczenie metod](#dziedziczenie-metod)
7. [Nadpisywanie metod](#nadpisywanie-metod)
8. [Dodawanie nowych metod](#dodawanie-nowych-metod)
9. [Czym jest `super()`](#czym-jest-super)
10. [`super()` w `__init__`](#super-w-__init__)
11. [`super()` w zwykłych metodach](#super-w-zwykłych-metodach)
12. [Dlaczego `super()` jest lepsze niż ręczne wywołanie klasy bazowej](#dlaczego-super-jest-lepsze-niż-ręczne-wywołanie-klasy-bazowej)
13. [Wielopoziomowe dziedziczenie](#wielopoziomowe-dziedziczenie)
14. [Wielodziedziczenie - krótki wstęp](#wielodziedziczenie---krótki-wstęp)
15. [MRO - Method Resolution Order](#mro---method-resolution-order)
16. [Typowe błędy początkujących](#typowe-błędy-początkujących)
17. [Praktyczne przykłady](#praktyczne-przykłady)
18. [Dobre praktyki](#dobre-praktyki)
19. [Podsumowanie](#podsumowanie)
20. [Mini ściąga](#mini-ściąga)
21. [Ćwiczenia](#ćwiczenia)
22. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Dziedziczenie to jeden z najbardziej znanych elementów OOP.

Pozwala tworzyć nowe klasy na podstawie już istniejących.

Dzięki temu:

- nie powtarzasz kodu,
- możesz rozszerzać zachowanie klasy,
- budujesz naturalne relacje typu:
  - zwierzę -> pies,
  - pojazd -> samochód,
  - konto -> konto oszczędnościowe.

W Pythonie bardzo ważnym narzędziem związanym z dziedziczeniem jest też `super()`.

---

## Czym jest dziedziczenie

Dziedziczenie oznacza, że jedna klasa przejmuje cechy innej klasy.

Przykład:

jeśli mamy klasę:

```python
class Zwierze:
    ...
```

to klasa:

```python
class Pies(Zwierze):
    ...
```

dziedziczy po `Zwierze`.

---

## Po co używać dziedziczenia

Główne powody:

- współdzielenie kodu,
- unikanie duplikacji,
- budowanie hierarchii typów,
- rozszerzanie już istniejących klas.

---

## Klasa bazowa i klasa pochodna

### Klasa bazowa

To klasa, z której dziedziczymy.

### Klasa pochodna

To klasa, która dziedziczy po bazowej.

Przykład:

```python
class Zwierze:
    pass

class Pies(Zwierze):
    pass
```

`Zwierze` to baza, `Pies` to klasa pochodna.

---

## Podstawowa składnia dziedziczenia

```python
class Zwierze:
    def oddychaj(self):
        print("Oddycham")

class Pies(Zwierze):
    pass
```

Teraz:

```python
azor = Pies()
azor.oddychaj()
```

zadziała, mimo że `Pies` nie definiuje własnej metody `oddychaj`.

---

## Dziedziczenie metod

Klasa pochodna automatycznie dostaje metody klasy bazowej, jeśli ich nie nadpisze.

To właśnie jedna z głównych zalet dziedziczenia.

---

## Nadpisywanie metod

Klasa pochodna może zdefiniować własną wersję metody.

```python
class Zwierze:
    def dzwiek(self):
        print("Jakis dzwiek")

class Pies(Zwierze):
    def dzwiek(self):
        print("Hau hau")
```

To nazywa się nadpisywanie metody.

---

## Dodawanie nowych metod

Klasa pochodna może też mieć własne dodatkowe metody.

```python
class Pies(Zwierze):
    def dzwiek(self):
        print("Hau hau")

    def aportuj(self):
        print("Przynosze pilke")
```

---

## Czym jest `super()`

`super()` pozwala odwołać się do klasy bazowej w elegancki i bezpieczny sposób.

Najczęściej używa się go do:

- wywołania `__init__` klasy bazowej,
- rozszerzania istniejącej metody zamiast całkowitego zastępowania jej.

---

## `super()` w `__init__`

Przykład:

```python
class Zwierze:
    def __init__(self, imie):
        self.imie = imie

class Pies(Zwierze):
    def __init__(self, imie, rasa):
        super().__init__(imie)
        self.rasa = rasa
```

Tutaj:

- klasa bazowa ustawia `imie`,
- klasa pochodna dodaje `rasa`.

---

## `super()` w zwykłych metodach

Przykład:

```python
class Zwierze:
    def przedstaw_sie(self):
        print("Jestem zwierzeciem")

class Pies(Zwierze):
    def przedstaw_sie(self):
        super().przedstaw_sie()
        print("I jestem psem")
```

To pozwala rozszerzyć zachowanie bazowe.

---

## Dlaczego `super()` jest lepsze niż ręczne wywołanie klasy bazowej

Można by pisać:

```python
Zwierze.__init__(self, imie)
```

ale `super()` jest lepsze, bo:

- działa bardziej elegancko,
- wspiera poprawnie bardziej złożone hierarchie,
- jest ważne przy wielodziedziczeniu.

---

## Wielopoziomowe dziedziczenie

Przykład:

```python
class Istota:
    pass

class Zwierze(Istota):
    pass

class Pies(Zwierze):
    pass
```

To dziedziczenie wielopoziomowe.

---

## Wielodziedziczenie - krótki wstęp

Python pozwala dziedziczyć po więcej niż jednej klasie.

```python
class A:
    pass

class B:
    pass

class C(A, B):
    pass
```

To temat bardziej zaawansowany i trzeba z nim uważać.

---

## MRO - Method Resolution Order

To kolejność, w jakiej Python szuka metod w hierarchii dziedziczenia.

Można ją sprawdzić:

```python
print(Pies.__mro__)
```

albo:

```python
print(Pies.mro())
```

To szczególnie ważne przy wielodziedziczeniu.

---

## Typowe błędy początkujących

### 1. Zapominanie o wywołaniu `super().__init__()`

### 2. Nadpisanie metody bez zrozumienia, że traci się zachowanie bazowe

### 3. Nadużywanie dziedziczenia tam, gdzie lepsza byłaby kompozycja

### 4. Mylenie "jest rodzajem" z "ma w sobie"

To bardzo ważne projektowo.

---

## Praktyczne przykłady

### Proste dziedziczenie

```python
class Zwierze:
    def jedz(self):
        print("Jem")

class Kot(Zwierze):
    def miaucz(self):
        print("Miau")
```

### `super()` w `__init__`

```python
class Pojazd:
    def __init__(self, marka):
        self.marka = marka

class Samochod(Pojazd):
    def __init__(self, marka, model):
        super().__init__(marka)
        self.model = model
```

### Rozszerzenie metody

```python
class Ptak:
    def ruch(self):
        print("Poruszam sie")

class Orzel(Ptak):
    def ruch(self):
        super().ruch()
        print("I latam")
```

---

## Dobre praktyki

### Używaj dziedziczenia, gdy istnieje relacja "jest rodzajem"

### Używaj `super()` zamiast ręcznego wywołania klasy bazowej

### Nie buduj zbyt głębokich hierarchii bez potrzeby

### Zastanów się, czy dziedziczenie naprawdę jest najlepszym wyborem

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- dziedziczenie pozwala tworzyć klasy na podstawie innych klas,
- klasa pochodna może dziedziczyć, nadpisywać i rozszerzać metody,
- `super()` pozwala elegancko odwoływać się do klasy bazowej,
- dziedziczenie jest potężne, ale trzeba używać go świadomie.

---

## Mini ściąga

```python
class A:
    def __init__(self, x):
        self.x = x

class B(A):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
```

---

## Ćwiczenia

### Ćwiczenie 1

Utwórz klasę `Pojazd` z metodą `jedz`.

### Ćwiczenie 2

Utwórz klasę `Rower`, która dziedziczy po `Pojazd`.

### Ćwiczenie 3

Dodaj `__init__` do klasy bazowej i pochodnej z użyciem `super()`.

---

## Przykładowe rozwiązania

### Ćwiczenie 1

```python
class Pojazd:
    def jedz(self):
        print("Jade")
```

### Ćwiczenie 2

```python
class Rower(Pojazd):
    def dzwon(self):
        print("Dzyń dzyń")
```

### Ćwiczenie 3

```python
class Pojazd:
    def __init__(self, marka):
        self.marka = marka

class Rower(Pojazd):
    def __init__(self, marka, typ):
        super().__init__(marka)
        self.typ = typ
```
