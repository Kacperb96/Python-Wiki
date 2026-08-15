# Dependency Injection w Pythonie

## O co tutaj chodzi?

Dependency Injection, czyli wstrzykiwanie zależności, to sposób budowania kodu, w którym obiekt **nie tworzy sam swoich współpracowników**, tylko **dostaje ich z zewnątrz**.

Brzmi technicznie, ale idea jest bardzo praktyczna.

Bez DI klasa często robi coś takiego:

- sama tworzy połączenie do bazy,
- sama tworzy klienta API,
- sama tworzy logger,
- sama decyduje, z jakiej implementacji korzysta.

Wtedy kod staje się:

- trudniejszy do testowania,
- mocno powiązany z konkretną implementacją,
- mniej elastyczny,
- trudniejszy do rozbudowy.

Z DI robimy odwrotnie:

- klasa dostaje zależności w parametrze konstruktora lub funkcji,
- nie interesuje jej, **jak** dana zależność została utworzona,
- interesuje ją tylko to, że może z niej korzystać.

## Intuicja życiowa

Wyobraź sobie klasę `OrderService`, która ma wysłać e-mail po złożeniu zamówienia.

Złe podejście:

- `OrderService` sama tworzy `EmailSender()`.

Lepsze podejście:

- `OrderService` dostaje gotowy obiekt `email_sender`.

Dzięki temu:

- możesz podmienić prawdziwy sender na testowy,
- możesz łatwo zmienić implementację,
- `OrderService` zajmuje się tylko logiką zamówienia.

## Problem bez Dependency Injection

### Słaby przykład mentalny

```python
class EmailSender:
    def send(self, to, subject, body):
        print(f"Wysylam e-mail do {to}")


class OrderService:
    def complete_order(self, user_email):
        email_sender = EmailSender()
        email_sender.send(user_email, "Zamowienie", "Dziekujemy")
```

Na pierwszy rzut oka to działa. Problem pojawia się później.

### Co tu jest nie tak?

`OrderService`:

- zna konkretną klasę `EmailSender`,
- sama ją tworzy,
- nie da się jej łatwo przetestować z atrapą,
- trudno zmienić sposób wysyłki.

Jeżeli później zechcesz:

- wysyłać SMS zamiast e-maila,
- użyć innej biblioteki,
- testować bez wysyłania prawdziwej wiadomości,

musisz modyfikować `OrderService`.

To znak zbyt silnego sprzężenia.

## Lepsze podejście: zależność z zewnątrz

```python
class EmailSender:
    def send(self, to, subject, body):
        print(f"Wysylam e-mail do {to}")


class OrderService:
    def __init__(self, email_sender):
        self.email_sender = email_sender

    def complete_order(self, user_email):
        self.email_sender.send(user_email, "Zamowienie", "Dziekujemy")
```

Teraz:

- `OrderService` nie tworzy zależności samodzielnie,
- dostaje ją z zewnątrz,
- można podać dowolny obiekt z metodą `send()`.

To jest właśnie sedno Dependency Injection.

## Formy wstrzykiwania zależności

Najczęściej spotkasz kilka form.

### 1. Constructor Injection

Zależność trafia do konstruktora `__init__`.

```python
class UserService:
    def __init__(self, repository):
        self.repository = repository
```

To najczęściej najlepszy i najczytelniejszy wariant.

Dobrze działa, gdy zależność jest wymagana do działania obiektu.

### 2. Parameter Injection

Zależność jest przekazywana bezpośrednio do metody.

```python
def generate_report(data, formatter):
    return formatter.format(data)
```

Dobre, gdy zależność potrzebna jest tylko w jednej operacji.

### 3. Setter Injection

Zależność jest ustawiana po utworzeniu obiektu.

```python
class Service:
    def set_logger(self, logger):
        self.logger = logger
```

Możliwe, ale zwykle mniej bezpieczne, bo obiekt może istnieć chwilowo w niepełnym stanie.

## Dlaczego DI pomaga?

### 1. Testowalność

Możesz podstawić atrapę lub fake.

```python
class FakeEmailSender:
    def __init__(self):
        self.sent_messages = []

    def send(self, to, subject, body):
        self.sent_messages.append((to, subject, body))


fake_sender = FakeEmailSender()
service = OrderService(fake_sender)
service.complete_order("anna@example.com")

print(fake_sender.sent_messages)
```

Przykładowy output:

```python
[("anna@example.com", "Zamowienie", "Dziekujemy")]
```

Nie musisz odpalać prawdziwej wysyłki. Test jest szybki i przewidywalny.

### 2. Mniejsze sprzężenie

Klasa zależy od zachowania, a nie od szczegółów tworzenia obiektu.

### 3. Łatwiejsza wymiana implementacji

Możesz dziś używać `EmailSender`, a jutro `SmsSender` lub `NotificationSender`.

### 4. Czytelniejsza architektura

Od razu widać, od czego klasa zależy.

## Python i duck typing a DI

