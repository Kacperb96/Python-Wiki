# `Pydantic` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `Pydantic`](#czym-jest-pydantic)
3. [Po co używać walidacji danych](#po-co-używać-walidacji-danych)
4. [Model danych](#model-danych)
5. [Parsowanie i walidacja](#parsowanie-i-walidacja)
6. [Typy i konwersje](#typy-i-konwersje)
7. [Błędy walidacji](#błędy-walidacji)
8. [Pydantic a FastAPI](#pydantic-a-fastapi)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczne przykłady](#praktyczne-przykłady)
11. [Dobre praktyki](#dobre-praktyki)
12. [Podsumowanie](#podsumowanie)
13. [Mini ściąga](#mini-ściąga)
14. [Ćwiczenia](#ćwiczenia)
15. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`Pydantic` to biblioteka do modelowania i walidacji danych.

Jest bardzo ważna w nowoczesnym Pythonie, szczególnie przy API i konfiguracji.

---

## Czym jest `Pydantic`

To narzędzie, które pozwala opisać strukturę danych klasą i sprawdzić, czy wejście jest poprawne.

Przykład:

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```

---

## Po co używać walidacji danych

Bo dane wejściowe z zewnątrz często są:

- niepełne,
- w złym typie,
- błędne,
- niebezpieczne biznesowo.

Walidacja pomaga to wcześnie wychwycić.

---

## Model danych

Modele `Pydantic` definiujesz jako klasy.

```python
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: float
```

To jest bardzo czytelny sposób opisu danych.

---

## Parsowanie i walidacja

```python
data = {"name": "Kawa", "price": 19.99}
product = Product(**data)
print(product)
```

Jeśli dane są niepoprawne, dostaniesz błąd walidacji.

---

## Typy i konwersje

`Pydantic` potrafi wykonać część sensownych konwersji.

Na przykład string `"123"` może zostać zamieniony na `int`, jeśli to ma sens dla modelu.

To wygodne, ale trzeba rozumieć, że nadal chodzi o walidację kontraktu danych.

---

## Błędy walidacji

Przy błędnych danych model zgłosi wyjątek walidacyjny.

To bardzo ważne, bo zamiast cichego psucia danych masz jasny sygnał problemu.

---

## Pydantic a FastAPI

To bardzo częsty duet.

FastAPI używa modeli `Pydantic` do:

- walidacji requestów,
- serializacji odpowiedzi,
- generowania dokumentacji API.

---

## Typowe błędy początkujących

- brak walidacji danych przy API,
- traktowanie modelu jak zwykłego słownika,
- zbyt luźne typy,
- brak rozróżnienia modeli wejściowych i wyjściowych.

---

## Praktyczne przykłady

### Model użytkownika

```python
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
```

### Walidacja

```python
user = UserCreate(name="Anna", email="anna@example.com")
print(user.email)
```

---

## Dobre praktyki

- twórz jasne modele danych,
- waliduj dane wejściowe jak najwcześniej,
- rozdzielaj modele do tworzenia, odczytu i aktualizacji, gdy ma to sens,
- używaj typów, które naprawdę opisują kontrakt danych.

---

## Podsumowanie

`Pydantic` to jedno z najważniejszych narzędzi nowoczesnego backendu Python.

Bardzo poprawia bezpieczeństwo danych i czytelność API.

---

## Mini ściąga

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```

Najważniejsze:

- model opisuje strukturę danych,
- `Pydantic` waliduje wejście,
- świetnie współpracuje z FastAPI.

---

## Ćwiczenia

1. Zdefiniuj model `User` z polami `name` i `age`.
2. Utwórz instancję modelu z poprawnych danych.
3. Podaj przykład błędnych danych wejściowych.
4. Wyjaśnij, po co walidować requesty API.
5. Wyjaśnij relację `Pydantic` i FastAPI.

---

## Przykładowe rozwiązania

### 1. Model

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```

### 2. Instancja

```python
user = User(name="Ola", age=22)
```

### 3. Błędne dane

Na przykład brak wymaganego pola albo wartość w kompletnie złym formacie.

### 4. Po co walidować

Żeby nie wpuszczać błędnych danych do logiki aplikacji i bazy.

### 5. Relacja

FastAPI używa modeli `Pydantic` do walidacji i dokumentowania danych API.
