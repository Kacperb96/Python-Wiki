# `enum` w Pythonie

## Wprowadzenie

`Enum` służy do reprezentowania małego, zamkniętego zestawu nazwanych wartości.

To bardzo praktyczne, gdy zamiast "luźnych stringów" albo "magicznych liczb" chcesz mieć coś:

- czytelniejszego,
- trudniejszego do pomylenia,
- lepiej komunikującego intencję,
- wygodniejszego w warunkach i modelach danych.

Bardzo częsty problem bez `Enum` wygląda tak:

```python
status = "shipped"
```

Niby działa, ale łatwo o literówki:

```python
status = "shipped"
status = "shiped"
status = "SHIPPED"
```

Każdy taki wariant może oznaczać błąd albo dodatkowe `if`-y rozrzucone po kodzie.

## Kiedy `Enum` ma sens

`Enum` jest dobry, gdy masz:

- status zamówienia,
- rolę użytkownika,
- dzień tygodnia,
- typ powiadomienia,
- poziom logowania,
- tryb działania programu,
- klasyfikację o małej liczbie dopuszczalnych wartości.

## Kiedy `Enum` zwykle nie ma sensu

Raczej nie warto używać `Enum`, gdy:

- wartości są całkowicie otwarte i użytkownik może wpisywać dowolne dane,
- zestaw wartości bardzo często się zmienia i nie jest logicznie zamknięty,
- zwykły `bool` lub prosty string w jednorazowym małym skrypcie jest wystarczający.

## Najprostszy `Enum`

```python
from enum import Enum


class OrderStatus(Enum):
    NEW = "new"
    PAID = "paid"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"


print(OrderStatus.NEW)
print(OrderStatus.NEW.name)
print(OrderStatus.NEW.value)
```

Output:

```python
OrderStatus.NEW
NEW
new
```

Tutaj:

- `OrderStatus.NEW` to element enum,
- `.name` to nazwa pola w enumie,
- `.value` to przypisana wartość.

## Dlaczego to jest lepsze od luźnych stringów

Porównaj dwa style.

### Luźny string

```python
status = "shipped"

if status == "shipped":
    print("Wyslane")
```

Tu bardzo łatwo o literówkę albo niespójny zapis w innym miejscu projektu.

### `Enum`

```python
status = OrderStatus.SHIPPED

if status == OrderStatus.SHIPPED:
    print("Wyslane")
```

Tutaj:

- intencja jest czytelniejsza,
- edytor i narzędzia łatwiej pomagają,
- mniej ryzykujesz literówkami.

Output:

```python
Wyslane
```

## Tworzenie enum z liczbami

Czasem wartości są liczbowe:

```python
from enum import Enum


class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3


print(Priority.HIGH)
print(Priority.HIGH.value)
```

Output:

```python
Priority.HIGH
3
```

To nadal jest pełny `Enum`, a nie zwykły `int`.

## Iterowanie po enumie

```python
from enum import Enum


class Role(Enum):
    USER = "user"
    MODERATOR = "moderator"
    ADMIN = "admin"


for role in Role:
    print(role.name, "->", role.value)
```

Output:

```python
USER -> user
MODERATOR -> moderator
ADMIN -> admin
```

To bardzo wygodne, gdy:

- budujesz listę do wyboru,
- chcesz wygenerować dokumentację,
- walidujesz dozwolone wartości.

## Porównywanie enumów

```python
from enum import Enum


class Status(Enum):
    NEW = "new"
    DONE = "done"


print(Status.NEW == Status.NEW)
print(Status.NEW == Status.DONE)
```

Output:

```python
True
False
```

Najczęściej porównujesz enum do enumu, a nie do gołego stringa.

## Tworzenie elementu enum z wartości

```python
from enum import Enum


class Status(Enum):
    NEW = "new"
    DONE = "done"


status = Status("new")
print(status)
```

Output:

```python
Status.NEW
```

To przydatne, gdy np. dostajesz dane z API, formularza albo pliku i chcesz je zamienić na bezpieczniejszy model wewnętrzny.

### Co się stanie dla złej wartości

```python
from enum import Enum


class Status(Enum):
    NEW = "new"
    DONE = "done"


print(Status("invalid"))
```

Output:

```python
ValueError: 'invalid' is not a valid Status
```

To jest dobra rzecz. System od razu sygnalizuje, że dostał coś spoza dozwolonego zestawu.

## `Enum` w warunkach

```python
from enum import Enum


class PaymentStatus(Enum):
    PENDING = "pending"
    PAID = "paid"
    FAILED = "failed"


status = PaymentStatus.PAID

if status == PaymentStatus.PAID:
    print("Mozna wyslac zamowienie")
elif status == PaymentStatus.PENDING:
    print("Czekamy na platnosc")
else:
    print("Nieudana platnosc")
```

Output:

```python
Mozna wyslac zamowienie
```

## `Enum` w połączeniu z `dataclass`

To bardzo naturalne połączenie.

