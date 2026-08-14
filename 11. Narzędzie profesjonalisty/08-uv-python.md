# `uv` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `uv`](#czym-jest-uv)
3. [Po co używać `uv`](#po-co-używać-uv)
4. [Zależności i środowisko](#zależności-i-środowisko)
5. [Relacja z `pip` i `venv`](#relacja-z-pip-i-venv)
6. [Relacja z `pyproject.toml`](#relacja-z-pyprojecttoml)
7. [Kiedy `uv` ma sens](#kiedy-uv-ma-sens)
8. [Typowe błędy początkujących](#typowe-błędy-początkujących)
9. [Praktyczne przykłady](#praktyczne-przykłady)
10. [Dobre praktyki](#dobre-praktyki)
11. [Podsumowanie](#podsumowanie)
12. [Mini ściąga](#mini-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`uv` to nowoczesne narzędzie do pracy z zależnościami i środowiskiem Python.

Jest cenione głównie za szybkość i wygodę.

---

## Czym jest `uv`

W dużym uproszczeniu to narzędzie, które pomaga:

- zarządzać środowiskiem,
- instalować zależności,
- pracować z projektem Python szybciej niż klasyczny zestaw narzędzi.

---

## Po co używać `uv`

Najczęstsze powody:

- szybkość,
- wygodniejszy workflow,
- nowocześniejsze podejście do projektu,
- dobra współpraca z `pyproject.toml`.

---

## Zależności i środowisko

W profesjonalnym projekcie trzeba sprawnie ogarnąć:

- wersję Pythona,
- środowisko wirtualne,
- zależności runtime,
- zależności developerskie.

`uv` próbuje ten workflow uprościć.

---

## Relacja z `pip` i `venv`

Klasyczny zestaw:

- `venv` do środowiska,
- `pip` do instalacji.

`uv` oferuje nowocześniejszą i często szybszą warstwę pracy nad tym samym problemem.

To nie znaczy, że trzeba zapomnieć o `pip`, ale warto znać nowoczesne narzędzia.

---

## Relacja z `pyproject.toml`

W nowoczesnych projektach coraz więcej rzeczy kręci się wokół `pyproject.toml`.

`uv` dobrze wpisuje się w ten model pracy.

---

## Kiedy `uv` ma sens

Szczególnie gdy:

- budujesz nowy projekt,
- zależy ci na szybkim workflow,
- chcesz mieć nowocześniejsze podejście do zależności,
- pracujesz często na wielu projektach.

---

## Typowe błędy początkujących

- używanie narzędzia bez zrozumienia podstaw `pip`, `venv` i `pyproject.toml`,
- mieszanie kilku sposobów zarządzania projektem bez planu,
- brak rozróżnienia zależności runtime i dev.

---

## Praktyczne przykłady

### Kiedy warto rozważyć `uv`

- nowe API w Pythonie,
- nowe narzędzie CLI,
- projekt zespołowy z `pyproject.toml`.

### Kiedy nie jest konieczne

- prosty jednorazowy skrypt,
- środowisko, gdzie i tak obowiązuje sztywny workflow zespołowy.

---

## Dobre praktyki

- najpierw rozumiej podstawy, potem wybieraj narzędzie,
- trzymaj jeden spójny workflow w projekcie,
- dokumentuj sposób pracy z zależnościami w README,
- nie mieszaj chaotycznie `pip`, `poetry`, `uv` i innych narzędzi.

---

## Podsumowanie

`uv` to ważne nowoczesne narzędzie, które warto znać jako profesjonalista Python, nawet jeśli nie każdy projekt będzie go używał.

Najważniejsze jest rozumienie problemu, który rozwiązuje.

---

## Mini ściąga

Najważniejsze:

- `uv` pomaga zarządzać środowiskiem i zależnościami,
- dobrze pasuje do nowoczesnych projektów,
- nie zastępuje potrzeby rozumienia `pip`, `venv` i `pyproject.toml`.

---

## Ćwiczenia

1. Wyjaśnij, jaki problem rozwiązuje `uv`.
2. Porównaj mentalnie `uv` z `pip` + `venv`.
3. Wskaż, kiedy w projekcie `uv` ma sens.
4. Wskaż, kiedy nie jest konieczny.
5. Wyjaśnij, czemu nie warto mieszać wielu workflow naraz.

---

## Przykładowe rozwiązania

### 1. Problem

Upraszcza i przyspiesza zarządzanie środowiskiem oraz zależnościami projektu.

### 2. Porównanie

`pip` i `venv` to klasyczne podstawy, a `uv` daje nowocześniejszy workflow wokół podobnych potrzeb.

### 3. Kiedy ma sens

Przy nowym, aktywnie rozwijanym projekcie.

### 4. Kiedy niekonieczny

Przy bardzo prostym skrypcie bez większego zaplecza projektowego.

### 5. Czemu nie mieszać

Bo łatwo o chaos konfiguracyjny i trudniejszy onboarding.
