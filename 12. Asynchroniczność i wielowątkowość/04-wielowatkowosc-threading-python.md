# Wielowątkowość w Pythonie — `threading`

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co używać wątków](#po-co-używać-wątków)
3. [Wątek a proces](#wątek-a-proces)
4. [Kiedy `threading` ma sens](#kiedy-threading-ma-sens)
5. [GIL i jego znaczenie](#gil-i-jego-znaczenie)
6. [Tworzenie wątku](#tworzenie-wątku)
7. [`start()` i `join()`](#start-i-join)
8. [Przykład z outputem](#przykład-z-outputem)
9. [Współdzielona pamięć](#współdzielona-pamięć)
10. [Race condition](#race-condition)
11. [`Lock`](#lock)
12. [`Event`, `Semaphore`, `ThreadPoolExecutor`](#event-semaphore-threadpoolexecutor)
13. [Kiedy nie używać wątków](#kiedy-nie-używać-wątków)
14. [Typowe błędy początkujących](#typowe-błędy-początkujących)
15. [Praktyczna ściąga](#praktyczna-ściąga)
16. [Ćwiczenia](#ćwiczenia)
17. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

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

- pobieranie plików blokującą biblioteką,
- obsługa wielu klientów,
- zadania w tle w aplikacji desktopowej,
- integracje z kodem, który nie ma wersji async.

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
- biblioteki, które nie mają API async.

---

## GIL i jego znaczenie

W CPythonie istnieje GIL, czyli Global Interpreter Lock.

W uproszczeniu oznacza to, że w danym momencie tylko jeden wątek wykonuje kod Pythona w interpreterze.

Skutek praktyczny:

- wątki zwykle nie dają dużego zysku dla czysto CPU-bound kodu Pythona,
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

## `start()` i `join()`

`start()`:

- uruchamia wątek.

`join()`:

- każe głównemu wątkowi poczekać, aż tamten się skończy.

Bez `join()` program może pójść dalej szybciej, niż oczekujesz.

---

## Przykład z outputem

```python
import threading
import time


def worker(nazwa, delay):
    print(f"start {nazwa}")
    time.sleep(delay)
    print(f"koniec {nazwa}")


t1 = threading.Thread(target=worker, args=("A", 1))
t2 = threading.Thread(target=worker, args=("B", 1))

t1.start()
t2.start()

t1.join()
t2.join()

print("wszystkie watki zakonczone")
```

Przykładowy output:

```text
start A
start B
koniec A
koniec B
wszystkie watki zakonczone
```

Najważniejsze:

- oba wątki mogły działać przeplatanie,
- główny wątek czeka przez `join()`,
- to nie oznacza jeszcze pełnego przyspieszenia CPU-bound.

---

## Współdzielona pamięć

Wątki w tym samym procesie widzą te same obiekty w pamięci.

To wygodne, ale ryzykowne.

Jeśli kilka wątków modyfikuje wspólny stan, łatwo o błędy trudne do odtworzenia.

---

## Race condition

Race condition pojawia się wtedy, gdy wynik zależy od niekontrolowanej kolejności działań kilku wątków.

Przykład mentalny:

- dwa wątki zwiększają ten sam licznik,
- oba czytają starą wartość,
- oba zapisują nową,
- część aktualizacji może zniknąć.

---

## `Lock`

`Lock` pozwala chronić fragment krytyczny.

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

To zmniejsza ryzyko race condition.

---

## `Event`, `Semaphore`, `ThreadPoolExecutor`

### `Event`

Pomaga sygnalizować między wątkami, że coś już się wydarzyło.

### `Semaphore`

Pozwala ograniczać liczbę jednoczesnych wejść do jakiegoś zasobu.

### `ThreadPoolExecutor`

To wygodniejszy sposób uruchamiania wielu zadań niż ręczne tworzenie każdego wątku osobno.

Jest bardzo praktyczny w codziennej pracy.

---

## Kiedy nie używać wątków

Wątki nie są najlepszym wyborem, gdy:

- problem jest czysto CPU-bound,
- potrzebujesz realnego wykorzystania wielu rdzeni dla kodu Pythona,
- łatwiej byłoby użyć async albo procesów,
- synchronizacja stanu robi się bardzo złożona.

---

## Typowe błędy początkujących

- oczekiwanie, że wątki zawsze przyspieszą program,
- ignorowanie GIL,
- brak `join()`,
- modyfikowanie wspólnego stanu bez synchronizacji,
- używanie wątków tam, gdzie procesy albo async pasują lepiej.

---

## Praktyczna ściąga

### Prosty wątek

```python
t = threading.Thread(target=praca)
t.start()
t.join()
```

### Ochrona stanu

```python
with lock:
    ...
```

### Kiedy warto

- I/O-bound,
- blokujące biblioteki,
- zadania w tle.

---

## Ćwiczenia

1. Uruchom dwie funkcje w osobnych wątkach.
2. Dodaj `join()`.
3. Zaimplementuj współdzielony licznik.
4. Zabezpiecz go przez `Lock`.
5. Użyj `ThreadPoolExecutor` do kilku prostych zadań.
6. Wyjaśnij własnymi słowami, czemu GIL ma znaczenie.

---

## Najważniejsze do zapamiętania

- Wątki są szczególnie przydatne przy I/O-bound.
- Współdzielą pamięć, więc łatwo o problemy synchronizacyjne.
- GIL ogranicza sens wątków przy CPU-bound w CPythonie.
- `Lock` pomaga chronić wspólny stan.
- Nie każdy problem współbieżności powinien być rozwiązywany przez `threading`.
