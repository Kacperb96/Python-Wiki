# `ParamSpec` w Pythonie

## O co chodzi

`ParamSpec` służy do opisywania **parametrów funkcji** jako całości.

To bardzo przydatne wtedy, gdy:

- piszesz dekoratory,
- przekazujesz funkcje dalej,
- chcesz zachować dokładną sygnaturę funkcji wejściowej.

Bez `ParamSpec` bardzo łatwo spłaszczyć typ funkcji do czegoś zbyt ogólnego, np. `Callable[..., Any]`.

## Problem bez `ParamSpec`

Załóżmy, że masz dekorator:

```python
from typing import Callable, Any


def log_calls(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Wywolanie {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

To działa, ale checker typów traci bardzo dużo informacji:

- jakie argumenty przyjmuje dekorowana funkcja,
- jaki ma dokładny kontrakt,
- jakie podpowiedzi powinno dawać IDE.

## Intuicja

`TypeVar` pomaga opisać typ wartości.

`ParamSpec` pomaga opisać zestaw parametrów funkcji.

Czyli jeśli chcesz powiedzieć:

- ta funkcja zwraca ten sam typ co wejściowa,
- i przyjmuje dokładnie te same argumenty,

to właśnie tu wchodzi `ParamSpec`.

## Podstawowy przykład

```python
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def log_calls(func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"Wywolanie {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

Teraz dekorator zachowuje:

- typ argumentów,
- typ zwracany.

To ogromna różnica jakościowa względem `Callable[..., Any]`.

## Przykład użycia

```python
from typing import Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def log_calls(func: Callable[P, R]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"Wywolanie {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@log_calls
def add(a: int, b: int) -> int:
    return a + b

print(add(2, 3))
```

Output:

```python
Wywolanie add
5
```

## Dlaczego to jest ważne

Dekoratory bez dobrego typowania często psują ergonomię kodu.

Objawy:

- IDE przestaje dobrze podpowiadać argumenty,
- checker typów widzi dekorowaną funkcję jako zbyt ogólną,
- łatwiej przegapić błędne wywołanie.

`ParamSpec` rozwiązuje właśnie ten problem.

## `ParamSpec` a dekoratory

To najbardziej praktyczny use case.

Jeśli dekorator:

- nie zmienia sygnatury funkcji,

`ParamSpec` zwykle jest świetnym wyborem.

Jeśli dekorator dodatkowo zmienia typ zwracany albo opakowuje wynik, nadal można to opisać, ale z trochę bardziej złożonym typowaniem.

## Kiedy to ma sens

Szczególnie gdy:

- piszesz biblioteki,
- tworzysz reusable dekoratory,
- zależy Ci na jakości typowania w większym kodzie,
- chcesz, by narzędzia rozumiały kontrakt funkcji po dekoracji.

## Kiedy to może być przesadą

Jeśli masz jednorazowy mały skrypt i dekorator użyty raz tylko lokalnie, możesz nie potrzebować takiej precyzji.

Ale w kodzie wielokrotnego użytku `ParamSpec` bardzo szybko się opłaca.

## Typowe błędy początkujących

- typowanie dekoratorów jako `Callable[..., Any]` bez świadomości kosztu,
- mylenie `TypeVar` z `ParamSpec`,
- brak rozróżnienia między typem zwracanym a typami argumentów,
- kopiowanie skomplikowanego kodu z internetu bez zrozumienia.

## Mini scenariusz praktyczny

Masz dekorator:

- logujący wywołania,
- mierzący czas,
- dodający retry,
- opakowujący błędy.

Jeśli chcesz, by dekorowana funkcja nadal była dobrze typowana, `ParamSpec` jest jednym z najlepszych narzędzi.

## Szybka ściąga

- `ParamSpec` opisuje parametry funkcji,
- `P.args` i `P.kwargs` pozwalają przenieść sygnaturę do wrappera,
- najczęściej używany przy dekoratorach,
- dobrze współpracuje z `TypeVar` dla typu zwracanego.

## Ćwiczenia

1. Napisz dekorator logujący z `ParamSpec`.
2. Napisz dekorator mierzący czas wykonania.
3. Porównaj dekorator z `Callable[..., Any]` i z `ParamSpec`.
4. Wyjaśnij, co dokładnie tracisz bez `ParamSpec`.
5. Zastanów się, które dekoratory z Twojego kodu warto byłoby opisać w ten sposób.

## Najważniejsze do zapamiętania

- `ParamSpec` służy do zachowywania informacji o parametrach funkcji.
- Jest szczególnie ważny przy dekoratorach.
- `Callable[..., Any]` bywa wygodne, ale traci precyzję.
- `ParamSpec` bardzo poprawia jakość typowania reusable wrapperów.
- To jedno z najbardziej praktycznych narzędzi zaawansowanego typingu.
