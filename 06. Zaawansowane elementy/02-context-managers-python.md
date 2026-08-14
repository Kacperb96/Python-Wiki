# Context managers w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest context manager](#czym-jest-context-manager)
3. [Po co istnieje `with`](#po-co-istnieje-with)
4. [Jak działa `with`](#jak-działa-with)
5. [`__enter__` i `__exit__`](#__enter__-i-__exit__)
6. [Najprostszy przykład klasycznego context managera](#najprostszy-przykład-klasycznego-context-managera)
7. [Obsługa wyjątków w `__exit__`](#obsługa-wyjątków-w-__exit__)
8. [`contextlib.contextmanager`](#contextlibcontextmanager)
9. [`contextlib.suppress`](#contextlibsuppress)
10. [Najczęstsze zastosowania](#najczęstsze-zastosowania)
11. [Context manager a pliki](#context-manager-a-pliki)
12. [Context manager a zasoby](#context-manager-a-zasoby)
13. [Typowe błędy początkujących](#typowe-błędy-początkujących)
14. [Praktyczne przykłady](#praktyczne-przykłady)
15. [Dobre praktyki](#dobre-praktyki)
16. [Podsumowanie](#podsumowanie)
17. [Mini ściąga](#mini-ściąga)
18. [Ćwiczenia](#ćwiczenia)
19. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Context managers to bardzo ważny mechanizm Pythona.

Najczęściej spotykasz go w postaci:

```python
with ...
```

To właśnie dzięki niemu Python potrafi bezpiecznie zarządzać zasobami, na przykład:

- plikami,
- połączeniami,
- blokadami,
- tymczasowymi ustawieniami.

---

## Czym jest context manager

To obiekt, który definiuje:

- co ma się stać na wejściu do bloku `with`,
- co ma się stać na wyjściu z bloku `with`.

To oznacza:

- przygotowanie zasobu,
- posprzątanie po pracy,
- nawet wtedy, gdy wydarzy się wyjątek.

---

## Po co istnieje `with`

Po to, by unikać ręcznego pisania:

- otwierania,
- zamykania,
- sprzątania,
- `try/finally` w kółko.

`with` daje czytelny, bezpieczny wzorzec.

---

## Jak działa `with`

Przykład:

```python
with open("plik.txt") as f:
    dane = f.read()
```

Pod spodem Python mniej więcej:

1. wywołuje `__enter__()`,
2. wykonuje blok,
3. wywołuje `__exit__()`.

---

## `__enter__` i `__exit__`

To serce klasycznego context managera.

### `__enter__`

uruchamia się na wejściu do `with`.

### `__exit__`

uruchamia się na wyjściu z `with`, nawet przy błędzie.

---

## Najprostszy przykład klasycznego context managera

```python
class MojContext:
    def __enter__(self):
        print("Wejscie")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Wyjscie")
```

Użycie:

```python
with MojContext():
    print("W srodku")
```

Wynik:

```python
Wejscie
W srodku
Wyjscie
```

---

## Obsługa wyjątków w `__exit__`

`__exit__` dostaje informacje o wyjątku:

- typ,
- wartość,
- traceback.

Może też zdecydować, czy wyjątek ma zostać stłumiony.

Jeśli `__exit__` zwróci `True`, wyjątek może zostać uznany za obsłużony.

To temat ważny, ale trzeba z tym uważać.

---

## `contextlib.contextmanager`

To bardzo wygodny sposób tworzenia context managera z funkcji i `yield`.

Przykład:

```python
from contextlib import contextmanager

@contextmanager
def moj_context():
    print("Wejscie")
    yield
    print("Wyjscie")
```

To często dużo prostsze niż pisanie całej klasy.

Przykład użycia:

```python
with moj_context():
    print("W bloku")
```

Wynik:

```python
Wejscie
W bloku
Wyjscie
```

---

## `contextlib.suppress`

To gotowy context manager, który tłumi wybrane wyjątki.

Przykład:

```python
from contextlib import suppress

with suppress(FileNotFoundError):
    open("brak.txt").read()
```

Trzeba używać go rozsądnie.

To znaczy:

jeśli wyjątek `FileNotFoundError` wystąpi, program nie przerwie działania w tym miejscu.

---

## Najczęstsze zastosowania

- pliki,
- blokady,
- połączenia,
- transakcje,
- tymczasowe ustawienia,
- tłumienie konkretnych wyjątków.

---

## Context manager a pliki

To klasyczny przykład:

```python
with open("dane.txt", "r") as f:
    tekst = f.read()
```

Po wyjściu z bloku plik zostaje poprawnie zamknięty.

---

## Context manager a zasoby

Wszędzie tam, gdzie coś trzeba:

- otworzyć,
- użyć,
- zamknąć albo posprzątać,

`with` jest bardzo dobrym kandydatem.

---

## Typowe błędy początkujących

- brak zrozumienia, że `with` dba o sprzątanie,
- ignorowanie różnicy między klasowym context managerem i `contextmanager`,
- nadużywanie `suppress`,
- stłumianie ważnych wyjątków bez potrzeby.

### 5. Myślenie, że `with` działa tylko dla plików

To dużo szerszy mechanizm do zarządzania zasobami i stanem.

---

## Praktyczne przykłady

### Klasa

```python
class Timer:
    def __enter__(self):
        print("Start")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Stop")
```

Przykład użycia:

```python
with Timer():
    print("Robie cos")
```

Wynik:

```python
Start
Robie cos
Stop
```

### Funkcyjny context manager

```python
from contextlib import contextmanager

@contextmanager
def log():
    print("Start")
    yield
    print("Stop")
```

Przykład użycia:

```python
with log():
    print("Praca")
```

Wynik:

```python
Start
Praca
Stop
```

### suppress

```python
from contextlib import suppress

with suppress(ZeroDivisionError):
    print(1 / 0)
```

Wynik:

```python
```

Nic nie zostanie wypisane, a wyjątek zostanie stłumiony.

---

## Dobre praktyki

- używaj `with`, gdy pracujesz z zasobami,
- jeśli prosty przypadek da się zrobić przez `contextmanager`, często warto,
- nie nadużywaj tłumienia wyjątków,
- czytaj `with` jako bezpieczny wzorzec „wejście-praca-wyjście”.

Praktyczna zasada:

myśl o `with` jak o bardzo czytelnym wzorcu:

przygotuj -> użyj -> posprzątaj.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- context manager kontroluje wejście i wyjście z bloku `with`,
- kluczowe są `__enter__` i `__exit__`,
- `contextlib.contextmanager` upraszcza tworzenie własnych context managerów,
- `contextlib.suppress` tłumi wybrane wyjątki,
- to podstawowy mechanizm bezpiecznej pracy z zasobami.

Najważniejsze do zapamiętania:

- `with` to nie ozdobnik składni, tylko mechanizm bezpiecznego zarządzania zasobem,
- sprzątanie dzieje się także przy błędach,
- context manager może zarządzać nie tylko plikiem, ale też czasem, stanem, blokadą albo wyjątkami.

---

## Mini ściąga

```python
with open("plik.txt") as f:
    ...
```

```python
def __enter__(self): ...
def __exit__(self, exc_type, exc_value, traceback): ...
```

```python
@contextmanager
def ctx():
    yield
```

---

## Ćwiczenia

### Ćwiczenie 1

Napisz prosty context manager jako klasę.

### Ćwiczenie 2

Napisz prosty context manager przez `@contextmanager`.

### Ćwiczenie 3

Użyj `suppress` dla wybranego wyjątku.

---

## Przykładowe rozwiązania

```python
class Ctx:
    def __enter__(self):
        print("in")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("out")
```
