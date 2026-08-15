# `TypeGuard` w Pythonie

## O co chodzi

`TypeGuard` pozwala powiedzieć checkerowi typów:

- jeśli ta funkcja zwróci `True`,
- to sprawdzana wartość ma już węższy, bardziej konkretny typ.

To bardzo praktyczne przy własnych funkcjach walidujących i zawężających typ.

## Problem bez `TypeGuard`

Załóżmy, że masz funkcję:

```python
def is_str_list(value: list[object]) -> bool:
    return all(isinstance(x, str) for x in value)
```

Człowiek widzi, co ona robi.

Ale checker typów po `if is_str_list(data):` nie zawsze wie, że teraz `data` można traktować jako `list[str]`.

## Intuicja

`TypeGuard` nie zmienia runtime magicznie.

On daje bardziej precyzyjną informację typom statycznym:

- jeśli warunek przeszedł,
- traktuj obiekt jako konkretniejszy typ.

## Podstawowy przykład

```python
from typing import TypeGuard


def is_str_list(value: list[object]) -> TypeGuard[list[str]]:
    return all(isinstance(x, str) for x in value)
```

Teraz checker może zrozumieć, że po przejściu tego checka typ listy jest zawężony.

## Przykład użycia

```python
from typing import TypeGuard


def is_str_list(value: list[object]) -> TypeGuard[list[str]]:
    return all(isinstance(x, str) for x in value)


data: list[object] = ["a", "b", "c"]

if is_str_list(data):
    print(", ".join(data))
```

Output:

```python
a, b, c
```

Bez `TypeGuard` checker może nie wiedzieć, że `join()` jest tu bezpieczne dla `list[str]`.

## `bool` vs `TypeGuard`

### `bool`

Mówi tylko:

- funkcja zwraca prawdę albo fałsz.

### `TypeGuard`

Mówi dodatkowo:

- jeśli zwróci `True`, to badana wartość ma konkretniejszy typ.

To ogromna różnica dla statycznej analizy.

## Kiedy `TypeGuard` ma sens

Szczególnie gdy:

- masz własne helpery typu `is_valid_xxx`,
- filtrujesz dane o szerokim typie,
- pracujesz na `Union` albo danych wejściowych z wielu źródeł,
- chcesz lepiej opisać przepływ walidacji.

## Kiedy nie komplikować na siłę

Jeśli zwykły `isinstance()` w miejscu użycia jest prostszy i w pełni wystarcza, to nie trzeba zawsze robić osobnego `TypeGuard`.

`TypeGuard` jest świetny tam, gdzie logika sprawdzania jest wspólna i wielokrotnie używana.

## Mini przykład z `Union`

Wyobraź sobie dane typu:

```python
str | list[str]
```

Własny checker może pozwolić bardziej czytelnie zawężać logikę dalszego przetwarzania.

To szczególnie przydatne w parserach, walidatorach i adapterach danych.

## Typowe błędy początkujących

- mylenie `TypeGuard` z walidacją runtime jako taką,
- oczekiwanie, że `TypeGuard` zrobi coś magicznego bez poprawnej logiki checkera,
- używanie go wszędzie zamiast prostego `isinstance()`,
- zwracanie nieprecyzyjnych checkerów, które nie dają realnego zawężenia.

## Mini scenariusz praktyczny

Masz dane z JSON-a, które po wstępnym parsowaniu są szeroko typowane. Potem chcesz przechodzić do coraz pewniejszych struktur.

Własne `TypeGuard` mogą wtedy bardzo poprawić czytelność kodu i pomóc checkerom.

## Szybka ściąga

- `TypeGuard[T]` oznacza: jeśli funkcja zwróci `True`, wartość można traktować jak `T`,
- jest przydatny do zawężania typu,
- dobrze pasuje do helperów walidujących,
- nie zastępuje poprawnej logiki sprawdzania runtime.

## Ćwiczenia

1. Napisz `TypeGuard` dla listy stringów.
2. Napisz `TypeGuard` dla słownika o prostym kształcie.
3. Porównaj zwykłe `bool` i `TypeGuard` dla tego samego checkera.
4. Znajdź miejsce, gdzie własny checker poprawiłby czytelność parsera danych.
5. Zastanów się, kiedy zwykły `isinstance()` jest lepszy niż osobny `TypeGuard`.

## Najważniejsze do zapamiętania

- `TypeGuard` pomaga statycznie zawężać typ po własnej funkcji sprawdzającej.
- Jest bardziej precyzyjny niż zwykły `bool`.
- Największą wartość daje przy reusable checkerach i szerokich typach wejściowych.
- Nie zastępuje poprawnego sprawdzania runtime.
- To bardzo praktyczne narzędzie w parserach, walidatorach i adapterach danych.
