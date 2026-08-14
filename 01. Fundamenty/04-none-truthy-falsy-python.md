# `None`, truthy i falsy w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `None`](#czym-jest-none)
3. [Kiedy pojawia się `None`](#kiedy-pojawia-się-none)
4. [`None` nie jest pustym stringiem ani zerem](#none-nie-jest-pustym-stringiem-ani-zerem)
5. [Truthy i falsy](#truthy-i-falsy)
6. [Najczęstsze wartości falsy](#najczęstsze-wartości-falsy)
7. [Jak Python ocenia warunki](#jak-python-ocenia-warunki)
8. [`if x` kontra `if x is None`](#if-x-kontra-if-x-is-none)
9. [Falsy nie oznacza braku danych](#falsy-nie-oznacza-braku-danych)
10. [Pułapka domyślnych wartości z `or`](#pułapka-domyślnych-wartości-z-or)
11. [`and` i `or` z wartościami nietypu `bool`](#and-i-or-z-wartościami-nietypu-bool)
12. [`any()` i `all()` a truthy/falsy](#any-i-all-a-truthyfalsy)
13. [Falsy w praktyce aplikacyjnej](#falsy-w-praktyce-aplikacyjnej)
14. [Typowe pułapki początkujących](#typowe-pułapki-początkujących)
15. [Praktyczne przykłady](#praktyczne-przykłady)
16. [Dobre praktyki](#dobre-praktyki)
17. [Podsumowanie](#podsumowanie)
18. [Mini ściąga](#mini-ściąga)
19. [Ćwiczenia](#ćwiczenia)
20. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`None`, truthy i falsy to temat prosty na wejściu, ale bardzo ważny w praktyce.

To właśnie tutaj początkujący często:

- mylą brak wartości z pustą wartością,
- źle sprawdzają warunki,
- używają `== None` zamiast `is None`,
- traktują `0`, `""`, `[]` i `None` jak to samo.

Żeby pisać czytelny Python, trzeba dobrze rozumieć te różnice.

---

## Czym jest `None`

`None` oznacza brak wartości.

```python
wynik = None
```

To specjalny singleton w Pythonie. W praktyce oznacza to, że istnieje jedna szczególna wartość `None`, a nie wiele różnych obiektów tego typu.

Typ:

```python
print(type(None))
```

Zobaczysz `NoneType`.

---

## Kiedy pojawia się `None`

Najczęściej:

- funkcja nie ma jawnego `return`,
- chcesz oznaczyć, że coś nie zostało znalezione,
- wartość jeszcze nie została ustawiona,
- operacja się nie udała i chcesz to jawnie zakomunikować.

Przykład:

```python
def przywitaj():
    print("Czesc")

wynik = przywitaj()
print(wynik)
```

Funkcja nic nie zwraca jawnie, więc wynik to `None`.

---

## `None` nie jest pustym stringiem ani zerem

To bardzo ważne:

- `None` to brak wartości,
- `""` to istniejący, ale pusty tekst,
- `[]` to istniejąca, ale pusta lista,
- `0` to konkretna wartość liczbowa.

Przykład:

```python
print(None == "")
print(None == 0)
print(None == [])
```

Wszystko będzie `False`.

---

## Truthy i falsy

W Pythonie wiele obiektów da się ocenić logicznie.

W warunku:

- obiekt truthy zachowuje się jak `True`,
- obiekt falsy zachowuje się jak `False`.

To nie znaczy, że obiekt jest dosłownie typu `bool`. To znaczy tylko, że Python potrafi go tak zinterpretować w kontekście logicznym.

---

## Najczęstsze wartości falsy

Najważniejsze:

- `False`
- `None`
- `0`
- `0.0`
- `""`
- `[]`
- `{}`
- `set()`
- `range(0)`

Przykład:

```python
if "":
    print("to sie nie wykona")

if [1, 2]:
    print("to sie wykona")
```

Output:

```python
to sie wykona
```

---

## Jak Python ocenia warunki

Przykład:

```python
dane = []

if dane:
    print("lista ma elementy")
else:
    print("lista jest pusta")
```

Output:

```python
lista jest pusta
```

To jest normalny, idiomatyczny Python.

Nie musisz pisać:

```python
if len(dane) > 0:
```

w prostych przypadkach.

Tak samo dla stringów:

```python
tekst = "abc"
if tekst:
    print("jest tekst")
```

Output:

```python
jest tekst
```

---

## `if x` kontra `if x is None`

To jedna z najważniejszych różnic.

### `if x`

Pyta:

"czy `x` jest truthy?"

To nie odróżnia `None` od innych wartości falsy.

### `if x is None`

Pyta:

"czy `x` jest dokładnie brakiem wartości?"

Przykład:

```python
x = 0

if not x:
    print("x jest falsy")

if x is None:
    print("x jest None")
```

Output:

```python
x jest falsy
```

Tutaj wykona się tylko pierwszy warunek.

---

## Falsy nie oznacza braku danych

To częsta pułapka.

Przykład:

```python
wiek = 0
```

`0` jest falsy, ale przecież to nadal może być poprawna wartość.

Albo:

```python
nazwa = ""
```

To pusty string, ale nadal istniejąca wartość.

Jeśli naprawdę chcesz odróżnić brak danych od pustej wartości, musisz jawnie sprawdzać `is None`.

---

## Pułapka domyślnych wartości z `or`

Częsty idiom:

```python
nazwa = user_input or "Anonim"
```

To bywa wygodne, ale trzeba uważać.

Jeśli `user_input` jest:

- `None`,
- `""`,
- `0`,

to dostaniesz `"Anonim"`.

To może być dobre albo błędne, zależnie od celu.

Przykład problemu:

```python
port = 0
realny_port = port or 8000
print(realny_port)
```

Output:

```python
8000
```

Tu `0` zostanie potraktowane jak brak wartości, choć może być świadomie podaną wartością.

Lepszy wariant, gdy chodzi konkretnie o `None`:

```python
realny_port = 8000 if port is None else port
```

---

## `and` i `or` z wartościami nietypu `bool`

W Pythonie `and` i `or` nie zawsze zwracają `True` albo `False`. Często zwracają jeden z operandów.

Przykłady:

```python
print("" or "domyslna wartosc")
print("tekst" and 123)
print(None or "backup")
```

Output:

```python
domyslna wartosc
123
backup
```

Najprostsza intuicja:

- `or` zwraca pierwszą truthy wartość,
- `and` zwraca pierwszą falsy wartość albo ostatnią, jeśli wszystkie są truthy.

Dlatego:

```python
print(0 or 5)      # 5
print(7 and 9)     # 9
print("" and 100)  # ""
```

Output:

```python
5
9

```

W trzecim przypadku wypisze się pusty string, więc wizualnie zobaczysz pustą linię.

---

## `any()` i `all()` a truthy/falsy

`any()` sprawdza, czy istnieje choć jeden element truthy.

```python
print(any([0, "", None, 5]))
```

Output:

```python
True
```

`all()` sprawdza, czy wszystkie elementy są truthy.

```python
print(all([1, "a", [1]]))
```

Output:

```python
True
```

Ważny edge case:

```python
print(all([]))
print(any([]))
```

Output:

```python
True
False
```

Wyniki:

- `all([])` to `True`
- `any([])` to `False`

To może zaskoczyć, ale jest zgodne z definicją logiczną tych funkcji.

---

## Falsy w praktyce aplikacyjnej

To temat, który wraca bardzo często.

Przykłady realnych sytuacji:

- wynik wyszukiwania może być `None`, ale lista wyników może być `[]`,
- wiek użytkownika może być `0`,
- liczba punktów może być `0`,
- pole tekstowe może być pustym stringiem,
- flaga może być `False`.

Jeśli wszystko potraktujesz jednym `if not x`, łatwo pomieszać różne stany programu.

---

## Typowe pułapki początkujących

- mylenie `None` z `0`, `""` albo `[]`,
- używanie `if not x`, gdy trzeba odróżnić `None` od pustej wartości,
- sprawdzanie `== None` zamiast `is None`,
- zakładanie, że `and` i `or` zawsze zwracają `bool`,
- błędne użycie `any()` i `all()` bez zrozumienia truthy/falsy,
- traktowanie `or` jako uniwersalnego mechanizmu defaultów.

---

## Praktyczne przykłady

### Funkcja zwracająca `None`

```python
def parse_int(tekst):
    try:
        return int(tekst)
    except ValueError:
        return None
```

### Odróżnienie pustego stringa od braku danych

```python
tekst = ""

if tekst is None:
    print("brak danych")
elif not tekst:
    print("tekst jest pusty")
```

Output:

```python
tekst jest pusty
```

### Liczenie elementów truthy i falsy

```python
dane = [0, 1, "", "Python", [], [1], None, True]
truthy = sum(1 for x in dane if x)
falsy = sum(1 for x in dane if not x)

print(truthy, falsy)
```

Output:

```python
4 4
```

### Pułapka z `or`

```python
wartosc = 0
wynik = wartosc or 100
print(wynik)
```

Output:

```python
100
```

---

## Dobre praktyki

- używaj `is None`, gdy chcesz sprawdzić brak wartości,
- używaj prostego `if lista:` do sprawdzania, czy kolekcja ma elementy,
- nie utożsamiaj każdej wartości falsy z błędem,
- pisz warunki tak, by jasno wynikało, czy sprawdzasz pustkę, czy brak danych,
- ostrożnie używaj `or` do ustawiania wartości domyślnych.

---

## Podsumowanie

Najważniejsze rozróżnienie:

- `None` oznacza brak wartości,
- falsy oznacza, że obiekt w warunku zachowuje się jak `False`.

To nie jest to samo.

Jeśli dobrze zrozumiesz tę różnicę, unikniesz wielu bardzo typowych błędów.

---

## Mini ściąga

```python
if x is None:
    print("brak wartosci")

if not x:
    print("wartosc jest falsy")

dane = [0, 1, "", "abc"]
print(sum(1 for x in dane if x))
print(sum(1 for x in dane if not x))
```

Najważniejsze:

- `None` to brak wartości,
- `None`, `0`, `""`, `[]` są falsy,
- `if x` sprawdza truthy/falsy,
- `if x is None` sprawdza dokładnie brak wartości.

---

## Ćwiczenia

1. Napisz funkcję, która zwraca `None`, jeśli nie uda się zamienić tekstu na liczbę.
2. Pokaż różnicę między `if x` i `if x is None` dla wartości `0`.
3. Przygotuj listę z wartościami truthy i falsy i policz je.
4. Sprawdź warunkiem `if`, czy lista jest pusta, bez porównywania do `[]`.
5. Napisz program, który rozróżnia `None`, pusty string i niepusty string.
6. Pokaż pułapkę z `or` i wartością `0`.

---

## Przykładowe rozwiązania

### 1. `parse_int`

```python
def parse_int(tekst):
    try:
        return int(tekst)
    except ValueError:
        return None
```

### 2. `0` kontra `None`

```python
x = 0

if not x:
    print("x jest falsy")

if x is None:
    print("x jest None")
```

### 3. Liczenie truthy i falsy

```python
dane = [0, 1, "", "Python", None]
print(sum(1 for x in dane if x))
print(sum(1 for x in dane if not x))
```

### 4. Pusta lista

```python
lista = []
if not lista:
    print("pusta")
```

### 5. Rozróżnienie stanów

```python
tekst = ""

if tekst is None:
    print("brak wartosci")
elif tekst == "":
    print("pusty string")
else:
    print("jest tekst")
```

### 6. `or`

```python
wartosc = 0
print(wartosc or 100)
```
