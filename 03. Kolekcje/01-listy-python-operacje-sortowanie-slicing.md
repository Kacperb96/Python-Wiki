# Listy w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest lista](#czym-jest-lista)
3. [Dlaczego listy są tak ważne](#dlaczego-listy-są-tak-ważne)
4. [Jak utworzyć listę](#jak-utworzyć-listę)
5. [Typy danych wewnątrz listy](#typy-danych-wewnątrz-listy)
6. [Indeksy w liście](#indeksy-w-liście)
7. [Odczytywanie elementów](#odczytywanie-elementów)
8. [Zmiana elementów listy](#zmiana-elementów-listy)
9. [Dodawanie elementów](#dodawanie-elementów)
10. [Usuwanie elementów](#usuwanie-elementów)
11. [Podstawowe operacje na listach](#podstawowe-operacje-na-listach)
12. [Sprawdzanie długości listy](#sprawdzanie-długości-listy)
13. [Sprawdzanie obecności elementu](#sprawdzanie-obecności-elementu)
14. [Łączenie i powielanie list](#łączenie-i-powielanie-list)
15. [Iterowanie po liście](#iterowanie-po-liście)
16. [Przydatne metody list](#przydatne-metody-list)
17. [Sortowanie list](#sortowanie-list)
18. [Sortowanie rosnące i malejące](#sortowanie-rosnące-i-malejące)
19. [Różnica między `sort()` a `sorted()`](#różnica-między-sort-a-sorted)
20. [Sortowanie z `key`](#sortowanie-z-key)
21. [Slicing list](#slicing-list)
22. [Slicing z krokiem](#slicing-z-krokiem)
23. [Odwracanie listy](#odwracanie-listy)
24. [Kopiowanie list](#kopiowanie-list)
25. [Listy zagnieżdżone](#listy-zagnieżdżone)
26. [Mutowalność list](#mutowalność-list)
27. [Typowe błędy początkujących](#typowe-błędy-początkujących)
28. [Praktyczne przykłady](#praktyczne-przykłady)
29. [Dobre praktyki](#dobre-praktyki)
30. [Podsumowanie](#podsumowanie)
31. [Mini ściąga](#mini-ściąga)
32. [Ćwiczenia](#ćwiczenia)
33. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Lista to jeden z najważniejszych typów danych w Pythonie.

Jeśli nauczysz się dobrze pracować z listami, będziesz umiał:

- przechowywać wiele wartości w jednym miejscu,
- dodawać i usuwać elementy,
- przetwarzać dane w pętlach,
- sortować dane,
- wycinać fragmenty listy,
- budować bardziej złożone programy.

Listy pojawiają się praktycznie wszędzie:

- w prostych ćwiczeniach,
- w pracy z danymi,
- w aplikacjach webowych,
- w automatyzacji,
- w analizie danych.

To jeden z absolutnych fundamentów Pythona.

---

## Czym jest lista

Lista to uporządkowana kolekcja elementów.

Najprościej:

**lista pozwala przechowywać wiele wartości pod jedną nazwą.**

Przykład:

```python
owoce = ["jablko", "banan", "gruszka"]
```

Tutaj `owoce` to lista zawierająca 3 elementy.

### Cechy listy

- zachowuje kolejność elementów,
- można ją zmieniać,
- może zawierać różne typy danych,
- może zawierać duplikaty.

---

## Dlaczego listy są tak ważne

Bez list musiałbyś tworzyć osobną zmienną dla każdej wartości.

Na przykład:

```python
imie1 = "Ania"
imie2 = "Bartek"
imie3 = "Celina"
```

To szybko staje się niewygodne.

Z listą jest dużo lepiej:

```python
imiona = ["Ania", "Bartek", "Celina"]
```

I możesz łatwo przejść po wszystkich elementach:

```python
for imie in imiona:
    print(imie)
```

---

## Jak utworzyć listę

Listę tworzy się za pomocą nawiasów kwadratowych:

```python
liczby = [1, 2, 3, 4, 5]
```

### Pusta lista

```python
pusta = []
```

### Lista tekstów

```python
kolory = ["czerwony", "zielony", "niebieski"]
```

### Lista liczb

```python
oceny = [5, 4, 3, 5, 2]
```

### Lista mieszana

```python
dane = ["Ala", 25, True, 175.5]
```

To działa, choć w praktyce często lepiej trzymać dane bardziej uporządkowane.

---

## Typy danych wewnątrz listy

Lista może zawierać:

- liczby,
- teksty,
- wartości logiczne,
- inne listy,
- a nawet różne typy naraz.

Przykład:

```python
lista = [10, "Python", False, [1, 2, 3]]
```

To jest poprawne.

### Ale warto pamiętać

To, że Python na to pozwala, nie znaczy, że zawsze to jest najlepszy pomysł.

W wielu sytuacjach czytelniejszy kod powstaje wtedy, gdy lista zawiera elementy tego samego rodzaju.

---

## Indeksy w liście

Każdy element listy ma swój numer, czyli indeks.

Python numeruje od `0`.

Przykład:

```python
owoce = ["jablko", "banan", "gruszka"]
```

Indeksy:

- `jablko` ma indeks `0`,
- `banan` ma indeks `1`,
- `gruszka` ma indeks `2`.

### Indeksy ujemne

Można też liczyć od końca:

- `-1` to ostatni element,
- `-2` to przedostatni,
- `-3` to trzeci od końca.

---

## Odczytywanie elementów

Do odczytu używa się nawiasów kwadratowych z indeksem.

```python
owoce = ["jablko", "banan", "gruszka"]

print(owoce[0])   # jablko
print(owoce[1])   # banan
print(owoce[-1])  # gruszka
```

### Błąd przy złym indeksie

```python
print(owoce[10])
```

To da:

```python
IndexError
```

Bo taki element nie istnieje.

---

## Zmiana elementów listy

Lista jest mutowalna, więc można zmieniać jej elementy.

Przykład:

```python
owoce = ["jablko", "banan", "gruszka"]
owoce[1] = "pomarancza"

print(owoce)
```

Wynik:

```python
['jablko', 'pomarancza', 'gruszka']
```

### Zmiana ostatniego elementu

```python
owoce[-1] = "kiwi"
```

---

## Dodawanie elementów

### `append()`

Dodaje element na koniec listy.

```python
liczby = [1, 2, 3]
liczby.append(4)
print(liczby)
```

### `insert()`

Wstawia element na konkretną pozycję.

```python
liczby = [1, 2, 3]
liczby.insert(1, 99)
print(liczby)
```

Wynik:

```python
[1, 99, 2, 3]
```

### `extend()`

Dodaje wiele elementów z innej kolekcji.

```python
liczby = [1, 2, 3]
liczby.extend([4, 5, 6])
print(liczby)
```

### Różnica między `append()` a `extend()`

```python
a = [1, 2]
a.append([3, 4])
print(a)
```

Wynik:

```python
[1, 2, [3, 4]]
```

Natomiast:

```python
a = [1, 2]
a.extend([3, 4])
print(a)
```

Wynik:

```python
[1, 2, 3, 4]
```

To bardzo ważna różnica.

---

## Usuwanie elementów

### `remove()`

Usuwa pierwszy element o podanej wartości.

```python
owoce = ["jablko", "banan", "gruszka", "banan"]
owoce.remove("banan")
print(owoce)
```

Usunięty zostanie tylko pierwszy `banan`.

### `pop()`

Usuwa element po indeksie i zwraca go.

```python
liczby = [10, 20, 30]
usuniety = liczby.pop()

print(usuniety)  # 30
print(liczby)    # [10, 20]
```

### `pop(indeks)`

```python
liczby.pop(1)
```

### `del`

Usuwa element albo fragment listy.

```python
liczby = [1, 2, 3, 4]
del liczby[1]
print(liczby)
```

### `clear()`

Usuwa wszystkie elementy.

```python
liczby = [1, 2, 3]
liczby.clear()
print(liczby)
```

---

## Podstawowe operacje na listach

Na listach można wykonywać wiele prostych operacji.

### Konkatenacja

```python
a = [1, 2]
b = [3, 4]
print(a + b)
```

### Powielanie

```python
print([1, 2] * 3)
```

### Porównywanie

```python
print([1, 2] == [1, 2])   # True
print([1, 2] == [2, 1])   # False
```

### Sprawdzanie elementu

```python
print(3 in [1, 2, 3])       # True
print(5 not in [1, 2, 3])   # True
```

---

## Sprawdzanie długości listy

Do tego służy `len()`.

```python
owoce = ["jablko", "banan", "gruszka"]
print(len(owoce))
```

To bardzo często używana funkcja.

---

## Sprawdzanie obecności elementu

Używa się operatora `in`.

```python
owoce = ["jablko", "banan", "gruszka"]

print("banan" in owoce)   # True
print("kiwi" in owoce)    # False
```

To wygodny sposób na sprawdzenie, czy element jest w liście.

---

## Łączenie i powielanie list

### Łączenie przez `+`

```python
a = [1, 2]
b = [3, 4]
c = a + b
print(c)
```

### Powielanie przez `*`

```python
print(["ha"] * 3)
```

### Uwaga na pułapkę

```python
lista = [[0] * 3] * 2
print(lista)
```

Na początku wygląda dobrze, ale to może prowadzić do problemów przy listach zagnieżdżonych.

Przykład:

```python
lista[0][0] = 99
print(lista)
```

Obie wewnętrzne listy mogą się zmienić, bo wskazują na te same obiekty.

---

## Iterowanie po liście

Najczęściej używa się pętli `for`.

```python
owoce = ["jablko", "banan", "gruszka"]

for owoc in owoce:
    print(owoc)
```

### Z `enumerate()`

Jeśli chcesz mieć indeks i wartość:

```python
for indeks, owoc in enumerate(owoce):
    print(indeks, owoc)
```

### Modyfikacja przez indeks

```python
liczby = [1, 2, 3]

for i in range(len(liczby)):
    liczby[i] *= 2

print(liczby)
```

---

## Przydatne metody list

### `count()`

Liczy, ile razy element występuje.

```python
liczby = [1, 2, 2, 3, 2]
print(liczby.count(2))
```

### `index()`

Zwraca indeks pierwszego wystąpienia.

```python
owoce = ["jablko", "banan", "gruszka"]
print(owoce.index("banan"))
```

Jeśli elementu nie ma, pojawi się błąd `ValueError`.

### `reverse()`

Odwraca listę w miejscu.

```python
liczby = [1, 2, 3]
liczby.reverse()
print(liczby)
```

### `copy()`

Tworzy płytką kopię listy.

```python
a = [1, 2, 3]
b = a.copy()
```

---

## Sortowanie list

Sortowanie to jedna z najczęstszych operacji na listach.

### `sort()`

Sortuje listę w miejscu.

```python
liczby = [5, 2, 8, 1]
liczby.sort()
print(liczby)
```

Wynik:

```python
[1, 2, 5, 8]
```

### Sortowanie tekstów

```python
owoce = ["gruszka", "jablko", "banan"]
owoce.sort()
print(owoce)
```

Python sortuje teksty alfabetycznie.

---

## Sortowanie rosnące i malejące

### Rosnąco

To jest domyślne zachowanie:

```python
liczby.sort()
```

### Malejąco

```python
liczby.sort(reverse=True)
```

Przykład:

```python
liczby = [5, 2, 8, 1]
liczby.sort(reverse=True)
print(liczby)
```

Wynik:

```python
[8, 5, 2, 1]
```

---

## Różnica między `sort()` a `sorted()`

To bardzo ważne.

### `sort()`

- działa tylko na listach,
- zmienia oryginalną listę,
- nic nie zwraca poza `None`.

```python
liczby = [3, 1, 2]
liczby.sort()
print(liczby)
```

### `sorted()`

- działa na różnych iterowalnych obiektach,
- nie zmienia oryginału,
- zwraca nową posortowaną listę.

```python
liczby = [3, 1, 2]
nowa = sorted(liczby)

print(liczby)
print(nowa)
```

### Częsty błąd

```python
liczby = [3, 1, 2]
wynik = liczby.sort()
print(wynik)
```

`wynik` będzie `None`.

Dlatego:

- jeśli chcesz zmienić listę, użyj `sort()`,
- jeśli chcesz nową listę, użyj `sorted()`.

---

## Sortowanie z `key`

Możesz określić, według czego Python ma sortować.

### Sortowanie tekstów według długości

```python
slowa = ["kot", "encyklopedia", "pies", "dom"]
slowa.sort(key=len)
print(slowa)
```

### Sortowanie bez uwzględniania wielkości liter

```python
slowa = ["Banan", "ala", "Zebra", "kot"]
slowa.sort(key=str.lower)
print(slowa)
```

### Sortowanie listy słowników

```python
uczniowie = [
    {"imie": "Ania", "wiek": 17},
    {"imie": "Bartek", "wiek": 15},
    {"imie": "Celina", "wiek": 16}
]

uczniowie.sort(key=lambda uczen: uczen["wiek"])
print(uczniowie)
```

To już trochę bardziej zaawansowane, ale bardzo praktyczne.

---

## Slicing list

Slicing to wycinanie fragmentu listy.

Składnia:

```python
lista[start:stop]
```

To oznacza:

- zacznij od indeksu `start`,
- zakończ przed `stop`.

Przykład:

```python
liczby = [10, 20, 30, 40, 50]
print(liczby[1:4])
```

Wynik:

```python
[20, 30, 40]
```

### Ważne

Prawa granica nie jest wliczana.

---

## Slicing z krokiem

Pełna forma:

```python
lista[start:stop:step]
```

### Co drugi element

```python
liczby = [0, 1, 2, 3, 4, 5, 6]
print(liczby[::2])
```

Wynik:

```python
[0, 2, 4, 6]
```

### Co trzeci element

```python
print(liczby[::3])
```

### Fragment od początku

```python
print(liczby[:3])
```

### Fragment do końca

```python
print(liczby[2:])
```

### Cała lista jako kopia

```python
kopia = liczby[:]
```

### Krok ujemny

```python
print(liczby[::-1])
```

To daje listę od końca.

---

## Odwracanie listy

Są na to różne sposoby.

### `reverse()`

Zmienia listę w miejscu.

```python
liczby = [1, 2, 3]
liczby.reverse()
print(liczby)
```

### Slicing `[::-1]`

Tworzy nową odwróconą listę.

```python
liczby = [1, 2, 3]
odwrocone = liczby[::-1]
print(odwrocone)
```

### `reversed()`

Zwraca iterator, który można zamienić na listę.

```python
liczby = [1, 2, 3]
print(list(reversed(liczby)))
```

---

## Kopiowanie list

To bardzo ważny temat.

### Przypisanie to nie kopia

```python
a = [1, 2, 3]
b = a

b.append(4)
print(a)
```

Wynik:

```python
[1, 2, 3, 4]
```

Obie zmienne wskazują na tę samą listę.

### Płytka kopia

```python
a = [1, 2, 3]
b = a.copy()
```

albo:

```python
b = a[:]
```

albo:

```python
b = list(a)
```

### Uwaga przy listach zagnieżdżonych

```python
a = [[1, 2], [3, 4]]
b = a.copy()

b[0].append(99)
print(a)
```

To zmieni też `a`, bo kopiowanie jest płytkie.

### Głęboka kopia

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
```

---

## Listy zagnieżdżone

Lista może zawierać inne listy.

Przykład:

```python
macierz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

### Dostęp do elementu

```python
print(macierz[0])      # [1, 2, 3]
print(macierz[0][1])   # 2
```

### Modyfikacja

```python
macierz[1][2] = 99
```

Listy zagnieżdżone są bardzo przydatne, ale trzeba uważać na kopiowanie i powielanie.

---

## Mutowalność list

Listy są mutowalne, czyli można je zmieniać po utworzeniu.

To oznacza, że możesz:

- zmieniać elementy,
- dodawać elementy,
- usuwać elementy,
- sortować listę,
- odwracać listę.

To bardzo odróżnia listy od na przykład stringów czy tuple.

---

## Typowe błędy początkujących

### 1. Mylenie indeksów

Python zaczyna od `0`, nie od `1`.

### 2. Zły indeks

```python
lista = [1, 2, 3]
print(lista[3])
```

To błąd, bo ostatni poprawny indeks to `2`.

### 3. Mylenie `append()` i `extend()`

To jedna z najczęstszych pułapek.

### 4. Mylenie `sort()` i `sorted()`

`sort()` zmienia listę i zwraca `None`.

### 5. Zakładanie, że `a = b` tworzy kopię

Nie tworzy.

### 6. Błędy przy listach zagnieżdżonych

Zwłaszcza przy kopiowaniu albo mnożeniu list.

### 7. Używanie `remove()` dla elementu, którego nie ma

To da `ValueError`.

### 8. Modyfikowanie listy podczas iteracji bez ostrożności

To może prowadzić do dziwnych efektów.

---

## Praktyczne przykłady

### Dodawanie elementów do listy zakupów

```python
zakupy = ["chleb", "mleko"]
zakupy.append("maslo")
print(zakupy)
```

### Usuwanie elementu

```python
zakupy.remove("mleko")
print(zakupy)
```

### Sortowanie ocen

```python
oceny = [4, 2, 5, 3, 1]
oceny.sort()
print(oceny)
```

### Sortowanie malejące

```python
oceny.sort(reverse=True)
print(oceny)
```

### Wycinanie fragmentu listy

```python
liczby = [10, 20, 30, 40, 50, 60]
print(liczby[1:4])
```

### Co drugi element

```python
print(liczby[::2])
```

### Kopia listy

```python
oryginal = [1, 2, 3]
kopia = oryginal[:]
```

### Praca z listą w pętli

```python
for liczba in [1, 2, 3, 4]:
    print(liczba * 2)
```

---

## Dobre praktyki

### Używaj czytelnych nazw list

```python
uczniowie = ["Ania", "Bartek", "Celina"]
```

zamiast:

```python
x = ["Ania", "Bartek", "Celina"]
```

### Nie modyfikuj listy bez potrzeby w trakcie iteracji

Lepiej czasem utworzyć nową listę albo iterować po kopii.

### Wybieraj właściwe narzędzie

- `append()` dla jednego elementu,
- `extend()` dla wielu elementów,
- `insert()` gdy pozycja ma znaczenie.

### Pamiętaj o różnicy między `sort()` a `sorted()`

To jedna z najczęściej używanych rzeczy w praktyce.

### Uważaj przy kopiowaniu list zagnieżdżonych

Płytka kopia nie zawsze wystarczy.

### Używaj slicing świadomie

To bardzo wygodne narzędzie, ale warto rozumieć dokładnie, jak działa zakres i krok.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- lista to uporządkowana, mutowalna kolekcja,
- elementy listy mają indeksy zaczynające się od `0`,
- można dodawać, usuwać i zmieniać elementy,
- `append()`, `insert()`, `extend()` służą do dodawania,
- `remove()`, `pop()`, `del()`, `clear()` służą do usuwania,
- `sort()` sortuje w miejscu,
- `sorted()` zwraca nową listę,
- slicing pozwala wycinać fragmenty listy,
- `[::-1]` odwraca listę,
- przypisanie to nie kopiowanie,
- listy zagnieżdżone wymagają ostrożności przy kopiowaniu.

Jeśli dobrze opanujesz listy, bardzo duża część codziennego Pythona stanie się dużo prostsza.

---

## Mini ściąga

### Tworzenie listy

```python
lista = [1, 2, 3]
```

### Odczyt

```python
lista[0]
lista[-1]
```

### Dodawanie

```python
lista.append(4)
lista.insert(1, 99)
lista.extend([5, 6])
```

### Usuwanie

```python
lista.remove(2)
lista.pop()
del lista[0]
lista.clear()
```

### Sortowanie

```python
lista.sort()
lista.sort(reverse=True)
nowa = sorted(lista)
```

### Slicing

```python
lista[1:4]
lista[:3]
lista[2:]
lista[::2]
lista[::-1]
```

### Kopiowanie

```python
kopia = lista[:]
kopia = lista.copy()
```

---

## Ćwiczenia

### Ćwiczenie 1

Utwórz listę 5 ulubionych filmów i wypisz:

- pierwszy element,
- ostatni element,
- długość listy.

### Ćwiczenie 2

Dodaj nowy element do listy przez `append()` i wstaw jeden element w środek przez `insert()`.

### Ćwiczenie 3

Usuń element przez:

- `remove()`,
- `pop()`,
- `del`.

### Ćwiczenie 4

Posortuj listę liczb rosnąco i malejąco.

### Ćwiczenie 5

Z listy `[10, 20, 30, 40, 50, 60]` wytnij:

- pierwsze 3 elementy,
- ostatnie 2 elementy,
- co drugi element,
- listę od końca.

### Ćwiczenie 6

Utwórz kopię listy i sprawdź, czy zmiana kopii wpływa na oryginał.

---

## Przykładowe rozwiązania

### Ćwiczenie 1

```python
filmy = ["Film A", "Film B", "Film C", "Film D", "Film E"]

print(filmy[0])
print(filmy[-1])
print(len(filmy))
```

### Ćwiczenie 2

```python
filmy.append("Film F")
filmy.insert(2, "Film X")
print(filmy)
```

### Ćwiczenie 3

```python
filmy.remove("Film B")
filmy.pop()
del filmy[0]
print(filmy)
```

### Ćwiczenie 4

```python
liczby = [5, 1, 4, 2, 3]

liczby.sort()
print(liczby)

liczby.sort(reverse=True)
print(liczby)
```

### Ćwiczenie 5

```python
lista = [10, 20, 30, 40, 50, 60]

print(lista[:3])
print(lista[-2:])
print(lista[::2])
print(lista[::-1])
```

### Ćwiczenie 6

```python
a = [1, 2, 3]
b = a.copy()

b.append(4)

print(a)
print(b)
```

---

## Na koniec

Najlepszy sposób nauki list to praktyka.

Warto:

1. samodzielnie tworzyć listy,
2. testować metody jedna po drugiej,
3. porównywać `append()` i `extend()`,
4. ćwiczyć slicing na różnych zakresach,
5. sprawdzać różnicę między `sort()` i `sorted()`,
6. eksperymentować z kopiowaniem.

Właśnie wtedy listy stają się naprawdę intuicyjne.
