# FastAPI w Pythonie — podstawy

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest FastAPI](#czym-jest-fastapi)
3. [Po co używać FastAPI](#po-co-używać-fastapi)
4. [Najprostsza aplikacja](#najprostsza-aplikacja)
5. [Endpointy](#endpointy)
6. [Path parameters i query parameters](#path-parameters-i-query-parameters)
7. [Request body](#request-body)
8. [Modele `Pydantic`](#modele-pydantic)
9. [Automatyczna dokumentacja](#automatyczna-dokumentacja)
10. [Typowe błędy początkujących](#typowe-błędy-początkujących)
11. [Praktyczne przykłady](#praktyczne-przykłady)
12. [Dobre praktyki](#dobre-praktyki)
13. [Podsumowanie](#podsumowanie)
14. [Mini ściąga](#mini-ściąga)
15. [Ćwiczenia](#ćwiczenia)
16. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

FastAPI to jeden z najpopularniejszych nowoczesnych frameworków backendowych w Pythonie do budowania API.

Łączy:

- szybkość pracy,
- typowanie,
- walidację,
- automatyczną dokumentację.

---

## Czym jest FastAPI

To framework do budowy API HTTP.

Bardzo dobrze współpracuje z:

- `Pydantic`,
- typowaniem Pythona,
- async/await.

---

## Po co używać FastAPI

Bo pomaga szybko tworzyć API, które są:

- czytelne,
- walidowane,
- dobrze udokumentowane,
- wygodne do rozwijania.

---

## Najprostsza aplikacja

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello"}
```

To minimalny punkt wejścia.

---

## Endpointy

Endpoint to funkcja powiązana z konkretną ścieżką i metodą HTTP.

Przykład:

```python
@app.get("/users")
def list_users():
    return []
```

---

## Path parameters i query parameters

Path parameter:

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id}
```

Query parameter:

```python
@app.get("/search")
def search(q: str):
    return {"query": q}
```

---

## Request body

Przy `POST` lub `PUT` często odbierasz dane w body żądania.

Tu bardzo przydają się modele `Pydantic`.

---

## Modele `Pydantic`

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: UserCreate):
    return user
```

---

## Automatyczna dokumentacja

Jedna z największych zalet FastAPI to automatyczne generowanie dokumentacji API.

To bardzo pomaga w developmentcie i integracjach.

---

## Typowe błędy początkujących

- brak rozdzielenia logiki endpointu od logiki biznesowej,
- wrzucanie wszystkiego do jednego pliku,
- brak modeli danych,
- ignorowanie walidacji i statusów odpowiedzi.

---

## Praktyczne przykłady

### Prosty endpoint

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}
```

### Tworzenie zasobu

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str

@app.post("/items")
def create_item(item: Item):
    return {"created": item.name}
```

---

## Dobre praktyki

- używaj modeli `Pydantic`,
- rozdzielaj endpointy od logiki biznesowej,
- utrzymuj czytelną strukturę projektu,
- zaczynaj od prostych endpointów i spójnej konwencji.

---

## Podsumowanie

FastAPI to bardzo mocny wybór do nauki i budowy nowoczesnych API w Pythonie.

Łączy czytelność Pythona z praktycznymi potrzebami backendu.

---

## Mini ściąga

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"ok": True}
```

Najważniejsze:

- `FastAPI()` tworzy aplikację,
- dekoratory `@app.get`, `@app.post` definiują endpointy,
- `Pydantic` waliduje dane wejściowe.

---

## Ćwiczenia

1. Napisz endpoint `GET /health`.
2. Napisz endpoint z path parametrem `user_id`.
3. Napisz prosty `POST` z modelem `Pydantic`.
4. Wyjaśnij, po co walidacja request body.
5. Wyjaśnij, czemu warto rozdzielać endpointy od logiki biznesowej.

---

## Przykładowe rozwiązania

### 1. `GET /health`

```python
@app.get("/health")
def health():
    return {"status": "ok"}
```

### 2. `user_id`

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id}
```

### 3. `POST`

```python
class User(BaseModel):
    name: str
```

### 4. Po co walidacja

Żeby od razu odrzucać błędne dane wejściowe.

### 5. Czemu rozdzielać

Bo logika biznesowa wtedy nie jest przyklejona do warstwy HTTP i łatwiej ją testować.
