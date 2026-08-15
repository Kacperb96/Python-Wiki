# SOLID w Pythonie

## Czym jest SOLID?

SOLID to zestaw pięciu zasad projektowania kodu obiektowego, które pomagają pisać kod:

- czytelniejszy,
- łatwiejszy do rozbudowy,
- mniej kruchy,
- prostszy w testowaniu,
- bardziej odporny na zmiany.

To nie są magiczne przepisy. To raczej zestaw pytań kontrolnych, które pomagają zauważyć, że architektura zaczyna się psuć.

Skrót SOLID oznacza:

- `S` – Single Responsibility Principle,
- `O` – Open/Closed Principle,
- `L` – Liskov Substitution Principle,
- `I` – Interface Segregation Principle,
- `D` – Dependency Inversion Principle.

W Pythonie trzeba do tego podejść rozsądnie.

Python jest językiem dynamicznym, więc nie wszystko wdraża się tak samo jak np. w Javie czy C#. Nie chodzi o produkowanie dziesiątek klas i interfejsów, tylko o budowanie kodu, który dobrze się rozwija.

---

## S – Single Responsibility Principle

### Jedna klasa lub funkcja powinna mieć jeden główny powód do zmiany

To chyba najważniejsza zasada na start.

Jeśli jedna klasa:

- liczy dane,
- zapisuje do bazy,
- generuje PDF,
- wysyła e-mail,
- loguje błędy,

to prawdopodobnie robi za dużo.

### Zły przykład

```python
class InvoiceService:
    def calculate_total(self, items):
        return sum(item["price"] for item in items)

    def save_to_database(self, invoice):
        print("Zapis do bazy")

    def send_email(self, email):
        print(f"Wysylka e-mail do {email}")
```

Ta klasa miesza:

- logikę biznesową,
- persystencję,
- komunikację.

### Lepszy kierunek

```python
class InvoiceCalculator:
    def calculate_total(self, items):
        return sum(item["price"] for item in items)


class InvoiceRepository:
    def save(self, invoice):
        print("Zapis do bazy")


class EmailSender:
    def send(self, email):
        print(f"Wysylka e-mail do {email}")
```

Teraz każda część ma wyraźniejszą odpowiedzialność.

### Pytanie kontrolne

Czy potrafisz jednym zdaniem opisać, za co odpowiada dana klasa?

Jeśli nie, to możliwe, że narusza SRP.

---

## O – Open/Closed Principle

### Kod powinien być otwarty na rozszerzanie, ale zamknięty na modyfikację

Idea jest taka:

- gdy pojawia się nowy przypadek,
- wolisz dopisać nową implementację,
- niż stale rozgrzebywać starą klasę pełną `if`-ów.

### Zły przykład

```python
class DiscountCalculator:
    def calculate(self, customer_type, price):
        if customer_type == "regular":
            return price
        if customer_type == "vip":
            return price * 0.8
        if customer_type == "student":
            return price * 0.9
```

Za każdym nowym typem klienta trzeba modyfikować klasę.

### Lepszy kierunek

```python
class RegularDiscount:
    def calculate(self, price):
        return price


class VipDiscount:
    def calculate(self, price):
        return price * 0.8


class StudentDiscount:
    def calculate(self, price):
        return price * 0.9
```

Kod używający zniżki może dostać odpowiednią strategię z zewnątrz.

Wtedy nowy typ zniżki oznacza zwykle dodanie nowej klasy, a nie psucie starej.

### Uwaga praktyczna

Nie każdy `if` łamie OCP. Jeśli masz 2 proste przypadki i kod jest mały, nie trzeba od razu budować całego systemu strategii.

---

## L – Liskov Substitution Principle

### Klasy potomne powinny dać się podstawiać za klasę bazową bez psucia programu

Brzmi abstrakcyjnie, ale chodzi o prostą rzecz:

- jeśli coś jest „rodzajem” czegoś innego,
- to powinno zachowywać się zgodnie z oczekiwaniami wobec typu bazowego.

### Klasyczny zły przykład

```python
class Bird:
    def fly(self):
        print("Lecę")


class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Pingwin nie lata")
```

Tu dziedziczenie jest złe, bo `Penguin` nie spełnia obietnicy typu `Bird` z metodą `fly()`.

### Co zrobić lepiej?

Można rozdzielić model:

```python
class Bird:
    pass


class FlyingBird(Bird):
    def fly(self):
        print("Lecę")


class Penguin(Bird):
    def swim(self):
        print("Płynę")
```

### Jak rozpoznawać naruszenia LSP?

Jeśli klasa potomna:

- rzuca wyjątek dla bazowej operacji,
- ignoruje ważne zachowanie,
- zmienia sens metody,
- wymaga innych warunków wejścia,

to możliwe, że projekt jest zły.

---

## I – Interface Segregation Principle

### Lepiej mieć kilka małych interfejsów niż jeden wielki

W Pythonie rzadziej używa się klasycznych interfejsów, ale idea nadal jest bardzo cenna.

