# `nox` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `nox`](#czym-jest-nox)
3. [Po co używać `nox`](#po-co-używać-nox)
4. [Sesje i automatyzacja](#sesje-i-automatyzacja)
5. [Nox a `tox`](#nox-a-tox)
6. [Nox a CI](#nox-a-ci)
7. [Kiedy `nox` ma sens](#kiedy-nox-ma-sens)
8. [Typowe błędy początkujących](#typowe-błędy-początkujących)
9. [Praktyczne przykłady](#praktyczne-przykłady)
10. [Dobre praktyki](#dobre-praktyki)
11. [Podsumowanie](#podsumowanie)
12. [Mini ściąga](#mini-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`nox` to narzędzie do automatyzacji zadań developerskich i testowych, podobne w roli do `tox`, ale oparte o konfigurację w Pythonie.

To jest jego największa cecha charakterystyczna.

---

## Czym jest `nox`

W `nox` definiujesz sesje, czyli zadania do uruchomienia.

Na przykład:

- testy,
- linting,
- type checking,
- budowanie projektu.

---

## Po co używać `nox`

Bo daje:

- automatyzację,
- elastyczność,
- czytelną konfigurację w samym Pythonie.

To bywa wygodne dla osób, które wolą programowalny workflow.

---

## Sesje i automatyzacja

W `nox` myślisz zwykle przez sesje:

- sesja `tests`,
- sesja `lint`,
- sesja `typecheck`.

To czytelny sposób organizacji pracy nad projektem.

---

## Nox a `tox`

Oba narzędzia rozwiązują podobny obszar.

W uproszczeniu:

- `tox` jest bardzo klasyczne i szeroko znane,
- `nox` daje bardziej programowalne podejście.

Najważniejsze nie jest to, które jest "lepsze", tylko które lepiej pasuje do projektu i zespołu.

---

## Nox a CI

Tak jak `tox`, `nox` dobrze współpracuje z CI.

Może być lokalnym i pipeline'owym punktem uruchamiania tych samych checków.

---

## Kiedy `nox` ma sens

Gdy:

- chcesz programowalną konfigurację,
- lubisz definiować workflow w Pythonie,
- projekt ma kilka różnych rodzajów checków i zadań.

---

## Typowe błędy początkujących

- wybór `nox` tylko dlatego, że brzmi nowocześniej,
- komplikowanie prostego projektu,
- zbyt duża liczba sesji bez wyraźnego celu,
- brak spójności z CI.

---

## Praktyczne przykłady

### Sensowny zestaw sesji

- `tests`
- `lint`
- `typecheck`

### Gdzie `nox` pasuje

- projekt biblioteczny,
- projekt z kilkoma różnymi workflow checków.

---

## Dobre praktyki

- trzymaj sesje proste i jednoznaczne,
- nie dubluj bez sensu funkcji różnych narzędzi,
- utrzymuj spójność między lokalnym workflow a CI,
- dobieraj narzędzie do potrzeb projektu.

---

## Podsumowanie

`nox` to wartościowe narzędzie automatyzacji dla profesjonalnych projektów Python.

Warto je znać nawet wtedy, gdy finalnie w danym repo wybierzesz `tox` albo prostszy workflow.

---

## Mini ściąga

Najważniejsze:

- `nox` organizuje zadania w sesje,
- dobrze nadaje się do automatyzacji checków,
- jest alternatywą dla `tox`.

---

## Ćwiczenia

1. Wyjaśnij, czym są sesje w `nox`.
2. Porównaj mentalnie `nox` i `tox`.
3. Wskaż projekt, gdzie `nox` ma sens.
4. Wskaż projekt, gdzie może być zbyt rozbudowany.
5. Wyjaśnij, czemu zgodność z CI jest ważna.

---

## Przykładowe rozwiązania

### 1. Sesje

To zdefiniowane zadania, np. testy, linting albo type checking.

### 2. `nox` vs `tox`

`nox` daje bardziej programowalny styl konfiguracji, a `tox` jest klasycznym narzędziem tego obszaru.

### 3. Gdzie ma sens

W projekcie z kilkoma różnymi checkami i potrzebą wygodnej automatyzacji.

### 4. Gdzie za duży

W małym projekcie z prostym workflow i jedną wersją Pythona.

### 5. Zgodność z CI

Bo zmniejsza rozjazd między tym, co działa lokalnie, a tym, co sprawdza pipeline.
