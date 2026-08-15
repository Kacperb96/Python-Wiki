# `ruff` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `ruff`](#czym-jest-ruff)
3. [Po co używać `ruff`](#po-co-używać-ruff)
4. [Linting](#linting)
5. [Autofix](#autofix)
6. [Podstawowe komendy](#podstawowe-komendy)
7. [Przykładowy output](#przykładowy-output)
8. [Konfiguracja w `pyproject.toml`](#konfiguracja-w-pyprojecttoml)
9. [Jak używać `ruff` z innymi narzędziami](#jak-używać-ruff-z-innymi-narzędziami)
10. [Typowe błędy początkujących](#typowe-błędy-początkujących)
11. [Praktyczna ściąga](#praktyczna-ściąga)
12. [Ćwiczenia](#ćwiczenia)
13. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

`ruff` to bardzo szybkie narzędzie do lintingu Pythona.

W nowoczesnych projektach jest jednym z najważniejszych elementów codziennego workflow jakościowego.

Pomaga łapać problemy wcześniej, zanim kod trafi do review albo CI.

---

## Czym jest `ruff`

`ruff` analizuje kod statycznie i wykrywa między innymi:

- nieużywane importy,
- nieużywane zmienne,
- część błędów jakościowych,
- wybrane potencjalne bugi,
- problemy z układem importów.

To nie jest formatter w klasycznym sensie `black`, ale potrafi też część rzeczy automatycznie poprawić.

---

## Po co używać `ruff`

Bo pomaga:

- szybciej zauważać błędy,
- odciążać code review z drobiazgów,
- utrzymywać spójność jakości,
- automatyzować część prostych poprawek,
- trzymać standard projektu lokalnie i w CI.

---

## Linting

Linting to statyczna analiza kodu.

Najprościej:

narzędzie patrzy na kod bez jego uruchamiania i próbuje wskazać problemy.

To ważne, bo część rzeczy możesz wykryć:

- wcześniej niż przy uruchomieniu,
- wcześniej niż w testach,
- zanim ktoś inny zobaczy to w pull requeście.

---

## Autofix

`ruff` potrafi część problemów naprawić automatycznie.

To bardzo wygodne przy takich rzeczach jak:

- niektóre importy,
- proste porządki w kodzie,
- część drobnych naruszeń reguł.

Automatyczne poprawki nie zwalniają z myślenia, ale oszczędzają dużo czasu.

---

## Podstawowe komendy

Sprawdzenie projektu:

```bash
ruff check .
```

Sprawdzenie i automatyczna próba naprawy:

```bash
ruff check . --fix
```

Jeśli projekt używa osobnego formatowania Ruff:

```bash
ruff format .
```

To są najczęstsze komendy, które zobaczysz w realnych repozytoriach.

---

## Przykładowy output

Kod:

```python
import os


def hello():
    x = 123
    return "ok"
```

Przykładowy output `ruff check .`:

```text
F401 [*] `os` imported but unused
 --> app.py:1:8
  |
1 | import os
  |        ^^

F841 Local variable `x` is assigned to but never used
 --> app.py:5:5
  |
5 |     x = 123
  |     ^

Found 2 errors.
[*] 1 fixable with the `--fix` option.
```

Jak to czytać:

- `F401` mówi o nieużywanym imporcie,
- `F841` mówi o nieużywanej zmiennej lokalnej,
- część problemów może być naprawiona automatycznie.

---

## Konfiguracja w `pyproject.toml`

Przykład prosty i sensowny na start:

```toml
[tool.ruff]
line-length = 88

[tool.ruff.lint]
select = ["E", "F", "I"]
```

Najprostsza interpretacja:

- `E` i `F` obejmują podstawowe problemy jakościowe,
- `I` obejmuje importy,
- `line-length` ustawia wspólną szerokość linii.

Na początku lepiej mieć małą i zrozumiałą konfigurację niż wielką listę reguł skopiowaną bez sensu.

---

## Jak używać `ruff` z innymi narzędziami

Najczęściej `ruff` działa razem z:

- `black` albo `ruff format`,
- `mypy`,
- `pytest`,
- `pre-commit`,
- CI.

Przykładowy zdrowy workflow:

1. piszesz kod,
2. odpalasz `ruff check . --fix`,
3. odpalasz formatter,
4. odpalasz testy,
5. commitujesz zmiany.

---

## Typowe błędy początkujących

- uruchamianie lintera dopiero na końcu projektu,
- ignorowanie wszystkich ostrzeżeń bez zrozumienia,
- kopiowanie ogromnej konfiguracji z internetu,
- traktowanie lintingu jako czystej kosmetyki,
- próba włączenia naraz wszystkiego bez oswojenia podstawowych reguł.

---

## Praktyczna ściąga

### Sprawdzenie projektu

```bash
ruff check .
```

### Autofix

```bash
ruff check . --fix
```

### Prosta konfiguracja

```toml
[tool.ruff]
line-length = 88

[tool.ruff.lint]
select = ["E", "F", "I"]
```

---

## Ćwiczenia

1. Przygotuj plik z nieużywanym importem i zobacz raport `ruff`.
2. Dodaj nieużywaną zmienną i sprawdź, czy zostanie zgłoszona.
3. Uruchom `ruff check . --fix` i zobacz, co narzędzie poprawi samo.
4. Dodaj minimalną konfigurację `ruff` do `pyproject.toml`.
5. Wyjaśnij własnymi słowami, czym różni się linting od testów.

---

## Najważniejsze do zapamiętania

- `ruff` bardzo szybko wykrywa wiele codziennych problemów jakościowych.
- Linting działa statycznie, bez uruchamiania programu.
- Część problemów `ruff` potrafi naprawić sam.
- Najlepiej używać go lokalnie, w `pre-commit` i w CI.
- Zacznij od małej, zrozumiałej konfiguracji.
