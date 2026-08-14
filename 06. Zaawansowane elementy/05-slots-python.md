# `__slots__` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `__slots__`](#czym-jest-__slots__)
3. [Po co istnieje `__slots__`](#po-co-istnieje-__slots__)
4. [Jak działa zwykły obiekt bez `__slots__`](#jak-działa-zwykły-obiekt-bez-__slots__)
5. [Jak działa obiekt z `__slots__`](#jak-działa-obiekt-z-__slots__)
6. [Oszczędność pamięci](#oszczędność-pamięci)
7. [Ograniczenie dozwolonych atrybutów](#ograniczenie-dozwolonych-atrybutów)
8. [Przykład podstawowy](#przykład-podstawowy)
9. [Kiedy `__slots__` ma sens](#kiedy-__slots__-ma-sens)
10. [Kiedy `__slots__` nie ma sensu](#kiedy-__slots__-nie-ma-sensu)
11. [Dziedziczenie a `__slots__`](#dziedziczenie-a-__slots__)
12. [`__slots__` a `__dict__`](#__slots__-a-__dict__)
13. [`__slots__` a `weakref`](#__slots__-a-weakref)
14. [Typowe błędy początkujących](#typowe-błędy-początkujących)
15. [Praktyczne przykłady](#praktyczne-przykłady)
16. [Dobre praktyki](#dobre-praktyki)
17. [Podsumowanie](#podsumowanie)
18. [Mini ściąga](#mini-ściąga)
19. [Ćwiczenia](#ćwiczenia)
20. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`__slots__` to bardziej zaawansowany mechanizm optymalizacji klas w Pythonie.

Najczęściej mówi się o nim w dwóch kontekstach:

- oszczędność pamięci,
- ograniczenie dynamicznego dodawania atrybutów.

To nie jest temat obowiązkowy na samym starcie, ale warto go znać.

---

## Czym jest `__slots__`

To specjalny atrybut klasy, który mówi Pythonowi:

"te obiekty mają mieć tylko te konkretne pola"

Przykład:

```python
class Punkt:
    __slots__ = ("x", "y")
```

---

## Po co istnieje `__slots__`

Bo zwykłe obiekty instancji mają zwykle własny `__dict__`, a to kosztuje pamięć.

Jeśli tworzysz bardzo dużo obiektów, `__slots__` może:

- zmniejszyć zużycie pamięci,
- lekko uprościć model atrybutów,
- zablokować przypadkowe dodawanie nowych pól.

---

## Jak działa zwykły obiekt bez `__slots__`

Najczęściej jego atrybuty trafiają do:

```python
obiekt.__dict__
```

czyli słownika instancji.

To bardzo elastyczne, ale ma koszt.

---

## Jak działa obiekt z `__slots__`

Przy `__slots__` Python nie tworzy zwykłego `__dict__` instancji w standardowy sposób.

Zamiast tego używa bardziej zwartego mechanizmu przechowywania atrybutów.

---

## Oszczędność pamięci

To główny praktyczny powód używania `__slots__`.

Jeśli masz:

- tysiące,
- setki tysięcy,
- miliony

prostych obiektów, oszczędność pamięci może być zauważalna.

W małych programach zwykle nie ma to dużego znaczenia.

---

## Ograniczenie dozwolonych atrybutów

Jeśli klasa ma:

```python
__slots__ = ("x", "y")
```

to nie możesz potem zrobić:

```python
p.z = 10
```

bo `z` nie jest dozwolone.

To daje prostą ochronę przed literówkami i przypadkowymi polami.

---

## Przykład podstawowy

```python
class Punkt:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y
```

To oznacza, że instancja ma mieć tylko `x` i `y`.

---

## Kiedy `__slots__` ma sens

Gdy:

- tworzysz bardzo dużo lekkich obiektów,
- struktura pól jest stała,
- zależy Ci na pamięci,
- nie potrzebujesz pełnej elastyczności `__dict__`.

---

## Kiedy `__slots__` nie ma sensu

Gdy:

- obiekt ma mieć dynamicznie dodawane pola,
- liczba obiektów jest mała,
- optymalizacja pamięci nic realnie nie daje,
- prostota kodu jest ważniejsza.

---

## Dziedziczenie a `__slots__`

To ważny temat.

Przy dziedziczeniu `__slots__` trzeba traktować ostrożnie, bo układ atrybutów robi się bardziej złożony.

Na poziomie podstawowym ważne jest, że:

`__slots__` w hierarchii klas wymaga świadomego projektowania.

---

## `__slots__` a `__dict__`

Domyślnie klasa ze `__slots__` może nie mieć standardowego `__dict__` instancji.

To oznacza m.in.:

- mniej elastyczne dynamiczne atrybuty,
- inną introspekcję,
- potencjalne problemy, jeśli kod zakłada obecność `__dict__`.

---

## `__slots__` a `weakref`

Jeśli potrzebujesz weak references, czasem trzeba jawnie dodać:

```python
"__weakref__"
```

do `__slots__`.

To już detal bardziej zaawansowany, ale warto wiedzieć, że takie rzeczy istnieją.

---

## Typowe błędy początkujących

- używanie `__slots__` bez realnej potrzeby,
- niezrozumienie, czemu nie da się dodać nowego pola,
- problemy przy dziedziczeniu,
- traktowanie `__slots__` jako magicznego przyspieszenia wszystkiego.

---

## Praktyczne przykłady

```python
class Punkt:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y
```

```python
p = Punkt(1, 2)
print(p.x)
```

To nie zadziała:

```python
p.z = 3
```

---

## Dobre praktyki

- używaj `__slots__` świadomie, nie z przyzwyczajenia,
- rozważ je tam, gdzie jest dużo małych obiektów,
- pamiętaj, że to optymalizacja i ograniczenie jednocześnie,
- nie komplikuj prostych projektów bez realnej korzyści.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- `__slots__` ogranicza zestaw atrybutów instancji,
- może zmniejszyć zużycie pamięci,
- jest sensowne głównie w określonych scenariuszach,
- nie zawsze warto go używać.

---

## Mini ściąga

```python
class A:
    __slots__ = ("x", "y")
```

---

## Ćwiczenia

### Ćwiczenie 1

Utwórz klasę `Punkt` ze `__slots__`.

### Ćwiczenie 2

Spróbuj dodać nowy atrybut spoza listy slotów.

---

## Przykładowe rozwiązania

```python
class Punkt:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y
```
