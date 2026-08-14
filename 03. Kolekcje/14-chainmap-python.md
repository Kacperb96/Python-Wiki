# ChainMap w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `ChainMap`](#czym-jest-chainmap)
3. [Skąd importować `ChainMap`](#skad-importowac-chainmap)
4. [Po co używać `ChainMap`](#po-co-uzywac-chainmap)
5. [Jak myśleć o `ChainMap`](#jak-myslec-o-chainmap)
6. [Tworzenie `ChainMap`](#tworzenie-chainmap)
7. [Jak działa wyszukiwanie kluczy](#jak-dziala-wyszukiwanie-kluczy)
8. [Kolejność słowników i priorytety](#kolejnosc-slownikow-i-priorytety)
9. [Odczyt danych](#odczyt-danych)
10. [Dodawanie i zmiana danych](#dodawanie-i-zmiana-danych)
11. [`new_child()`](#new_child)
12. [`maps`](#maps)
13. [`ChainMap` a scalanie słowników](#chainmap-a-scalanie-slownikow)
14. [Kiedy `ChainMap` jest lepszy od `|`](#kiedy-chainmap-jest-lepszy-od-)
15. [Typowe zastosowania](#typowe-zastosowania)
16. [Typowe błędy początkujących](#typowe-bledy-poczatkujacych)
17. [Praktyczne przykłady](#praktyczne-przyklady)
18. [Dobre praktyki](#dobre-praktyki)
19. [Podsumowanie](#podsumowanie)
20. [Mini ściąga](#mini-sciaga)
21. [Ćwiczenia](#cwiczenia)
22. [Przykładowe rozwiązania](#przykladowe-rozwiazania)

---

## Wprowadzenie

`ChainMap` to mniej znana, ale bardzo praktyczna struktura z modułu `collections`.

Pozwala traktować kilka słowników jak jeden wspólny widok.

To przydaje się wtedy, gdy masz dane z różnych warstw, na przykład:

- ustawienia domyślne,
- ustawienia użytkownika,
- ustawienia chwilowe,
- dane lokalne i globalne,
- nadpisania dla testów.

---

## Czym jest `ChainMap`

`ChainMap` łączy kilka mapowań, najczęściej słowników, w jeden obiekt odczytowy-zapisowy.

Przykład:

```python
from collections import ChainMap

a = {"x": 1, "y": 2}
b = {"y": 99, "z": 3}

c = ChainMap(a, b)
print(c)
```

Wynik:

```python
ChainMap({'x': 1, 'y': 2}, {'y': 99, 'z': 3})
```

To nie jest nowy scalony słownik.
To widok na kilka słowników.

---

## Skąd importować `ChainMap`

```python
from collections import ChainMap
```

---

## Po co używać `ChainMap`

Bo czasem nie chcesz kopiować i scalać danych.

Chcesz tylko:

- czytać je warstwowo,
- mieć priorytety,
- zachować osobne źródła danych,
- łatwo nadpisywać wybrane wartości.

`ChainMap` jest właśnie takim narzędziem.

---

## Jak myśleć o `ChainMap`

Najprostszy model mentalny:

`ChainMap(a, b, c)` znaczy:

1. najpierw szukaj w `a`,
2. jeśli nie ma, szukaj w `b`,
3. jeśli dalej nie ma, szukaj w `c`.

Pierwsze trafienie wygrywa.

---

## Tworzenie `ChainMap`

```python
from collections import ChainMap

domyslne = {"kolor": "niebieski", "jezyk": "pl"}
uzytkownik = {"jezyk": "en"}

ustawienia = ChainMap(uzytkownik, domyslne)
print(ustawienia)
```

Wynik:

```python
ChainMap({'jezyk': 'en'}, {'kolor': 'niebieski', 'jezyk': 'pl'})
```

---

## Jak działa wyszukiwanie kluczy

```python
from collections import ChainMap

domyslne = {"kolor": "niebieski", "jezyk": "pl"}
uzytkownik = {"jezyk": "en"}

ustawienia = ChainMap(uzytkownik, domyslne)

print(ustawienia["jezyk"])
print(ustawienia["kolor"])
```

Wynik:

```python
en
niebieski
```

`"jezyk"` został znaleziony w pierwszym słowniku.
`"kolor"` nie było w pierwszym, więc został znaleziony w drugim.

---

## Kolejność słowników i priorytety

Kolejność jest kluczowa.

```python
from collections import ChainMap

a = {"x": 1}
b = {"x": 99}

print(ChainMap(a, b)["x"])
print(ChainMap(b, a)["x"])
```

Wynik:

```python
1
99
```

Ten sam zestaw danych, ale inny priorytet.

---

## Odczyt danych

`ChainMap` możesz czytać podobnie jak zwykły słownik.

```python
from collections import ChainMap

ustawienia = ChainMap({"jezyk": "en"}, {"kolor": "niebieski"})

print(ustawienia["jezyk"])
print("kolor" in ustawienia)
print(ustawienia.get("motyw"))
```

Wynik:

```python
en
True
None
```

---

## Dodawanie i zmiana danych

To bardzo ważna zasada:

**zapis trafia tylko do pierwszego słownika w `ChainMap`.**

```python
from collections import ChainMap

a = {"x": 1}
b = {"y": 2}

c = ChainMap(a, b)
c["z"] = 3
c["x"] = 99

print(a)
print(b)
print(c)
```

Wynik:

```python
{'x': 99, 'z': 3}
{'y': 2}
ChainMap({'x': 99, 'z': 3}, {'y': 2})
```

Drugi słownik nie został zmieniony.

---

## `new_child()`

Tworzy nowy `ChainMap` z dodatkowym pustym słownikiem na początku.

```python
from collections import ChainMap

base = ChainMap({"x": 1})
child = base.new_child()

child["x"] = 99
child["y"] = 2

print(child["x"])
print(base["x"])
print(child.maps)
```

Wynik:

```python
99
1
[{'x': 99, 'y': 2}, {'x': 1}]
```

To bardzo wygodny mechanizm lokalnego nadpisania.

---

## `maps`

`ChainMap` przechowuje swoje wewnętrzne mapy w atrybucie `.maps`.

```python
from collections import ChainMap

c = ChainMap({"a": 1}, {"b": 2})
print(c.maps)
```

Wynik:

```python
[{'a': 1}, {'b': 2}]
```

To po prostu lista słowników, po których `ChainMap` chodzi przy wyszukiwaniu.

---

## `ChainMap` a scalanie słowników

Porównajmy:

```python
domyslne = {"motyw": "jasny", "jezyk": "pl"}
uzytkownik = {"jezyk": "en"}

nowy = domyslne | uzytkownik
print(nowy)
```

Wynik:

```python
{'motyw': 'jasny', 'jezyk': 'en'}
```

To jest nowy słownik.

A `ChainMap`:

```python
from collections import ChainMap

ustawienia = ChainMap(uzytkownik, domyslne)
print(ustawienia["motyw"])
print(ustawienia["jezyk"])
```

Wynik:

```python
jasny
en
```

Efekt odczytu jest podobny, ale mechanizm zupełnie inny.

---

## Kiedy `ChainMap` jest lepszy od `|`

`ChainMap` jest lepszy, gdy:

- nie chcesz kopiować danych,
- chcesz zachować warstwy osobno,
- chcesz dynamicznie widzieć zmiany w oryginalnych słownikach,
- chcesz łatwo dodać lokalną warstwę nadpisania.

Operator `|` jest lepszy, gdy:

- naprawdę chcesz dostać jeden nowy słownik,
- nie interesują Cię już źródłowe warstwy,
- zależy Ci na prostym finalnym obiekcie.

---

## Typowe zastosowania

- system konfiguracji,
- zmienne lokalne i globalne,
- warstwy domyślne i użytkownika,
- testowe nadpisania ustawień,
- proste systemy scope.

---

## Typowe błędy początkujących

### 1. Oczekiwanie, że zapis zmienia wszystkie słowniki

Nie.
Zmienia tylko pierwszy.

### 2. Niezrozumienie kolejności

Pierwszy słownik ma najwyższy priorytet.

### 3. Mylenie `ChainMap` ze scaleniem

To widok na wiele słowników, a nie pełna kopia w jeden.

### 4. Zapominanie, że zmiany w oryginalnych słownikach są widoczne

Jeśli zmienisz jeden z bazowych słowników, `ChainMap` też to “zobaczy”.

---

## Praktyczne przykłady

### Ustawienia z nadpisaniem użytkownika

```python
from collections import ChainMap

domyslne = {"motyw": "jasny", "jezyk": "pl", "timeout": 30}
uzytkownik = {"jezyk": "en"}

ustawienia = ChainMap(uzytkownik, domyslne)

print(ustawienia["motyw"])
print(ustawienia["jezyk"])
print(ustawienia["timeout"])
```

Wynik:

```python
jasny
en
30
```

### Tymczasowe lokalne nadpisanie

```python
from collections import ChainMap

globalne = {"debug": False, "timeout": 30}
ustawienia = ChainMap(globalne)

lokalne = ustawienia.new_child()
lokalne["debug"] = True

print(lokalne["debug"])
print(ustawienia["debug"])
```

Wynik:

```python
True
False
```

---

## Dobre praktyki

- Używaj `ChainMap`, gdy pracujesz na warstwach danych.
- Dbaj o kolejność słowników.
- Pamiętaj, że zapis trafia do pierwszej mapy.
- Gdy chcesz finalny słownik, użyj raczej `|` albo `dict(...)`.
- Dobrze nazywaj warstwy: `domyslne`, `uzytkownik`, `lokalne`, `tymczasowe`.

---

## Podsumowanie

`ChainMap` pozwala traktować kilka słowników jak jeden widok z priorytetami.

Najważniejsze do zapamiętania:

- odczyt przeszukuje mapy od lewej do prawej,
- pierwsze trafienie wygrywa,
- zapis trafia tylko do pierwszego słownika.

To świetne narzędzie do konfiguracji i pracy warstwowej na danych.

---

## Mini ściąga

```python
from collections import ChainMap

domyslne = {"jezyk": "pl"}
uzytkownik = {"jezyk": "en"}

ustawienia = ChainMap(uzytkownik, domyslne)
print(ustawienia["jezyk"])

lokalne = ustawienia.new_child()
lokalne["debug"] = True
```

---

## Ćwiczenia

1. Połącz dwa słowniki przez `ChainMap` i sprawdź odczyt kluczy.
2. Zmień kolejność słowników i pokaż różnicę.
3. Pokaż, że zapis trafia do pierwszej mapy.
4. Użyj `new_child()` do stworzenia lokalnego nadpisania konfiguracji.
5. Porównaj `ChainMap` z operatorem `|`.

---

## Przykładowe rozwiązania

```python
from collections import ChainMap

domyslne = {"motyw": "jasny", "jezyk": "pl"}
uzytkownik = {"jezyk": "en"}

ustawienia = ChainMap(uzytkownik, domyslne)
print(ustawienia["jezyk"])
print(ustawienia["motyw"])
```

```python
from collections import ChainMap

base = ChainMap({"x": 1})
child = base.new_child()
child["x"] = 99

print(child["x"])
print(base["x"])
```
