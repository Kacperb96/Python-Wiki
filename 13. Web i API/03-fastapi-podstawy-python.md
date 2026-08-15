# FastAPI w Pythonie — podstawy

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest FastAPI](#czym-jest-fastapi)
3. [Po co używać FastAPI](#po-co-używać-fastapi)
4. [Najprostsza aplikacja](#najprostsza-aplikacja)
5. [Jak uruchomić aplikację](#jak-uruchomić-aplikację)
6. [Endpointy](#endpointy)
7. [Path parameters i query parameters](#path-parameters-i-query-parameters)
8. [Request body](#request-body)
9. [Modele `Pydantic`](#modele-pydantic)
10. [Przykładowe odpowiedzi i statusy](#przykładowe-odpowiedzi-i-statusy)
11. [Automatyczna dokumentacja](#automatyczna-dokumentacja)
12. [Typowe błędy początkujących](#typowe-błędy-początkujących)
13. [Praktyczna ściąga](#praktyczna-ściąga)
14. [Ćwiczenia](#ćwiczenia)
15. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

FastAPI to jeden z najpopularniejszych nowoczesnych frameworków backendowych w Pythonie do budowania API.

Łączy:

- szybkość pracy,
- typowanie,
- walidację,
- automatyczną dokumentację,
- dobrą współpracę z async.

---

## Czym jest FastAPI

To framework do budowy API HTTP.

Bardzo dobrze współpracuje z:

- `Pydantic`,
- typowaniem Pythona,
- `async` i `await`.

Dzięki temu dużo rzeczy, które w starszych frameworkach wymagały ręcznego kodu, tutaj dostajesz bardzo naturalnie.

---

## Po co używać FastAPI

Bo pomaga szybko tworzyć API, które są:

- czytelne,
- walidowane,
- dobrze udokumentowane,
- wygodne do rozwijania,
- przyjemne do testowania.

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

## Jak uruchomić aplikację

Najczęściej używasz `uvicorn`:

```bash
uvicorn main:app --reload
```

Interpretacja:

- `main` to nazwa pliku `main.py`,
- `app` to obiekt aplikacji FastAPI,
- `--reload` przydaje się w developmentcie.

Po uruchomieniu aplikacji możesz zwykle wejść na:

- `http://127.0.0.1:8000/`
- dokumentację `http://127.0.0.1:8000/docs`

---

## Endpointy

Endpoint to funkcja powiązana z konkretną ścieżką i metodą HTTP.

Przykład:

```python
@app.get("/users")
def list_users():
    return []
```

To bardzo naturalny model: dekorator mówi, jaki request trafia do jakiej funkcji.

---

## Path parameters i query parameters

### Path parameter

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id}
```

### Query parameter

```python
@app.get("/search")
def search(q: str):
    return {"query": q}
```

FastAPI automatycznie:

- rozpoznaje parametry,
- konwertuje typy,
- waliduje dane.

---

## Request body

Przy `POST` lub `PUT` często odbierasz dane w body żądania.

Tu bardzo przydają się modele `Pydantic`.

```python
from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    age: int


@app.post("/users")
def create_user(user: UserCreate):
    return user
```

---

## Modele `Pydantic`

To jedna z największych zalet FastAPI.

Framework od razu wie:

- jakiego kształtu danych oczekujesz,
- jak zwalidować request,
- jak zbudować dokumentację endpointu.

---

## Przykładowe odpowiedzi i statusy

Dla endpointu tworzącego zasób często sensowny jest status `201 Created`.

Przykład mentalny:

- `GET /users/1` -> `200 OK`,
- `POST /users` -> `201 Created`,
- błędne dane wejściowe -> np. `422`.

To ważne, bo backend powinien być przewidywalny dla klienta.

---

## Automatyczna dokumentacja

Jedna z największych zalet FastAPI to automatyczne generowanie dokumentacji API.

Najczęściej zobaczysz:

- `/docs`
- `/redoc`

To bardzo pomaga podczas developmentu i integracji.

---

## Typowe błędy początkujących

- brak rozdzielenia logiki endpointu od logiki biznesowej,
- wrzucanie wszystkiego do jednego pliku,
- brak modeli danych,
- ignorowanie walidacji i statusów odpowiedzi,
- traktowanie FastAPI jak magicznego generatora API bez rozumienia HTTP.

---

## Praktyczna ściąga

### Minimalna aplikacja

```python
app = FastAPI()
```

### Endpoint GET

```python
@app.get("/users")
def list_users():
    return []
```

### Endpoint POST z modelem

```python
@app.post("/users")
def create_user(user: UserCreate):
    return user
```

### Uruchomienie

```bash
uvicorn main:app --reload
```

---

## Ćwiczenia

1. Napisz aplikację z endpointem `GET /health`.
2. Dodaj endpoint `GET /users/{user_id}`.
3. Dodaj endpoint `POST /users` z modelem `Pydantic`.
4. Dodaj query parameter `limit`.
5. Uruchom aplikację i sprawdź dokumentację `/docs`.
6. Wyjaśnij własnymi słowami, po co FastAPI korzysta z typów i modeli danych.

---

## Najważniejsze do zapamiętania

- FastAPI to framework do budowy nowoczesnych API HTTP.
- Bardzo dobrze współpracuje z `Pydantic` i typowaniem.
- Endpointy są deklarowane jasno przez dekoratory.
- Walidacja i dokumentacja są dużą częścią jego siły.
- Rozumienie HTTP nadal jest ważniejsze niż sam framework.
