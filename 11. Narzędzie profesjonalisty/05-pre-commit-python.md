# `pre-commit` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `pre-commit`](#czym-jest-pre-commit)
3. [Po co używać hooków przed commitem](#po-co-używać-hooków-przed-commitem)
4. [Jakie narzędzia warto podpiąć](#jakie-narzędzia-warto-podpiąć)
5. [Przykładowa konfiguracja](#przykładowa-konfiguracja)
6. [Korzyści w pracy zespołowej](#korzyści-w-pracy-zespołowej)
7. [Typowe błędy początkujących](#typowe-błędy-początkujących)
8. [Praktyczne przykłady](#praktyczne-przykłady)
9. [Dobre praktyki](#dobre-praktyki)
10. [Podsumowanie](#podsumowanie)
11. [Mini ściąga](#mini-ściąga)
12. [Ćwiczenia](#ćwiczenia)
13. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`pre-commit` to narzędzie, które uruchamia wybrane checki automatycznie przed wykonaniem commita.

Dzięki temu wiele drobnych problemów zatrzymujesz jeszcze zanim trafią do repozytorium.

---

## Czym jest `pre-commit`

To menedżer hooków Git.

Pozwala odpalać na przykład:

- `ruff`,
- `black`,
- `mypy`,
- sprawdzenie końcowych spacji,
- sprawdzenie końca pliku nową linią.

---

## Po co używać hooków przed commitem

Bo pomagają:

- wymuszać standard jakości,
- oszczędzać czas reviewerów,
- zmniejszać liczbę drobnych poprawek po pushu,
- budować powtarzalny workflow.

---

## Jakie narzędzia warto podpiąć

Na start zwykle sensowne są:

- `ruff`,
- `black`,
- proste hooki tekstowe,
- czasem `mypy`.

Nie zawsze warto od razu podpinać bardzo ciężkie checki do każdego commita, jeśli dramatycznie spowalniają pracę.

---

## Przykładowa konfiguracja

Najczęściej tworzy się plik `.pre-commit-config.yaml`.

Przykład:

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.6.9
    hooks:
      - id: ruff
      - id: ruff-format

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: end-of-file-fixer
      - id: trailing-whitespace
```

---

## Korzyści w pracy zespołowej

`pre-commit` sprawia, że standard jest bardziej automatyczny niż umowny.

Zespół nie musi wciąż przypominać:

- "usuń spacje",
- "napraw importy",
- "sformatuj plik".

To robi narzędzie.

---

## Typowe błędy początkujących

- brak hooków mimo używania linterów i formatterów,
- podpinanie zbyt wielu ciężkich testów do każdego commita,
- ignorowanie błędów hooków zamiast poprawienia kodu,
- brak wersjonowania konfiguracji w repo.

---

## Praktyczne przykłady

### Minimalny zestaw

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.6.9
    hooks:
      - id: ruff

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: trailing-whitespace
```

### Rozsądny zestaw dla małego projektu

- `ruff`
- `ruff-format` lub formatter
- `end-of-file-fixer`
- `trailing-whitespace`

---

## Dobre praktyki

- zacznij od lekkich i naprawdę użytecznych hooków,
- trzymaj konfigurację w repo,
- dbaj, aby hooki były szybkie,
- używaj `pre-commit` razem z CI, a nie zamiast CI.

---

## Podsumowanie

`pre-commit` to małe narzędzie, które daje bardzo duży efekt organizacyjny i jakościowy.

W profesjonalnych projektach jest często jedną z najtańszych i najbardziej opłacalnych automatyzacji.

---

## Mini ściąga

Przykład:

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.6.9
    hooks:
      - id: ruff
```

Najważniejsze:

- `pre-commit` odpala checki przed commitem,
- pomaga utrzymać standard,
- najlepiej zacząć od małej konfiguracji.

---

## Ćwiczenia

1. Wyjaśnij, po co zespołowi `pre-commit`.
2. Wypisz 2-3 hooki, które warto włączyć na start.
3. Napisz minimalny `.pre-commit-config.yaml` z `ruff`.
4. Wyjaśnij, czemu nie każdy test warto odpalać przed każdym commitem.
5. Wyjaśnij różnicę między `pre-commit` a CI.

---

## Przykładowe rozwiązania

### 1. Po co zespołowi

Żeby automatycznie wychwytywać drobne problemy przed commitem i utrzymać spójny standard.

### 2. Hooki startowe

- `ruff`
- `trailing-whitespace`
- `end-of-file-fixer`

### 3. Minimalna konfiguracja

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.6.9
    hooks:
      - id: ruff
```

### 4. Czemu nie wszystko

Bo zbyt ciężkie hooki mogą mocno spowolnić codzienną pracę.

### 5. `pre-commit` vs CI

`pre-commit` działa lokalnie przed commitem, a CI działa na serwerze lub platformie po pushu lub pull requeście.
