# `mypy` i `pyright` w większym kodzie Python

## O co chodzi

Samo dodanie adnotacji typów nie daje pełnej wartości, jeśli nigdzie ich nie sprawdzasz.

Tu właśnie wchodzą narzędzia takie jak:

- `mypy`,
- `pyright`.

One analizują kod statycznie i pomagają wykrywać błędy zanim program w ogóle się uruchomi.

## Co dają w praktyce

Dzięki checkerom typów możesz wcześniej złapać np.:

- zły typ argumentu,
- błędne użycie `None`,
- niezgodny zwracany typ,
- niepoprawne użycie interfejsu,
- problemy przy refaktoryzacji.

To nie zastępuje testów, ale jest bardzo silnym wsparciem jakości kodu.

## `mypy` vs `pyright`

Na poziomie nauki najważniejsze jest to, że oba narzędzia robią podobną klasę pracy:

- sprawdzają typy statycznie,
- analizują kontrakty,
- pomagają rozwijać większy kod.

Różnią się szczegółami, stylem działania i ergonomią, ale nie trzeba na start robić z tego wojny religijnej.

Najważniejsze jest świadome używanie przynajmniej jednego z nich.

## Kiedy checker typów daje największą wartość

Szczególnie gdy:

- projekt ma wiele modułów,
- pracujesz zespołowo,
- API jest używane w wielu miejscach,
- robisz refaktoryzację,
- wracasz do starego kodu,
- logika danych jest złożona.

## Czego checker nie robi

To ważne:

- nie zastępuje runtime walidacji,
- nie zastępuje testów,
- nie gwarantuje poprawności biznesowej,
- nie sprawia automatycznie, że kod jest dobrze zaprojektowany.

On pomaga w jednej bardzo konkretnej warstwie: zgodności typów i kontraktów.

## Jak wdrażać typing do istniejącego projektu

Nie trzeba robić wszystkiego naraz.

Bardzo zdrowe podejście:

1. zacząć od najważniejszych modułów,
2. typować publiczne API,
3. ograniczać `Any`,
4. poprawiać błędy iteracyjnie,
5. stopniowo podnosić jakość.

To zwykle działa lepiej niż wielka jednorazowa rewolucja.

## Najczęstsze pułapki

### 1. Zbyt dużo `Any`

To często znak, że typing formalnie istnieje, ale nie daje pełnej wartości.

### 2. Zbyt szybkie włączenie bardzo restrykcyjnych reguł

Może zabić motywację i zamienić cały temat w walkę z narzędziem.

### 3. Typowanie wszystkiego naraz

To często kończy się chaosem.

### 4. Traktowanie checkera jak wroga

Jeśli narzędzie coś zgłasza, zwykle warto zrozumieć dlaczego, a nie tylko je uciszyć.

## Jak rozsądnie pracować z błędami typów

Dobre pytania przy błędzie:

- czy kontrakt funkcji jest źle opisany,
- czy kod runtime rzeczywiście jest niebezpieczny,
- czy tu powinien być węższy typ,
- czy przypadkiem nie użyłem `Any` albo złego `Optional`,
- czy ten błąd nie pokazuje realnego problemu architektonicznego.

## Typing a refaktoryzacja

To jedna z największych wartości.

Gdy zmieniasz API albo przenosisz logikę między modułami, checker typów potrafi szybko pokazać miejsca, które przestały być spójne.

W większym kodzie to ogromna pomoc.

## Większy przykład modułu typowanego krok po kroku

Załóżmy, że mamy prosty moduł powiadomień.

### Krok 1: wersja zbyt luźna

```python
class EmailSender:
    def send(self, message):
        print(f"Email: {message}")


class NotificationService:
    def __init__(self, sender):
        self.sender = sender

    def notify(self, text):
        self.sender.send(text)
```

Kod działa, ale:

- brak kontraktu,
- brak typów,
- brak jasności, co sender musi umieć.

### Krok 2: proste typy, ale nadal zbyt konkretne

```python
class EmailSender:
    def send(self, message: str) -> None:
        print(f"Email: {message}")


class NotificationService:
    def __init__(self, sender: EmailSender) -> None:
        self.sender = sender

    def notify(self, text: str) -> None:
        self.sender.send(text)
```

To już lepsze, ale serwis zależy od konkretnej klasy `EmailSender`.

### Krok 3: `Protocol`

```python
from typing import Protocol


class Sender(Protocol):
    def send(self, message: str) -> None:
        ...


class EmailSender:
    def send(self, message: str) -> None:
        print(f"Email: {message}")


class SmsSender:
    def send(self, message: str) -> None:
        print(f"SMS: {message}")


class NotificationService:
    def __init__(self, sender: Sender) -> None:
        self.sender = sender

    def notify(self, text: str) -> None:
        self.sender.send(text)
```

Teraz serwis zależy od zachowania, nie od konkretnej implementacji.

### Krok 4: generyczny kontener wyniku

```python
from typing import Generic, TypeVar

T = TypeVar("T")


class Box(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

    def get(self) -> T:
        return self.value
```

To może się przydać, jeśli chcesz przenosić wynik bez utraty informacji o typie.

### Krok 5: dekorator z `ParamSpec`

```python
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def log_call(func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"Wywolanie {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

Teraz możesz udekorować `notify()` albo inne funkcje bez utraty ich sygnatury.

### Krok 6: checker zawężający typ

```python
from typing import TypeGuard


def is_str_list(value: list[object]) -> TypeGuard[list[str]]:
    return all(isinstance(x, str) for x in value)
