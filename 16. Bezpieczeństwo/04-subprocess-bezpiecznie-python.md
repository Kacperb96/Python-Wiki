# Bezpieczne użycie `subprocess` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Dlaczego `subprocess` bywa ryzykowny](#dlaczego-subprocess-bywa-ryzykowny)
3. [Lista argumentów vs string polecenia](#lista-argumentów-vs-string-polecenia)
4. [`shell=True` i zagrożenia](#shelltrue-i-zagrożenia)
5. [Dane od użytkownika](#dane-od-użytkownika)
6. [Timeouty i kontrola procesu](#timeouty-i-kontrola-procesu)
7. [Kody wyjścia i błędy](#kody-wyjścia-i-błędy)
8. [Typowe błędy początkujących](#typowe-błędy-początkujących)
9. [Praktyczne przykłady](#praktyczne-przykłady)
10. [Dobre praktyki](#dobre-praktyki)
11. [Podsumowanie](#podsumowanie)
12. [Mini ściąga](#mini-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`subprocess` jest bardzo przydatny, ale przy złym użyciu może prowadzić do poważnych problemów bezpieczeństwa.

Szczególnie niebezpieczne jest łączenie go z danymi od użytkownika bez kontroli.

---

## Dlaczego `subprocess` bywa ryzykowny

Bo uruchamia zewnętrzne procesy systemowe.

Jeśli źle zbudujesz polecenie, możesz dopuścić do:

- command injection,
- niekontrolowanego wykonania poleceń,
- nieprzewidzianych skutków ubocznych.

---

## Lista argumentów vs string polecenia

Bezpieczniejszy wzorzec:

```python
subprocess.run(["ls", "-l"])
```

Mniej bezpieczny wzorzec:

```python
subprocess.run("ls -l", shell=True)
```

Lista argumentów zwykle daje dużo lepszą kontrolę.

---

## `shell=True` i zagrożenia

`shell=True` bywa wygodne, ale zwiększa ryzyko, zwłaszcza gdy do komendy trafiają dane z zewnątrz.

Jeśli nie musisz go używać, zwykle lepiej go unikać.

---

## Dane od użytkownika

To najważniejsza zasada:

nie sklejaj komend z niezweryfikowanym inputem użytkownika.

To klasyczny punkt wejścia dla command injection.

---

## Timeouty i kontrola procesu

Nawet bez aspektu injection warto kontrolować:

- czas działania procesu,
- błędy,
- wynik wykonania.

To poprawia odporność aplikacji.

---

## Kody wyjścia i błędy

Trzeba sprawdzać:

- `returncode`,
- wyjątki,
- sytuacje niepowodzenia.

Bez tego łatwo nie zauważyć, że wywołanie systemowe się nie udało.

---

## Typowe błędy początkujących

- `shell=True` bez potrzeby,
- składanie polecenia z danych użytkownika,
- brak timeoutu,
- brak obsługi błędów i kodu wyjścia.

---

## Praktyczne przykłady

### Bezpieczniej

```python
import subprocess

subprocess.run(["echo", "hello"], check=True)
```

### Ryzykownie

```python
import subprocess

name = input("Podaj nazwe: ")
subprocess.run(f"echo {name}", shell=True)
```

---

## Dobre praktyki

- przekazuj argumenty jako listę,
- unikaj `shell=True`, jeśli nie jest konieczne,
- nie sklejaj komend z inputem użytkownika,
- ustawiaj timeout tam, gdzie proces może się zawiesić,
- sprawdzaj błędy i kody wyjścia.

---

## Podsumowanie

Bezpieczne użycie `subprocess` to jeden z najważniejszych praktycznych tematów bezpieczeństwa w Pythonie.

Tu małe zaniedbanie może mieć bardzo duże skutki.

---

## Mini ściąga

Najważniejsze:

- preferuj listę argumentów,
- ostrożnie z `shell=True`,
- nie przekazuj nieufnego inputu do komendy,
- kontroluj błędy i timeouty.

---

## Ćwiczenia

1. Wyjaśnij, czemu lista argumentów jest bezpieczniejsza niż string.
2. Wyjaśnij ryzyko `shell=True`.
3. Podaj przykład command injection.
4. Wyjaśnij, po co używać timeoutu.
5. Wyjaśnij, czemu trzeba sprawdzać kod wyjścia procesu.

---

## Przykładowe rozwiązania

### 1. Lista argumentów

Bo ogranicza ryzyko błędnej interpretacji polecenia przez shell.

### 2. `shell=True`

Może otworzyć drogę do wykonania niechcianych poleceń, zwłaszcza przy danych zewnętrznych.

### 3. Command injection

Sytuacja, gdy użytkownik przemyca do polecenia dodatkowe komendy systemowe.

### 4. Timeout

Żeby proces nie wisiał bez końca.

### 5. Kod wyjścia

Bo mówi, czy proces zakończył się sukcesem czy błędem.
