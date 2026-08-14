# defaultdict w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `defaultdict`](#czym-jest-defaultdict)
3. [Skąd importować `defaultdict`](#skąd-importować-defaultdict)
4. [Jaki problem rozwiązuje `defaultdict`](#jaki-problem-rozwiazuje-defaultdict)
5. [Zwykły `dict` kontra `defaultdict`](#zwykly-dict-kontra-defaultdict)
6. [Jak działa wartość domyślna](#jak-dziala-wartosc-domyslna)
7. [Tworzenie `defaultdict`](#tworzenie-defaultdict)
8. [`defaultdict(int)`](#defaultdictint)
9. [`defaultdict(list)`](#defaultdictlist)
10. [`defaultdict(set)`](#defaultdictset)
11. [Własna funkcja domyślna](#wlasna-funkcja-domyslna)
12. [Ważna pułapka: odczyt może utworzyć klucz](#wazna-pulapka-odczyt-moze-utworzyc-klucz)
13. [Grouping danych](#grouping-danych)
14. [Liczenie elementów](#liczenie-elementow)
15. [`defaultdict` a `dict.get()`](#defaultdict-a-dictget)
16. [`defaultdict` a `Counter`](#defaultdict-a-counter)
17. [Kiedy używać `defaultdict`](#kiedy-uzywac-defaultdict)
18. [Kiedy lepiej użyć zwykłego `dict`](#kiedy-lepiej-uzyc-zwyklego-dict)
19. [Typowe błędy początkujących](#typowe-bledy-poczatkujacych)
20. [Praktyczne przykłady](#praktyczne-przyklady)
21. [Dobre praktyki](#dobre-praktyki)
22. [Podsumowanie](#podsumowanie)
23. [Mini ściąga](#mini-sciaga)
24. [Ćwiczenia](#cwiczenia)
25. [Przykładowe rozwiązania](#przykladowe-rozwiazania)

---

## Wprowadzenie

`defaultdict` to bardzo wygodna odmiana słownika z modułu `collections`.

Jego główna zaleta:

**potrafi sam utworzyć wartość początkową dla brakującego klucza.**

To usuwa bardzo częsty wzorzec:

```python
if klucz not in slownik:
    slownik[klucz] = ...
```

albo:

```python
slownik.setdefault(klucz, ...)
```

Jeśli dużo liczysz, grupujesz albo dopisujesz elementy pod klucze, `defaultdict` potrafi mocno uprościć kod.

---

## Czym jest `defaultdict`

To słownik, który dla brakującego klucza może wygenerować wartość domyślną zamiast od razu rzucać `KeyError`.

Najprościej:

- zwykły `dict` mówi: "tego klucza nie ma",
- `defaultdict` mówi: "jeśli trzeba, to utworzę dla niego wartość startową".

---

## Skąd importować `defaultdict`

```python
from collections import defaultdict
```

To standardowa biblioteka Pythona, więc niczego nie trzeba instalować.

---

## Jaki problem rozwiązuje `defaultdict`

Wyobraź sobie, że chcesz policzyć wystąpienia liter.

Bez `defaultdict`:

```python
tekst = "banana"
licznik = {}

for znak in tekst:
    if znak not in licznik:
        licznik[znak] = 0
    licznik[znak] += 1

print(licznik)
```

Wynik:

```python
{'b': 1, 'a': 3, 'n': 2}
```

Z `defaultdict(int)`:

```python
from collections import defaultdict

tekst = "banana"
licznik = defaultdict(int)

for znak in tekst:
    licznik[znak] += 1

print(licznik)
```

Wynik:

```python
defaultdict(<class 'int'>, {'b': 1, 'a': 3, 'n': 2})
```

Logika jest ta sama, ale kod jest krótszy i bardziej naturalny.

---

## Zwykły `dict` kontra `defaultdict`

### Zwykły `dict`

```python
slownik = {}
slownik["a"] += 1
```

Wynik:

```python
KeyError: 'a'
```

### `defaultdict(int)`

```python
from collections import defaultdict

slownik = defaultdict(int)
slownik["a"] += 1
print(slownik)
```

Wynik:

```python
defaultdict(<class 'int'>, {'a': 1})
```

Dlaczego?

Bo `int()` bez argumentów zwraca `0`, więc brakujący klucz dostaje wartość startową `0`.

---

## Jak działa wartość domyślna

`defaultdict` przyjmuje funkcję tworzącą wartość domyślną.

Najczęstsze przykłady:

- `int` daje `0`,
- `list` daje `[]`,
- `set` daje `set()`,
- własna funkcja może zwrócić dowolną wartość.

Ważne:

przekazujesz **funkcję**, a nie wynik jej wywołania.

Poprawnie:

```python
defaultdict(list)
```

Niepoprawnie:

```python
defaultdict(list())
```

Bo `list()` tworzy od razu konkretną listę, zamiast przekazać "przepis na nową listę".

---

## Tworzenie `defaultdict`

```python
from collections import defaultdict

d1 = defaultdict(int)
d2 = defaultdict(list)
d3 = defaultdict(set)
```

Każda wersja będzie inaczej zachowywać się przy brakującym kluczu.

---

## `defaultdict(int)`

Ta wersja jest idealna do liczenia.

```python
from collections import defaultdict

licznik = defaultdict(int)
licznik["kot"] += 1
licznik["kot"] += 1
licznik["pies"] += 1

print(licznik)
```

Wynik:

```python
defaultdict(<class 'int'>, {'kot': 2, 'pies': 1})
```

### Co się tu stało

- pierwszy odczyt `licznik["kot"]` utworzył wartość `0`,
- potem `+= 1` zmieniło ją na `1`,
- drugi raz zrobiło `2`.

---

## `defaultdict(list)`

Ta wersja jest świetna do grupowania danych.

```python
from collections import defaultdict

grupy = defaultdict(list)
grupy["A"].append("Ania")
grupy["A"].append("Adam")
grupy["B"].append("Bartek")

print(grupy)
```

Wynik:

```python
defaultdict(<class 'list'>, {'A': ['Ania', 'Adam'], 'B': ['Bartek']})
```

To bardzo częsty scenariusz:

- klucz oznacza grupę,
- pod kluczem rośnie lista elementów tej grupy.

---

## `defaultdict(set)`

Ta wersja grupuje dane, ale pilnuje unikalności.

```python
from collections import defaultdict

grupy = defaultdict(set)
grupy["A"].add("Ania")
grupy["A"].add("Ania")
grupy["A"].add("Adam")

print(grupy)
```

Wynik:

```python
defaultdict(<class 'set'>, {'A': {'Adam', 'Ania'}})
```

Kolejność w zbiorze nie jest gwarantowana, ale duplikat `"Ania"` nie został zapisany drugi raz.

---

## Własna funkcja domyślna

Możesz przekazać własną funkcję.

```python
from collections import defaultdict

def domyslna():
    return "brak"

d = defaultdict(domyslna)
print(d["x"])
print(d)
```

Wynik:

```python
brak
defaultdict(<function domyslna at ...>, {'x': 'brak'})
```

Ważna obserwacja:

sam odczyt `d["x"]` nie tylko zwrócił `"brak"`, ale też zapisał ten klucz do słownika.

---

## Ważna pułapka: odczyt może utworzyć klucz

To jedna z rzeczy, które początkujący często przeoczają.

```python
from collections import defaultdict

d = defaultdict(list)
print(d)
print(d["nowy"])
print(d)
```

Wynik:

```python
defaultdict(<class 'list'>, {})
[]
defaultdict(<class 'list'>, {'nowy': []})
```

Samo sprawdzenie przez `d["nowy"]` utworzyło nowy wpis.

Jeśli tylko chcesz bezpiecznie odczytać wartość bez tworzenia klucza, użyj na przykład:

```python
print(d.get("nowy"))
```

Wynik:

```python
None
```

I wtedy klucz nie zostanie dodany.

---

## Grouping danych

To jedno z najważniejszych zastosowań `defaultdict(list)`.

```python
from collections import defaultdict

osoby = [
    ("A", "Ania"),
    ("B", "Bartek"),
    ("A", "Adam"),
    ("B", "Beata"),
]

grupy = defaultdict(list)

for grupa, osoba in osoby:
    grupy[grupa].append(osoba)

print(grupy)
```

Wynik:

```python
defaultdict(<class 'list'>, {'A': ['Ania', 'Adam'], 'B': ['Bartek', 'Beata']})
```

To samo dałoby się zrobić zwykłym słownikiem, ale byłoby więcej kodu.

---

## Liczenie elementów

```python
from collections import defaultdict

tekst = "informatyka"
licznik = defaultdict(int)

for znak in tekst:
    licznik[znak] += 1

print(licznik)
```

Przykładowy wynik:

```python
defaultdict(<class 'int'>, {'i': 1, 'n': 1, 'f': 1, 'o': 1, 'r': 1, 'm': 1, 'a': 2, 't': 2, 'y': 1, 'k': 1})
```

---

## `defaultdict` a `dict.get()`

Zwykły słownik też potrafi trochę pomóc:

```python
licznik = {}

for znak in "banana":
    licznik[znak] = licznik.get(znak, 0) + 1

print(licznik)
```

Wynik:

```python
{'b': 1, 'a': 3, 'n': 2}
```

To jest poprawne i bardzo popularne.

`defaultdict(int)` jest po prostu krótszy:

```python
from collections import defaultdict

licznik = defaultdict(int)

for znak in "banana":
    licznik[znak] += 1
```

Obie wersje warto znać.

---

## `defaultdict` a `Counter`

Przy liczeniu znaków albo słów często pojawia się pytanie:

czy użyć `defaultdict(int)`, czy `Counter`?

### `defaultdict(int)`

- świetny, gdy sam budujesz logikę liczenia,
- wygodny przy bardziej niestandardowym przetwarzaniu,
- zachowuje się jak zwykły słownik z domyślnym zerem.

### `Counter`

- lepszy, gdy głównym celem jest samo zliczanie,
- ma dodatkowe metody jak `most_common()`.

Jeśli tylko liczysz wystąpienia, `Counter` bywa jeszcze wygodniejszy.

---

## Kiedy używać `defaultdict`

Najczęściej wtedy, gdy:

- grupujesz rekordy,
- liczysz elementy,
- budujesz słownik list,
- budujesz słownik zbiorów,
- chcesz uniknąć ręcznej inicjalizacji brakujących kluczy.

---

## Kiedy lepiej użyć zwykłego `dict`

Zwykły słownik bywa lepszy, gdy:

- brakujący klucz powinien być błędem,
- nie chcesz przypadkowo tworzyć wpisów przy odczycie,
- struktura jest prosta i nie potrzebujesz wartości domyślnej,
- zależy Ci na maksymalnie oczywistej semantyce dla czytelnika.

---

## Typowe błędy początkujących

### 1. Używanie `defaultdict(list())`

Źle:

```python
defaultdict(list())
```

Poprawnie:

```python
defaultdict(list)
```

### 2. Zaskoczenie, że odczyt tworzy klucz

To cecha `defaultdict`, a nie bug.

### 3. Używanie `defaultdict`, gdy brakujący klucz powinien oznaczać błąd

Czasem zwykły `dict` jest bezpieczniejszy.

### 4. Mylenie `defaultdict(int)` z `Counter`

Są podobne, ale nie identyczne.

---

## Praktyczne przykłady

### Grupowanie produktów po kategorii

```python
from collections import defaultdict

produkty = [
    ("owoce", "jablko"),
    ("owoce", "banan"),
    ("nabial", "mleko"),
    ("nabial", "ser"),
]

grupy = defaultdict(list)

for kategoria, produkt in produkty:
    grupy[kategoria].append(produkt)

print(grupy)
```

Wynik:

```python
defaultdict(<class 'list'>, {'owoce': ['jablko', 'banan'], 'nabial': ['mleko', 'ser']})
```

### Grupowanie unikalnych tagów

```python
from collections import defaultdict

tagi = [
    ("python", "backend"),
    ("python", "backend"),
    ("python", "api"),
    ("sql", "baza"),
]

grupy = defaultdict(set)

for technologia, tag in tagi:
    grupy[technologia].add(tag)

print(grupy)
```

Przykładowy wynik:

```python
defaultdict(<class 'set'>, {'python': {'backend', 'api'}, 'sql': {'baza'}})
```

---

## Dobre praktyki

- Używaj `defaultdict(list)` do grupowania.
- Używaj `defaultdict(int)` do prostego liczenia.
- Używaj `defaultdict(set)`, gdy chcesz unikalnych elementów.
- Pamiętaj, że odczyt przez `[]` może tworzyć klucz.
- Nie używaj `defaultdict` na siłę, jeśli zwykły `dict` jest czytelniejszy.

---

## Podsumowanie

`defaultdict` to słownik z automatyczną wartością startową dla brakujących kluczy.

Najbardziej przydaje się do:

- liczenia,
- grupowania,
- budowania słowników list i zbiorów.

Najważniejsza rzecz do zapamiętania:

**przy odczycie brakującego klucza przez `[]` `defaultdict` może utworzyć nowy wpis.**

---

## Mini ściąga

```python
from collections import defaultdict

licznik = defaultdict(int)
grupy = defaultdict(list)
unikalne = defaultdict(set)

licznik["a"] += 1
grupy["A"].append("Ania")
unikalne["python"].add("api")
```

---

## Ćwiczenia

1. Policz wystąpienia liter w napisie przez `defaultdict(int)`.
2. Pogrupuj imiona po pierwszej literze przez `defaultdict(list)`.
3. Pogrupuj unikalne hobby użytkowników po mieście przez `defaultdict(set)`.
4. Pokaż przykład, w którym sam odczyt klucza dodaje go do słownika.
5. Przepisz kod z ręcznym `if klucz not in slownik` na `defaultdict`.

---

## Przykładowe rozwiązania

```python
from collections import defaultdict

tekst = "banana"
licznik = defaultdict(int)

for znak in tekst:
    licznik[znak] += 1

print(licznik)
```

```python
from collections import defaultdict

imiona = ["Ania", "Adam", "Bartek", "Beata", "Celina"]
grupy = defaultdict(list)

for imie in imiona:
    grupy[imie[0]].append(imie)

print(grupy)
```