```

To się przyda np. przy walidacji wejścia do modułu.

### Krok 7: finalny kształt małego modułu

```python
from typing import Callable, Generic, ParamSpec, Protocol, TypeGuard, TypeVar

P = ParamSpec("P")
R = TypeVar("R")
T = TypeVar("T")


class Sender(Protocol):
    def send(self, message: str) -> None:
        ...


class Box(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

    def get(self) -> T:
        return self.value


class EmailSender:
    def send(self, message: str) -> None:
        print(f"Email: {message}")


class NotificationService:
    def __init__(self, sender: Sender) -> None:
        self.sender = sender

    def notify(self, text: str) -> Box[str]:
        self.sender.send(text)
        return Box(text)


def log_call(func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"Wywolanie {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@log_call
def notify_many(service: NotificationService, messages: list[str]) -> list[Box[str]]:
    return [service.notify(msg) for msg in messages]


def is_str_list(value: list[object]) -> TypeGuard[list[str]]:
    return all(isinstance(x, str) for x in value)
```

To nadal mały przykład, ale pokazuje już spójne użycie kilku narzędzi typowania w jednym module.

## Przykłady realnych błędów checkera i poprawki

### 1. Błędny typ argumentu

Kod:

```python
def greet(name: str) -> str:
    return "Hello " + name


greet(123)
```

Przykładowy błąd checkera:

```text
Argument 1 to "greet" has incompatible type "int"; expected "str"
```

Poprawka:

```python
greet("123")
```

albo zmiana kontraktu funkcji, jeśli naprawdę miała przyjmować więcej typów.

### 2. Możliwe `None`

Kod:

```python
def find_user(user_id: int) -> str | None:
    if user_id == 1:
        return "Anna"
    return None


user = find_user(2)
print(user.upper())
```

Przykładowy błąd checkera:

```text
Item "None" of "str | None" has no attribute "upper"
```

Poprawka:

```python
user = find_user(2)
if user is not None:
    print(user.upper())
```

### 3. Zły typ zwracany

Kod:

```python
def get_ids() -> list[int]:
    return [1, 2, "3"]
```

Przykładowy błąd checkera:

```text
List item 2 has incompatible type "str"; expected "int"
```

Poprawka:

```python
def get_ids() -> list[int]:
    return [1, 2, 3]
```

### 4. Niezgodność z `Protocol`

Kod:

```python
from typing import Protocol


class Sender(Protocol):
    def send(self, message: str) -> None:
        ...


class BadSender:
    def send(self, message: int) -> None:
        print(message)
```

Przykładowy sens błędu:

```text
Argument of type "BadSender" cannot be assigned to parameter "sender" of type "Sender"
```

Poprawka:

```python
class GoodSender:
    def send(self, message: str) -> None:
        print(message)
```

### 5. Dekorator traci sygnaturę

Kod:

```python
from typing import Callable, Any


def log_call(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        return func(*args, **kwargs)
    return wrapper
```

To może nie dawać jednego spektakularnego błędu, ale psuje precyzję typów i podpowiedzi IDE.

Poprawka:

- użyj `ParamSpec` i `TypeVar`,
- zachowaj prawdziwy kontrakt funkcji.

## Jak czytać komunikaty błędów dobrze

Zamiast odruchowo uciszać błąd, zapytaj:

- jaki typ checker widzi teraz,
- jaki typ ja chciałem mieć,
- gdzie typ się rozszerzył za bardzo,
- czy problem wynika z braku walidacji,
- czy to błąd kontraktu, czy błąd implementacji.

## Kiedy typing może przeszkadzać

Jeśli:

- projekt jest bardzo eksperymentalny,
- kod żyje 15 minut,
- adnotacje są cięższe niż sama logika,
- narzędzie wymusza zbyt dużo formalizmu na prostym kodzie,

to trzeba zachować rozsądek.

Zaawansowany typing ma pomagać, nie dominować.

## Mini strategia dla projektu

Rozsądna ścieżka wygląda tak:

1. typuj nowe moduły,
2. typuj warstwy publiczne,
3. unikaj `Any`, jeśli da się go usunąć,
4. dodawaj `Protocol`, generyki i `TypeGuard` tam, gdzie naprawdę pomagają,
5. uruchamiaj checker regularnie.

## Typowe błędy początkujących

- mylenie typingu z runtime walidacją,
- nadmiar `Any`,
- zbyt ciężkie typowanie bez potrzeby,
- brak strategii stopniowego wdrażania,
- ignorowanie błędów zamiast rozumienia ich przyczyny.

## Szybka ściąga

- `mypy` i `pyright` wspierają statyczną analizę typów,
- największy zysk dają w większym i dłużej utrzymywanym kodzie,
- nie zastępują testów ani walidacji runtime,
- najlepiej wdrażać je iteracyjnie i świadomie.

## Ćwiczenia

1. Weź powyższy moduł powiadomień i rozbuduj go o drugi typ sendera.
2. Dodaj celowy błąd typów i opisz, jaki komunikat checkera byś oczekiwał.
3. Napisz przykład błędu z `None` i popraw go.
4. Zamień zbyt ogólny dekorator na wersję z `ParamSpec`.
5. Zastanów się, które błędy checker typów wykrywa wcześniej niż testy manualne.

## Najważniejsze do zapamiętania

- Typy dają pełniejszą wartość dopiero razem z checkerem statycznym.
- `mypy` i `pyright` pomagają wykrywać problemy wcześniej.
- Największy sens mają w większym i wielokrotnie używanym kodzie.
- Realne komunikaty błędów są świetnym materiałem do nauki.
- Najlepiej wdrażać typing stopniowo i świadomie.
