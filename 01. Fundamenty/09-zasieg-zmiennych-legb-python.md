# Zasięg zmiennych (LEGB) w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest zasięg zmiennej](#czym-jest-zasięg-zmiennej)
3. [Dlaczego zasięg zmiennych jest ważny](#dlaczego-zasięg-zmiennych-jest-ważny)
4. [Podstawowy pomysł: skąd Python bierze zmienną](#podstawowy-pomysł-skąd-python-bierze-zmienną)
5. [Zasada LEGB](#zasada-legb)
6. [L jak Local](#l-jak-local)
7. [E jak Enclosing](#e-jak-enclosing)
8. [G jak Global](#g-jak-global)
9. [B jak Built-in](#b-jak-built-in)
10. [Kolejność wyszukiwania nazw](#kolejność-wyszukiwania-nazw)
11. [Zmienne lokalne](#zmienne-lokalne)
12. [Zmienne globalne](#zmienne-globalne)
13. [Różnica między odczytem a modyfikacją](#różnica-między-odczytem-a-modyfikacją)
14. [Słowo kluczowe `global`](#słowo-kluczowe-global)
15. [Funkcje zagnieżdżone](#funkcje-zagnieżdżone)
16. [Słowo kluczowe `nonlocal`](#słowo-kluczowe-nonlocal)
17. [Closures i pamiętanie stanu](#closures-i-pamiętanie-stanu)
18. [Pułapka `UnboundLocalError`](#pułapka-unboundlocalerror)
19. [Zasięg a instrukcje `if`, `for`, `while`](#zasięg-a-instrukcje-if-for-while)
20. [Zasięg a comprehensions](#zasięg-a-comprehensions)
21. [Zasięg a argumenty funkcji](#zasięg-a-argumenty-funkcji)
22. [Mutowalne i niemutowalne obiekty a zasięg](#mutowalne-i-niemutowalne-obiekty-a-zasięg)
23. [Cieniowanie nazw](#cieniowanie-nazw)
24. [Nadpisywanie nazw wbudowanych](#nadpisywanie-nazw-wbudowanych)
25. [Dobre praktyki pracy z zasięgiem](#dobre-praktyki-pracy-z-zasięgiem)
26. [Typowe błędy początkujących](#typowe-błędy-początkujących)
27. [Praktyczne przykłady](#praktyczne-przykłady)
28. [Podsumowanie](#podsumowanie)
29. [Mini ściąga](#mini-ściąga)
30. [Ćwiczenia](#ćwiczenia)
31. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Zasięg zmiennych to temat, który na początku wydaje się trochę abstrakcyjny, ale w praktyce jest bardzo ważny.

To właśnie zasięg decyduje:

- gdzie dana zmienna jest widoczna,
- skąd Python bierze jej wartość,
- dlaczego czasem zmienna działa w jednym miejscu, a w innym daje błąd,
- kiedy trzeba użyć `global` albo `nonlocal`.

Ten temat nie jest tylko teorią. Bardzo często wyjaśnia dziwne zachowania programu.

---

## Czym jest zasięg zmiennej

Najprościej:

**zasięg zmiennej mówi, w jakiej części programu można używać danej nazwy.**

Przykład:

```python
def przywitaj():
    imie = "Ania"
    print(imie)
```

Zmienna `imie` istnieje tylko wewnątrz funkcji `przywitaj()`.

---

## Dlaczego zasięg zmiennych jest ważny

Bez zrozumienia zasięgu łatwo popełnić błędy takie jak:

- użycie zmiennej tam, gdzie nie istnieje,
- przypadkowe nadpisanie zmiennej globalnej,
- niezrozumienie, czemu funkcja nie zmienia wartości na zewnątrz,
- problemy z funkcjami zagnieżdżonymi,
- błędy typu `NameError` albo `UnboundLocalError`.

---

## Podstawowy pomysł: skąd Python bierze zmienną

Kiedy piszesz:

```python
print(x)
```

Python musi sprawdzić:

"skąd wziąć `x`?"

Nie zgaduje tego losowo. Ma określoną kolejność szukania nazw.

---

## Zasada LEGB

LEGB to skrót od:

- `L` - Local
- `E` - Enclosing
- `G` - Global
- `B` - Built-in

To kolejność, w jakiej Python szuka nazwy zmiennej.

Jeśli nazwa nie zostanie znaleziona na żadnym poziomie, pojawi się `NameError`.

---

## L jak Local

`Local` to zakres lokalny, czyli wnętrze aktualnie wykonywanej funkcji.

```python
def pokaz():
    x = 10
    print(x)
```

Output po wywołaniu `pokaz()`:

```python
10
```

Ta zmienna żyje tylko wewnątrz funkcji.

---

## E jak Enclosing

`Enclosing` to zakres funkcji otaczającej.

```python
def zewnetrzna():
    x = "zewnetrzne x"

    def wewnetrzna():
        print(x)

    wewnetrzna()
```

Output po wywołaniu `zewnetrzna()`:

```python
zewnetrzne x
```

Funkcja `wewnetrzna()` nie ma własnego `x`, więc Python szuka poziom wyżej.

---

## G jak Global

`Global` to poziom całego pliku, czyli modułu.

```python
x = 100

def pokaz():
    print(x)
```

Output po wywołaniu `pokaz()`:

```python
100
```

Jeśli funkcja nie znajdzie nazwy lokalnie, może sięgnąć do poziomu globalnego.

---

## B jak Built-in

Na końcu Python sprawdza nazwy wbudowane, takie jak:

- `print`
- `len`
- `sum`

Przykład:

```python
print(len([1, 2, 3]))
```

Jeśli nadpiszesz taką nazwę własną zmienną, możesz sobie narobić bałaganu.

---

## Kolejność wyszukiwania nazw

Python zawsze szuka od najbliższego zakresu do coraz dalszych:

1. Local
2. Enclosing
3. Global
4. Built-in

To bardzo ważne, bo tłumaczy, która wartość zostanie użyta, gdy ta sama nazwa istnieje w kilku miejscach.

---

## Zmienne lokalne

Zmienne lokalne są tworzone wewnątrz funkcji.

```python
def licz():
    wynik = 5
    print(wynik)
```

Poza funkcją `wynik` nie istnieje.

To dobry domyślny model pracy: większość zmiennych powinna być lokalna.

---

## Zmienne globalne

To zmienne zdefiniowane poza funkcjami.

```python
licznik = 0
```

Mogą być odczytywane wewnątrz funkcji:

```python
licznik = 0

def pokaz():
    print(licznik)
```

Output po wywołaniu `pokaz()`:

```python
0
```

Ale modyfikacja to osobny temat.

---

## Różnica między odczytem a modyfikacją

To kluczowa rzecz.

Odczyt globalnej zmiennej z funkcji zwykle działa:

```python
x = 10

def pokaz():
    print(x)
```

Ale jeśli spróbujesz ją modyfikować:

```python
x = 10

def zmien():
    x = x + 1
```

to dostaniesz problem, bo Python potraktuje `x` jako lokalne w tej funkcji.

---

## Słowo kluczowe `global`

Jeśli naprawdę chcesz modyfikować zmienną globalną w funkcji, możesz użyć `global`.

```python
licznik = 0

def zwieksz():
    global licznik
    licznik += 1
```

Jeśli wywołasz:

```python
zwieksz()
print(licznik)
```

to output będzie:

```python
1
```

To działa, ale należy używać ostrożnie.

Nadmierne używanie `global` zwykle prowadzi do kodu trudniejszego do śledzenia.

---

## Funkcje zagnieżdżone

Możesz definiować funkcję w funkcji:

```python
def outer():
    x = 10

    def inner():
        print(x)

    inner()
```

To właśnie miejsce, gdzie poziom `Enclosing` zaczyna być ważny.

---

## Słowo kluczowe `nonlocal`

Jeśli chcesz zmienić zmienną z funkcji otaczającej, ale nie globalną, używasz `nonlocal`.

```python
def outer():
    x = 10

    def inner():
        nonlocal x
        x += 1

    inner()
    print(x)
```

Output po wywołaniu `outer()`:

```python
11
```

To przydaje się głównie w funkcjach zagnieżdżonych.

---

## Closures i pamiętanie stanu

Funkcja wewnętrzna może zapamiętać wartości z zakresu otaczającego.

```python
def make_counter():
    x = 0

    def inc():
        nonlocal x
        x += 1
        return x

    return inc
```

Jeśli zrobisz:

```python
counter = make_counter()
print(counter())
print(counter())
```

to output będzie:

```python
1
2
```

To jest podstawowa idea closure.

Nie musisz jeszcze umieć budować złożonych closure, ale warto wiedzieć, że zakres enclosing może żyć dłużej, niż trwa samo wywołanie funkcji zewnętrznej.

---

## Pułapka `UnboundLocalError`

To jeden z klasycznych błędów.

```python
x = 10

def pokaz():
    print(x)
    x = 20
```

Python uzna, że skoro w funkcji przypisujesz do `x`, to `x` jest lokalne.
Ale próbujesz odczytać je przed przypisaniem.

To daje `UnboundLocalError`.

---

## Zasięg a instrukcje `if`, `for`, `while`

W Pythonie `if`, `for`, `while` nie tworzą osobnego zakresu tak jak funkcja.

```python
if True:
    x = 10

print(x)
```

Output:

```python
10
```

To zadziała.

Podobnie z pętlą:

```python
for i in range(3):
    pass

print(i)
```

Output:

```python
2
```

To ważna cecha języka.

---

## Zasięg a comprehensions

Comprehensions są trochę bardziej subtelne niż zwykłe pętle.

Na tym etapie wystarczy pamiętać, że zmienna użyta wewnątrz comprehension nie zachowuje się dokładnie tak samo jak zmienna ze zwykłego `for` w kontekście wychodzenia na zewnątrz.

To nie jest temat krytyczny na start, ale warto wiedzieć, że istnieje tu pewien niuans.

---

## Zasięg a argumenty funkcji

Argumenty funkcji są lokalnymi nazwami wewnątrz funkcji.

```python
def hello(imie):
    print(imie)
```

`imie` jest lokalne dla funkcji `hello`.

---

## Mutowalne i niemutowalne obiekty a zasięg

To temat, który często myli początkujących.

Jeśli przekazujesz listę do funkcji:

```python
def dodaj_element(lista):
    lista.append(10)
```

to funkcja może zmienić ten sam obiekt.

Ale jeśli przypiszesz nową wartość do nazwy lokalnej:

```python
def ustaw_zero(x):
    x = 0
```

to nie zmieniasz zewnętrznej zmiennej, tylko lokalną nazwę.

To nie jest tylko kwestia zakresu, ale też modelu obiektów i mutowalności.

---

## Cieniowanie nazw

Cieniowanie oznacza, że lokalna nazwa zasłania zewnętrzną nazwę o tej samej nazwie.

```python
x = 100

def pokaz():
    x = 5
    print(x)
```

W funkcji używane jest lokalne `x`, nie globalne.

---

## Nadpisywanie nazw wbudowanych

Bardzo zły nawyk:

```python
list = [1, 2, 3]
str = "tekst"
sum = 10
```

To psuje dostęp do nazw wbudowanych.

Potem:

```python
# print(sum([1, 2, 3]))
```

może już nie działać tak, jak oczekujesz.

---

## Dobre praktyki pracy z zasięgiem

- domyślnie używaj zmiennych lokalnych,
- unikaj `global`, jeśli nie jest naprawdę potrzebne,
- nie nadpisuj nazw wbudowanych,
- dawaj zmiennym czytelne nazwy,
- rozbijaj logikę na małe funkcje, bo to upraszcza zakresy.

---

## Typowe błędy początkujących

- oczekiwanie, że zmienna z funkcji będzie dostępna poza nią,
- przypadkowe cieniowanie nazw,
- niezrozumienie `UnboundLocalError`,
- nadużywanie `global`,
- nadpisywanie nazw takich jak `list`, `str`, `sum`.

---

## Praktyczne przykłady

### Zmienna lokalna

```python
def f():
    x = 10
    print(x)
```

### Odczyt globalnej

```python
x = 5

def f():
    print(x)
```

### `global`

```python
licznik = 0

def inc():
    global licznik
    licznik += 1
```

### `nonlocal`

```python
def outer():
    x = 1

    def inner():
        nonlocal x
        x += 1

    inner()
    print(x)
```

---

## Podsumowanie

Zasięg zmiennych wyjaśnia, skąd Python bierze nazwy i dlaczego czasem coś działa albo nie działa.

Najważniejsze do zapamiętania:

- LEGB,
- różnica między odczytem a modyfikacją,
- sens `global` i `nonlocal`,
- unikanie nadpisywania nazw wbudowanych.

---

## Mini ściąga

```python
x = 10

def f():
    y = 5
    print(x, y)
```

```python
def outer():
    x = 1

    def inner():
        nonlocal x
        x += 1
```

---

## Ćwiczenia

1. Napisz funkcję z lokalną zmienną i sprawdź, że poza funkcją nie działa.
2. Odczytaj zmienną globalną wewnątrz funkcji.
3. Spróbuj zmodyfikować globalną zmienną bez `global` i zobacz błąd.
4. Użyj `global`, aby poprawić przykład.
5. Użyj `nonlocal` w funkcji zagnieżdżonej.
6. Zrób prosty licznik oparty o closure.

---

## Przykładowe rozwiązania

### 1. Lokalna

```python
def hello():
    imie = "Anna"
    print(imie)
```

### 2. Globalna

```python
x = 10

def show():
    print(x)
```

### 3. Błąd

```python
x = 1

def bad():
    x = x + 1
```

### 4. `global`

```python
x = 1

def good():
    global x
    x += 1
```

### 5. `nonlocal`

```python
def outer():
    x = 1

    def inner():
        nonlocal x
        x += 1
```

### 6. Closure

```python
def make_counter():
    x = 0

    def inc():
        nonlocal x
        x += 1
        return x

    return inc
```
