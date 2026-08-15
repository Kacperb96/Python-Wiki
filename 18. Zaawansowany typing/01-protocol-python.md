# `Protocol` w Pythonie

## O co chodzi

`Protocol` pozwala opisywać typ przez **zachowanie**, a nie przez dziedziczenie.

To bardzo pythonowe podejście.

Zamiast mówić:

- ten obiekt musi dziedziczyć po konkretnej klasie,

możesz powiedzieć:

- ten obiekt ma mieć metodę `send()`,
- albo metodę `save()`,
- albo właściwość `name` i metodę `close()`.

To dobrze współgra z duck typingiem.

## Intuicja

W Pythonie od dawna istnieje myślenie w stylu:

- jeśli coś zachowuje się jak kaczka, to traktuj to jak kaczkę.

`Protocol` daje temu bardziej formalny opis na poziomie typów.

## Prosty przykład

```python
from typing import Protocol


class Sender(Protocol):
    def send(self, message: str) -> None:
        ...
```

Ten `Protocol` nie mówi nic o dziedziczeniu. On mówi tylko, że obiekt ma mieć metodę `send()` o odpowiedniej sygnaturze.

## Dwie klasy spełniające ten sam `Protocol`

```python
from typing import Protocol


class Sender(Protocol):
    def send(self, message: str) -> None:
        ...


class EmailSender:
    def send(self, message: str) -> None:
        print(f"Email: {message}")


class SmsSender:
    def send(self, message: str) -> None:
        print(f"SMS: {message}")
```

Obie klasy pasują do `Sender`, mimo że nie dziedziczą po żadnej wspólnej klasie bazowej.

## Serwis korzystający z `Protocol`

```python
from typing import Protocol


class Sender(Protocol):
    def send(self, message: str) -> None:
        ...


class NotificationService:
    def __init__(self, sender: Sender) -> None:
        self.sender = sender

    def notify(self, text: str) -> None:
        self.sender.send(text)
```

To jest bardzo praktyczny use case.

Serwis nie zależy od konkretnej klasy `EmailSender`, tylko od zachowania `send()`.

## Dlaczego to jest dobre

Dzięki temu:

- kod jest bardziej elastyczny,
- łatwiej testować zależności,
- lepiej widać kontrakt,
- nie trzeba sztucznie budować hierarchii dziedziczenia.

## `Protocol` vs zwykła klasa bazowa

### Klasa bazowa

Narzucone dziedziczenie.

### `Protocol`

Liczy się zgodność zachowania.

To szczególnie wygodne w Pythonie, gdzie wiele obiektów pasuje do danego interfejsu naturalnie, bez potrzeby wspólnego drzewa klas.

## `Protocol` a duck typing

To bardzo ważne połączenie.

Duck typing istniał w Pythonie długo przed `Protocol`.

`Protocol` nie zastępuje duck typing-u w runtime. On raczej:

- dokumentuje oczekiwane zachowanie,
- pozwala checkerom typów lepiej rozumieć kod,
- poprawia czytelność kontraktów.

## Kiedy `Protocol` ma sens

Szczególnie gdy:

- serwis przyjmuje zależność z metodami,
- chcesz opisać callback-like obiekt,
- budujesz architekturę na kontraktach zamiast konkretnych klas,
- chcesz czytelnego, lekkiego interfejsu bez wymuszania dziedziczenia.

## Kiedy może nie być potrzebny

Jeśli masz bardzo prosty kod i wszystko dzieje się lokalnie w jednym pliku, `Protocol` może być przesadą.

Jak zwykle: używaj tam, gdzie daje realną wartość.

## `Protocol` a testy

To ogromnie praktyczny punkt.

Jeśli serwis przyjmuje `Sender`, możesz bardzo łatwo podstawić atrapę.

```python
class FakeSender:
    def __init__(self) -> None:
        self.messages: list[str] = []

    def send(self, message: str) -> None:
        self.messages.append(message)
```

Taki fake też spełnia kontrakt `Sender`.

## Typowe błędy początkujących

- mylenie `Protocol` z klasą bazową,
- tworzenie `Protocol` dla wszystkiego,
- zbyt ciężkie interfejsy z wieloma metodami,
- brak refleksji, czy zwykła adnotacja konkretnej klasy już nie wystarcza,
- myślenie, że `Protocol` zmienia runtime behavior sam z siebie.

## Mini scenariusz praktyczny

Masz `UserRepository`, `EmailSender`, `Logger`, `PaymentGateway`.

Zamiast zależeć od konkretnych implementacji, możesz opisać ich zachowanie przez `Protocol` i dzięki temu:

- łatwiej testować,
- łatwiej podmieniać implementacje,
- łatwiej zrozumieć kontrakt zależności.

## Szybka ściąga

- `Protocol` opisuje zachowanie,
- nie wymaga wspólnego dziedziczenia,
- dobrze współgra z duck typingiem,
- jest bardzo praktyczny przy zależnościach i interfejsach.

## Ćwiczenia

1. Zdefiniuj `Protocol` z metodą `save()`.
2. Napisz dwie klasy spełniające go bez dziedziczenia.
3. Zbuduj serwis przyjmujący zależność opisaną przez `Protocol`.
4. Napisz fake do testów zgodny z tym kontraktem.
5. Porównaj `Protocol` i klasę bazową dla prostego przypadku.

## Najważniejsze do zapamiętania

- `Protocol` opisuje typ przez zachowanie, a nie przez dziedziczenie.
- To jedno z najbardziej praktycznych narzędzi zaawansowanego typingu w Pythonie.
- Świetnie pasuje do zależności, serwisów i testów.
- Nie trzeba używać go wszędzie, ale w większym kodzie daje dużą wartość.
- To formalizacja pythonowego podejścia duck typing.
