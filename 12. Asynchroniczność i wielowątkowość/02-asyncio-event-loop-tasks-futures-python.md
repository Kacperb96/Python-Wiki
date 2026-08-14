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
10. [`await` i oddawanie sterowania](#await-i-oddawanie-sterowania)
11. [`create_task()`](#create_task)
12. [Uruchamianie wielu zadań naraz](#uruchamianie-wielu-zadań-naraz)
13. [`gather()`](#gather)
14. [Anulowanie zadań](#anulowanie-zadań)
15. [Timeouty](#timeouty)
16. [Typowe błędy początkujących](#typowe-błędy-początkujących)
17. [Praktyczne przykłady](#praktyczne-przykłady)
18. [Dobre praktyki](#dobre-praktyki)
19. [Podsumowanie](#podsumowanie)
20. [Mini ściąga](#mini-ściąga)
21. [Ćwiczenia](#ćwiczenia)
22. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

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

Gdyby robić to sekwencyjnie, program długo stoi bezczynnie.

`asyncio` pozwala wykorzystać ten czas lepiej.

---

## Asynchroniczność a współbieżność

To nie jest dokładnie to samo co równoległość.

W `asyncio` zwykle masz:

- jeden wątek,
- jedną pętlę zdarzeń,
- wiele zadań przełączanych wtedy, gdy któreś czeka.

Czyli program nie robi wszystkiego naraz na wielu rdzeniach, ale potrafi bardzo sprawnie przeplatać oczekujące operacje.

---

## Czym jest event loop

Event loop to serce `asyncio`.

To pętla, która:

- uruchamia coroutines,
- pilnuje zadań,
- sprawdza, które operacje są gotowe do wznowienia,
- przekazuje sterowanie odpowiednim fragmentom kodu.

Można myśleć o niej jak o koordynatorze ruchu.

---

## Jak działa event loop krok po kroku

W uproszczeniu:

1. uruchamiasz program asynchroniczny,
2. event loop startuje,
3. uruchamia coroutine,
4. coroutine dochodzi do `await`,
5. oddaje sterowanie,
6. event loop w tym czasie uruchamia inne zadania,
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

Najczęściej tworzy się ją przez:

```python
task = asyncio.create_task(moja_coroutine())
```

Task działa jak jednostka pracy zarządzana przez `asyncio`.

---

## Future

`Future` reprezentuje wynik, który będzie dostępny później.

To obiekt niskiego poziomu.

W praktyce początkujący częściej pracują z:

- coroutine,
- taskami,
- `await`,

a rzadziej bezpośrednio z `Future`.

Ważne jednak rozumieć, że `Task` jest szczególnym rodzajem `Future`.

---

## `asyncio.run()`

Najprostszy sposób uruchomienia programu asynchronicznego:

```python
import asyncio

async def main():
    print("start")

asyncio.run(main())
```

`asyncio.run()`:

- tworzy event loop,
- uruchamia `main()`,
- zamyka wszystko po zakończeniu.

---

## `await` i oddawanie sterowania

`await` oznacza:

"poczekaj na wynik tej operacji i w międzyczasie pozwól event loop robić inne rzeczy".

Przykład:

```python
import asyncio

async def main():
    print("przed")
    await asyncio.sleep(1)
    print("po")
```

`asyncio.sleep(1)` nie blokuje całego programu tak jak `time.sleep(1)`.

---

## `create_task()`

Jeśli napiszesz:

```python
await funkcja()
```

to po prostu czekasz na nią w tym miejscu.

Jeśli chcesz uruchomić zadanie współbieżnie:

```python
task = asyncio.create_task(funkcja())
```

To zadanie zacznie działać niezależnie, a ty możesz później zrobić:

```python
wynik = await task
```

---

## Uruchamianie wielu zadań naraz

Przykład:

```python
import asyncio

async def praca(n):
    await asyncio.sleep(1)
    return f"zadanie {n}"

async def main():
    task1 = asyncio.create_task(praca(1))
    task2 = asyncio.create_task(praca(2))

    wynik1 = await task1
    wynik2 = await task2

    print(wynik1, wynik2)

asyncio.run(main())
```

Oba zadania śpią współbieżnie, więc całość trwa około 1 sekundy, a nie 2.

---

## `gather()`

`asyncio.gather()` pozwala wygodnie czekać na wiele zadań jednocześnie.

```python
import asyncio

async def praca(n):
    await asyncio.sleep(1)
    return n * 10

async def main():
    wyniki = await asyncio.gather(
        praca(1),
        praca(2),
        praca(3),
    )
    print(wyniki)

asyncio.run(main())
```

Wynik:

```python
[10, 20, 30]
```

---

## Anulowanie zadań

Czasem zadanie trzeba zatrzymać.

```python
task.cancel()
```

W coroutine warto obsłużyć anulowanie:

```python
import asyncio

async def worker():
    try:
        await asyncio.sleep(10)
    except asyncio.CancelledError:
        print("zadanie anulowane")
        raise
```

To ważne przy sprzątaniu zasobów.

---

## Timeouty

Nie każda operacja powinna czekać w nieskończoność.

```python
import asyncio

async def wolna_operacja():
    await asyncio.sleep(5)

async def main():
    try:
        await asyncio.wait_for(wolna_operacja(), timeout=1)
    except asyncio.TimeoutError:
        print("przekroczono limit czasu")
```

---

## Typowe błędy początkujących

- mylenie `time.sleep()` z `asyncio.sleep()`,
- zapominanie o `await`,
- tworzenie tasków i nigdy na nie nieczekanie,
- mieszanie kodu blokującego z asynchronicznym,
- oczekiwanie, że `asyncio` przyspieszy kod CPU-bound.

---

## Praktyczne przykłady

### Prosty współbieżny licznik

```python
import asyncio

async def licz(nazwa):
    for i in range(3):
        print(nazwa, i)
        await asyncio.sleep(0.5)

async def main():
    await asyncio.gather(
        licz("A"),
        licz("B"),
    )

asyncio.run(main())
```

### Tło i główna praca

```python
import asyncio

async def monitor():
    for _ in range(3):
        print("monitor dziala")
        await asyncio.sleep(1)

async def main():
    task = asyncio.create_task(monitor())
    print("glowna praca")
    await asyncio.sleep(2)
    await task

asyncio.run(main())
```

---

## Dobre praktyki

- używaj `asyncio` głównie do I/O-bound,
- trzymaj punkt wejścia w `asyncio.run(main())`,
- pilnuj, by długie operacje blokujące nie trafiały do event loop,
- stosuj timeouty dla operacji sieciowych,
- anulowanie traktuj jako normalny scenariusz działania.

---

## Podsumowanie

`asyncio` pozwala pisać wydajne programy współbieżne bez mnożenia wątków.

Najważniejsze pojęcia to:

- event loop,
- coroutine,
- `await`,
- task,
- future.

Jeśli dobrze rozumiesz te elementy, dużo łatwiej wejść potem w `aiohttp`, `httpx`, asynchroniczne bazy danych i bardziej zaawansowane systemy.

---

## Mini ściąga

```python
import asyncio

async def praca():
    await asyncio.sleep(1)
    return "ok"

async def main():
    task = asyncio.create_task(praca())
    wynik = await task
    print(wynik)

asyncio.run(main())
```

Najważniejsze:

- `async def` tworzy coroutine,
- `await` czeka bez blokowania całego programu,
- `create_task()` uruchamia pracę współbieżnie,
- `gather()` zbiera wiele wyników,
- `wait_for()` dodaje timeout.

---

## Ćwiczenia

1. Napisz dwie coroutine, które wypisują liczby z opóźnieniem, i uruchom je współbieżnie.
2. Napisz funkcję `pobierz(n)`, która czeka `n` sekund i zwraca komunikat.
3. Użyj `asyncio.gather()`, aby uruchomić trzy zadania jednocześnie.
4. Dodaj timeout do wolnej operacji.
5. Utwórz task w tle przez `create_task()` i odbierz jego wynik później.

---

## Przykładowe rozwiązania

### 1. Dwie coroutine

```python
import asyncio

async def a():
    for i in range(3):
        print("A", i)
        await asyncio.sleep(0.3)

async def b():
    for i in range(3):
        print("B", i)
        await asyncio.sleep(0.3)

async def main():
    await asyncio.gather(a(), b())

asyncio.run(main())
```

### 2. Funkcja `pobierz`

```python
import asyncio

async def pobierz(n):
    await asyncio.sleep(n)
    return f"gotowe po {n} s"
```

### 3. Trzy zadania

```python
import asyncio

async def pobierz(n):
    await asyncio.sleep(n)
    return n

async def main():
    wyniki = await asyncio.gather(
        pobierz(1),
        pobierz(2),
        pobierz(3),
    )
    print(wyniki)

asyncio.run(main())
```

### 4. Timeout

```python
import asyncio

async def wolna():
    await asyncio.sleep(5)

async def main():
    try:
        await asyncio.wait_for(wolna(), timeout=1)
    except asyncio.TimeoutError:
        print("timeout")

asyncio.run(main())
```

### 5. Task w tle

```python
import asyncio

async def praca():
    await asyncio.sleep(1)
    return "wynik"

async def main():
    task = asyncio.create_task(praca())
    print("robi sie cos innego")
    wynik = await task
    print(wynik)

asyncio.run(main())
```
