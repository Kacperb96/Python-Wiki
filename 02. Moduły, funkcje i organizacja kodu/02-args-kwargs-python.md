# `*args` i `**kwargs` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co istnieją `*args` i `**kwargs`](#po-co-istnieją-args-i-kwargs)
3. [Czym jest `*args`](#czym-jest-args)
4. [Czym jest `**kwargs`](#czym-jest-kwargs)
5. [Łączenie zwykłych parametrów z `*args` i `**kwargs`](#łączenie-zwykłych-parametrów-z-args-i-kwargs)
6. [Rozpakowywanie argumentów przy wywołaniu](#rozpakowywanie-argumentów-przy-wywołaniu)
7. [Kiedy to ma sens](#kiedy-to-ma-sens)
8. [Kiedy lepiej nie używać `*args` i `**kwargs`](#kiedy-lepiej-nie-używać-args-i-kwargs)
9. [Typowe pułapki początkujących](#typowe-pułapki-początkujących)
10. [Praktyczne przykłady](#praktyczne-przykłady)
11. [Dobre praktyki](#dobre-praktyki)
12. [Podsumowanie](#podsumowanie)
13. [Mini ściąga](#mini-ściąga)
14. [Ćwiczenia](#ćwiczenia)
15. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`*args` i `**kwargs` pozwalają pisać funkcje przyjmujące zmienną liczbę argumentów.

To bardzo użyteczne, ale trzeba rozumieć:

- co dokładnie zbierają,
- kiedy poprawiają elastyczność,
- kiedy zaczynają psuć czytelność.

---

## Po co istnieją `*args` i `**kwargs`

Przydają się, gdy:

- nie znasz z góry liczby argumentów,
- chcesz przekazać argumenty dalej do innej funkcji,
- budujesz ogólniejsze API,
- potrzebujesz elastycznej warstwy pośredniej.

Nie są jednak obowiązkowe w każdej funkcji.

---

## Czym jest `*args`

`*args` zbiera dodatkowe argumenty pozycyjne do krotki.

```python
def suma(*args):
    print(args)

suma(1, 2, 3)
```

Wynik:

```python
(1, 2, 3)
```

Najczęstszy przypadek:

```python
def suma(*args):
    return sum(args)
```

---

## Czym jest `**kwargs`

`**kwargs` zbiera dodatkowe argumenty nazwane do słownika.

```python
def pokaz(**kwargs):
    print(kwargs)

pokaz(imie="Anna", wiek=30)
```

Wynik:

```python
{"imie": "Anna", "wiek": 30}
```

Możesz po tym iterować:

```python
def pokaz(**kwargs):
    for klucz, wartosc in kwargs.items():
        print(klucz, wartosc)
```

Jeśli wywołasz:

```python
pokaz(imie="Anna", wiek=30)
```

to output będzie:

```python
imie Anna
wiek 30
```

---

## Łączenie zwykłych parametrów z `*args` i `**kwargs`

```python
def funkcja(prefix, *args, **kwargs):
    print(prefix)
    print(args)
    print(kwargs)
```

Jeśli wywołasz:

```python
funkcja("ID:", 1, 2, 3, active=True)
```

to output będzie:

```python
ID:
(1, 2, 3)
{'active': True}
```

To pozwala mieć:

- zwykłe wymagane argumenty,
- dodatkowe pozycyjne,
- dodatkowe nazwane.

Kolejność ma znaczenie.

---

## Rozpakowywanie argumentów przy wywołaniu

To druga strona tego samego mechanizmu.

Lista lub krotka:

```python
def dodaj(a, b, c):
    return a + b + c

dane = [1, 2, 3]
print(dodaj(*dane))
```

Output:

```python
6
```

Słownik:

```python
def hello(imie, wiek):
    print(imie, wiek)

dane = {"imie": "Ola", "wiek": 22}
hello(**dane)
```

Output:

```python
Ola 22
```

---

## Kiedy to ma sens

`*args`:

- gdy liczba argumentów jest naprawdę zmienna,
- np. funkcja sumująca wiele liczb.

`**kwargs`:

- gdy chcesz przyjąć zestaw nazwanych ustawień,
- gdy budujesz cienką warstwę przekazującą dane dalej.

W przeciwnym razie zwykłe jawne argumenty bywają lepsze.

---

## Kiedy lepiej nie używać `*args` i `**kwargs`

Nie używaj ich tylko dlatego, że "brzmią bardziej zaawansowanie".

Jeśli wiesz, że funkcja potrzebuje:

- `name`,
- `email`,
- `active`,

to zwykle lepiej napisać:

```python
def create_user(name, email, active=True):
    ...
```

niż:

```python
def create_user(**kwargs):
    ...
```

Jawne API jest czytelniejsze i mniej zaskakujące.

---

## Typowe pułapki początkujących

- mylenie `*args` z listą, choć to krotka,
- iterowanie po `kwargs` jak po parach bez użycia `.items()`,
- nadużywanie `**kwargs` zamiast normalnych parametrów,
- brak zrozumienia, że `*` przy definicji i przy wywołaniu pełni różne role.

---

## Praktyczne przykłady

### Sumowanie wielu liczb

```python
def suma(*args):
    return sum(args)
```

### Wypisywanie profilu

```python
def pokaz_profil(**kwargs):
    for klucz, wartosc in kwargs.items():
        print(f"{klucz}: {wartosc}")
```

### Prefix dla wielu wartości

```python
def dodaj_prefix(prefix, *args):
    return [prefix + x for x in args]
```

---

## Dobre praktyki

- używaj `*args` i `**kwargs`, gdy naprawdę rozwiązują konkretny problem,
- preferuj jawne argumenty, gdy API jest znane,
- pamiętaj, że czytelność jest ważniejsza niż elastyczność dla samej elastyczności,
- jasno oddzielaj argumenty wymagane od opcjonalnych.

---

## Podsumowanie

`*args` i `**kwargs` są bardzo przydatne, ale nie powinny zastępować dobrze zaprojektowanej, czytelnej funkcji.

Najpierw pytaj:

"czy naprawdę potrzebuję zmiennej liczby argumentów?"

---

## Mini ściąga

```python
def suma(*args):
    return sum(args)

def pokaz(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

def f(a, b, *args, **kwargs):
    print(a, b, args, kwargs)
```

---

## Ćwiczenia

1. Napisz funkcję `suma(*args)`.
2. Napisz funkcję `pokaz_dane(**kwargs)`.
3. Napisz funkcję z `prefix` i `*args`.
4. Wywołaj funkcję przez `*lista`.
5. Wywołaj funkcję przez `**slownik`.

---

## Przykładowe rozwiązania

### 1. `suma`

```python
def suma(*args):
    return sum(args)
```

### 2. `pokaz_dane`

```python
def pokaz_dane(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")
```

### 3. Prefix

```python
def dodaj_prefix(prefix, *args):
    return [prefix + x for x in args]
```

### 4. `*lista`

```python
def dodaj(a, b):
    return a + b

print(dodaj(*[2, 3]))
```

### 5. `**slownik`

```python
def hello(imie, wiek):
    print(imie, wiek)

hello(**{"imie": "Ola", "wiek": 22})
```
