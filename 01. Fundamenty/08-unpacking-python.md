# Unpacking w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest unpacking](#czym-jest-unpacking)
3. [Rozpakowywanie list i krotek](#rozpakowywanie-list-i-krotek)
4. [Extended unpacking](#extended-unpacking)
5. [Rozpakowywanie wielopoziomowe](#rozpakowywanie-wielopoziomowe)
6. [Rozpakowywanie w pętlach](#rozpakowywanie-w-pętlach)
7. [Rozpakowywanie przy wywołaniu funkcji](#rozpakowywanie-przy-wywołaniu-funkcji)
8. [Rozpakowywanie słowników przez `**`](#rozpakowywanie-słowników-przez-)
9. [Łączenie unpackingu z `*args` i `**kwargs`](#łączenie-unpackingu-z-args-i-kwargs)
10. [Typowe pułapki początkujących](#typowe-pułapki-początkujących)
11. [Praktyczne przykłady](#praktyczne-przykłady)
12. [Dobre praktyki](#dobre-praktyki)
13. [Podsumowanie](#podsumowanie)
14. [Mini ściąga](#mini-ściąga)
15. [Ćwiczenia](#ćwiczenia)
16. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Unpacking to bardzo pythonowy mechanizm.

Pozwala:

- rozdzielać elementy sekwencji do zmiennych,
- wygodniej przechodzić po danych,
- przekazywać listy, krotki i słowniki do funkcji,
- pisać czytelniejszy kod.

Na początku może wyglądać jak magia składni, ale w praktyce szybko staje się codziennym narzędziem.

---

## Czym jest unpacking

Najprostszy przykład:

```python
a, b = (1, 2)
```

To znaczy:

- pierwszy element trafia do `a`,
- drugi do `b`.

Python rozpakowuje sekwencję na osobne zmienne.

---

## Rozpakowywanie list i krotek

```python
imie, wiek = ["Anna", 30]
print(imie, wiek)
```

Output:

```python
Anna 30
```

```python
x, y, z = (1, 2, 3)
print(x, y, z)
```

Output:

```python
1 2 3
```

Ważne:

- liczba zmiennych po lewej stronie musi pasować do liczby elementów,
- jeśli nie pasuje, dostaniesz `ValueError`.

---

## Extended unpacking

Możesz użyć `*`, żeby zebrać część elementów do listy.

```python
first, *middle, last = [1, 2, 3, 4, 5]
print(first)
print(middle)
print(last)
```

Output:

```python
1
[2, 3, 4]
5
```

Możliwe są też inne formy:

```python
*poczatek, ostatni = [1, 2, 3]
pierwszy, *reszta = [1, 2, 3]
```

Element ze `*` zawsze dostaje listę, nawet jeśli ma zero albo jeden element.

---

## Rozpakowywanie wielopoziomowe

Możesz rozpakowywać także struktury zagnieżdżone.

```python
dane = ("Anna", (30, "Krakow"))
imie, (wiek, miasto) = dane
```

To bywa bardzo czytelne, jeśli struktura danych jest prosta i przewidywalna.

---

## Rozpakowywanie w pętlach

Bardzo częsty idiom:

```python
dane = [("Anna", 30), ("Jan", 25)]

for imie, wiek in dane:
    print(imie, wiek)
```

Output:

```python
Anna 30
Jan 25
```

Łączy się to też świetnie z `enumerate()`:

```python
for i, (imie, wiek) in enumerate(dane, start=1):
    print(i, imie, wiek)
```

Output:

```python
1 Anna 30
2 Jan 25
```

---

## Rozpakowywanie przy wywołaniu funkcji

Jeśli masz listę albo krotkę z argumentami, możesz użyć `*`.

```python
def dodaj(a, b, c):
    return a + b + c

wartosci = [1, 2, 3]
print(dodaj(*wartosci))
```

Output:

```python
6
```

To przydaje się, gdy dane są już zebrane w jednej sekwencji.

---

## Rozpakowywanie słowników przez `**`

Jeśli masz słownik z nazwanymi argumentami:

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

Tu ważne jest dopasowanie kluczy słownika do nazw parametrów funkcji.

Jeśli nazwy się nie zgadzają, dostaniesz `TypeError`.

---

## Łączenie unpackingu z `*args` i `**kwargs`

Tematy są ze sobą powiązane:

- `*args` zbiera wiele argumentów pozycyjnych do krotki,
- `**kwargs` zbiera wiele argumentów nazwanych do słownika,
- `*lista` rozpakowuje sekwencję przy wywołaniu,
- `**slownik` rozpakowuje słownik przy wywołaniu.

Przykład:

```python
def pokaz(a, b, c):
    print(a, b, c)

dane = [10, 20, 30]
pokaz(*dane)
```

To podobne mechanicznie, ale użyte w innym miejscu składni.

---

## Typowe pułapki początkujących

- zła liczba zmiennych po lewej stronie,
- mylenie unpackingu z `*args` i `**kwargs`,
- brak zrozumienia, że `*` w przypisaniu i w wywołaniu pełni inne role,
- nieczytelne nadużywanie unpackingu tam, gdzie prosty kod byłby lepszy,
- oczekiwanie, że `**slownik` zadziała z dowolnymi kluczami.

---

## Praktyczne przykłady

### Rozpakowanie danych użytkownika

```python
uzytkownik = ("Anna", 29, "Krakow")
imie, wiek, miasto = uzytkownik
```

### Wydzielenie pierwszego i ostatniego elementu

```python
liczby = [1, 2, 3, 4, 5]
pierwszy, *srodek, ostatni = liczby
```

### Rozpakowanie w pętli

```python
pary = [("a", 1), ("b", 2)]
for litera, liczba in pary:
    print(litera, liczba)
```

### Rozpakowanie argumentów do funkcji

```python
def pole(a, b):
    return a * b

wymiary = (3, 4)
print(pole(*wymiary))
```

### Rozpakowanie słownika

```python
def user_info(imie, wiek):
    print(imie, wiek)

user_info(**{"imie": "Ola", "wiek": 22})
```

---

## Dobre praktyki

- używaj unpackingu, gdy poprawia czytelność,
- nie nadużywaj go w bardzo złożonych przypisaniach,
- pamiętaj o zgodności liczby elementów,
- używaj `*` i `**` świadomie przy wywołaniach funkcji.

---

## Podsumowanie

Unpacking to wygodne narzędzie do rozdzielania i przekazywania danych.

Warto dobrze rozumieć:

- zwykłe rozpakowanie,
- extended unpacking,
- rozpakowanie wielopoziomowe,
- rozpakowanie przy wywołaniu funkcji,
- rozpakowanie słowników przez `**`.

---

## Mini ściąga

```python
a, b = (1, 2)
first, *middle, last = [1, 2, 3, 4]

for x, y in [(1, 2), (3, 4)]:
    print(x, y)

def f(a, b):
    return a + b

print(f(*[10, 20]))
```

---

## Ćwiczenia

1. Rozpakuj krotkę `("Anna", 29, "Krakow")`.
2. Użyj extended unpacking na liście `[1, 2, 3, 4, 5]`.
3. Wypisz pary danych z listy krotek przez unpacking w pętli.
4. Wywołaj funkcję przez `*lista`.
5. Wywołaj funkcję przez `**slownik`.
6. Zrób przykład rozpakowania wielopoziomowego.

---

## Przykładowe rozwiązania

### 1. Krotka

```python
imie, wiek, miasto = ("Anna", 29, "Krakow")
```

### 2. Extended unpacking

```python
first, *middle, last = [1, 2, 3, 4, 5]
```

### 3. Pętla

```python
for imie, wiek in [("Anna", 30), ("Jan", 25)]:
    print(imie, wiek)
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

### 6. Wielopoziomowe

```python
dane = ("Anna", (30, "Krakow"))
imie, (wiek, miasto) = dane
```
