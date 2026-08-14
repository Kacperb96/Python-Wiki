# `isort` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `isort`](#czym-jest-isort)
3. [Po co porządkować importy](#po-co-porządkować-importy)
4. [Jak działa `isort`](#jak-działa-isort)
5. [Grupowanie importów](#grupowanie-importów)
6. [Konfiguracja](#konfiguracja)
7. [Relacja z `ruff` i `black`](#relacja-z-ruff-i-black)
8. [Typowe błędy początkujących](#typowe-błędy-początkujących)
9. [Praktyczne przykłady](#praktyczne-przykłady)
10. [Dobre praktyki](#dobre-praktyki)
11. [Podsumowanie](#podsumowanie)
12. [Mini ściąga](#mini-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`isort` służy do porządkowania importów w Pythonie.

W wielu projektach tę rolę częściowo przejmuje też `ruff`, ale `isort` nadal warto znać.

---

## Czym jest `isort`

To narzędzie, które:

- sortuje importy,
- grupuje je,
- poprawia ich układ,
- pomaga utrzymać porządek na górze plików.

---

## Po co porządkować importy

Bo chaotyczne importy:

- utrudniają czytanie pliku,
- zwiększają ryzyko duplikatów,
- utrudniają szybkie rozpoznanie zależności.

---

## Jak działa `isort`

Narzędzie bierze blok importów i układa go według zasad.

Najczęściej oddziela:

- standard library,
- third-party,
- lokalne importy projektu.

---

## Grupowanie importów

Przykład docelowego układu:

```python
import os
import sys

import httpx
import pytest

from app.services import run_job
```

To dużo czytelniejsze niż przypadkowa mieszanka.

---

## Konfiguracja

W `pyproject.toml`:

```toml
[tool.isort]
profile = "black"
line_length = 88
```

`profile = "black"` pomaga utrzymać zgodność z formatterem.

---

## Relacja z `ruff` i `black`

Dziś często masz dwa warianty:

- `isort` + `black`,
- `ruff` z regułami importów + formatter.

Ważne jest nie tyle narzędzie samo w sobie, ile spójny workflow.

---

## Typowe błędy początkujących

- ręczne sortowanie importów raz tak, raz inaczej,
- brak rozdziału standard library i lokalnych importów,
- niespójna konfiguracja między narzędziami,
- dublowanie różnych narzędzi bez planu.

---

## Praktyczne przykłady

### Chaos

```python
import httpx
import os
from app.services import task
import sys
```

### Porządek

```python
import os
import sys

import httpx

from app.services import task
```

---

## Dobre praktyki

- automatyzuj sortowanie importów,
- trzymaj zgodność z formatterem,
- nie poprawiaj ręcznie tego, co narzędzie zrobi lepiej,
- w projekcie wybierz jedno spójne podejście.

---

## Podsumowanie

`isort` to praktyczne narzędzie porządkujące importy.

Nawet jeśli część jego roli przejmie `ruff`, rozumienie zasad układu importów nadal jest bardzo ważne.

---

## Mini ściąga

```toml
[tool.isort]
profile = "black"
line_length = 88
```

Najważniejsze:

- `isort` porządkuje importy,
- rozdziela grupy importów,
- dobrze współpracuje z `black`.

---

## Ćwiczenia

1. Wyjaśnij, czemu warto grupować importy.
2. Dodaj konfigurację `isort`.
3. Uporządkuj przykładowy blok importów.
4. Wyjaśnij, czemu `profile = "black"` bywa przydatne.
5. Porównaj rolę `isort` i `ruff` przy importach.

---

## Przykładowe rozwiązania

### 1. Po co grupowanie

Bo poprawia czytelność i ułatwia zrozumienie zależności pliku.

### 2. Konfiguracja

```toml
[tool.isort]
profile = "black"
```

### 3. Uporządkowanie

```python
import os
import sys

import httpx
```

### 4. `profile = "black"`

Pomaga uniknąć konfliktów formatowania między narzędziami.

### 5. `isort` vs `ruff`

Oba mogą pomagać z importami, ale ważne jest, by narzędzia nie robiły tego w sprzeczny sposób.
