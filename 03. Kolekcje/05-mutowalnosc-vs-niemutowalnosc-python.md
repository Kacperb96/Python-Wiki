# Mutowalność vs Niemutowalność w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest mutowalność](#czym-jest-mutowalność)
3. [Czym jest niemutowalność](#czym-jest-niemutowalność)
4. [Dlaczego ten temat jest ważny](#dlaczego-ten-temat-jest-ważny)
5. [Najważniejsze typy mutowalne](#najważniejsze-typy-mutowalne)
6. [Najważniejsze typy niemutowalne](#najważniejsze-typy-niemutowalne)
7. [Jak rozumieć zmianę obiektu](#jak-rozumieć-zmianę-obiektu)
8. [Mutowalność a przypisanie](#mutowalność-a-przypisanie)
9. [Mutowalność a funkcje](#mutowalność-a-funkcje)
10. [Mutowalność a kopiowanie](#mutowalność-a-kopiowanie)
11. [Mutowalność a klucze słownika](#mutowalność-a-klucze-słownika)
12. [Mutowalność a elementy zbioru](#mutowalność-a-elementy-zbioru)
13. [Pułapka z domyślnymi argumentami funkcji](#pułapka-z-domyślnymi-argumentami-funkcji)
14. [Pułapka z listą w tuple](#pułapka-z-listą-w-tuple)
15. [Pułapka z mnożeniem list zagnieżdżonych](#pułapka-z-mnożeniem-list-zagnieżdżonych)
16. [Konsekwencje praktyczne](#konsekwencje-praktyczne)
17. [Kiedy mutowalność pomaga](#kiedy-mutowalność-pomaga)
18. [Kiedy niemutowalność pomaga](#kiedy-niemutowalność-pomaga)
19. [Typowe błędy początkujących](#typowe-błędy-początkujących)
20. [Praktyczne przykłady](#praktyczne-przykłady)
21. [Dobre praktyki](#dobre-praktyki)
22. [Podsumowanie](#podsumowanie)
23. [Mini ściąga](#mini-ściąga)
24. [Ćwiczenia](#ćwiczenia)
25. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Mutowalność i niemutowalność to jeden z najważniejszych tematów w Pythonie.

Od tego zależy między innymi:

- czy obiekt można zmienić po utworzeniu,
- jak działa przypisanie,
- jak działa kopiowanie,
- dlaczego niektóre typy mogą być kluczami słownika, a inne nie,
- skąd biorą się niektóre bardzo podstępne błędy.

To temat, który wpływa na prawie wszystko:

- listy,
- tuple,
- słowniki,
- zbiory,
- funkcje,
- kopiowanie danych.

---

## Czym jest mutowalność

Mutowalność oznacza, że obiekt można zmienić po jego utworzeniu.

Przykład:

```python
lista = [1, 2, 3]
lista.append(4)
print(lista)
```

Ta sama lista została zmieniona.

Nie powstał nowy obiekt w sensie, który nas tu interesuje.

---

## Czym jest niemutowalność

Niemutowalność oznacza, że obiektu nie można zmienić po utworzeniu.

Przykład:

```python
tekst = "kot"
tekst = tekst + "ek"
print(tekst)
```

To nie zmienia starego stringa "w miejscu".
Powstaje nowa wartość.

---

## Dlaczego ten temat jest ważny

Bo wpływa na:

- działanie funkcji,
- działanie przypisania,
- kopiowanie,
- bezpieczeństwo danych,
- zachowanie struktur zagnieżdżonych.

Bez tego tematu wiele rzeczy w Pythonie wygląda "magicznie".
Po jego zrozumieniu stają się logiczne.

---

## Najważniejsze typy mutowalne

Najczęściej:

- `list`
- `dict`
- `set`

Przykłady:

```python
lista = [1, 2, 3]
slownik = {"a": 1}
zbior = {1, 2, 3}
```

Każdy z tych obiektów można zmieniać po utworzeniu.

---

## Najważniejsze typy niemutowalne

Najczęściej:

- `int`
- `float`
- `bool`
- `str`
- `tuple`

Przykłady:

```python
x = 10
tekst = "Python"
krotka = (1, 2, 3)
```

Tych obiektów nie zmieniasz "w miejscu".

---

## Jak rozumieć zmianę obiektu

To bardzo ważne rozróżnienie:

### Zmiana obiektu

```python
lista = [1, 2]
lista.append(3)
```

### Przypisanie nowej wartości do nazwy

```python
x = 10
x = 20
```

W drugim przykładzie nie zmieniasz starego `10`.
Po prostu nazwa `x` zaczyna wskazywać na `20`.

---

## Mutowalność a przypisanie

### Typ niemutowalny

```python
a = 10
b = a
b = 20

print(a)
print(b)
```

`a` pozostaje bez zmian.

### Typ mutowalny

```python
a = [1, 2, 3]
b = a
b.append(4)

print(a)
print(b)
```

Obie nazwy widzą zmianę, bo wskazują na ten sam obiekt.

---

## Mutowalność a funkcje

To bardzo ważne w praktyce.

### Lista przekazana do funkcji

```python
def dodaj_element(lista):
    lista.append(100)

dane = [1, 2, 3]
dodaj_element(dane)
print(dane)
```

Oryginalna lista się zmieni.

### String przekazany do funkcji

```python
def zmien(tekst):
    tekst = tekst + "!"

napis = "Hej"
zmien(napis)
print(napis)
```

Oryginalny string się nie zmieni.

---

## Mutowalność a kopiowanie

To bardzo silnie powiązane tematy.

Jeśli obiekt jest mutowalny i przekażesz tylko referencję do niego, zmiany mogą być widoczne w wielu miejscach.

Przykład:

```python
a = [1, 2, 3]
b = a
b.append(4)
```

Jeśli chcesz osobny obiekt, musisz zrobić kopię.

---

## Mutowalność a klucze słownika

Klucze słownika muszą być hashowalne, a więc zwykle niemutowalne.

Dlatego działa:

```python
d = {"imie": "Ania"}
```

ale nie działa:

```python
d = {[1, 2]: "lista"}
```

Lista jest mutowalna, więc nie może być kluczem.

---

## Mutowalność a elementy zbioru

Podobnie jest ze zbiorem.

Elementy zbioru też muszą być hashowalne.

Dlatego działa:

```python
zbior = {(1, 2), (3, 4)}
```

ale nie działa:

```python
zbior = {[1, 2], [3, 4]}
```

---

## Pułapka z domyślnymi argumentami funkcji

To bardzo ważny klasyczny problem.

Przykład:

```python
def dodaj(element, lista=[]):
    lista.append(element)
    return lista
```

Na pierwszy rzut oka wygląda dobrze, ale:

```python
print(dodaj(1))
print(dodaj(2))
print(dodaj(3))
```

wynik może być zaskakujący, bo ta sama lista domyślna jest współdzielona między wywołaniami.

### Poprawny wzorzec

```python
def dodaj(element, lista=None):
    if lista is None:
        lista = []
    lista.append(element)
    return lista
```

To jedna z najważniejszych praktycznych konsekwencji mutowalności.

---

## Pułapka z listą w tuple

Tuple jest niemutowalna, ale może zawierać obiekt mutowalny.

Przykład:

```python
dane = (1, 2, [3, 4])
dane[2].append(5)
print(dane)
```

To zadziała.

Nie zmieniasz samej struktury tuple, tylko listę w środku.

---

## Pułapka z mnożeniem list zagnieżdżonych

Przykład:

```python
macierz = [[0] * 3] * 2
macierz[0][0] = 99
print(macierz)
```

To może zmienić więcej niż jeden wiersz, bo wewnętrzne listy są współdzielone.

To też jest konsekwencja mutowalności i współdzielenia referencji.

---

## Konsekwencje praktyczne

Mutowalność wpływa na:

- bezpieczeństwo danych,
- kopiowanie,
- przekazywanie argumentów,
- zachowanie struktur zagnieżdżonych,
- możliwość użycia obiektu jako klucza lub elementu zbioru.

To nie jest tylko teoria.
To temat, który bardzo często decyduje, czy kod zachowuje się tak, jak oczekujesz.

---

## Kiedy mutowalność pomaga

Mutowalność jest wygodna, gdy:

- chcesz dopisywać elementy do listy,
- aktualizujesz słownik,
- budujesz dane krok po kroku,
- chcesz efektywnie modyfikować strukturę.

Przykład:

```python
wyniki = []
wyniki.append(10)
wyniki.append(20)
```

---

## Kiedy niemutowalność pomaga

Niemutowalność jest wygodna, gdy:

- chcesz mieć pewność, że dane się nie zmienią,
- potrzebujesz bezpieczniejszych struktur,
- chcesz używać obiektu jako klucza słownika,
- chcesz uniknąć przypadkowych modyfikacji.

Przykład:

```python
punkt = (10, 20)
```

To dobry kandydat na dane stałe.

---

## Typowe błędy początkujących

### 1. Zakładanie, że `a = b` tworzy kopię mutowalnego obiektu

Nie tworzy.

### 2. Niezrozumienie, czemu lista zmienia się po wywołaniu funkcji

Bo funkcja mogła zmienić ten sam obiekt.

### 3. Próba użycia listy jako klucza słownika

To nie działa.

### 4. Zakładanie, że tuple z listą w środku jest całkowicie "niezmienna"

Nie jest.

### 5. Używanie mutowalnych domyślnych argumentów funkcji

To klasyczna pułapka.

---

## Praktyczne przykłady

### Lista jako typ mutowalny

```python
lista = [1, 2, 3]
lista.append(4)
print(lista)
```

### String jako typ niemutowalny

```python
tekst = "kot"
tekst = tekst + "ek"
print(tekst)
```

### Funkcja modyfikująca listę

```python
def dodaj_zero(lista):
    lista.append(0)

dane = [1, 2]
dodaj_zero(dane)
print(dane)
```

### Funkcja ze stringiem

```python
def dodaj_wykrzyknik(tekst):
    tekst = tekst + "!"

napis = "Hej"
dodaj_wykrzyknik(napis)
print(napis)
```

### Tuple z listą

```python
dane = (1, [2, 3])
dane[1].append(4)
print(dane)
```

---

## Dobre praktyki

### Rozpoznawaj, z jakim typem pracujesz

To pierwszy krok do uniknięcia błędów.

### Uważaj przy przekazywaniu mutowalnych obiektów do funkcji

Funkcja może zmienić oryginał.

### Nie używaj mutowalnych domyślnych argumentów

To jedna z najważniejszych zasad praktycznych.

### Używaj niemutowalnych typów tam, gdzie dane mają być stałe

Na przykład `tuple` dla współrzędnych czy stałych rekordów.

### Jeśli potrzebujesz niezależności danych, kopiuj je świadomie

Nie zakładaj, że Python zrobi to za Ciebie.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- mutowalne obiekty można zmieniać po utworzeniu,
- niemutowalne obiekty nie zmieniają się "w miejscu",
- `list`, `dict`, `set` są mutowalne,
- `int`, `float`, `bool`, `str`, `tuple` są niemutowalne,
- mutowalność wpływa na przypisanie, funkcje i kopiowanie,
- listy nie mogą być kluczami słownika ani elementami zwykłego zbioru,
- bardzo ważna jest pułapka z domyślnymi argumentami funkcji.

Jeśli dobrze opanujesz ten temat, zaczniesz dużo lepiej rozumieć zachowanie danych w Pythonie.

---

## Mini ściąga

### Mutowalne

```python
list
dict
set
```

### Niemutowalne

```python
int
float
bool
str
tuple
```

### Typowa pułapka

```python
a = [1, 2]
b = a
b.append(3)
```

### Bezpieczniejszy wzorzec funkcji

```python
def f(lista=None):
    if lista is None:
        lista = []
```

---

## Ćwiczenia

### Ćwiczenie 1

Sprawdź różnicę między zachowaniem listy i stringa po przekazaniu do funkcji.

### Ćwiczenie 2

Spróbuj użyć listy jako klucza słownika i zobacz, jaki błąd się pojawi.

### Ćwiczenie 3

Utwórz tuple zawierającą listę i sprawdź, czy da się zmienić listę w środku.

### Ćwiczenie 4

Napisz funkcję z błędnym domyślnym argumentem listowym, a potem popraw ją.

### Ćwiczenie 5

Sprawdź, co się stanie po:

```python
macierz = [[0] * 3] * 2
```

i zmianie jednego elementu.

---

## Przykładowe rozwiązania

### Ćwiczenie 1

```python
def zmien_liste(lista):
    lista.append(99)

def zmien_tekst(tekst):
    tekst = tekst + "!"

a = [1, 2]
b = "Hej"

zmien_liste(a)
zmien_tekst(b)

print(a)
print(b)
```

### Ćwiczenie 2

```python
# d = {[1, 2]: "blad"}  # TypeError
```

### Ćwiczenie 3

```python
dane = (1, [2, 3])
dane[1].append(4)
print(dane)
```

### Ćwiczenie 4

```python
def zla_funkcja(x, lista=[]):
    lista.append(x)
    return lista

def dobra_funkcja(x, lista=None):
    if lista is None:
        lista = []
    lista.append(x)
    return lista
```

### Ćwiczenie 5

```python
macierz = [[0] * 3] * 2
macierz[0][0] = 99
print(macierz)
```

---

## Na koniec

Najlepszy sposób nauki mutowalności to eksperymenty na małych przykładach.

Warto:

1. porównywać listy i tuple,
2. porównywać listy i stringi,
3. testować funkcje z mutowalnymi argumentami,
4. sprawdzać, kiedy zmiana jednego obiektu wpływa na drugi.

Właśnie na takich przykładach ten temat zaczyna być naprawdę intuicyjny.
