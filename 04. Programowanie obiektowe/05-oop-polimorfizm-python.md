# Polimorfizm w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest polimorfizm](#czym-jest-polimorfizm)
3. [Dlaczego polimorfizm jest ważny](#dlaczego-polimorfizm-jest-ważny)
4. [Najprostsza intuicja](#najprostsza-intuicja)
5. [Polimorfizm a wspólny interfejs](#polimorfizm-a-wspólny-interfejs)
6. [Polimorfizm przez dziedziczenie](#polimorfizm-przez-dziedziczenie)
7. [Polimorfizm przez duck typing](#polimorfizm-przez-duck-typing)
8. [Nadpisywanie metod a polimorfizm](#nadpisywanie-metod-a-polimorfizm)
9. [Polimorfizm w funkcjach](#polimorfizm-w-funkcjach)
10. [Polimorfizm w metodach](#polimorfizm-w-metodach)
11. [Polimorfizm a `len`, `+`, `str` i inne](#polimorfizm-a-len--str-i-inne)
12. [Abstrakcyjny przykład interfejsu](#abstrakcyjny-przykład-interfejsu)
13. [Kiedy polimorfizm daje największą korzyść](#kiedy-polimorfizm-daje-największą-korzyść)
14. [Typowe błędy początkujących](#typowe-błędy-początkujących)
15. [Praktyczne przykłady](#praktyczne-przykłady)
16. [Dobre praktyki](#dobre-praktyki)
17. [Podsumowanie](#podsumowanie)
18. [Mini ściąga](#mini-ściąga)
19. [Ćwiczenia](#ćwiczenia)
20. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Polimorfizm to jedno z najważniejszych pojęć w OOP.

Brzmi groźnie, ale idea jest prosta:

**różne obiekty mogą być używane w podobny sposób, jeśli wspierają to samo zachowanie.**

To sprawia, że kod staje się:

- bardziej elastyczny,
- mniej zależny od konkretnej klasy,
- łatwiejszy do rozbudowy.

---

## Czym jest polimorfizm

Najprościej:

polimorfizm oznacza, że ten sam kod może działać na różnych obiektach.

Przykład:

```python
def wydaj_dzwiek(zwierze):
    zwierze.dzwiek()
```

Ta funkcja może działać dla:

- psa,
- kota,
- ptaka,

jeśli każdy z nich ma metodę `dzwiek`.

---

## Dlaczego polimorfizm jest ważny

Bo nie musisz pisać osobnej funkcji dla każdej klasy.

Zamiast:

- `wydaj_dzwiek_psa`
- `wydaj_dzwiek_kota`
- `wydaj_dzwiek_ptaka`

możesz mieć jedną funkcję.

---

## Najprostsza intuicja

Jeśli kilka obiektów umie:

```python
drukuj()
```

to kod nie musi wiedzieć, czy to:

- dokument PDF,
- raport,
- faktura,
- etykieta.

Ważne jest to, że każdy umie być wydrukowany.

---

## Polimorfizm a wspólny interfejs

Wspólny interfejs oznacza, że różne obiekty udostępniają te same metody lub zachowania.

Na przykład:

- `Pies.dzwiek()`
- `Kot.dzwiek()`
- `Krowa.dzwiek()`

To daje wspólny sposób użycia:

```python
obiekt.dzwiek()
```

---

## Polimorfizm przez dziedziczenie

Przykład:

```python
class Zwierze:
    def dzwiek(self):
        raise NotImplementedError

class Pies(Zwierze):
    def dzwiek(self):
        print("Hau")

class Kot(Zwierze):
    def dzwiek(self):
        print("Miau")
```

Teraz:

```python
for zwierze in [Pies(), Kot()]:
    zwierze.dzwiek()
```

to klasyczny przykład polimorfizmu.

Wynik:

```python
Hau
Miau
```

---

## Polimorfizm przez duck typing

W Pythonie polimorfizm nie musi opierać się tylko na dziedziczeniu.

Przykład:

```python
class Pies:
    def dzwiek(self):
        print("Hau")

class Alarm:
    def dzwiek(self):
        print("Beeeep")
```

Jeśli funkcja oczekuje tylko metody `dzwiek`, to oba obiekty mogą działać.

To bardzo pythonowe podejście.

Przykład:

```python
for obiekt in [Pies(), Alarm()]:
    obiekt.dzwiek()
```

Wynik:

```python
Hau
Beeeep
```

---

## Nadpisywanie metod a polimorfizm

Polimorfizm bardzo często działa dzięki nadpisywaniu metod.

Każda klasa implementuje własną wersję tego samego zachowania.

Na przykład:

```python
class Figura:
    def pole(self):
        raise NotImplementedError
```

Potem:

- `Kwadrat.pole()`
- `Kolo.pole()`

działają inaczej, ale interfejs jest wspólny.

---

## Polimorfizm w funkcjach

To jeden z najważniejszych praktycznych wzorców.

```python
def pokaz_pole(figura):
    print(figura.pole())
```

Ta funkcja nie musi wiedzieć, czy dostała:

- kwadrat,
- prostokąt,
- koło.

Ważne, że obiekt ma metodę `pole`.

To jest sedno praktycznego polimorfizmu:

funkcja oczekuje zachowania, a nie konkretnej klasy.

---

## Polimorfizm w metodach

To samo może dotyczyć metod wewnątrz klas.

Jedna klasa może przyjmować różne obiekty i używać ich w ten sam sposób.

---

## Polimorfizm a `len`, `+`, `str` i inne

Python jest pełen polimorfizmu.

Przykład:

```python
len([1, 2, 3])
len("Python")
len({"a": 1, "b": 2})
```

Ta sama funkcja `len()` działa na różnych typach.

To też jest forma polimorfizmu.

Podobnie:

- `str(obiekt)`
- `+`
- `in`

działają na różnych obiektach zgodnie z ich implementacją.

Wynik:

```python
3
6
2
```

---

## Abstrakcyjny przykład interfejsu

Można myśleć tak:

mamy kilka obiektów, które wszystkie potrafią:

```python
uruchom()
```

To, jak dokładnie to zrobią, zależy od klasy.

Ale kod używający tych obiektów nie musi znać szczegółów.

To sedno polimorfizmu.

---

## Kiedy polimorfizm daje największą korzyść

Najbardziej przydaje się, gdy:

- masz wiele podobnych klas,
- chcesz traktować je wspólnie,
- nie chcesz pisać wielu `if type(...)`,
- chcesz mieć kod otwarty na rozbudowę.

---

## Typowe błędy początkujących

### 1. Pisanie wielu `if` zamiast wspólnego interfejsu

### 2. Mylenie polimorfizmu tylko z dziedziczeniem

W Pythonie duck typing też jest bardzo ważny.

### 3. Brak spójnych nazw metod w klasach, które mają współpracować

### 4. Zbyt ścisłe sprawdzanie typów zamiast oczekiwania zachowania

---

## Praktyczne przykłady

### Zwierzęta

```python
class Pies:
    def dzwiek(self):
        print("Hau")

class Kot:
    def dzwiek(self):
        print("Miau")

def wydaj_dzwiek(obiekt):
    obiekt.dzwiek()
```

Przykład użycia:

```python
wydaj_dzwiek(Pies())
wydaj_dzwiek(Kot())
```

Wynik:

```python
Hau
Miau
```

### Figury

```python
class Kwadrat:
    def __init__(self, bok):
        self.bok = bok

    def pole(self):
        return self.bok ** 2

class Prostokat:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def pole(self):
        return self.a * self.b
```

Przykład użycia:

```python
print(Kwadrat(4).pole())
print(Prostokat(2, 5).pole())
```

Wynik:

```python
16
10
```

### Wspólna funkcja

```python
def pokaz_pole(figura):
    print(figura.pole())
```

To lepsze niż pisanie czegoś takiego:

```python
def pokaz_pole(figura):
    if isinstance(figura, Kwadrat):
        print(figura.bok ** 2)
    elif isinstance(figura, Prostokat):
        print(figura.a * figura.b)
```

Taki kod jest mniej elastyczny i gorzej się skaluje.

---

## Dobre praktyki

### Projektuj klasy tak, by miały spójne zachowanie

### Myśl o tym, czego kod potrzebuje od obiektu

Nie zawsze musi znać jego dokładny typ.

### Unikaj rozgałęzień typu:

```python
if isinstance(...)
```

jeśli polimorfizm może rozwiązać problem czyściej.

### Praktyczna zasada

Jeśli kilka klas ma być używanych tak samo, zadbaj o wspólną nazwę metody i spójne zachowanie.

Wtedy reszta kodu będzie prostsza, krótsza i łatwiejsza do rozbudowy.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- polimorfizm pozwala używać różnych obiektów przez wspólne zachowanie,
- może działać przez dziedziczenie albo duck typing,
- bardzo pomaga upraszczać kod,
- w Pythonie polimorfizm jest naturalny i bardzo powszechny.

Najważniejsze do zapamiętania:

- kod powinien często pytać "czy obiekt umie to zrobić?", a nie "czy jest tego typu?",
- wspólny interfejs może wynikać z dziedziczenia albo po prostu z tych samych metod,
- polimorfizm bardzo ogranicza potrzebę pisania wielu `if isinstance(...)`.

---

## Mini ściąga

```python
def zrob_cos(obiekt):
    obiekt.metoda()
```

Jeśli różne klasy mają `metoda()`, to funkcja działa polimorficznie.

---

## Ćwiczenia

### Ćwiczenie 1

Utwórz klasy `Pies` i `Kot`, obie z metodą `dzwiek`.

### Ćwiczenie 2

Napisz funkcję, która przyjmuje obiekt i wywołuje `dzwiek()`.

### Ćwiczenie 3

Utwórz klasy figur z metodą `pole` i jedną funkcję do wypisywania pola.

---

## Przykładowe rozwiązania

### Ćwiczenie 1

```python
class Pies:
    def dzwiek(self):
        print("Hau")

class Kot:
    def dzwiek(self):
        print("Miau")
```

### Ćwiczenie 2

```python
def wydaj_dzwiek(obiekt):
    obiekt.dzwiek()
```

### Ćwiczenie 3

```python
class Kwadrat:
    def __init__(self, bok):
        self.bok = bok

    def pole(self):
        return self.bok ** 2

class Kolo:
    def __init__(self, r):
        self.r = r

    def pole(self):
        return 3.14 * self.r * self.r
```
