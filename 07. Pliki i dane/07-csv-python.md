# `csv` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest CSV](#czym-jest-csv)
3. [Po co używać modułu `csv`](#po-co-używać-modułu-csv)
4. [`reader`](#reader)
5. [`writer`](#writer)
6. [`DictReader`](#dictreader)
7. [`DictWriter`](#dictwriter)
8. [Delimiter i nagłówki](#delimiter-i-nagłówki)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczne przykłady](#praktyczne-przykłady)
11. [Dobre praktyki](#dobre-praktyki)
12. [Podsumowanie](#podsumowanie)
13. [Mini ściąga](#mini-ściąga)
14. [Ćwiczenia](#ćwiczenia)
15. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`csv` to moduł standardowej biblioteki do pracy z plikami CSV.

CSV jest bardzo popularny przy:

- eksportach z Excela,
- prostych raportach,
- wymianie danych między systemami,
- analizie tabelarycznej.

---

## Czym jest CSV

CSV to tekstowy format tabelaryczny.

Przykład:

```text
name,age
Anna,30
Jan,25
```

Kolumny są zwykle rozdzielone przecinkiem, ale nie zawsze.

---

## Po co używać modułu `csv`

Moduł `csv` pomaga poprawnie:

- czytać wiersze,
- zapisywać wiersze,
- pracować z nagłówkami,
- obsługiwać różne separatory.

Lepiej używać go niż ręcznie robić `split(",")`.

---

## `reader`

```python
import csv

with open("dane.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

Każdy wiersz to lista stringów.

---

## `writer`

```python
import csv

with open("wynik.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerow(["Anna", 30])
```

---

## `DictReader`

To bardzo wygodne przy plikach z nagłówkami.

```python
import csv

with open("dane.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])
```

Każdy wiersz jest słownikiem.

---

## `DictWriter`

```python
import csv

with open("users.csv", "w", encoding="utf-8", newline="") as f:
    fieldnames = ["name", "age"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"name": "Anna", "age": 30})
```

---

## Delimiter i nagłówki

Nie każdy CSV używa przecinka.

Na przykład:

```python
reader = csv.reader(f, delimiter=";")
```

To częste w danych eksportowanych z różnych systemów.

---

## Typowe błędy początkujących

- brak `newline=""` przy otwieraniu pliku,
- ręczne dzielenie po przecinku zamiast modułu `csv`,
- zakładanie, że separator zawsze jest taki sam,
- zapominanie, że wartości z CSV są stringami.

---

## Praktyczne przykłady

### Odczyt z nagłówkami

```python
import csv

with open("users.csv", "r", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        print(row["name"])
```

### Zapis raportu

```python
import csv

rows = [
    ["produkt", "cena"],
    ["kawa", 20],
    ["herbata", 15],
]

with open("raport.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
```

---

## Dobre praktyki

- zawsze używaj `newline=""`,
- używaj `DictReader` i `DictWriter`, gdy plik ma sensowne nagłówki,
- pamiętaj o konwersji typów po odczycie,
- jawnie ustawiaj `delimiter`, jeśli format tego wymaga.

---

## Podsumowanie

`csv` to prosty, ale bardzo praktyczny moduł do pracy z danymi tabelarycznymi.

W codziennej pracy szczególnie wygodne są:

- `DictReader`,
- `DictWriter`,
- poprawne otwieranie plików z `newline=""`.

---

## Mini ściąga

```python
import csv

with open("dane.csv", "r", encoding="utf-8", newline="") as f:
    for row in csv.reader(f):
        print(row)
```

Najważniejsze:

- `reader` czyta listy,
- `writer` zapisuje listy,
- `DictReader` czyta słowniki,
- `DictWriter` zapisuje słowniki.

---

## Ćwiczenia

1. Wczytaj plik CSV i wypisz każdy wiersz.
2. Zapisz prostą tabelę do pliku CSV.
3. Użyj `DictReader` do odczytu nazw kolumn.
4. Użyj `DictWriter` do zapisania listy słowników.
5. Wczytaj plik rozdzielany średnikiem.

---

## Przykładowe rozwiązania

### 1. Odczyt

```python
import csv

with open("dane.csv", "r", encoding="utf-8", newline="") as f:
    for row in csv.reader(f):
        print(row)
```

### 2. Zapis

```python
import csv

with open("out.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["a", "b"])
    writer.writerow([1, 2])
```

### 3. `DictReader`

```python
import csv

with open("users.csv", "r", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        print(row["name"])
```

### 4. `DictWriter`

```python
import csv

with open("users.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerow({"name": "Ala", "age": 20})
```

### 5. Średnik

```python
import csv

with open("dane.csv", "r", encoding="utf-8", newline="") as f:
    for row in csv.reader(f, delimiter=";"):
        print(row)
```
