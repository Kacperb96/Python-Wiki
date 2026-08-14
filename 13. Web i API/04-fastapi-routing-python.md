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
10. [Typowe błędy początkujących](#typowe-błędy-początkujących)
11. [Praktyczne przykłady](#praktyczne-przykłady)
12. [Dobre praktyki](#dobre-praktyki)
13. [Podsumowanie](#podsumowanie)
14. [Mini ściąga](#mini-ściąga)
15. [Ćwiczenia](#ćwiczenia)
16. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Routing to sposób mapowania żądań HTTP na konkretne funkcje aplikacji.

W małej aplikacji może wydawać się prosty, ale w większym projekcie jego dobra organizacja robi ogromną różnicę.

---

## Czym jest routing

Routing odpowiada na pytanie:

"która funkcja ma obsłużyć dane żądanie pod konkretnym adresem i metodą HTTP?"

Na przykład:

- `GET /users`
- `POST /users`
- `GET /orders/10`

---

## Po co porządkować trasy

Bo bez tego większe API szybko staje się chaotyczne.

Dobry routing pomaga:

- czytać projekt,
- utrzymywać porządek,
- rozdzielać obszary domenowe,
- łatwiej testować endpointy.

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

To częsty wzorzec dla filtrowania, paginacji i wyszukiwania.

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

- `routes/users.py`
- `routes/orders.py`
- `routes/auth.py`

Każdy moduł ma swój router.

---

## Prefix i tagi

Router może mieć wspólny prefiks:

```python
router = APIRouter(prefix="/users", tags=["users"])
```

To upraszcza strukturę i dokumentację.

---

## Typowe błędy początkujących

- wszystkie endpointy w jednym pliku,
- brak podziału na obszary domenowe,
- chaotyczne adresy URL,
- mieszanie logiki routingu z logiką biznesową.

---

## Praktyczne przykłady

### Prosty router

```python
from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def list_users():
    return []

@router.get("/{user_id}")
def get_user(user_id: int):
    return {"id": user_id}
```

### Włączenie routera do aplikacji

```python
from fastapi import FastAPI
from routes.users import router as users_router

app = FastAPI()
app.include_router(users_router)
```

---

## Dobre praktyki

- grupuj trasy domenowo,
- używaj `APIRouter`,
- trzymaj spójne nazewnictwo URL,
- oddziel routing od logiki biznesowej i dostępu do danych.

---

## Podsumowanie

Dobry routing w FastAPI to nie tylko składnia dekoratorów, ale też świadoma organizacja API.

To jeden z fundamentów większego, czytelnego backendu.

---

## Mini ściąga

```python
from fastapi import APIRouter

router = APIRouter(prefix="/users")
```

Najważniejsze:

- dekoratory mapują ścieżki na funkcje,
- `APIRouter` pomaga organizować większe API,
- parametry ścieżki i query są obsługiwane bardzo wygodnie.

---

## Ćwiczenia

1. Napisz endpoint `GET /products`.
2. Napisz endpoint `GET /products/{product_id}`.
3. Dodaj query parameter `limit`.
4. Utwórz prosty `APIRouter` z prefiksem.
5. Wyjaśnij, czemu nie warto trzymać wszystkiego w `main.py`.

---

## Przykładowe rozwiązania

### 1. `GET /products`

```python
@app.get("/products")
def list_products():
    return []
```

### 2. `product_id`

```python
@app.get("/products/{product_id}")
def get_product(product_id: int):
    return {"id": product_id}
```

### 3. `limit`

```python
@app.get("/products")
def list_products(limit: int = 10):
    return {"limit": limit}
```

### 4. Router

```python
router = APIRouter(prefix="/products", tags=["products"])
```

### 5. Czemu nie wszystko w `main.py`

Bo projekt szybko robi się trudny do czytania i rozwijania.
