# Funkcje jako obiekty w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym to właściwie znaczy](#czym-to-właściwie-znaczy)
3. [Dlaczego to ważne](#dlaczego-to-ważne)
4. [Przypisanie funkcji do zmiennej](#przypisanie-funkcji-do-zmiennej)
5. [Przekazywanie funkcji jako argumentu](#przekazywanie-funkcji-jako-argumentu)
6. [Zwracanie funkcji z funkcji](#zwracanie-funkcji-z-funkcji)
7. [Funkcja jako element listy lub słownika](#funkcja-jako-element-listy-lub-słownika)
8. [Funkcja jako callback](#funkcja-jako-callback)
9. [Związek z dekoratorami](#związek-z-dekoratorami)
10. [Typowe błędy początkujących](#typowe-błędy-początkujących)
11. [Praktyczne przykłady](#praktyczne-przykłady)
12. [Dobre praktyki](#dobre-praktyki)
13. [Podsumowanie](#podsumowanie)
14. [Mini ściąga](#mini-ściąga)
15. [Ćwiczenia](#ćwiczenia)
16. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Jedna z najważniejszych cech Pythona brzmi:

**funkcje są obiektami.**

To bardzo ważne, bo właśnie na tym opiera się:

- przekazywanie funkcji,
- callbacki,
- closures,
- dekoratory,
- część stylu funkcyjnego w Pythonie.

---

## Czym to właściwie znaczy

To znaczy, że funkcję można traktować jak wartość.

Można ją:

- zapisać do zmiennej,
- przekazać gdzieś dalej,
- zwrócić z innej funkcji,
- umieścić w kolekcji.

---

## Dlaczego to ważne

Bo dzięki temu możesz pisać dużo bardziej elastyczny kod.

Zamiast twardo zakodować:

- co dokładnie ma się wykonać,

możesz przekazać funkcję jako zachowanie.

---

## Przypisanie funkcji do zmiennej

```python
def przywitaj():
    print("Czesc")

f = przywitaj
f()
```

Tutaj `f` wskazuje na tę samą funkcję.

Wynik:

```python
Czesc
```

### Uwaga

To nie jest:

```python
f = przywitaj()
```

bo to już wywołuje funkcję.

---

## Przekazywanie funkcji jako argumentu

```python
def wykonaj(f):
    f()

def hello():
    print("Hello")

wykonaj(hello)
```

To bardzo ważny mechanizm.

Wynik:

```python
Hello
```

---

## Zwracanie funkcji z funkcji

```python
def wybierz(przyjaznie):
    def mily():
        print("Czesc!")

    def oficjalny():
        print("Dzien dobry")

    return mily if przyjaznie else oficjalny
```

Tu funkcja zwraca inną funkcję.

Przykład użycia:

```python
f1 = wybierz(True)
f2 = wybierz(False)

f1()
f2()
```

Wynik:

```python
Czesc!
Dzien dobry
```

---

## Funkcja jako element listy lub słownika

```python
def a():
    print("A")

def b():
    print("B")

funkcje = [a, b]
funkcje[0]()
```

Albo:

```python
akcje = {"start": a, "stop": b}
akcje["start"]()
```

Wynik:

```python
A
A
```

---

## Funkcja jako callback

Callback to funkcja przekazana po to, by coś wywołało ją później.

To bardzo częsty wzorzec.

Przykład:

```python
def zakoncz():
    print("Koniec zadania")

def zrob_cos(callback):
    print("Robie cos")
    callback()

zrob_cos(zakoncz)
```

Wynik:

```python
Robie cos
Koniec zadania
```

---

## Związek z dekoratorami

Dekoratory działają właśnie dlatego, że:

- funkcję można przekazać do dekoratora,
- dekorator może zwrócić nową funkcję.

Bez traktowania funkcji jak obiektów dekoratory by nie działały.

---

## Typowe błędy początkujących

- mylenie `f` i `f()`,
- przypadkowe wywoływanie funkcji przy przekazywaniu,
- brak zrozumienia, że funkcja może być wartością jak każda inna.

---

## Praktyczne przykłady

```python
def dodaj(a, b):
    return a + b

operacja = dodaj
print(operacja(2, 3))
```

Wynik:

```python
5
```

```python
def wykonaj_dwa_razy(f):
    f()
    f()
```

Przykład użycia:

```python
def hej():
    print("Hej")

wykonaj_dwa_razy(hej)
```

Wynik:

```python
Hej
Hej
```

---

## Dobre praktyki

- rozróżniaj funkcję od wyniku jej wywołania,
- nadawaj callbackom czytelne nazwy,
- pamiętaj, że to bardzo potężny mechanizm, ale nie trzeba go nadużywać.

Praktyczna zasada:

jeśli chcesz przekazać funkcję dalej, zwykle podajesz jej nazwę bez nawiasów.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- funkcje w Pythonie są obiektami,
- można je przypisywać, przekazywać i zwracać,
- to fundament dekoratorów i callbacków.

Najważniejsze do zapamiętania:

- `f` to funkcja jako wartość,
- `f()` to wynik jej wywołania,
- bez tego rozróżnienia dekoratory i callbacki będą wyglądały nielogicznie.

---

## Mini ściąga

```python
f = moja_funkcja
wykonaj(moja_funkcja)
return inna_funkcja
```

---

## Ćwiczenia

### Ćwiczenie 1

Przypisz funkcję do zmiennej i wywołaj ją przez nową nazwę.

### Ćwiczenie 2

Napisz funkcję przyjmującą inną funkcję jako argument.

### Ćwiczenie 3

Zrób słownik komend mapujący tekst na funkcje.

---

## Przykładowe rozwiązania

```python
def hello():
    print("Hello")

f = hello
f()
```

```python
def wykonaj(f):
    f()
```
