# Metaklasy w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Dlaczego metaklasy są zaawansowane](#dlaczego-metaklasy-są-zaawansowane)
3. [Najpierw ważna intuicja](#najpierw-ważna-intuicja)
4. [Klasa też jest obiektem](#klasa-też-jest-obiektem)
5. [Czym jest metaklasa](#czym-jest-metaklasa)
6. [Domyślna metaklasa `type`](#domyślna-metaklasa-type)
7. [`type` jako metaklasa](#type-jako-metaklasa)
8. [`type` do dynamicznego tworzenia klas](#type-do-dynamicznego-tworzenia-klas)
9. [Po co w ogóle używać metaklas](#po-co-w-ogóle-używać-metaklas)
10. [Najprostsza własna metaklasa](#najprostsza-własna-metaklasa)
11. [`__new__` w metaklasie](#__new__-w-metaklasie)
12. [`__init__` w metaklasie](#__init__-w-metaklasie)
13. [`__call__` w metaklasie](#__call__-w-metaklasie)
14. [Kontrolowanie tworzenia klas](#kontrolowanie-tworzenia-klas)
15. [Walidowanie klas przez metaklasę](#walidowanie-klas-przez-metaklasę)
16. [Metaklasy a dekoratory klas](#metaklasy-a-dekoratory-klas)
17. [Kiedy metaklasa ma sens](#kiedy-metaklasa-ma-sens)
18. [Kiedy metaklasa to zły pomysł](#kiedy-metaklasa-to-zły-pomysł)
19. [Typowe błędy początkujących](#typowe-błędy-początkujących)
20. [Praktyczne przykłady](#praktyczne-przykłady)
21. [Dobre praktyki](#dobre-praktyki)
22. [Podsumowanie](#podsumowanie)
23. [Mini ściąga](#mini-ściąga)
24. [Ćwiczenia](#ćwiczenia)
25. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Metaklasy to jeden z najbardziej zaawansowanych tematów w Pythonie.

To nie jest pierwszy temat, który trzeba umieć w OOP.

Najpierw warto dobrze znać:

- klasy,
- obiekty,
- dziedziczenie,
- magic methods.

Dopiero potem metaklasy zaczynają mieć sens.

Ten poradnik ma wyjaśnić temat możliwie prosto i intuicyjnie.

---

## Dlaczego metaklasy są zaawansowane

Bo działają poziom wyżej niż zwykłe klasy.

Zwykła klasa tworzy obiekty.

Metaklasa tworzy klasy.

To już abstrakcja nad abstrakcją.

---

## Najpierw ważna intuicja

W Pythonie:

- obiekt jest instancją klasy,
- klasa sama też jest obiektem,
- klasa jest instancją metaklasy.

To klucz do zrozumienia całego tematu.

---

## Klasa też jest obiektem

Przykład:

```python
class Pies:
    pass

print(type(Pies))
```

Wynik:

```python
<class 'type'>
```

To znaczy, że sama klasa `Pies` jest obiektem typu `type`.

---

## Czym jest metaklasa

Metaklasa to klasa, która tworzy klasy.

Najprościej:

- zwykła klasa tworzy obiekty,
- metaklasa tworzy klasy.

---

## Domyślna metaklasa `type`

W Pythonie domyślną metaklasą jest `type`.

To właśnie dlatego:

```python
type(Pies)
```

zwraca `type`.

---

## `type` jako metaklasa

`type` jest wyjątkowe, bo:

- jest klasą,
- tworzy klasy,
- można go użyć także bezpośrednio.

---

## `type` do dynamicznego tworzenia klas

Przykład:

```python
Pies = type("Pies", (), {})
```

To tworzy klasę dynamicznie.

Można też dodać atrybuty:

```python
Pies = type("Pies", (), {"gatunek": "pies"})
```

To mniej czytelne niż zwykłe `class`, ale pokazuje, co dzieje się pod spodem.

---

## Po co w ogóle używać metaklas

Najczęściej do:

- automatycznego modyfikowania klas przy ich tworzeniu,
- walidowania definicji klas,
- rejestrowania klas,
- budowania frameworków i bibliotek.

To raczej narzędzie dla bardziej zaawansowanych zastosowań niż do codziennego prostego kodu.

---

## Najprostsza własna metaklasa

```python
class Meta(type):
    pass
```

Taka klasa dziedziczy po `type`, więc sama jest metaklasą.

Można jej użyć tak:

```python
class MojaKlasa(metaclass=Meta):
    pass
```

---

## `__new__` w metaklasie

To jedno z najważniejszych miejsc, gdzie kontroluje się tworzenie klasy.

Przykład:

```python
class Meta(type):
    def __new__(mcls, name, bases, namespace):
        print(f"Tworze klase {name}")
        return super().__new__(mcls, name, bases, namespace)
```

Teraz:

```python
class Test(metaclass=Meta):
    pass
```

spowoduje dodatkowe działanie przy tworzeniu klasy.

---

## `__init__` w metaklasie

Można też wykonywać logikę w `__init__` metaklasy.

To kolejny etap po stworzeniu klasy.

W praktyce początkującego najważniejsze jest jednak zrozumienie, że metaklasa może przechwycić moment tworzenia klasy.

---

## `__call__` w metaklasie

Metaklasa może też wpływać na to, co dzieje się przy tworzeniu instancji klasy.

To już temat bardziej zaawansowany, ale warto wiedzieć, że metaklasa może kontrolować nie tylko klasę, ale też sposób wywoływania klasy.

---

## Kontrolowanie tworzenia klas

To jeden z głównych powodów używania metaklas.

Możesz np.:

- wymusić obecność konkretnej metody,
- automatycznie dopisać atrybuty,
- rejestrować klasy.

---

## Walidowanie klas przez metaklasę

Przykład idei:

```python
class Meta(type):
    def __new__(mcls, name, bases, namespace):
        if "uruchom" not in namespace:
            raise TypeError("Klasa musi miec metode uruchom")
        return super().__new__(mcls, name, bases, namespace)
```

To już pokazuje, że metaklasa może sprawdzać definicję klasy.

---

## Metaklasy a dekoratory klas

Czasem metaklasa nie jest potrzebna, bo wystarczy dekorator klasy.

To ważne pytanie projektowe:

czy naprawdę potrzebujesz metaklasy, czy da się to zrobić prościej?

W wielu przypadkach prościej.

---

## Kiedy metaklasa ma sens

Najczęściej wtedy, gdy:

- tworzysz framework,
- budujesz rozbudowaną bibliotekę,
- potrzebujesz centralnie kontrolować klasy.

W zwykłych małych programach bardzo rzadko jest konieczna.

---

## Kiedy metaklasa to zły pomysł

Gdy:

- da się to zrobić zwykłą klasą,
- wystarczy dekorator,
- rozwiązanie staje się zbyt trudne do zrozumienia,
- komplikacja przewyższa korzyść.

---

## Typowe błędy początkujących

### 1. Próba używania metaklas za wcześnie

### 2. Mylenie klasy z metaklasą

### 3. Używanie metaklasy do problemów, które da się rozwiązać dużo prościej

### 4. Brak zrozumienia `type`

---

## Praktyczne przykłady

### `type` dynamicznie

```python
Pies = type("Pies", (), {"gatunek": "pies"})
print(Pies.gatunek)
```

### Prosta metaklasa

```python
class Meta(type):
    def __new__(mcls, name, bases, namespace):
        namespace["opis"] = "Dodano przez metaklase"
        return super().__new__(mcls, name, bases, namespace)

class Test(metaclass=Meta):
    pass

print(Test.opis)
```

### Walidacja klasy

```python
class WymagajUruchom(type):
    def __new__(mcls, name, bases, namespace):
        if name != "Bazowa" and "uruchom" not in namespace:
            raise TypeError("Brak metody uruchom")
        return super().__new__(mcls, name, bases, namespace)
```

---

## Dobre praktyki

### Traktuj metaklasy jako narzędzie zaawansowane

### Najpierw szukaj prostszego rozwiązania

### Jeśli używasz metaklasy, dokumentuj to bardzo jasno

### Zadbaj o czytelność, bo ten temat szybko robi się trudny

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- klasa w Pythonie też jest obiektem,
- klasy są zwykle instancjami `type`,
- metaklasa to klasa tworząca klasy,
- metaklasy służą do bardziej zaawansowanej kontroli tworzenia klas,
- w codziennym kodzie są potrzebne rzadko,
- najpierw warto bardzo dobrze rozumieć zwykłe klasy i OOP.

---

## Mini ściąga

```python
class Meta(type):
    pass

class Test(metaclass=Meta):
    pass
```

### Ważna intuicja

- obiekt -> instancja klasy
- klasa -> instancja metaklasy

---

## Ćwiczenia

### Ćwiczenie 1

Sprawdź `type()` dla własnej klasy.

### Ćwiczenie 2

Utwórz prostą klasę przez `type(...)`.

### Ćwiczenie 3

Napisz prostą metaklasę, która dodaje klasie atrybut `opis`.

---

## Przykładowe rozwiązania

### Ćwiczenie 1

```python
class A:
    pass

print(type(A))
```

### Ćwiczenie 2

```python
Pies = type("Pies", (), {"gatunek": "pies"})
print(Pies.gatunek)
```

### Ćwiczenie 3

```python
class Meta(type):
    def __new__(mcls, name, bases, namespace):
        namespace["opis"] = "dodano automatycznie"
        return super().__new__(mcls, name, bases, namespace)

class Test(metaclass=Meta):
    pass

print(Test.opis)
```
