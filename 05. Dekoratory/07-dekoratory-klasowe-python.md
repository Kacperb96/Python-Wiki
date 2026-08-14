# Dekoratory klasowe w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest dekorator klasowy](#czym-jest-dekorator-klasowy)
3. [Funkcyjny dekorator klasy](#funkcyjny-dekorator-klasy)
4. [Klasa jako dekorator funkcji](#klasa-jako-dekorator-funkcji)
5. [`__call__` w dekoratorze klasowym](#__call__-w-dekoratorze-klasowym)
6. [Po co używać dekoratorów klasowych](#po-co-używać-dekoratorów-klasowych)
7. [Stan w dekoratorze klasowym](#stan-w-dekoratorze-klasowym)
8. [Typowe błędy początkujących](#typowe-błędy-początkujących)
9. [Praktyczne przykłady](#praktyczne-przykłady)
10. [Dobre praktyki](#dobre-praktyki)
11. [Podsumowanie](#podsumowanie)
12. [Mini ściąga](#mini-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Dekorator nie musi być tylko funkcją.

Może być też obiektem klasy.

Jeśli klasa implementuje:

```python
__call__
```

to jej instancja może zachowywać się jak funkcja.

To właśnie otwiera drogę do dekoratorów klasowych.

---

## Czym jest dekorator klasowy

Najczęściej mówi się tak o dwóch rzeczach:

1. klasie użytej jako dekorator funkcji,
2. dekoratorze, który modyfikuje klasę.

W praktyce w nauce dekoratorów najczęściej chodzi o pierwszy przypadek: klasa jako dekorator funkcji.

---

## Funkcyjny dekorator klasy

Można też dekorować samą klasę funkcją:

```python
def dekoruj_klase(cls):
    cls.opis = "Dodano dekoratorem"
    return cls

@dekoruj_klase
class A:
    pass
```

To też jest dekorator klasowy, ale innego rodzaju niż klasa z `__call__`.

---

## Klasa jako dekorator funkcji

Przykład:

```python
class Dekorator:
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        print("Przed")
        wynik = self.f(*args, **kwargs)
        print("Po")
        return wynik
```

Użycie:

```python
@Dekorator
def hello():
    print("Hello")
```

---

## `__call__` w dekoratorze klasowym

To właśnie `__call__` sprawia, że instancja klasy może być wywoływana jak funkcja.

Python zrobi coś w rodzaju:

```python
hello = Dekorator(hello)
```

a potem:

```python
hello()
```

wywoła `__call__`.

---

## Po co używać dekoratorów klasowych

Gdy:

- dekorator ma przechowywać stan,
- logika jest bardziej rozbudowana,
- chcesz mieć bardziej obiektowy model dekoracji.

---

## Stan w dekoratorze klasowym

To jego duża zaleta.

Można np. liczyć wywołania:

```python
class LiczWywolania:
    def __init__(self, f):
        self.f = f
        self.licznik = 0

    def __call__(self, *args, **kwargs):
        self.licznik += 1
        print("Wywolanie:", self.licznik)
        return self.f(*args, **kwargs)
```

---

## Typowe błędy początkujących

- mylenie dekorowania klasy i dekorowania funkcji klasą,
- brak `__call__`,
- brak przechowywania dekorowanej funkcji,
- zbyt szybkie przechodzenie do dekoratorów klasowych bez zrozumienia zwykłych.

---

## Praktyczne przykłady

```python
class Loguj:
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        print("Wywoluje", self.f.__name__)
        return self.f(*args, **kwargs)
```

```python
@Loguj
def dodaj(a, b):
    return a + b
```

---

## Dobre praktyki

- najpierw dobrze zrozum dekoratory funkcyjne,
- używaj dekoratora klasowego wtedy, gdy naprawdę potrzebujesz stanu,
- pilnuj czytelności.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- dekorator może być klasą,
- wtedy zwykle korzysta z `__call__`,
- dekoratory klasowe przydają się, gdy chcesz przechowywać stan lub bardziej rozbudowaną logikę.

---

## Mini ściąga

```python
class Dekorator:
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        return self.f(*args, **kwargs)
```

---

## Ćwiczenia

### Ćwiczenie 1

Napisz klasę-dekorator, która wypisuje komunikat przed wywołaniem funkcji.

### Ćwiczenie 2

Rozszerz ją o licznik wywołań.

---

## Przykładowe rozwiązania

```python
class Info:
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        print("Start")
        return self.f(*args, **kwargs)
```
