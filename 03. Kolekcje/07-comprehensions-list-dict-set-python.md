# Comprehensions w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym są comprehensions](#czym-są-comprehensions)
3. [Dlaczego warto ich używać](#dlaczego-warto-ich-używać)
4. [List comprehensions](#list-comprehensions)
5. [Podstawowa składnia](#podstawowa-składnia)
6. [List comprehension z warunkiem](#list-comprehension-z-warunkiem)
7. [If else w comprehension](#if-else-w-comprehension)
8. [Comprehensions dla stringów](#comprehensions-dla-stringów)
9. [Dict comprehensions](#dict-comprehensions)
10. [Podstawowa składnia dict comprehension](#podstawowa-składnia-dict-comprehension)
11. [Filtrowanie w dict comprehension](#filtrowanie-w-dict-comprehension)
12. [Set comprehensions](#set-comprehensions)
13. [Różnice między list, dict i set comprehension](#różnice-między-list-dict-i-set-comprehension)
14. [Kiedy comprehension jest lepsze od pętli](#kiedy-comprehension-jest-lepsze-od-pętli)
15. [Kiedy lepiej użyć zwykłej pętli](#kiedy-lepiej-użyć-zwykłej-pętli)
16. [Typowe błędy początkujących](#typowe-błędy-początkujących)
17. [Praktyczne przykłady](#praktyczne-przykłady)
18. [Dobre praktyki](#dobre-praktyki)
19. [Podsumowanie](#podsumowanie)
20. [Mini ściąga](#mini-ściąga)
21. [Ćwiczenia](#ćwiczenia)
22. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Comprehensions to jeden z najbardziej charakterystycznych i wygodnych elementów Pythona.

Pozwalają tworzyć:

- listy,
- słowniki,
- zbiory

w krótkim i czytelnym zapisie.

Zamiast pisać kilka linii pętli `for`, często można zapisać to w jednej linijce.

To jednak nie jest tylko "krótszy zapis".
Dobrze użyte comprehensions potrafią sprawić, że kod jest:

- krótszy,
- bardziej czytelny,
- bardziej pythonowy.

---

## Czym są comprehensions

Comprehension to specjalny zapis służący do budowania nowej kolekcji na podstawie innej kolekcji.

Najczęściej:

- bierzesz elementy z jakiejś listy lub innej sekwencji,
- przekształcasz je,
- ewentualnie filtrujesz,
- tworzysz nową kolekcję.

Przykład:

```python
liczby = [1, 2, 3, 4]
kwadraty = [x ** 2 for x in liczby]
```

Tutaj:

- bierzemy kolejne `x` z listy `liczby`,
- podnosimy je do kwadratu,
- tworzymy nową listę `kwadraty`.

---

## Dlaczego warto ich używać

Comprehensions są przydatne, bo:

- skracają kod,
- eliminują powtarzalną pętlę,
- pozwalają od razu zobaczyć transformację danych,
- bardzo dobrze nadają się do prostych przekształceń.

### Zwykła pętla

```python
kwadraty = []

for x in [1, 2, 3, 4]:
    kwadraty.append(x ** 2)
```

### To samo jako comprehension

```python
kwadraty = [x ** 2 for x in [1, 2, 3, 4]]
```

Drugi zapis jest krótszy i często czytelniejszy.

---

## List comprehensions

To najczęstszy typ comprehension.

Tworzy nową listę.

Przykład:

```python
liczby = [1, 2, 3, 4]
podwojone = [x * 2 for x in liczby]
print(podwojone)
```

Wynik:

```python
[2, 4, 6, 8]
```

---

## Podstawowa składnia

Ogólny schemat:

```python
[wyrazenie for element in kolekcja]
```

Przykład:

```python
napisy = ["a", "bb", "ccc"]
dlugosci = [len(napis) for napis in napisy]
print(dlugosci)
```

### Jak to czytać

"Dla każdego `napis` w `napisy`, zapisz `len(napis)` do nowej listy."

---

## List comprehension z warunkiem

Możesz filtrować elementy przez `if`.

Przykład:

```python
liczby = [1, 2, 3, 4, 5, 6]
parzyste = [x for x in liczby if x % 2 == 0]
print(parzyste)
```

Wynik:

```python
[2, 4, 6]
```

### Schemat

```python
[wyrazenie for element in kolekcja if warunek]
```

### Inny przykład

```python
slowa = ["kot", "encyklopedia", "dom", "pies"]
krotkie = [slowo for slowo in slowa if len(slowo) <= 4]
print(krotkie)
```

---

## If else w comprehension

To ważne rozróżnienie.

`if` na końcu służy do filtrowania.

Ale można też użyć:

```python
wartosc_if_true if warunek else wartosc_if_false
```

wewnątrz wyrażenia.

Przykład:

```python
liczby = [1, 2, 3, 4]
etykiety = ["parzysta" if x % 2 == 0 else "nieparzysta" for x in liczby]
print(etykiety)
```

Wynik:

```python
['nieparzysta', 'parzysta', 'nieparzysta', 'parzysta']
```

### Schemat

```python
[A if warunek else B for element in kolekcja]
```

---

## Comprehensions dla stringów

String też jest iterowalny, więc można po nim przechodzić.

Przykład:

```python
tekst = "python"
litery = [znak.upper() for znak in tekst]
print(litery)
```

Wynik:

```python
['P', 'Y', 'T', 'H', 'O', 'N']
```

### Usuwanie spacji

```python
tekst = "a b c d"
bez_spacji = [znak for znak in tekst if znak != " "]
print(bez_spacji)
```

---

## Dict comprehensions

Służą do tworzenia słowników.

Przykład:

```python
liczby = [1, 2, 3, 4]
kwadraty = {x: x ** 2 for x in liczby}
print(kwadraty)
```

Wynik:

```python
{1: 1, 2: 4, 3: 9, 4: 16}
```

---

## Podstawowa składnia dict comprehension

Schemat:

```python
{klucz: wartosc for element in kolekcja}
```

Przykład:

```python
slowa = ["kot", "pies", "dom"]
mapa = {slowo: len(slowo) for slowo in slowa}
print(mapa)
```

### Inny przykład

```python
liczby = [1, 2, 3]
slownik = {x: x * 10 for x in liczby}
print(slownik)
```

---

## Filtrowanie w dict comprehension

Można dodać warunek:

```python
liczby = [1, 2, 3, 4, 5, 6]
parzyste_kwadraty = {x: x ** 2 for x in liczby if x % 2 == 0}
print(parzyste_kwadraty)
```

Wynik:

```python
{2: 4, 4: 16, 6: 36}
```

### Przykład na gotowym słowniku

```python
oceny = {"Ania": 5, "Bartek": 3, "Celina": 4}
dobrzy = {imie: ocena for imie, ocena in oceny.items() if ocena >= 4}
print(dobrzy)
```

---

## Set comprehensions

Służą do tworzenia zbiorów.

Przykład:

```python
liczby = [1, 2, 2, 3, 3, 4]
kwadraty = {x ** 2 for x in liczby}
print(kwadraty)
```

Wynik:

```python
{1, 4, 9, 16}
```

### Co ważne

Ponieważ `set` usuwa duplikaty, wynik może mieć mniej elementów niż wejście.

### Inny przykład

```python
slowa = ["Kot", "kot", "PIES", "pies"]
male = {slowo.lower() for slowo in slowa}
print(male)
```

---

## Różnice między list, dict i set comprehension

### List comprehension

Tworzy listę:

```python
[x * 2 for x in liczby]
```

### Dict comprehension

Tworzy słownik:

```python
{x: x * 2 for x in liczby}
```

### Set comprehension

Tworzy zbiór:

```python
{x * 2 for x in liczby}
```

### Uwaga

Zapis:

```python
{x for x in liczby}
```

to `set comprehension`, nie `dict comprehension`.

W słowniku musi być para:

```python
klucz: wartosc
```

---

## Kiedy comprehension jest lepsze od pętli

Comprehension jest świetne, gdy:

- transformacja jest prosta,
- filtr jest prosty,
- nowa kolekcja powstaje od razu,
- jedna linia naprawdę poprawia czytelność.

Przykład:

```python
parzyste = [x for x in liczby if x % 2 == 0]
```

To jest bardzo czytelne.

---

## Kiedy lepiej użyć zwykłej pętli

Lepiej użyć zwykłej pętli, gdy:

- logika robi się długa,
- masz kilka warunków i złożone przekształcenia,
- comprehension robi się trudne do czytania,
- chcesz dodać komentarze lub debugować krok po kroku.

Jeśli comprehension wygląda jak zagadka, zwykła pętla będzie lepsza.

---

## Typowe błędy początkujących

### 1. Mylenie filtrującego `if` z `if else`

To dwa różne zastosowania.

### 2. Próba zrobienia zbyt skomplikowanej comprehension w jednej linii

Krótko nie zawsze znaczy czytelnie.

### 3. Mylenie `set comprehension` ze słownikiem

```python
{x for x in liczby}
```

to zbiór, nie słownik.

### 4. Zakładanie, że `set comprehension` zachowa duplikaty

Nie zachowa.

### 5. Nieuważne używanie nazw zmiennych

Na przykład zbyt ogólnego `x` w długim zapisie.

---

## Praktyczne przykłady

### Lista kwadratów

```python
kwadraty = [x ** 2 for x in range(1, 6)]
print(kwadraty)
```

### Lista tylko dodatnich liczb

```python
liczby = [-2, -1, 0, 1, 2, 3]
dodatnie = [x for x in liczby if x > 0]
print(dodatnie)
```

### Słownik długości słów

```python
slowa = ["kot", "pies", "samolot"]
dlugosci = {slowo: len(slowo) for slowo in slowa}
print(dlugosci)
```

### Zbiór unikalnych pierwszych liter

```python
slowa = ["kot", "koza", "pies", "papuga"]
pierwsze_litery = {slowo[0] for slowo in slowa}
print(pierwsze_litery)
```

### Zamiana liczb na etykiety

```python
liczby = [1, 2, 3, 4]
etykiety = ["duza" if x > 2 else "mala" for x in liczby]
print(etykiety)
```

---

## Dobre praktyki

### Używaj comprehension do prostych rzeczy

To najważniejsza zasada.

### Nie walcz o jedną linię za wszelką cenę

Czytelność jest ważniejsza od skrótu.

### Nadawaj sensowne nazwy zmiennym

```python
[slowo.upper() for slowo in slowa]
```

jest czytelniejsze niż:

```python
[x.upper() for x in y]
```

### Pamiętaj, jaki typ kolekcji tworzysz

- `[]` tworzy listę,
- `{k: v ...}` tworzy słownik,
- `{x ...}` tworzy zbiór.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- comprehension to krótki sposób tworzenia nowej kolekcji,
- istnieją `list`, `dict` i `set comprehensions`,
- można w nich filtrować elementy przez `if`,
- można używać `if else` wewnątrz wyrażenia,
- świetnie nadają się do prostych transformacji danych,
- nie warto robić ich zbyt skomplikowanych.

Jeśli dobrze opanujesz comprehensions, Twój kod w Pythonie stanie się krótszy, czytelniejszy i bardziej naturalny.

---

## Mini ściąga

### Lista

```python
[x * 2 for x in liczby]
[x for x in liczby if x > 0]
```

### Lista z `if else`

```python
["parzysta" if x % 2 == 0 else "nieparzysta" for x in liczby]
```

### Słownik

```python
{x: x ** 2 for x in liczby}
{k: v for k, v in dane.items() if v > 0}
```

### Zbiór

```python
{x ** 2 for x in liczby}
```

---

## Ćwiczenia

### Ćwiczenie 1

Utwórz listę kwadratów liczb od 1 do 10 za pomocą list comprehension.

### Ćwiczenie 2

Z listy liczb utwórz nową listę zawierającą tylko liczby parzyste.

### Ćwiczenie 3

Z listy słów utwórz słownik, w którym kluczem będzie słowo, a wartością jego długość.

### Ćwiczenie 4

Z listy słów utwórz zbiór pierwszych liter.

### Ćwiczenie 5

Utwórz listę etykiet `"duza"` i `"mala"` zależnie od tego, czy liczba jest większa od 5.

---

## Przykładowe rozwiązania

### Ćwiczenie 1

```python
kwadraty = [x ** 2 for x in range(1, 11)]
print(kwadraty)
```

### Ćwiczenie 2

```python
liczby = [1, 2, 3, 4, 5, 6]
parzyste = [x for x in liczby if x % 2 == 0]
print(parzyste)
```

### Ćwiczenie 3

```python
slowa = ["kot", "pies", "dom"]
slownik = {slowo: len(slowo) for slowo in slowa}
print(slownik)
```

### Ćwiczenie 4

```python
slowa = ["kot", "koza", "pies"]
litery = {slowo[0] for slowo in slowa}
print(litery)
```

### Ćwiczenie 5

```python
liczby = [2, 4, 6, 8]
etykiety = ["duza" if x > 5 else "mala" for x in liczby]
print(etykiety)
```

---

## Na koniec

Najlepszy sposób nauki comprehension to przepisywanie zwykłych pętli `for` do krótszego zapisu.

Warto:

1. najpierw napisać zwykłą pętlę,
2. potem zamienić ją na comprehension,
3. porównać czytelność,
4. ćwiczyć osobno listy, słowniki i zbiory.

Wtedy szybko staje się jasne, kiedy comprehension naprawdę pomaga, a kiedy tylko skraca kod na siłę.
