# Counter w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `Counter`](#czym-jest-counter)
3. [Skąd importować `Counter`](#skąd-importować-counter)
4. [Do czego służy `Counter`](#do-czego-służy-counter)
5. [Tworzenie `Counter`](#tworzenie-counter)
6. [Liczenie elementów w liście](#liczenie-elementów-w-liście)
7. [Liczenie znaków w stringu](#liczenie-znaków-w-stringu)
8. [Dostęp do wartości](#dostęp-do-wartości)
9. [Brak klucza w `Counter`](#brak-klucza-w-counter)
10. [Najważniejsze metody](#najważniejsze-metody)
11. [`most_common()`](#most_common)
12. [`elements()`](#elements)
13. [`update()`](#update)
14. [`subtract()`](#subtract)
15. [Operacje matematyczne na `Counter`](#operacje-matematyczne-na-counter)
16. [Counter a zwykły słownik](#counter-a-zwykły-słownik)
17. [Typowe zastosowania](#typowe-zastosowania)
18. [Typowe błędy początkujących](#typowe-błędy-początkujących)
19. [Praktyczne przykłady](#praktyczne-przykłady)
20. [Dobre praktyki](#dobre-praktyki)
21. [Podsumowanie](#podsumowanie)
22. [Mini ściąga](#mini-ściąga)
23. [Ćwiczenia](#ćwiczenia)
24. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`Counter` to bardzo wygodna struktura z modułu `collections`, która służy do liczenia wystąpień elementów.

Zamiast pisać ręcznie:

```python
wynik = {}

for element in dane:
    if element in wynik:
        wynik[element] += 1
    else:
        wynik[element] = 1
```

możesz użyć:

```python
from collections import Counter

wynik = Counter(dane)
```

To dużo prostsze i bardzo pythonowe.

---

## Czym jest `Counter`

`Counter` to specjalny rodzaj słownika.

Najprościej:

**klucz to element, a wartość to liczba jego wystąpień.**

Przykład:

```python
from collections import Counter

licznik = Counter(["a", "b", "a", "c", "a", "b"])
print(licznik)
```

Wynik:

```python
Counter({'a': 3, 'b': 2, 'c': 1})
```

---

## Skąd importować `Counter`

`Counter` importuje się z modułu `collections`.

```python
from collections import Counter
```

To standardowa biblioteka Pythona, więc niczego nie trzeba doinstalowywać.

---

## Do czego służy `Counter`

Najczęstsze zastosowania:

- liczenie liter,
- liczenie słów,
- liczenie ocen,
- szukanie najczęstszych elementów,
- porównywanie częstotliwości,
- prosta analiza danych tekstowych.

---

## Tworzenie `Counter`

Można go utworzyć na kilka sposobów.

### Z listy

```python
Counter([1, 2, 2, 3, 3, 3])
```

### Ze stringa

```python
Counter("python")
```

### Ze słownika

```python
Counter({"a": 3, "b": 2})
```

### Z argumentów nazwanych

```python
Counter(a=3, b=2)
```

---

## Liczenie elementów w liście

```python
from collections import Counter

oceny = [5, 4, 5, 3, 4, 5, 2]
licznik = Counter(oceny)
print(licznik)
```

To bardzo wygodny sposób policzenia, ile razy występuje każda ocena.

---

## Liczenie znaków w stringu

```python
from collections import Counter

tekst = "ala ma kota"
licznik = Counter(tekst)
print(licznik)
```

`Counter` policzy wszystkie znaki, łącznie ze spacjami.

Jeśli nie chcesz spacji:

```python
licznik = Counter(znak for znak in tekst if znak != " ")
```

---

## Dostęp do wartości

`Counter` działa podobnie do słownika.

```python
from collections import Counter

licznik = Counter("banana")
print(licznik["a"])
print(licznik["b"])
```

---

## Brak klucza w `Counter`

To bardzo wygodna cecha.

W zwykłym słowniku odczyt nieistniejącego klucza przez `[]` daje `KeyError`.

W `Counter`:

```python
from collections import Counter

licznik = Counter("abc")
print(licznik["z"])
```

wynik to:

```python
0
```

To bardzo praktyczne.

---

## Najważniejsze metody

Najczęściej używane:

- `most_common()`
- `elements()`
- `update()`
- `subtract()`

---

## `most_common()`

Zwraca najczęstsze elementy.

```python
from collections import Counter

licznik = Counter("banana")
print(licznik.most_common())
```

### Najczęstszy jeden

```python
print(licznik.most_common(1))
```

### Najczęstsze dwa

```python
print(licznik.most_common(2))
```

To jedna z najważniejszych metod `Counter`.

---

## `elements()`

Zwraca iterator, który oddaje elementy tyle razy, ile wynosi ich licznik.

```python
from collections import Counter

licznik = Counter({"a": 2, "b": 1})
print(list(licznik.elements()))
```

Wynik:

```python
['a', 'a', 'b']
```

---

## `update()`

Dodaje nowe zliczenia.

```python
from collections import Counter

licznik = Counter("abc")
licznik.update("aba")
print(licznik)
```

To nie nadpisuje wartości, tylko je zwiększa.

---

## `subtract()`

Odejmuje zliczenia.

```python
from collections import Counter

licznik = Counter("banana")
licznik.subtract("ana")
print(licznik)
```

To przydaje się przy porównywaniu częstotliwości.

---

## Operacje matematyczne na `Counter`

`Counter` wspiera różne operacje:

### Dodawanie

```python
from collections import Counter

a = Counter("abca")
b = Counter("bccd")

print(a + b)
```

### Odejmowanie

```python
print(a - b)
```

### Część wspólna

```python
print(a & b)
```

### Suma maksymalnych liczników

```python
print(a | b)
```

To już bardziej zaawansowane, ale bardzo przydatne.

---

## Counter a zwykły słownik

`Counter` zachowuje się podobnie do `dict`, ale:

- automatycznie liczy wystąpienia,
- brakujący klucz daje `0`,
- ma metody związane z liczeniem.

To świetny wybór, gdy Twoje dane są typu:

"ile razy coś wystąpiło?"

---

## Typowe zastosowania

- analiza tekstu,
- ranking najczęstszych słów,
- liczenie ocen,
- liczenie głosów,
- porównywanie częstotliwości liter.

---

## Typowe błędy początkujących

### 1. Oczekiwanie zwykłego zachowania `dict`

`Counter` ma trochę inne zachowanie przy brakującym kluczu.

### 2. Nierozumienie `update()`

To nie jest zwykłe nadpisywanie.

### 3. Zapominanie, że `Counter` liczy elementy iterowalne znak po znaku

Dla stringa liczy litery, nie całe słowa.

---

## Praktyczne przykłady

### Liczenie słów

```python
from collections import Counter

slowa = ["kot", "pies", "kot", "ptak", "kot", "pies"]
print(Counter(slowa))
```

### Najczęstsza litera

```python
from collections import Counter

tekst = "programowanie"
licznik = Counter(tekst)
print(licznik.most_common(1))
```

### Ranking ocen

```python
from collections import Counter

oceny = [5, 4, 5, 3, 5, 4, 2]
print(Counter(oceny).most_common())
```

---

## Dobre praktyki

### Używaj `Counter`, gdy naprawdę liczysz wystąpienia

Nie używaj go na siłę do wszystkiego.

### Korzystaj z `most_common()`

To jedna z największych zalet tej struktury.

### Pamiętaj, że to nadal słownikopodobna struktura

Możesz iterować po niej podobnie jak po słowniku.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- `Counter` pochodzi z `collections`,
- służy do liczenia wystąpień,
- działa podobnie do słownika,
- brakujący klucz daje `0`,
- `most_common()` to bardzo ważna metoda,
- `update()` i `subtract()` modyfikują liczniki,
- świetnie nadaje się do analizy danych i tekstu.

---

## Mini ściąga

```python
from collections import Counter

Counter([1, 2, 2, 3])
Counter("banana")
licznik["a"]
licznik.most_common()
licznik.most_common(1)
list(licznik.elements())
licznik.update("abc")
licznik.subtract("ab")
```

---

## Ćwiczenia

### Ćwiczenie 1

Policz wystąpienia liter w słowie `"informatyka"`.

### Ćwiczenie 2

Znajdź najczęstszą ocenę w liście ocen.

### Ćwiczenie 3

Policz słowa w liście wyrazów i wypisz dwa najczęstsze.

---

## Przykładowe rozwiązania

### Ćwiczenie 1

```python
from collections import Counter

print(Counter("informatyka"))
```

### Ćwiczenie 2

```python
from collections import Counter

oceny = [5, 4, 5, 3, 5, 4]
print(Counter(oceny).most_common(1))
```

### Ćwiczenie 3

```python
from collections import Counter

slowa = ["kot", "pies", "kot", "ptak", "pies", "kot"]
print(Counter(slowa).most_common(2))
```
