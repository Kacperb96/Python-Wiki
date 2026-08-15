# Logowanie w Pythonie — `logging`

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co używać `logging` zamiast `print`](#po-co-używać-logging-zamiast-print)
3. [Czym jest moduł `logging`](#czym-jest-moduł-logging)
4. [Poziomy logowania](#poziomy-logowania)
5. [`basicConfig`](#basicconfig)
6. [Najprostszy przykład](#najprostszy-przykład)
7. [Logger, handler, formatter](#logger-handler-formatter)
8. [Logowanie do pliku](#logowanie-do-pliku)
9. [Format logów](#format-logów)
10. [Kiedy używać `debug`, `info`, `warning`, `error`, `critical`](#kiedy-używać-debug-info-warning-error-critical)
11. [Logowanie wyjątków](#logowanie-wyjątków)
12. [Loggery modułowe](#loggery-modułowe)
13. [Typowe błędy początkujących](#typowe-błędy-początkujących)
14. [Praktyczne przykłady](#praktyczne-przykłady)
15. [Dobre praktyki](#dobre-praktyki)
16. [Podsumowanie](#podsumowanie)
17. [Mini ściąga](#mini-ściąga)
18. [Ćwiczenia](#ćwiczenia)
19. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

W małych skryptach ludzie często używają `print()`.

Ale w prawdziwym projekcie dużo lepszym rozwiązaniem jest `logging`.

Dlaczego?

Bo logowanie pozwala:

- kontrolować poziom ważności komunikatu,
- zapisywać logi do pliku,
- filtrować komunikaty,
- lepiej debugować aplikację,
- działać profesjonalnie.

---

## Po co używać `logging` zamiast `print`

`print()`:

- jest proste,
- ale mało elastyczne.

`logging`:

- ma poziomy logów,
- ma formatowanie,
- może pisać do pliku,
- może pisać do wielu miejsc,
- jest standardem produkcyjnym.

---

## Czym jest moduł `logging`

To wbudowany moduł Pythona do logowania zdarzeń w aplikacji.

Import:

```python
import logging
```

---

## Poziomy logowania

Najważniejsze poziomy:

- `DEBUG`
- `INFO`
- `WARNING`
- `ERROR`
- `CRITICAL`

Każdy oznacza inną wagę komunikatu.

---

## `basicConfig`

Najprostszy sposób konfiguracji logowania:

```python
import logging

logging.basicConfig(level=logging.INFO)
```

To zwykle dobry start do małych programów.

---

## Najprostszy przykład

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Program startuje")
logging.warning("To jest ostrzezenie")
logging.error("To jest blad")
```

Przykładowy wynik:

```text
INFO:root:Program startuje
WARNING:root:To jest ostrzezenie
ERROR:root:To jest blad
```

---

## Logger, handler, formatter

W uproszczeniu:

### Logger

Tworzy komunikat logu.

### Handler

Decyduje, gdzie log trafi.

### Formatter

Decyduje, jak log wygląda.

To ważne pojęcia, nawet jeśli na początku używasz tylko `basicConfig`.

---

## Logowanie do pliku

```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)
```

Teraz logi będą trafiać do pliku.

Efekt w pliku może wyglądać tak:

```text
INFO:root:Program startuje
```

---

## Format logów

Przykład:

```python
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
```

To pozwala dodać:

- czas,
- poziom,
- treść komunikatu.

Przykładowy wynik:

```text
2026-08-15 10:00:00,000 INFO Program startuje
```

---

## Kiedy używać `debug`, `info`, `warning`, `error`, `critical`

### `DEBUG`

Szczegóły techniczne dla programisty.

### `INFO`

Normalne ważne informacje o pracy programu.

### `WARNING`

Coś nie jest idealne, ale program działa.

### `ERROR`

Pojawił się błąd.

### `CRITICAL`

Poważna awaria.

---

## Logowanie wyjątków

Przykład:

```python
import logging

try:
    1 / 0
except ZeroDivisionError:
    logging.exception("Wystapil blad dzielenia")
```

`logging.exception()` automatycznie dodaje traceback.

Przykładowy wynik:

```text
ERROR:root:Wystapil blad dzielenia
Traceback (most recent call last):
...
ZeroDivisionError: division by zero
```

---

## Loggery modułowe

Popularny wzorzec:

```python
logger = logging.getLogger(__name__)
```

To pozwala mieć osobny logger dla modułu.

To bardzo powszechna dobra praktyka.

---

## Typowe błędy początkujących

- używanie `print()` zamiast `logging` w większym projekcie,
- logowanie zbyt dużo albo zbyt mało,
- mylenie poziomów logowania,
- logowanie błędów bez sensownego kontekstu,
- brak formatowania logów.

### 6. Logowanie poufnych danych

Nie wszystko powinno trafiać do logów, np. hasła, tokeny czy pełne dane wrażliwe.

---

## Praktyczne przykłady

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

logging.info("Aplikacja uruchomiona")
logging.warning("Brak pliku konfiguracyjnego")
```

Wynik:

```text
INFO: Aplikacja uruchomiona
WARNING: Brak pliku konfiguracyjnego
```

### Logger modułowy

```python
import logging

logger = logging.getLogger(__name__)
logger.info("Hello")
```

---

## Dobre praktyki

- używaj `logging`, nie `print`, w większych projektach,
- dobieraj sensownie poziomy,
- loguj kontekst, a nie tylko ogólny błąd,
- używaj loggerów modułowych,
- unikaj zalewania logów bezwartościowymi komunikatami.

Praktyczna zasada:

log powinien pomagać odpowiedzieć na pytanie "co się stało?", a nie tylko zwiększać liczbę linii w pliku.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- `logging` to standardowe narzędzie logowania w Pythonie,
- ma poziomy ważności,
- pozwala logować do pliku i konsoli,
- jest dużo lepsze niż `print` w profesjonalnym kodzie.

Najważniejsze do zapamiętania:

- `print()` służy do prostych, chwilowych komunikatów,
- `logging` służy do kontrolowanego śledzenia działania aplikacji,
- poziomy logów i format mają ogromne znaczenie praktyczne.

---

## Mini ściąga

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.debug("...")
logging.info("...")
logging.warning("...")
logging.error("...")
logging.critical("...")
```

---

## Ćwiczenia

### Ćwiczenie 1

Skonfiguruj logowanie na poziomie `INFO`.

### Ćwiczenie 2

Wyślij log `warning` i `error`.

### Ćwiczenie 3

Zaloguj wyjątek przez `logging.exception`.

---

## Przykładowe rozwiązania

```python
import logging

logging.basicConfig(level=logging.INFO)

try:
    1 / 0
except ZeroDivisionError:
    logging.exception("Dzielenie przez zero")
```
