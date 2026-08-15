# `@overload` w Pythonie

## O co chodzi

`@overload` pozwala opisać kilka możliwych kontraktów tej samej funkcji.

Jest przydatny wtedy, gdy:

- funkcja przy różnych typach wejściowych zwraca różne typy wyjściowe,
- zwykły `Union` jest zbyt mało precyzyjny,
- chcesz lepiej opisać API dla użytkownika i checkera typów.

## Problem bez `@overload`

Załóżmy funkcję:

```python
def normalize(value: int | str) -> int | str:
    if isinstance(value, int):
        return value
    return value.strip()
```

To działa, ale checker widzi tylko:

- wejście: `int | str`,
- wyjście: `int | str`.

A Ty wiesz coś bardziej precyzyjnego:

- dla `int` zwraca `int`,
- dla `str` zwraca `str`.

## Intuicja

`@overload` pozwala rozdzielić te przypadki na poziomie deklaracji typów.

## Podstawowy przykład

```python
from typing import overload


@overload
def normalize(value: int) -> int:
    ...


@overload
def normalize(value: str) -> str:
    ...


def normalize(value: int | str) -> int | str:
    if isinstance(value, int):
        return value
    return value.strip()
```

To daje checkerowi bardziej precyzyjną wiedzę o funkcji.

## Co ważne

Przeciążenia `@overload` są deklaracjami typów.

Prawdziwa implementacja i tak jest jedna.

Czyli:

- kilka podpisów,
- jedna realna funkcja.

## Kiedy `Union` wystarcza, a kiedy nie

### `Union` wystarcza

Gdy nie zależy Ci na precyzyjnej relacji wejście -> wyjście.

### `@overload` ma sens

Gdy chcesz dokładnie opisać:

- ten typ wejścia daje taki typ wyniku,
- inny typ wejścia daje inny typ wyniku.

To bardzo poprawia ergonomię API.

## Przykład użycia

```python
print(normalize(10))
print(normalize("  Python  "))
```

Output:

```python
10
Python
```

## Kiedy `@overload` ma sens praktycznie

Szczególnie przy:

- helperach narzędziowych,
- parserach,
- funkcjach akceptujących kilka różnych trybów wejścia,
- API bibliotek, które mają być bardzo czytelne dla użytkownika.

## Kiedy nie przesadzać

Jeśli funkcja ma jeden prosty kontrakt albo `Union` jest w pełni wystarczający, nie trzeba dodawać `@overload` tylko dla ozdoby.

## Typowe błędy początkujących

- oczekiwanie, że `@overload` zastąpi implementację,
- dodawanie przeciążeń do bardzo prostych funkcji bez wartości praktycznej,
- niespójność między overloadami a realną implementacją,
- mieszanie precyzyjnych deklaracji z bardzo ogólną logiką runtime.

## Mini scenariusz praktyczny

Masz funkcję, która:

- dla ścieżki zwraca treść pliku,
- dla listy ścieżek zwraca listę treści,
- dla flagi zwraca inny kształt wyniku.

W takich API `@overload` potrafi bardzo pomóc użytkownikowi i narzędziom.

## Szybka ściąga

- `@overload` opisuje kilka kontraktów jednej funkcji,
- implementacja pozostaje jedna,
- przydaje się tam, gdzie typ wyniku zależy od typu wejścia,
- daje większą precyzję niż sam `Union`.

## Ćwiczenia

1. Napisz funkcję z overloadem dla `int` i `str`.
2. Porównaj wersję z `Union` i wersję z `@overload`.
3. Opisz przypadek, gdzie overload daje realną wartość.
4. Znajdź funkcję w swoim kodzie, która zmienia typ wyniku zależnie od wejścia.
5. Uzasadnij, kiedy `@overload` jest przesadą.

## Najważniejsze do zapamiętania

- `@overload` pozwala precyzyjnie opisać kilka kontraktów jednej funkcji.
- Jest szczególnie przydatny, gdy typ wyjścia zależy od typu wejścia.
- Daje większą precyzję niż sam `Union`.
- Nie zastępuje implementacji runtime.
- Ma sens wtedy, gdy realnie poprawia API i czytelność typów.