```python
from dataclasses import dataclass
from enum import Enum


class OrderStatus(Enum):
    NEW = "new"
    PAID = "paid"
    SHIPPED = "shipped"


@dataclass
class Order:
    order_id: int
    status: OrderStatus


order = Order(order_id=101, status=OrderStatus.PAID)
print(order)
print(order.status.value)
```

Output:

```python
Order(order_id=101, status=<OrderStatus.PAID: 'paid'>)
paid
```

To daje dużo lepszy model niż:

```python
{"order_id": 101, "status": "paid"}
```

bo od razu wiadomo, że `status` ma należeć do konkretnego zbioru wartości.

## `str` + `Enum`

Czasem chcesz, żeby enum był jednocześnie łatwy do porównania i serializacji jako string.

Wtedy używa się wzorca:

```python
from enum import Enum


class Color(str, Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


print(Color.RED)
print(Color.RED.value)
print(isinstance(Color.RED.value, str))
```

Output:

```python
Color.RED
red
True
```

To bywa wygodne np. przy API, JSON i konfiguracji.

## `auto()`

Jeśli nie zależy Ci na ręcznym wpisywaniu wartości, możesz użyć `auto()`.

```python
from enum import Enum, auto


class LogLevel(Enum):
    DEBUG = auto()
    INFO = auto()
    WARNING = auto()
    ERROR = auto()


print(LogLevel.DEBUG.value)
print(LogLevel.INFO.value)
```

Output:

```python
1
2
```

To wygodne, gdy:

- potrzebujesz głównie nazw,
- konkretna liczba nie ma większego znaczenia,
- chcesz uniknąć ręcznego numerowania.

## `IntEnum`

Python ma też `IntEnum`, gdy elementy mają zachowywać się bardziej jak liczby.

```python
from enum import IntEnum


class ExitCode(IntEnum):
    SUCCESS = 0
    ERROR = 1


print(ExitCode.SUCCESS)
print(int(ExitCode.ERROR))
print(ExitCode.ERROR > ExitCode.SUCCESS)
```

Output:

```python
0
1
True
```

To narzędzie bardziej specjalistyczne. Najczęściej zwykły `Enum` wystarcza.

## Typowe błędy początkujących

### 1. Porównywanie `.value` wszędzie zamiast enumu

Zamiast:

```python
if status.value == "paid":
```

często lepiej:

```python
if status == OrderStatus.PAID:
```

`.value` zostawiaj głównie na moment:

- serializacji,
- wypisania,
- komunikacji z zewnętrznym systemem.

### 2. Używanie `Enum` do wszystkiego

Nie każda wartość musi być enumem.

Jeśli masz jedno pole `debug = True`, to zwykły `bool` jest lepszy niż:

```python
class DebugMode(Enum):
    ON = True
    OFF = False
```

### 3. Mieszanie stringów i enumów bez planu

Zły styl:

```python
if status == "paid" or status == OrderStatus.PAID:
```

To sygnał, że model danych jest niespójny.

### 4. Trzymanie nieprzemyślanych wartości

Jeśli enum ma reprezentować stabilny model domeny, to wartości powinny być sensowne i konsekwentne.

## Mini case study

Załóżmy, że masz system zamówień.

### Wersja słaba

```python
order = {"id": 1, "status": "payed"}
```

Problem:

- literówka przechodzi dalej,
- kod nie ma jednego źródła prawdy,
- różne moduły mogą używać różnych zapisów.

### Wersja lepsza

```python
from enum import Enum


class OrderStatus(Enum):
    NEW = "new"
    PAID = "paid"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"
```

Teraz:

- status jest jawnie modelowany,
- łatwiej testować logikę,
- łatwiej budować walidację,
- mniej literówek i rozjazdów.

## `Enum` a czytelność projektu

`Enum` jest bardzo dobry, gdy chcesz powiedzieć:

`to pole nie przyjmuje dowolnej wartości; ono ma skończony, nazwany zestaw opcji`

To jest wartość nie tylko techniczna, ale też komunikacyjna dla człowieka czytającego kod.

## Dobre praktyki

- używaj `Enum` dla zamkniętych zestawów wartości,
- porównuj enum do enumu,
- używaj `.value` głównie przy wyjściu na zewnątrz,
- łącz `Enum` z `dataclass`, `typing` i walidacją danych,
- nie wciskaj enumów tam, gdzie prostszy typ wystarcza.

## Szybka ściąga

Najczęściej przydatne:

- `Enum`
- `IntEnum`
- `auto()`
- `.name`
- `.value`
- iteracja po enumie
- konwersja `Status("new")`

## Zadania

1. Zbuduj `Enum` dla statusów zamówienia.
2. Wypisz wszystkie elementy enumu wraz z `.name` i `.value`.
3. Zamień string `"paid"` na odpowiedni element enumu.
4. Połącz `Enum` z `dataclass` w modelu `Order`.
5. Porównaj wersję na luźnych stringach i wersję z `Enum` dla tego samego problemu.
6. Opisz trzy sytuacje, w których `Enum` realnie poprawia jakość kodu.
