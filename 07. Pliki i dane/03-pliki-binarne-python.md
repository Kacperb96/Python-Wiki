# Pliki binarne w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Tekst vs dane binarne](#tekst-vs-dane-binarne)
3. [Tryb binarny `b`](#tryb-binarny-b)
4. [Odczyt pliku binarnego](#odczyt-pliku-binarnego)
5. [Zapis pliku binarnego](#zapis-pliku-binarnego)
6. [Kiedy używa się plików binarnych](#kiedy-używa-się-plików-binarnych)
7. [`bytes`](#bytes)
8. [Typowe błędy początkujących](#typowe-błędy-początkujących)
9. [Praktyczne przykłady](#praktyczne-przykłady)
10. [Dobre praktyki](#dobre-praktyki)
11. [Podsumowanie](#podsumowanie)
12. [Mini ściąga](#mini-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Nie każdy plik jest tekstem.

Obrazy, PDF-y, archiwa czy surowe dane bajtowe to przykłady plików binarnych.

---

## Tekst vs dane binarne

Tekst:

- pracujesz na `str`,
- ma znaczenie kodowanie, np. `utf-8`.

Dane binarne:

- pracujesz na `bytes`,
- nie interpretujesz danych jako tekstu.

---

## Tryb binarny `b`

Przy `open()` używasz trybu binarnego:

- `"rb"` do odczytu,
- `"wb"` do zapisu,
- `"ab"` do dopisywania.

---

## Odczyt pliku binarnego

```python
with open("obraz.png", "rb") as f:
    dane = f.read()
    print(type(dane))
```

Wynik będzie typu `bytes`.

---

## Zapis pliku binarnego

```python
dane = b"\x00\x01\x02"

with open("out.bin", "wb") as f:
    f.write(dane)
```

---

## Kiedy używa się plików binarnych

Najczęściej przy:

- obrazach,
- PDF-ach,
- plikach audio,
- archiwach,
- przesyłaniu surowych danych.

---

## `bytes`

To typ reprezentujący dane bajtowe.

Przykład:

```python
dane = b"ABC"
print(dane[0])
```

---

## Typowe błędy początkujących

- próba czytania pliku binarnego jak tekstu,
- mylenie `str` i `bytes`,
- używanie `encoding` przy trybie binarnym,
- traktowanie każdego pliku jak tekstu.

---

## Praktyczne przykłady

### Kopiowanie pliku binarnego

```python
with open("wejscie.bin", "rb") as src:
    dane = src.read()

with open("wyjscie.bin", "wb") as dst:
    dst.write(dane)
```

### Prosty zapis bajtów

```python
with open("liczby.bin", "wb") as f:
    f.write(b"\x01\x02\x03")
```

---

## Dobre praktyki

- dla plików binarnych używaj `rb` i `wb`,
- odróżniaj `bytes` od `str`,
- nie próbuj interpretować danych jako tekstu bez potrzeby,
- przy większych plikach rozważ czytanie kawałkami.

---

## Podsumowanie

Pliki binarne to ważna część praktycznej pracy z danymi.

Profesjonalny Python wymaga swobodnego rozróżniania pracy z tekstem i z bajtami.

---

## Mini ściąga

```python
with open("plik.bin", "rb") as f:
    dane = f.read()
```

Najważniejsze:

- `"rb"` czyta binarnie,
- `"wb"` zapisuje binarnie,
- wynik to zwykle `bytes`,
- tekst i bajty to różne światy.

---

## Ćwiczenia

1. Odczytaj plik binarny.
2. Zapisz kilka bajtów do pliku.
3. Skopiuj plik binarny.
4. Wyjaśnij różnicę między `str` a `bytes`.
5. Wyjaśnij, czemu `encoding` nie jest używane przy `rb`.

---

## Przykładowe rozwiązania

### 1. Odczyt

```python
with open("a.bin", "rb") as f:
    print(f.read())
```

### 2. Zapis

```python
with open("a.bin", "wb") as f:
    f.write(b"\x10\x20")
```

### 3. Kopia

```python
with open("a.bin", "rb") as src, open("b.bin", "wb") as dst:
    dst.write(src.read())
```

### 4. Różnica

`str` reprezentuje tekst, a `bytes` surowe dane bajtowe.

### 5. Czemu bez `encoding`

Bo w trybie binarnym nie pracujesz na tekście, tylko na bajtach.
