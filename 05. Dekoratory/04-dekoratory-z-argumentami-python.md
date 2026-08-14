# Dekoratory z argumentami w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co dekoratorowi argumenty](#po-co-dekoratorowi-argumenty)
3. [Struktura trzech poziomów](#struktura-trzech-poziomów)
4. [Najprostszy przykład](#najprostszy-przykład)
5. [Jak to czytać](#jak-to-czytać)
6. [Dekorator powtarzający funkcję](#dekorator-powtarzający-funkcję)
7. [Dekorator logujący z etykietą](#dekorator-logujący-z-etykietą)
8. [Typowe błędy początkujących](#typowe-błędy-początkujących)
9. [Praktyczne przykłady](#praktyczne-przykłady)
10. [Dobre praktyki](#dobre-praktyki)
11. [Podsumowanie](#podsumowanie)
12. [Mini ściąga](#mini-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Zwykły dekorator bierze funkcję.

Dekorator z argumentami robi krok więcej:

- najpierw bierze konfigurację,
- potem tworzy właściwy dekorator,
- a ten dopiero bierze funkcję.

Dlatego taki dekorator ma zwykle **trzy poziomy funkcji**.

---

## Po co dekoratorowi argumenty

Po to, by można było zmieniać jego zachowanie.

Na przykład:

- ile razy wywołać funkcję,
- jaki prefiks logowania ustawić,
- jaki limit lub tryb działania wybrać.

---

## Struktura trzech poziomów

Schemat:

```python
def dekorator(arg):
    def prawdziwy_dekorator(f):
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return wrapper
    return prawdziwy_dekorator
```

To najważniejszy wzorzec.

---

## Najprostszy przykład

```python
def powtorz(n):
    def dekorator(f):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                f(*args, **kwargs)
        return wrapper
    return dekorator

@powtorz(3)
def hello():
    print("Hello")
```

---

## Jak to czytać

```python
@powtorz(3)
```

czytaj jako:

1. wywołaj `powtorz(3)`,
2. dostaniesz dekorator,
3. ten dekorator zastosuj do funkcji `hello`.

---

## Dekorator powtarzający funkcję

```python
def powtorz(n):
    def dekorator(f):
        def wrapper(*args, **kwargs):
            wynik = None
            for _ in range(n):
                wynik = f(*args, **kwargs)
            return wynik
        return wrapper
    return dekorator
```

---

## Dekorator logujący z etykietą

```python
def loguj(prefix):
    def dekorator(f):
        def wrapper(*args, **kwargs):
            print(prefix, f.__name__)
            return f(*args, **kwargs)
        return wrapper
    return dekorator
```

---

## Typowe błędy początkujących

- mylenie poziomów funkcji,
- brak `return dekorator`,
- brak `return wrapper`,
- zbyt szybkie przechodzenie do trudnych wersji,
- mylenie argumentów dekoratora z argumentami dekorowanej funkcji.

---

## Praktyczne przykłady

```python
def prefiks(txt):
    def dekorator(f):
        def wrapper(*args, **kwargs):
            print(txt)
            return f(*args, **kwargs)
        return wrapper
    return dekorator
```

---

## Dobre praktyki

- najpierw zrozum zwykły dekorator,
- dopiero potem ucz się dekoratorów z argumentami,
- czytaj kod warstwa po warstwie,
- używaj `*args, **kwargs`.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- dekorator z argumentami ma zwykle trzy poziomy,
- pierwszy poziom bierze konfigurację,
- drugi bierze funkcję,
- trzeci ją opakowuje.

---

## Mini ściąga

```python
def dekorator(arg):
    def realny(f):
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return wrapper
    return realny
```

---

## Ćwiczenia

### Ćwiczenie 1

Napisz dekorator `@powtorz(2)`.

### Ćwiczenie 2

Napisz dekorator z argumentem tekstowym, który wypisze dany nagłówek.

---

## Przykładowe rozwiązania

```python
def powtorz(n):
    def dekorator(f):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                f(*args, **kwargs)
        return wrapper
    return dekorator
```