Jeśli obiekt musi implementować metody, których nie potrzebuje, to coś jest nie tak.

### Zły przykład mentalny

Wyobraź sobie interfejs:

- `print_document()`
- `scan_document()`
- `fax_document()`

A potem masz klasę prostego urządzenia, które tylko drukuje. Musi udawać, że wspiera skanowanie i faks.

To zły projekt.

### Lepszy kierunek

Rozdziel zachowania:

- osobny kontrakt dla drukowania,
- osobny dla skanowania,
- osobny dla wysyłki.

### W Pythonie często realizujesz to przez:

- małe klasy,
- kompozycję,
- `Protocol`,
- wstrzykiwanie tylko potrzebnych zależności.

Przykład z `Protocol`:

```python
from typing import Protocol


class Printer(Protocol):
    def print_document(self, text: str) -> None:
        ...
```

Jeśli jakaś funkcja potrzebuje tylko drukowania, nie powinna wymagać jeszcze skanowania i eksportu PDF.

---

## D – Dependency Inversion Principle

### Wysokopoziomowe moduły nie powinny zależeć od niskopoziomowych szczegółów

To zasada mocno związana z Dependency Injection.

Chodzi o to, żeby logika biznesowa nie była przywiązana do konkretnej technologii.

### Zły przykład

```python
class MySQLDatabase:
    def save(self, data):
        print("Zapis do MySQL")


class UserService:
    def __init__(self):
        self.database = MySQLDatabase()

    def register(self, user):
        self.database.save(user)
```

Problem:

- `UserService` zależy od konkretnej implementacji.

### Lepszy kierunek

```python
class UserService:
    def __init__(self, repository):
        self.repository = repository

    def register(self, user):
        self.repository.save(user)
```

Teraz `UserService` zależy od zachowania repozytorium, a nie od szczegółu technologicznego.

W Pythonie można to wspierać przez:

- duck typing,
- `Protocol`,
- Dependency Injection.

---

## Czy trzeba stosować wszystkie zasady zawsze?

Nie.

To bardzo ważne.

SOLID nie służy do tego, żeby:

- mnożyć klasy bez potrzeby,
- komplikować mały skrypt,
- udawać enterprise tam, gdzie wystarczy prosta funkcja.

Jeśli masz mały plik i 30 linii kodu, to rozbudowana architektura może być gorsza niż prosty kod.

Ale gdy projekt rośnie, SOLID pomaga zauważać problemy wcześniej.

## SOLID w praktyce Pythona

W Pythonie dobre praktyki związane z SOLID często wyglądają tak:

- mniejsze klasy i funkcje,
- kompozycja zamiast ciężkiego dziedziczenia,
- zależności przekazywane z zewnątrz,
- unikanie klas „wszystko w jednym”,
- `Protocol` tam, gdzie kontrakt ma znaczenie,
- sensowne rozdzielanie odpowiedzialności między moduły.

## Jak nie popaść w przesadę?

### Zły kierunek

- 12 klas dla bardzo prostego zadania,
- abstrakcje bez realnej potrzeby,
- interfejsy tylko „bo SOLID”,
- kod trudniejszy niż problem, który rozwiązuje.

### Lepszy kierunek

- najpierw prosty kod,
- potem refaktoryzacja, gdy rośnie złożoność,
- abstrakcje dopiero wtedy, gdy rzeczywiście coś upraszczają.

## Szybka ściąga

### SRP

Jedna odpowiedzialność.

### OCP

Rozszerzaj przez dodawanie, nie ciągłe przerabianie istniejącego kodu.

### LSP

Typ potomny nie może łamać obietnic typu bazowego.

### ISP

Nie zmuszaj obiektów do implementowania rzeczy, których nie potrzebują.

### DIP

Logika wysokiego poziomu nie powinna zależeć od technologicznych detali.

## Ćwiczenia

1. Weź klasę, która liczy, zapisuje i loguje, i rozbij ją zgodnie z SRP.
2. Napisz kalkulator zniżek oparty na `if`, a potem przerób go na osobne strategie.
3. Znajdź przykład złego dziedziczenia i zamień je na kompozycję lub lepszą hierarchię.
4. Zdefiniuj `Protocol` dla repozytorium i użyj go w serwisie.
5. Sprawdź klasę z projektu i odpowiedz, którą zasadę SOLID łamie najbardziej.
6. Zbuduj prosty `NotificationService`, do którego można wstrzykiwać różne sposoby wysyłki.

## Najważniejsze do zapamiętania

- SOLID to zestaw zasad pomagających projektować kod, który dobrze się rozwija.
- Najbardziej praktyczne na początku są SRP i DIP.
- W Pythonie często lepiej stawiać na kompozycję niż ciężkie dziedziczenie.
- Nie chodzi o ślepe stosowanie wzorców, tylko o świadome upraszczanie architektury.
- Dobra architektura ma pomagać, a nie imponować liczbą abstrakcji.
