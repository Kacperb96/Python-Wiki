# `re` w Pythonie

## Wprowadzenie

`re` to moduł do pracy z wyrażeniami regularnymi.

Pozwala wyszukiwać, dopasowywać i przekształcać tekst według wzorców. Jest bardzo przydatny przy:

- walidacji,
- parsowaniu tekstu,
- ekstrakcji danych,
- czyszczeniu danych wejściowych.

## Kiedy `re` ma sens

Regex ma sens wtedy, gdy problem dotyczy wzorca tekstowego.

Przykłady:

- format `ABC-123`,
- data `2026-08-15`,
- e-mail w środku tekstu,
- wszystkie liczby w zdaniu,
- zamiana wielu białych znaków na jeden.

## Kiedy `re` nie ma sensu

Nie używaj regexu tylko dlatego, że się da.

Jeśli wystarczy:

- `in`,
- `startswith()`,
- `endswith()`,
- `split()`,
- `replace()`,

to często te rozwiązania będą czytelniejsze.

### Przykład

Zamiast:

```python
import re

text = "abc,def,ghi"
print(re.split(r",", text))
```

często wystarczy:

```python
text = "abc,def,ghi"
print(text.split(","))
```

Output:

```python
['abc', 'def', 'ghi']
```

## Podstawowy import

```python
import re
```

## `search()`, `match()`, `fullmatch()`

### `search()`

Szuka wzorca gdziekolwiek w tekście.

```python
import re

text = "Kontakt: anna@example.com"
result = re.search(r"\S+@\S+\.\S+", text)
print(result.group())
```

Output:

```python
anna@example.com
```

### `match()`

Sprawdza dopasowanie od początku tekstu.

```python
import re

print(re.match(r"abc", "abcdef") is not None)
print(re.match(r"abc", "xxabcdef") is not None)
```

Output:

```python
True
False
```

### `fullmatch()`

Wymaga, żeby cały tekst pasował do wzorca.

```python
import re

print(re.fullmatch(r"\d{3}", "123") is not None)
print(re.fullmatch(r"\d{3}", "1234") is not None)
```

Output:

```python
True
False
```

## `findall()` i `finditer()`

### `findall()`

Zwraca listę dopasowań.

```python
import re

text = "Ala ma 2 koty i 3 psy"
print(re.findall(r"\d+", text))
```

Output:

```python
['2', '3']
```

### `finditer()`

Zwraca iterator po dopasowaniach.

```python
import re

text = "Ala ma 2 koty i 3 psy"
for match in re.finditer(r"\d+", text):
    print(match.group(), match.start())
```

Output:

```python
2 7
3 16
```

## Grupy

Grupy pozwalają wyciągać części dopasowania.

```python
import re

text = "2026-08-15"
match = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", text)
print(match.group(1))
print(match.group(2))
print(match.group(3))
```

Output:

```python
2026
08
15
```

### Grupy nazwane

```python
import re

text = "2026-08-15"
match = re.fullmatch(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", text)
print(match.group("year"))
print(match.group("month"))
print(match.group("day"))
```

## Podstawowe metaznaki

Najczęściej spotkasz:

- `.` dowolny znak,
- `\d` cyfra,
- `\w` znak słowa,
- `\s` biały znak,
- `^` początek,
- `$` koniec.

## Kwantyfikatory

Najważniejsze:

- `*` zero lub więcej,
- `+` jeden lub więcej,
- `?` zero lub jeden,
- `{n}` dokładnie `n`,
- `{n,m}` od `n` do `m`.

## `sub()` i zamiana tekstu

```python
import re

text = "Telefon: 123-456-789"
masked = re.sub(r"\d", "X", text)
print(masked)
```

Output:

```python
Telefon: XXX-XXX-XXX
```

## Raw stringi

Regex prawie zawsze zapisuj jako raw string.

```python
r"\d+"
```

Zamiast:

```python
"\\d+"
```

## Regex vs zwykły kod

### Gdy regex wygrywa

```python
import re

text = "ID: 12, 45, 78"
print(re.findall(r"\d+", text))
```

Tu regex jest naturalny.

### Gdy prostszy kod wygrywa

```python
text = "Python jest super"
print(text.startswith("Python"))
```

Pisanie regexu do takiego zadania byłoby przesadą.

## Typowe błędy początkujących

- używanie `match()` tam, gdzie potrzebne jest `search()`,
- brak `r"..."` przy wzorcu,
- tworzenie zbyt skomplikowanych regexów na start,
- używanie regexu do najprostszych operacji tekstowych,
- brak sprawdzenia, czy dopasowanie w ogóle istnieje przed `group()`.

## Mini scenariusz praktyczny

Masz logi w postaci:

```text
2026-08-15 INFO User logged in
2026-08-15 ERROR Invalid password
```

Regex pomaga wyciągnąć:

- datę,
- poziom logowania,
- komunikat.

To jest bardzo sensowne użycie, bo dane mają wyraźny wzorzec.

## Dobre praktyki

- używaj regexu do wzorców, nie do wszystkiego,
- zaczynaj od prostych wyrażeń,
- testuj na kilku wejściach,
- rozważ grupy nazwane, gdy wzorzec rośnie,
- jeśli prostszy kod jest czytelniejszy, wybierz prostszy kod.

## Szybka ściąga

Najczęściej używane:

- `search()` — szuka gdziekolwiek,
- `fullmatch()` — dopasowuje cały tekst,
- `findall()` — zwraca listę dopasowań,
- `finditer()` — zwraca iterator dopasowań,
- `sub()` — zamienia fragmenty tekstu.

## Ćwiczenia

1. Znajdź wszystkie liczby w tekście.
2. Wyciągnij e-mail z dłuższego zdania.
3. Sprawdź, czy string ma format `ABC-123`.
4. Zamień wiele spacji na jedną.
5. Porównaj regex i `split()` dla prostego dzielenia po przecinku.

## Najważniejsze do zapamiętania

- `re` jest świetne do wzorców tekstowych.
- Nie każde zadanie tekstowe wymaga regexu.
- `search()`, `match()` i `fullmatch()` robią różne rzeczy.
- `findall()` i `finditer()` są bardzo praktyczne.
- Dobry regex upraszcza kod, zły regex go zaciemnia.
