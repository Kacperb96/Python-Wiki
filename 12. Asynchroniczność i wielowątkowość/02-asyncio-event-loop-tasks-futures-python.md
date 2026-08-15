# `asyncio` w Pythonie — event loop, tasks, futures

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co istnieje `asyncio`](#po-co-istnieje-asyncio)
3. [Asynchroniczność a współbieżność](#asynchroniczność-a-współbieżność)
4. [Czym jest event loop](#czym-jest-event-loop)
5. [Jak działa event loop krok po kroku](#jak-działa-event-loop-krok-po-kroku)
6. [Coroutine](#coroutine)
7. [Task](#task)
8. [Future](#future)
9. [`asyncio.run()`](#asynciorun)
10. [`create_task()`](#create_task)
11. [`gather()`](#gather)
12. [Przykład z outputem](#przykład-z-outputem)
13. [Anulowanie zadań](#anulowanie-zadań)
14. [Timeouty](#timeouty)
15. [Typowe błędy początkujących](#typowe-błędy-początkujących)
16. [Praktyczna ściąga](#praktyczna-ściąga)
17. [Ćwiczenia](#ćwiczenia)
18. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

`asyncio` to standardowy moduł Pythona do programowania asynchronicznego.

Pozwala uruchamiać wiele operacji współbieżnie bez tworzenia wielu wątków.

Najlepiej sprawdza się tam, gdzie program dużo czeka:

- na sieć,
- na API,
- na bazę danych,
- na pliki,
- na inne operacje wejścia/wyjścia.

---

## Po co istnieje `asyncio`

W wielu programach procesor nie jest głównym problemem.

Problemem jest czekanie.

Na przykład:

- wysyłasz 100 zapytań HTTP,
- każde czeka 200 ms na odpowiedź,
- ale samo liczenie trwa bardzo krótko.

`asyncio` pozwala lepiej wykorzystać czas oczekiwania.

---

## Asynchroniczność a współbieżność

To nie jest dokładnie to samo co równoległość na wielu rdzeniach.

W `asyncio` zwykle masz:

- jeden wątek,
- jedną pętlę zdarzeń,
- wiele zadań przełączanych wtedy, gdy któreś czeka.

Czyli program nie robi wszystkiego naraz na wielu rdzeniach, ale bardzo sprawnie przeplata oczekujące operacje.

---

## Czym jest event loop

Event loop to serce `asyncio`.

To pętla, która:

- uruchamia coroutine,
- pilnuje tasków,
- sprawdza, które operacje są gotowe do wznowienia,
- oddaje sterowanie właściwym fragmentom kodu.

Można myśleć o niej jak o koordynatorze ruchu.

---

## Jak działa event loop krok po kroku

W uproszczeniu:

1. uruchamiasz program async,
2. event loop startuje,
3. uruchamia coroutine,
4. coroutine dochodzi do `await`,
5. oddaje sterowanie,
6. event loop uruchamia inne zadania,
7. gdy wynik jest gotowy, coroutine zostaje wznowiona.

To właśnie daje efekt współbieżności.

---

## Coroutine

Coroutine to funkcja zdefiniowana przez `async def`.

Przykład:

```python
async def pobierz_dane():
    return "gotowe"
```

Samo wywołanie takiej funkcji nie wykonuje jej od razu.

Zwraca obiekt coroutine.

---

## Task

Task to coroutine opakowana tak, aby event loop mógł ją planować i wykonywać.

Najczęściej tworzysz go tak:

```python
task = asyncio.create_task(moja_coroutine())
```

Task jest jednostką pracy zarządzaną przez `asyncio`.

---

## Future

`Future` reprezentuje wynik, który będzie dostępny później.

To obiekt bardziej niskiego poziomu.

W praktyce początkujący dużo częściej pracują z:

- coroutine,
- taskami,
- `await`,
- `gather()`.

Ważne jednak wiedzieć, że `Task` jest szczególnym rodzajem `Future`.

---

## `asyncio.run()`

Najprostszy sposób uruchomienia programu async:

```python
import asyncio


async def main():
    print("hello async")


asyncio.run(main())
```

To najczęstszy punkt wejścia do programu asynchronicznego.

---

## `create_task()`

`create_task()` pozwala uruchomić coroutine jako task zarządzany przez event loop.

Przykład:

```python
import asyncio


async def praca():
    await asyncio.sleep(1)
    return "gotowe"


async def main():
    task = asyncio.create_task(praca())
    print("task uruchomiony")
    wynik = await task
    print(wynik)


asyncio.run(main())
```

---

## `gather()`

`asyncio.gather()` pozwala poczekać na wiele awaitable naraz.

```python
wyniki = await asyncio.gather(a(), b(), c())
```

To bardzo częsta konstrukcja przy niezależnych requestach, pobieraniach i innych operacjach I/O.

---

## Przykład z outputem

```python
import asyncio


async def worker(nazwa, delay):
    print(f"start {nazwa}")
    await asyncio.sleep(delay)
    print(f"koniec {nazwa}")
    return nazwa


async def main():
    task1 = asyncio.create_task(worker("A", 1))
    task2 = asyncio.create_task(worker("B", 2))

    print("taski utworzone")

    wyniki = await asyncio.gather(task1, task2)
    print(wyniki)


asyncio.run(main())
```

Przykładowy output:

```text
taski utworzone
start A
start B
koniec A
koniec B
['A', 'B']
```

Co tu warto zauważyć:

- oba taski zostały uruchomione,
- event loop przeplata ich wykonanie,
- końcowy wynik wraca jako lista.

---

## Anulowanie zadań

Task można anulować.

```python
import asyncio


async def wolne_zadanie():
    try:
        await asyncio.sleep(10)
    except asyncio.CancelledError:
        print("zadanie anulowane")
        raise


async def main():
    task = asyncio.create_task(wolne_zadanie())
    await asyncio.sleep(1)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("main potwierdza anulowanie")


asyncio.run(main())
```

Przykładowy output:

```text
zadanie anulowane
main potwierdza anulowanie
```

---

## Timeouty

Czasem nie chcesz czekać zbyt długo.

```python
await asyncio.wait_for(zadanie(), timeout=2)
```

Jeśli zadanie nie skończy się w czasie, dostaniesz błąd timeoutu.

To bardzo przydatne przy sieci, bazach i integracjach.

---

## Typowe błędy początkujących

- tworzenie coroutine bez ich uruchomienia,
- mylenie taska z gotowym wynikiem,
- przekonanie, że `asyncio` daje automatycznie wiele rdzeni CPU,
- wrzucanie blokującego kodu do event loopa,
- tworzenie zbyt wielu tasków bez kontroli współbieżności.

---

## Praktyczna ściąga

### Start programu async

```python
asyncio.run(main())
```

### Task

```python
task = asyncio.create_task(praca())
```

### Wiele wyników

```python
wyniki = await asyncio.gather(a(), b())
```

### Timeout

```python
await asyncio.wait_for(zadanie(), timeout=2)
```

---

## Ćwiczenia

1. Napisz prosty program uruchamiany przez `asyncio.run()`.
2. Utwórz dwa taski przez `create_task()`.
3. Odbierz ich wyniki przez `gather()`.
4. Dodaj anulowanie zadania.
5. Dodaj timeout do wolnego zadania.
6. Wyjaśnij własnymi słowami rolę event loopa.

---

## Najważniejsze do zapamiętania

- Event loop zarządza wykonywaniem tasków async.
- Coroutine to nie to samo co task ani gotowy wynik.
- `create_task()` pozwala uruchomić coroutine jako jednostkę pracy event loopa.
- `gather()` służy do czekania na wiele zadań naraz.
- `asyncio` świetnie nadaje się do I/O-bound, ale nie rozwiązuje CPU-bound przez samą magię.
