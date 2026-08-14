# `ruff` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `ruff`](#czym-jest-ruff)
3. [Po co używać `ruff`](#po-co-używać-ruff)
4. [Linting](#linting)
5. [Autofix](#autofix)
6. [Konfiguracja w `pyproject.toml`](#konfiguracja-w-pyprojecttoml)
7. [Praca lokalna i w CI](#praca-lokalna-i-w-ci)
8. [Typowe błędy początkujących](#typowe-błędy-początkujących)
9. [Praktyczne przykłady](#praktyczne-przykłady)
10. [Dobre praktyki](#dobre-praktyki)
11. [Podsumowanie](#podsumowanie)
12. [Mini ściąga](#mini-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`ruff` to bardzo szybkie narzędzie do lintingu i częściowo także autofixów w Pythonie.

W nowoczesnych projektach jest dziś jednym z najważniejszych elementów jakości kodu.

---

## Czym jest `ruff`

`ruff` analizuje kod i wykrywa problemy takie jak:

- nieużywane importy,
- nieużywane zmienne,
- część błędów stylistycznych,
- wybrane potencjalne bugi,
- niespójności formatowania i jakości kodu.

---

## Po co używać `ruff`

Bo pomaga:

- szybciej wyłapywać błędy,
- utrzymywać spójny standard,
- odciążyć code review z drobiazgów,
- automatyzować część poprawek.

---

## Linting

Linting to statyczna analiza kodu pod kątem jakości i błędów.

Przykład mentalny:

- interpreter często wykrywa błąd dopiero przy uruchomieniu,
- linter może wskazać problem wcześniej.

---

## Autofix

`ruff` potrafi część rzeczy poprawić automatycznie.

To bardzo przydatne dla:

- importów,
- części prostych wykroczeń jakościowych,
- porządkowania drobnych rzeczy.

---

## Konfiguracja w `pyproject.toml`

Przykład:

```toml
[tool.ruff]
line-length = 88

[tool.ruff.lint]
select = ["E", "F", "I"]
```

To oznacza zwykle:

- `E` i `F` dla typowych problemów stylu i błędów,
- `I` dla importów.

---

## Praca lokalna i w CI

`ruff` warto uruchamiać:

- lokalnie przed commitem,
- w `pre-commit`,
- w CI.

Dzięki temu standard jakości jest stale pilnowany.

---

## Typowe błędy początkujących

- uruchamianie lintera dopiero na końcu projektu,
- ignorowanie wszystkich ostrzeżeń bez zrozumienia,
- kopiowanie ogromnej konfiguracji bez potrzeby,
- traktowanie lintingu jako czystej kosmetyki.

---

## Praktyczne przykłady

### Prosta konfiguracja

```toml
[tool.ruff]
line-length = 100

[tool.ruff.lint]
select = ["E", "F", "I"]
```

### Przykład problemu

```python
import os

def hello():
    x = 123
    return "ok"
```

`ruff` prawdopodobnie zgłosi:

- nieużywany import,
- nieużywaną zmienną.

---

## Dobre praktyki

- zacznij od małej, zrozumiałej konfiguracji,
- odpalaj `ruff` często,
- włącz go do `pre-commit`,
- poprawiaj realne problemy, a nie tylko wygładzaj licznik ostrzeżeń.

---

## Podsumowanie

`ruff` to jedno z najważniejszych narzędzi profesjonalnego workflow w Pythonie.

Jest szybki, praktyczny i bardzo dobrze podnosi jakość kodu w codziennej pracy.

---

## Mini ściąga

Przykładowa konfiguracja:

```toml
[tool.ruff]
line-length = 88

[tool.ruff.lint]
select = ["E", "F", "I"]
```

Najważniejsze:

- `ruff` lintuje kod,
- pomaga wyłapać błędy wcześniej,
- część problemów umie poprawić sam,
- najlepiej działa jako element codziennego workflow.

---

## Ćwiczenia

1. Dodaj konfigurację `ruff` do `pyproject.toml`.
2. Wskaż przykład nieużywanego importu.
3. Wskaż przykład nieużywanej zmiennej.
4. Wyjaśnij, dlaczego warto uruchamiać linter przed commitem.
5. Podaj 2-3 rodziny reguł, które warto włączyć na start.

---

## Przykładowe rozwiązania

### 1. Konfiguracja

```toml
[tool.ruff]
line-length = 88

[tool.ruff.lint]
select = ["E", "F", "I"]
```

### 2. Nieużywany import

```python
import json

print("hello")
```

### 3. Nieużywana zmienna

```python
def f():
    x = 10
    return 1
```

### 4. Po co przed commitem

Bo łatwiej poprawić małe problemy od razu niż zbierać je przez tygodnie.

### 5. Startowe reguły

- `E`
- `F`
- `I`
