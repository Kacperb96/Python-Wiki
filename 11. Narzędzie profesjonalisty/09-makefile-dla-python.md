# `Makefile` dla projektów Python

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co Pythonowcowi `Makefile`](#po-co-pythonowcowi-makefile)
3. [Czym jest target](#czym-jest-target)
4. [Typowe zastosowania](#typowe-zastosowania)
5. [Relacja z innymi narzędziami](#relacja-z-innymi-narzędziami)
6. [Czy `Makefile` jest obowiązkowy](#czy-makefile-jest-obowiązkowy)
7. [Typowe błędy początkujących](#typowe-błędy-początkujących)
8. [Praktyczne przykłady](#praktyczne-przykłady)
9. [Dobre praktyki](#dobre-praktyki)
10. [Podsumowanie](#podsumowanie)
11. [Mini ściąga](#mini-ściąga)
12. [Ćwiczenia](#ćwiczenia)
13. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`Makefile` to prosty sposób na zebranie często używanych komend projektu pod krótkimi nazwami.

W Pythonie nie jest obowiązkowy, ale często bardzo wygodny.

---

## Po co Pythonowcowi `Makefile`

Bo zamiast pamiętać długie polecenia, można mieć krótkie cele:

- `make test`
- `make lint`
- `make format`

To poprawia ergonomię pracy zespołowej.

---

## Czym jest target

Target to nazwane zadanie.

Na przykład:

```make
test:
	pytest
```

To oznacza, że `make test` uruchomi `pytest`.

---

## Typowe zastosowania

Najczęściej:

- testy,
- linting,
- formatowanie,
- type checking,
- uruchamianie aplikacji,
- budowanie projektu.

---

## Relacja z innymi narzędziami

`Makefile` zwykle nie zastępuje:

- `pytest`,
- `ruff`,
- `mypy`,

tylko daje wygodny punkt wejścia do ich uruchamiania.

---

## Czy `Makefile` jest obowiązkowy

Nie.

Ale bywa bardzo użyteczny, zwłaszcza gdy projekt ma kilka często powtarzanych poleceń.

---

## Typowe błędy początkujących

- wrzucanie do `Makefile` wszystkiego bez planu,
- ukrywanie zbyt skomplikowanej logiki,
- brak dokumentacji, co robią cele,
- różny workflow lokalnie i w dokumentacji.

---

## Praktyczne przykłady

### Minimalny `Makefile`

```make
test:
	pytest

lint:
	ruff check .

format:
	black .
```

### Wygoda zespołowa

Zamiast tłumaczyć każdemu długie komendy, można napisać:

- uruchom `make test`
- uruchom `make lint`

---

## Dobre praktyki

- trzymaj cele proste i czytelne,
- używaj go jako skrótu do workflow,
- nie ukrywaj w nim magicznych, trudnych do zrozumienia działań,
- dbaj o zgodność z README i CI.

---

## Podsumowanie

`Makefile` to małe narzędzie, które może znacząco poprawić ergonomię codziennej pracy z projektem Python.

---

## Mini ściąga

```make
test:
	pytest
```

Najważniejsze:

- target to nazwane zadanie,
- `Makefile` upraszcza codzienny workflow,
- dobrze sprawdza się jako warstwa skrótów nad innymi narzędziami.

---

## Ćwiczenia

1. Napisz target `test`.
2. Napisz target `lint`.
3. Napisz target `format`.
4. Wyjaśnij, po co zespołowi `Makefile`.
5. Wyjaśnij, czemu nie warto ukrywać w nim zbyt skomplikowanej logiki.

---

## Przykładowe rozwiązania

### 1. `test`

```make
test:
	pytest
```

### 2. `lint`

```make
lint:
	ruff check .
```

### 3. `format`

```make
format:
	black .
```

### 4. Po co zespołowi

Żeby skrócić i ujednolicić najczęściej używane komendy projektu.

### 5. Czemu nie komplikować

Bo wtedy `Makefile` przestaje upraszczać, a zaczyna ukrywać trudny workflow.
