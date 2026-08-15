# `concurrent.futures` w Pythonie

## Wprowadzenie

`concurrent.futures` daje prostszy interfejs do pracy z:

- wątkami,
- procesami,
- uruchamianiem wielu zadań przez executor.

To bardzo praktyczne, bo nie zawsze chcesz schodzić od razu do niższego poziomu `threading` albo `multiprocessing`.

Najczęściej używa się:

- `ThreadPoolExecutor`
- `ProcessPoolExecutor`

## Kiedy to ma sens

### `ThreadPoolExecutor`

Najczęściej dla:

- I/O-bound,
- wielu requestów,
- pracy z plikami,
- integracji z zewnętrznymi usługami,
- zadań blokujących, ale nie CPU-heavy.

### `ProcessPoolExecutor`

Najczęściej dla:

- CPU-bound,
- ciężkich obliczeń,
- zadań, które mają wykorzystać wiele rdzeni.

## Najprostszy `ThreadPoolExecutor`

```python
from concurrent.futures import ThreadPoolExecutor
import time


def task(n):
    time.sleep(1)
    return f"done {n}"


with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(task, i) for i in range(3)]

    for future in futures:
        print(future.result())
```

Output:

```text
done 0
done 1
done 2
```

## `submit()` i `Future`

`submit()` zwraca obiekt `Future`.

To obiekt reprezentujący wynik pracy, która:

- może już się skończyła,
- może właśnie trwa,
- może dopiero się wykona.

```python
from concurrent.futures import ThreadPoolExecutor
import time


def slow():
    time.sleep(1)
    return 123


with ThreadPoolExecutor() as executor:
    future = executor.submit(slow)
    print(future.result())
```

Output:

```text
123
```

## `map()`

To wygodniejszy wariant dla wielu danych.

```python
from concurrent.futures import ThreadPoolExecutor
import time


def square(x):
    time.sleep(0.5)
    return x * x


with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(square, [1, 2, 3, 4]))

print(results)
```

Output:

```python
[1, 4, 9, 16]
```

## `ThreadPoolExecutor` w praktyce

To bardzo naturalne, gdy masz wiele niezależnych zadań I/O-bound.

Przykład myślowy:

- 20 plików do odczytu,
- 30 requestów HTTP,
- 10 wolnych integracji.

Zamiast robić je jeden po drugim, możesz puścić je przez pulę wątków.

## `ProcessPoolExecutor`

```python
from concurrent.futures import ProcessPoolExecutor


def cube(x):
    return x ** 3


with ProcessPoolExecutor() as executor:
    results = list(executor.map(cube, [1, 2, 3, 4]))

print(results)
```

Output:

```python
[1, 8, 27, 64]
```

To narzędzie jest bliższe `multiprocessing`, ale daje wygodniejszy interfejs.

## `ThreadPoolExecutor` vs `ProcessPoolExecutor`

### Wątki

Lepsze, gdy:

- czekasz na I/O,
- program dużo stoi i czeka,
- zadania są blokujące, ale nie ciężkie CPU.

### Procesy

Lepsze, gdy:

- zadanie naprawdę liczy,
- chcesz ominąć ograniczenia GIL dla CPU-bound,
- praca jest intensywna obliczeniowo.

## `as_completed()`

Przydatne, gdy chcesz obrabiać wyniki w kolejności zakończenia, a nie w kolejności startu.

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time


def task(n):
    time.sleep(3 - n)
    return f"done {n}"


with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(task, i) for i in range(3)]

    for future in as_completed(futures):
        print(future.result())
```

Przykładowy output:

```text
done 2
done 1
done 0
```

## Mini case study

Masz 50 URL-i do pobrania.

Jeśli:

- nie chcesz od razu pisać pełnego async,
- biblioteka jest blokująca,
- zadania są niezależne,

to `ThreadPoolExecutor` jest bardzo praktycznym wyborem.

## Typowe błędy początkujących

### 1. Używanie `ThreadPoolExecutor` do ciężkiego CPU-bound

To zwykle nie daje tego efektu, którego oczekujesz.

### 2. Brak rozróżnienia I/O-bound vs CPU-bound

To kluczowa decyzja przy wyborze executora.

### 3. Zbyt wiele workerów bez namysłu

Więcej nie zawsze znaczy lepiej.

### 4. Zakładanie, że executor magicznie naprawia architekturę

To nadal tylko narzędzie. Trzeba wiedzieć, jaki problem rozwiązujesz.

## Dobre praktyki

- używaj `ThreadPoolExecutor` dla blokującego I/O,
- używaj `ProcessPoolExecutor` dla CPU-bound,
- zacznij od prostych przykładów z `map()` albo `submit()`,
- nie zgaduj: myśl o typie obciążenia,
- jeśli zadania są bardzo duże i systemowe, rozważ też kolejkę albo osobne workery.

## Zadania

1. Użyj `ThreadPoolExecutor` do uruchomienia kilku prostych zadań z `sleep`.
2. Użyj `executor.map()` do policzenia kwadratów.
3. Użyj `as_completed()` i pokaż kolejność zakończenia.
4. Zrób ten sam przykład przez `ProcessPoolExecutor`.
5. Opisz, kiedy wybrać `ThreadPoolExecutor`, a kiedy `ProcessPoolExecutor`.
