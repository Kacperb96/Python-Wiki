# `async` i `await` w praktyce w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co znać `async` i `await`](#po-co-znać-async-i-await)
3. [Co oznacza `async def`](#co-oznacza-async-def)
4. [Co oznacza `await`](#co-oznacza-await)
5. [Kiedy `await` ma sens](#kiedy-await-ma-sens)
6. [Sekwencyjnie vs współbieżnie](#sekwencyjnie-vs-współbieżnie)
7. [Najczęstszy mentalny model](#najczęstszy-mentalny-model)
8. [Jak projektować funkcje asynchroniczne](#jak-projektować-funkcje-asynchroniczne)
9. [Łączenie wielu wywołań](#łączenie-wielu-wywołań)
10. [Obsługa wyjątków](#obsługa-wyjątków)
11. [Timeouty i anulowanie](#timeouty-i-anulowanie)
12. [Kod blokujący w świecie async](#kod-blokujący-w-świecie-async)
13. [Kiedy nie używać async](#kiedy-nie-używać-async)
14. [Typowe błędy początkujących](#typowe-błędy-początkujących)
15. [Praktyczne przykłady](#praktyczne-przykłady)
16. [Dobre praktyki](#dobre-praktyki)
17. [Podsumowanie](#podsumowanie)
18. [Mini ściąga](#mini-ściąga)
19. [Ćwiczenia](#ćwiczenia)
20. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`async` i `await` to składnia, która pozwala pisać kod asynchroniczny w sposób czytelniejszy niż starsze style oparte na callbackach.

Dzięki temu kod wygląda prawie jak zwykły kod sekwencyjny, ale potrafi wykonywać wiele oczekujących operacji współbieżnie.

---

## Po co znać `async` i `await`

Te słowa kluczowe są dziś podstawą pracy z:

- API HTTP,
- websocketami,
- asynchronicznymi bazami danych,
- crawlerami,
- workerami sieciowymi,
- nowoczesnymi frameworkami backendowymi.

Bez nich trudno swobodnie poruszać się po nowoczesnym Pythonie.

---

## Co oznacza `async def`

`async def` definiuje funkcję asynchroniczną.

Przykład:

```python
async def pobierz_uzytkownika():
    return {"id": 1, "name": "Anna"}
```

Wywołanie takiej funkcji nie daje od razu gotowego wyniku.

Daje coroutine, którą trzeba uruchomić i zwykle `await`-ować.

---

## Co oznacza `await`

`await` mówi:

"zaczekaj na wynik tej asynchronicznej operacji, ale nie blokuj całej pętli zdarzeń".

Przykład:

```python
uzytkownik = await pobierz_uzytkownika()
```

To jest najważniejszy mechanizm w codziennej pracy z async.

---

## Kiedy `await` ma sens

`await` ma sens tylko wobec obiektów awaitable, czyli takich, które wspierają mechanizm asynchronicznego oczekiwania.

Najczęściej będą to:

- coroutine,
- taski,
- niektóre futures.

Tego nie zrobisz:

```python
await 123
```

To spowoduje błąd.

---

## Sekwencyjnie vs współbieżnie

To bardzo ważna różnica.

Sekwencyjnie:

```python
async def main():
    a = await pobierz_a()
    b = await pobierz_b()
    c = await pobierz_c()
```

Tutaj każde pobieranie startuje dopiero po poprzednim.

Współbieżnie:

```python
async def main():
    a, b, c = await asyncio.gather(
        pobierz_a(),
        pobierz_b(),
        pobierz_c(),
    )
```

To często daje dużą różnicę wydajnościową.

---

## Najczęstszy mentalny model

Najprościej myśleć tak:

- `async def` tworzy funkcję, która potrafi się zatrzymać,
- `await` to moment oddania sterowania,
- event loop w tym czasie może robić coś innego,
- po gotowości wyników funkcja wraca do pracy.

Ten model wystarcza do bardzo wielu praktycznych zastosowań.

---

## Jak projektować funkcje asynchroniczne

Dobra funkcja async zwykle:

- robi operacje I/O,
- jasno oddziela logikę od dostępu do zewnętrznych zasobów,
- nie ukrywa ciężkich blokujących obliczeń,
- zwraca normalne dane, a nie side effecty rozsiane po całym systemie.

Przykład:

```python
async def pobierz_json(client, url):
    response = await client.get(url)
    response.raise_for_status()
    return response.json()
```

---

## Łączenie wielu wywołań

W praktyce bardzo często chcesz pobrać wiele rzeczy naraz.

```python
import asyncio

async def pobierz(n):
    await asyncio.sleep(1)
    return f"dane {n}"

async def main():
    wyniki = await asyncio.gather(
        pobierz(1),
        pobierz(2),
        pobierz(3),
    )
    print(wyniki)
```

To podstawowy wzorzec produkcyjny.

---

## Obsługa wyjątków

Async nie usuwa potrzeby obsługi błędów.

```python
import asyncio

async def zepsuta():
    await asyncio.sleep(0.1)
    raise ValueError("blad")

async def main():
    try:
        await zepsuta()
    except ValueError as e:
        print("zlapano:", e)

asyncio.run(main())
```

Przy `gather()` warto pamiętać, że wyjątek jednego zadania może zatrzymać całość, jeśli nie używasz odpowiedniej strategii.

---

## Timeouty i anulowanie

W praktycznych systemach sieciowych timeout to obowiązek, a nie dodatek.

```python
import asyncio

async def pobierz():
    await asyncio.sleep(5)

async def main():
    try:
        await asyncio.wait_for(pobierz(), timeout=1)
    except asyncio.TimeoutError:
        print("za dlugo")
```

Anulowanie zadań też trzeba traktować jako normalne zdarzenie.

---

## Kod blokujący w świecie async

To jeden z najczęstszych problemów.

Jeśli wewnątrz `async def` zrobisz:

```python
import time

time.sleep(3)
```

to blokujesz event loop.

W efekcie cała zaleta async znika.

Dlatego:

- do czekania używaj `await asyncio.sleep(...)`,
- ciężkie obliczenia przenoś do procesów lub osobnych mechanizmów,
- blokujące biblioteki zastępuj asynchronicznymi odpowiednikami.

---

## Kiedy nie używać async

Nie każdy program potrzebuje async.

Nie warto komplikować kodu, jeśli:

- program jest prostym skryptem,
- nie ma wielu operacji I/O,
- głównym problemem są obliczenia CPU-bound,
- biblioteki, których używasz, są całkowicie synchroniczne.

Wtedy prosty kod bywa lepszy.

---

## Typowe błędy początkujących

- używanie `async def` wszędzie bez potrzeby,
- zapominanie o `await`,
- blokowanie event loop przez `time.sleep()` lub ciężką pętlę,
- mylenie współbieżności z równoległością,
- próba wywołania `await` poza kontekstem asynchronicznym.

---

## Praktyczne przykłady

### Proste użycie `await`

```python
import asyncio

async def przywitaj():
    await asyncio.sleep(1)
    return "czesc"

async def main():
    tekst = await przywitaj()
    print(tekst)

asyncio.run(main())
```

### Sekwencyjnie

```python
import asyncio

async def pobierz(n):
    await asyncio.sleep(1)
    return n

async def main():
    print(await pobierz(1))
    print(await pobierz(2))
```

### Współbieżnie

```python
import asyncio

async def pobierz(n):
    await asyncio.sleep(1)
    return n

async def main():
    wyniki = await asyncio.gather(
        pobierz(1),
        pobierz(2),
    )
    print(wyniki)

asyncio.run(main())
```

---

## Dobre praktyki

- używaj async tam, gdzie rzeczywiście jest dużo I/O,
- trzymaj granice odpowiedzialności czytelne,
- dodawaj timeouty do wywołań zewnętrznych,
- nie mieszaj bez potrzeby stylu sync i async,
- testuj błędy, anulowanie i scenariusze przeciążenia.

---

## Podsumowanie

`async` i `await` to praktyczna składnia do budowania wydajnych aplikacji I/O-bound.

Najważniejsze jest nie samo zapamiętanie składni, ale zrozumienie, kiedy kod oddaje sterowanie i kiedy naprawdę działa współbieżnie.

To fundament pod `asyncio`, `aiohttp`, `httpx`, FastAPI i wiele innych narzędzi.

---

## Mini ściąga

```python
import asyncio

async def pobierz():
    await asyncio.sleep(1)
    return "ok"

async def main():
    wynik = await pobierz()
    print(wynik)

asyncio.run(main())
```

Pamiętaj:

- `async def` tworzy funkcję asynchroniczną,
- `await` czeka na wynik,
- `gather()` uruchamia wiele rzeczy współbieżnie,
- `time.sleep()` nie pasuje do async,
- timeouty są ważne.

---

## Ćwiczenia

1. Napisz funkcję `async def hello()`, która po sekundzie zwróci napis `"hello"`.
2. Uruchom trzy funkcje asynchroniczne współbieżnie.
3. Zasymuluj timeout dla zbyt wolnej operacji.
4. Pokaż różnicę czasu między wykonaniem sekwencyjnym i współbieżnym.
5. Napisz funkcję async, która łapie wyjątek i zwraca komunikat błędu.

---

## Przykładowe rozwiązania

### 1. `hello`

```python
import asyncio

async def hello():
    await asyncio.sleep(1)
    return "hello"
```

### 2. Trzy funkcje współbieżnie

```python
import asyncio

async def praca(n):
    await asyncio.sleep(1)
    return n

async def main():
    wyniki = await asyncio.gather(
        praca(1),
        praca(2),
        praca(3),
    )
    print(wyniki)

asyncio.run(main())
```

### 3. Timeout

```python
import asyncio

async def wolna():
    await asyncio.sleep(10)

async def main():
    try:
        await asyncio.wait_for(wolna(), timeout=1)
    except asyncio.TimeoutError:
        print("timeout")

asyncio.run(main())
```

### 4. Różnica czasu

```python
import asyncio
import time

async def praca():
    await asyncio.sleep(1)

async def sekwencyjnie():
    await praca()
    await praca()

async def wspolbieznie():
    await asyncio.gather(praca(), praca())

start = time.perf_counter()
asyncio.run(sekwencyjnie())
print("sek:", time.perf_counter() - start)

start = time.perf_counter()
asyncio.run(wspolbieznie())
print("wsp:", time.perf_counter() - start)
```

### 5. Obsługa błędu

```python
import asyncio

async def niebezpieczna():
    try:
        raise ValueError("ups")
    except ValueError as e:
        return f"blad: {e}"

print(asyncio.run(niebezpieczna()))
```
