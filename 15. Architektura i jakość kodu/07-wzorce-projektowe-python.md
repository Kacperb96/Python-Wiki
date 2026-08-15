# Wzorce projektowe w Pythonie

## Czym są wzorce projektowe?

Wzorce projektowe to powtarzalne sposoby rozwiązywania typowych problemów projektowych.

To nie są gotowe biblioteki ani specjalne elementy języka. To raczej sprawdzone pomysły na organizację kodu.

Ważne:

- wzorzec nie jest celem samym w sobie,
- wzorzec ma rozwiązywać realny problem,
- źle użyty wzorzec może tylko skomplikować kod.

W Pythonie szczególnie łatwo przesadzić, bo wiele problemów można rozwiązać prościej niż w bardziej sztywnych językach.

Dlatego tutaj skupiamy się na wzorcach, które naprawdę warto rozumieć praktycznie.

## Kiedy myśleć o wzorcu?

Nie wtedy, gdy chcesz „napisać coś profesjonalnie”, tylko wtedy, gdy widzisz konkretny problem, np.:

- wiele wariantów zachowania,
- trudne tworzenie obiektów,
- zbyt dużo `if`-ów,
- potrzeba odseparowania odpowiedzialności,
- konieczność powiadamiania wielu elementów o zmianie,
- powtarzający się problem architektoniczny.

## Najważniejsza zasada

Najpierw prosty kod. Wzorzec dopiero wtedy, gdy rzeczywiście upraszcza rozwiązanie.

---

## 1. Strategy

### Kiedy używać?

Gdy masz kilka wariantów tego samego działania i chcesz móc je podmieniać bez rozbijania kodu przez duże `if`-y.

### Problem

```python
class ShippingCostCalculator:
    def calculate(self, method, price):
        if method == "standard":
            return 10
        if method == "express":
            return 20
        if method == "pickup":
            return 0
```

Im więcej metod dostawy, tym większy chaos.

### Lepszy kierunek

```python
class StandardShipping:
    def calculate(self, price):
        return 10


class ExpressShipping:
    def calculate(self, price):
        return 20


class PickupShipping:
    def calculate(self, price):
        return 0


class ShippingCostCalculator:
    def __init__(self, strategy):
        self.strategy = strategy

    def calculate(self, price):
        return self.strategy.calculate(price)
```

### Korzyść

- łatwo dodać nową strategię,
- mniej `if`-ów,
- czytelniejsze rozdzielenie odpowiedzialności.

---

## 2. Factory

### Kiedy używać?

Gdy tworzenie obiektu jest bardziej złożone albo zależy od warunków.

### Problem

```python
def create_notification(channel):
    if channel == "email":
        return EmailSender()
    if channel == "sms":
        return SmsSender()
```

To może być okej w małym kodzie, ale gdy tworzenie robi się bardziej skomplikowane, warto je wydzielić.

### Prosty wariant fabryki

```python
class NotificationFactory:
    def create(self, channel):
        if channel == "email":
            return EmailSender()
        if channel == "sms":
            return SmsSender()
        raise ValueError("Nieznany kanal")
```

### Korzyść

- logika tworzenia obiektów jest w jednym miejscu,
- kod używający obiektów nie musi znać szczegółów konstrukcji.

### Uwaga

W Pythonie często wystarczy zwykła funkcja fabrykująca zamiast rozbudowanej klasy fabryki.

---

## 3. Observer

### Kiedy używać?

Gdy zmiana w jednym obiekcie ma powiadomić wiele innych elementów.

Przykłady:

- system eventów,
- notyfikacje,
- reakcje na zmianę stanu,
- hooki i callbacki.

### Idea

Masz obiekt główny i listę obserwatorów.

```python
class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)
```

Obserwatorzy implementują metodę `update()`.

### Korzyść

- jeden element nie musi znać szczegółów wszystkich reakcji,
- łatwiej rozszerzać system o nowe reakcje.

### Ryzyko

- jeśli obserwatorów jest bardzo dużo, przepływ logiki może stać się trudny do śledzenia.

---

## 4. Adapter

### Kiedy używać?

Gdy chcesz użyć istniejącej klasy lub zewnętrznej biblioteki, ale jej interfejs nie pasuje do twojego kodu.

### Problem

Twój system oczekuje metody `send(message)`, ale biblioteka ma metodę `push(text)`.

### Rozwiązanie

```python
class ExternalNotifier:
    def push(self, text):
        print(f"Wysylka: {text}")


class NotifierAdapter:
    def __init__(self, external_notifier):
        self.external_notifier = external_notifier

    def send(self, message):
        self.external_notifier.push(message)
```

### Korzyść

