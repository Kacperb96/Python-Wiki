# Async HTTP w Pythonie — `aiohttp`, `httpx`

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co robić HTTP asynchronicznie](#po-co-robić-http-asynchronicznie)
3. [Kiedy async HTTP ma sens](#kiedy-async-http-ma-sens)
4. [`aiohttp` i `httpx` — ogólny obraz](#aiohttp-i-httpx--ogólny-obraz)
5. [Najważniejsze pojęcia](#najważniejsze-pojęcia)
6. [`httpx.AsyncClient`](#httpxasyncclient)
7. [`aiohttp.ClientSession`](#aiohttpclientsession)
8. [Wysyłanie wielu żądań naraz](#wysyłanie-wielu-żądań-naraz)
9. [Przykład z outputem](#przykład-z-outputem)
10. [Timeouty](#timeouty)
11. [Obsługa błędów HTTP](#obsługa-błędów-http)
12. [Connection pooling](#connection-pooling)
13. [Nagłówki, parametry i JSON](#nagłówki-parametry-i-json)
14. [Limity współbieżności](#limity-współbieżności)
15. [Typowe błędy początkujących](#typowe-błędy-początkujących)
16. [Praktyczna ściąga](#praktyczna-ściąga)
17. [Ćwiczenia](#ćwiczenia)
18. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

Asynchroniczne HTTP w Pythonie pozwala wykonywać wiele zapytań sieciowych bez blokowania programu na każdą odpowiedź osobno.

To bardzo ważne przy:

- integracjach z API,
- crawlerach,
- agregatorach danych,
- mikroserwisach,
- systemach pobierających dużo informacji równolegle.

---

## Po co robić HTTP asynchronicznie

Każde zapytanie HTTP zwykle spędza większość czasu na czekaniu:

- na połączenie,
- na odpowiedź serwera,
- na przesłanie danych.

Jeśli robisz 100 zapytań jedno po drugim, marnujesz mnóstwo czasu.

Przy async możesz uruchomić wiele z nich współbieżnie.

---

## Kiedy async HTTP ma sens

Najbardziej opłaca się, gdy:

- zapytań jest dużo,
- są niezależne,
- aplikacja ma obsługiwać wiele rzeczy naraz,
- czekanie na sieć dominuje nad lokalnym liczeniem.

Jeśli wysyłasz pojedyncze żądanie raz na jakiś czas, zwykły sync bywa wystarczający.

---

## `aiohttp` i `httpx` — ogólny obraz

`aiohttp`:

- bardzo znane narzędzie do async HTTP,
- ma klienta i serwer,
- jest często spotykane w starszych i dojrzałych projektach async.

`httpx`:

- ma bardzo przyjemne API,
- obsługuje zarówno sync, jak i async,
- bywa wygodny, gdy chcesz spójny styl w różnych częściach projektu.

Oba rozwiązania są sensowne.

---

## Najważniejsze pojęcia

W async HTTP warto rozumieć:

- klienta albo sesję,
- timeouty,
- błędy sieciowe,
- statusy HTTP,
- connection pooling,
- limity współbieżności.

---

## `httpx.AsyncClient`

Przykład:

```python
import asyncio
import httpx


async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://example.com")
        print(response.status_code)
        print(response.text[:40])


asyncio.run(main())
```

Ważne:

- klient tworzysz raz,
- używasz go wielokrotnie,
- zamykasz przez `async with`.

---

## `aiohttp.ClientSession`

Przykład:

```python
import asyncio
import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://example.com") as response:
            text = await response.text()
            print(response.status)
            print(text[:40])


asyncio.run(main())
```

W `aiohttp` samo ciało odpowiedzi też pobierasz asynchronicznie.

---

## Wysyłanie wielu żądań naraz

```python
import asyncio
import httpx


URLS = [
    "https://example.com",
    "https://example.org",
    "https://example.net",
]


async def fetch(client, url):
    response = await client.get(url)
    return url, response.status_code


async def main():
    async with httpx.AsyncClient() as client:
        wyniki = await asyncio.gather(*(fetch(client, url) for url in URLS))
        print(wyniki)


asyncio.run(main())
```

---

## Przykład z outputem

Przykładowy output:

```text
[('https://example.com', 200), ('https://example.org', 200), ('https://example.net', 200)]
```

Najważniejsze:

- wszystkie requesty mogły być wykonywane współbieżnie,
- czekanie na jeden nie blokuje sensownie całej grupy,
- końcowo dostajesz listę wyników.

---

## Timeouty

Przy sieci timeout to obowiązek, nie luksus.

Przykład w `httpx`:

```python
import httpx


async with httpx.AsyncClient(timeout=5.0) as client:
    response = await client.get("https://example.com")
```

Bez timeoutów ryzykujesz zbyt długie wiszenie na problematycznych połączeniach.

---

## Obsługa błędów HTTP

Ważne jest rozróżnienie:

- błąd transportowy,
- timeout,
- status HTTP typu `404` albo `500`.

Przykład:

```python
import httpx


async def fetch(client, url):
    try:
        response = await client.get(url)
        response.raise_for_status()
        return response.text
    except httpx.HTTPStatusError as e:
        print(f"blad statusu: {e.response.status_code}")
    except httpx.RequestError as e:
        print(f"blad sieci: {e}")
```

---

## Connection pooling

To bardzo ważne praktycznie.

Jeśli tworzysz klienta raz i używasz go wielokrotnie, możesz korzystać z ponownego użycia połączeń.

To daje:

- mniejszy koszt połączeń,
- lepszą wydajność,
- zdrowszy workflow HTTP.

Dlatego zwykle nie tworzysz nowego klienta dla każdego pojedynczego requestu.

---

## Nagłówki, parametry i JSON

Przykład:

```python
response = await client.get(
    "https://api.example.com/users",
    params={"page": 1},
    headers={"Authorization": "Bearer TOKEN"},
)
```

Wysyłanie JSON:

```python
response = await client.post(
    "https://api.example.com/items",
    json={"name": "item"},
)
```

To są bardzo codzienne przypadki użycia.

---

## Limity współbieżności

Nie zawsze chcesz odpalić 1000 requestów naraz.

Czasem trzeba ograniczyć współbieżność.

Przykład z semaforem:

```python
import asyncio


semafor = asyncio.Semaphore(10)


async def fetch_limited(client, url):
    async with semafor:
        return await client.get(url)
```

To chroni:

- Twoją aplikację,
- zewnętrzne API,
- połączenia sieciowe.

---

## Typowe błędy początkujących

- tworzenie nowego klienta dla każdego requestu,
- brak timeoutów,
- brak obsługi błędów sieciowych,
- odpalanie zbyt wielu requestów naraz bez limitu,
- używanie async HTTP tam, gdzie jedno rzadkie żądanie sync byłoby prostsze.

---

## Praktyczna ściąga

### Jeden klient `httpx`

```python
async with httpx.AsyncClient() as client:
    ...
```

### Wiele requestów

```python
await asyncio.gather(...)
```

### Timeout

```python
httpx.AsyncClient(timeout=5.0)
```

### Limit współbieżności

```python
asyncio.Semaphore(10)
```

---

## Ćwiczenia

1. Pobierz jeden endpoint przez `httpx.AsyncClient`.
2. Pobierz kilka endpointów współbieżnie.
3. Dodaj timeout.
4. Obsłuż błąd `404` albo błąd transportowy.
5. Dodaj semafor ograniczający liczbę jednoczesnych requestów.
6. Wyjaśnij, czemu klient HTTP warto współdzielić.

---

## Najważniejsze do zapamiętania

- Async HTTP ma największy sens, gdy requestów jest dużo i są niezależne.
- Klienta albo sesję zwykle tworzysz raz i używasz wielokrotnie.
- Timeouty i obsługa błędów są obowiązkowe.
- `gather()` i semafory to bardzo częste narzędzia praktyczne.
