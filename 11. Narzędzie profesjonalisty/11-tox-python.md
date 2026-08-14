# `tox` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `tox`](#czym-jest-tox)
3. [Po co używać `tox`](#po-co-używać-tox)
4. [Testowanie w wielu środowiskach](#testowanie-w-wielu-środowiskach)
5. [Relacja z CI](#relacja-z-ci)
6. [Relacja z `pytest`, `ruff`, `mypy`](#relacja-z-pytest-ruff-mypy)
7. [Kiedy `tox` ma sens](#kiedy-tox-ma-sens)
8. [Typowe błędy początkujących](#typowe-błędy-początkujących)
9. [Praktyczne przykłady](#praktyczne-przykłady)
10. [Dobre praktyki](#dobre-praktyki)
11. [Podsumowanie](#podsumowanie)
12. [Mini ściąga](#mini-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

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
- type checking.

---

## Po co używać `tox`

Bo pomaga:

- sprawdzać projekt w powtarzalny sposób,
- testować wiele wersji Pythona,
- uniezależnić lokalne checki od ręcznego odpalania wszystkiego osobno.

---

## Testowanie w wielu środowiskach

To największa zaleta `tox`.

Możesz sprawdzić, czy projekt działa:

- na Pythonie 3.11,
- na Pythonie 3.12,
- na Pythonie 3.13,

albo w różnych zestawach zależności.

---

## Relacja z CI

`tox` nie zastępuje CI.

Dobrze współpracuje z CI, bo daje jeden spójny sposób uruchamiania checków lokalnie i w pipeline.

---

## Relacja z `pytest`, `ruff`, `mypy`

`tox` nie testuje sam z siebie logiki aplikacji.

On raczej orkiestruje narzędzia takie jak:

- `pytest`,
- `ruff`,
- `mypy`.

---

## Kiedy `tox` ma sens

Szczególnie gdy:

- rozwijasz bibliotekę,
- wspierasz wiele wersji Pythona,
- chcesz mieć powtarzalne środowiska checków.

---

## Typowe błędy początkujących

- używanie `tox` bez realnej potrzeby,
- zbyt skomplikowana konfiguracja na start,
- traktowanie go jako zamiennika testów,
- brak spójności między tym, co robi lokalnie `tox`, a tym, co robi CI.

---

## Praktyczne przykłady

### Kiedy warto

- biblioteka open source,
- narzędzie używane na kilku wersjach Pythona.

### Kiedy niekoniecznie

- bardzo mały projekt wewnętrzny z jedną wersją Pythona i prostym workflow.

---

## Dobre praktyki

- używaj `tox`, gdy daje realną wartość,
- trzymaj konfigurację możliwie prostą,
- mapuj środowiska na konkretne cele,
- utrzymuj zgodność między lokalnym workflow i CI.

---

## Podsumowanie

`tox` to ważne narzędzie profesjonalnego ekosystemu Python, szczególnie dla projektów wymagających wielu środowisk testowych.

---

## Mini ściąga

Najważniejsze:

- `tox` orkiestruje checki,
- świetnie nadaje się do wielu wersji Pythona,
- dobrze współpracuje z CI.

---

## Ćwiczenia

1. Wyjaśnij, po co testować projekt w wielu środowiskach.
2. Wyjaśnij relację `tox` i CI.
3. Wskaż projekt, gdzie `tox` ma sens.
4. Wskaż projekt, gdzie może być zbędny.
5. Wyjaśnij, czemu `tox` nie zastępuje testów.

---

## Przykładowe rozwiązania

### 1. Po co wiele środowisk

Żeby sprawdzić zgodność projektu z różnymi wersjami Pythona lub różnymi zestawami zależności.

### 2. `tox` i CI

`tox` daje spójny lokalny workflow, który CI może później uruchamiać automatycznie.

### 3. Gdzie ma sens

W bibliotece wspierającej kilka wersji interpretera.

### 4. Gdzie zbędny

W małym projekcie z jedną wersją Pythona i prostymi checkami.

### 5. Czemu nie zastępuje testów

Bo sam nie jest frameworkiem testowym, tylko uruchamia inne narzędzia.
