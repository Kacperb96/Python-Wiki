# Operatory logiczne i arytmetyczne w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym są operatory](#czym-są-operatory)
3. [Operandy i wynik działania](#operandy-i-wynik-działania)
4. [Podział operatorów](#podział-operatorów)
5. [Operatory arytmetyczne](#operatory-arytmetyczne)
6. [Dodawanie `+`](#dodawanie-)
7. [Odejmowanie `-`](#odejmowanie--)
8. [Mnożenie `*`](#mnożenie-)
9. [Dzielenie `/`](#dzielenie-)
10. [Dzielenie całkowite `//`](#dzielenie-całkowite-)
11. [Reszta z dzielenia `%`](#reszta-z-dzielenia-)
12. [Potęgowanie `**`](#potęgowanie-)
13. [Kolejność wykonywania działań](#kolejność-wykonywania-działań)
14. [Operatory przypisania z działaniem](#operatory-przypisania-z-działaniem)
15. [Operatory arytmetyczne a typy danych](#operatory-arytmetyczne-a-typy-danych)
16. [Najczęstsze pułapki arytmetyczne](#najczęstsze-pułapki-arytmetyczne)
17. [Operatory porównania](#operatory-porównania)
18. [Operatory logiczne](#operatory-logiczne)
19. [Operator `and`](#operator-and)
20. [Operator `or`](#operator-or)
21. [Operator `not`](#operator-not)
22. [Łączenie warunków](#łączenie-warunków)
23. [Krótkie obliczanie warunków](#krótkie-obliczanie-warunków)
24. [Prawda i fałsz w Pythonie](#prawda-i-fałsz-w-pythonie)
25. [Różnica między `==` a `is`](#różnica-między--a-is)
26. [Typowe błędy początkujących](#typowe-błędy-początkujących)
27. [Praktyczne przykłady](#praktyczne-przykłady)
28. [Dobre praktyki](#dobre-praktyki)
29. [Podsumowanie](#podsumowanie)
30. [Mini ściąga](#mini-ściąga)
31. [Ćwiczenia](#ćwiczenia)
32. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Operatory to jeden z najważniejszych tematów w Pythonie.

Dzięki nim możemy:

- wykonywać obliczenia,
- porównywać wartości,
- sprawdzać warunki,
- łączyć kilka warunków w jedną całość,
- budować logikę programu.

Jeśli zmienne są danymi, to operatory są narzędziami, które coś z tymi danymi robią.

---

## Czym są operatory

Operator to specjalny znak lub słowo, które mówi Pythonowi, jaką operację wykonać.

Przykład:

```python
2 + 3
```

Tutaj:

- `2` i `3` to wartości,
- `+` to operator,
- wynik to `5`.

Inny przykład:

```python
5 > 3
```

Tutaj:

- `5` i `3` to wartości,
- `>` to operator porównania,
- wynik to `True`.

---

## Operandy i wynik działania

W działaniu takim jak:

```python
10 - 4
```

`10` i `4` to **operandy**, czyli wartości, na których działa operator.

Wynik działania operatora jest nową wartością.

To ważne, bo większość operatorów niczego nie "drukuje". Po prostu zwraca wynik, który potem możesz:

- przypisać do zmiennej,
- wykorzystać w `if`,
- przekazać do funkcji.

---

## Podział operatorów

W Pythonie mamy wiele rodzajów operatorów. W tym poradniku najważniejsze będą:

- arytmetyczne,
- porównania,
- logiczne,
- przypisania z działaniem.

### Arytmetyczne

Służą do obliczeń.

### Porównania

Sprawdzają relacje między wartościami.

### Logiczne

Łączą warunki lub odwracają ich wynik.

### Przypisania z działaniem

Pozwalają skrócić zapis typu `x = x + 1`.

---

## Operatory arytmetyczne

Najważniejsze:

| Operator | Znaczenie | Przykład | Wynik |
|---|---|---|---|
| `+` | dodawanie | `2 + 3` | `5` |
| `-` | odejmowanie | `7 - 2` | `5` |
| `*` | mnożenie | `4 * 3` | `12` |
| `/` | dzielenie | `10 / 2` | `5.0` |
| `//` | dzielenie całkowite | `10 // 3` | `3` |
| `%` | reszta z dzielenia | `10 % 3` | `1` |
| `**` | potęgowanie | `2 ** 3` | `8` |

---

## Dodawanie `+`

```python
print(2 + 3)
print(10 + 7)
```

Output:

```python
5
17
```

Można też dodawać zmienne:

```python
a = 5
b = 8
print(a + b)
```

Output:

```python
13
```

Jeśli w działaniu pojawia się `float`, wynik zwykle też będzie `float`.

```python
print(2 + 3.5)
```

Output:

```python
5.5
```

Operator `+` działa też na innych typach:

```python
print("Ala" + " ma kota")
print([1, 2] + [3, 4])
```

Output:

```python
Ala ma kota
[1, 2, 3, 4]
```

To ważna lekcja: zachowanie operatora zależy od typu.

---

## Odejmowanie `-`

```python
print(10 - 3)
print(5 - 8)
```

Output:

```python
7
-3
```

Odejmowanie jest typowo liczbowe.

Przy okazji warto zauważyć liczby ujemne:

```python
saldo = 100 - 150
print(saldo)
```

Output:

```python
-50
```

---

## Mnożenie `*`

```python
print(4 * 3)
print(2.5 * 2)
```

Output:

```python
12
5.0
```

Operator `*` działa też na stringach:

```python
print("ha" * 3)
```

Output:

```python
hahaha
```

I na listach:

```python
print([1, 2] * 2)
```

Output:

```python
[1, 2, 1, 2]
```

To przydatne, ale trzeba uważać, bo przy bardziej złożonych mutowalnych strukturach może dawać pułapki.

---

## Dzielenie `/`

```python
print(10 / 2)
print(7 / 2)
```

Output:

```python
5.0
3.5
```

W Pythonie `/` zawsze zwraca `float`, nawet jeśli wynik wygląda "całkowicie".

```python
print(4 / 2)   # 2.0
```

Output:

```python
2.0
```

Dzielenie przez zero:

```python
# print(10 / 0)
```

spowoduje `ZeroDivisionError`.

---

## Dzielenie całkowite `//`

```python
print(10 // 3)
print(7 // 2)
```

Output:

```python
3
3
```

To dzielenie z obcięciem części ułamkowej w dół zgodnie z zasadami Pythona.

Uwaga:

```python
print(-7 // 2)
```

Output:

```python
-4
```

To może zaskoczyć początkujących, bo wynik nie jest po prostu "ucięciem cyferek", tylko wynika z reguł matematycznych zaokrąglania w dół.

---

## Reszta z dzielenia `%`

```python
print(10 % 3)
print(8 % 2)
```

Output:

```python
1
0
```

To bardzo przydatny operator, np. do sprawdzania parzystości:

```python
print(4 % 2 == 0)
```

Output:

```python
True
```

---

## Potęgowanie `**`

```python
print(2 ** 3)
print(5 ** 2)
```

Output:

```python
8
25
```

To znaczy:

- `2 ** 3` to `2 * 2 * 2`
- `5 ** 2` to `25`

---

## Kolejność wykonywania działań

Python przestrzega standardowych zasad matematycznych:

- nawiasy,
- potęgowanie,
- mnożenie i dzielenie,
- dodawanie i odejmowanie.

Przykład:

```python
print(2 + 3 * 4)
print((2 + 3) * 4)
```

Output:

```python
14
20
```

Jeśli zależy Ci na pełnej czytelności, używaj nawiasów nawet wtedy, gdy formalnie nie są konieczne.

---

## Operatory przypisania z działaniem

Zamiast:

```python
x = x + 1
```

możesz napisać:

```python
x += 1
```

Podobnie:

- `-=`
- `*=`
- `/=`
- `//=`
- `%=`

Przykład:

```python
punkty = 10
punkty += 5
print(punkty)
```

Output:

```python
15
```

---

## Operatory arytmetyczne a typy danych

Nie każda operacja ma sens dla każdego typu.

```python
print("Ala" + " ma kota")
```

działa, ale:

```python
# print("5" + 5)
```

da `TypeError`.

Python nie zgaduje automatycznie, że chcesz połączyć string z liczbą. Musisz zdecydować sam:

```python
print("5" + str(5))
print(int("5") + 5)
```

Output:

```python
55
10
```

---

## Najczęstsze pułapki arytmetyczne

- mylenie `/` i `//`,
- zapominanie, że `/` daje `float`,
- dzielenie przez zero,
- mylenie stringa `"5"` z liczbą `5`,
- używanie `%` bez rozumienia, do czego służy.

---

## Operatory porównania

Najważniejsze:

| Operator | Znaczenie |
|---|---|
| `==` | równe |
| `!=` | różne |
| `>` | większe |
| `<` | mniejsze |
| `>=` | większe lub równe |
| `<=` | mniejsze lub równe |

Przykłady:

```python
print(5 == 5)
print(5 != 3)
print(7 > 2)
print(4 <= 4)
```

Output:

```python
True
True
True
True
```

Wynikiem porównania jest `bool`.

---

## Operatory logiczne

Najważniejsze:

- `and`
- `or`
- `not`

Służą do łączenia warunków albo odwracania ich sensu.

---

## Operator `and`

`and` zwraca prawdę tylko wtedy, gdy oba warunki są prawdziwe.

```python
wiek = 20
ma_bilet = True

print(wiek >= 18 and ma_bilet)
```

Output:

```python
True
```

---

## Operator `or`

`or` zwraca prawdę, jeśli przynajmniej jeden warunek jest prawdziwy.

```python
print(5 > 10 or 3 < 4)
```

Output:

```python
True
```

---

## Operator `not`

`not` odwraca wartość logiczną.

```python
print(not True)
print(not False)
```

Output:

```python
False
True
```

Przydaje się np. przy pustych kolekcjach:

```python
lista = []
if not lista:
    print("lista pusta")
```

---

## Łączenie warunków

Możesz łączyć warunki:

```python
wiek = 22
ma_dokument = True

if wiek >= 18 and ma_dokument:
    print("wejscie dozwolone")
```

Albo:

```python
if wiek < 18 or not ma_dokument:
    print("wejscie zabronione")
```

W bardziej złożonych przypadkach warto używać nawiasów dla czytelności.

---

## Krótkie obliczanie warunków

Python stosuje tzw. short-circuit evaluation.

To znaczy:

- w `and` jeśli pierwszy warunek jest falsy, Python nie sprawdza dalej,
- w `or` jeśli pierwszy warunek jest truthy, Python nie sprawdza dalej.

Przykład:

```python
x = 0
print(x != 0 and 10 / x > 1)
```

Output:

```python
False
```

To się nie wywali, bo drugi warunek nie zostanie już sprawdzony.

To bardzo ważne i praktyczne.

---

## Prawda i fałsz w Pythonie

Nie tylko `True` i `False` biorą udział w logice.

Falsy są m.in.:

- `0`
- `0.0`
- `""`
- `[]`
- `{}`
- `None`

To temat szerzej rozwinięty w:

- [04-none-truthy-falsy-python.md](/home/kacper/Desktop/Python/01.%20Fundamenty/04-none-truthy-falsy-python.md)

---

## Różnica między `==` a `is`

`==` porównuje wartości.
`is` porównuje tożsamość obiektu.

To temat na tyle ważny, że został szerzej rozwinięty osobno:

- [05-is-vs-rowne-python.md](/home/kacper/Desktop/Python/01.%20Fundamenty/05-is-vs-rowne-python.md)

---

## Typowe błędy początkujących

- mylenie `=` z `==`,
- mylenie `/` z `//`,
- dzielenie przez zero,
- składanie stringa i liczby bez konwersji,
- używanie `is` do zwykłych porównań wartości,
- pisanie warunków bez zrozumienia `and`, `or`, `not`.

---

## Praktyczne przykłady

### Sprawdzenie parzystości

```python
liczba = 8
print(liczba % 2 == 0)
```

### Sprawdzenie przedziału

```python
wiek = 20
print(wiek >= 18 and wiek < 65)
```

### Bezpieczny warunek z short-circuit

```python
tekst = ""
if tekst and tekst[0] == "A":
    print("zaczyna sie od A")
```

---

## Dobre praktyki

- pisz warunki jasno, nawet kosztem jednej linijki więcej,
- używaj nawiasów, gdy poprawiają czytelność,
- rozumiej typy danych biorące udział w operacji,
- nie zakładaj, że operator zawsze znaczy to samo dla każdego typu,
- testuj małe przykłady w interpreterze.

---

## Podsumowanie

Operatory są wszędzie w Pythonie.

Najważniejsze rzeczy do opanowania:

- działania arytmetyczne,
- porównania,
- logika warunków,
- short-circuit,
- wpływ typu danych na działanie operatora.

---

## Mini ściąga

```python
print(2 + 3)
print(7 // 2)
print(7 % 2)
print(2 ** 3)

print(5 > 3 and 2 < 4)
print(not False)
```

---

## Ćwiczenia

1. Wczytaj dwie liczby i wypisz wszystkie podstawowe działania.
2. Sprawdź, czy liczba jest parzysta.
3. Sprawdź, czy liczba mieści się w przedziale.
4. Pokaż różnicę między `/` i `//`.
5. Napisz warunek z `and`, `or`, `not`.

---

## Przykładowe rozwiązania

### 1. Działania

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
```

### 2. Parzystość

```python
liczba = 12
print(liczba % 2 == 0)
```

### 3. Przedział

```python
x = 7
print(x >= 1 and x <= 10)
```

### 4. `/` kontra `//`

```python
print(7 / 2)
print(7 // 2)
```

### 5. Logika

```python
ma_login = True
ma_haslo = False

print(ma_login and ma_haslo)
print(ma_login or ma_haslo)
print(not ma_haslo)
```
