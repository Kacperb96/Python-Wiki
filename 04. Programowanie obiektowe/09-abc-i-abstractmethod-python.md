# `abc` i `@abstractmethod` w Pythonie

## Wprowadzenie

W OOP czasem chcesz powiedzieć:

- ta klasa opisuje wspólny kontrakt,
- nie powinna być tworzona bezpośrednio,
- klasy potomne muszą zaimplementować pewne metody.

Właśnie do tego służą:

- moduł `abc`,
- `ABC`,
- `@abstractmethod`.

To jest bardzo przydatne, gdy budujesz:

- wspólne API klas,
- bazę dla wielu implementacji,
- warstwę, która ma wymagać określonych metod od klas potomnych.

## Problem bez klasy abstrakcyjnej

Załóżmy, że chcesz mieć różne płatności:

```python
class PaymentMethod:
    def pay(self, amount):
        pass
```

To jest słabe, bo:

- klasa bazowa nic realnie nie wymusza,
- można utworzyć obiekt `PaymentMethod()`,
- można zapomnieć nadpisać metodę w klasie potomnej.

## Najprostsza klasa abstrakcyjna

```python
from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
```

To znaczy:

- `PaymentMethod` jest klasą abstrakcyjną,
- metoda `pay()` musi zostać zaimplementowana przez klasę potomną.

## Co się stanie, jeśli spróbujesz utworzyć klasę abstrakcyjną

```python
from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


PaymentMethod()
```

Output:

```python
TypeError: Can't instantiate abstract class PaymentMethod with abstract method pay
```

To bardzo ważne:

Python nie pozwoli utworzyć klasy, która nadal ma niespełniony kontrakt abstrakcyjny.

## Implementacja klasy potomnej

```python
from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Placę kartą: {amount}"


payment = CardPayment()
print(payment.pay(120))
```

Output:

```python
Placę kartą: 120
```

## Co jeśli klasa potomna nie zaimplementuje metody

```python
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    pass


Dog()
```

Output:

```python
TypeError: Can't instantiate abstract class Dog with abstract method sound
```

To właśnie daje realne wymuszenie kontraktu.

## Po co to w praktyce

To bardzo przydatne, gdy:

- masz kilka implementacji tego samego pomysłu,
- chcesz uniknąć "pustych klas bazowych",
- chcesz jasno powiedzieć innym programistom, co trzeba zaimplementować.

Przykłady:

- różne bramki płatności,
- różne magazyny danych,
- różne typy raportów,
- różne źródła powiadomień,
- różne strategie liczenia ceny.

## Abstrakcyjna klasa bazowa z częścią wspólną

Klasa abstrakcyjna nie musi być pusta.

Może mieć:

- pola,
- zwykłe metody,
- wspólną logikę,
- i tylko część metod abstrakcyjnych.

```python
from abc import ABC, abstractmethod


class Report(ABC):
    def header(self):
        return "=== RAPORT ==="

    @abstractmethod
    def generate(self):
        pass


class SalesReport(Report):
    def generate(self):
        return "Dane sprzedażowe"


report = SalesReport()
print(report.header())
print(report.generate())
```

Output:

```python
=== RAPORT ===
Dane sprzedażowe
```

To bardzo praktyczny układ:

- wspólne rzeczy są w bazie,
- specyficzne rzeczy wymuszasz jako abstrakcyjne.

## Abstrakcyjna właściwość

Można wymuszać też `property`.

```python
from abc import ABC, abstractmethod


class Shape(ABC):
    @property
    @abstractmethod
    def name(self):
        pass
```

To znaczy, że klasy potomne muszą udostępnić tę właściwość.

## Polimorfizm + `abc`

To naturalne połączenie.

```python
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Hau"


class Cat(Animal):
    def sound(self):
        return "Miau"


animals = [Dog(), Cat()]

for animal in animals:
    print(animal.sound())
```

Output:

```python
Hau
Miau
```

Tu `abc` pomaga pilnować, że każdy `Animal` naprawdę umie zrobić `sound()`.

## `abc` vs duck typing

Python bardzo często działa dobrze bez klas abstrakcyjnych.

To ważne.

Nie zawsze potrzebujesz `ABC`.

Python lubi styl:

`jeśli obiekt zachowuje się jak trzeba, to go użyj`

czyli duck typing.

Dlatego `abc` ma sens głównie wtedy, gdy:

- chcesz jawnego kontraktu,
- pracujesz w większym kodzie,
- zależy Ci na czytelności architektury,
- chcesz jasno wymuszyć implementację.

## Kiedy `abc` ma sens

- wspólna baza dla kilku implementacji,
- projekt biblioteczny,
- większy system z kilkoma adapterami,
- architektura z wyraźnymi kontraktami.

## Kiedy `abc` bywa przesadą

- mały skrypt,
- dwie klasy, które i tak są bardzo proste,
- przypadki, gdzie wystarcza zwykła metoda w klasie bazowej,
- sytuacje, gdzie duck typing daje prostszy kod.

## Typowe błędy początkujących

### 1. Robienie `ABC` za wcześnie

Nie każda klasa bazowa musi być abstrakcyjna.

### 2. Nadmierna architektura

Tworzenie pięciu warstw abstrakcji dla bardzo prostego programu.

### 3. Mylenie klasy abstrakcyjnej z interfejsem z innych języków

Python nie wymaga kopiowania stylu z Javy 1:1.

### 4. Pusta abstrakcja bez sensu domenowego

Jeśli nie umiesz powiedzieć, jaki kontrakt naprawdę wymuszasz, to może `ABC` nie jest potrzebne.

## Mini case study

Masz system powiadomień:

- e-mail,
- SMS,
- push.

Każdy typ powiadomienia musi mieć metodę `send(message)`.

Bez `ABC` łatwo zrobić klasę, która zapomni tę metodę wdrożyć.

Z `ABC` kontrakt jest jawny i wymuszony.

## Dobre praktyki

- używaj `ABC`, gdy naprawdę chcesz wymusić kontrakt,
- nie rób abstrakcji dla samej abstrakcji,
- łącz `abc` z polimorfizmem i sensownym modelem domeny,
- pamiętaj, że zwykła klasa lub duck typing często też są bardzo dobrym wyborem.

## Szybka ściąga

Najczęściej przydatne:

- `from abc import ABC, abstractmethod`
- `class MyBase(ABC): ...`
- `@abstractmethod`
- abstrakcyjna metoda + wspólna logika w klasie bazowej

## Zadania

1. Zbuduj abstrakcyjną klasę `Shape` z metodą `area()`.
2. Utwórz klasy `Rectangle` i `Circle`, które implementują `area()`.
3. Pokaż, co się stanie, gdy spróbujesz utworzyć obiekt klasy abstrakcyjnej.
4. Zbuduj abstrakcyjną klasę `Notifier` z metodą `send(message)`.
5. Opisz, kiedy `ABC` ma sens, a kiedy jest przesadą.
