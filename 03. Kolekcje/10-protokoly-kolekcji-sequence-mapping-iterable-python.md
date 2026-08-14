# Sequence, Mapping, Iterable w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym są protokoły kolekcji](#czym-sa-protokoly-kolekcji)
3. [Dlaczego ten temat jest ważny](#dlaczego-ten-temat-jest-wazny)
4. [Duck typing i protokoły](#duck-typing-i-protokoly)
5. [Czym jest `Iterable`](#czym-jest-iterable)
6. [Jak Python rozpoznaje obiekt iterowalny](#jak-python-rozpoznaje-obiekt-iterowalny)
7. [Przykłady obiektów iterowalnych](#przyklady-obiektow-iterowalnych)
8. [Iterator a `Iterable`](#iterator-a-iterable)
9. [Czym jest `Sequence`](#czym-jest-sequence)
10. [Najważniejsze cechy sekwencji](#najwazniejsze-cechy-sekwencji)
11. [Przykłady sekwencji](#przyklady-sekwencji)
12. [Czym jest `Mapping`](#czym-jest-mapping)
13. [Najważniejsze cechy mapowania](#najwazniejsze-cechy-mapowania)
14. [Przykłady mapowań](#przyklady-mapowan)
15. [Różnice między `Sequence` i `Mapping`](#roznice-miedzy-sequence-i-mapping)
16. [Moduł `collections.abc`](#modul-collectionsabc)
17. [Sprawdzanie protokołów przez `isinstance`](#sprawdzanie-protokolow-przez-isinstance)
18. [Jakie metody zwykle definiują protokoły](#jakie-metody-zwykle-definiuja-protokoly)
19. [Protokół a klasa bazowa abstrakcyjna](#protokol-a-klasa-bazowa-abstrakcyjna)
20. [Znaczenie protokołów w praktyce](#znaczenie-protokolow-w-praktyce)
21. [Typowe błędy początkujących](#typowe-bledy-poczatkujacych)
22. [Praktyczne przykłady](#praktyczne-przyklady)
23. [Dobre praktyki](#dobre-praktyki)
24. [Podsumowanie](#podsumowanie)
25. [Mini ściąga](#mini-sciaga)
26. [Ćwiczenia](#cwiczenia)
27. [Przykładowe rozwiązania](#przykladowe-rozwiazania)

---

## Wprowadzenie

W Pythonie bardzo wiele obiektów zachowuje się "jak kolekcje".

Na przykład:

- po liście można iterować,
- string ma długość i indeksy,
- słownik przechowuje pary klucz-wartość,
- zbiór wspiera `for`,
- generator daje kolejne elementy.

To wszystko nie dzieje się przypadkiem.
Za takim zachowaniem stoją **protokoły kolekcji**.

Najważniejsze z nich w tym poradniku to:

- `Iterable`,
- `Sequence`,
- `Mapping`.

To nie są tylko trudne słowa z dokumentacji.
To bardzo praktyczne pojęcia, które pomagają zrozumieć:

- jak Python "widzi" kolekcje,
- dlaczego różne typy można używać w podobny sposób,
- jak pisać własne klasy zgodne z zachowaniem Pythona.

---

## Czym są protokoły kolekcji

Najprościej:

**protokół to umowa dotycząca zachowania obiektu.**

To znaczy:

- jeśli obiekt umie coś robić,
- Python i inne fragmenty kodu mogą traktować go w określony sposób.

Przykład:

jeśli obiekt można iterować:

```python
for x in obiekt:
    print(x)
```

to taki obiekt spełnia ideę bycia `Iterable`.

---

## Dlaczego ten temat jest ważny

Bo pozwala lepiej rozumieć:

- `for`,
- `in`,
- `len()`,
- indeksowanie `[]`,
- slicing,
- działanie słowników,
- działanie własnych klas.

Bez tego wiele rzeczy w Pythonie wydaje się "magiczne".

Po zrozumieniu protokołów robi się dużo bardziej logicznie:

- czemu można zrobić `for x in tekst`,
- czemu `dict` nie jest sekwencją,
- czemu generator działa raz,
- czemu własna klasa może zachowywać się jak lista.

---

## Duck typing i protokoły

Python bardzo często działa według zasady:

**jeśli coś zachowuje się jak dany typ, można tego użyć jak tego typu.**

To jest tzw. **duck typing**.

Klasyczna idea:

"jeśli coś chodzi jak kaczka i kwacze jak kaczka, to traktuj to jak kaczkę"

W praktyce:

jeśli obiekt umie być iterowany, to można użyć go w `for`, nawet jeśli nie jest listą.

---

## Czym jest `Iterable`

`Iterable` to obiekt, po którym można iterować.

Na przykład:

```python
for znak in "Python":
    print(znak)
```

Wynik:

```python
P
y
t
h
o
n
```

String nie jest listą, ale jest iterowalny.

To samo dotyczy:

- list,
- tuple,
- zbiorów,
- słowników,
- plików,
- generatorów.

---

## Jak Python rozpoznaje obiekt iterowalny

Najczęściej przez metodę:

```python
__iter__()
```

To ona mówi Pythonowi, jak dostać iterator.

W starszym stylu czasem działa też wsparcie przez:

```python
__getitem__()
```

ale we współczesnym rozumieniu najważniejsze jest `__iter__()`.

Przykład:

```python
class Liczby:
    def __init__(self):
        self.dane = [1, 2, 3]

    def __iter__(self):
        return iter(self.dane)

for x in Liczby():
    print(x)
```

Wynik:

```python
1
2
3
```

---

## Przykłady obiektów iterowalnych

```python
lista = [1, 2, 3]
krotka = (1, 2, 3)
tekst = "abc"
zbior = {1, 2, 3}
slownik = {"a": 1, "b": 2}
```

Po wszystkich można przejść w `for`.

```python
for element in lista:
    print(element)
```

Wynik:

```python
1
2
3
```

Przy słowniku:

```python
for klucz in slownik:
    print(klucz)
```

Wynik:

```python
a
b
```

Ważna uwaga:

iteracja po słowniku domyślnie idzie po kluczach, a nie po parach klucz-wartość.

---

## Iterator a `Iterable`

To bardzo ważne rozróżnienie.

### `Iterable`

To coś, z czego można uzyskać iterator.

### Iterator

To obiekt, który:

- pamięta aktualną pozycję,
- zwraca kolejne elementy,
- zużywa się podczas przechodzenia.

Przykład:

```python
lista = [10, 20, 30]
iterator = iter(lista)

print(iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
```

Wynik będzie wyglądał mniej więcej tak:

```python
<list_iterator object ...>
10
20
30
```

Lista jest `Iterable`, a wynik `iter(lista)` to iterator.

### Co dzieje się po zużyciu iteratora

```python
lista = [1, 2]
it = iter(lista)

print(next(it))
print(next(it))
# print(next(it))
```

Trzecie `next(it)` da:

```python
StopIteration
```

### Ważna różnica praktyczna

```python
lista = [1, 2, 3]

for x in lista:
    print(x)

for x in lista:
    print(x)
```

Obie pętle działają, bo z listy można za każdym razem dostać nowy iterator.

Ale:

```python
it = iter([1, 2, 3])

for x in it:
    print(x)

for x in it:
    print(x)
```

Wynik:

```python
1
2
3
```

Druga pętla nic już nie wypisze, bo iterator został zużyty.

---

## Czym jest `Sequence`

`Sequence` to uporządkowana kolekcja elementów dostępnych po pozycji.

Najprościej:

to coś, co zachowuje się jak sekwencja:

- ma długość,
- ma indeksy,
- zachowuje kolejność,
- zwykle wspiera slicing.

---

## Najważniejsze cechy sekwencji

Sekwencja zwykle wspiera:

- `len(obj)`,
- `obj[index]`,
- iterację,
- `in`,
- indeksy dodatnie i ujemne,
- slicing.

Przykład:

```python
tekst = "Python"
print(len(tekst))
print(tekst[0])
print(tekst[-1])
print(tekst[1:4])
```

Wynik:

```python
6
P
n
yth
```

---

## Przykłady sekwencji

Najczęściej:

- `list`,
- `tuple`,
- `str`,
- `range`.

Przykład:

```python
liczby = [10, 20, 30, 40]
print(liczby[0])
print(liczby[1:3])
print(30 in liczby)
```

Wynik:

```python
10
[20, 30]
True
```

String też jest sekwencją:

```python
tekst = "abc"
print(tekst[1])
```

Wynik:

```python
b
```

---

## Czym jest `Mapping`

`Mapping` to kolekcja typu:

**klucz -> wartość**

Najważniejszy przykład:

- `dict`.

To inna idea niż sekwencja.
Tutaj nie chodzi o pozycję, tylko o klucz.

---

## Najważniejsze cechy mapowania

Mapowanie zwykle wspiera:

- dostęp po kluczu,
- sprawdzanie klucza przez `in`,
- iterację po kluczach,
- `keys()`, `values()`, `items()`.

Przykład:

```python
slownik = {"imie": "Ania", "wiek": 17}
print(slownik["imie"])
print("wiek" in slownik)
print(list(slownik.keys()))
```

Wynik:

```python
Ania
True
['imie', 'wiek']
```

---

## Przykłady mapowań

Najczęściej:

- `dict`,
- `defaultdict`,
- `ChainMap`,
- słownikopodobne klasy użytkownika.

W praktyce najważniejszym klasycznym przykładem jest zwykły słownik.

---

## Różnice między `Sequence` i `Mapping`

### `Sequence`

- działa po indeksie,
- ma pozycję elementu,
- zachowuje kolejność,
- przykład: `list`, `tuple`, `str`.

### `Mapping`

- działa po kluczu,
- nie interesuje go pozycja w sensie indeksu,
- przykład: `dict`.

To dwa różne modele pracy z danymi.

Porównanie:

```python
lista = ["Ania", "Bartek"]
slownik = {"pierwszy": "Ania", "drugi": "Bartek"}

print(lista[0])
print(slownik["pierwszy"])
```

Wynik:

```python
Ania
Ania
```

Wynik ten sam, ale sposób dostępu zupełnie inny.

---

## Moduł `collections.abc`

W module `collections.abc` znajdziesz abstrakcyjne klasy bazowe opisujące zachowanie kolekcji.

Najczęściej używane:

```python
from collections.abc import Iterable, Sequence, Mapping
```

Pozwalają:

- sprawdzać typ zachowania przez `isinstance`,
- budować własne klasy zgodne z tymi interfejsami,
- czytelniej opisywać intencję kodu.

---

## Sprawdzanie protokołów przez `isinstance`

```python
from collections.abc import Iterable, Sequence, Mapping

print(isinstance([1, 2, 3], Iterable))
print(isinstance([1, 2, 3], Sequence))
print(isinstance({"a": 1}, Mapping))
print(isinstance({1, 2, 3}, Sequence))
```

Wynik:

```python
True
True
True
False
```

Set jest iterowalny, ale nie jest sekwencją.

```python
print(isinstance({1, 2, 3}, Iterable))
```

Wynik:

```python
True
```

---

## Jakie metody zwykle definiują protokoły

To nie jest pełna formalna definicja wszystkiego, ale bardzo dobry model praktyczny.

### `Iterable`

Najważniejsze:

- `__iter__()`.

### `Sequence`

Najczęściej:

- `__len__()`,
- `__getitem__()`.

### `Mapping`

Najczęściej:

- `__getitem__()`,
- `__iter__()`,
- `__len__()`.

To właśnie dlatego:

- sekwencja daje indeksowanie,
- mapowanie daje dostęp po kluczu.

---

## Protokół a klasa bazowa abstrakcyjna

W praktyce często miesza się te dwa pojęcia.

Najprościej:

- **protokół** to oczekiwane zachowanie,
- **ABC** z `collections.abc` to formalny sposób opisania takiego zachowania.

Czyli:

- możesz "zachowywać się jak sekwencja", nawet bez dziedziczenia po `Sequence`,
- ale dziedziczenie po `Sequence` daje bardziej jawny i uporządkowany model.

---

## Znaczenie protokołów w praktyce

To nie jest tylko teoria.

Protokoły wpływają na to, jak projektujesz funkcje.

Przykład:

zamiast myśleć:

"ta funkcja działa tylko dla list"

często lepiej myśleć:

"ta funkcja działa dla dowolnego obiektu iterowalnego"

Przykład:

```python
def wypisz_wszystko(dane):
    for element in dane:
        print(element)

wypisz_wszystko([1, 2, 3])
wypisz_wszystko(("a", "b"))
wypisz_wszystko("OK")
```

Wynik:

```python
1
2
3
a
b
O
K
```

To jest bardzo pythonowy sposób myślenia.

---

## Typowe błędy początkujących

### 1. Mylenie iteratora z iterowalnym obiektem

Lista i iterator z listy to nie to samo.

### 2. Zakładanie, że wszystko iterowalne jest sekwencją

Na przykład `set` jest iterowalny, ale nie ma indeksów.

### 3. Zakładanie, że słownik działa jak lista

`dict` to mapowanie, nie sekwencja.

### 4. Niezrozumienie, czemu generator działa tylko raz

Bo generator jest iteratorem i zużywa się podczas przechodzenia.

### 5. Nadużywanie sprawdzania konkretnych typów

Często lepiej polegać na zachowaniu niż pytać, czy coś jest dokładnie listą.

---

## Praktyczne przykłady

### Funkcja działająca na dowolnym `Iterable`

```python
def policz_elementy(dane):
    licznik = 0
    for _ in dane:
        licznik += 1
    return licznik

print(policz_elementy([1, 2, 3]))
print(policz_elementy("abc"))
```

Wynik:

```python
3
3
```

### Sprawdzanie, czy obiekt jest sekwencją

```python
from collections.abc import Sequence

print(isinstance("Python", Sequence))
print(isinstance((1, 2), Sequence))
print(isinstance({1, 2}, Sequence))
```

Wynik:

```python
True
True
False
```

### Sprawdzanie mapowania

```python
from collections.abc import Mapping

print(isinstance({"a": 1}, Mapping))
```

Wynik:

```python
True
```

---

## Dobre praktyki

- Myśl kategoriami zachowania, nie tylko konkretnych typów.
- Odróżniaj `Iterable` od iteratora.
- Pamiętaj, że `dict` to `Mapping`, a nie sekwencja.
- Nie zakładaj indeksowania tam, gdzie masz tylko iterowalność.
- Jeśli tworzysz własne kolekcje, trzymaj się pythonowych protokołów.

---

## Podsumowanie

Najważniejsze pojęcia:

- `Iterable` oznacza: można po tym przejść w `for`,
- `Sequence` oznacza: uporządkowana kolekcja z indeksami,
- `Mapping` oznacza: kolekcja klucz -> wartość.

Jeśli to rozumiesz, dużo łatwiej pojąć:

- działanie wbudowanych typów,
- zachowanie generatorów,
- projektowanie własnych klas kolekcji.

---

## Mini ściąga

```python
from collections.abc import Iterable, Sequence, Mapping

isinstance([1, 2], Iterable)   # True
isinstance([1, 2], Sequence)   # True
isinstance("abc", Sequence)    # True
isinstance({"a": 1}, Mapping)  # True
isinstance({1, 2}, Sequence)   # False
```

---

## Ćwiczenia

1. Sprawdź przez `isinstance`, które z obiektów są `Iterable`, `Sequence` i `Mapping`.
2. Pokaż różnicę między listą a iteratorem z listy.
3. Napisz funkcję działającą dla dowolnego obiektu iterowalnego.
4. Pokaż przykład obiektu iterowalnego, który nie jest sekwencją.
5. Pokaż przykład mapowania i porównaj go z sekwencją.

---

## Przykładowe rozwiązania

```python
from collections.abc import Iterable, Sequence, Mapping

print(isinstance([1, 2, 3], Iterable))
print(isinstance([1, 2, 3], Sequence))
print(isinstance({"a": 1}, Mapping))
print(isinstance({1, 2, 3}, Sequence))
```

```python
lista = [1, 2, 3]
it = iter(lista)

print(next(it))
print(next(it))
print(list(it))
```
