# `poetry` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `poetry`](#czym-jest-poetry)
3. [Po co używać `poetry`](#po-co-używać-poetry)
4. [Zależności i środowisko](#zależności-i-środowisko)
5. [Relacja z `pyproject.toml`](#relacja-z-pyprojecttoml)
6. [Poetry a `pip` i `venv`](#poetry-a-pip-i-venv)
7. [Kiedy `poetry` ma sens](#kiedy-poetry-ma-sens)
8. [Typowe błędy początkujących](#typowe-błędy-początkujących)
9. [Praktyczne przykłady](#praktyczne-przykłady)
10. [Dobre praktyki](#dobre-praktyki)
11. [Podsumowanie](#podsumowanie)
12. [Mini ściąga](#mini-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`poetry` to popularne narzędzie do zarządzania zależnościami i projektami Python.

Łączy kilka potrzebnych elementów w jeden spójny workflow.

---

## Czym jest `poetry`

To narzędzie, które pomaga:

- zarządzać zależnościami,
- pracować ze środowiskiem,
- budować pakiet,
- utrzymywać projekt wokół `pyproject.toml`.

---

## Po co używać `poetry`

Bo daje:

- uporządkowany workflow,
- wygodne zarządzanie zależnościami,
- lepszą spójność projektu,
- prostszy onboarding.

---

## Zależności i środowisko

W projekcie trzeba panować nad:

- zależnościami runtime,
- zależnościami developerskimi,
- wersją Pythona,
- środowiskiem izolowanym od systemu.

`poetry` dobrze adresuje ten zestaw problemów.

---

## Relacja z `pyproject.toml`

`poetry` bardzo mocno opiera się na `pyproject.toml`.

To dobry przykład nowoczesnego podejścia do organizacji projektu Python.

---

## Poetry a `pip` i `venv`

`pip` i `venv` to klasyczne fundamenty.

`poetry` buduje wygodniejszy workflow na poziomie zarządzania całym projektem.

Warto znać oba podejścia.

---

## Kiedy `poetry` ma sens

Najczęściej gdy:

- budujesz pełny projekt,
- zależy ci na przewidywalnym workflow,
- pracujesz zespołowo,
- chcesz mieć porządek w zależnościach i metadanych projektu.

---

## Typowe błędy początkujących

- używanie `poetry` bez rozumienia, co robi środowisko i zależności,
- mieszanie kilku systemów zarządzania projektem bez planu,
- brak rozdzielenia zależności dev i runtime.

---

## Praktyczne przykłady

### Gdzie `poetry` pasuje

- aplikacja backendowa,
- projekt biblioteczny,
- narzędzie CLI.

### Gdzie nie zawsze jest konieczne

- bardzo mały jednorazowy skrypt.

---

## Dobre praktyki

- trzymaj jeden spójny workflow na projekt,
- dokumentuj sposób pracy z zależnościami,
- rozdzielaj zależności produkcyjne i developerskie,
- rozumiej, co dzieje się pod spodem, zamiast tylko klikać komendy.

---

## Podsumowanie

`poetry` to ważne narzędzie ekosystemu Python i warto je znać jako profesjonalista.

Nie jest jedyną drogą, ale dobrze pokazuje nowoczesny sposób organizacji projektu.

---

## Mini ściąga

Najważniejsze:

- `poetry` pomaga ogarniać zależności i projekt,
- opiera się o `pyproject.toml`,
- dobrze sprawdza się w pełnych projektach.

---

## Ćwiczenia

1. Wyjaśnij, jaki problem rozwiązuje `poetry`.
2. Porównaj je mentalnie z `pip` + `venv`.
3. Wskaż projekt, w którym `poetry` ma sens.
4. Wskaż projekt, gdzie może być nadmiarowe.
5. Wyjaśnij, po co rozdzielać zależności runtime i dev.

---

## Przykładowe rozwiązania

### 1. Problem

Porządkuje zarządzanie zależnościami, środowiskiem i projektem wokół jednego workflow.

### 2. Porównanie

`pip` i `venv` są bazą, a `poetry` daje wyższy poziom organizacji projektu.

### 3. Gdzie ma sens

W rozwijanym projekcie aplikacyjnym lub bibliotecznym.

### 4. Gdzie nadmiarowe

W jednorazowym, bardzo prostym skrypcie.

### 5. Po co rozdzielać

Żeby nie instalować narzędzi developerskich tam, gdzie potrzebne jest tylko uruchomienie aplikacji.
