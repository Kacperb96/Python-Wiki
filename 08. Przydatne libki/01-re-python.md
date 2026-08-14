# `re` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co używać wyrażeń regularnych](#po-co-używać-wyrażeń-regularnych)
3. [Czym jest `re`](#czym-jest-re)
4. [`search()`, `match()`, `fullmatch()`](#search-match-fullmatch)
5. [`findall()` i `finditer()`](#findall-i-finditer)
6. [Grupy](#grupy)
7. [Podstawowe metaznaki](#podstawowe-metaznaki)
8. [Kwantyfikatory](#kwantyfikatory)
9. [`sub()` i zamiana tekstu](#sub-i-zamiana-tekstu)
10. [Raw stringi](#raw-stringi)
11. [Typowe błędy początkujących](#typowe-błędy-początkujących)
12. [Praktyczne przykłady](#praktyczne-przykłady)
13. [Dobre praktyki](#dobre-praktyki)
14. [Podsumowanie](#podsumowanie)
15. [Mini ściąga](#mini-ściąga)
16. [Ćwiczenia](#ćwiczenia)
17. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`re` to moduł do pracy z wyrażeniami regularnymi.

Pozwala wyszukiwać, dopasowywać i przekształcać tekst według wzorców.

Jest bardzo przydatny przy:

- walidacji,
- parsowaniu tekstu,
- ekstrakcji danych,
- czyszczeniu danych wejściowych.

---

## Po co używać wyrażeń regularnych

Gdy zwykłe `in`, `split()` lub `replace()` przestają wystarczać.

Regex pozwala opisać wzorzec, np.:

- adres e-mail,
- numer telefonu,
- kod pocztowy,
- liczby w tekście.

---

## Czym jest `re`

Podstawowy import:

```python
import re
```

Prosty przykład:

```python
tekst = "Kontakt: anna@example.com"
wynik = re.search(r"\S+@\S+\.\S+", tekst)
print(wynik.group())
```

---

## `search()`, `match()`, `fullmatch()`

`search()`:

- szuka wzorca gdziekolwiek w tekście.

`match()`:

- sprawdza początek tekstu.

`fullmatch()`:

- wymaga, żeby cały tekst pasował do wzorca.

To bardzo ważna różnica praktyczna.

---

## `findall()` i `finditer()`

`findall()` zwraca listę dopasowań:

```python
import re

tekst = "Ala ma 2 koty i 3 psy"
print(re.findall(r"\d+", tekst))
```

`finditer()` zwraca iterator po dopasowaniach:

```python
for m in re.finditer(r"\d+", tekst):
    print(m.group(), m.start())
```

---

## Grupy

Grupy pozwalają wyodrębnić części dopasowania.

```python
import re

tekst = "2026-07-25"
m = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", tekst)

print(m.group(1))
print(m.group(2))
print(m.group(3))
```

---

## Podstawowe metaznaki

Najczęstsze:

- `.` dowolny znak,
- `\d` cyfra,
- `\w` znak słowa,
- `\s` biały znak,
- `^` początek,
- `$` koniec.

To rdzeń wielu praktycznych wzorców.

---

## Kwantyfikatory

Najważniejsze:

- `*` zero lub więcej,
- `+` jeden lub więcej,
- `?` zero lub jeden,
- `{n}` dokładnie `n`,
- `{n,m}` od `n` do `m`.

---

## `sub()` i zamiana tekstu

```python
import re

tekst = "Telefon: 123-456-789"
nowy = re.sub(r"\d", "X", tekst)
print(nowy)
```

Przydaje się do maskowania danych i czyszczenia tekstu.

---

## Raw stringi

Regex prawie zawsze zapisuj jako raw string:

```python
r"\d+"
```

Zamiast:

```python
"\\d+"
```

To dużo czytelniejsze.

---

## Typowe błędy początkujących

- używanie `match()` tam, gdzie potrzebne jest `search()`,
- brak raw stringów,
- zbyt skomplikowane regexy na start,
- brak sprawdzenia, czy dopasowanie istnieje przed `group()`.

---

## Praktyczne przykłady

### Wyciąganie liczb z tekstu

```python
import re

tekst = "Produkty: 12 jabłek, 7 gruszek"
print(re.findall(r"\d+", tekst))
```

### Walidacja prostego kodu

```python
import re

kod = "ABC-123"

if re.fullmatch(r"[A-Z]{3}-\d{3}", kod):
    print("OK")
```

---

## Dobre praktyki

- zaczynaj od prostych wzorców,
- używaj `fullmatch()` do walidacji całego tekstu,
- zapisuj wzorce jako raw stringi,
- przy często używanych wzorcach rozważ `re.compile()`.

---

## Podsumowanie

`re` to bardzo mocne narzędzie do pracy z tekstem.

Nie zawsze jest najlepszym wyborem, ale tam, gdzie trzeba opisać wzorzec tekstowy, bywa niezastąpione.

---

## Mini ściąga

```python
import re

print(re.search(r"\d+", "abc123").group())
print(re.findall(r"\d+", "a1 b22 c333"))
```

Najważniejsze:

- `search()` szuka w całym tekście,
- `match()` sprawdza początek,
- `fullmatch()` sprawdza całość,
- `findall()` zwraca listę,
- `sub()` zamienia tekst według wzorca.

---

## Ćwiczenia

1. Znajdź pierwszą liczbę w tekście.
2. Wyciągnij wszystkie adresy e-mail z krótkiego tekstu.
3. Sprawdź, czy napis ma format `ABC-123`.
4. Zamień wszystkie cyfry na `*`.
5. Wyciągnij rok, miesiąc i dzień z daty `2026-07-25`.

---

## Przykładowe rozwiązania

### 1. Pierwsza liczba

```python
import re

tekst = "Mam 42 pomysly"
m = re.search(r"\d+", tekst)
print(m.group())
```

### 2. E-maile

```python
import re

tekst = "Napisz na anna@example.com lub jan@test.pl"
print(re.findall(r"\S+@\S+\.\S+", tekst))
```

### 3. Format kodu

```python
import re

print(bool(re.fullmatch(r"[A-Z]{3}-\d{3}", "ABC-123")))
```

### 4. Maskowanie cyfr

```python
import re

print(re.sub(r"\d", "*", "PIN 1234"))
```

### 5. Data

```python
import re

m = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", "2026-07-25")
print(m.groups())
```
