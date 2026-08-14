# `os` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co używać `os`](#po-co-używać-os)
3. [Pliki i katalogi](#pliki-i-katalogi)
4. [Aktualny katalog roboczy](#aktualny-katalog-roboczy)
5. [Tworzenie i usuwanie katalogów](#tworzenie-i-usuwanie-katalogów)
6. [Zmienne środowiskowe](#zmienne-środowiskowe)
7. [Listowanie katalogów](#listowanie-katalogów)
8. [`os.path`](#ospath)
9. [Identyfikacja systemu](#identyfikacja-systemu)
10. [Typowe błędy początkujących](#typowe-błędy-początkujących)
11. [Praktyczne przykłady](#praktyczne-przykłady)
12. [Dobre praktyki](#dobre-praktyki)
13. [Podsumowanie](#podsumowanie)
14. [Mini ściąga](#mini-ściąga)
15. [Ćwiczenia](#ćwiczenia)
16. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`os` to jeden z podstawowych modułów standardowej biblioteki Pythona.

Pozwala komunikować się z systemem operacyjnym.

Przydaje się do pracy z:

- katalogami,
- plikami,
- zmiennymi środowiskowymi,
- informacjami o systemie.

---

## Po co używać `os`

`os` jest przydatny, gdy chcesz:

- sprawdzić bieżący katalog,
- listować pliki,
- odczytać zmienne środowiskowe,
- tworzyć katalogi,
- pisać skrypty systemowe.

---

## Pliki i katalogi

Wiele operacji systemowych zaczyna się właśnie od `os`.

```python
import os

print(os.getcwd())
```

To zwraca aktualny katalog roboczy.

---

## Aktualny katalog roboczy

```python
import os

print(os.getcwd())
os.chdir("..")
print(os.getcwd())
```

`chdir()` zmienia katalog roboczy procesu.

---

## Tworzenie i usuwanie katalogów

```python
import os

os.mkdir("raporty")
os.makedirs("a/b/c", exist_ok=True)
```

Usuwanie:

```python
os.rmdir("pusty_folder")
```

---

## Zmienne środowiskowe

```python
import os

print(os.environ.get("HOME"))
print(os.getenv("HOME"))
```

To bardzo częste w konfiguracji aplikacji.

---

## Listowanie katalogów

```python
import os

for nazwa in os.listdir("."):
    print(nazwa)
```

To zwraca nazwy elementów jako stringi.

---

## `os.path`

Choć dziś często wygodniejszy jest `pathlib`, `os.path` nadal jest bardzo spotykany.

```python
import os

sciezka = os.path.join("dane", "raport.txt")
print(os.path.exists(sciezka))
print(os.path.isfile(sciezka))
print(os.path.isdir("dane"))
```

---

## Identyfikacja systemu

```python
import os

print(os.name)
```

To pomaga w prostych skryptach zależnych od platformy.

---

## Typowe błędy początkujących

- ręczne sklejanie ścieżek zamiast `os.path.join()`,
- zakładanie, że zmienna środowiskowa zawsze istnieje,
- usuwanie katalogów bez upewnienia się, że są puste,
- mieszanie `os` i `pathlib` bez planu.

---

## Praktyczne przykłady

### Odczyt zmiennej środowiskowej

```python
import os

token = os.getenv("API_TOKEN")
print(token)
```

### Tworzenie katalogu, jeśli nie istnieje

```python
import os

os.makedirs("wyniki", exist_ok=True)
```

---

## Dobre praktyki

- do nowych projektów często wybieraj `pathlib` do ścieżek,
- `os` zachowaj do operacji systemowych i env varów,
- używaj `getenv()` lub `environ.get()` zamiast bezpośredniego indeksowania,
- ostrożnie zmieniaj katalog roboczy `chdir()`.

---

## Podsumowanie

`os` to podstawowe narzędzie do pracy z systemem operacyjnym z poziomu Pythona.

Nawet jeśli część pracy ze ścieżkami przejmie `pathlib`, `os` nadal pozostaje bardzo ważnym modułem.

---

## Mini ściąga

```python
import os

print(os.getcwd())
print(os.getenv("HOME"))
print(os.listdir("."))
```

Najważniejsze:

- `getcwd()` zwraca bieżący katalog,
- `chdir()` zmienia katalog,
- `listdir()` listuje elementy,
- `getenv()` czyta zmienne środowiskowe,
- `makedirs()` tworzy zagnieżdżone katalogi.

---

## Ćwiczenia

1. Wypisz bieżący katalog roboczy.
2. Pobierz wartość zmiennej środowiskowej `HOME`.
3. Utwórz katalog `tmp/test`.
4. Wypisz wszystkie elementy z bieżącego katalogu.
5. Zbuduj ścieżkę do `dane/raport.csv` przez `os.path.join()`.

---

## Przykładowe rozwiązania

### 1. Katalog roboczy

```python
import os

print(os.getcwd())
```

### 2. `HOME`

```python
import os

print(os.getenv("HOME"))
```

### 3. Tworzenie katalogu

```python
import os

os.makedirs("tmp/test", exist_ok=True)
```

### 4. Listowanie

```python
import os

for nazwa in os.listdir("."):
    print(nazwa)
```

### 5. `join`

```python
import os

sciezka = os.path.join("dane", "raport.csv")
print(sciezka)
```
