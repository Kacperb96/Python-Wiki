# Zaawansowane użycie `pytest`

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co wchodzić głębiej w `pytest`](#po-co-wchodzić-głębiej-w-pytest)
3. [Fixtures](#fixtures)
4. [Najprostsza fixture](#najprostsza-fixture)
5. [Fixture z setupem i cleanupem](#fixture-z-setupem-i-cleanupem)
6. [Zakres fixture](#zakres-fixture)
7. [Fixtures zależne od innych fixtures](#fixtures-zależne-od-innych-fixtures)
8. [Parametryzacja testów](#parametryzacja-testów)
9. [Przykład `@pytest.mark.parametrize`](#przykład-pytestmarkparametrize)
10. [`conftest.py`](#conftestpy)
11. [Po co istnieje `conftest.py`](#po-co-istnieje-conftestpy)
12. [Znaczniki `pytest.mark`](#znaczniki-pytestmark)
13. [Testowanie async](#testowanie-async)
14. [`pytest-asyncio`](#pytest-asyncio)
15. [Jak czytać output bardziej złożonych testów](#jak-czytać-output-bardziej-złożonych-testów)
16. [Typowe błędy początkujących](#typowe-błędy-początkujących)
17. [Praktyczna ściąga](#praktyczna-ściąga)
18. [Ćwiczenia](#ćwiczenia)
19. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

Podstawowy `pytest` jest bardzo prosty.

Ale prawdziwa wygoda zaczyna się wtedy, gdy poznasz:

- fixture'y,
- parametryzację,
- `conftest.py`,
- znaczniki,
- testowanie kodu asynchronicznego.

To właśnie te rzeczy sprawiają, że testy zaczynają być wygodne także w większym projekcie.

---

## Po co wchodzić głębiej w `pytest`

W małym przykładzie możesz wszystko wpisać ręcznie w jednym pliku.

Ale w prawdziwym projekcie szybko pojawia się potrzeba:

- współdzielonego setupu,
- danych testowych w wielu testach,
- wygodnego czyszczenia zasobów,
- testowania wielu przypadków jedną funkcją,
- oddzielenia testów szybkich od wolniejszych,
- testowania `async def`.

---

## Fixtures

Fixture to funkcja przygotowująca coś dla testu.

Może to być:

- obiekt,
- konfiguracja,
- dane wejściowe,
- plik tymczasowy,
- klient testowy,
- połączenie do bazy.

Najprostsza składnia:

```python
import pytest


@pytest.fixture
def liczba():
    return 10
```

A użycie:

```python
def test_liczba(liczba):
    assert liczba == 10
```

`pytest` sam podaje fixture do argumentu testu.

---

## Najprostsza fixture

Pełny przykład:

```python
import pytest


@pytest.fixture
def user_data():
    return {"name": "Ania", "age": 25}


def test_user_name(user_data):
    assert user_data["name"] == "Ania"


def test_user_age(user_data):
    assert user_data["age"] == 25
```

Korzyść:

- nie powtarzasz danych ręcznie,
- oba testy korzystają z tego samego setupu.

---

## Fixture z setupem i cleanupem

Jeśli coś trzeba posprzątać po teście, używasz `yield`.

```python
import pytest


@pytest.fixture
def zasob():
    print("setup")
    yield [1, 2, 3]
    print("cleanup")


def test_zasob(zasob):
    assert len(zasob) == 3
```

Przykładowy output z `pytest -s`:

```text
setup
cleanup
1 passed in 0.02s
```

To bardzo ważny wzorzec przy plikach, połączeniach i innych zasobach.

---

## Zakres fixture

Fixture może mieć różny zakres życia.

Najczęstsze wartości `scope`:

- `function`
- `class`
- `module`
- `session`

Przykład:

```python
@pytest.fixture(scope="module")
def dane():
    return [1, 2, 3]
```

To znaczy, że fixture zostanie utworzona raz dla całego modułu testowego.

Im szerszy zakres, tym mniej powtórzeń setupu, ale też większe ryzyko niechcianego współdzielenia stanu.

---

## Fixtures zależne od innych fixtures

Jedna fixture może korzystać z innej.

```python
import pytest


@pytest.fixture
def user():
    return {"name": "Ania", "age": 25}


@pytest.fixture
def user_name(user):
    return user["name"]


def test_user_name(user_name):
    assert user_name == "Ania"
```

To pozwala budować bardziej złożone przygotowanie danych krok po kroku.

---

## Parametryzacja testów

Parametryzacja pozwala uruchomić ten sam test dla wielu zestawów danych.

Bez niej często kopiowałbyś bardzo podobne testy.

---

## Przykład `@pytest.mark.parametrize`

```python
import pytest


def jest_parzysta(n: int) -> bool:
    return n % 2 == 0


@pytest.mark.parametrize(
    "wartosc, oczekiwany",
    [
        (2, True),
        (3, False),
        (0, True),
        (-4, True),
    ],
)
def test_jest_parzysta(wartosc, oczekiwany):
    assert jest_parzysta(wartosc) is oczekiwany
```

Przykładowy output:

```text
....                                                                     [100%]
4 passed in 0.02s
```

Każdy zestaw danych to osobne wykonanie tego samego testu.

Jeśli jeden przypadek padnie, `pytest` pokaże dokładnie który.

---

## `conftest.py`

`conftest.py` to specjalny plik, w którym możesz trzymać wspólne fixture'y i konfigurację dla testów.

Przykład struktury:

```text
tests/
    conftest.py
    test_users.py
    test_orders.py
```

Plik `conftest.py`:

```python
import pytest


@pytest.fixture
def sample_user():
    return {"name": "Jan", "active": True}
```

Test:

```python
def test_sample_user(sample_user):
    assert sample_user["active"] is True
```

Nie musisz nic importować ręcznie z `conftest.py`.

---

## Po co istnieje `conftest.py`

Bo w większym projekcie szybko pojawiają się rzeczy wspólne dla wielu testów.

Na przykład:

- przykładowy użytkownik,
- klient API,
- konfiguracja aplikacji,
- obiekt repozytorium,
- pomocnicze dane wejściowe.

`conftest.py` pozwala to uporządkować.

---

## Znaczniki `pytest.mark`

Markery pozwalają oznaczać testy.

Na przykład:

```python
import pytest


@pytest.mark.slow
def test_duzy_proces():
    assert True
```

Potem możesz uruchomić tylko wybrane grupy testów, zależnie od konfiguracji projektu.

To bardzo wygodne przy większych zestawach testów.

---

## Testowanie async

Jeśli testujesz funkcję `async def`, zwykły test nie wystarczy.

Przykład funkcji:

```python
async def pobierz_wiadomosc() -> str:
    return "hello"
```

Do testowania kodu async zwykle używa się `pytest-asyncio`.

---

## `pytest-asyncio`

Przykład:

```python
import pytest


async def pobierz_wiadomosc() -> str:
    return "hello"


@pytest.mark.asyncio
async def test_pobierz_wiadomosc():
    wynik = await pobierz_wiadomosc()
    assert wynik == "hello"
```

Tu sam test też jest `async def`.

Bez odpowiedniej obsługi async taki test nie zadziała poprawnie.

---

## Jak czytać output bardziej złożonych testów

Przy parametryzacji możesz zobaczyć coś takiego:

```text
============================= test session starts =============================
collected 5 items

test_numbers.py ...F.                                                  [100%]

================================== FAILURES ==================================
_______________________ test_jest_parzysta[3-True] ________________________

wartosc = 3, oczekiwany = True

    def test_jest_parzysta(wartosc, oczekiwany):
>       assert jest_parzysta(wartosc) is oczekiwany
E       assert False is True

========================= 1 failed, 4 passed in 0.03s =========================
```

Bardzo ważny fragment to:

```text
test_jest_parzysta[3-True]
```

To oznacza dokładnie, który zestaw danych spowodował błąd.

---

## Typowe błędy początkujących

- kopiowanie kilku podobnych testów zamiast użycia parametryzacji,
- zbyt szerokie fixture'y współdzielące stan między testami,
- niepotrzebne komplikowanie `conftest.py`,
- traktowanie fixture jako magazynu wszystkiego,
- brak cleanupu zasobów,
- próba testowania `async def` bez odpowiedniego narzędzia,
- mylenie wygody z nadmierną magią.

---

## Praktyczna ściąga

### Prosta fixture

```python
@pytest.fixture
def user():
    return {"name": "Ania"}
```

### Fixture z cleanupem

```python
@pytest.fixture
def zasob():
    yield "dane"
```

### Parametryzacja

```python
@pytest.mark.parametrize("x, y", [(1, 2), (2, 4)])
def test_cos(x, y):
    ...
```

### Async test

```python
@pytest.mark.asyncio
async def test_async():
    ...
```

---

## Ćwiczenia

1. Napisz fixture zwracającą przykładowego użytkownika.
2. Użyj jednej fixture w dwóch różnych testach.
3. Napisz fixture z `yield`, która wypisuje `setup` i `cleanup`.
4. Zparametryzuj test funkcji `czy_pelnoletni()`.
5. Przenieś wspólną fixture do `conftest.py`.
6. Dodaj marker `slow` do przykładowego testu.
7. Napisz prosty test async z `pytest.mark.asyncio`.
8. Celowo zepsuj jeden przypadek parametryzacji i przeanalizuj raport błędu.

---

## Najważniejsze do zapamiętania

- Fixture przygotowuje dane albo zasób dla testu.
- `yield` w fixture pomaga zrobić cleanup.
- Parametryzacja pozwala testować wiele przypadków jednym testem.
- `conftest.py` służy do wspólnych fixture i konfiguracji.
- Szerszy `scope` daje mniej setupu, ale większe ryzyko współdzielenia stanu.
- Kod async zwykle wymaga odpowiedniego wsparcia, np. `pytest-asyncio`.
