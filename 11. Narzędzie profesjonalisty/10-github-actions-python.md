# GitHub Actions dla projektów Python

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest CI](#czym-jest-ci)
3. [Po co Pythonowcowi GitHub Actions](#po-co-pythonowcowi-github-actions)
4. [Co zwykle uruchamia pipeline](#co-zwykle-uruchamia-pipeline)
5. [Podstawowa struktura workflow](#podstawowa-struktura-workflow)
6. [Najczęstsze checki](#najczęstsze-checki)
7. [Korzyści zawodowe](#korzyści-zawodowe)
8. [Typowe błędy początkujących](#typowe-błędy-początkujących)
9. [Praktyczne przykłady](#praktyczne-przykłady)
10. [Dobre praktyki](#dobre-praktyki)
11. [Podsumowanie](#podsumowanie)
12. [Mini ściąga](#mini-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

GitHub Actions to popularne narzędzie CI/CD.

W projektach Python najczęściej używa się go do automatycznego uruchamiania testów i kontroli jakości po pushu lub pull requeście.

---

## Czym jest CI

CI, czyli Continuous Integration, to automatyczne sprawdzanie projektu po zmianach w kodzie.

Najczęściej obejmuje:

- instalację zależności,
- linting,
- type checking,
- testy.

---

## Po co Pythonowcowi GitHub Actions

Bo pomaga:

- szybko wykrywać regresje,
- utrzymać standard jakości,
- automatyzować rutynowe checki,
- pracować zespołowo bez zgadywania, czy projekt przechodzi testy.

---

## Co zwykle uruchamia pipeline

Najczęściej:

- `ruff`,
- `mypy`,
- `pytest`,
- czasem coverage.

To bardzo sensowny minimalny zestaw.

---

## Podstawowa struktura workflow

Workflow opisuje się w pliku YAML.

Typowe elementy:

- `name`
- `on`
- `jobs`
- `steps`

---

## Najczęstsze checki

W projekcie Python zwykle chcesz:

- sprawdzić jakość kodu,
- odpalić testy,
- sprawdzić typy,
- upewnić się, że projekt buduje się poprawnie.

---

## Korzyści zawodowe

To ważne, bo profesjonalny projekt powinien sam potwierdzać podstawową jakość po zmianach.

To zmniejsza ryzyko:

- zepsutego maina,
- nieprzechodzących testów,
- błędów wykrywanych zbyt późno.

---

## Typowe błędy początkujących

- brak CI mimo pracy zespołowej,
- odpalanie tylko testów bez lintingu i typów,
- zbyt skomplikowany pipeline na start,
- ignorowanie czerwonych buildów.

---

## Praktyczne przykłady

### Minimalny workflow

```yaml
name: Python CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: pytest
```

### Lepszy kierunek

- `ruff`
- `mypy`
- `pytest`

---

## Dobre praktyki

- zacznij od prostego pipeline,
- uruchamiaj tylko najważniejsze checki,
- trzymaj CI spójne z lokalnym workflow,
- traktuj czerwony pipeline poważnie.

---

## Podsumowanie

GitHub Actions to ważny element profesjonalnego workflow Python.

Nie chodzi o samą platformę, tylko o nawyk automatycznej weryfikacji jakości projektu.

---

## Mini ściąga

Najważniejsze:

- CI sprawdza projekt po zmianach,
- GitHub Actions to popularne narzędzie CI,
- w Pythonie zwykle odpalasz `ruff`, `mypy`, `pytest`.

---

## Ćwiczenia

1. Wyjaśnij, czym jest CI.
2. Wypisz 3 checki, które warto odpalać dla projektu Python.
3. Napisz minimalny workflow z testami.
4. Wyjaśnij, czemu czerwony build jest ważnym sygnałem.
5. Wyjaśnij, czemu warto mieć zgodność między lokalnym workflow a CI.

---

## Przykładowe rozwiązania

### 1. CI

To automatyczne sprawdzanie jakości projektu po zmianach w kodzie.

### 2. 3 checki

- `ruff`
- `mypy`
- `pytest`

### 3. Minimalny workflow

```yaml
name: Python CI
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
```

### 4. Czerwony build

Sygnalizuje, że projekt po zmianie nie przechodzi ustalonych checków.

### 5. Zgodność

Bo wtedy to, co działa lokalnie, ma dużą szansę działać też w pipeline.
