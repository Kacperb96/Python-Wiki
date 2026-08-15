# `async` i `await` w praktyce w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co znać `async` i `await`](#po-co-znać-async-i-await)
3. [Co oznacza `async def`](#co-oznacza-async-def)
4. [Co oznacza `await`](#co-oznacza-await)
5. [Co naprawdę zwraca funkcja async](#co-naprawdę-zwraca-funkcja-async)
6. [Sekwencyjnie vs współbieżnie](#sekwencyjnie-vs-współbieżnie)
7. [Przykład z outputem](#przykład-z-outputem)
8. [Najważniejszy mentalny model](#najważniejszy-mentalny-model)
9. [Łączenie wielu wywołań](#łączenie-wielu-wywołań)
10. [Obsługa wyjątków](#obsługa-wyjątków)
11. [Timeouty i anulowanie](#timeouty-i-anulowanie)
12. [Kod blokujący w świecie async](#kod-blokujący-w-świecie-async)
13. [Kiedy nie używać async](#kiedy-nie-używać-async)
14. [Typowe błędy początkujących](#typowe-błędy-początkujących)
15. [Praktyczna ściąga](#praktyczna-ściąga)
16. [Ćwiczenia](#ćwiczenia)
17. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

`async` i `await` to składnia, która pozwala pisać kod asynchroniczny w dużo bardziej czytelny sposób niż starsze style oparte na callbackach.

Dzięki temu kod może wyglądać prawie jak zwykły kod sekwencyjny, ale potrafi wykonywać wiele oczekujących operacji współbieżnie.

---

## Po co znać `async` i `await`

Te słowa kluczowe są dziś podstawą pracy z:

- API HTTP,
- websocketami,
- asynchronicznymi bazami danych,
- crawlerami,
- nowoczesnymi frameworkami backendowymi,
- workerami sieciowymi.

Bez nich trudno swobodnie poruszać się po nowoczesnym Pythonie backendowym.

---

## Co oznacza `async def`

`async def` definiuje funkcję asynchroniczną.

Przykład:

```python
async def pobierz_uzytkownika():
    return {"id": 1, "name": "Anna"}
```

Taka funkcja nie działa dokładnie jak zwykła funkcja `def`.

Jej wywołanie nie daje od razu gotowego wyniku.

---

## Co oznacza `await`

`await` mówi:

"zaczekaj na wynik tej asynchronicznej operacji, ale oddaj w tym czasie sterowanie event loopowi".

Przykład:

```python
uzytkownik = await pobierz_uzytkownika()
```

To jest kluczowy moment całego modelu async.

---

## Co naprawdę zwraca funkcja async

To bardzo ważne.

```python
async def hello():
    return "ok"
```

Jeśli zrobisz:

```python
wynik = hello()
print(wynik)
```

Przykładowy output:

```text
<coroutine object hello at 0x...>
```

Czyli:

- nie dostałeś jeszcze stringa `"ok"`,
- dostałeś coroutine,
- trzeba ją uruchomić, zwykle przez `await` albo `asyncio.run()`.

---

## Sekwencyjnie vs współbieżnie

To jedna z najważniejszych różnic.

### Sekwencyjnie

```python
async def main():
    a = await pobierz_a()
    b = await pobierz_b()
    c = await pobierz_c()
```

Tutaj każde pobieranie startuje dopiero po poprzednim.

### Współbieżnie

```python
async def main():
    a, b, c = await asyncio.gather(
        pobierz_a(),
        pobierz_b(),
        pobierz_c(),
    )
```

Tu zadania mogą czekać równolegle na swoje wyniki.

---

## Przykład z outputem

```python
import asyncio


async def zadanie(nazwa, delay):
    print(f"start {nazwa}")
    await asyncio.sleep(delay)
    print(f"koniec {nazwa}")
    return nazwa


async def main():
    wyniki = await asyncio.gather(
        zadanie("A", 1),
        zadanie("B", 1),
    )
    print(wyniki)


asyncio.run(main())
```

Przykładowy output:

```text
start A
start B
koniec A
koniec B
['A', 'B']
```

Najważniejsze obserwacje:

- oba zadania startują szybko jedno po drugim,
- nie czekasz na pełne zakończenie `A`, żeby dopiero zacząć `B`,
- oba śpią współbieżnie.

---

## Najważniejszy mentalny model

Najprościej myśl tak:

- `async def` tworzy funkcję, która potrafi się zatrzymać,
- `await` to moment oddania sterowania,
- event loop w tym czasie może robić coś innego,
- po gotowości wyniku funkcja wraca do pracy.

To wystarcza do bardzo wielu praktycznych zastosowań.

---

## Łączenie wielu wywołań

Najczęściej spotkasz:

- zwykły `await`,
- `asyncio.gather(...)`,
- `asyncio.create_task(...)`.

Praktyczna intuicja:

- `await` dla pojedynczego wyniku,
- `gather()` gdy chcesz poczekać na kilka rzeczy naraz,
- `create_task()` gdy chcesz uruchomić coś jako task zarządzany przez event loop.

---

## Obsługa wyjątków

Wyjątki w async obsługujesz podobnie jak w zwykłym kodzie.

```python
async def pobierz_dane():
    raise ValueError("blad")


async def main():
    try:
        await pobierz_dane()
    except ValueError as e:
        print(f"blad: {e}")
```

To ważne, bo asynchroniczność nie usuwa potrzeby normalnej obsługi błędów.

---

## Timeouty i anulowanie

Czasem nie chcesz czekać bez końca.

Przykład timeoutu:

```python
import asyncio


async def wolne_zadanie():
    await asyncio.sleep(5)


async def main():
    try:
        await asyncio.wait_for(wolne_zadanie(), timeout=1)
    except TimeoutError:
        print("przekroczono limit czasu")
```

Przykładowy output:

```text
przekroczono limit czasu
```

To bardzo praktyczne przy HTTP, bazach danych i zewnętrznych usługach.

---

## Kod blokujący w świecie async

To jedna z największych pułapek.

Jeśli wewnątrz async wstawisz blokującą operację, np. ciężkie `time.sleep()` albo CPU-bound liczenie, to blokujesz event loop.

Zły przykład:

```python
import time

async def zla_funkcja():
    time.sleep(2)
```

To nie jest prawdziwie asynchroniczne oczekiwanie.

To zatrzymuje cały loop.

---

## Kiedy nie używać async

Async nie jest magicznym przyspieszaczem wszystkiego.

Nie warto go wciskać na siłę, gdy:

- program jest bardzo prosty,
- masz głównie CPU-bound obliczenia,
- nie masz realnego I/O do przeplatania,
- kod zrobiłby się dużo bardziej skomplikowany bez wyraźnego zysku.

---

## Typowe błędy początkujących

- mylenie coroutine z gotowym wynikiem,
- zapominanie o `await`,
- używanie blokującego kodu w funkcjach async,
- przekonanie, że async automatycznie daje wiele rdzeni CPU,
- używanie async tam, gdzie zwykły kod byłby prostszy i wystarczający.

---

## Praktyczna ściąga

### Definicja coroutine

```python
async def moja_funkcja():
    ...
```

### Uruchomienie programu async

```python
asyncio.run(main())
```

### Wiele zadań naraz

```python
await asyncio.gather(a(), b(), c())
```

### Timeout

```python
await asyncio.wait_for(zadanie(), timeout=2)
```

---

## Ćwiczenia

1. Napisz coroutine zwracającą tekst po `asyncio.sleep()`.
2. Pokaż, co zwraca wywołanie funkcji async bez `await`.
3. Porównaj wykonanie sekwencyjne i przez `gather()`.
4. Dodaj timeout do wolnego zadania.
5. Napisz przykład blokującego kodu w async i wyjaśnij, dlaczego to błąd.

---

## Najważniejsze do zapamiętania

- `async def` tworzy coroutine, a nie gotowy wynik.
- `await` oddaje sterowanie event loopowi.
- Async najlepiej sprawdza się przy I/O-bound.
- `gather()` pozwala współbieżnie czekać na wiele zadań.
- Kod blokujący wewnątrz async psuje model współbieżności.
