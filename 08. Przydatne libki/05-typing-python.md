# `typing` w Pythonie

## Wprowadzenie

`typing` wspiera statyczne typowanie w Pythonie.

Python nadal pozostaje językiem dynamicznym, ale adnotacje typów pomagają:

- czytać kod,
- łapać błędy wcześniej,
- lepiej wspierać IDE,
- łatwiej rozwijać większy projekt.

## Po co używać `typing`

Typy są bardzo przydatne jako kontrakt.

Dają odpowiedź na pytania:

- co funkcja przyjmuje,
- co funkcja zwraca,
- jakiej struktury oczekuje kod,
- kiedy `None` jest możliwe,
- jaki callback ma być przekazany.

## Kiedy `typing` ma sens

Szczególnie wtedy, gdy:

- projekt rośnie,
- masz więcej funkcji i modułów,
- pracujesz z innymi ludźmi,
- wracasz do kodu po czasie,
- zależy Ci na wsparciu narzędzi jak mypy.

## Kiedy nie przesadzać

Typy mają pomagać, a nie dominować nad kodem.

Jeśli adnotacje robią się bardziej skomplikowane niż sama logika, trzeba się zatrzymać i zapytać, czy to naprawdę daje wartość.

## Adnotacje typów

```python
def add(a: int, b: int) -> int:
    return a + b

print(add(2, 3))
```

Output:

```python
5
```

## Typy podstawowe

Najczęstsze:

- `int`,
- `str`,
- `float`,
- `bool`,
- `list`,
- `dict`.

```python
name: str = "Anna"
age: int = 30
```

## `list[str]`, `dict[str, int]`

Nowoczesny zapis:

```python
def process(data: list[str]) -> dict[str, int]:
    return {x: len(x) for x in data}

print(process(["Ala", "Python"]))
```

Output:

```python
{'Ala': 3, 'Python': 6}
```

## `Optional` i `Union`

W nowoczesnym Pythonie często używa się składni z `|`.

```python
def find_user(user_id: int) -> str | None:
    if user_id == 1:
        return "Anna"
    return None
```

To znaczy, że funkcja może zwrócić tekst albo brak wyniku.

## `Callable`

Do opisu funkcji przekazywanych jako argument.

```python
from typing import Callable

def run(f: Callable[[int], int], x: int) -> int:
    return f(x)

print(run(lambda x: x * 2, 5))
```

Output:

```python
10
```

## `Literal` i `TypeAlias`

```python
from typing import Literal, TypeAlias

Mode: TypeAlias = Literal["dev", "prod"]

def set_mode(mode: Mode) -> None:
    print(mode)
```

To jest świetne, gdy dopuszczasz tylko kilka konkretnych wariantów.

## `TypedDict`

Do opisu słowników o znanej strukturze.

```python
from typing import TypedDict

class User(TypedDict):
    name: str
    age: int

user: User = {"name": "Anna", "age": 30}
print(user["name"])
```

Output:

```python
Anna
```

To bardzo przydatne przy danych JSON-like.

## `typing` vs brak typów

### Gdy typy wygrywają

- funkcje używane w wielu miejscach,
- moduły narzędziowe,
- dane wejściowe o znanej strukturze,
- callbacki,
- większe projekty.

### Gdy nie warto przesadzać

- bardzo krótki jednorazowy skrypt,
- sytuacja, gdzie adnotacje są gęstsze niż sama logika,
- eksperyment albo throwaway code.

Nie znaczy to, że w małym kodzie typy są złe. Po prostu nie zawsze trzeba iść w pełny formalizm.

## `typing` a runtime

To ważne: same adnotacje typów nie wymuszają typów podczas działania programu.

One pomagają:

- człowiekowi,
- IDE,
- statycznym analizatorom.

Jeśli chcesz walidacji runtime, zwykle potrzebujesz dodatkowych narzędzi albo jawnych checków.

## Typowe błędy początkujących

- mylenie typowania z walidacją runtime,
- nadużywanie `Any`,
- brak oznaczenia `None`, gdy funkcja realnie może go zwrócić,
- tworzenie bardzo skomplikowanych typów bez korzyści,
- kopiowanie adnotacji bez rozumienia ich celu.

## Mini scenariusz praktyczny

Masz parser danych użytkownika i kilka funkcji, które pracują na słownikach, callbackach i opcjonalnych wynikach.

Tu `typing` potrafi znacząco poprawić czytelność i ograniczyć liczbę pomyłek przy rozwijaniu kodu.

## Dobre praktyki

- zaczynaj od prostych i czytelnych typów,
- typuj publiczne funkcje i ważne modele danych,
- używaj `TypedDict`, gdy pracujesz z przewidywalnym słownikiem,
- nie traktuj `Any` jako ucieczki od myślenia,
- pamiętaj, że typowanie ma pomagać w utrzymaniu kodu.

## Szybka ściąga

Najczęściej przydatne:

- `list[str]`, `dict[str, int]`,
- `str | None`,
- `Callable`,
- `Literal`,
- `TypedDict`.

## Ćwiczenia

1. Dodaj typy do kilku prostych funkcji.
2. Zrób funkcję zwracającą `str | None`.
3. Użyj `Callable` w funkcji przyjmującej callback.
4. Utwórz `TypedDict` dla prostego JSON-a.
5. Opisz przypadek, gdzie typy pomagają bardziej niż komentarz tekstowy.

## Najważniejsze do zapamiętania

- `typing` poprawia komunikację i czytelność kodu.
- Typy są szczególnie wartościowe w większym i dłużej żyjącym kodzie.
- Adnotacje nie zastępują walidacji runtime.
- Nie warto przesadzać ze złożonością typów bez realnej potrzeby.
- Dobre typy pomagają myśleć o interfejsie funkcji i danych.
