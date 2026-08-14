# Deskryptory w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest deskryptor](#czym-jest-deskryptor)
3. [Dlaczego to ważny temat](#dlaczego-to-ważny-temat)
4. [`__get__`](#__get__)
5. [`__set__`](#__set__)
6. [`__delete__`](#__delete__)
7. [Deskryptor tylko do odczytu](#deskryptor-tylko-do-odczytu)
8. [Deskryptor walidujący dane](#deskryptor-walidujący-dane)
9. [Deskryptory a `property`](#deskryptory-a-property)
10. [Deskryptory a ORM-y](#deskryptory-a-orm-y)
11. [Deskryptor danych i niedanych](#deskryptor-danych-i-niedanych)
12. [Jak Python szuka atrybutów](#jak-python-szuka-atrybutów)
13. [Typowe błędy początkujących](#typowe-błędy-początkujących)
14. [Praktyczne przykłady](#praktyczne-przykłady)
15. [Dobre praktyki](#dobre-praktyki)
16. [Podsumowanie](#podsumowanie)
17. [Mini ściąga](#mini-ściąga)
18. [Ćwiczenia](#ćwiczenia)
19. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Deskryptory to jeden z bardziej zaawansowanych mechanizmów Pythona.

Na pierwszy rzut oka nie widać ich często w zwykłym kodzie, ale pod spodem są bardzo ważne.

To właśnie deskryptory stoją za:

- `property`,
- metodami związanymi z atrybutami,
- wieloma mechanizmami ORM-ów,
- częścią działania modelu obiektowego Pythona.

---

## Czym jest deskryptor

Deskryptor to obiekt, który kontroluje dostęp do atrybutu.

Najprościej:

zamiast zwykłego przechowywania wartości, możesz przejąć:

- odczyt,
- zapis,
- usuwanie.

Dzieje się to przez specjalne metody:

- `__get__`
- `__set__`
- `__delete__`

---

## Dlaczego to ważny temat

Bo pokazuje, że w Pythonie dostęp do atrybutu może być czymś dużo bardziej inteligentnym niż zwykłe „weź z pamięci”.

To daje:

- walidację,
- kontrolę,
- leniwe obliczanie,
- integrację z frameworkami.

---

## `__get__`

Obsługuje odczyt atrybutu.

Przykład idei:

```python
def __get__(self, instance, owner):
    ...
```

`instance` to obiekt instancji, a `owner` to klasa.

---

## `__set__`

Obsługuje przypisanie:

```python
obiekt.pole = wartosc
```

Możesz tam robić walidację albo inne akcje.

---

## `__delete__`

Obsługuje usuwanie:

```python
del obiekt.pole
```

---

## Deskryptor tylko do odczytu

Możesz zrobić deskryptor, który pozwala tylko czytać.

Przykład:

```python
class TylkoDoOdczytu:
    def __get__(self, instance, owner):
        return 42
```

Przykład użycia:

```python
class Test:
    wartosc = TylkoDoOdczytu()

t = Test()
print(t.wartosc)
```

Wynik:

```python
42
```

---

## Deskryptor walidujący dane

To bardzo częsty sensowny przykład.

```python
class DodatniaLiczba:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Musi byc dodatnia")
        instance.__dict__[self.name] = value
```

To już bardzo praktyczna wersja.

Przykład użycia:

```python
class Produkt:
    cena = DodatniaLiczba()

    def __init__(self, cena):
        self.cena = cena

p = Produkt(100)
print(p.cena)
```

Wynik:

```python
100
```

---

## Deskryptory a `property`

`property` to w praktyce wygodny, gotowy deskryptor.

Dlatego zrozumienie deskryptorów pomaga zrozumieć, jak naprawdę działa `@property`.

---

## Deskryptory a ORM-y

W ORM-ach pola modelu często nie są zwykłymi atrybutami.

Framework może przechwytywać odczyt i zapis:

- walidować dane,
- śledzić zmiany,
- budować zapytania,
- mapować pola na bazę danych.

Deskryptory są jednym z mechanizmów, które to umożliwiają.

---

## Deskryptor danych i niedanych

To ważne rozróżnienie:

### Deskryptor danych

Ma `__set__` albo `__delete__`.

### Deskryptor niedanych

Ma tylko `__get__`.

To wpływa na priorytet przy wyszukiwaniu atrybutów.

---

## Jak Python szuka atrybutów

Python ma określoną kolejność przy dostępie do atrybutów.

Deskryptory wchodzą w tę logikę bardzo głęboko.

Na poziomie początkująco-średnim najważniejsze jest to:

deskryptor może przejąć kontrolę nad atrybutem zamiast zwykłego odczytu ze słownika obiektu.

To jest jeden z powodów, dla których temat wydaje się trudny:

pod prostym zapisem:

```python
obiekt.pole
```

może kryć się dużo więcej niż zwykły odczyt wartości.

---

## Typowe błędy początkujących

- próba nauki deskryptorów bez zrozumienia `property`,
- brak zrozumienia `instance.__dict__`,
- mylenie deskryptora z zwykłą klasą pomocniczą,
- zbyt szybkie używanie ich tam, gdzie wystarczy prostsze rozwiązanie.

---

## Praktyczne przykłady

```python
class Dodatnia:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Wartosc musi byc dodatnia")
        instance.__dict__[self.name] = value
```

```python
class Produkt:
    cena = Dodatnia()

    def __init__(self, cena):
        self.cena = cena
```

Przykład użycia:

```python
p = Produkt(50)
print(p.cena)
```

Wynik:

```python
50
```

Jeśli spróbujesz:

```python
p.cena = -10
```

to dostaniesz:

```python
ValueError
```

---

## Dobre praktyki

- traktuj deskryptory jako temat zaawansowany,
- używaj ich, gdy naprawdę potrzebujesz centralnej kontroli atrybutów,
- do prostych przypadków zwykle wystarczy `property`,
- rozumiej, że to mechanizm stojący pod spodem wielu narzędzi.

Praktyczna zasada:

jeśli chcesz kontrolować jedno pole w jednej klasie, `@property` często będzie czytelniejsze.

Jeśli chcesz ten sam mechanizm walidacji lub dostępu współdzielić między wieloma klasami i polami, deskryptor robi się dużo ciekawszy.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- deskryptor kontroluje dostęp do atrybutu,
- opiera się na `__get__`, `__set__`, `__delete__`,
- `property` jest przykładem deskryptora,
- deskryptory są ważne dla bardziej zaawansowanego modelu obiektowego Pythona.

Najważniejsze do zapamiętania:

- deskryptor to nie „dziwna klasa pomocnicza”, tylko oficjalny mechanizm modelu atrybutów w Pythonie,
- dzięki niemu zwykły zapis `obiekt.pole` może uruchamiać własną logikę,
- to temat zaawansowany, ale bardzo rozwijający zrozumienie OOP w Pythonie.

---

## Mini ściąga

```python
def __get__(self, instance, owner): ...
def __set__(self, instance, value): ...
def __delete__(self, instance): ...
```

---

## Ćwiczenia

### Ćwiczenie 1

Napisz deskryptor walidujący liczbę dodatnią.

### Ćwiczenie 2

Użyj go w klasie `Produkt`.

---

## Przykładowe rozwiązania

```python
class Dodatnia:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Za mala wartosc")
        instance.__dict__[self.name] = value
```
