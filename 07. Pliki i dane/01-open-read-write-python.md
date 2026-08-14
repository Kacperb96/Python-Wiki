# Odczyt i zapis plików w Pythonie — `open()`

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co znać `open()`](#po-co-znać-open)
3. [Podstawowy zapis i odczyt](#podstawowy-zapis-i-odczyt)
4. [Tryby otwierania plików](#tryby-otwierania-plików)
5. [`with open(...)`](#with-open)
6. [Odczyt całego pliku vs linie](#odczyt-całego-pliku-vs-linie)
7. [Dopisanie do pliku](#dopisanie-do-pliku)
8. [Typowe błędy początkujących](#typowe-błędy-początkujących)
9. [Praktyczne przykłady](#praktyczne-przykłady)
10. [Dobre praktyki](#dobre-praktyki)
11. [Podsumowanie](#podsumowanie)
12. [Mini ściąga](#mini-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Praca z plikami to jedna z najczęstszych codziennych czynności w Pythonie.

Podstawowym narzędziem jest funkcja `open()`.

---

## Po co znać `open()`

Bo pozwala:

- czytać dane z pliku,
- zapisywać dane do pliku,
- dopisywać nowe treści,
- pracować z logami, konfiguracją, raportami i eksportami.

---

## Podstawowy zapis i odczyt

Zapis:

```python
with open("plik.txt", "w", encoding="utf-8") as f:
    f.write("Czesc")
```

Odczyt:

```python
with open("plik.txt", "r", encoding="utf-8") as f:
    tekst = f.read()
    print(tekst)
```

Wynik:

```python
Czesc
```

---

## Tryby otwierania plików

Najczęstsze:

- `"r"` odczyt,
- `"w"` zapis od zera,
- `"a"` dopisanie,
- `"x"` utworzenie nowego pliku,
- `"b"` tryb binarny,
- `"t"` tryb tekstowy.

Praktycznie najważniejsze do zapamiętania:

- `"r"` czyta istniejący plik,
- `"w"` tworzy nowy plik albo nadpisuje stary,
- `"a"` dopisuje na końcu,
- `"x"` tworzy plik tylko wtedy, gdy jeszcze go nie ma.

---

## `with open(...)`

To najbezpieczniejszy i najczęstszy wzorzec.

`with` dba o poprawne zamknięcie pliku nawet wtedy, gdy wystąpi błąd.

---

## Odczyt całego pliku vs linie

Cały plik:

```python
tekst = f.read()
```

Linia po linii:

```python
for linia in f:
    print(linia.strip())
```

Drugi wariant bywa lepszy przy większych plikach.

Przykład:

jeśli plik ma zawartość:

```text
Ala
Ola
Jan
```

to pętla wypisze:

```python
Ala
Ola
Jan
```

---

## Dopisanie do pliku

```python
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("Nowa linia\n")
```

To nie nadpisuje starej zawartości.

Jeśli plik wcześniej zawierał:

```text
Start
```

to po dopisaniu może wyglądać tak:

```text
Start
Nowa linia
```

---

## Typowe błędy początkujących

- brak `with`,
- brak `encoding="utf-8"`,
- używanie `"w"` tam, gdzie chodziło o dopisanie,
- czytanie ogromnych plików na raz bez potrzeby.

### 5. Zakładanie, że zapis niczego nie usuwa

Tryb `"w"` nadpisuje plik od zera.

---

## Praktyczne przykłady

### Raport tekstowy

```python
with open("raport.txt", "w", encoding="utf-8") as f:
    f.write("Raport dzienny\n")
```

Efekt w pliku:

```text
Raport dzienny
```

### Odczyt linia po linii

```python
with open("dane.txt", "r", encoding="utf-8") as f:
    for linia in f:
        print(linia.strip())
```

Wynik przykładowy:

```python
pierwsza linia
druga linia
trzecia linia
```

---

## Dobre praktyki

- używaj `with open(...)`,
- jawnie ustawiaj `encoding`,
- wybieraj tryb otwarcia świadomie,
- dla dużych plików preferuj iterację po liniach.

Praktyczna zasada:

jeśli nie masz konkretnego powodu, domyślnie używaj:

```python
with open(..., encoding="utf-8")
```

---

## Podsumowanie

`open()` to absolutna podstawa pracy z danymi w Pythonie.

Profesjonalny kod zwykle używa go razem z `with` i jawnym `encoding`.

Najważniejsze do zapamiętania:

- `with` bezpiecznie zamyka plik,
- tryb otwarcia decyduje, czy czytasz, nadpisujesz czy dopisujesz,
- przy tekstach warto jawnie podać `encoding="utf-8"`.

---

## Mini ściąga

```python
with open("plik.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

Najważniejsze:

- `"r"` czyta,
- `"w"` nadpisuje,
- `"a"` dopisuje,
- `with` bezpiecznie zamyka plik.

---

## Ćwiczenia

1. Zapisz napis do pliku.
2. Odczytaj plik tekstowy.
3. Dopisz linię do istniejącego pliku.
4. Wypisz plik linia po linii.
5. Wyjaśnij, po co używać `with`.

---

## Przykładowe rozwiązania

### 1. Zapis

```python
with open("a.txt", "w", encoding="utf-8") as f:
    f.write("hello")
```

### 2. Odczyt

```python
with open("a.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

### 3. Dopisanie

```python
with open("a.txt", "a", encoding="utf-8") as f:
    f.write("\nnowa linia")
```

### 4. Linie

```python
with open("a.txt", "r", encoding="utf-8") as f:
    for linia in f:
        print(linia.strip())
```

### 5. `with`

Bo automatycznie zamyka plik i jest bezpieczniejszy przy błędach.
