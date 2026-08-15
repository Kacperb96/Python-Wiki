# FastAPI w Pythonie — routing

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest routing](#czym-jest-routing)
3. [Po co porządkować trasy](#po-co-porządkować-trasy)
4. [Path operations](#path-operations)
5. [Path parameters](#path-parameters)
6. [Query parameters](#query-parameters)
7. [`APIRouter`](#apirouter)
8. [Dzielenie endpointów na moduły](#dzielenie-endpointów-na-moduły)
9. [Prefix i tagi](#prefix-i-tagi)
10. [Przykład struktury projektu](#przykład-struktury-projektu)
11. [Typowe błędy początkujących](#typowe-błędy-początkujących)
12. [Praktyczna ściąga](#praktyczna-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

Routing to sposób mapowania żądań HTTP na konkretne funkcje aplikacji.

W małej aplikacji może wydawać się prosty, ale w większym projekcie jego dobra organizacja robi ogromną różnicę.

---

## Czym jest routing

Routing odpowiada na pytanie:

"która funkcja ma obsłużyć dane żądanie pod konkretnym adresem i metodą HTTP?"

Na przykład:

- `GET /users`,
- `POST /users`,
- `GET /orders/10`.

---

## Po co porządkować trasy

Bo bez tego większe API szybko staje się chaotyczne.

Dobry routing pomaga:

- czytać projekt,
- utrzymywać porządek,
- rozdzielać obszary domenowe,
- łatwiej testować endpointy,
- lepiej ogarniać dokumentację.

---

## Path operations

W FastAPI trasa jest zwykle opisana dekoratorem:

```python
@app.get("/users")
def list_users():
    return []
```

To jest podstawowa jednostka routingu.

---

## Path parameters

Przykład:

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id}
```

FastAPI potrafi automatycznie sparsować i zwalidować parametr ścieżki.

---

## Query parameters

Przykład:

```python
@app.get("/users")
def list_users(limit: int = 10):
    return {"limit": limit}
```

To częsty wzorzec dla:

- filtrowania,
- paginacji,
- wyszukiwania.

---

## `APIRouter`

Gdy projekt rośnie, warto wydzielać routery.

```python
from fastapi import APIRouter

router = APIRouter()


@router.get("/users")
def list_users():
    return []
```

To dużo lepsze niż trzymanie wszystkiego w `main.py`.

---

## Dzielenie endpointów na moduły

Popularny układ:

- `routes/users.py`,
- `routes/orders.py`,
- `routes/auth.py`.

Każdy moduł ma swój router.

To bardzo poprawia czytelność projektu.

---

## Prefix i tagi

Router może mieć wspólny prefiks:

```python
router = APIRouter(prefix="/users", tags=["users"])
```

To upraszcza:

- strukturę ścieżek,
- dokumentację,
- grupowanie endpointów.

---

## Przykład struktury projektu

```text
app/
    main.py
    routes/
        users.py
        orders.py
```

`users.py`:

```python
from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def list_users():
    return []
```

`main.py`:

```python
from fastapi import FastAPI
from app.routes.users import router as users_router

app = FastAPI()
app.include_router(users_router)
```

To już jest dużo bliższe realnemu projektowi niż wszystko w jednym pliku.

---

## Typowe błędy początkujących

- wszystkie endpointy w jednym pliku,
- brak podziału na obszary domenowe,
- chaotyczne adresy URL,
- mieszanie logiki routingu z logiką biznesową,
- brak konsekwencji w nazewnictwie ścieżek.

---

## Praktyczna ściąga

### Prosty router

```python
router = APIRouter(prefix="/users", tags=["users"])
```

### Wpięcie routera

```python
app.include_router(users_router)
```

### Dobra praktyka

- dziel routery według domen,
- trzymaj spójne prefiksy,
- nie ładuj wszystkiego do `main.py`.

---

## Ćwiczenia

1. Zrób router `users`.
2. Zrób router `orders`.
3. Dodaj prefiksy i tagi.
4. Połącz routery w `main.py`.
5. Rozpisz prostą strukturę katalogów dla małego API.
6. Wyjaśnij, czemu dobry routing poprawia czytelność projektu.

---

## Najważniejsze do zapamiętania

- Routing mapuje request na konkretną funkcję.
- W małym projekcie może być prosty, ale w większym trzeba go organizować świadomie.
- `APIRouter` pomaga porządkować endpointy.
- Dobry routing wspiera czytelność, testowalność i rozwój API.
