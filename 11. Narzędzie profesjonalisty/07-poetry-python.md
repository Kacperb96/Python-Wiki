# `poetry` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `poetry`](#czym-jest-poetry)
3. [Po co używać `poetry`](#po-co-używać-poetry)
4. [Relacja z `pyproject.toml`](#relacja-z-pyprojecttoml)
5. [Poetry a `pip` i `venv`](#poetry-a-pip-i-venv)
6. [Typowy workflow](#typowy-workflow)
7. [Kiedy `poetry` ma sens](#kiedy-poetry-ma-sens)
8. [Kiedy może być nadmiarowe](#kiedy-może-być-nadmiarowe)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczna ściąga](#praktyczna-ściąga)
11. [Ćwiczenia](#ćwiczenia)
12. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

`poetry` to popularne narzędzie do zarządzania zależnościami i projektami Python.

Łączy kilka potrzebnych elementów w jeden spójny workflow.

---

## Czym jest `poetry`

`poetry` pomaga:

- zarządzać zależnościami,
- pracować ze środowiskiem,
- utrzymywać metadane projektu,
- budować pakiet,
- opierać projekt o `pyproject.toml`.

To narzędzie bardzo często spotykane w nowoczesnych repozytoriach Pythona.

---

## Po co używać `poetry`

Bo daje jeden spójny model pracy.

Zamiast składać workflow z wielu ręcznych kroków, dostajesz bardziej uporządkowane podejście do:

- instalacji zależności,
- rozróżniania runtime i dev dependencies,
- zarządzania projektem.

---

## Relacja z `pyproject.toml`

`poetry` bardzo mocno opiera się o `pyproject.toml`.

To tam zwykle trzymasz:

- metadane projektu,
- zależności,
- grupy zależności.

To dobrze wpisuje się w nowoczesny kierunek ekosystemu Python.

---

## Poetry a `pip` i `venv`

Klasyczny model:

- `venv` tworzy środowisko,
- `pip` instaluje zależności.

`poetry` daje bardziej zintegrowany workflow nad podobnym problemem.

To nie znaczy, że klasyczny model jest zły.

To znaczy tylko, że `poetry` próbuje go uporządkować i uprościć.

---

## Typowy workflow

Mentalny przykład pracy:

1. tworzysz projekt,
2. dodajesz zależności,
3. dodajesz zależności dev,
4. uruchamiasz projekt w kontekście środowiska,
5. trzymasz wszystko spójnie w jednym workflow.

Najważniejsza wartość to porządek i przewidywalność.

---

## Kiedy `poetry` ma sens

Szczególnie gdy:

- budujesz pełny projekt, a nie jednorazowy skrypt,
- chcesz mieć porządek w zależnościach,
- pracujesz zespołowo,
- projekt ma rosnąć,
- zależy Ci na czytelnym workflow wokół `pyproject.toml`.

---

## Kiedy może być nadmiarowe

Nie zawsze musisz go używać.

Dla bardzo małego, jednorazowego skryptu często wystarczy:

- `venv`,
- `pip`,
- prosty `requirements.txt` albo minimalny setup projektu.

Narzędzie ma pomagać, a nie komplikować prostą sytuację.

---

## Typowe błędy początkujących

- używanie `poetry` bez rozumienia środowiska i zależności,
- mieszanie kilku systemów zarządzania projektem bez planu,
- brak rozdzielenia runtime i dev dependencies,
- wybieranie narzędzia tylko dlatego, że jest modne.

---

## Praktyczna ściąga

### Gdzie `poetry` pasuje

- aplikacja backendowa,
- narzędzie CLI,
- projekt biblioteczny,
- repo zespołowe.

### Gdzie nie zawsze jest konieczne

- mały jednorazowy skrypt,
- bardzo prosty projekt bez rozbudowanego workflow.

---

## Ćwiczenia

1. Wyjaśnij, jaki problem rozwiązuje `poetry`.
2. Porównaj je mentalnie z `pip` + `venv`.
3. Wskaż projekt, w którym `poetry` ma sens.
4. Wskaż projekt, gdzie może być nadmiarowe.
5. Wyjaśnij, po co rozdzielać zależności runtime i dev.

---

## Najważniejsze do zapamiętania

- `poetry` porządkuje zależności i projekt wokół jednego workflow.
- Dobrze współpracuje z `pyproject.toml`.
- Nie jest jedyną drogą, ale warto je znać.
- Najważniejsze to wybrać jeden spójny model pracy dla projektu.
