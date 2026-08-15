# `Makefile` dla projektów Python

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co Pythonowcowi `Makefile`](#po-co-pythonowcowi-makefile)
3. [Czym jest target](#czym-jest-target)
4. [Typowe zastosowania](#typowe-zastosowania)
5. [Przykład praktyczny](#przykład-praktyczny)
6. [Jak używa się tego w zespole](#jak-używa-się-tego-w-zespole)
7. [Relacja z innymi narzędziami](#relacja-z-innymi-narzędziami)
8. [Czy `Makefile` jest obowiązkowy](#czy-makefile-jest-obowiązkowy)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczna ściąga](#praktyczna-ściąga)
11. [Ćwiczenia](#ćwiczenia)
12. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

`Makefile` to prosty sposób na zebranie często używanych komend projektu pod krótkimi nazwami.

W Pythonie nie jest obowiązkowy, ale często bardzo wygodny.

---

## Po co Pythonowcowi `Makefile`

Bo zamiast pamiętać długie polecenia, możesz mieć krótkie cele:

- `make test`,
- `make lint`,
- `make format`,
- `make check`.

To poprawia ergonomię pracy lokalnej i zespołowej.

---

## Czym jest target

Target to nazwane zadanie.

Przykład:

```make
test:
	pytest
```

To oznacza, że `make test` uruchomi `pytest`.

---

## Typowe zastosowania

Najczęściej do:

- testów,
- lintingu,
- formatowania,
- type checkingu,
- uruchamiania aplikacji,
- budowania projektu.

---

## Przykład praktyczny

```make
test:
	pytest

lint:
	ruff check .

format:
	black .

check:
	ruff check .
	mypy .
	pytest
```

To prosty przykład, ale daje już bardzo wygodny punkt wejścia do codziennej pracy.

---

## Jak używa się tego w zespole

Bardzo praktyczna zaleta:

zamiast tłumaczyć każdej osobie długie komendy, możesz powiedzieć po prostu:

- uruchom `make test`,
- uruchom `make check`,
- uruchom `make format`.

To zmniejsza chaos i upraszcza onboarding.

---

## Relacja z innymi narzędziami

`Makefile` zwykle nie zastępuje:

- `pytest`,
- `ruff`,
- `mypy`,
- `black`.

On jest tylko wygodną warstwą skrótów nad nimi.

To ważne rozróżnienie.

---

## Czy `Makefile` jest obowiązkowy

Nie.

Ale bywa bardzo użyteczny, zwłaszcza gdy projekt ma kilka często powtarzanych poleceń.

Dla bardzo małego skryptu może być zbędny.

Dla większego repo zwykle jest wygodny.

---

## Typowe błędy początkujących

- wrzucanie do `Makefile` wszystkiego bez planu,
- ukrywanie zbyt skomplikowanej logiki,
- brak zgodności między `Makefile`, README i CI,
- robienie targetów o niejasnych nazwach.

---

## Praktyczna ściąga

### Minimalny przykład

```make
test:
	pytest

lint:
	ruff check .
```

### Po co to mieć

- krótsze komendy,
- wygodniejsza praca,
- prostszy onboarding,
- bardziej przewidywalny workflow.

---

## Ćwiczenia

1. Napisz target `test`.
2. Napisz target `lint`.
3. Napisz target `format`.
4. Dodaj target `check` uruchamiający kilka narzędzi jakości.
5. Wyjaśnij, po co zespołowi `Makefile`.

---

## Najważniejsze do zapamiętania

- `Makefile` upraszcza codzienny workflow przez krótkie komendy.
- Nie zastępuje narzędzi, tylko je wygodnie uruchamia.
- Najlepiej trzymać targety proste, czytelne i zgodne z dokumentacją projektu.
