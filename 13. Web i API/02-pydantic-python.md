# `Pydantic` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `Pydantic`](#czym-jest-pydantic)
3. [Po co używać walidacji danych](#po-co-używać-walidacji-danych)
4. [Model danych](#model-danych)
5. [Parsowanie i walidacja](#parsowanie-i-walidacja)
6. [Typy i konwersje](#typy-i-konwersje)
7. [Błędy walidacji](#błędy-walidacji)
8. [Przykład z outputem](#przykład-z-outputem)
9. [Modele wejściowe i wyjściowe](#modele-wejściowe-i-wyjściowe)
10. [Pydantic a FastAPI](#pydantic-a-fastapi)
11. [Typowe błędy początkujących](#typowe-błędy-początkujących)
12. [Praktyczna ściąga](#praktyczna-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

`Pydantic` to biblioteka do modelowania i walidacji danych.

Jest bardzo ważna w nowoczesnym Pythonie, szczególnie przy API, konfiguracji i pracy z danymi wejściowymi z zewnątrz.

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

To jest bardzo czytelny sposób zdefiniowania kontraktu danych.

---

## Po co używać walidacji danych

Bo dane wejściowe z zewnątrz często są:

- niepełne,
- w złym typie,
- błędne,
- niebezpieczne biznesowo.

Walidacja pomaga wychwycić to wcześnie, zanim dane trafią głębiej do systemu.

---

## Model danych

Modele `Pydantic` definiujesz jako klasy.

```python
from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: float
```

To dużo czytelniejsze niż ręczne sprawdzanie wielu pól przez `if` i `try/except` rozrzucone po kodzie.

---

## Parsowanie i walidacja

```python
from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: float


data = {"name": "Kawa", "price": 19.99}
product = Product(**data)
print(product)
```

Jeśli dane są poprawne, model zostanie utworzony.

Jeśli są niepoprawne, dostaniesz błąd walidacji.

---

## Typy i konwersje

`Pydantic` potrafi wykonać część sensownych konwersji.

Na przykład string `"123"` może zostać zamieniony na `int`, jeśli to pasuje do modelu.

To wygodne, ale ważne jest rozumienie, że nadal chodzi o walidację kontraktu danych, a nie o zgadywanie wszystkiego za programistę.

---

## Błędy walidacji

Przy błędnych danych model zgłosi błąd walidacyjny.

To bardzo ważne, bo zamiast cichego psucia danych masz jasny sygnał problemu.

---

## Przykład z outputem

```python
from pydantic import BaseModel, ValidationError


class UserCreate(BaseModel):
    name: str
    age: int


try:
    user = UserCreate(name="Anna", age="abc")
except ValidationError as e:
    print(e)
```

Przykładowy output:

```text
1 validation error for UserCreate
age
  Input should be a valid integer, unable to parse string as an integer
```

Najważniejsze:

- dokładnie wiesz, które pole jest błędne,
- dostajesz czytelny sygnał, co poszło nie tak.

---

## Modele wejściowe i wyjściowe

Bardzo dobra praktyka:

nie zawsze używaj jednego modelu do wszystkiego.

Przykład:

```python
class UserCreate(BaseModel):
    name: str
    email: str


class UserRead(BaseModel):
    id: int
    name: str
    email: str
```

Dlaczego to ma sens:

- model wejściowy opisuje dane, które klient wysyła,
- model wyjściowy opisuje dane, które API zwraca,
- możesz nie chcieć przyjmować `id` od klienta przy tworzeniu użytkownika.

---

## Pydantic a FastAPI

To bardzo częsty duet.

FastAPI używa modeli `Pydantic` do:

- walidacji requestów,
- serializacji odpowiedzi,
- generowania dokumentacji API.

Dlatego dobre zrozumienie `Pydantic` bardzo pomaga w pracy z FastAPI.

---

## Typowe błędy początkujących

- brak walidacji danych przy API,
- traktowanie modelu jak zwykłego słownika bez zrozumienia kontraktu,
- zbyt luźne typy,
- brak rozróżnienia modeli wejściowych i wyjściowych,
- próba wrzucania całej logiki biznesowej do modelu danych.

---

## Praktyczna ściąga

### Prosty model

```python
class UserCreate(BaseModel):
    name: str
    email: str
```

### Tworzenie modelu

```python
user = UserCreate(name="Anna", email="anna@example.com")
```

### Obsługa błędu walidacji

```python
except ValidationError as e:
    print(e)
```

---

## Ćwiczenia

1. Napisz model `UserCreate`.
2. Napisz model `ProductCreate`.
3. Utwórz model z poprawnych danych.
4. Wywołaj model z błędnymi danymi i przeanalizuj błąd.
5. Rozdziel model wejściowy i model wyjściowy dla jednego zasobu.
6. Wyjaśnij własnymi słowami, po co backendowi walidacja danych.

---

## Najważniejsze do zapamiętania

- `Pydantic` pomaga modelować i walidować dane.
- Dane wejściowe z zewnątrz powinny być walidowane jak najwcześniej.
- Modele wejściowe i wyjściowe często warto rozdzielać.
- Czytelny błąd walidacji to duża zaleta w API i backendzie.
