# Tworzenie Własnych Kolekcji Zgodnych z Protokołem w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Co to znaczy, że kolekcja jest zgodna z protokołem](#co-to-znaczy-ze-kolekcja-jest-zgodna-z-protokolem)
3. [Dlaczego warto tworzyć własne kolekcje](#dlaczego-warto-tworzyc-wlasne-kolekcje)
4. [Najprostsza idea własnej kolekcji](#najprostsza-idea-wlasnej-kolekcji)
5. [Własny obiekt iterowalny](#wlasny-obiekt-iterowalny)
6. [`__iter__()`](#__iter__)
7. [Własna sekwencja](#wlasna-sekwencja)
8. [`__len__()` i `__getitem__()`](#__len__-i-__getitem__)
9. [Własne mapowanie](#wlasne-mapowanie)
10. [`__getitem__()`, `__iter__()`, `__len__()` dla `Mapping`](#__getitem____iter____len__-dla-mapping)
11. [Dziedziczenie po `collections.abc`](#dziedziczenie-po-collectionsabc)
12. [Własna klasa zgodna z `Sequence`](#wlasna-klasa-zgodna-z-sequence)
13. [Własna klasa zgodna z `Mapping`](#wlasna-klasa-zgodna-z-mapping)
14. [Dlaczego to działa z `for`, `len()` i `in`](#dlaczego-to-dziala-z-for-len-i-in)
15. [Dodatkowe metody specjalne](#dodatkowe-metody-specjalne)
16. [`__contains__()`, `__repr__()` i inne wygody](#__contains____repr__-i-inne-wygody)
17. [Kiedy pisać własną kolekcję](#kiedy-pisac-wlasna-kolekcje)
18. [Kiedy lepiej użyć zwykłej listy lub słownika](#kiedy-lepiej-uzyc-zwyklej-listy-lub-slownika)
19. [Typowe błędy początkujących](#typowe-bledy-poczatkujacych)
20. [Praktyczne przykłady](#praktyczne-przyklady)
21. [Dobre praktyki](#dobre-praktyki)
22. [Podsumowanie](#podsumowanie)
23. [Mini ściąga](#mini-sciaga)
24. [Ćwiczenia](#cwiczenia)
25. [Przykładowe rozwiązania](#przykladowe-rozwiazania)

---

## Wprowadzenie

Jedną z najlepszych cech Pythona jest to, że możesz pisać własne klasy, które zachowują się jak wbudowane kolekcje.

Możesz stworzyć obiekt, który:

- działa w pętli `for`,
- ma długość przez `len()`,
- pozwala na indeksowanie `[]`,
- wspiera `in`,
- zachowuje się jak sekwencja albo mapowanie.

To właśnie oznacza zgodność z protokołem.

I to jest bardzo praktyczne, bo zamiast zmuszać użytkownika klasy do pamiętania Twojego nietypowego API, możesz sprawić, że obiekt zachowuje się "po pythonowemu".

---

## Co to znaczy, że kolekcja jest zgodna z protokołem

To znaczy, że implementuje odpowiednie metody specjalne, których Python oczekuje.

Przykład:

jeśli klasa ma:

```python
__iter__()
```

to Python może po niej iterować.

Jeśli ma:

```python
__len__()
```

to działa `len(obiekt)`.

Jeśli ma:

```python
__getitem__()
```

to można zrobić:

```python
obiekt[0]
```

To właśnie jest sedno: Python nie potrzebuje "magii frameworka", tylko kilku dobrze znanych metod specjalnych.

---

## Dlaczego warto tworzyć własne kolekcje

Bo czasem chcesz mieć obiekt bardziej dopasowany do problemu.

Na przykład:

- kolekcję tylko dodatnich liczb,
- kolekcję opakowującą listę, ale z dodatkowymi zasadami,
- specjalny widok na dane,
- obiekt, który przechowuje dane w niestandardowy sposób, ale zachowuje się jak lista albo słownik.

Przykład praktyczny:

zamiast pracować na "gołej" liście ocen, możesz stworzyć klasę `Oceny`, która:

- pilnuje poprawnych wartości,
- nadal działa z `for`,
- nadal działa z `len()`,
- nadal pozwala pobrać element przez indeks.

---

## Najprostsza idea własnej kolekcji

Najczęściej własna kolekcja po prostu przechowuje dane wewnętrznie, na przykład w:

- liście,
- słowniku,
- tuple.

A Twoja klasa udostępnia odpowiednie metody specjalne.

Czyli:

- w środku zwykła struktura,
- na zewnątrz własny, sensowny interfejs.

---

## Własny obiekt iterowalny

Najprostsza wersja:

```python
class MojaKolekcja:
    def __init__(self, dane):
        self._dane = dane

    def __iter__(self):
        return iter(self._dane)
```

Teraz:

```python
obiekt = MojaKolekcja([1, 2, 3])

for x in obiekt:
    print(x)
```

Wynik:

```python
1
2
3
```

To najprostszy sposób, by Twoja klasa weszła w świat `for`.

---

## `__iter__()`

To jedna z najważniejszych metod specjalnych.

Powinna zwracać iterator.

Najprostszy wzorzec:

```python
def __iter__(self):
    return iter(self._dane)
```

Jeśli wewnątrz masz listę lub inną iterowalną strukturę, to bardzo wygodne rozwiązanie.

Możesz też zrobić własną logikę:

```python
class TylkoDodatnie:
    def __init__(self, dane):
        self._dane = dane

    def __iter__(self):
        for x in self._dane:
            if x > 0:
                yield x

obiekt = TylkoDodatnie([-2, 0, 3, 5])

for x in obiekt:
    print(x)
```

Wynik:

```python
3
5
```

---

## Własna sekwencja

Żeby obiekt zachowywał się jak sekwencja, zwykle potrzebujesz:

- `__len__()`,
- `__getitem__()`.

Przykład:

```python
class MojaSekwencja:
    def __init__(self, dane):
        self._dane = list(dane)

    def __len__(self):
        return len(self._dane)

    def __getitem__(self, index):
        return self._dane[index]
```

Teraz działają:

- `len(obiekt)`,
- `obiekt[0]`,
- iteracja.

```python
obiekt = MojaSekwencja([10, 20, 30, 40])

print(len(obiekt))
print(obiekt[0])
print(obiekt[1:3])
```

Wynik:

```python
4
10
[20, 30]
```

---

## `__len__()` i `__getitem__()`

### `__len__()`

Obsługuje:

```python
len(obiekt)
```

### `__getitem__()`

Obsługuje:

```python
obiekt[index]
```

oraz często także slicing:

```python
obiekt[1:4]
```

jeśli wewnętrzna struktura to wspiera.

Przykład:

```python
class Liczby:
    def __init__(self, dane):
        self._dane = list(dane)

    def __len__(self):
        return len(self._dane)

    def __getitem__(self, index):
        return self._dane[index]

liczby = Liczby([1, 2, 3, 4, 5])
print(liczby[2])
print(liczby[1:4])
```

Wynik:

```python
3
[2, 3, 4]
```

---

## Własne mapowanie

Jeśli chcesz strukturę podobną do słownika, najczęściej potrzebujesz:

- `__getitem__()`,
- `__iter__()`,
- `__len__()`.

Przykład:

```python
class MojeMapowanie:
    def __init__(self, dane):
        self._dane = dict(dane)

    def __getitem__(self, key):
        return self._dane[key]

    def __iter__(self):
        return iter(self._dane)

    def __len__(self):
        return len(self._dane)
```

```python
obiekt = MojeMapowanie({"imie": "Ania", "wiek": 19})

print(len(obiekt))
print(obiekt["imie"])

for klucz in obiekt:
    print(klucz)
```

Wynik:

```python
2
Ania
imie
wiek
```

---

## `__getitem__()`, `__iter__()`, `__len__()` dla `Mapping`

To właśnie te trzy metody są podstawą `Mapping`.

Python dzięki nim może:

- pobierać wartość po kluczu,
- iterować po kluczach,
- zwracać długość.

Ważna różnica względem sekwencji:

`__getitem__()` tutaj nie oznacza "daj element o indeksie 0", tylko "daj wartość dla podanego klucza".

---

## Dziedziczenie po `collections.abc`

To bardzo wygodny sposób na tworzenie zgodnych klas.

Możesz dziedziczyć po:

- `Sequence`,
- `Mapping`.

z modułu `collections.abc`.

Przykład:

```python
from collections.abc import Sequence
```

To daje bardziej formalny i czytelny model tworzenia kolekcji.

---

## Własna klasa zgodna z `Sequence`

Przykład:

```python
from collections.abc import Sequence

class MojaSekwencja(Sequence):
    def __init__(self, dane):
        self._dane = list(dane)

    def __getitem__(self, index):
        return self._dane[index]

    def __len__(self):
        return len(self._dane)
```

```python
liczby = MojaSekwencja([10, 20, 30])

print(len(liczby))
print(liczby[0])
print(20 in liczby)

for x in liczby:
    print(x)
```

Wynik:

```python
3
10
True
10
20
30
```

Taka klasa:

- formalnie jest `Sequence`,
- działa z `len`,
- działa z indeksami,
- działa w `for`,
- wspiera `in`.

---

## Własna klasa zgodna z `Mapping`

Przykład:

```python
from collections.abc import Mapping

class MojeMapowanie(Mapping):
    def __init__(self, dane):
        self._dane = dict(dane)

    def __getitem__(self, key):
        return self._dane[key]

    def __iter__(self):
        return iter(self._dane)

    def __len__(self):
        return len(self._dane)
```

```python
dane = MojeMapowanie({"a": 1, "b": 2})

print(len(dane))
print(dane["a"])
print("b" in dane)
print(list(dane))
```

Wynik:

```python
2
1
True
['a', 'b']
```

---

## Dlaczego to działa z `for`, `len()` i `in`

Bo Python używa metod specjalnych.

### `for`

Korzysta z iteracji.

### `len()`

Korzysta z `__len__()`.

### `[]`

Korzysta z `__getitem__()`.

### `in`

Może korzystać z iteracji albo specjalnych metod, jeśli są dostępne.

Przykład:

```python
class Liczby:
    def __init__(self, dane):
        self._dane = list(dane)

    def __len__(self):
        return len(self._dane)

    def __getitem__(self, index):
        return self._dane[index]

liczby = Liczby([3, 6, 9])

print(len(liczby))
print(liczby[1])
print(6 in liczby)
```

Wynik:

```python
3
6
True
```

---

## Dodatkowe metody specjalne

Podstawy często wystarczą, ale możesz dodać też wygody:

- `__contains__()` dla `in`,
- `__repr__()` dla ładnego wypisywania,
- `__setitem__()` dla ustawiania przez `[]`,
- `__delitem__()` dla usuwania,
- `__reversed__()` dla `reversed(...)`.

Nie wszystko naraz.
Najpierw zrób mały, sensowny interfejs.

---

## `__contains__()`, `__repr__()` i inne wygody

### `__contains__()`

Pozwala jawnie zdefiniować zachowanie `in`.

```python
class Liczby:
    def __init__(self, dane):
        self._dane = list(dane)

    def __contains__(self, element):
        return element in self._dane

liczby = Liczby([2, 4, 6])
print(4 in liczby)
print(5 in liczby)
```

Wynik:

```python
True
False
```

### `__repr__()`

Poprawia czytelność przy `print(...)` i debugowaniu.

```python
class Liczby:
    def __init__(self, dane):
        self._dane = list(dane)

    def __repr__(self):
        return f"Liczby({self._dane})"

liczby = Liczby([1, 2, 3])
print(liczby)
```

Wynik:

```python
Liczby([1, 2, 3])
```

---

## Kiedy pisać własną kolekcję

Warto, gdy:

- zwykła lista lub słownik nie oddają dobrze modelu domenowego,
- chcesz pilnować reguł danych,
- chcesz ukryć szczegóły implementacji,
- chcesz mieć wygodny, pythonowy interfejs.

Przykłady:

- `Oceny`,
- `HistoriaZdarzen`,
- `TylkoDodatnie`,
- `Konfiguracja`,
- `RejestrUzytkownikow`.

---

## Kiedy lepiej użyć zwykłej listy lub słownika

Nie twórz własnej kolekcji tylko dlatego, że "można".

Lepiej zostać przy `list` albo `dict`, gdy:

- potrzebujesz tylko prostego przechowywania danych,
- nie masz dodatkowych zasad domenowych,
- własna klasa niczego realnie nie upraszcza,
- kod z klasą byłby cięższy niż problem.

To ważna zasada: nie komplikuj na siłę.

---

## Typowe błędy początkujących

### 1. Pisanie zbyt skomplikowanej klasy na prosty przypadek

Czasem lista naprawdę wystarczy.

### 2. Implementowanie "połowy protokołu"

Na przykład chcesz sekwencję, ale zapominasz o `__len__()` albo `__getitem__()`.

### 3. Zła semantyka `__getitem__()`

Dla sekwencji powinno chodzić o indeks.
Dla mapowania o klucz.

### 4. Zwracanie czegoś nieiterowalnego z `__iter__()`

`__iter__()` musi zwrócić iterator.

### 5. Brak czytelnego `__repr__()`

To nie jest obowiązkowe, ale mocno pomaga przy nauce i debugowaniu.

---

## Praktyczne przykłady

### Kolekcja ocen

```python
from collections.abc import Sequence

class Oceny(Sequence):
    def __init__(self, dane):
        self._dane = list(dane)

    def __getitem__(self, index):
        return self._dane[index]

    def __len__(self):
        return len(self._dane)

    def srednia(self):
        return sum(self._dane) / len(self._dane)

oceny = Oceny([4, 5, 3, 5])

print(len(oceny))
print(oceny[0])
print(list(oceny))
print(oceny.srednia())
```

Wynik:

```python
4
4
[4, 5, 3, 5]
4.25
```

### Tylko dodatnie liczby

```python
class TylkoDodatnie:
    def __init__(self, dane):
        self._dane = [x for x in dane if x > 0]

    def __iter__(self):
        return iter(self._dane)

    def __repr__(self):
        return f"TylkoDodatnie({self._dane})"

liczby = TylkoDodatnie([-3, 0, 2, 7])
print(liczby)

for x in liczby:
    print(x)
```

Wynik:

```python
TylkoDodatnie([2, 7])
2
7
```

---

## Dobre praktyki

- Zaczynaj od najprostszego możliwego interfejsu.
- Opieraj własną kolekcję na wbudowanej strukturze wewnętrznej.
- Używaj `collections.abc`, gdy chcesz jasno zadeklarować typ zachowania.
- Dbaj o sensowny `__repr__()`.
- Pisz własną kolekcję tylko wtedy, gdy naprawdę wnosi wartość.

---

## Podsumowanie

Własna kolekcja zgodna z protokołem to po prostu klasa, która implementuje metody specjalne oczekiwane przez Pythona.

Najważniejsze rzeczy do zapamiętania:

- `__iter__()` daje iterację,
- `__len__()` daje `len()`,
- `__getitem__()` daje `[]`,
- `Sequence` i `Mapping` z `collections.abc` pomagają budować czytelne klasy.

Jeśli to rozumiesz, umiesz pisać obiekty, które zachowują się naturalnie i pythonowo.

---

## Mini ściąga

```python
from collections.abc import Sequence

class MojaSekwencja(Sequence):
    def __init__(self, dane):
        self._dane = list(dane)

    def __getitem__(self, index):
        return self._dane[index]

    def __len__(self):
        return len(self._dane)
```

---

## Ćwiczenia

1. Napisz klasę iterowalną, która przechowuje liczby.
2. Dodaj do niej `__len__()`.
3. Dodaj `__getitem__()`, żeby działało indeksowanie.
4. Napisz klasę zgodną z `Sequence`.
5. Napisz klasę zgodną z `Mapping`.
6. Dodaj `__repr__()` i `__contains__()` do własnej klasy.

---

## Przykładowe rozwiązania

```python
class MojaKolekcja:
    def __init__(self, dane):
        self._dane = list(dane)

    def __iter__(self):
        return iter(self._dane)

obiekt = MojaKolekcja([1, 2, 3])
print(list(obiekt))
```

```python
from collections.abc import Sequence

class Liczby(Sequence):
    def __init__(self, dane):
        self._dane = list(dane)

    def __getitem__(self, index):
        return self._dane[index]

    def __len__(self):
        return len(self._dane)

liczby = Liczby([10, 20, 30])
print(len(liczby))
print(liczby[1])
```
