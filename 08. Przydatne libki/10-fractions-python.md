# `fractions` w Pythonie

## Wprowadzenie

`fractions` pozwala pracować na dokładnych ułamkach.

To niszowsze narzędzie niż `decimal`, ale bardzo przydatne wtedy, gdy chcesz:

- zachować dokładny ułamek,
- uniknąć błędów `float`,
- reprezentować wynik jako proporcję, a nie przybliżenie dziesiętne.

## Najprostszy przykład

```python
from fractions import Fraction

value = Fraction(1, 3)
print(value)
```

Output:

```python
1/3
```

To nie jest przybliżenie `0.333333...`, tylko dokładny ułamek.

## Dodawanie ułamków

```python
from fractions import Fraction

result = Fraction(1, 3) + Fraction(1, 6)
print(result)
```

Output:

```python
1/2
```

## Automatyczne skracanie

```python
from fractions import Fraction

print(Fraction(2, 4))
print(Fraction(10, 20))
```

Output:

```python
1/2
1/2
```

To bardzo wygodne, bo moduł sam upraszcza wynik.

## `Fraction` z liczby dziesiętnej jako string

```python
from fractions import Fraction

print(Fraction("0.5"))
print(Fraction("1.25"))
```

Output:

```python
1/2
5/4
```

## `Fraction` vs `float`

```python
print(1 / 3)
```

Output:

```python
0.3333333333333333
```

To przybliżenie.

Natomiast:

```python
from fractions import Fraction

print(Fraction(1, 3))
```

Output:

```python
1/3
```

## `Fraction` a `Decimal`

### `Fraction`

Lepsze, gdy:

- chcesz dokładny ułamek,
- pracujesz na proporcjach,
- wynik ma zachować postać wymierną.

### `Decimal`

Lepsze, gdy:

- liczysz pieniądze,
- chcesz kontrolować miejsca po przecinku,
- myślisz w systemie dziesiętnym.

## Mini case study

Masz przepis:

- 1/2 szklanki mleka,
- 1/3 szklanki oleju.

```python
from fractions import Fraction

total = Fraction(1, 2) + Fraction(1, 3)
print(total)
```

Output:

```python
5/6
```

To dużo bardziej naturalne niż ręczne liczenie na przybliżeniach.

## Typowe błędy

- używanie `Fraction` tam, gdzie biznes oczekuje kwot w systemie dziesiętnym,
- mylenie `Fraction` z lepszym `Decimal`,
- brak świadomości, że to narzędzie do trochę innych problemów.

## Dobre praktyki

- używaj `Fraction`, gdy problem jest naprawdę "ułamkowy",
- używaj `Decimal`, gdy problem jest finansowy,
- nie wciskaj `Fraction` tam, gdzie zwykły `float` lub `Decimal` są naturalniejsze.

## Zadania

1. Dodaj `1/3` i `1/6` przez `Fraction`.
2. Pokaż, że `Fraction(2, 4)` upraszcza się do `1/2`.
3. Porównaj `1/3` jako `float` i jako `Fraction`.
4. Opisz, kiedy lepszy jest `Fraction`, a kiedy `Decimal`.
