# Wirtualne środowiska w Pythonie — `venv`, `pipenv`, `poetry`

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co istnieją wirtualne środowiska](#po-co-istnieją-wirtualne-środowiska)
3. [Problem bez wirtualnych środowisk](#problem-bez-wirtualnych-środowisk)
4. [Czym jest wirtualne środowisko](#czym-jest-wirtualne-środowisko)
5. [`venv`](#venv)
6. [Tworzenie środowiska `venv`](#tworzenie-środowiska-venv)
7. [Aktywacja i dezaktywacja](#aktywacja-i-dezaktywacja)
8. [Instalowanie pakietów w `venv`](#instalowanie-pakietów-w-venv)
9. [`pipenv`](#pipenv)
10. [`poetry`](#poetry)
11. [Różnice między `venv`, `pipenv` i `poetry`](#różnice-między-venv-pipenv-i-poetry)
12. [Które narzędzie wybrać](#które-narzędzie-wybrać)
13. [Dobre praktyki pracy ze środowiskami](#dobre-praktyki-pracy-ze-środowiskami)
14. [Typowe błędy początkujących](#typowe-błędy-początkujących)
15. [Praktyczne przykłady](#praktyczne-przykłady)
16. [Podsumowanie](#podsumowanie)
17. [Mini ściąga](#mini-ściąga)
18. [Ćwiczenia](#ćwiczenia)
19. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Wirtualne środowiska to jedna z podstaw profesjonalnej pracy w Pythonie.

Jeśli ich nie używasz, bardzo szybko możesz wpaść w problemy typu:

- „u mnie działa, u Ciebie nie działa”,
- konflikt wersji bibliotek,
- bałagan w globalnie zainstalowanych pakietach,
- trudności z odtworzeniem projektu na innym komputerze.

Dlatego praktycznie każdy sensowny projekt Pythona powinien działać w osobnym środowisku.

---

## Po co istnieją wirtualne środowiska

Najprościej:

wirtualne środowisko pozwala mieć osobny zestaw bibliotek dla konkretnego projektu.

To oznacza, że:

- projekt A może mieć `requests==2.x`,
- projekt B może mieć inną wersję,
- oba projekty nie przeszkadzają sobie nawzajem.

---

## Problem bez wirtualnych środowisk

Jeśli instalujesz wszystko globalnie:

- wszystkie projekty dzielą te same biblioteki,
- aktualizacja jednej biblioteki może popsuć inny projekt,
- trudniej kontrolować wersje,
- środowisko szybko robi się nieczytelne.

---

## Czym jest wirtualne środowisko

To odizolowane środowisko Pythona dla konkretnego projektu.

Ma własne:

- pakiety,
- `pip`,
- ścieżki wykonywania,
- często własną konfigurację.

---

## `venv`

`venv` to wbudowane narzędzie Pythona do tworzenia wirtualnych środowisk.

Jest najprostsze i bardzo często w zupełności wystarcza.

Nie wymaga dodatkowej instalacji, jeśli masz współczesnego Pythona.

---

## Tworzenie środowiska `venv`

Typowo:

```bash
python -m venv .venv
```

albo:

```bash
python3 -m venv .venv
```

To utworzy katalog `.venv` z izolowanym środowiskiem.

---

## Aktywacja i dezaktywacja

Na Linux/macOS:

```bash
source .venv/bin/activate
```

Na Windows:

```bash
.venv\Scripts\activate
```

Wyjście ze środowiska:

```bash
deactivate
```

---

## Instalowanie pakietów w `venv`

Po aktywacji środowiska:

```bash
pip install requests
```

Pakiet trafi do tego konkretnego środowiska, a nie do globalnego Pythona.

---

## `pipenv`

`pipenv` to narzędzie, które łączy:

- zarządzanie środowiskiem,
- zarządzanie zależnościami.

Tworzy pliki:

- `Pipfile`
- `Pipfile.lock`

Przez pewien czas było bardzo popularne, dziś nadal jest używane, choć często ustępuje miejsca `poetry`.

---

## `poetry`

`poetry` to nowoczesne narzędzie do:

- zarządzania zależnościami,
- publikowania pakietów,
- zarządzania środowiskiem.

Używa głównie:

- `pyproject.toml`

To dziś bardzo popularny wybór w nowych projektach.

---

## Różnice między `venv`, `pipenv` i `poetry`

### `venv`

- proste,
- wbudowane,
- tylko środowisko,
- zależności kontrolujesz zwykle przez `pip` i `requirements.txt`.

### `pipenv`

- łączy środowisko i zależności,
- korzysta z `Pipfile`.

### `poetry`

- bardziej rozbudowane,
- nowocześniejszy workflow,
- dobre do większych projektów i bibliotek.

---

## Które narzędzie wybrać

### Jeśli zaczynasz

`venv` + `pip` to bardzo dobry start.

### Jeśli chcesz nowocześniejsze zarządzanie projektem

`poetry` jest bardzo sensownym wyborem.

### Jeśli projekt już używa `pipenv`

Najczęściej najlepiej trzymać się konwencji projektu.

---

## Dobre praktyki pracy ze środowiskami

- używaj osobnego środowiska dla każdego projektu,
- nie wrzucaj katalogu środowiska do repozytorium,
- dodaj `.venv/` do `.gitignore`,
- trzymaj jawny opis zależności,
- nie instaluj przypadkowych rzeczy globalnie bez potrzeby.

---

## Typowe błędy początkujących

- brak wirtualnego środowiska,
- aktywowanie nie tego środowiska co trzeba,
- mieszanie globalnego `pip` z lokalnym środowiskiem,
- commitowanie całego `.venv`,
- brak pliku z zależnościami.

---

## Praktyczne przykłady

### `venv`

```bash
python -m venv .venv
source .venv/bin/activate
pip install pytest
```

### zapis zależności

```bash
pip freeze > requirements.txt
```

### `poetry`

Przykładowo:

```bash
poetry init
poetry add requests
poetry shell
```

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- wirtualne środowiska izolują zależności projektu,
- `venv` to podstawowe, wbudowane rozwiązanie,
- `pipenv` i `poetry` dają bardziej rozbudowane workflow,
- profesjonalna praca w Pythonie praktycznie zawsze powinna używać środowiska per projekt.

---

## Mini ściąga

```bash
python -m venv .venv
source .venv/bin/activate
deactivate
pip freeze > requirements.txt
```

---

## Ćwiczenia

### Ćwiczenie 1

Utwórz lokalne środowisko `.venv`.

### Ćwiczenie 2

Zainstaluj w nim `pytest`.

### Ćwiczenie 3

Wygeneruj `requirements.txt`.

---

## Przykładowe rozwiązania

```bash
python -m venv .venv
source .venv/bin/activate
pip install pytest
pip freeze > requirements.txt
```
