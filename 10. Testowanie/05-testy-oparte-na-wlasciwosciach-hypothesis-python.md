# Testy oparte na właściwościach — `hypothesis`

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym są testy oparte na właściwościach](#czym-są-testy-oparte-na-właściwościach)
3. [Jak różnią się od zwykłych testów](#jak-różnią-się-od-zwykłych-testów)
4. [Dlaczego `hypothesis` jest ważne](#dlaczego-hypothesis-jest-ważne)
5. [Strategie danych](#strategie-danych)
6. [Najprostszy test `hypothesis`](#najprostszy-test-hypothesis)
7. [Czym jest dobra właściwość](#czym-jest-dobra-właściwość)
8. [Przykłady dobrych właściwości](#przykłady-dobrych-właściwości)
9. [Przykłady słabych właściwości](#przykłady-słabych-właściwości)
10. [Shrinkowanie danych](#shrinkowanie-danych)
11. [Przykładowy błąd znaleziony przez `hypothesis`](#przykładowy-błąd-znaleziony-przez-hypothesis)
12. [Kiedy warto używać `hypothesis`](#kiedy-warto-używać-hypothesis)
13. [Typowe błędy początkujących](#typowe-błędy-początkujących)
14. [Praktyczna ściąga](#praktyczna-ściąga)
15. [Ćwiczenia](#ćwiczenia)
16. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

Zwykłe testy najczęściej działają tak:

- wybierasz kilka konkretnych danych wejściowych,
- sprawdzasz oczekiwany wynik.

`hypothesis` działa inaczej.

Tutaj opisujesz właściwość, czyli ogólną zasadę, która zawsze powinna być prawdziwa, a narzędzie samo generuje wiele danych testowych.

To bardzo mocne podejście, bo może znaleźć przypadki, o których sam byś nie pomyślał.

---

## Czym są testy oparte na właściwościach

To testy, które nie skupiają się na kilku ręcznie wybranych przykładach, tylko na regule ogólnej.

Przykład zwykłego testu:

```python
assert sorted([3, 1, 2]) == [1, 2, 3]
```

Przykład myślenia property-based:

- posortowana lista powinna mieć tę samą długość,
- posortowana lista powinna zawierać te same elementy,
- wynik sortowania powinien być uporządkowany niemalejąco.

---

## Jak różnią się od zwykłych testów

### Zwykły test

Sprawdza konkretny przypadek.

### Test property-based

Sprawdza ogólną własność dla wielu automatycznie generowanych danych.

Oba podejścia są wartościowe.

One się nie wykluczają.

Najczęściej się uzupełniają.

---

## Dlaczego `hypothesis` jest ważne

Bo:

- generuje dużo przypadków,
- szuka nietypowych wejść,
- zmniejsza ryzyko pominięcia edge case'ów,
- potrafi uprościć dane prowadzące do błędu,
- pomaga myśleć o logice programu bardziej ogólnie.

To nie jest narzędzie do wszystkiego, ale bywa bardzo skuteczne.

---

## Strategie danych

`hypothesis` generuje dane za pomocą strategii.

Najczęstszy import:

```python
from hypothesis import given
from hypothesis import strategies as st
```

Przykłady strategii:

- `st.integers()`
- `st.text()`
- `st.lists(st.integers())`
- `st.booleans()`

To właśnie z nich budujesz dane wejściowe dla testu.

---

## Najprostszy test `hypothesis`

```python
from hypothesis import given
from hypothesis import strategies as st


@given(st.integers())
def test_podwojenie_jest_parzyste(x):
    assert (x * 2) % 2 == 0
```

Tu `hypothesis` sam wygeneruje wiele różnych liczb całkowitych.

Ty opisujesz tylko zasadę.

---

## Czym jest dobra właściwość

Dobra właściwość jest:

- ogólna,
- prawdziwa dla wszystkich poprawnych danych z danego zakresu,
- związana z realnym zachowaniem programu,
- na tyle konkretna, żeby wykryć błąd.

Zła właściwość to taka, która brzmi efektownie, ale praktycznie niczego nie sprawdza.

---

## Przykłady dobrych właściwości

### Odwrócenie listy dwa razy

```python
from hypothesis import given
from hypothesis import strategies as st


@given(st.lists(st.integers()))
def test_reverse_reverse_daje_oryginal(xs):
    assert list(reversed(list(reversed(xs)))) == xs
```

### Sortowanie nie zmienia długości

```python
@given(st.lists(st.integers()))
def test_sortowanie_nie_zmienia_dlugosci(xs):
    assert len(sorted(xs)) == len(xs)
```

### Dodawanie jest przemienne

```python
@given(st.integers(), st.integers())
def test_dodawanie_jest_przemienne(a, b):
    assert a + b == b + a
```

To są realne, sensowne zasady.

---

## Przykłady słabych właściwości

Słaba właściwość:

- "funkcja coś zwraca",
- "program się nie wywala",
- "wynik istnieje".

Takie testy zwykle są za słabe, bo nie sprawdzają zachowania, tylko sam fakt wykonania.

---

## Shrinkowanie danych

To jedna z największych zalet `hypothesis`.

Jeśli narzędzie znajdzie przypadek powodujący błąd, próbuje go uprościć do jak najmniejszego kontrprzykładu.

To bardzo pomaga w debugowaniu.

Zamiast dostać ogromną losową strukturę danych, możesz dostać minimalny przypadek, który dalej łamie program.

---

## Przykładowy błąd znaleziony przez `hypothesis`

Załóżmy błędną funkcję:

```python
def pierwszy_element(xs: list[int]) -> int:
    return xs[0]
```

I test:

```python
from hypothesis import given
from hypothesis import strategies as st


@given(st.lists(st.integers()))
def test_pierwszy_element_dziala(xs):
    assert pierwszy_element(xs) == xs[0]
```

Ten test jest źle pomyślany, bo lista może być pusta.

`hypothesis` może znaleźć taki kontrprzykład.

Uproszczony przykład raportu:

```text
Falsifying example: test_pierwszy_element_dziala(xs=[])
IndexError: list index out of range
```

To bardzo cenna informacja.

Pokazuje dokładnie, jaki przypadek łamie kod.

---

## Kiedy warto używać `hypothesis`

`hypothesis` szczególnie dobrze sprawdza się wtedy, gdy:

- masz dużo możliwych kombinacji danych,
- chcesz sprawdzać ogólne własności funkcji,
- pracujesz na parserach, normalizacji danych, kolekcjach, przekształceniach,
- podejrzewasz, że ręczne przykłady nie pokrywają edge case'ów.

Nie zawsze jest to pierwszy wybór.

Dla bardzo prostych funkcji zwykłe testy często są wystarczające.

---

## Typowe błędy początkujących

- wybieranie właściwości, które nic nie znaczą,
- mylenie property-based tests z losowym zgadywaniem,
- brak zawężenia danych wejściowych, gdy domena powinna być ograniczona,
- próba użycia `hypothesis` tam, gdzie zwykły test jest prostszy i czytelniejszy,
- brak zrozumienia, że narzędzie może znaleźć błąd w samym założeniu testu.

---

## Praktyczna ściąga

### Import

```python
from hypothesis import given
from hypothesis import strategies as st
```

### Jedna liczba

```python
@given(st.integers())
def test_cos(x):
    ...
```

### Lista liczb

```python
@given(st.lists(st.integers()))
def test_lista(xs):
    ...
```

### Co warto sobie zadać

- Jaka ogólna zasada ma być zawsze prawdziwa?
- Czy ta właściwość naprawdę coś sprawdza?
- Czy zakres danych ma sens?
- Czy zwykły test nie byłby tu prostszy?

---

## Ćwiczenia

1. Napisz test property-based dla przemienności dodawania.
2. Napisz test właściwości: odwrócenie listy dwa razy daje oryginał.
3. Napisz test właściwości: sortowanie nie zmienia długości listy.
4. Napisz test dla funkcji normalizującej string i wymyśl do niej sensowną właściwość.
5. Napisz celowo błędną funkcję i sprawdź, czy `hypothesis` znajdzie kontrprzykład.
6. Spróbuj opisać własnymi słowami, dlaczego test property-based nie zastępuje wszystkich zwykłych testów.
7. Wymyśl jedną dobrą i jedną słabą właściwość dla tej samej funkcji.
8. Przeanalizuj raport błędu z `Falsifying example` i wyjaśnij, co on oznacza.

---

## Najważniejsze do zapamiętania

- `hypothesis` generuje wiele danych i sprawdza ogólne właściwości.
- Test property-based nie zastępuje zwykłych testów, tylko je uzupełnia.
- Dobra właściwość musi być ogólna i naprawdę związana z logiką programu.
- Jedną z największych zalet jest shrinkowanie kontrprzykładów.
- To świetne narzędzie do znajdowania edge case'ów, których sam mógłbyś nie wymyślić.
