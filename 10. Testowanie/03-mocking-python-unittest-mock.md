# Mocking w Pythonie — `unittest.mock`

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest mocking](#czym-jest-mocking)
3. [Po co używa się mocków](#po-co-używa-się-mocków)
4. [`Mock` i `MagicMock`](#mock-i-magicmock)
5. [`return_value`](#return_value)
6. [`side_effect`](#side_effect)
7. [`patch`](#patch)
8. [Patchowanie funkcji](#patchowanie-funkcji)
9. [Patchowanie klas](#patchowanie-klas)
10. [Patchowanie obiektów](#patchowanie-obiektów)
11. [Patchowanie we właściwym miejscu](#patchowanie-we-właściwym-miejscu)
12. [Sprawdzanie wywołań mocka](#sprawdzanie-wywołań-mocka)
13. [Mocki a testy integracyjne](#mocki-a-testy-integracyjne)
14. [Typowe błędy początkujących](#typowe-błędy-początkujących)
15. [Praktyczna ściąga](#praktyczna-ściąga)
16. [Ćwiczenia](#ćwiczenia)
17. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

Mocking to bardzo ważna część testowania.

Pomaga wtedy, gdy testowany kod korzysta z czegoś zewnętrznego, czego nie chcesz naprawdę uruchamiać podczas testu.

Przykłady:

- request HTTP,
- baza danych,
- wysyłka maila,
- zapis do zewnętrznego systemu,
- odczyt aktualnego czasu,
- losowość,
- kosztowna albo niestabilna zależność.

---

## Czym jest mocking

Mocking to zastępowanie prawdziwego obiektu albo funkcji kontrolowaną wersją testową.

Najprościej:

zamiast uruchamiać prawdziwe działanie, podstawiasz obiekt, nad którym masz pełną kontrolę.

Dzięki temu możesz:

- ustawić, co ma zwrócić,
- sprawdzić, czy został wywołany,
- zasymulować wyjątek,
- odizolować logikę od świata zewnętrznego.

---

## Po co używa się mocków

Po to, żeby test:

- był szybszy,
- był stabilniejszy,
- nie wymagał internetu ani bazy,
- nie wykonywał kosztownych działań,
- skupiał się na logice, którą naprawdę chcesz sprawdzić.

To bardzo ważne przy testach jednostkowych.

---

## `Mock` i `MagicMock`

Najczęściej importujesz:

```python
from unittest.mock import Mock, MagicMock, patch
```

### `Mock`

Prosty obiekt testowy.

```python
from unittest.mock import Mock

m = Mock()
m.return_value = 123

print(m())
```

Przykładowy output:

```text
123
```

### `MagicMock`

To wygodniejsza wersja, lepiej wspierająca magic methods.

W praktyce często właśnie jej używa się najczęściej.

---

## `return_value`

`return_value` ustawia wartość zwracaną przez mock.

```python
from unittest.mock import Mock

api = Mock()
api.get_user.return_value = {"name": "Ania"}

wynik = api.get_user(1)
print(wynik)
```

Przykładowy output:

```text
{'name': 'Ania'}
```

To przydatne, gdy chcesz zasymulować odpowiedź zależności.

---

## `side_effect`

`side_effect` pozwala:

- rzucić wyjątek,
- zwrócić kolejne wartości,
- wykonać niestandardową logikę.

Przykład z wyjątkiem:

```python
from unittest.mock import Mock

api = Mock()
api.fetch.side_effect = TimeoutError("Za dlugo")
```

Test:

```python
import pytest


def test_fetch_timeout():
    with pytest.raises(TimeoutError):
        api.fetch()
```

---

## `patch`

`patch` tymczasowo podmienia obiekt w czasie testu.

To jeden z najważniejszych mechanizmów mockowania.

Przykład ogólnej idei:

```python
with patch("modul.funkcja") as mock_f:
    ...
```

Po wyjściu z bloku podmiana znika.

---

## Patchowanie funkcji

Załóżmy taki kod:

```python
# notifications.py

def send_email(to: str, subject: str) -> bool:
    return True
```

```python
# service.py
from notifications import send_email


def register_user(email: str) -> str:
    send_email(email, "Witamy")
    return "ok"
```

Test:

```python
from unittest.mock import patch
from service import register_user


def test_register_user_wysyla_maila():
    with patch("service.send_email") as mock_send:
        wynik = register_user("a@example.com")

        assert wynik == "ok"
        mock_send.assert_called_once_with("a@example.com", "Witamy")
```

Tu nie wysyłasz prawdziwego maila.

Sprawdzasz tylko, czy logika próbowała go wysłać.

---

## Patchowanie klas

Załóżmy taki kod:

```python
class EmailClient:
    def send(self, to: str, subject: str) -> bool:
        return True


def notify_user(email: str) -> bool:
    client = EmailClient()
    return client.send(email, "Hello")
```

Test:

```python
from unittest.mock import patch


def test_notify_user():
    with patch("service.EmailClient") as mock_client_cls:
        mock_client = mock_client_cls.return_value
        mock_client.send.return_value = True

        wynik = notify_user("a@example.com")

        assert wynik is True
        mock_client.send.assert_called_once_with("a@example.com", "Hello")
```

---

## Patchowanie obiektów

Czasem nie chcesz podmieniać całej klasy, tylko konkretny obiekt albo jego metodę.

Przykład:

```python
from unittest.mock import Mock

repo = Mock()
repo.get_user.return_value = {"id": 1}

assert repo.get_user(1) == {"id": 1}
```

To często wystarcza w prostych testach serwisów.

---

## Patchowanie we właściwym miejscu

To jedna z najważniejszych zasad całego mockowania.

Patchujesz nie tam, gdzie funkcja została zdefiniowana, tylko tam, skąd jest używana.

Jeśli `service.py` zrobił:

```python
from notifications import send_email
```

To w teście patchujesz:

```python
patch("service.send_email")
```

A nie:

```python
patch("notifications.send_email")
```

w tym konkretnym scenariuszu.

To bardzo częsta pułapka początkujących.

---

## Sprawdzanie wywołań mocka

Najczęstsze metody:

```python
mock.called
mock.assert_called()
mock.assert_called_once()
mock.assert_called_once_with(...)
mock.assert_not_called()
```

Przykład:

```python
from unittest.mock import Mock

m = Mock()
m("abc")

m.assert_called_once_with("abc")
```

Dzięki temu testujesz nie tylko wynik, ale też interakcję z zależnością.

---

## Mocki a testy integracyjne

Bardzo ważne:

jeśli mockujesz wszystko, to przestajesz testować integrację.

Dlatego:

- w testach jednostkowych mocki są bardzo częste,
- w testach integracyjnych zwykle chcesz mniej mocków i więcej realnej współpracy elementów.

Mocki nie są celem samym w sobie.

One mają pomóc izolować to, co trzeba izolować.

---

## Typowe błędy początkujących

- patchowanie nie tego miejsca, co trzeba,
- mockowanie wszystkiego bez zastanowienia,
- testowanie szczegółów implementacji zamiast zachowania,
- brak sprawdzenia argumentów wywołania,
- zbyt rozbudowane testy z wieloma mockami naraz,
- używanie mocka tam, gdzie prosty fake albo fixture byłby czytelniejszy.

---

## Praktyczna ściąga

### Prosty `Mock`

```python
m = Mock()
m.return_value = 10
assert m() == 10
```

### Symulacja wyjątku

```python
m.side_effect = ValueError("blad")
```

### Patch funkcji

```python
with patch("service.send_email") as mock_send:
    ...
```

### Sprawdzenie wywołania

```python
mock_send.assert_called_once_with("a@example.com", "Witamy")
```

---

## Ćwiczenia

1. Zbuduj prosty `Mock`, który zwraca liczbę `5`.
2. Ustaw `side_effect`, żeby mock rzucał `ValueError`.
3. Napisz funkcję, która wywołuje klienta API, i zamockuj tę zależność w teście.
4. Sprawdź, czy mock został wywołany raz i z poprawnymi argumentami.
5. Napisz przykład patchowania klasy tworzonej wewnątrz funkcji.
6. Celowo patchuj złe miejsce i zobacz, co się stanie.
7. Popraw test tak, by patchował właściwy symbol.
8. Zastanów się, czy w Twoim przykładzie to nadal test jednostkowy, czy już nie.

---

## Najważniejsze do zapamiętania

- Mock pozwala zastąpić prawdziwą zależność kontrolowaną wersją testową.
- `return_value` ustawia wynik mocka.
- `side_effect` pozwala symulować wyjątki albo bardziej złożone zachowanie.
- `patch` działa tymczasowo w czasie testu.
- Patchujesz tam, skąd obiekt jest używany, a nie tylko tam, gdzie został zdefiniowany.
- Mockuj tyle, ile trzeba, ale nie więcej.
