# Zaawansowane użycie `pytest` — fixtures, parametryzacja, `conftest`, async

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Dlaczego warto znać bardziej zaawansowany `pytest`](#dlaczego-warto-znać-bardziej-zaawansowany-pytest)
3. [Fixtures](#fixtures)
4. [Najprostsza fixture](#najprostsza-fixture)
5. [Po co używać fixture’ów](#po-co-używać-fixtureów)
6. [Zakres fixture](#zakres-fixture)
7. [Fixtures zależne od innych fixtures](#fixtures-zależne-od-innych-fixtures)
8. [Yield fixtures](#yield-fixtures)
9. [Parametryzacja testów](#parametryzacja-testów)
10. [`@pytest.mark.parametrize`](#pytestmarkparametrize)
11. [`conftest.py`](#conftestpy)
12. [Po co istnieje `conftest.py`](#po-co-istnieje-conftestpy)
13. [Testowanie async](#testowanie-async)
14. [`pytest-asyncio`](#pytest-asyncio)
15. [Async fixtures](#async-fixtures)
16. [Typowe błędy początkujących](#typowe-błędy-początkujących)
17. [Praktyczne przykłady](#praktyczne-przykłady)
18. [Dobre praktyki](#dobre-praktyki)
19. [Podsumowanie](#podsumowanie)
20. [Mini ściąga](#mini-ściąga)
21. [Ćwiczenia](#ćwiczenia)
22. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Podstawowy `pytest` jest bardzo prosty.

Ale prawdziwa siła tego narzędzia zaczyna się wtedy, gdy poznasz:

- fixtures,
- parametryzację,
- `conftest.py`,
- testowanie kodu asynchronicznego.

To właśnie te elementy bardzo często odróżniają „proste testy” od wygodnego, skalowalnego systemu testowania.

---

## Dlaczego warto znać bardziej zaawansowany `pytest`

Bo w większym projekcie szybko pojawiają się potrzeby:

- współdzielone dane testowe,
- setup i cleanup,
- testowanie wielu przypadków tym samym kodem,
- wspólne narzędzia dla całego pakietu testów,
- testowanie funkcji `async`.

---

## Fixtures

Fixture to funkcja, która przygotowuje coś dla testu.

Może to być:

- obiekt,
- dane,
- klient API,
- połączenie do bazy,
- tymczasowy plik,
- środowisko testowe.

Fixture tworzy się dekoratorem:

```python
@pytest.fixture
```

---

## Najprostsza fixture

```python
import pytest

@pytest.fixture
def liczba():
    return 10

def test_liczba(liczba):
    assert liczba == 10
```

Tu `pytest` sam wstrzykuje fixture do testu.

---

## Po co używać fixture’ów

Po to, żeby:

- nie powtarzać setupu,
- lepiej organizować testy,
- budować zależności między elementami testowymi,
- mieć czytelniejszy kod testów.

---

## Zakres fixture

Fixture może mieć różny zakres, np.:

- na funkcję,
- na klasę,
- na moduł,
- na sesję.

Przykład:

```python
@pytest.fixture(scope="module")
def dane():
    return [1, 2, 3]
```

To oznacza, że fixture będzie tworzona na poziomie modułu.

---

## Fixtures zależne od innych fixtures

Fixture może korzystać z innej fixture.

```python
@pytest.fixture
def user():
    return {"name": "Ania"}

@pytest.fixture
def user_id(user):
    return user["name"]
```

To bardzo wygodny mechanizm.

---

## Yield fixtures

Jeśli trzeba coś posprzątać po teście, można użyć `yield`.

```python
@pytest.fixture
def zasob():
    print("setup")
    yield "dane"
    print("cleanup")
```

To bardzo ważny wzorzec przy zasobach i cleanupie.

---

## Parametryzacja testów

Parametryzacja pozwala uruchamiać ten sam test dla wielu zestawów danych.

To świetne narzędzie do unikania duplikacji.

---

## `@pytest.mark.parametrize`

Przykład:

```python
import pytest

@pytest.mark.parametrize("a,b,wynik", [
    (1, 2, 3),
    (2, 3, 5),
    (10, 5, 15),
])
def test_dodaj(a, b, wynik):
    assert a + b == wynik
```

To jeden z najczęściej używanych mechanizmów w `pytest`.

---

## `conftest.py`

`conftest.py` to specjalny plik, w którym można umieszczać:

- wspólne fixtures,
- konfigurację testów,
- pomocnicze ustawienia dla `pytest`.

Dzięki temu nie trzeba kopiować fixture’ów do wielu plików testowych.

---

## Po co istnieje `conftest.py`

Po to, by mieć wspólne miejsce dla elementów używanych przez wiele testów.

To bardzo ważne w większych projektach.

---

## Testowanie async

Jeśli testujesz funkcje `async def`, zwykły test nie wystarczy.

Potrzebujesz wsparcia dla asynchronicznego event loopa.

---

## `pytest-asyncio`

Do testowania async często używa się pluginu `pytest-asyncio`.

Przykład:

```python
import pytest

@pytest.mark.asyncio
async def test_async():
    assert 1 + 1 == 2
```

To pozwala uruchamiać testy asynchroniczne.

---

## Async fixtures

Przy bardziej zaawansowanych testach możesz mieć też fixture asynchroniczne.

To już trochę wyższy poziom, ale ważne, jeśli testujesz async API lub async aplikacje.

---

## Typowe błędy początkujących

### 1. Duplikowanie setupu zamiast użycia fixture

### 2. Pisanie wielu bardzo podobnych testów zamiast parametryzacji

### 3. Trzymanie wszystkiego w jednym pliku zamiast użycia `conftest.py`

### 4. Próba uruchamiania `async def` bez wsparcia async testów

### 5. Niezrozumienie zakresu fixture

---

## Praktyczne przykłady

### Prosta fixture

```python
import pytest

@pytest.fixture
def user():
    return {"name": "Ania"}

def test_user(user):
    assert user["name"] == "Ania"
```

### Parametryzacja

```python
import pytest

@pytest.mark.parametrize("x,wynik", [
    (2, 4),
    (3, 9),
    (4, 16),
])
def test_kwadrat(x, wynik):
    assert x * x == wynik
```

### Async test

```python
import pytest

@pytest.mark.asyncio
async def test_async_add():
    assert 1 + 1 == 2
```

---

## Dobre praktyki

### Używaj fixture do setupu i współdzielonych danych

### Używaj parametryzacji tam, gdzie test różni się tylko danymi

### Trzymaj współdzielone fixtures w `conftest.py`

### Rozdzielaj testy async od zwykłych logicznie i czytelnie

### Nie przesadzaj z bardzo złożonymi fixture dependency graph

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- fixtures upraszczają setup testów,
- `parametrize` pozwala uruchamiać jeden test dla wielu przypadków,
- `conftest.py` przechowuje wspólne elementy dla testów,
- `pytest-asyncio` pomaga testować kod async.

---

## Mini ściąga

```python
@pytest.fixture
def dane():
    return ...
```

```python
@pytest.mark.parametrize("x,y", [...])
```

```python
@pytest.mark.asyncio
async def test_x():
    ...
```

---

## Ćwiczenia

### Ćwiczenie 1

Napisz fixture zwracającą listę liczb.

### Ćwiczenie 2

Napisz test parametryzowany dla funkcji mnożenia.

### Ćwiczenie 3

Przygotuj prosty test async.

---

## Przykładowe rozwiązania

### Ćwiczenie 1

```python
import pytest

@pytest.fixture
def liczby():
    return [1, 2, 3]
```

### Ćwiczenie 2

```python
import pytest

@pytest.mark.parametrize("a,b,wynik", [
    (2, 3, 6),
    (4, 5, 20),
])
def test_mnoz(a, b, wynik):
    assert a * b == wynik
```

### Ćwiczenie 3

```python
import pytest

@pytest.mark.asyncio
async def test_async_simple():
    assert True
```
