# `uv` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `uv`](#czym-jest-uv)
3. [Po co używać `uv`](#po-co-używać-uv)
4. [Relacja z `pip` i `venv`](#relacja-z-pip-i-venv)
5. [Relacja z `pyproject.toml`](#relacja-z-pyprojecttoml)
6. [Dlaczego `uv` jest kojarzone z szybkością](#dlaczego-uv-jest-kojarzone-z-szybkością)
7. [Kiedy `uv` ma sens](#kiedy-uv-ma-sens)
8. [Kiedy nie jest konieczne](#kiedy-nie-jest-konieczne)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczna ściąga](#praktyczna-ściąga)
11. [Ćwiczenia](#ćwiczenia)
12. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

`uv` to nowoczesne narzędzie do pracy z zależnościami i środowiskiem Python.

Jest cenione głównie za szybkość i wygodę.

---

## Czym jest `uv`

W dużym uproszczeniu to narzędzie, które pomaga:

- zarządzać środowiskiem,
- instalować zależności,
- pracować z projektem Python szybciej niż klasyczny zestaw narzędzi,
- lepiej wpisywać się w nowoczesny workflow projektu.

---

## Po co używać `uv`

Najczęstsze powody:

- szybkość,
- wygodniejszy workflow,
- nowocześniejsze podejście do zależności,
- dobra współpraca z `pyproject.toml`.

To narzędzie warto znać nawet jeśli nie każdy projekt będzie go używał.

---

## Relacja z `pip` i `venv`

Klasyczny zestaw:

- `venv` do środowiska,
- `pip` do instalacji.

`uv` oferuje nowocześniejszą i często szybszą warstwę pracy nad tym samym problemem.

To nie znaczy, że klasyczny model przestaje mieć sens.

To znaczy tylko, że pojawiły się wygodniejsze opcje dla wielu projektów.

---

## Relacja z `pyproject.toml`

W nowoczesnych projektach coraz więcej rzeczy kręci się wokół `pyproject.toml`.

`uv` dobrze wpisuje się w ten model pracy.

To jeden z powodów, dla których jest dziś coraz częściej brane pod uwagę przy nowych projektach.

---

## Dlaczego `uv` jest kojarzone z szybkością

To narzędzie zdobyło popularność między innymi dlatego, że workflow związany z:

- tworzeniem środowisk,
- instalacją zależności,
- pracą na wielu projektach,

potrafi być odczuwalnie szybszy i wygodniejszy.

Dla osoby pracującej na wielu repozytoriach to naprawdę robi różnicę.

---

## Kiedy `uv` ma sens

Szczególnie gdy:

- budujesz nowy projekt,
- zależy Ci na szybkim workflow,
- pracujesz często na wielu projektach,
- chcesz podejścia nowocześniejszego niż samo `pip` + `venv`.

---

## Kiedy nie jest konieczne

Nie zawsze musisz go używać.

Dla bardzo prostego skryptu albo projektu, który już ma ustalony workflow zespołowy, zmiana narzędzia może nic realnie nie dawać.

Narzędzie ma pomagać, a nie tylko wyglądać nowocześnie.

---

## Typowe błędy początkujących

- używanie `uv` bez zrozumienia podstaw `pip`, `venv` i `pyproject.toml`,
- mieszanie wielu workflow zależności bez planu,
- brak rozróżnienia runtime i dev dependencies,
- wybór narzędzia tylko dlatego, że jest szybkie, bez oceny potrzeb projektu.

---

## Praktyczna ściąga

### Gdzie `uv` pasuje

- nowe API w Pythonie,
- nowe narzędzie CLI,
- projekt zespołowy z `pyproject.toml`,
- praca na wielu repozytoriach.

### Gdzie nie musi być konieczne

- prosty jednorazowy skrypt,
- środowisko ze sztywnym istniejącym workflow.

---

## Ćwiczenia

1. Wyjaśnij, jaki problem rozwiązuje `uv`.
2. Porównaj je mentalnie z `pip` + `venv`.
3. Wskaż projekt, w którym `uv` ma sens.
4. Wskaż projekt, gdzie nie jest konieczne.
5. Wyjaśnij, czemu nie warto mieszać wielu workflow naraz.

---

## Najważniejsze do zapamiętania

- `uv` pomaga zarządzać środowiskiem i zależnościami nowocześniej i często szybciej.
- Dobrze wpisuje się w świat `pyproject.toml`.
- Nie zwalnia z rozumienia podstaw `pip` i `venv`.
- Narzędzie powinno być dopasowane do projektu, a nie wybrane tylko dlatego, że jest modne.
