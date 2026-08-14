# Testy oparte na właściwościach — `hypothesis` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym są testy oparte na właściwościach](#czym-są-testy-oparte-na-właściwościach)
3. [Jak to się różni od zwykłych testów](#jak-to-się-różni-od-zwykłych-testów)
4. [Dlaczego `hypothesis` jest ważne](#dlaczego-hypothesis-jest-ważne)
5. [Strategie danych](#strategie-danych)
6. [Najprostszy test `hypothesis`](#najprostszy-test-hypothesis)
7. [Co to jest właściwość](#co-to-jest-właściwość)
8. [Przykłady dobrych właściwości](#przykłady-dobrych-właściwości)
9. [Przykłady słabych właściwości](#przykłady-słabych-właściwości)
10. [Shrinkowanie danych](#shrinkowanie-danych)
11. [Typowe zastosowania](#typowe-zastosowania)
12. [Typowe błędy początkujących](#typowe-błędy-początkujących)
13. [Praktyczne przykłady](#praktyczne-przykłady)
14. [Dobre praktyki](#dobre-praktyki)
15. [Podsumowanie](#podsumowanie)
16. [Mini ściąga](#mini-ściąga)
17. [Ćwiczenia](#ćwiczenia)
18. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Zwykłe testy najczęściej działają tak:

- wybierasz kilka konkretnych danych,
- sprawdzasz wynik.

`hypothesis` działa inaczej:

- opisujesz właściwość,
- narzędzie samo generuje wiele danych testowych.

To bardzo potężne podejście, bo może znaleźć przypadki, o których sam byś nie pomyślał.

---

## Czym są testy oparte na właściwościach

To testy, w których nie skupiasz się na kilku ręcznie wybranych przykładach, tylko na ogólnej zasadzie, która powinna być prawdziwa.

Przykład właściwości:

"Po posortowaniu lista powinna mieć tę samą długość co wcześniej."

albo:

"Odwrócenie listy dwa razy powinno dać tę samą listę."

---

## Jak to się różni od zwykłych testów

### Zwykły test

Sprawdza konkretne przypadki.

### Test property-based

Sprawdza ogólne własności dla wielu automatycznie generowanych danych.

Oba podejścia są wartościowe i często się uzupełniają.

---

## Dlaczego `hypothesis` jest ważne

Bo:

- generuje dużo przypadków,
- potrafi znaleźć nietypowe wejścia,
- zmniejsza ryzyko pominięcia ważnych edge case’ów,
- umie uprościć dane prowadzące do błędu.

---

## Strategie danych

`hypothesis` generuje dane przez strategie.

Najczęściej importuje się:

```python
from hypothesis import given
from hypothesis import strategies as st
```

Na przykład:

- `st.integers()`
- `st.text()`
- `st.lists(...)`

---

## Najprostszy test `hypothesis`

```python
from hypothesis import given
from hypothesis import strategies as st

@given(st.integers())
def test_podwojenie_jest_parzyste(x):
    assert (x * 2) % 2 == 0
```

Tu `hypothesis` sam wygeneruje wiele liczb.

---

## Co to jest właściwość

Właściwość to ogólna zasada, która zawsze powinna być prawdziwa.

Na przykład:

- wynik sortowania ma tę samą długość,
- odwrócenie dwa razy daje oryginał,
- suma nie zależy od kolejności dwóch liczb,
- funkcja nie powinna rzucać błędu dla poprawnych danych.

---

## Przykłady dobrych właściwości

- `sorted(xs)` ma długość równą `len(xs)`
- `list(reversed(list(reversed(xs)))) == xs`
- dla dodatnich `x`, `sqrt(x) ** 2` jest blisko `x`

Właściwość powinna być:

- ogólna,
- sensowna,
- powiązana z logiką programu.

---

## Przykłady słabych właściwości

Słaba właściwość to taka, która prawie nic nie sprawdza.

Na przykład:

"funkcja zwraca coś"

To za mało.

Chcesz sprawdzać realne zasady działania programu.

---

## Shrinkowanie danych

Jedna z największych zalet `hypothesis`.

Jeśli znajdzie błąd, próbuje znaleźć prostszy przypadek wejściowy, który nadal ten błąd powoduje.

To bardzo pomaga w debugowaniu.

---

## Typowe zastosowania

- algorytmy,
- parsery,
- walidacja danych,
- operacje na listach i stringach,
- własne struktury danych,
- funkcje matematyczne i transformacje danych.

---

## Typowe błędy początkujących

- mylenie property-based testing z losowym testowaniem bez sensu,
- wybieranie złych właściwości,
- pisanie zbyt słabych asercji,
- brak zrozumienia, że `hypothesis` nie zastępuje wszystkich zwykłych testów.

---

## Praktyczne przykłady

### Odwrócenie dwa razy

```python
from hypothesis import given
from hypothesis import strategies as st

@given(st.lists(st.integers()))
def test_reverse_reverse(xs):
    assert list(reversed(list(reversed(xs)))) == xs
```

### Sortowanie nie zmienia długości

```python
@given(st.lists(st.integers()))
def test_sort_len(xs):
    assert len(sorted(xs)) == len(xs)
```

### Łączenie stringów

```python
@given(st.text(), st.text())
def test_concat_len(a, b):
    assert len(a + b) == len(a) + len(b)
```

---

## Dobre praktyki

### Najpierw zrozum właściwość, potem pisz test

### Łącz `hypothesis` ze zwykłymi testami przykładowymi

### Nie próbuj na siłę robić wszystkiego property-based

### Używaj tego tam, gdzie dane wejściowe mają dużo możliwych kombinacji

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- `hypothesis` generuje dane testowe automatycznie,
- testujesz właściwości, nie tylko pojedyncze przykłady,
- to świetne narzędzie do szukania trudnych przypadków brzegowych,
- szczególnie przydaje się w bardziej ogólnych algorytmach i transformacjach danych.

---

## Mini ściąga

```python
from hypothesis import given
from hypothesis import strategies as st

@given(st.integers())
def test_x(x):
    ...
```

---

## Ćwiczenia

### Ćwiczenie 1

Napisz test, że podwojenie liczby zawsze daje liczbę parzystą.

### Ćwiczenie 2

Napisz test, że długość po sortowaniu listy się nie zmienia.

### Ćwiczenie 3

Napisz test, że odwrócenie listy dwa razy daje oryginał.

---

## Przykładowe rozwiązania

```python
from hypothesis import given
from hypothesis import strategies as st

@given(st.integers())
def test_double_even(x):
    assert (x * 2) % 2 == 0
```
