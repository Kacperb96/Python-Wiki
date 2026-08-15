# `nox` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `nox`](#czym-jest-nox)
3. [Po co używać `nox`](#po-co-używać-nox)
4. [Sesje i automatyzacja](#sesje-i-automatyzacja)
5. [Nox a `tox`](#nox-a-tox)
6. [Nox a CI](#nox-a-ci)
7. [Kiedy `nox` ma sens](#kiedy-nox-ma-sens)
8. [Kiedy może być nadmiarem](#kiedy-może-być-nadmiarem)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczna ściąga](#praktyczna-ściąga)
11. [Ćwiczenia](#ćwiczenia)
12. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

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

To daje bardziej programowalny styl konfiguracji niż klasyczny plik konfiguracyjny.

---

## Po co używać `nox`

Bo daje:

- automatyzację,
- elastyczność,
- czytelną konfigurację w samym Pythonie,
- wygodny sposób organizacji wielu rodzajów checków.

To bywa bardzo wygodne dla osób, które wolą programowalny workflow.

---

## Sesje i automatyzacja

W `nox` myślisz zwykle przez sesje:

- sesja `tests`,
- sesja `lint`,
- sesja `typecheck`.

To czytelny sposób organizacji pracy nad projektem.

Zamiast pamiętać wiele osobnych poleceń, możesz mieć zestaw nazwanych zadań.

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

To pomaga utrzymać spójność między pracą lokalną a automatyzacją w repo.

---

## Kiedy `nox` ma sens

Gdy:

- chcesz programowalną konfigurację,
- lubisz definiować workflow w Pythonie,
- projekt ma kilka różnych rodzajów checków i zadań,
- potrzebujesz bardziej elastycznej organizacji sesji.

---

## Kiedy może być nadmiarem

Dla bardzo prostego projektu może być zbyt rozbudowany.

Jeśli repo ma:

- jedną wersję Pythona,
- prosty zestaw checków,
- bardzo mały zespół,

czasem prostszy workflow wystarczy.

---

## Typowe błędy początkujących

- wybór `nox` tylko dlatego, że brzmi nowocześniej,
- komplikowanie prostego projektu,
- zbyt duża liczba sesji bez wyraźnego celu,
- brak spójności z CI.

---

## Praktyczna ściąga

### Sensowny zestaw sesji

- `tests`,
- `lint`,
- `typecheck`.

### O czym pamiętać

- `nox` organizuje zadania w sesje,
- dobrze nadaje się do automatyzacji checków,
- nie każdy projekt musi go używać.

---

## Ćwiczenia

1. Wyjaśnij, czym są sesje w `nox`.
2. Porównaj mentalnie `nox` i `tox`.
3. Wskaż projekt, gdzie `nox` ma sens.
4. Wskaż projekt, gdzie może być zbyt rozbudowany.
5. Wyjaśnij, czemu zgodność z CI jest ważna.

---

## Najważniejsze do zapamiętania

- `nox` organizuje zadania w sesje i daje bardziej programowalny workflow.
- Dobrze nadaje się do automatyzacji checków developerskich.
- Jest alternatywą dla `tox`, ale nie zawsze musi być potrzebny.
- Najważniejsza jest spójność całego workflow projektu.
