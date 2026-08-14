# Dict w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `dict`](#czym-jest-dict)
3. [Dlaczego słowniki są tak ważne](#dlaczego-słowniki-są-tak-ważne)
4. [Klucz i wartość](#klucz-i-wartość)
5. [Jak utworzyć słownik](#jak-utworzyć-słownik)
6. [Pusty słownik](#pusty-słownik)
7. [Typy danych w słowniku](#typy-danych-w-słowniku)
8. [Jak działają klucze](#jak-działają-klucze)
9. [Jakie typy mogą być kluczami](#jakie-typy-mogą-być-kluczami)
10. [Odczyt wartości](#odczyt-wartości)
11. [Dodawanie i zmiana elementów](#dodawanie-i-zmiana-elementów)
12. [Usuwanie elementów](#usuwanie-elementów)
13. [Sprawdzanie obecności klucza](#sprawdzanie-obecności-klucza)
14. [Najważniejsze metody słownika](#najważniejsze-metody-słownika)
15. [Iteracja po słowniku](#iteracja-po-słowniku)
16. [Iteracja po kluczach](#iteracja-po-kluczach)
17. [Iteracja po wartościach](#iteracja-po-wartościach)
18. [Iteracja po parach klucz-wartość](#iteracja-po-parach-klucz-wartość)
19. [Słowniki zagnieżdżone](#słowniki-zagnieżdżone)
20. [Kopiowanie słowników](#kopiowanie-słowników)
21. [Łączenie słowników](#łączenie-słowników)
22. [Sortowanie przy pracy ze słownikiem](#sortowanie-przy-pracy-ze-słownikiem)
23. [Złożoność operacji na słowniku](#złożoność-operacji-na-słowniku)
24. [Dlaczego słownik jest szybki](#dlaczego-słownik-jest-szybki)
25. [Kiedy słownik jest lepszy od listy](#kiedy-słownik-jest-lepszy-od-listy)
26. [Typowe błędy początkujących](#typowe-błędy-początkujących)
27. [Praktyczne przykłady](#praktyczne-przykłady)
28. [Dobre praktyki](#dobre-praktyki)
29. [Podsumowanie](#podsumowanie)
30. [Mini ściąga](#mini-ściąga)
31. [Ćwiczenia](#ćwiczenia)
32. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`dict`, czyli słownik, to jeden z najważniejszych typów danych w Pythonie.

Jest używany praktycznie wszędzie:

- do przechowywania danych użytkownika,
- konfiguracji programu,
- wyników obliczeń,
- mapowania jednych wartości na inne,
- liczenia wystąpień,
- reprezentowania obiektów i rekordów danych.

Jeśli lista przechowuje elementy po kolei, to słownik przechowuje dane w postaci:

**klucz -> wartość**

To sprawia, że można bardzo szybko znaleźć potrzebną informację po nazwie klucza.

W tym poradniku omówimy:

- czym jest słownik,
- jak działa para klucz-wartość,
- jak iterować po słowniku,
- jakie są najważniejsze operacje,
- jaka jest ich złożoność i co to praktycznie znaczy.

---

## Czym jest `dict`

Słownik to kolekcja par:

**klucz : wartość**

Przykład:

```python
osoba = {
    "imie": "Ania",
    "wiek": 17,
    "miasto": "Krakow"
}
```

Tutaj:

- `"imie"` to klucz,
- `"Ania"` to wartość,
- `"wiek"` to klucz,
- `17` to wartość.

### Najprościej

Słownik działa trochę jak prawdziwy słownik:

- szukasz hasła,
- dostajesz odpowiadającą mu wartość.

---

## Dlaczego słowniki są tak ważne

Słownik jest bardzo wygodny, gdy dane mają nazwy.

Na przykład:

```python
osoba = {
    "imie": "Adam",
    "wiek": 30,
    "zawod": "Tester"
}
```

Gdybyś trzymał to w liście:

```python
osoba = ["Adam", 30, "Tester"]
```

to musiałbyś pamiętać:

- indeks `0` to imię,
- indeks `1` to wiek,
- indeks `2` to zawód.

Słownik jest dużo czytelniejszy.

---

## Klucz i wartość

To podstawa działania słownika.

### Klucz

To nazwa, po której szukasz danych.

### Wartość

To dane przypisane do klucza.

Przykład:

```python
produkt = {
    "nazwa": "Laptop",
    "cena": 3500,
    "dostepny": True
}
```

Tutaj:

- `"nazwa"` to klucz,
- `"Laptop"` to wartość.

### Ważna zasada

Klucze w słowniku muszą być unikalne.

Nie możesz mieć dwóch takich samych kluczy z różnymi wartościami w tym samym słowniku.

---

## Jak utworzyć słownik

Najczęściej tworzy się go za pomocą nawiasów klamrowych:

```python
osoba = {
    "imie": "Ania",
    "wiek": 17
}
```

### Krótszy przykład

```python
dane = {"a": 1, "b": 2}
```

### Można też użyć `dict()`

```python
osoba = dict(imie="Ania", wiek=17)
```

To działa, ale przy bardziej złożonych danych częściej używa się zwykłej formy z `{}`.

---

## Pusty słownik

Pusty słownik tworzy się tak:

```python
pusty = {}
```

albo:

```python
pusty = dict()
```

### Uwaga

To odróżnia słownik od zbioru:

- `{}` to pusty `dict`,
- `set()` to pusty `set`.

---

## Typy danych w słowniku

### Klucze

Muszą być hashowalne, czyli zwykle niemutowalne.

Najczęściej używa się:

- `str`,
- `int`,
- `float`,
- `tuple`.

### Wartości

Mogą być praktycznie dowolne:

- liczby,
- teksty,
- listy,
- inne słowniki,
- zbiory,
- obiekty.

Przykład:

```python
dane = {
    "imie": "Ola",
    "wiek": 20,
    "oceny": [5, 4, 3],
    "adres": {
        "miasto": "Warszawa",
        "kod": "00-001"
    }
}
```

---

## Jak działają klucze

Klucz jest sposobem odnajdywania wartości.

Przykład:

```python
slownik = {
    "kolor": "niebieski"
}

print(slownik["kolor"])
```

Python nie szuka tu wartości po pozycji jak w liście.
Szuka po kluczu `"kolor"`.

To bardzo ważna różnica.

---

## Jakie typy mogą być kluczami

### Poprawne przykłady

```python
d1 = {"imie": "Ania"}
d2 = {1: "jeden"}
d3 = {(1, 2): "punkt"}
```

### Niepoprawny przykład

```python
d = {[1, 2]: "lista"}
```

To da błąd, bo lista jest mutowalna i nie może być kluczem.

### Dobra praktyka

Najczęściej używaj kluczy typu `str`.
To zwykle daje najbardziej czytelny kod.

---

## Odczyt wartości

### Przez `[]`

```python
osoba = {"imie": "Ania", "wiek": 17}

print(osoba["imie"])
print(osoba["wiek"])
```

### Uwaga

Jeśli klucza nie ma, pojawi się:

```python
KeyError
```

Przykład:

```python
print(osoba["miasto"])
```

### Przez `get()`

Bezpieczniejszy sposób:

```python
print(osoba.get("miasto"))
```

Jeśli klucza nie ma, dostaniesz `None`.

### Wartość domyślna

```python
print(osoba.get("miasto", "brak danych"))
```

To bardzo przydatne w praktyce.

---

## Dodawanie i zmiana elementów

W słowniku dodawanie i zmiana wartości wyglądają podobnie.

### Dodawanie nowej pary

```python
osoba = {"imie": "Ania"}
osoba["wiek"] = 17
print(osoba)
```

### Zmiana istniejącej wartości

```python
osoba["wiek"] = 18
print(osoba)
```

### Jak Python to rozpoznaje

- jeśli klucz nie istnieje, para zostanie dodana,
- jeśli klucz istnieje, wartość zostanie nadpisana.

---

## Usuwanie elementów

### `del`

```python
osoba = {"imie": "Ania", "wiek": 17}
del osoba["wiek"]
print(osoba)
```

### `pop()`

Usuwa klucz i zwraca jego wartość.

```python
wiek = osoba.pop("wiek")
print(wiek)
```

Jeśli klucza nie ma, będzie `KeyError`, chyba że podasz wartość domyślną:

```python
wartosc = osoba.pop("miasto", "brak")
```

### `popitem()`

Usuwa i zwraca ostatnią parę klucz-wartość.

```python
dane = {"a": 1, "b": 2}
print(dane.popitem())
```

### `clear()`

Usuwa wszystkie elementy.

```python
dane.clear()
```

---

## Sprawdzanie obecności klucza

Najczęściej sprawdzamy, czy istnieje klucz.

```python
osoba = {"imie": "Ania", "wiek": 17}

print("imie" in osoba)    # True
print("miasto" in osoba)  # False
```

### Ważne

Operator `in` sprawdza **klucze**, nie wartości.

```python
print("Ania" in osoba)  # False
```

Bo `"Ania"` to wartość, nie klucz.

---

## Najważniejsze metody słownika

Najczęściej używane:

- `get()`
- `keys()`
- `values()`
- `items()`
- `update()`
- `pop()`
- `popitem()`
- `clear()`
- `copy()`
- `setdefault()`

Za chwilę omówimy najważniejsze z nich w praktyce.

---

## Iteracja po słowniku

To jeden z najważniejszych tematów przy pracy ze słownikami.

Możesz iterować po:

- kluczach,
- wartościach,
- parach klucz-wartość.

---

## Iteracja po kluczach

Domyślnie pętla `for` po słowniku przechodzi po kluczach.

```python
osoba = {"imie": "Ania", "wiek": 17, "miasto": "Krakow"}

for klucz in osoba:
    print(klucz)
```

To samo można zapisać bardziej jawnie:

```python
for klucz in osoba.keys():
    print(klucz)
```

### Kiedy to przydatne

Gdy chcesz przejść po nazwach pól i coś z nimi zrobić.

---

## Iteracja po wartościach

Do tego służy `values()`.

```python
osoba = {"imie": "Ania", "wiek": 17, "miasto": "Krakow"}

for wartosc in osoba.values():
    print(wartosc)
```

### Kiedy to przydatne

Gdy interesują Cię same dane, a nie ich klucze.

---

## Iteracja po parach klucz-wartość

To bardzo częsty i bardzo wygodny sposób.

Do tego służy `items()`.

```python
osoba = {"imie": "Ania", "wiek": 17, "miasto": "Krakow"}

for klucz, wartosc in osoba.items():
    print(klucz, wartosc)
```

### To zwykle najlepszy wybór

Jeśli potrzebujesz jednocześnie:

- nazwy pola,
- wartości pola.

---

## Słowniki zagnieżdżone

Słownik może zawierać w sobie inne słowniki.

Przykład:

```python
uczen = {
    "imie": "Ania",
    "oceny": {
        "matematyka": 5,
        "polski": 4
    }
}
```

### Dostęp do zagnieżdżonych danych

```python
print(uczen["oceny"]["matematyka"])
```

To bardzo częsty wzorzec przy bardziej złożonych danych.

---

## Kopiowanie słowników

### Przypisanie to nie kopia

```python
a = {"x": 1, "y": 2}
b = a

b["x"] = 99
print(a)
```

`a` też się zmieni, bo obie zmienne wskazują na ten sam słownik.

### Płytka kopia

```python
a = {"x": 1, "y": 2}
b = a.copy()
```

albo:

```python
b = dict(a)
```

### Uwaga na zagnieżdżenia

```python
a = {"dane": {"x": 1}}
b = a.copy()

b["dane"]["x"] = 99
print(a)
```

To zmieni też `a`, bo kopiowanie jest płytkie.

### Głęboka kopia

```python
import copy

b = copy.deepcopy(a)
```

---

## Łączenie słowników

### `update()`

```python
a = {"x": 1, "y": 2}
b = {"y": 99, "z": 3}

a.update(b)
print(a)
```

### Co się stanie

- nowe klucze zostaną dodane,
- istniejące klucze zostaną nadpisane.

### Operator `|`

W nowszym Pythonie można też użyć:

```python
a = {"x": 1, "y": 2}
b = {"y": 99, "z": 3}

nowy = a | b
print(nowy)
```

To tworzy nowy słownik.

---

## Sortowanie przy pracy ze słownikiem

Sam słownik nie sortuje się tak jak lista przez `sort()`, ale możesz sortować jego klucze albo pary.

### Sortowanie po kluczach

```python
dane = {"b": 2, "a": 1, "c": 3}

for klucz in sorted(dane):
    print(klucz, dane[klucz])
```

### Sortowanie po wartościach

```python
dane = {"Ania": 90, "Bartek": 75, "Celina": 82}

for imie, wynik in sorted(dane.items(), key=lambda para: para[1]):
    print(imie, wynik)
```

To bardzo praktyczne przy rankingach i raportach.

---

## Złożoność operacji na słowniku

To ważna część tematu.

Gdy mówimy o złożoności, pytamy:

**jak szybko rośnie koszt operacji, gdy danych jest coraz więcej?**

W praktyce dla zwykłego słownika Pythona najważniejsze jest to:

- odczyt po kluczu jest zwykle bardzo szybki,
- dodawanie nowej pary jest zwykle bardzo szybkie,
- sprawdzanie, czy klucz istnieje, też jest zwykle bardzo szybkie,
- usuwanie po kluczu też jest zwykle bardzo szybkie.

### Najważniejsze przybliżenia

- odczyt `d[key]` - średnio `O(1)`,
- zapis `d[key] = value` - średnio `O(1)`,
- sprawdzenie `key in d` - średnio `O(1)`,
- usuwanie `del d[key]` - średnio `O(1)`,
- iteracja po całym słowniku - `O(n)`.

### Co to znaczy `O(1)`

To znaczy, że czas operacji nie rośnie mocno wraz z wielkością słownika.

W praktyce:

szukanie jednego klucza w słowniku jest zwykle bardzo szybkie, nawet jeśli słownik jest duży.

### Co to znaczy `O(n)`

To znaczy, że trzeba przejść przez wszystkie elementy.

Na przykład:

```python
for klucz in slownik:
    ...
```

Im więcej elementów, tym dłużej to potrwa.

---

## Dlaczego słownik jest szybki

Python implementuje słownik przy pomocy tablicy haszującej.

Nie musisz znać wszystkich szczegółów technicznych, ale warto rozumieć ideę:

- klucz jest przekształcany na specjalną liczbę zwaną hashem,
- dzięki temu Python może bardzo szybko odnaleźć miejsce, gdzie przechowywana jest wartość.

Dlatego:

- `slownik["imie"]`

jest zwykle dużo wygodniejsze i szybsze do wyszukiwania niż ręczne przeszukiwanie listy.

### Ważne

Mówimy o **średniej** złożoności.
W szczególnych przypadkach może być gorzej, ale w praktyce słownik jest bardzo szybki i dlatego tak często używany.

---

## Kiedy słownik jest lepszy od listy

Użyj słownika, gdy:

- chcesz odwoływać się do danych po nazwie,
- dane mają strukturę klucz-wartość,
- chcesz szybko wyszukiwać po kluczu,
- chcesz mapować jedną wartość na drugą.

Użyj listy, gdy:

- liczy się kolejność elementów,
- pracujesz głównie po indeksach,
- przechowujesz serię podobnych elementów.

### Przykład

Lepszy `dict`:

```python
uczen = {"imie": "Ania", "wiek": 17}
```

Lepsza lista:

```python
oceny = [5, 4, 3, 5]
```

---

## Typowe błędy początkujących

### 1. Zakładanie, że `in` sprawdza wartości

```python
osoba = {"imie": "Ania"}
print("Ania" in osoba)
```

To da `False`, bo `in` sprawdza klucze.

### 2. Odczyt nieistniejącego klucza przez `[]`

```python
print(osoba["wiek"])
```

To da `KeyError`.

### 3. Używanie listy jako klucza

```python
d = {[1, 2]: "x"}
```

To błąd.

### 4. Mylenie słownika ze zbiorem

`{}` to pusty słownik, nie pusty zbiór.

### 5. Przekonanie, że przypisanie tworzy kopię

```python
a = {"x": 1}
b = a
```

To nie kopia.

### 6. Modyfikowanie słownika podczas iteracji bez ostrożności

To może prowadzić do błędów albo nieczytelnego kodu.

### 7. Zbyt mechaniczne uczenie się złożoności bez rozumienia

Najważniejsze praktycznie:

- operacje po kluczu są szybkie,
- przechodzenie po wszystkich elementach rośnie wraz z rozmiarem słownika.

---

## Praktyczne przykłady

### Dane użytkownika

```python
uzytkownik = {
    "login": "ania123",
    "email": "ania@example.com",
    "aktywny": True
}

print(uzytkownik["email"])
```

### Liczenie wystąpień

```python
tekst = "ala"
licznik = {}

for znak in tekst:
    if znak in licznik:
        licznik[znak] += 1
    else:
        licznik[znak] = 1

print(licznik)
```

### Bezpieczny odczyt przez `get()`

```python
ustawienia = {"jezyk": "pl"}
print(ustawienia.get("motyw", "jasny"))
```

### Iteracja po parach

```python
oceny = {"matematyka": 5, "polski": 4, "angielski": 5}

for przedmiot, ocena in oceny.items():
    print(przedmiot, ocena)
```

### Słownik zagnieżdżony

```python
firma = {
    "nazwa": "ABC",
    "adres": {
        "miasto": "Gdansk",
        "ulica": "Dluga 10"
    }
}

print(firma["adres"]["miasto"])
```

### Łączenie danych

```python
a = {"imie": "Ania", "wiek": 17}
b = {"wiek": 18, "miasto": "Krakow"}

nowy = a | b
print(nowy)
```

---

## Dobre praktyki

### Używaj czytelnych kluczy

Najczęściej typu `str`.

### Używaj `get()`, gdy klucz może nie istnieć

To zmniejsza ryzyko `KeyError`.

### Iteruj przez `items()`, jeśli potrzebujesz klucza i wartości

To zwykle najczytelniejsze rozwiązanie.

### Nie nadużywaj zagnieżdżeń

Bardzo głęboko zagnieżdżone słowniki stają się trudne do czytania.

### Uważaj przy kopiowaniu

Szczególnie gdy w środku są inne słowniki lub listy.

### Pamiętaj o praktycznej złożoności

Jeśli chcesz szybko szukać danych po nazwie, słownik zwykle będzie świetnym wyborem.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- `dict` przechowuje dane jako pary klucz-wartość,
- klucze muszą być unikalne i hashowalne,
- wartości mogą być prawie dowolne,
- odczyt po `[]` daje `KeyError`, jeśli klucza nie ma,
- `get()` pozwala czytać bezpieczniej,
- `items()`, `keys()`, `values()` są podstawą iteracji,
- słowniki świetnie nadają się do danych nazwanych,
- operacje po kluczu są zwykle bardzo szybkie, średnio `O(1)`,
- iteracja po całym słowniku ma złożoność `O(n)`,
- słownik jest jednym z najważniejszych i najczęściej używanych typów w Pythonie.

Jeśli dobrze opanujesz słowniki, bardzo duża część praktycznego Pythona stanie się dużo prostsza i bardziej naturalna.

---

## Mini ściąga

### Tworzenie

```python
d = {"imie": "Ania", "wiek": 17}
```

### Odczyt

```python
d["imie"]
d.get("miasto")
d.get("miasto", "brak")
```

### Dodawanie i zmiana

```python
d["miasto"] = "Krakow"
d["wiek"] = 18
```

### Usuwanie

```python
del d["wiek"]
d.pop("miasto")
d.clear()
```

### Iteracja

```python
for k in d:
    ...

for v in d.values():
    ...

for k, v in d.items():
    ...
```

### Kopia

```python
kopia = d.copy()
```

### Złożoność

```python
d[key]          # srednio O(1)
key in d        # srednio O(1)
del d[key]      # srednio O(1)
for k in d:     # O(n)
```

---

## Ćwiczenia

### Ćwiczenie 1

Utwórz słownik opisujący osobę:

- imię,
- wiek,
- miasto.

Potem wypisz wszystkie wartości.

### Ćwiczenie 2

Dodaj do słownika nowy klucz `zawod`, a potem zmień wartość klucza `wiek`.

### Ćwiczenie 3

Przejdź po słowniku:

- po kluczach,
- po wartościach,
- po parach klucz-wartość.

### Ćwiczenie 4

Spróbuj odczytać nieistniejący klucz przez `[]`, a potem zrób to samo przez `get()`.

### Ćwiczenie 5

Napisz program liczący wystąpienia liter w krótkim napisie.

### Ćwiczenie 6

Utwórz zagnieżdżony słownik opisujący firmę i jej adres.

---

## Przykładowe rozwiązania

### Ćwiczenie 1

```python
osoba = {
    "imie": "Ania",
    "wiek": 17,
    "miasto": "Krakow"
}

print(osoba.values())
```

### Ćwiczenie 2

```python
osoba["zawod"] = "Uczennica"
osoba["wiek"] = 18
print(osoba)
```

### Ćwiczenie 3

```python
for klucz in osoba:
    print(klucz)

for wartosc in osoba.values():
    print(wartosc)

for klucz, wartosc in osoba.items():
    print(klucz, wartosc)
```

### Ćwiczenie 4

```python
# print(osoba["telefon"])  # KeyError
print(osoba.get("telefon"))
print(osoba.get("telefon", "brak numeru"))
```

### Ćwiczenie 5

```python
tekst = "python"
wynik = {}

for znak in tekst:
    if znak in wynik:
        wynik[znak] += 1
    else:
        wynik[znak] = 1

print(wynik)
```

### Ćwiczenie 6

```python
firma = {
    "nazwa": "ABC",
    "adres": {
        "miasto": "Gdansk",
        "ulica": "Dluga 10"
    }
}

print(firma["adres"]["ulica"])
```

---

## Na koniec

Najlepszy sposób nauki słowników to używanie ich do opisywania prawdziwych danych.

Warto:

1. tworzyć słowniki opisujące osoby, produkty, zamówienia,
2. ćwiczyć `get()`, `items()`, `update()` i `pop()`,
3. porównywać sytuacje, w których lepsza jest lista, a w których słownik,
4. budować zagnieżdżone struktury,
5. obserwować, jak wygodne jest szybkie wyszukiwanie po kluczu.

Wtedy bardzo szybko staje się jasne, dlaczego `dict` jest jednym z najważniejszych narzędzi w Pythonie.
