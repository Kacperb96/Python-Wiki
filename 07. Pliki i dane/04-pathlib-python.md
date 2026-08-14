# `pathlib` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co używać `pathlib`](#po-co-używać-pathlib)
3. [Czym jest `Path`](#czym-jest-path)
4. [Tworzenie ścieżek](#tworzenie-ścieżek)
5. [Łączenie ścieżek](#łączenie-ścieżek)
6. [Sprawdzanie istnienia plików i folderów](#sprawdzanie-istnienia-plików-i-folderów)
7. [Odczyt i zapis plików](#odczyt-i-zapis-plików)
8. [Iterowanie po katalogach](#iterowanie-po-katalogach)
9. [`glob()` i `rglob()`](#glob-i-rglob)
10. [Tworzenie katalogów](#tworzenie-katalogów)
11. [Typowe błędy początkujących](#typowe-błędy-początkujących)
12. [Praktyczne przykłady](#praktyczne-przykłady)
13. [Dobre praktyki](#dobre-praktyki)
14. [Podsumowanie](#podsumowanie)
15. [Mini ściąga](#mini-ściąga)
16. [Ćwiczenia](#ćwiczenia)
17. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`pathlib` to nowoczesny moduł Pythona do pracy ze ścieżkami i plikami.

Zamiast ręcznie sklejać stringi reprezentujące ścieżki, możesz operować na obiektach.

To zwykle czytelniejsze, bezpieczniejsze i wygodniejsze.

---

## Po co używać `pathlib`

`pathlib` pomaga:

- czytelnie budować ścieżki,
- pracować przenośnie między systemami,
- łatwo czytać i zapisywać pliki,
- wygodnie iterować po katalogach.

To jedno z tych narzędzi, które szybko staje się codziennym standardem.

---

## Czym jest `Path`

Najważniejsza klasa to `Path`.

```python
from pathlib import Path
```

Przykład:

```python
sciezka = Path("dane/plik.txt")
print(sciezka)
```

`Path` reprezentuje ścieżkę do pliku lub katalogu.

Wynik:

```python
dane/plik.txt
```

---

## Tworzenie ścieżek

```python
from pathlib import Path

plik = Path("raport.txt")
folder = Path("dane")
```

Możesz też odwołać się do katalogu domowego:

```python
home = Path.home()
print(home)
```

Wynik będzie zależał od systemu, np.:

```python
/home/kacper
```

---

## Łączenie ścieżek

Jedna z największych zalet `pathlib`:

```python
from pathlib import Path

sciezka = Path("dane") / "2026" / "raport.csv"
print(sciezka)
```

Operator `/` łączy fragmenty ścieżki w czytelny sposób.

Wynik:

```python
dane/2026/raport.csv
```

---

## Sprawdzanie istnienia plików i folderów

```python
from pathlib import Path

sciezka = Path("dane.txt")

print(sciezka.exists())
print(sciezka.is_file())
print(sciezka.is_dir())
```

To bardzo częste operacje.

Przykładowy wynik dla istniejącego pliku:

```python
True
True
False
```

---

## Odczyt i zapis plików

```python
from pathlib import Path

plik = Path("notatka.txt")
plik.write_text("Czesc", encoding="utf-8")

tekst = plik.read_text(encoding="utf-8")
print(tekst)
```

Wynik:

```python
Czesc
```

Do bajtów masz:

- `write_bytes()`
- `read_bytes()`

---

## Iterowanie po katalogach

```python
from pathlib import Path

folder = Path(".")

for element in folder.iterdir():
    print(element)
```

To zwraca obiekty `Path`, a nie zwykłe stringi.

Przykładowy wynik:

```python
README.md
main.py
dane
```

---

## `glob()` i `rglob()`

Wyszukiwanie plików po wzorcu:

```python
from pathlib import Path

for plik in Path(".").glob("*.py"):
    print(plik)
```

Rekurencyjnie:

```python
for plik in Path(".").rglob("*.md"):
    print(plik)
```

Różnica:

- `glob("*.py")` szuka tylko w jednym katalogu,
- `rglob("*.md")` schodzi też do podkatalogów.

---

## Tworzenie katalogów

```python
from pathlib import Path

Path("wyniki").mkdir(exist_ok=True)
Path("a/b/c").mkdir(parents=True, exist_ok=True)
```

`parents=True` tworzy brakujące katalogi po drodze.

To odpowiednik „utwórz cały brakujący łańcuch folderów”.

---

## Typowe błędy początkujących

- traktowanie `Path` jak zwykłego stringa w każdym miejscu,
- ręczne sklejanie ścieżek zamiast używania `/`,
- brak `encoding` przy pracy z tekstem,
- mylenie `glob()` z `rglob()`.

### 5. Zakładanie, że `pathlib` służy tylko do ścieżek

`Path` potrafi też wygodnie czytać i zapisywać pliki.

---

## Praktyczne przykłady

### Lista plików `.txt`

```python
from pathlib import Path

for plik in Path(".").glob("*.txt"):
    print(plik.name)
```

Wynik przykładowy:

```python
notatka.txt
log.txt
```

### Zapis raportu

```python
from pathlib import Path

folder = Path("raporty")
folder.mkdir(exist_ok=True)

plik = folder / "dzienny.txt"
plik.write_text("Raport gotowy", encoding="utf-8")
```

Efekt:

powstanie plik `raporty/dzienny.txt` z podaną treścią.

---

## Dobre praktyki

- preferuj `pathlib` zamiast ręcznej pracy na stringach,
- używaj `/` do łączenia ścieżek,
- zawsze jawnie ustawiaj `encoding` dla tekstu,
- operuj na obiektach `Path` możliwie długo.

Praktyczna zasada:

jeśli pracujesz ze ścieżką, trzymaj ją jako `Path`, a nie jako zwykły string, tak długo jak się da.

---

## Podsumowanie

`pathlib` upraszcza pracę z plikami i katalogami.

To jeden z najbardziej praktycznych modułów standardowej biblioteki Pythona i bardzo szybko poprawia czytelność kodu.

Najważniejsze do zapamiętania:

- `Path` daje czytelniejszą pracę ze ścieżkami niż ręczne sklejenia,
- `/` to podstawowy operator budowania ścieżek,
- `pathlib` łączy wygodną pracę ze ścieżką i z samym plikiem.

---

## Mini ściąga

```python
from pathlib import Path

plik = Path("dane") / "raport.txt"

print(plik.exists())
print(plik.read_text(encoding="utf-8"))
```

Najważniejsze:

- `Path(...)` tworzy ścieżkę,
- `/` łączy ścieżki,
- `exists()`, `is_file()`, `is_dir()` sprawdzają typ,
- `read_text()` i `write_text()` upraszczają pracę z plikami.

---

## Ćwiczenia

1. Utwórz ścieżkę do pliku `dane/2026/wynik.txt`.
2. Sprawdź, czy istnieje plik `config.json`.
3. Odczytaj zawartość pliku tekstowego przez `pathlib`.
4. Znajdź wszystkie pliki `.py` w bieżącym katalogu.
5. Utwórz katalog `backup/2026`.

---

## Przykładowe rozwiązania

### 1. Ścieżka

```python
from pathlib import Path

sciezka = Path("dane") / "2026" / "wynik.txt"
```

### 2. Istnienie pliku

```python
from pathlib import Path

print(Path("config.json").exists())
```

### 3. Odczyt

```python
from pathlib import Path

tekst = Path("notatka.txt").read_text(encoding="utf-8")
print(tekst)
```

### 4. Pliki `.py`

```python
from pathlib import Path

for plik in Path(".").glob("*.py"):
    print(plik)
```

### 5. Katalog

```python
from pathlib import Path

Path("backup/2026").mkdir(parents=True, exist_ok=True)
```
