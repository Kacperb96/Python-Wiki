# Kodowanie tekstu w Pythonie — `utf-8`

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co znać kodowanie](#po-co-znać-kodowanie)
3. [Tekst a bajty](#tekst-a-bajty)
4. [Dlaczego `utf-8` jest ważne](#dlaczego-utf-8-jest-ważne)
5. [Kodowanie przy pracy z plikami](#kodowanie-przy-pracy-z-plikami)
6. [Najczęstsze problemy z polskimi znakami](#najczęstsze-problemy-z-polskimi-znakami)
7. [`encode()` i `decode()`](#encode-i-decode)
8. [Typowe błędy początkujących](#typowe-błędy-początkujących)
9. [Praktyczne przykłady](#praktyczne-przykłady)
10. [Dobre praktyki](#dobre-praktyki)
11. [Podsumowanie](#podsumowanie)
12. [Mini ściąga](#mini-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Kodowanie tekstu to temat, który wraca wszędzie tam, gdzie pojawiają się pliki, API i dane tekstowe.

Najważniejsze kodowanie, które warto znać, to `utf-8`.

---

## Po co znać kodowanie

Bo bez tego łatwo o:

- błędne polskie znaki,
- wyjątki przy odczycie plików,
- uszkodzony tekst przy wymianie danych.

---

## Tekst a bajty

To kluczowe rozróżnienie:

- tekst to znaki,
- bajty to surowa reprezentacja danych.

Kodowanie opisuje, jak zamienić jedno w drugie.

---

## Dlaczego `utf-8` jest ważne

`utf-8` jest dziś praktycznym standardem dla ogromnej części świata programistycznego.

Dobrze obsługuje polskie znaki i świetnie sprawdza się w plikach, API i JSON.

---

## Kodowanie przy pracy z plikami

Najbezpieczniej pisać jawnie:

```python
with open("tekst.txt", "r", encoding="utf-8") as f:
    dane = f.read()
```

To zmniejsza ryzyko problemów między różnymi systemami.

To jest dobry domyślny nawyk przy plikach tekstowych.

---

## Najczęstsze problemy z polskimi znakami

Na przykład:

- `Łódź` zapisuje się źle,
- pojawia się `UnicodeDecodeError`,
- pojawiają się "krzaki" w tekście.

To zwykle oznacza problem z kodowaniem lub błędne założenie o nim.

---

## `encode()` i `decode()`

Tekst na bajty:

```python
tekst = "zażółć"
bajty = tekst.encode("utf-8")
```

Wynik przykładowy:

```python
b'za\\xc5\\xbc\\xc3\\xb3\\xc5\\x82\\xc4\\x87'
```

Bajty na tekst:

```python
odzyskany = bajty.decode("utf-8")
```

Po dekodowaniu z powrotem dostajesz zwykły tekst:

```python
zażółć
```

---

## Typowe błędy początkujących

- brak jawnego `encoding`,
- mylenie `str` i `bytes`,
- próba zapisu tekstu do miejsca oczekującego bajtów lub odwrotnie,
- zakładanie, że każdy plik ma `utf-8`, gdy nie wiadomo, skąd pochodzi.

---

## Praktyczne przykłady

### Zapis polskiego tekstu

```python
with open("miasto.txt", "w", encoding="utf-8") as f:
    f.write("Łódź")
```

Po poprawnym odczycie:

```python
Łódź
```

### Konwersja tekstu

```python
tekst = "gęś"
b = tekst.encode("utf-8")
print(b)
print(b.decode("utf-8"))
```

Wynik:

```python
b'g\\xc4\\x99\\xc5\\x9b'
gęś
```

---

## Dobre praktyki

- dla plików tekstowych zwykle ustawiaj `encoding="utf-8"`,
- rozróżniaj `str` i `bytes`,
- przy integracjach z zewnętrznymi systemami sprawdzaj, jakie kodowanie jest używane,
- traktuj błędy kodowania jako ważny sygnał, a nie drobiazg.

Praktyczna zasada:

`str` to to, co chcesz czytać jako tekst.

`bytes` to to, co faktycznie idzie po dysku, sieci albo w pliku binarnym.

---

## Podsumowanie

Zrozumienie `utf-8` i różnicy między tekstem a bajtami jest bardzo ważne w profesjonalnej pracy z Pythonem.

To oszczędza mnóstwo trudnych i irytujących problemów.

Najważniejsze do zapamiętania:

- `encode()` zamienia tekst na bajty,
- `decode()` zamienia bajty na tekst,
- `utf-8` jest najlepszym praktycznym domyślnym wyborem w większości projektów.

---

## Mini ściąga

```python
tekst = "Łódź"
bajty = tekst.encode("utf-8")
odzyskany = bajty.decode("utf-8")
```

Najważniejsze:

- `str` to tekst,
- `bytes` to bajty,
- `utf-8` to najczęstsze praktyczne kodowanie,
- przy plikach warto jawnie podawać `encoding`.

---

## Ćwiczenia

1. Zapisz polski tekst do pliku w `utf-8`.
2. Odczytaj ten plik z jawnym `encoding`.
3. Zamień napis na bajty przez `encode`.
4. Zamień bajty z powrotem na tekst przez `decode`.
5. Wyjaśnij różnicę między `str` a `bytes`.

---

## Przykładowe rozwiązania

### 1. Zapis

```python
with open("polski.txt", "w", encoding="utf-8") as f:
    f.write("zażółć gęślą jaźń")
```

### 2. Odczyt

```python
with open("polski.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

### 3. `encode`

```python
print("Łódź".encode("utf-8"))
```

### 4. `decode`

```python
b = "Łódź".encode("utf-8")
print(b.decode("utf-8"))
```

### 5. Różnica

`str` reprezentuje tekst, a `bytes` surowe dane bajtowe.
