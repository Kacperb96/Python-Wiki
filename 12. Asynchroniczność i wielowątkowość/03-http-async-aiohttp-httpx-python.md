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
9. [Timeouty](#timeouty)
10. [Obsługa błędów HTTP](#obsługa-błędów-http)
11. [Connection pooling](#connection-pooling)
12. [Nagłówki, parametry i JSON](#nagłówki-parametry-i-json)
13. [Limity współbieżności](#limity-współbieżności)
14. [Typowe błędy początkujących](#typowe-błędy-początkujących)
15. [Praktyczne przykłady](#praktyczne-przykłady)
16. [Dobre praktyki](#dobre-praktyki)
17. [Podsumowanie](#podsumowanie)
18. [Mini ściąga](#mini-ściąga)
19. [Ćwiczenia](#ćwiczenia)
20. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

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

- nowocześniejszy interfejs,
- bardzo przyjemne API,
- obsługuje zarówno sync, jak i async,
- bywa wygodny, gdy chcesz spójny styl w różnych częściach projektu.

Oba rozwiązania są sensowne.

---

## Najważniejsze pojęcia

W async HTTP warto rozumieć:

- sesję lub klienta,
- połączenia wielokrotnego użytku,
- timeouty,
- statusy HTTP,
- limity współbieżności,
- obsługę wyjątków sieciowych.

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
        print(response.text[:100])

asyncio.run(main())
```

Ważne:

- klient tworzymy raz,
- używamy go wielokrotnie,
- zamykamy przez `async with`.

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
            print(text[:100])

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
        wyniki = await asyncio.gather(
            *(fetch(client, url) for url in URLS)
        )
        print(wyniki)

asyncio.run(main())
```

To jest jedna z najczęstszych praktycznych korzyści async.

---

## Timeouty

Sieć bywa zawodna.

Trzeba ustawiać limity czasu.

W `httpx`:

```python
import httpx

timeout = httpx.Timeout(5.0)
```

Przykład:

```python
async with httpx.AsyncClient(timeout=5.0) as client:
    response = await client.get("https://example.com")
```

W `aiohttp` też można ustawić timeout na sesji lub żądaniu.

---

## Obsługa błędów HTTP

Trzeba odróżnić:

- błędy transportowe,
- timeouty,
- poprawną odpowiedź z błędnym statusem, np. `404` lub `500`.

Przykład `httpx`:

```python
import asyncio
import httpx

async def main():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://example.com")
            response.raise_for_status()
    except httpx.HTTPError as e:
        print("blad HTTP:", e)

asyncio.run(main())
```

---

## Connection pooling

To bardzo ważny temat wydajnościowy.

Jeśli tworzysz nowego klienta dla każdego requestu, tracisz korzyści z:

- utrzymywania połączeń,
- oszczędności czasu na handshaku,
- ponownego użycia zasobów.

Dlatego zwykle:

- tworzysz jednego klienta,
- używasz go do wielu żądań,
- zamykasz dopiero na końcu.

---

## Nagłówki, parametry i JSON

Przykład `httpx`:

```python
import asyncio
import httpx

async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.example.com/users",
            params={"page": 1},
            headers={"Authorization": "Bearer TOKEN"},
        )
        data = response.json()
        print(data)

asyncio.run(main())
```

Przykład POST z JSON:

```python
response = await client.post(
    "https://api.example.com/items",
    json={"name": "produkt", "price": 10},
)
```

---

## Limity współbieżności

To, że async pozwala wysłać setki zapytań, nie znaczy, że zawsze warto.

Zbyt duża liczba równoległych requestów może:

- przeciążyć serwer,
- spowodować rate limiting,
- zużyć za dużo pamięci,
- pogorszyć stabilność.

Dlatego często stosuje się semafor:

```python
import asyncio

semafor = asyncio.Semaphore(10)
```

I w zadaniu:

```python
async with semafor:
    ...
```

---

## Typowe błędy początkujących

- tworzenie nowego klienta dla każdego requestu,
- brak timeoutów,
- brak `raise_for_status()` tam, gdzie status ma znaczenie,
- uruchamianie zbyt wielu requestów naraz,
- mieszanie bibliotek sync z async w tym samym przepływie.

---

## Praktyczne przykłady

### Pobranie JSON przez `httpx`

```python
import asyncio
import httpx

async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/todos/1")
        response.raise_for_status()
        print(response.json())

asyncio.run(main())
```

### Wiele requestów z limitem

```python
import asyncio
import httpx

URLS = [f"https://jsonplaceholder.typicode.com/todos/{i}" for i in range(1, 11)]
semafor = asyncio.Semaphore(3)

async def fetch(client, url):
    async with semafor:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()

async def main():
    async with httpx.AsyncClient(timeout=5.0) as client:
        wyniki = await asyncio.gather(*(fetch(client, url) for url in URLS))
        print(len(wyniki))

asyncio.run(main())
```

---

## Dobre praktyki

- używaj jednego klienta lub sesji na wiele żądań,
- zawsze ustawiaj timeouty,
- obsługuj błędy transportowe i błędne statusy,
- ograniczaj współbieżność,
- loguj nieudane wywołania do zewnętrznych API.

---

## Podsumowanie

Async HTTP to jeden z najbardziej praktycznych powodów używania `asyncio`.

`aiohttp` i `httpx` pozwalają budować szybkie integracje sieciowe, ale wymagają dyscypliny:

- klient wielokrotnego użytku,
- timeouty,
- limity współbieżności,
- dobra obsługa błędów.

---

## Mini ściąga

```python
import asyncio
import httpx

async def main():
    async with httpx.AsyncClient(timeout=5.0) as client:
        response = await client.get("https://example.com")
        response.raise_for_status()
        print(response.text)

asyncio.run(main())
```

Najważniejsze:

- `AsyncClient` lub `ClientSession` twórz raz,
- używaj `await client.get(...)`,
- ustawiaj timeouty,
- przy wielu requestach używaj `gather()`,
- kontroluj liczbę równoległych wywołań.

---

## Ćwiczenia

1. Pobierz jeden endpoint JSON asynchronicznie przez `httpx`.
2. Pobierz 5 endpointów współbieżnie.
3. Dodaj timeout do klienta.
4. Obsłuż błąd `404` lub inny błąd HTTP.
5. Ogranicz liczbę jednoczesnych requestów do 2.

---

## Przykładowe rozwiązania

### 1. Jeden endpoint

```python
import asyncio
import httpx

async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/posts/1")
        print(response.json())

asyncio.run(main())
```

### 2. Pięć endpointów

```python
import asyncio
import httpx

async def fetch(client, post_id):
    response = await client.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    return response.json()

async def main():
    async with httpx.AsyncClient() as client:
        wyniki = await asyncio.gather(*(fetch(client, i) for i in range(1, 6)))
        print(wyniki)

asyncio.run(main())
```

### 3. Timeout

```python
import asyncio
import httpx

async def main():
    async with httpx.AsyncClient(timeout=2.0) as client:
        response = await client.get("https://example.com")
        print(response.status_code)

asyncio.run(main())
```

### 4. Obsługa błędu

```python
import asyncio
import httpx

async def main():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://example.com/nie-ma")
            response.raise_for_status()
    except httpx.HTTPError as e:
        print("blad:", e)

asyncio.run(main())
```

### 5. Limit 2

```python
import asyncio
import httpx

semafor = asyncio.Semaphore(2)

async def fetch(client, url):
    async with semafor:
        response = await client.get(url)
        return response.status_code
```
