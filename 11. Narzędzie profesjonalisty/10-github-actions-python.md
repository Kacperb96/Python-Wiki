# GitHub Actions dla projektów Python

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest CI](#czym-jest-ci)
3. [Po co Pythonowcowi GitHub Actions](#po-co-pythonowcowi-github-actions)
4. [Co zwykle uruchamia pipeline](#co-zwykle-uruchamia-pipeline)
5. [Podstawowa struktura workflow](#podstawowa-struktura-workflow)
6. [Minimalny workflow](#minimalny-workflow)
7. [Jak czytać taki plik](#jak-czytać-taki-plik)
8. [Przykładowy output i sens czerwonego buildu](#przykładowy-output-i-sens-czerwonego-buildu)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczna ściąga](#praktyczna-ściąga)
11. [Ćwiczenia](#ćwiczenia)
12. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

GitHub Actions to popularne narzędzie CI/CD.

W projektach Python najczęściej używa się go do automatycznego uruchamiania testów i kontroli jakości po pushu albo pull requeście.

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
- mieć pewność, że projekt przechodzi podstawową weryfikację poza lokalną maszyną.

---

## Co zwykle uruchamia pipeline

W projekcie Python bardzo często chcesz w CI uruchamiać:

- `ruff`,
- `mypy`,
- `pytest`,
- czasem coverage.

To sensowny minimalny zestaw dla wielu repozytoriów.

---

## Podstawowa struktura workflow

Workflow opisuje się w YAML-u.

Typowe elementy:

- `name`,
- `on`,
- `jobs`,
- `steps`.

To jest szkielet, który będziesz widzieć praktycznie zawsze.

---

## Minimalny workflow

```yaml
name: Python CI

on: [push, pull_request]

jobs:
  checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt
      - run: pytest
```

To najprostszy punkt wejścia.

Rozsądny kierunek rozbudowy:

- dodać `ruff`,
- dodać `mypy`,
- zadbać o spójność z lokalnym workflow.

---

## Jak czytać taki plik

Patrz po kolei:

1. kiedy workflow się uruchamia,
2. jakie joby istnieją,
3. jaka wersja Pythona jest używana,
4. jak instalowane są zależności,
5. jakie checki są naprawdę odpalane.

To pozwala szybko ocenić dojrzałość projektu.

---

## Przykładowy output i sens czerwonego buildu

W praktyce najważniejszy jest nie sam YAML, tylko to, że pipeline daje prosty sygnał:

- zielono: podstawowe checki przeszły,
- czerwono: coś wymaga poprawy.

Czerwony build nie jest ozdobą.

To znak, że projekt przestał spełniać ustalone warunki jakości.

Dlatego powinno się go traktować poważnie.

---

## Typowe błędy początkujących

- brak CI mimo pracy zespołowej,
- odpalanie tylko testów bez lintingu i typów,
- zbyt skomplikowany pipeline na start,
- brak zgodności między tym, co działa lokalnie, a tym, co robi CI,
- ignorowanie czerwonych buildów.

---

## Praktyczna ściąga

### Minimalny sensowny zestaw

- checkout repo,
- setup Pythona,
- instalacja zależności,
- `ruff`,
- `mypy`,
- `pytest`.

### O czym pamiętać

- CI ma odtwarzać realny workflow projektu,
- nie powinno być całkowicie oderwane od pracy lokalnej,
- im prostszy start, tym lepiej.

---

## Ćwiczenia

1. Napisz minimalny workflow GitHub Actions dla projektu Python.
2. Dodaj `ruff` do pipeline.
3. Dodaj `mypy` do pipeline.
4. Wyjaśnij, po co CI uruchamia się na `push` i `pull_request`.
5. Opisz, czemu czerwony build powinien blokować dalszą pracę nad zmianą.

---

## Najważniejsze do zapamiętania

- GitHub Actions automatyzuje sprawdzanie jakości projektu.
- W Pythonie najczęściej odpala testy, linting i type checking.
- CI powinno być spójne z lokalnym workflow.
- Prosty pipeline jest lepszy niż przesadnie skomplikowany od pierwszego dnia.
