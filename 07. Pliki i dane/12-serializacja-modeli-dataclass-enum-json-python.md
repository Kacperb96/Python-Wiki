# Serializacja modeli: `dataclass` + `Enum` + JSON w Pythonie

## Wprowadzenie

Gdy model danych robi się trochę dojrzalszy, bardzo szybko trafiasz na taki zestaw:

- `dataclass` do reprezentowania danych,
- `Enum` do zamkniętych zestawów wartości,
- JSON do wymiany danych z plikami albo API.

I wtedy pojawia się praktyczne pytanie:

`jak to sensownie zserializować?`

## Prosty model

```python
from dataclasses import dataclass
from enum import Enum


class OrderStatus(Enum):
    NEW = "new"
    PAID = "paid"


@dataclass
class Order:
    order_id: int
    status: OrderStatus
```

Taki model jest czytelny w Pythonie.

Ale JSON nie rozumie bezpośrednio twoich klas ani enumów.

## `asdict()` dla `dataclass`

```python
from dataclasses import dataclass, asdict


@dataclass
class User:
    name: str
    age: int


user = User("Anna", 30)
print(asdict(user))
```

Output:

```python
{'name': 'Anna', 'age': 30}
```

To bardzo wygodne.

## Problem z `Enum`

```python
from dataclasses import dataclass, asdict
from enum import Enum


class OrderStatus(Enum):
    NEW = "new"
    PAID = "paid"


@dataclass
class Order:
    order_id: int
    status: OrderStatus


order = Order(1, OrderStatus.PAID)
print(asdict(order))
```

Output:

```python
{'order_id': 1, 'status': <OrderStatus.PAID: 'paid'>}
```

To jest już słownik Pythona, ale nie taki, który od razu nadaje się ładnie do JSON.

## Ręczne mapowanie do JSON-friendly danych

```python
from dataclasses import dataclass
from enum import Enum
import json


class OrderStatus(Enum):
    NEW = "new"
    PAID = "paid"


@dataclass
class Order:
    order_id: int
    status: OrderStatus


order = Order(1, OrderStatus.PAID)

payload = {
    "order_id": order.order_id,
    "status": order.status.value,
}

print(json.dumps(payload))
```

Output:

```python
{"order_id": 1, "status": "paid"}
```

To jest bardzo praktyczny i bezpieczny kierunek.

## Odczyt z JSON z powrotem do modelu

```python
from dataclasses import dataclass
from enum import Enum
import json


class OrderStatus(Enum):
    NEW = "new"
    PAID = "paid"


@dataclass
class Order:
    order_id: int
    status: OrderStatus


text = '{"order_id": 2, "status": "new"}'
data = json.loads(text)

order = Order(
    order_id=data["order_id"],
    status=OrderStatus(data["status"]),
)

print(order)
print(order.status.value)
```

Output:

```python
Order(order_id=2, status=<OrderStatus.NEW: 'new'>)
new
```

To jest właśnie typowy flow:

- JSON -> `dict`
- `dict` -> model Pythona

## Dlaczego to jest przydatne

Taki model daje:

- lepszy porządek w kodzie,
- mniej luźnych stringów,
- czytelniejsze dane domenowe,
- łatwiejsze testy,
- bezpieczniejsze użycie statusów i typów.

## Typowe błędy

### 1. Zakładanie, że `json.dumps()` rozumie wszystko automatycznie

Nie rozumie od razu twoich klas i enumów tak, jak byś chciał.

### 2. Mieszanie luźnych stringów z enumami

W jednym miejscu `"paid"`, w drugim `OrderStatus.PAID`.

To robi chaos.

### 3. Brak jawnego mapowania

Im bardziej model rośnie, tym bardziej warto mieć jawne przejście:

- model -> payload
- payload -> model

## Mini case study

Masz backend zamówień:

- w Pythonie chcesz mieć `dataclass` i `Enum`,
- ale do API i plików chcesz wysyłać zwykły JSON.

Najlepsze podejście to zwykle:

- w środku systemu trzymaj mocny model,
- na granicy systemu zamieniaj go na JSON-friendly dane.

## Dobre praktyki

- używaj `dataclass` dla modeli danych,
- używaj `Enum` dla statusów i ról,
- na wyjściu do JSON mapuj enum przez `.value`,
- na wejściu zamieniaj string z JSON na enum,
- nie mieszaj "pół-modelu" i "pół-luźnego dicta" bez planu.

## Zadania

1. Zbuduj `dataclass` `User` i zamień ją przez `asdict()` na słownik.
2. Zbuduj `Enum` statusów zamówienia i zapisz model do JSON-friendly słownika.
3. Odczytaj JSON i zbuduj z niego `dataclass` z `Enum`.
4. Opisz, czemu warto trzymać `Enum` wewnątrz modelu, a string dopiero na granicy systemu.
