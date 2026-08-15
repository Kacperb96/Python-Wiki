# `isort` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `isort`](#czym-jest-isort)
3. [Po co porządkować importy](#po-co-porządkować-importy)
4. [Jak działa `isort`](#jak-działa-isort)
5. [Grupowanie importów](#grupowanie-importów)
6. [Przykład przed i po](#przykład-przed-i-po)
7. [Konfiguracja](#konfiguracja)
8. [Relacja z `ruff` i `black`](#relacja-z-ruff-i-black)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczna ściąga](#praktyczna-ściąga)
11. [Ćwiczenia](#ćwiczenia)
12. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

`isort` służy do porządkowania importów w Pythonie.

Dziś część tej roli bywa przejęta przez `ruff`, ale samo rozumienie zasad porządku importów nadal jest bardzo ważne.

---

## Czym jest `isort`

To narzędzie, które:

- sortuje importy,
- grupuje je,
- poprawia ich układ,
- pomaga utrzymać porządek na górze pliku.

---

## Po co porządkować importy

Chaotyczne importy:

- utrudniają czytanie pliku,
- ukrywają zależności,
- zwiększają bałagan,
- utrudniają szybkie skanowanie modułu.

Dobrze ułożone importy od razu dają czytelniejszy start każdego pliku.

---

## Jak działa `isort`

Najprościej:

bierze blok importów i układa go według ustalonych zasad.

Najczęściej rozdziela:

- standard library,
- third-party,
- lokalne importy projektu.

---

## Grupowanie importów

Docelowy układ zwykle wygląda tak:

```python
import os
import sys

import httpx
import pytest

from app.services import run_job
```

To dużo czytelniejsze niż przypadkowa mieszanka wszystkiego.

---

## Przykład przed i po

### Przed

```python
import httpx
import os
from app.services import task
import sys
```

### Po

```python
import os
import sys

import httpx

from app.services import task
```

To prosty przykład, ale bardzo dobrze pokazuje sens narzędzia.

---

## Konfiguracja

W `pyproject.toml`:

```toml
[tool.isort]
profile = "black"
line_length = 88
```

`profile = "black"` pomaga zachować zgodność z formatterem.

---

## Relacja z `ruff` i `black`

Dziś częsty wybór wygląda tak:

- `isort` + `black`,
- albo `ruff` z obsługą importów + formatter.

Najważniejsze nie jest samo narzędzie, tylko spójny workflow.

Nie chcesz mieć konfliktu między jednym narzędziem a drugim.

---

## Typowe błędy początkujących

- ręczne sortowanie importów za każdym razem inaczej,
- brak rozdziału między standard library i lokalnym kodem,
- niespójna konfiguracja narzędzi,
- dublowanie roli kilku narzędzi bez planu.

---

## Praktyczna ściąga

### Minimalna konfiguracja

```toml
[tool.isort]
profile = "black"
line_length = 88
```

### Sens porządkowania

- czytelniejszy plik,
- łatwiejszy review,
- spójny układ zależności.

---

## Ćwiczenia

1. Przygotuj chaotyczny blok importów i uporządkuj go.
2. Dodaj konfigurację `isort` do `pyproject.toml`.
3. Wyjaśnij, czemu `profile = "black"` jest przydatne.
4. Porównaj rolę `isort` z regułami importów w `ruff`.
5. Własnymi słowami opisz, dlaczego porządek importów poprawia czytelność.

---

## Najważniejsze do zapamiętania

- `isort` porządkuje i grupuje importy.
- Importy powinny być uporządkowane i czytelne.
- Warto utrzymywać zgodność między `isort` i formatterem.
- Nawet jeśli używasz `ruff`, zasady porządku importów nadal są ważne.
