# Walrus operator `:=` w Pythonie

## Wprowadzenie

`Walrus operator`, czyli `:=`, to operator przypisania w wyrażeniu.

Pozwala:

- przypisać wartość do zmiennej,
- i od razu użyć tej wartości w tym samym wyrażeniu.

To znaczy, że zamiast:

```python
text = input("Podaj tekst: ")
if text:
    print(text)
```

czasem możesz napisać:

```python
if text := input("Podaj tekst: "):
    print(text)
```

To jest wygodne, ale tylko wtedy, gdy rzeczywiście poprawia czytelność.

## 1. Co dokładnie robi `:=`

Zobacz prosty przykład:

```python
if (n := len("Python")) > 3:
    print(n)
```

Najpierw:

- `len("Python")` daje `6`,
- `6` trafia do `n`,
- potem warunek sprawdza `6 > 3`.

Output:

```python
6
```

Bez walrusa wyglądałoby to tak:

```python
n = len("Python")
if n > 3:
    print(n)
```

Obie wersje są poprawne. `Walrus` ma sens tylko tam, gdzie skraca kod bez pogarszania zrozumienia.

## 2. Najprostszy sensowny przypadek

```python
data = "abcdef"

if (size := len(data)) > 5:
    print(f"Dlugosc: {size}")
```

Output:

```python
Dlugosc: 6
```

Tu zaleta jest taka, że:

- liczysz `len(data)` raz,
- używasz wyniku w warunku,
- i od razu masz go do wypisania.

## 3. `Walrus` w `while`

To jeden z najbardziej naturalnych przypadków użycia.

Bez walrusa:

```python
line = input("Podaj cos: ")
while line != "koniec":
    print("Wpisales:", line)
    line = input("Podaj cos: ")
```

Z walrusem:

```python
while (line := input("Podaj cos: ")) != "koniec":
    print("Wpisales:", line)
```

Przykładowa sesja:

```text
Podaj cos: Ala
Wpisales: Ala
Podaj cos: kot
Wpisales: kot
Podaj cos: koniec
```

Tu `walrus` naprawdę upraszcza kod, bo usuwa powtarzające się pobieranie danych.

## 4. `Walrus` w `if`

```python
numbers = [1, 2, 3, 4]

if (count := len(numbers)) > 2:
    print("Za duzo elementow:", count)
```

Output:

```python
Za duzo elementow: 4
```

To jest czytelne, bo przypisanie i warunek są ściśle powiązane.

## 5. `Walrus` z `match`? Nie tędy droga

`Walrus` nie jest narzędziem do wszystkiego.

Nie chodzi o to, żeby wszędzie wciskać `:=`.

To nie jest:

- zamiennik zwykłego przypisania,
- sposób na "sprytniejszy" kod za wszelką cenę,
- obowiązkowy nowoczesny styl.

## 6. `Walrus` w list comprehensions

Da się go używać także w comprehension, ale tu trzeba uważać.

Przykład:

```python
words = ["python", "is", "great", "ok"]

lengths = [n for word in words if (n := len(word)) > 2]
print(lengths)
```

Output:

```python
[6, 5, 5]
```

To działa, ale dla części osób może być mniej czytelne niż wersja klasyczna:

```python
lengths = [len(word) for word in words if len(word) > 2]
```

Wniosek:

`to, że się da, nie znaczy, że zawsze warto`

## 7. `Walrus` przy regexie albo parsowaniu

To częsty praktyczny przypadek.

```python
import re

text = "Numer zamowienia: 12345"

if match := re.search(r"\d+", text):
    print("Znaleziono:", match.group())
```

Output:

```python
Znaleziono: 12345
```

Bez walrusa często pisałbyś:

```python
match = re.search(r"\d+", text)
if match:
    print("Znaleziono:", match.group())
```

Obie wersje są dobre. `Walrus` skraca ten bardzo częsty wzorzec.

## 8. `Walrus` przy odczycie danych

```python
values = ["10", "20", "", "30"]
index = 0

while index < len(values) and (value := values[index]):
    print("Mam wartosc:", value)
    index += 1
```

Output:

