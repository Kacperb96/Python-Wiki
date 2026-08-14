# `subprocess` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co używać `subprocess`](#po-co-używać-subprocess)
3. [`subprocess.run()`](#subprocessrun)
4. [Przechwytywanie wyjścia](#przechwytywanie-wyjścia)
5. [Kody wyjścia](#kody-wyjścia)
6. [`check=True`](#checktrue)
7. [Przekazywanie argumentów](#przekazywanie-argumentów)
8. [`shell=True` i ostrożność](#shelltrue-i-ostrożność)
9. [`Popen`](#popen)
10. [Timeouty](#timeouty)
11. [Typowe błędy początkujących](#typowe-błędy-początkujących)
12. [Praktyczne przykłady](#praktyczne-przykłady)
13. [Dobre praktyki](#dobre-praktyki)
14. [Podsumowanie](#podsumowanie)
15. [Mini ściąga](#mini-ściąga)
16. [Ćwiczenia](#ćwiczenia)
17. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`subprocess` pozwala uruchamiać zewnętrzne programy z poziomu Pythona.

To bardzo przydatne w skryptach automatyzujących, integracjach z CLI i narzędziach developerskich.

---

## Po co używać `subprocess`

Gdy chcesz:

- uruchomić komendę systemową,
- pobrać wynik z programu,
- zautomatyzować pracę z narzędziami CLI,
- kontrolować kody wyjścia.

---

## `subprocess.run()`

Najczęstszy punkt wejścia:

```python
import subprocess

subprocess.run(["ls", "-l"])
```

Najlepiej przekazywać argumenty jako listę.

---

## Przechwytywanie wyjścia

```python
import subprocess

result = subprocess.run(
    ["echo", "hello"],
    capture_output=True,
    text=True
)

print(result.stdout)
```

---

## Kody wyjścia

Wynik ma m.in. `returncode`.

```python
import subprocess

result = subprocess.run(["python", "--version"], capture_output=True, text=True)
print(result.returncode)
```

---

## `check=True`

Jeśli chcesz, aby błąd uruchomił wyjątek:

```python
import subprocess

subprocess.run(["false"], check=True)
```

To rzuci `CalledProcessError`, gdy komenda zakończy się niepowodzeniem.

---

## Przekazywanie argumentów

Najbezpieczniej:

```python
subprocess.run(["python", "script.py", "--name", "Anna"])
```

To lepsze niż ręczne sklejanie stringa polecenia.

---

## `shell=True` i ostrożność

`shell=True` bywa wygodne, ale jest ryzykowne, szczególnie przy danych pochodzących od użytkownika.

Jeśli nie musisz, unikaj tego trybu.

---

## `Popen`

`Popen` daje większą kontrolę nad procesem.

Jest przydatne, gdy:

- chcesz zarządzać procesem dłużej,
- komunikujesz się z nim strumieniowo,
- potrzebujesz bardziej zaawansowanego sterowania.

Na start zwykle wystarczy `run()`.

---

## Timeouty

```python
import subprocess

subprocess.run(["sleep", "10"], timeout=1)
```

To przydatne, gdy zewnętrzne polecenie może się zawiesić.

---

## Typowe błędy początkujących

- ręczne sklejanie poleceń jako string, gdy wystarczy lista argumentów,
- brak obsługi błędów,
- nieświadome używanie `shell=True`,
- brak timeoutu dla potencjalnie długich komend.

---

## Praktyczne przykłady

### Odczyt wersji Pythona

```python
import subprocess

result = subprocess.run(
    ["python", "--version"],
    capture_output=True,
    text=True
)
print(result.stdout or result.stderr)
```

### Bezpieczne uruchomienie komendy

```python
import subprocess

result = subprocess.run(
    ["echo", "Raport gotowy"],
    capture_output=True,
    text=True,
    check=True
)
print(result.stdout)
```

---

## Dobre praktyki

- preferuj `subprocess.run()` do prostych przypadków,
- przekazuj argumenty jako listę,
- używaj `check=True`, gdy błąd ma przerwać przepływ,
- ustawiaj timeout dla ryzykownych poleceń,
- unikaj `shell=True`, jeśli nie jest konieczne.

---

## Podsumowanie

`subprocess` to podstawowe narzędzie do łączenia Pythona ze światem zewnętrznych programów.

Najważniejsze jest bezpieczne przekazywanie argumentów i rozsądna obsługa błędów.

---

## Mini ściąga

```python
import subprocess

result = subprocess.run(
    ["echo", "hello"],
    capture_output=True,
    text=True,
    check=True
)

print(result.stdout)
```

Najważniejsze:

- `run()` uruchamia komendę,
- `capture_output=True` przechwytuje stdout i stderr,
- `text=True` daje string zamiast bajtów,
- `check=True` rzuca wyjątek przy błędzie,
- `timeout=` ogranicza czas działania.

---

## Ćwiczenia

1. Uruchom prostą komendę systemową.
2. Przechwyć wynik `echo`.
3. Sprawdź kod wyjścia procesu.
4. Użyj `check=True`.
5. Dodaj timeout do komendy.

---

## Przykładowe rozwiązania

### 1. Prosta komenda

```python
import subprocess

subprocess.run(["echo", "hej"])
```

### 2. Przechwycenie wyjścia

```python
import subprocess

result = subprocess.run(["echo", "hej"], capture_output=True, text=True)
print(result.stdout)
```

### 3. Kod wyjścia

```python
import subprocess

result = subprocess.run(["python", "--version"], capture_output=True, text=True)
print(result.returncode)
```

### 4. `check=True`

```python
import subprocess

subprocess.run(["echo", "ok"], check=True)
```

### 5. Timeout

```python
import subprocess

subprocess.run(["sleep", "1"], timeout=2)
```
