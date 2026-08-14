# Mocking w Pythonie — `unittest.mock`, patchowanie funkcji, klas i obiektów

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest mocking](#czym-jest-mocking)
3. [Po co używa się mocków](#po-co-używa-się-mocków)
4. [`unittest.mock`](#unittestmock)
5. [Czym jest `Mock`](#czym-jest-mock)
6. [Czym jest `MagicMock`](#czym-jest-magicmock)
7. [`patch`](#patch)
8. [Patchowanie funkcji](#patchowanie-funkcji)
9. [Patchowanie klas](#patchowanie-klas)
10. [Patchowanie obiektów](#patchowanie-obiektów)
11. [Patchowanie „we właściwym miejscu”](#patchowanie-we-właściwym-miejscu)
12. [Mocki a testy API](#mocki-a-testy-api)
13. [Sprawdzanie wywołań mocka](#sprawdzanie-wywołań-mocka)
14. [`return_value` i `side_effect`](#return_value-i-side_effect)
15. [Mockowanie wyjątków](#mockowanie-wyjątków)
16. [Typowe błędy początkujących](#typowe-błędy-początkujących)
17. [Praktyczne przykłady](#praktyczne-przykłady)
18. [Dobre praktyki](#dobre-praktyki)
19. [Podsumowanie](#podsumowanie)
20. [Mini ściąga](#mini-ściąga)
21. [Ćwiczenia](#ćwiczenia)
22. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Mocking to bardzo ważna część testowania.

Pozwala zastępować prawdziwe elementy programu sztucznymi obiektami testowymi.

To przydaje się wtedy, gdy nie chcesz podczas testu naprawdę:

- robić requestu HTTP,
- pisać do bazy,
- wysyłać maili,
- wywoływać zewnętrznych usług,
- używać kosztownych lub niestabilnych zależności.

---

## Czym jest mocking

Mocking to tworzenie zastępczego obiektu albo zastępczego zachowania na potrzeby testu.

Najprościej:

zamiast prawdziwego elementu używasz kontrolowanej wersji testowej.

---

## Po co używa się mocków

Po to, żeby test:

- był szybszy,
- był stabilniejszy,
- nie zależał od internetu lub API,
- nie wykonywał kosztownych akcji,
- testował właściwy fragment logiki, a nie wszystko naraz.

---

## `unittest.mock`

To standardowy moduł Pythona do mockowania.

Najczęściej importuje się:

```python
from unittest.mock import Mock, MagicMock, patch
```

---

## Czym jest `Mock`

`Mock` to prosty sztuczny obiekt, który możesz skonfigurować i sprawdzać.

Przykład:

```python
from unittest.mock import Mock

m = Mock()
m.return_value = 123
print(m())
```

---

## Czym jest `MagicMock`

`MagicMock` to rozszerzona wersja `Mock`, lepiej wspierająca magic methods.

W praktyce bardzo często używa się właśnie `MagicMock`, bo jest wygodniejszy.

---

## `patch`

`patch` pozwala tymczasowo podmienić funkcję, klasę albo obiekt.

To jeden z najważniejszych elementów mockowania.

Przykład idei:

```python
with patch("modul.funkcja") as mock_f:
    ...
```

---

## Patchowanie funkcji

Jeśli funkcja robi coś zewnętrznego, możesz ją podmienić.

Na przykład zamiast prawdziwego requestu HTTP podstawiasz mock.

---

## Patchowanie klas

Możesz podmienić klasę, żeby zamiast prawdziwego obiektu tworzyła mock.

To przydatne, gdy testowany kod tworzy instancje samodzielnie.

---

## Patchowanie obiektów

Możesz też patchować konkretne atrybuty obiektu.

Na przykład metodę klienta API albo atrybut konfiguracyjny.

---

## Patchowanie „we właściwym miejscu”

To jedna z najważniejszych zasad mockowania.

Patchujesz nie tam, gdzie funkcja „powstała”, tylko tam, skąd jest używana w testowanym module.

To bardzo częsta pułapka.

---

## Mocki a testy API

W testach API bardzo często mockuje się:

- requesty do zewnętrznych serwisów,
- klientów HTTP,
- warstwę dostępu do bazy,
- wysyłkę maili,
- kolejki zadań.

To pozwala testować logikę endpointu bez prawdziwego wyjścia na zewnątrz.

---

## Sprawdzanie wywołań mocka

Mocki potrafią pamiętać, jak zostały użyte.

Na przykład:

```python
mock.assert_called_once()
mock.assert_called_once_with(1, 2)
```

To bardzo ważne, bo testujesz nie tylko wynik, ale też interakcję.

---

## `return_value` i `side_effect`

### `return_value`

Ustawia zwracany wynik.

### `side_effect`

Pozwala:

- rzucić wyjątek,
- zwracać różne rzeczy,
- dodać własne zachowanie.

---

## Mockowanie wyjątków

Możesz wymusić błąd:

```python
mock.side_effect = ValueError("blad")
```

To przydatne przy testowaniu obsługi wyjątków.

---

## Typowe błędy początkujących

### 1. Patchowanie w złym miejscu

### 2. Mockowanie za dużo

### 3. Pisanie testów, które tylko sprawdzają mocki, a nie logikę

### 4. Nadużywanie mocków tam, gdzie prostszy fake albo fixture byłby lepszy

### 5. Brak zrozumienia, co dokładnie jest zależnością zewnętrzną

---

## Praktyczne przykłady

### Prosty mock

```python
from unittest.mock import Mock

m = Mock(return_value=10)
assert m() == 10
```

### Patchowanie funkcji

```python
from unittest.mock import patch

with patch("modul.pobierz_dane") as mock_pobierz:
    mock_pobierz.return_value = {"ok": True}
```

### Sprawdzenie wywołania

```python
mock_pobierz.assert_called_once()
```

### Mock wyjątku

```python
mock_pobierz.side_effect = ConnectionError("brak polaczenia")
```

---

## Dobre praktyki

### Mockuj tylko prawdziwe zależności zewnętrzne

### Nie mockuj własnej prostej logiki bez potrzeby

### Patchuj w miejscu użycia

### Testuj i wynik, i interakcję tam, gdzie to ważne

### Utrzymuj testy czytelne

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- mocking pozwala zastępować zależności kontrolowanymi obiektami testowymi,
- `Mock`, `MagicMock` i `patch` to podstawowe narzędzia,
- bardzo ważne jest patchowanie we właściwym miejscu,
- mocki są świetne do testów API i integracji z usługami zewnętrznymi.

---

## Mini ściąga

```python
from unittest.mock import Mock, MagicMock, patch
```

```python
m = Mock(return_value=10)
m.assert_called_once()
```

```python
with patch("modul.funkcja") as mock_f:
    ...
```

---

## Ćwiczenia

### Ćwiczenie 1

Utwórz `Mock`, który zwraca `123`.

### Ćwiczenie 2

Ustaw `side_effect` na wyjątek.

### Ćwiczenie 3

Sprawdź, czy mock został wywołany raz z konkretnymi argumentami.

---

## Przykładowe rozwiązania

### Ćwiczenie 1

```python
from unittest.mock import Mock

m = Mock(return_value=123)
assert m() == 123
```

### Ćwiczenie 2

```python
m.side_effect = ValueError("blad")
```

### Ćwiczenie 3

```python
m(1, 2)
m.assert_called_once_with(1, 2)
```
