# `pre-commit` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `pre-commit`](#czym-jest-pre-commit)
3. [Po co używać hooków przed commitem](#po-co-używać-hooków-przed-commitem)
4. [Jakie narzędzia warto podpiąć](#jakie-narzędzia-warto-podpiąć)
5. [Przykładowa konfiguracja](#przykładowa-konfiguracja)
6. [Jak działa ten workflow w praktyce](#jak-działa-ten-workflow-w-praktyce)
7. [Przykładowy output](#przykładowy-output)
8. [Korzyści w pracy zespołowej](#korzyści-w-pracy-zespołowej)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczna ściąga](#praktyczna-ściąga)
11. [Ćwiczenia](#ćwiczenia)
12. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

`pre-commit` to narzędzie, które uruchamia wybrane checki automatycznie przed wykonaniem commita.

Dzięki temu wiele drobnych problemów zatrzymujesz jeszcze zanim trafią do repozytorium.

---

## Czym jest `pre-commit`

To menedżer hooków Git.

Pozwala odpalać na przykład:

- `ruff`,
- formatter,
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

To jedna z najtańszych automatyzacji, które dają bardzo duży efekt.

---

## Jakie narzędzia warto podpiąć

Na start zwykle wystarczą:

- `ruff`,
- formatter,
- `trailing-whitespace`,
- `end-of-file-fixer`.

Czasem warto dodać też `mypy`, ale nie zawsze na sam początek, jeśli ma mocno spowalniać workflow.

---

## Przykładowa konfiguracja

Plik `.pre-commit-config.yaml`:

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

To bardzo sensowny lekki zestaw na start.

---

## Jak działa ten workflow w praktyce

Typowy przebieg:

1. zmieniasz kod,
2. robisz `git commit`,
3. `pre-commit` uruchamia hooki,
4. jeśli coś jest nie tak, commit zostaje zatrzymany,
5. poprawiasz kod i próbujesz jeszcze raz.

To znaczy, że wiele drobiazgów nie przedostaje się dalej.

---

## Przykładowy output

Przykładowy output przy pierwszym uruchomieniu:

```text
ruff.....................................................................Passed
ruff-format..............................................................Passed
fix end of files.........................................................Passed
trim trailing whitespace.................................................Passed
```

Przykładowy output przy błędzie:

```text
ruff.....................................................................Failed
- hook id: ruff
- exit code: 1

F401 `os` imported but unused
 --> app.py:1:8
```

Interpretacja:

- commit został zatrzymany,
- narzędzie mówi dokładnie, co poprawić,
- po poprawce próbujesz ponownie.

---

## Korzyści w pracy zespołowej

`pre-commit` sprawia, że standard jakości jest bardziej automatyczny niż umowny.

Zespół nie musi ciągle pisać w review:

- "usuń spacje",
- "posortuj importy",
- "sformatuj plik".

To robi narzędzie.

---

## Typowe błędy początkujących

- brak hooków mimo używania linterów i formatterów,
- podpinanie zbyt wielu ciężkich checków do każdego commita,
- ignorowanie błędów hooków zamiast poprawiania kodu,
- brak wersjonowania konfiguracji w repo.

---

## Praktyczna ściąga

### Minimalny zestaw

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.6.9
    hooks:
      - id: ruff
```

### Rozsądny start

- `ruff`,
- formatter,
- `end-of-file-fixer`,
- `trailing-whitespace`.

---

## Ćwiczenia

1. Napisz minimalny `.pre-commit-config.yaml`.
2. Dodaj `ruff` i przynajmniej jeden prosty hook tekstowy.
3. Opisz, co się dzieje podczas `git commit`, gdy hook wykryje błąd.
4. Zastanów się, które checki są lekkie, a które mogą być zbyt ciężkie na każdy commit.
5. Wyjaśnij, czemu `pre-commit` nie zastępuje CI.

---

## Najważniejsze do zapamiętania

- `pre-commit` uruchamia checki automatycznie przed commitem.
- To świetny sposób na zatrzymywanie drobnych problemów bardzo wcześnie.
- Najlepiej zacząć od lekkich i użytecznych hooków.
- `pre-commit` uzupełnia CI, ale go nie zastępuje.
