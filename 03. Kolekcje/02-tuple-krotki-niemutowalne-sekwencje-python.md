# Tuple w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `tuple`](#czym-jest-tuple)
3. [Dlaczego tuple są ważne](#dlaczego-tuple-są-ważne)
4. [Lista a tuple](#lista-a-tuple)
5. [Jak utworzyć tuple](#jak-utworzyć-tuple)
6. [Pusta krotka](#pusta-krotka)
7. [Jednoelementowa krotka](#jednoelementowa-krotka)
8. [Typy danych wewnątrz tuple](#typy-danych-wewnątrz-tuple)
9. [Indeksy i dostęp do elementów](#indeksy-i-dostęp-do-elementów)
10. [Slicing tuple](#slicing-tuple)
11. [Niemutowalność tuple](#niemutowalność-tuple)
12. [Co można robić z tuple](#co-można-robić-z-tuple)
13. [Operacje na tuple](#operacje-na-tuple)
14. [Metody tuple](#metody-tuple)
15. [Iterowanie po tuple](#iterowanie-po-tuple)
16. [Packing i unpacking](#packing-i-unpacking)
17. [Rozpakowywanie z gwiazdką](#rozpakowywanie-z-gwiazdką)
18. [Zwracanie wielu wartości z funkcji](#zwracanie-wielu-wartości-z-funkcji)
19. [Tuple zagnieżdżone](#tuple-zagnieżdżone)
20. [Tuple a mutowalne elementy w środku](#tuple-a-mutowalne-elementy-w-środku)
21. [Kiedy używać tuple zamiast listy](#kiedy-używać-tuple-zamiast-listy)
22. [Konwersja między listą a tuple](#konwersja-między-listą-a-tuple)
23. [Tuple jako klucze słownika](#tuple-jako-klucze-słownika)
24. [Typowe błędy początkujących](#typowe-błędy-początkujących)
25. [Praktyczne przykłady](#praktyczne-przykłady)
26. [Dobre praktyki](#dobre-praktyki)
27. [Podsumowanie](#podsumowanie)
28. [Mini ściąga](#mini-ściąga)
29. [Ćwiczenia](#ćwiczenia)
30. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`tuple`, czyli po polsku najczęściej **krotka**, to bardzo ważny typ danych w Pythonie.

Na pierwszy rzut oka tuple przypomina listę, bo też przechowuje wiele elementów w kolejności.

Najważniejsza różnica jest taka:

**tuple jest niemutowalna**, czyli po utworzeniu nie można zmieniać jej zawartości tak jak listy.

To sprawia, że tuple są bardzo przydatne, gdy chcesz:

- przechowywać dane, które nie powinny się zmieniać,
- zwracać kilka wartości z funkcji,
- bezpiecznie przekazywać uporządkowany zestaw danych,
- używać sekwencji jako klucza w słowniku.

W tym poradniku przejdziemy przez cały temat prostym językiem, z wieloma przykładami.

---

## Czym jest `tuple`

`tuple` to uporządkowana sekwencja elementów.

Podobnie jak lista:

- zachowuje kolejność,
- ma indeksy,
- można po niej iterować,
- może zawierać różne typy danych.

Ale w przeciwieństwie do listy:

- nie można zmieniać jej elementów po utworzeniu,
- nie można dodawać ani usuwać elementów "w miejscu".

Przykład:

```python
punkt = (10, 20)
```

To krotka składająca się z dwóch wartości.

---

## Dlaczego tuple są ważne

Tuple pojawiają się w Pythonie bardzo często, nawet jeśli na początku tego nie zauważasz.

Są używane między innymi do:

- współrzędnych, na przykład `(x, y)`,
- dat, na przykład `(rok, miesiac, dzien)`,
- zwracania kilku wartości z funkcji,
- przekazywania danych, które nie powinny być zmieniane,
- kluczy w słownikach,
- pracy z danymi o stałej strukturze.

Tuple to nie tylko "lista, której nie da się zmienić".
To bardzo praktyczny sposób reprezentowania stałych, uporządkowanych danych.

---

## Lista a tuple

Porównajmy je:

### Lista

```python
lista = [1, 2, 3]
```

### Tuple

```python
krotka = (1, 2, 3)
```

### Główne różnice

- lista używa `[]`,
- tuple najczęściej używa `()`,
- lista jest mutowalna,
- tuple jest niemutowalna.

### Co to oznacza w praktyce

Lista:

```python
lista[0] = 99
lista.append(4)
```

Tuple:

```python
krotka[0] = 99
```

To da błąd.

---

## Jak utworzyć tuple

Najczęściej tworzy się tuple przy użyciu nawiasów okrągłych:

```python
liczby = (1, 2, 3)
```

### Tuple tekstów

```python
kolory = ("czerwony", "zielony", "niebieski")
```

### Tuple liczb

```python
wspolrzedne = (10, 20)
```

### Tuple mieszana

```python
dane = ("Ania", 17, True, 165.5)
```

---

## Pusta krotka

Pustą krotkę można utworzyć tak:

```python
pusta = ()
```

Można też użyć:

```python
pusta = tuple()
```

---

## Jednoelementowa krotka

To bardzo ważna pułapka.

Jeśli napiszesz:

```python
x = (5)
```

to **nie** jest tuple.

To po prostu liczba `int`.

### Aby utworzyć jednoelementową krotkę, potrzebny jest przecinek

```python
x = (5,)
```

albo:

```python
x = 5,
```

To już jest tuple.

### Sprawdzenie typu

```python
print(type((5)))    # int
print(type((5,)))   # tuple
```

To jedna z najczęstszych pułapek przy nauce tuple.

---

## Typy danych wewnątrz tuple

Tuple może zawierać różne typy danych, tak jak lista.

Przykład:

```python
moja_krotka = (10, "Python", False, 3.14)
```

Może też zawierać inne tuple albo listy:

```python
zagniezdzona = (1, 2, [3, 4], (5, 6))
```

To jest poprawne.

---

## Indeksy i dostęp do elementów

Tuple działa pod tym względem podobnie do listy.

Przykład:

```python
owoce = ("jablko", "banan", "gruszka")

print(owoce[0])   # jablko
print(owoce[1])   # banan
print(owoce[-1])  # gruszka
```

### Zły indeks

```python
print(owoce[10])
```

To da:

```python
IndexError
```

Bo taki element nie istnieje.

---

## Slicing tuple

Tuple obsługuje slicing tak samo jak lista.

Przykład:

```python
liczby = (10, 20, 30, 40, 50)

print(liczby[1:4])
```

Wynik:

```python
(20, 30, 40)
```

### Od początku

```python
print(liczby[:3])
```

### Do końca

```python
print(liczby[2:])
```

### Co drugi element

```python
print(liczby[::2])
```

### Od końca

```python
print(liczby[::-1])
```

Ważne:

slicing tuple zwraca nową tuple.

---

## Niemutowalność tuple

To najważniejsza cecha krotki.

Po utworzeniu tuple nie można:

- zmienić elementu,
- dodać nowego elementu,
- usunąć elementu.

### Przykład błędu

```python
kolory = ("czerwony", "zielony", "niebieski")
kolory[1] = "zolty"
```

To da:

```python
TypeError
```

### Dlaczego to bywa przydatne

Bo masz pewność, że dane nie zostaną przypadkiem zmienione.

---

## Co można robić z tuple

Mimo niemutowalności tuple nadal można:

- odczytywać elementy,
- iterować po elementach,
- sprawdzać długość,
- łączyć tuple,
- powielać tuple,
- używać slicingu,
- sprawdzać obecność elementu,
- liczyć wystąpienia,
- szukać indeksu.

To znaczy, że tuple nie jest "bezużyteczna".
Po prostu służy do trochę innego celu niż lista.

---

## Operacje na tuple

### Łączenie

```python
a = (1, 2)
b = (3, 4)
print(a + b)
```

### Powielanie

```python
print((1, 2) * 3)
```

### Sprawdzanie elementu

```python
print(2 in (1, 2, 3))       # True
print(5 not in (1, 2, 3))   # True
```

### Długość

```python
print(len((10, 20, 30)))
```

### Porównywanie

```python
print((1, 2) == (1, 2))   # True
print((1, 2) == (2, 1))   # False
```

---

## Metody tuple

Tuple ma tylko dwie główne metody:

### `count()`

Liczy, ile razy element występuje.

```python
liczby = (1, 2, 2, 3, 2)
print(liczby.count(2))
```

### `index()`

Zwraca indeks pierwszego wystąpienia.

```python
owoce = ("jablko", "banan", "gruszka")
print(owoce.index("banan"))
```

Jeśli element nie istnieje, pojawi się `ValueError`.

### Dlaczego jest tak mało metod

Bo tuple jest niemutowalna.
Nie potrzebuje metod takich jak:

- `append()`,
- `remove()`,
- `sort()`,
- `clear()`.

---

## Iterowanie po tuple

Po tuple można przechodzić pętlą `for`.

```python
kolory = ("czerwony", "zielony", "niebieski")

for kolor in kolory:
    print(kolor)
```

### Z `enumerate()`

```python
for indeks, kolor in enumerate(kolory):
    print(indeks, kolor)
```

---

## Packing i unpacking

To bardzo ważny i bardzo pythonowy temat.

### Packing

Packing to "pakowanie" kilku wartości do jednej tuple.

```python
dane = 10, 20, 30
print(dane)
```

To automatycznie tworzy tuple:

```python
(10, 20, 30)
```

### Unpacking

Unpacking to rozpakowanie tuple do kilku zmiennych.

```python
punkt = (5, 8)
x, y = punkt

print(x)
print(y)
```

### Bardzo ważna zasada

Liczba zmiennych po lewej musi pasować do liczby elementów po prawej.

To da błąd:

```python
a, b = (1, 2, 3)
```

---

## Rozpakowywanie z gwiazdką

Python pozwala też użyć `*` przy unpackingu.

Przykład:

```python
liczby = (1, 2, 3, 4, 5)
a, *reszta = liczby

print(a)
print(reszta)
```

Wynik:

```python
1
[2, 3, 4, 5]
```

### Uwaga

Element oznaczony `*` staje się listą, nie tuple.

### Inne przykłady

```python
a, b, *reszta = (10, 20, 30, 40, 50)
```

```python
*poczatek, koniec = (1, 2, 3, 4)
```

To bardzo wygodne narzędzie.

---

## Zwracanie wielu wartości z funkcji

To bardzo częsty przypadek użycia tuple.

Przykład:

```python
def dane_osoby():
    return "Ania", 17

wynik = dane_osoby()
print(wynik)
```

Wynik:

```python
('Ania', 17)
```

### Rozpakowanie wyniku

```python
imie, wiek = dane_osoby()
print(imie)
print(wiek)
```

To wygląda tak, jakby funkcja zwracała dwie rzeczy naraz, ale w praktyce bardzo często zwraca tuple.

---

## Tuple zagnieżdżone

Tuple może zawierać inne tuple.

Przykład:

```python
punkty = ((1, 2), (3, 4), (5, 6))
```

### Dostęp do elementów

```python
print(punkty[0])      # (1, 2)
print(punkty[0][1])   # 2
```

To bywa przydatne na przykład przy współrzędnych.

---

## Tuple a mutowalne elementy w środku

To bardzo ważna pułapka.

Tuple sama jest niemutowalna, ale może zawierać obiekty mutowalne.

Przykład:

```python
dane = (1, 2, [3, 4])
```

Nie możesz podmienić elementu tuple:

```python
dane[0] = 99
```

Ale możesz zmienić listę znajdującą się w środku:

```python
dane[2].append(5)
print(dane)
```

Wynik:

```python
(1, 2, [3, 4, 5])
```

### Dlaczego tak

Bo tuple nie pozwala zmienić, który obiekt jest na danej pozycji.
Ale jeśli ten obiekt sam w sobie jest mutowalny, jego wnętrze może się zmienić.

---

## Kiedy używać tuple zamiast listy

Użyj tuple, gdy:

- dane nie powinny się zmieniać,
- kolejność ma znaczenie,
- struktura jest stała,
- chcesz zwrócić kilka wartości z funkcji,
- chcesz użyć sekwencji jako klucza słownika,
- chcesz wyraźnie pokazać, że to zestaw stałych danych.

### Przykłady

- współrzędne punktu: `(x, y)`,
- kolor RGB: `(255, 128, 0)`,
- dane logowania: `("admin", "1234")`,
- data: `(2026, 7, 24)`.

### Kiedy lepiej użyć listy

Gdy planujesz:

- dodawać elementy,
- usuwać elementy,
- zmieniać elementy,
- sortować w miejscu.

---

## Konwersja między listą a tuple

### Z listy do tuple

```python
lista = [1, 2, 3]
krotka = tuple(lista)
print(krotka)
```

### Z tuple do listy

```python
krotka = (1, 2, 3)
lista = list(krotka)
print(lista)
```

### Po co to robić

Czasem chcesz chwilowo zamienić tuple na listę, coś zmienić, a potem znowu zrobić tuple.

Przykład:

```python
krotka = (1, 2, 3)
lista = list(krotka)
lista.append(4)
krotka = tuple(lista)
print(krotka)
```

---

## Tuple jako klucze słownika

Tuple może być kluczem w słowniku, jeśli zawiera tylko hashowalne elementy.

Przykład:

```python
lokacje = {
    (52.23, 21.01): "Warszawa",
    (50.06, 19.94): "Krakow"
}

print(lokacje[(52.23, 21.01)])
```

### Dlaczego lista nie może być kluczem

Bo lista jest mutowalna.

Tuple jest niemutowalna, więc może być używana jako klucz, o ile jej elementy też się do tego nadają.

---

## Typowe błędy początkujących

### 1. Zapomnienie przecinka w jednoelementowej tuple

```python
x = (5)
```

To nie tuple.

### 2. Próba zmiany elementu tuple

```python
krotka[0] = 10
```

To da `TypeError`.

### 3. Mylenie tuple z listą

Tuple nie ma metod takich jak:

- `append()`,
- `remove()`,
- `sort()`.

### 4. Zakładanie, że tuple z listą w środku jest całkowicie "niezmienna"

Wewnętrzna lista nadal może się zmieniać.

### 5. Błąd przy unpackingu

```python
a, b = (1, 2, 3)
```

Za dużo elementów.

### 6. Mylenie nawiasów

To nie nawiasy robią tuple, tylko często **przecinki**.

Na przykład:

```python
x = 1, 2, 3
```

to też tuple.

---

## Praktyczne przykłady

### Współrzędne punktu

```python
punkt = (10, 20)
print(punkt[0])
print(punkt[1])
```

### Zwracanie wielu wartości z funkcji

```python
def policz():
    suma = 2 + 3
    iloczyn = 2 * 3
    return suma, iloczyn

wynik = policz()
print(wynik)
```

### Rozpakowanie zwróconych wartości

```python
suma, iloczyn = policz()
print(suma)
print(iloczyn)
```

### Iteracja po tuple

```python
kolory = ("czerwony", "zielony", "niebieski")

for kolor in kolory:
    print(kolor)
```

### Slicing

```python
liczby = (10, 20, 30, 40, 50)
print(liczby[1:4])
print(liczby[::-1])
```

### Tuple jako klucz

```python
slownik = {
    (1, 1): "start",
    (2, 3): "meta"
}

print(slownik[(1, 1)])
```

---

## Dobre praktyki

### Używaj tuple dla danych o stałej strukturze

Na przykład:

- punkt,
- data,
- para wartości,
- wynik funkcji.

### Używaj list, gdy dane mają się zmieniać

To najprostsza praktyczna zasada.

### Pilnuj jednoelementowych tuple

Przecinek jest obowiązkowy.

### Nie nadpisuj tuple, jeśli semantycznie dane miały być stałe

Technicznie możesz przypisać nową tuple do tej samej zmiennej, ale warto zachować sens nazwy i intencji.

### Uważaj na mutowalne elementy w środku tuple

To częsta pułapka.

### Korzystaj z unpackingu

To jeden z najbardziej eleganckich elementów Pythona.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- `tuple` to uporządkowana, niemutowalna sekwencja,
- działa podobnie do listy przy odczycie, indeksach i slicing,
- nie można zmieniać jej elementów po utworzeniu,
- jednoelementowa tuple wymaga przecinka,
- tuple ma mało metod, głównie `count()` i `index()`,
- świetnie nadaje się do zwracania wielu wartości z funkcji,
- unpacking jest bardzo ważnym zastosowaniem tuple,
- tuple może zawierać obiekty mutowalne, które same mogą się zmieniać,
- tuple bywa lepsza od listy, gdy dane mają być stałe.

Jeśli dobrze zrozumiesz tuple, łatwiej będzie Ci pisać czytelny i bardziej precyzyjny kod w Pythonie.

---

## Mini ściąga

### Tworzenie tuple

```python
krotka = (1, 2, 3)
```

### Jednoelementowa tuple

```python
x = (5,)
```

### Odczyt

```python
krotka[0]
krotka[-1]
```

### Slicing

```python
krotka[1:4]
krotka[:3]
krotka[::2]
krotka[::-1]
```

### Operacje

```python
(1, 2) + (3, 4)
(1, 2) * 2
len((1, 2, 3))
2 in (1, 2, 3)
```

### Metody

```python
krotka.count(2)
krotka.index(3)
```

### Unpacking

```python
a, b = (10, 20)
```

### Konwersja

```python
tuple([1, 2, 3])
list((1, 2, 3))
```

---

## Ćwiczenia

### Ćwiczenie 1

Utwórz tuple z 5 ulubionymi kolorami i wypisz:

- pierwszy element,
- ostatni element,
- długość tuple.

### Ćwiczenie 2

Utwórz jednoelementową tuple i sprawdź jej typ.

### Ćwiczenie 3

Zrób slicing tuple:

- pierwsze 3 elementy,
- ostatnie 2 elementy,
- co drugi element,
- tuple od końca.

### Ćwiczenie 4

Utwórz funkcję, która zwraca imię i wiek jako tuple, a potem rozpakuj wynik do dwóch zmiennych.

### Ćwiczenie 5

Utwórz słownik, w którym kluczami będą tuple współrzędnych.

### Ćwiczenie 6

Sprawdź, co się stanie, gdy w tuple umieścisz listę i zmienisz tę listę.

---

## Przykładowe rozwiązania

### Ćwiczenie 1

```python
kolory = ("czerwony", "zielony", "niebieski", "zolty", "czarny")

print(kolory[0])
print(kolory[-1])
print(len(kolory))
```

### Ćwiczenie 2

```python
x = (5,)
print(type(x))
```

### Ćwiczenie 3

```python
liczby = (10, 20, 30, 40, 50, 60)

print(liczby[:3])
print(liczby[-2:])
print(liczby[::2])
print(liczby[::-1])
```

### Ćwiczenie 4

```python
def dane():
    return "Ania", 17

imie, wiek = dane()
print(imie)
print(wiek)
```

### Ćwiczenie 5

```python
miasta = {
    (52.23, 21.01): "Warszawa",
    (50.06, 19.94): "Krakow"
}

print(miasta[(52.23, 21.01)])
```

### Ćwiczenie 6

```python
dane = (1, 2, [3, 4])
dane[2].append(5)

print(dane)
```

---

## Na koniec

Tuple najlepiej zrozumieć przez porównywanie ich z listami.

Warto:

1. tworzyć tuple obok list i porównywać zachowanie,
2. ćwiczyć slicing i unpacking,
3. sprawdzać, kiedy tuple daje błąd przy modyfikacji,
4. testować jednoelementowe tuple,
5. używać tuple tam, gdzie dane naprawdę mają być stałe.

Wtedy bardzo szybko staje się jasne, po co ten typ istnieje i kiedy naprawdę warto go używać.
