# `tox` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `tox`](#czym-jest-tox)
3. [Po co używać `tox`](#po-co-używać-tox)
4. [Testowanie w wielu środowiskach](#testowanie-w-wielu-środowiskach)
5. [Relacja z CI](#relacja-z-ci)
6. [Relacja z `pytest`, `ruff`, `mypy`](#relacja-z-pytest-ruff-mypy)
7. [Kiedy `tox` ma sens](#kiedy-tox-ma-sens)
8. [Kiedy może być nadmiarem](#kiedy-może-być-nadmiarem)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczna ściąga](#praktyczna-ściąga)
11. [Ćwiczenia](#ćwiczenia)
12. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

`tox` to narzędzie do automatyzacji testów i checków w wielu środowiskach.

Jest szczególnie ważne przy bibliotekach i projektach, które mają działać na więcej niż jednej wersji Pythona.

---

## Czym jest `tox`

`tox` pozwala definiować zestawy środowisk i zadań, które mają się w nich wykonać.

Na przykład:

- testy,
- linting,
- type checking,
- różne wersje Pythona.

---

## Po co używać `tox`

Bo pomaga:

- sprawdzać projekt w powtarzalny sposób,
- testować wiele wersji Pythona,
- uporządkować lokalne checki,
- zbliżyć lokalny workflow do CI.

---

## Testowanie w wielu środowiskach

To największa zaleta `tox`.

Możesz sprawdzić, czy projekt działa:

- na Pythonie 3.11,
- na Pythonie 3.12,
- na Pythonie 3.13,
- albo z różnymi zestawami zależności.

To bardzo ważne szczególnie dla bibliotek i narzędzi używanych szerzej niż tylko w jednym środowisku.

---

## Relacja z CI

`tox` nie zastępuje CI.

Dobrze współpracuje z CI, bo daje jeden spójny sposób uruchamiania checków lokalnie i w pipeline.

To bardzo pomaga uniknąć rozjazdu typu:

- lokalnie odpalamy jedno,
- w CI odpalamy coś zupełnie innego.

---

## Relacja z `pytest`, `ruff`, `mypy`

`tox` nie testuje sam z siebie logiki aplikacji.

On raczej orkiestruje narzędzia takie jak:

- `pytest`,
- `ruff`,
- `mypy`.

To ważne rozróżnienie:

`tox` organizuje środowiska i sposób uruchamiania, a nie zastępuje samych narzędzi jakości.

---

## Kiedy `tox` ma sens

Szczególnie gdy:

- rozwijasz bibliotekę,
- wspierasz wiele wersji Pythona,
- chcesz mieć powtarzalne środowiska checków,
- repo ma bardziej dojrzały workflow.

---

## Kiedy może być nadmiarem

Nie każdy projekt go potrzebuje.

Dla bardzo małego projektu wewnętrznego z jedną wersją Pythona i prostym workflow może być zbędny.

Narzędzie ma dawać realną wartość, a nie tylko zwiększać liczbę plików konfiguracyjnych.

---

## Typowe błędy początkujących

- używanie `tox` bez realnej potrzeby,
- zbyt skomplikowana konfiguracja na start,
- traktowanie go jako zamiennika testów,
- brak spójności między tym, co robi lokalnie `tox`, a tym, co robi CI.

---

## Praktyczna ściąga

### Gdzie `tox` pasuje

- biblioteka open source,
- projekt wspierający wiele wersji Pythona,
- repo z bardziej rozbudowanym QA workflow.

### O czym pamiętać

- `tox` orkiestruje środowiska i checki,
- dobrze współpracuje z CI,
- nie jest obowiązkowy w każdym projekcie.

---

## Ćwiczenia

1. Wyjaśnij, po co testować projekt w wielu środowiskach.
2. Wyjaśnij relację `tox` i CI.
3. Wskaż projekt, gdzie `tox` ma sens.
4. Wskaż projekt, gdzie może być zbędny.
5. Wyjaśnij, czemu `tox` nie zastępuje testów.

---

## Najważniejsze do zapamiętania

- `tox` służy do orkiestracji checków w wielu środowiskach.
- Największą wartość daje tam, gdzie liczy się kompatybilność wielowersyjna.
- Dobrze współpracuje z CI.
- Nie każdy projekt go potrzebuje.
