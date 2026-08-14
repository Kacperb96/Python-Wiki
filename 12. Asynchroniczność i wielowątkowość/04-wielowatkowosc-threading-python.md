# Wielowątkowość w Pythonie — `threading`

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co używać wątków](#po-co-używać-wątków)
3. [Wątek a proces](#wątek-a-proces)
4. [Kiedy `threading` ma sens](#kiedy-threading-ma-sens)
5. [GIL i jego znaczenie](#gil-i-jego-znaczenie)
6. [Tworzenie wątku](#tworzenie-wątku)
7. [`Thread` i `target`](#thread-i-target)
8. [`start()` i `join()`](#start-i-join)
9. [Współdzielona pamięć](#współdzielona-pamięć)
10. [Race condition](#race-condition)
11. [`Lock`](#lock)
12. [`RLock`, `Event`, `Semaphore`](#rlock-event-semaphore)
13. [Wątki daemon](#wątki-daemon)
14. [`ThreadPoolExecutor`](#threadpoolexecutor)
15. [Typowe błędy początkujących](#typowe-błędy-początkujących)
16. [Praktyczne przykłady](#praktyczne-przykłady)
17. [Dobre praktyki](#dobre-praktyki)
18. [Podsumowanie](#podsumowanie)
19. [Mini ściąga](#mini-ściąga)
20. [Ćwiczenia](#ćwiczenia)
21. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Wielowątkowość pozwala uruchomić wiele ścieżek wykonania w obrębie jednego procesu.

W Pythonie najczęściej korzysta się z modułu `threading`.

Wątki są przydatne przede wszystkim tam, gdzie program:

- dużo czeka,
- obsługuje I/O,
- komunikuje się z siecią,
- pracuje z plikami,
- reaguje na wiele zdarzeń.

---

## Po co używać wątków

Wątki pomagają wtedy, gdy jedna część programu czeka, a inna może w tym czasie robić coś pożytecznego.

Przykłady:

- pobieranie plików,
- obsługa wielu klientów,
- praca z kolejkami,
- zadania w tle w aplikacji desktopowej,
- równoległe wywołania bibliotek blokujących.

---

## Wątek a proces

Wątek:

- działa wewnątrz procesu,
- współdzieli pamięć z innymi wątkami tego procesu,
- jest lżejszy od procesu.

Proces:

- ma własną przestrzeń pamięci,
- jest bardziej odizolowany,
- lepiej nadaje się do ciężkich obliczeń CPU-bound.

---

## Kiedy `threading` ma sens

Najczęściej przy zadaniach I/O-bound.

Na przykład:

- requesty sieciowe blokującą biblioteką,
- operacje na plikach,
- czekanie na urządzenia zewnętrzne,
- integracje z kodem, który nie ma wersji async.

---

## GIL i jego znaczenie

W CPythonie istnieje GIL, czyli Global Interpreter Lock.

W uproszczeniu oznacza to, że w danym momencie tylko jeden wątek wykonuje kod Pythona w interpreterze.

Skutek:

- wątki nie dają zwykle realnego przyspieszenia dla czysto CPU-bound kodu Pythona,
- ale nadal są bardzo użyteczne dla I/O-bound.

To jedna z najważniejszych rzeczy do zapamiętania.

---

## Tworzenie wątku

Najprostszy przykład:

```python
import threading

def praca():
    print("watek dziala")

t = threading.Thread(target=praca)
t.start()
t.join()
```

---

## `Thread` i `target`

`target` to funkcja, którą ma wykonać wątek.

Możesz przekazać argumenty:

```python
import threading

def powitanie(imie):
    print(f"Czesc, {imie}")

t = threading.Thread(target=powitanie, args=("Anna",))
t.start()
t.join()
```

---

## `start()` i `join()`

`start()`:

- uruchamia wątek.

`join()`:

- każe głównemu wątkowi poczekać, aż tamten się skończy.

Bez `join()` program może pójść dalej i zakończyć się wcześniej, niż oczekujesz.

---

## Współdzielona pamięć

Wątki w tym samym procesie widzą te same obiekty w pamięci.

To wygodne, ale ryzykowne.

Jeśli kilka wątków modyfikuje wspólny stan, łatwo o błędy trudne do odtworzenia.

---

## Race condition

Race condition to sytuacja, gdy wynik zależy od niekontrolowanej kolejności wykonania wątków.

Przykład problemu:

```python
import threading

licznik = 0

def zwieksz():
    global licznik
    for _ in range(100000):
        licznik += 1
```

Jeśli wiele wątków robi to naraz, wynik może być nieprzewidywalny.

---

## `Lock`

`Lock` pozwala zabezpieczyć sekcję krytyczną.

```python
import threading

licznik = 0
lock = threading.Lock()

def zwieksz():
    global licznik
    for _ in range(100000):
        with lock:
            licznik += 1
```

Dzięki temu tylko jeden wątek naraz modyfikuje chroniony fragment.

---

## `RLock`, `Event`, `Semaphore`

### `RLock`

Wersja locka, którą ten sam wątek może zablokować wielokrotnie.

### `Event`

Służy do sygnalizacji między wątkami.

### `Semaphore`

Pozwala ograniczyć liczbę wątków wchodzących jednocześnie do danego obszaru.

To bardzo praktyczne narzędzia synchronizacji.

---

## Wątki daemon

Wątek daemon działa w tle i nie blokuje zakończenia programu.

```python
t = threading.Thread(target=praca, daemon=True)
```

Użyteczne dla pomocniczych zadań, ale trzeba uważać, bo taki wątek może zostać brutalnie przerwany przy zamykaniu procesu.

---

## `ThreadPoolExecutor`

W praktyce często wygodniej używać puli wątków niż ręcznie zarządzać każdym wątkiem.

```python
from concurrent.futures import ThreadPoolExecutor

def kwadrat(x):
    return x * x

with ThreadPoolExecutor(max_workers=4) as executor:
    wyniki = list(executor.map(kwadrat, [1, 2, 3, 4]))
    print(wyniki)
```

To częsty wzorzec w realnych projektach.

---

## Typowe błędy początkujących

- używanie wątków do ciężkich obliczeń CPU-bound z oczekiwaniem dużego przyspieszenia,
- brak synchronizacji wspólnego stanu,
- tworzenie zbyt wielu wątków,
- zapominanie o `join()`,
- trudne do debugowania side effecty między wątkami.

---

## Praktyczne przykłady

### Dwa wątki

```python
import threading
import time

def praca(nazwa):
    for i in range(3):
        print(nazwa, i)
        time.sleep(0.5)

t1 = threading.Thread(target=praca, args=("A",))
t2 = threading.Thread(target=praca, args=("B",))

t1.start()
t2.start()

t1.join()
t2.join()
```

### `Event`

```python
import threading
import time

event = threading.Event()

def worker():
    print("czekam na sygnal")
    event.wait()
    print("ruszam")

t = threading.Thread(target=worker)
t.start()

time.sleep(1)
event.set()
t.join()
```

---

## Dobre praktyki

- używaj wątków głównie do I/O-bound,
- minimalizuj współdzielony stan,
- sekcje krytyczne chroń lockami,
- rozważ `ThreadPoolExecutor` zamiast ręcznej orkiestracji,
- projektuj kod tak, by dało się go debugować i testować.

---

## Podsumowanie

`threading` jest bardzo przydatny, ale wymaga ostrożności.

Najważniejsze rzeczy to:

- rozumieć GIL,
- wiedzieć, kiedy wątki pomagają,
- umieć synchronizować dostęp do wspólnego stanu,
- nie komplikować rozwiązania bardziej, niż to potrzebne.

---

## Mini ściąga

```python
import threading

def praca():
    print("dzialam")

t = threading.Thread(target=praca)
t.start()
t.join()
```

Pamiętaj:

- `start()` uruchamia wątek,
- `join()` czeka na jego koniec,
- `Lock` chroni wspólny stan,
- GIL ogranicza zysk dla CPU-bound,
- `ThreadPoolExecutor` bywa wygodniejszy.

---

## Ćwiczenia

1. Uruchom dwie funkcje w osobnych wątkach.
2. Przekaż argument do funkcji uruchamianej w wątku.
3. Zaimplementuj licznik współdzielony przez dwa wątki i zabezpiecz go lockiem.
4. Użyj `Event`, aby jeden wątek czekał na sygnał od drugiego.
5. Zastosuj `ThreadPoolExecutor` do przetworzenia listy liczb.

---

## Przykładowe rozwiązania

### 1. Dwa wątki

```python
import threading

def praca(nazwa):
    print(f"pracuje {nazwa}")

t1 = threading.Thread(target=praca, args=("A",))
t2 = threading.Thread(target=praca, args=("B",))

t1.start()
t2.start()
t1.join()
t2.join()
```

### 2. Argument

```python
import threading

def powitaj(imie):
    print(f"Czesc {imie}")

t = threading.Thread(target=powitaj, args=("Ola",))
t.start()
t.join()
```

### 3. Licznik z lockiem

```python
import threading

licznik = 0
lock = threading.Lock()

def zwieksz():
    global licznik
    for _ in range(10000):
        with lock:
            licznik += 1
```

### 4. `Event`

```python
import threading

event = threading.Event()

def worker():
    event.wait()
    print("start")
```

### 5. `ThreadPoolExecutor`

```python
from concurrent.futures import ThreadPoolExecutor

def kwadrat(x):
    return x * x

with ThreadPoolExecutor(max_workers=3) as executor:
    print(list(executor.map(kwadrat, [1, 2, 3, 4])))
```