- reszta systemu pracuje na jednym spójnym interfejsie,
- łatwiej wymieniać integracje.

---

## 5. Facade

### Kiedy używać?

Gdy kilka elementów systemu trzeba uruchomić w określonej kolejności i chcesz dać prostszy punkt wejścia.

### Problem

Aby wykonać operację, trzeba:

- pobrać dane,
- zwalidować je,
- zapisać,
- wysłać powiadomienie,
- zalogować wynik.

Kod kliencki robi się ciężki.

### Rozwiązanie

```python
class OrderFacade:
    def __init__(self, validator, repository, notifier):
        self.validator = validator
        self.repository = repository
        self.notifier = notifier

    def place_order(self, order):
        self.validator.validate(order)
        self.repository.save(order)
        self.notifier.send("Nowe zamowienie")
```

### Korzyść

- prostsze API,
- mniej wiedzy potrzebnej po stronie wywołującej,
- lepsza organizacja złożonego procesu.

---

## 6. Singleton

### O co chodzi?

Singleton to wzorzec zapewniający istnienie tylko jednej instancji danego obiektu.

### Dlaczego trzeba uważać?

W teorii bywa używany np. dla konfiguracji lub loggera. W praktyce często prowadzi do:

- ukrytych zależności,
- trudniejszych testów,
- globalnego stanu,
- kodu trudniejszego do przewidywania.

### Wniosek praktyczny

Znaj ten wzorzec, ale stosuj ostrożnie. Bardzo często lepiej użyć zwykłego obiektu przekazywanego jawnie.

---

## Python a wzorce projektowe

W Pythonie wiele klasycznych wzorców bywa lżejszych niż w innych językach.

Przykładowo:

- zamiast rozbudowanego interfejsu często wystarczy `Protocol` lub duck typing,
- zamiast skomplikowanej fabryki wystarczy funkcja,
- zamiast ciężkiej hierarchii klas lepiej użyć kompozycji.

Dlatego ważniejsze od pamiętania definicji wzorca jest rozumienie:

- jaki problem rozwiązuje,
- kiedy warto go użyć,
- kiedy już przesadzasz.

## Najczęstsze błędy

### 1. Używanie wzorca bez problemu

„Zrobię Factory, Strategy, Observer i Facade, bo tak będzie profesjonalnie”.

To droga do nadmiarowej architektury.

### 2. Za dużo klas dla prostego zadania

Jeśli prosta funkcja rozwiązuje problem czytelnie, to często wystarczy.

### 3. Dziedziczenie tam, gdzie wystarczy kompozycja

W Pythonie kompozycja zwykle daje większą elastyczność.

### 4. Ślepe kopiowanie wzorców z innych języków

Python ma swoją specyfikę. To, co jest konieczne w Javie, w Pythonie może być przesadą.

## Jak uczyć się wzorców dobrze?

Najlepiej tak:

1. poznaj problem,
2. zobacz prosty kod bez wzorca,
3. zauważ jego ograniczenia,
4. dopiero wtedy wprowadź wzorzec,
5. porównaj, czy rzeczywiście poprawił czytelność i elastyczność.

## Szybka ściąga

### Strategy

Różne warianty jednego zachowania.

### Factory

Oddzielenie logiki tworzenia obiektów.

### Observer

Powiadamianie wielu elementów o zmianie.

### Adapter

Dopasowanie niepasującego interfejsu.

### Facade

Uproszczony punkt wejścia do złożonego procesu.

### Singleton

Jedna instancja w całym systemie, ale zwykle trzeba uważać.

## Ćwiczenia

1. Przerób kalkulator kosztów wysyłki z `if`-ami na wzorzec Strategy.
2. Napisz prostą funkcję fabrykującą różne typy powiadomień.
3. Dodaj adapter dla zewnętrznej klasy, której interfejs nie pasuje do twojego systemu.
4. Zbuduj prosty `Subject` z listą obserwatorów i metodą `notify()`.
5. Stwórz `Facade` dla procesu składania zamówienia.
6. Znajdź w swoim kodzie miejsce, gdzie wzorzec byłby przesadą, i uzasadnij dlaczego.

## Najważniejsze do zapamiętania

- Wzorce projektowe to sprawdzone sposoby organizacji kodu, a nie obowiązkowe ozdobniki.
- Najważniejsze jest rozumienie problemu, nie pamięciowe definicje.
- W Pythonie wzorce zwykle wdraża się lżej niż w bardziej sztywnych językach.
- Strategy, Factory, Adapter i Facade są bardzo praktyczne na start.
- Zły wzorzec dodany bez potrzeby pogarsza kod zamiast go poprawiać.