```python
Mam wartosc: 10
Mam wartosc: 20
```

Pętla zatrzyma się na pustym stringu `""`, bo jest falsy.

To pokazuje też ważną rzecz:

`walrus` bardzo często łączy się z truthy/falsy`

## 9. Pułapka: mylenie przypisania z porównaniem

Jeśli ktoś nie zna `:=`, może przez chwilę nie zauważyć, że to przypisanie.

Dlatego bardzo ważna jest czytelność.

Ten kod:

```python
if (result := compute()) > 10:
    print(result)
```

jest jeszcze okej.

Ale taki:

```python
if (a := f(x)) and (b := g(a)) and (c := h(b)) and c > 10:
    ...
```

jest już zwykle przesadnie zagęszczony.

## 10. Kiedy `walrus` jest dobry

Najczęściej wtedy, gdy:

- oszczędza powtórzenie tej samej operacji,
- przypisanie jest lokalne i krótkie,
- warunek i przypisana wartość są logicznie mocno związane,
- poprawia płynność czytania.

Typowe dobre miejsca:

- `while`,
- `if` z jednorazowym wynikiem,
- `re.search(...)`,
- parsowanie danych,
- pobranie długości lub wyniku kosztownego wywołania używanego od razu.

## 11. Kiedy `walrus` jest zły

Najczęściej wtedy, gdy:

- kod robi się zbyt sprytny,
- przypisanie ukrywa ważną logikę,
- trzeba się zatrzymać i dekodować składnię,
- zwykłe 2 linie są czytelniejsze.

Zły przykład:

```python
if ((x := get_x()) + (y := get_y()) + (z := get_z())) > 100:
    ...
```

To nie daje zysku czytelności.

## 12. `Walrus` a scope

`Walrus` przypisuje normalnie do zmiennej.

```python
if (n := len("abc")) > 0:
    print("w if:", n)

print("po if:", n)
```

Output:

```python
w if: 3
po if: 3
```

To nie jest zmienna "tylko na chwilę". Ona zostaje w bieżącym zakresie.

## 13. Porównanie: wersja dobra i przesadzona

### Wersja dobra

```python
import re

if match := re.search(r"\d+", "abc 123"):
    print(match.group())
```

Output:

```python
123
```

### Wersja przesadzona

```python
if (m := re.search(r"\d+", text)) and (value := int(m.group())) > 100 and (flag := value % 2 == 0):
    print(value, flag)
```

Technicznie może działać, ale czytelność mocno spada.

## 14. Mini case study

Masz parser linii wejściowych.

Bez walrusa:

```python
line = file.readline()
while line:
    print(line.strip())
    line = file.readline()
```

Z walrusem:

```python
while line := file.readline():
    print(line.strip())
```

To jest bardzo idiomatyczne i czytelne użycie.

## 15. Najważniejsza zasada

`Walrus` ma upraszczać, a nie imponować.

Jeśli po użyciu:

- kod jest krótszy,
- nie traci czytelności,
- naturalnie łączy obliczenie z warunkiem,

to dobrze.

Jeśli kod wygląda jak łamigłówka, to lepiej wrócić do zwykłego przypisania.

## Dobre praktyki

- używaj `:=` oszczędnie,
- preferuj proste przypadki,
- szczególnie rozważaj go w `while` i prostym `if`,
- unikaj zagnieżdżonych, wielokrotnych przypisań w jednym warunku,
- pamiętaj, że czytelność jest ważniejsza niż skrócenie kodu o jedną linijkę.

## Szybka ściąga

Najbardziej naturalne przypadki:

- `if (n := len(data)) > 0:`
- `while (line := input()) != "koniec":`
- `if match := re.search(...):`

## Zadania

1. Przepisz prostą pętlę `while` z ręcznym pobieraniem danych na wersję z `:=`.
2. Użyj `walrus operator` razem z `len()` w `if`.
3. Użyj `walrus operator` razem z `re.search()`.
4. Pokaż przykład, w którym `:=` poprawia czytelność.
5. Pokaż przykład, w którym `:=` pogarsza czytelność.
6. Wyjaśnij, czemu `walrus` nie powinien być używany wszędzie.
