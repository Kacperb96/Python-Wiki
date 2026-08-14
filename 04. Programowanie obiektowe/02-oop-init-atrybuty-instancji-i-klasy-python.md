# `__init__`, atrybuty instancji i klasy w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co istnieje `__init__`](#po-co-istnieje-__init__)
3. [Czym jest konstruktor w Pythonie](#czym-jest-konstruktor-w-pythonie)
4. [Jak działa `__init__`](#jak-działa-__init__)
5. [Pierwszy przykład z `__init__`](#pierwszy-przykład-z-__init__)
6. [Atrybuty instancji](#atrybuty-instancji)
7. [Atrybuty klasy](#atrybuty-klasy)
8. [Różnica między atrybutem instancji a klasy](#różnica-między-atrybutem-instancji-a-klasy)
9. [Dostęp do atrybutów](#dostęp-do-atrybutów)
10. [Modyfikacja atrybutów](#modyfikacja-atrybutów)
11. [Wartości domyślne w `__init__`](#wartości-domyślne-w-__init__)
12. [Pułapki z mutowalnymi wartościami](#pułapki-z-mutowalnymi-wartościami)
13. [Metody instancji a dane obiektu](#metody-instancji-a-dane-obiektu)
14. [Czy `__init__` coś zwraca](#czy-__init__-coś-zwraca)
15. [Typowe błędy początkujących](#typowe-błędy-początkujących)
16. [Praktyczne przykłady](#praktyczne-przykłady)
17. [Dobre praktyki](#dobre-praktyki)
18. [Podsumowanie](#podsumowanie)
19. [Mini ściąga](#mini-ściąga)
20. [Ćwiczenia](#ćwiczenia)
21. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Kiedy zaczynasz pisać klasy, bardzo szybko pojawia się temat:

- `__init__`
- atrybutów instancji
- atrybutów klasy

To absolutny fundament OOP w Pythonie.

Bez tego trudno budować obiekty, które mają własne dane.

---

## Po co istnieje `__init__`

`__init__` służy do przygotowania nowego obiektu po jego utworzeniu.

Najczęściej:

- zapisujesz w nim dane początkowe,
- ustawiasz atrybuty,
- przygotowujesz stan obiektu.

---

## Czym jest konstruktor w Pythonie

W praktyce początkującego najczęściej mówi się, że `__init__` to konstruktor.

Bardziej precyzyjnie:

- obiekt jest tworzony wcześniej,
- `__init__` go inicjalizuje.

Na początku wystarczy jednak myśleć:

`__init__` uruchamia się przy tworzeniu obiektu i ustawia jego dane.

---

## Jak działa `__init__`

Przykład:

```python
class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek
```

Przy tworzeniu:

```python
ania = Osoba("Ania", 17)
```

Python wywoła `__init__` i ustawi dane obiektu.

---

## Pierwszy przykład z `__init__`

```python
class Pies:
    def __init__(self, imie):
        self.imie = imie

azor = Pies("Azor")
print(azor.imie)
```

Wynik:

```python
Azor
```

---

## Atrybuty instancji

To dane należące do konkretnego obiektu.

Przykład:

```python
class Osoba:
    def __init__(self, imie):
        self.imie = imie
```

`self.imie` to atrybut instancji.

Każdy obiekt może mieć własną wartość:

```python
a = Osoba("Ania")
b = Osoba("Bartek")
```

---

## Atrybuty klasy

To dane współdzielone przez wszystkie obiekty klasy, jeśli nie zostaną nadpisane na poziomie instancji.

Przykład:

```python
class Pies:
    gatunek = "pies"
```

`gatunek` to atrybut klasy.

---

## Różnica między atrybutem instancji a klasy

### Atrybut instancji

- należy do konkretnego obiektu,
- zwykle ustawiany w `__init__`,
- może mieć inną wartość dla każdego obiektu.

### Atrybut klasy

- należy do klasy,
- jest wspólny dla obiektów,
- dobry dla danych wspólnych.

---

## Dostęp do atrybutów

### Atrybut instancji

```python
print(a.imie)
```

### Atrybut klasy

```python
print(Pies.gatunek)
print(azor.gatunek)
```

Obiekt też może odczytać atrybut klasy.

---

## Modyfikacja atrybutów

### Zmiana atrybutu instancji

```python
a.imie = "Anna"
```

### Zmiana atrybutu klasy

```python
Pies.gatunek = "canis familiaris"
```

### Uwaga

Jeśli zrobisz:

```python
azor.gatunek = "inne"
```

to utworzysz atrybut instancji, który zasłoni atrybut klasy dla tego obiektu.

---

## Wartości domyślne w `__init__`

Można ustawić domyślne argumenty:

```python
class Konto:
    def __init__(self, saldo=0):
        self.saldo = saldo
```

Teraz:

```python
k1 = Konto()
k2 = Konto(100)
```

---

## Pułapki z mutowalnymi wartościami

To bardzo ważne.

Źle:

```python
class Zespol:
    def __init__(self, osoby=[]):
        self.osoby = osoby
```

Lepiej:

```python
class Zespol:
    def __init__(self, osoby=None):
        if osoby is None:
            osoby = []
        self.osoby = osoby
```

To ta sama pułapka co przy funkcjach.

---

## Metody instancji a dane obiektu

Metody bardzo często używają atrybutów instancji.

```python
class Konto:
    def __init__(self, saldo):
        self.saldo = saldo

    def pokaz_saldo(self):
        print(self.saldo)
```

---

## Czy `__init__` coś zwraca

Nie powinien zwracać wartości.

Nie pisze się:

```python
return cos
```

w `__init__`.

Jego zadaniem jest inicjalizacja obiektu, nie zwracanie wyniku.

---

## Typowe błędy początkujących

### 1. Zapominanie o `self`

### 2. Pisanie `imie = imie` zamiast `self.imie = imie`

### 3. Mylenie atrybutów klasy i instancji

### 4. Używanie mutowalnych domyślnych wartości

### 5. Próba zwracania czegoś z `__init__`

---

## Praktyczne przykłady

### Osoba

```python
class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

ania = Osoba("Ania", 17)
print(ania.imie)
print(ania.wiek)
```

### Klasa z atrybutem klasy

```python
class Ptak:
    gatunek = "ptak"

    def __init__(self, imie):
        self.imie = imie
```

### Wspólna wartość

```python
a = Ptak("Koko")
b = Ptak("Lolo")

print(a.gatunek)
print(b.gatunek)
```

---

## Dobre praktyki

### Dane obiektu trzymaj w atrybutach instancji

### Dane wspólne trzymaj w atrybutach klasy

### Uważaj na mutowalne wartości domyślne

### Nadawaj atrybutom czytelne nazwy

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- `__init__` inicjalizuje obiekt,
- atrybuty instancji należą do konkretnego obiektu,
- atrybuty klasy są współdzielone,
- `self.imie = imie` to bardzo ważny wzorzec,
- trzeba uważać na mutowalne wartości domyślne.

---

## Mini ściąga

```python
class Osoba:
    gatunek = "czlowiek"

    def __init__(self, imie):
        self.imie = imie
```

---

## Ćwiczenia

### Ćwiczenie 1

Utwórz klasę `Samochod` z `__init__`, która zapisuje markę i rok.

### Ćwiczenie 2

Dodaj atrybut klasy `typ = "pojazd"`.

### Ćwiczenie 3

Utwórz dwa obiekty i pokaż różnicę między atrybutem instancji a klasy.

---

## Przykładowe rozwiązania

### Ćwiczenie 1

```python
class Samochod:
    def __init__(self, marka, rok):
        self.marka = marka
        self.rok = rok
```

### Ćwiczenie 2

```python
class Samochod:
    typ = "pojazd"

    def __init__(self, marka, rok):
        self.marka = marka
        self.rok = rok
```

### Ćwiczenie 3

```python
a = Samochod("Toyota", 2020)
b = Samochod("BMW", 2021)

print(a.marka, a.typ)
print(b.marka, b.typ)
```