W Pythonie DI jest wygodne, bo język nie wymaga sztywnych interfejsów jak część innych języków.

Jeśli obiekt ma potrzebną metodę, to często już wystarczy.

```python
class ConsoleLogger:
    def log(self, message):
        print(message)


class FileLogger:
    def log(self, message):
        print(f"Zapis do pliku: {message}")


class AppService:
    def __init__(self, logger):
        self.logger = logger

    def run(self):
        self.logger.log("Start aplikacji")
```

Oba loggery mogą działać z `AppService`, jeśli mają metodę `log()`.

## Kiedy warto dodać Protocol?

W większych projektach można doprecyzować oczekiwany interfejs przez `Protocol`.

```python
from typing import Protocol


class LoggerProtocol(Protocol):
    def log(self, message: str) -> None:
        ...


class AppService:
    def __init__(self, logger: LoggerProtocol):
        self.logger = logger
```

To daje:

- czytelniejszy kontrakt,
- lepsze wsparcie narzędzi typu mypy,
- większą jasność dla innych programistów.

## Czego DI nie oznacza?

Dependency Injection nie oznacza, że:

- trzeba używać skomplikowanego frameworka,
- trzeba wszędzie tworzyć fabryki i kontenery,
- każda funkcja musi przyjmować 10 zależności.

Na początku DI to po prostu zdrowa zasada:

- nie twórz wszystkiego wewnątrz klasy,
- przekazuj zależności jawnie.

## Zły i dobry przykład

### Zły przykład

```python
class ReportService:
    def generate(self):
        db = DatabaseConnection()
        logger = FileLogger()
        data = db.get_data()
        logger.log("Pobrano dane")
        return data
```

Problemy:

- klasa sama tworzy zależności,
- trudno ją testować,
- trudno podmienić bazę lub logger.

### Lepszy przykład

```python
class ReportService:
    def __init__(self, db, logger):
        self.db = db
        self.logger = logger

    def generate(self):
        data = self.db.get_data()
        self.logger.log("Pobrano dane")
        return data
```

Teraz konfiguracja dzieje się na zewnątrz, a klasa skupia się na swojej pracy.

## Gdzie tworzyć zależności?

To ważne pytanie.

Zwykle:

- obiekty tworzymy na poziomie „wejścia” do aplikacji,
- a potem przekazujemy je dalej.

Przykład:

```python
repository = UserRepository()
logger = ConsoleLogger()
service = UserService(repository, logger)
```

Czyli:

- na brzegu aplikacji składamy obiekty,
- wewnątrz aplikacji używamy już gotowych zależności.

To często nazywa się **composition root**.

## Najczęstsze błędy

### 1. Udawane DI

```python
class Service:
    def __init__(self, repo=None):
        self.repo = repo or UserRepository()
```

To jest częściowo lepsze niż nic, ale nadal klasa zna konkretną implementację.

### 2. Zbyt wiele zależności

Jeśli konstruktor ma 9 parametrów, to często znak, że klasa robi za dużo.

### 3. Wstrzykiwanie wszystkiego na siłę

Nie każda drobna rzecz potrzebuje osobnej abstrakcji.

### 4. Mylenie DI z globalami

```python
logger = ConsoleLogger()

class Service:
    def run(self):
        logger.log("hello")
```

To nie jest DI. To ukryta zależność globalna.

## Praktyczne wskazówki

- Wymagane zależności podawaj przez `__init__`.
- Staraj się zależeć od zachowania, nie od konkretnej implementacji.
- Konfiguruj obiekty na brzegu aplikacji.
- Jeśli klasa ma za dużo zależności, sprawdź, czy nie robi za dużo.
- W testach podmieniaj zależności na fake lub mock.

## Szybka ściąga

DI oznacza:

- obiekt nie tworzy sam zależności,
- zależności dostaje z zewnątrz,
- kod jest bardziej elastyczny i testowalny.

Najczęściej używaj:

- constructor injection.

Największa korzyść:

- łatwe testy i mniejsze sprzężenie.

## Ćwiczenia

1. Napisz klasę `MessageService`, która bez DI sama tworzy `ConsoleSender`.
2. Przerób ją tak, aby `sender` był przekazywany przez `__init__`.
3. Dodaj drugą implementację wysyłki, np. `FileSender`.
4. Napisz fake sender do testów, który zapisuje wiadomości do listy.
5. Zbuduj `OrderService`, która korzysta z repozytorium i loggera przekazywanych z zewnątrz.
6. Zastanów się, czy klasa z 7 zależnościami nie łamie zasady jednej odpowiedzialności.

## Najważniejsze do zapamiętania

- Dependency Injection zmniejsza sprzężenie między klasami.
- Klasa nie powinna sama tworzyć wszystkich swoich współpracowników.
- Najwygodniej przekazywać zależności przez konstruktor.
- DI bardzo ułatwia testowanie.
- W Pythonie DI dobrze współgra z duck typing i `Protocol`.
