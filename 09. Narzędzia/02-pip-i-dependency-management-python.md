# `pip` i dependency management w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `pip`](#czym-jest-pip)
3. [Czym są zależności](#czym-są-zależności)
4. [Po co zarządzać zależnościami świadomie](#po-co-zarządzać-zależnościami-świadomie)
5. [Instalowanie pakietów](#instalowanie-pakietów)
6. [Usuwanie pakietów](#usuwanie-pakietów)
7. [Aktualizacja pakietów](#aktualizacja-pakietów)
8. [Sprawdzanie zainstalowanych pakietów](#sprawdzanie-zainstalowanych-pakietów)
9. [`requirements.txt`](#requirementstxt)
10. [`pip freeze`](#pip-freeze)
11. [Pinowanie wersji](#pinowanie-wersji)
12. [Semver i zakresy wersji](#semver-i-zakresy-wersji)
13. [Zależności bezpośrednie i pośrednie](#zależności-bezpośrednie-i-pośrednie)
14. [Dlaczego warto trzymać zależności jawnie](#dlaczego-warto-trzymać-zależności-jawnie)
15. [Konflikty wersji](#konflikty-wersji)
16. [Bezpieczne aktualizowanie zależności](#bezpieczne-aktualizowanie-zależności)
17. [Typowe błędy początkujących](#typowe-błędy-początkujących)
18. [Praktyczne przykłady](#praktyczne-przykłady)
19. [Dobre praktyki](#dobre-praktyki)
20. [Podsumowanie](#podsumowanie)
21. [Mini ściąga](#mini-ściąga)
22. [Ćwiczenia](#ćwiczenia)
23. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

W profesjonalnej pracy z Pythonem nie wystarczy tylko „zainstalować biblioteki”.

Trzeba jeszcze umieć:

- kontrolować wersje,
- zapisywać zależności projektu,
- odtwarzać środowisko na innym komputerze,
- unikać przypadkowych konfliktów.

To właśnie jest dependency management.

---

## Czym jest `pip`

`pip` to podstawowy menedżer pakietów w Pythonie.

Pozwala:

- instalować biblioteki,
- usuwać biblioteki,
- aktualizować biblioteki,
- zarządzać zestawem pakietów w środowisku.

---

## Czym są zależności

Zależności to biblioteki, których potrzebuje Twój projekt.

Na przykład:

- `requests`
- `pytest`
- `fastapi`
- `pandas`

Część z nich może zależeć od kolejnych bibliotek.

---

## Po co zarządzać zależnościami świadomie

Bo bez tego szybko pojawiają się problemy:

- projekt działa tylko u jednej osoby,
- po aktualizacji coś się psuje,
- nie wiadomo, jaka wersja biblioteki była potrzebna,
- wdrożenie na serwer jest niestabilne.

---

## Instalowanie pakietów

Najprościej:

```bash
pip install requests
```

Z konkretną wersją:

```bash
pip install requests==2.31.0
```

---

## Usuwanie pakietów

```bash
pip uninstall requests
```

---

## Aktualizacja pakietów

```bash
pip install --upgrade requests
```

Z tym trzeba uważać, bo aktualizacja może zmienić zachowanie projektu.

---

## Sprawdzanie zainstalowanych pakietów

```bash
pip list
```

albo:

```bash
pip freeze
```

To drugie częściej używa się do zapisu zależności.

Przykładowy wynik `pip list` może wyglądać tak:

```text
Package    Version
pytest     8.0.0
requests   2.31.0
```

---

## `requirements.txt`

To bardzo popularny plik z listą zależności projektu.

Przykład:

```txt
requests==2.31.0
pytest==8.0.0
fastapi==0.110.0
```

Instalacja:

```bash
pip install -r requirements.txt
```

---

## `pip freeze`

Pozwala zapisać aktualny stan pakietów:

```bash
pip freeze > requirements.txt
```

To wygodne, ale trzeba rozumieć, że zapisujesz nie tylko bezpośrednie biblioteki, ale też zależności pośrednie.

---

## Pinowanie wersji

Pinowanie oznacza zapisanie konkretnej wersji:

```txt
requests==2.31.0
```

To ważne, bo pomaga zachować powtarzalność środowiska.

---

## Semver i zakresy wersji

Czasem spotyka się różne sposoby określania wersji:

- `==`
- `>=`
- `<`
- `~=`

W praktyce początkującego najważniejsze jest zrozumienie, że:

- dokładna wersja daje większą powtarzalność,
- luźniejsze zakresy dają większą elastyczność, ale też więcej ryzyka.

---

## Zależności bezpośrednie i pośrednie

### Bezpośrednie

To te, które instalujesz świadomie.

### Pośrednie

To biblioteki wymagane przez Twoje biblioteki.

Na przykład instalujesz `fastapi`, ale ono samo ma swoje zależności.

---

## Dlaczego warto trzymać zależności jawnie

Bo projekt powinien dać się łatwo odtworzyć:

- na innym komputerze,
- w CI,
- na serwerze,
- po kilku miesiącach.

---

## Konflikty wersji

To sytuacja, gdy różne części projektu chcą różnych wersji tej samej biblioteki.

Wirtualne środowiska i świadome zarządzanie wersjami bardzo pomagają takie problemy ograniczyć.

---

## Bezpieczne aktualizowanie zależności

Dobra praktyka:

1. aktualizujesz zależność,
2. uruchamiasz testy,
3. sprawdzasz changelog,
4. upewniasz się, że nic się nie popsuło.

Nie warto aktualizować wszystkiego w ciemno.

---

## Typowe błędy początkujących

- brak `requirements.txt`,
- instalowanie globalne zamiast w środowisku,
- brak pinowania wersji,
- aktualizacja zależności bez testów,
- chaos między bibliotekami dev i produkcyjnymi.

### 6. Wrzucanie całego `pip freeze` bez zrozumienia, co tam jest

Warto wiedzieć, które pakiety są naprawdę Twoimi zależnościami bezpośrednimi.

---

## Praktyczne przykłady

```bash
pip install requests
pip install pytest
pip freeze > requirements.txt
pip install -r requirements.txt
```

### Pinowanie

```txt
pytest==8.0.0
requests==2.31.0
```

### Odtworzenie środowiska

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Efekt:

masz środowisko z tym samym zestawem pakietów, co w projekcie źródłowym.

---

## Dobre praktyki

- pracuj w wirtualnym środowisku,
- zapisuj zależności projektu,
- pinuj ważne wersje,
- testuj projekt po aktualizacji,
- utrzymuj porządek w zależnościach.

Praktyczna zasada:

jeśli projekt ma działać u kogoś innego niż Ty, zależności muszą być opisane jawnie i możliwe do odtworzenia.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- `pip` służy do zarządzania pakietami,
- dependency management to świadome zarządzanie zależnościami projektu,
- `requirements.txt` pomaga odtwarzać środowisko,
- wersje bibliotek trzeba kontrolować świadomie.

Najważniejsze do zapamiętania:

- samo `pip install` nie kończy tematu,
- zależności trzeba umieć odtworzyć,
- aktualizacje bez testów i bezmyślne zmiany wersji szybko prowadzą do problemów.

---

## Mini ściąga

```bash
pip install pakiet
pip uninstall pakiet
pip list
pip freeze
pip install -r requirements.txt
```

---

## Ćwiczenia

### Ćwiczenie 1

Zainstaluj `requests` i `pytest`.

### Ćwiczenie 2

Zapisz zależności do `requirements.txt`.

### Ćwiczenie 3

Zastanów się, dlaczego warto przypiąć wersję `pytest`.

---

## Przykładowe rozwiązania

```bash
pip install requests pytest
pip freeze > requirements.txt
```
