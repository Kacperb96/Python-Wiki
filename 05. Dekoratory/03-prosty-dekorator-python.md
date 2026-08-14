# Prosty dekorator w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Najprostsza idea dekoratora](#najprostsza-idea-dekoratora)
3. [Dekorator bez składni `@`](#dekorator-bez-składni-)
4. [Wrapper](#wrapper)
5. [Składnia `@`](#składnia-)
6. [Dekorator z `*args, **kwargs`](#dekorator-z-args-kwargs)
7. [Po co używać prostych dekoratorów](#po-co-używać-prostych-dekoratorów)
8. [Typowe błędy początkujących](#typowe-błędy-początkujących)
9. [Praktyczne przykłady](#praktyczne-przykłady)
10. [Dobre praktyki](#dobre-praktyki)
11. [Podsumowanie](#podsumowanie)
12. [Mini ściąga](#mini-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Najprostszy dekorator to najlepszy sposób, żeby zrozumieć cały temat.

Jeśli opanujesz prosty dekorator:

- z wrapperem,
- z przejęciem funkcji,
- ze zwracaniem nowej funkcji,

to reszta będzie już tylko rozwinięciem tego pomysłu.

---

## Najprostsza idea dekoratora

Dekorator:

1. dostaje funkcję,
2. tworzy nową funkcję,
3. zwraca tę nową funkcję.

---

## Dekorator bez składni `@`

```python
def dekorator(f):
    def wrapper():
        print("Przed funkcja")
        f()
        print("Po funkcji")
    return wrapper

def hello():
    print("Hello")

hello = dekorator(hello)
hello()
```

Wynik:

```python
Przed funkcja
Hello
Po funkcji
```

---

## Wrapper

`wrapper` to funkcja opakowująca oryginalną funkcję.

To właśnie ona dodaje nowe zachowanie:

- przed wywołaniem,
- po wywołaniu,
- czasem zamiast wywołania.

---

## Składnia `@`

To skrót:

```python
@dekorator
def hello():
    print("Hello")
```

jest równoważne:

```python
def hello():
    print("Hello")

hello = dekorator(hello)
```

Czyli składnia z `@` niczego magicznego nie dodaje.

To tylko krótszy i wygodniejszy zapis.

---

## Dekorator z `*args, **kwargs`

Jeśli dekorowana funkcja ma argumenty, wrapper też musi je przyjąć.

```python
def dekorator(f):
    def wrapper(*args, **kwargs):
        print("Start")
        wynik = f(*args, **kwargs)
        print("Koniec")
        return wynik
    return wrapper
```

To bardzo ważny wzorzec.

Jeśli o nim zapomnisz, dekorator będzie działał tylko dla bardzo prostych funkcji bez argumentów.

---

## Po co używać prostych dekoratorów

Na przykład do:

- logowania,
- mierzenia czasu,
- prostego debugowania,
- wypisywania komunikatów.

---

## Typowe błędy początkujących

- brak `return wrapper`,
- wywołanie `f()` za wcześnie,
- brak `*args, **kwargs`,
- brak zwracania wyniku oryginalnej funkcji.

---

## Praktyczne przykłady

```python
def loguj(f):
    def wrapper(*args, **kwargs):
        print("Wywoluje:", f.__name__)
        return f(*args, **kwargs)
    return wrapper

@loguj
def dodaj(a, b):
    return a + b
```

Przykład użycia:

```python
print(dodaj(2, 3))
```

Wynik:

```python
Wywoluje: dodaj
5
```

---

## Dobre praktyki

- zawsze pamiętaj o `*args, **kwargs`, jeśli dekorator ma być uniwersalny,
- jeśli funkcja coś zwraca, wrapper też powinien zwrócić wynik,
- zaczynaj od prostych dekoratorów zanim przejdziesz do dekoratorów z argumentami.

Praktyczna zasada:

najpierw zrozum ręcznie zapis `f = dekorator(f)`, a dopiero potem używaj `@dekorator`.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- dekorator przyjmuje funkcję,
- wrapper opakowuje jej wykonanie,
- składnia `@` to tylko skrót,
- `*args, **kwargs` są bardzo ważne w praktyce.

Najważniejsze do zapamiętania:

- dekorator nie zmienia środka funkcji, tylko podmienia ją na nową wersję,
- wrapper jest nową funkcją, która decyduje co zrobić przed, po albo zamiast oryginału,
- brak `return wynik` to jeden z najczęstszych błędów.

---

## Mini ściąga

```python
def dekorator(f):
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper
```

---

## Ćwiczenia

### Ćwiczenie 1

Napisz dekorator, który wypisuje komunikat przed i po funkcji.

### Ćwiczenie 2

Udekoruj funkcję dodającą dwie liczby.

---

## Przykładowe rozwiązania

```python
def info(f):
    def wrapper(*args, **kwargs):
        print("Start")
        wynik = f(*args, **kwargs)
        print("Stop")
        return wynik
    return wrapper
```
