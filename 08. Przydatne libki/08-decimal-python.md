# `decimal` w Pythonie

## Wprowadzenie

`decimal` służy do precyzyjnych obliczeń dziesiętnych.

Najczęściej pojawia się wtedy, gdy zwykły `float` zaczyna być problemem, na przykład przy:

- pieniądzach,
- podatkach,
- rabatach,
- zaokrągleniach biznesowych,
- raportach finansowych.

To bardzo ważne, bo początkujący często myślą:

`przeciez 0.1 to po prostu 0.1`

A dla `float` to nie zawsze jest tak proste.

## Problem z `float`

Zobacz klasyczny przykład:

```python
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
```

Output:

```python
0.30000000000000004
False
```

To nie jest "bug Pythona". To efekt sposobu reprezentowania liczb zmiennoprzecinkowych.

W wielu miejscach to jest akceptowalne.

Ale w finansach bardzo często nie chcesz takiego zachowania.

## Najprostszy `Decimal`

```python
from decimal import Decimal

print(Decimal("0.1") + Decimal("0.2"))
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
```

Output:

```python
0.3
True
```

To już jest dokładnie to, czego intuicyjnie oczekujesz.

## Bardzo ważna zasada

Jeśli używasz `Decimal`, to zwykle twórz go ze stringa, a nie z gotowego `float`.

### Dobrze

```python
Decimal("0.1")
```

### Źle lub co najmniej ryzykownie

```python
Decimal(0.1)
```

Sprawdźmy:

```python
from decimal import Decimal

print(Decimal(0.1))
print(Decimal("0.1"))
```

Output:

```python
0.1000000000000000055511151231257827021181583404541015625
0.1
```

To bardzo ważna pułapka.

`Decimal(0.1)` nie "naprawia" floata. On bierze jego już niedokładną reprezentację.

## Dodawanie i odejmowanie

```python
from decimal import Decimal

price = Decimal("19.90")
tax = Decimal("4.10")

total = price + tax
print(total)
```

Output:

```python
24.00
```

## Mnożenie w praktyce

```python
from decimal import Decimal

price = Decimal("12.50")
quantity = Decimal("3")

total = price * quantity
print(total)
```

Output:

```python
37.50
```

## Zaokrąglanie przez `quantize()`

To bardzo praktyczna rzecz.

```python
from decimal import Decimal

value = Decimal("19.999")
rounded = value.quantize(Decimal("0.01"))

print(rounded)
```

Output:

```python
20.00
```

To bardzo typowe przy kwotach pieniężnych.

## Przykład z rabatem

```python
from decimal import Decimal

price = Decimal("99.99")
discount = Decimal("0.10")

final_price = price * (Decimal("1") - discount)
print(final_price)
print(final_price.quantize(Decimal("0.01")))
```

Output:

```python
89.9910
89.99
```

Widzisz tu ważną rzecz:

- sam wynik obliczeń może mieć więcej miejsc,
- końcową prezentację często chcesz jawnie zaokrąglić.

## `float` vs `Decimal`

### `float`

Lepszy, gdy:

- liczysz naukowo,
- obrabiasz dane numeryczne,
- wydajność jest ważniejsza niż dziesiętna dokładność,
- drobny błąd reprezentacji jest akceptowalny.

### `Decimal`

Lepszy, gdy:

- liczysz pieniądze,
- chcesz przewidywalne wyniki dziesiętne,
- biznes oczekuje konkretnych zaokrągleń,
- wynik ma być "dokładnie jak w księgowości", a nie "w przybliżeniu".

## Typowe błędy początkujących

### 1. Mieszanie `float` i `Decimal`

Zły styl:

```python
from decimal import Decimal

price = Decimal("10.50")
tax = 1.25
```

To prowadzi do niespójności modelu danych.

Jeśli wchodzisz w `Decimal`, to zwykle trzymaj się go konsekwentnie.

### 2. Tworzenie `Decimal` z `float`

To już widzieliśmy. To częsta pułapka.

### 3. Brak jawnego zaokrąglenia na końcu

Jeśli system ma pokazywać kwoty do 2 miejsc po przecinku, trzeba to świadomie zrobić.

## Mini case study

Masz koszyk:

- produkt A: `19.90`
- produkt B: `5.10`
- rabat: `10%`

Wersja finansowa:

```python
from decimal import Decimal

subtotal = Decimal("19.90") + Decimal("5.10")
discounted = subtotal * Decimal("0.90")
final = discounted.quantize(Decimal("0.01"))

print(subtotal)
print(discounted)
print(final)
```

Output:

```python
25.00
22.5000
22.50
```

To jest bardzo naturalny use case dla `decimal`.

## Dobre praktyki

- używaj `Decimal("...")`, a nie `Decimal(0.1)`,
- nie mieszaj bez potrzeby `float` i `Decimal`,
- jawnie kontroluj zaokrąglenie końcowe,
- używaj `Decimal` tam, gdzie dokładność dziesiętna ma znaczenie biznesowe.

## Szybka ściąga

Najczęściej przydatne:

- `Decimal("0.1")`
- działania `+`, `-`, `*`, `/`
- `quantize(Decimal("0.01"))`

## Zadania

1. Pokaż różnicę między `0.1 + 0.2` dla `float` i dla `Decimal`.
2. Policz cenę 3 produktów po `19.99` z `Decimal`.
3. Policz rabat 15% i zaokrąglij wynik do 2 miejsc.
4. Wyjaśnij, czemu `Decimal(0.1)` to zły nawyk.
5. Opisz 3 sytuacje, w których `Decimal` ma sens w prawdziwym projekcie.
