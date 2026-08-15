# Testowanie w Pythonie — podstawy `pytest`

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co w ogóle pisać testy](#po-co-w-ogóle-pisać-testy)
3. [Czym jest test](#czym-jest-test)
4. [Testy jednostkowe](#testy-jednostkowe)
5. [Testy integracyjne](#testy-integracyjne)
6. [Różnica między testem jednostkowym a integracyjnym](#różnica-między-testem-jednostkowym-a-integracyjnym)
7. [Dlaczego `pytest` jest tak popularny](#dlaczego-pytest-jest-tak-popularny)
8. [Najprostszy test](#najprostszy-test)
9. [Struktura pliku testowego](#struktura-pliku-testowego)
10. [Asercje w `pytest`](#asercje-w-pytest)
11. [Testowanie wyjątków](#testowanie-wyjątków)
12. [Uruchamianie testów](#uruchamianie-testów)
13. [Przykładowy output `pytest`](#przykładowy-output-pytest)
14. [Jak czytać błąd testu](#jak-czytać-błąd-testu)
15. [Organizacja katalogu `tests`](#organizacja-katalogu-tests)
16. [Co powinien testować dobry test jednostkowy](#co-powinien-testować-dobry-test-jednostkowy)
17. [Co powinien testować dobry test integracyjny](#co-powinien-testować-dobry-test-integracyjny)
18. [Typowe błędy początkujących](#typowe-błędy-początkujących)
19. [Praktyczna ściąga](#praktyczna-ściąga)
20. [Ćwiczenia](#ćwiczenia)
21. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

Testowanie to sposób sprawdzania, czy kod zachowuje się zgodnie z oczekiwaniem.

Nie chodzi tylko o to, żeby raz ręcznie uruchomić program i zobaczyć, że działa.

Chodzi o to, żeby mieć powtarzalny sposób sprawdzania:

- poprawnych przypadków,
- błędnych przypadków,
- edge case'ów,
- zachowania po kolejnych zmianach w kodzie.

W Pythonie najpopularniejszym narzędziem do tego jest `pytest`.

---

## Po co w ogóle pisać testy

Testy pomagają:

- szybciej zauważyć błąd,
- bezpiecznie refaktoryzować,
- rozwijać projekt bez psucia starej funkcjonalności,
- lepiej rozumieć wymagane zachowanie kodu,
- dokumentować, jak funkcja powinna działać.

Bez testów bardzo łatwo wpaść w schemat:

1. poprawiasz jeden błąd,
2. przypadkiem psujesz coś innego,
3. orientujesz się dopiero później.

---

## Czym jest test

Test to fragment kodu, który sprawdza inny fragment kodu.

Przykład:

```python
def dodaj(a, b):
    return a + b


def test_dodaj():
    assert dodaj(2, 3) == 5
```

Tutaj test mówi:

- wywołaj `dodaj(2, 3)`,
- sprawdź, czy wynik to `5`.

---

## Testy jednostkowe

Test jednostkowy sprawdza mały fragment programu.

Najczęściej:

- jedną funkcję,
- jedną metodę,
- jedną małą klasę,
- jedną zasadę logiki biznesowej.

Przykład:

```python
def czy_pelnoletni(wiek: int) -> bool:
    return wiek >= 18


def test_czy_pelnoletni():
    assert czy_pelnoletni(20) is True
    assert czy_pelnoletni(15) is False
```

To jest mały, szybki test konkretnej reguły.

---

## Testy integracyjne

Test integracyjny sprawdza współpracę kilku elementów.

Przykłady:

- zapis do pliku i odczyt z pliku,
- endpoint API i warstwa logiki,
- serwis i baza danych,
- parser i walidator działające razem.

Przykład prosty:

```python
import json
from pathlib import Path


def zapisz_dane(sciezka: Path, dane: dict) -> None:
    sciezka.write_text(json.dumps(dane), encoding="utf-8")


def wczytaj_dane(sciezka: Path) -> dict:
    return json.loads(sciezka.read_text(encoding="utf-8"))


def test_zapis_i_odczyt(tmp_path):
    plik = tmp_path / "dane.json"
    dane = {"name": "Ania"}

    zapisz_dane(plik, dane)

    wynik = wczytaj_dane(plik)
    assert wynik == dane
```

Tu test sprawdza więcej niż jedną funkcję i prawdziwą współpracę elementów.

---

## Różnica między testem jednostkowym a integracyjnym

### Test jednostkowy

- mały zakres,
- szybki,
- zwykle izolowany,
- łatwiej wskazać źródło błędu.

### Test integracyjny

- większy zakres,
- sprawdza współpracę części systemu,
- zwykle wolniejszy,
- lepiej pokazuje zachowanie całości.

Dobrze mieć oba typy testów.

---

## Dlaczego `pytest` jest tak popularny

`pytest` jest bardzo ceniony, bo:

- ma prostą składnię,
- używa zwykłego `assert`,
- daje czytelne raporty błędów,
- ma fixture'y,
- ma parametryzację,
- ma duży ekosystem pluginów.

To narzędzie jest jednocześnie wygodne dla początkujących i bardzo mocne w większych projektach.

---

## Najprostszy test

Plik `math_utils.py`:

```python
def dodaj(a: int, b: int) -> int:
    return a + b
```

Plik `test_math_utils.py`:

```python
from math_utils import dodaj


def test_dodaj_dwie_liczby():
    assert dodaj(2, 3) == 5
```

To już jest pełnoprawny test.

---

## Struktura pliku testowego

Typowa konwencja:

- pliki testowe zaczynają się od `test_` albo kończą na `_test.py`,
- funkcje testowe zaczynają się od `test_`.

Przykład:

```python
from math_utils import dodaj, odejmij


def test_dodaj_dwie_liczby():
    assert dodaj(2, 3) == 5


def test_odejmij_dwie_liczby():
    assert odejmij(10, 4) == 6
```

Dzięki temu `pytest` potrafi automatycznie odnaleźć testy.

---

## Asercje w `pytest`

Najczęściej używasz po prostu `assert`.

Przykłady:

```python
assert 2 + 2 == 4
assert "Py" in "Python"
assert [1, 2] == [1, 2]
assert wynik is None
assert czy_aktywne is True
```

Ogromna zaleta `pytest` jest taka, że przy błędzie pokazuje, co dokładnie się nie zgadza.

---

## Testowanie wyjątków

Czasem chcesz sprawdzić nie poprawny wynik, ale to, czy kod rzuca właściwy wyjątek.

Przykład:

```python
import pytest


def dziel(a: float, b: float) -> float:
    return a / b


def test_dzielenie_przez_zero_rzuca_blad():
    with pytest.raises(ZeroDivisionError):
        dziel(10, 0)
```

To bardzo ważny typ testu.

Bo kod trzeba sprawdzać nie tylko dla sytuacji poprawnych, ale też błędnych.

---

## Uruchamianie testów

Najprościej:

```bash
pytest
```

Możesz też uruchomić konkretny plik:

```bash
pytest test_math_utils.py
```

Albo konkretny test:

```bash
pytest test_math_utils.py::test_dodaj_dwie_liczby
```

Tryb krótszego outputu:

```bash
pytest -q
```

---

## Przykładowy output `pytest`

Jeśli wszystko przechodzi:

```text
============================= test session starts =============================
collected 3 items

test_math_utils.py ...                                                 [100%]

============================== 3 passed in 0.03s ==============================
```

Co to znaczy:

- zebrano 3 testy,
- wszystkie przeszły,
- wykonanie zajęło `0.03s`.

Jeśli jeden test nie przejdzie:

```text
============================= test session starts =============================
collected 3 items

test_math_utils.py .F.                                                 [100%]

================================== FAILURES ==================================
___________________________ test_dodaj_dwie_liczby ____________________________

    def test_dodaj_dwie_liczby():
>       assert dodaj(2, 3) == 6
E       assert 5 == 6
E        +  where 5 = dodaj(2, 3)

=========================== short test summary info ===========================
FAILED test_math_utils.py::test_dodaj_dwie_liczby - assert 5 == 6
========================= 1 failed, 2 passed in 0.04s =========================
```

---

## Jak czytać błąd testu

W raporcie błędu patrz przede wszystkim na:

- nazwę testu,
- linię, która padła,
- realne wartości po lewej i prawej stronie asercji,
- ścieżkę wywołania.

W powyższym przykładzie od razu widać:

- test oczekiwał `6`,
- funkcja zwróciła `5`,
- więc błąd jest w teście albo w założeniu testu.

To bardzo ważne:

nie każdy czerwony test znaczy, że kod aplikacji jest błędny.
Czasem błędny jest sam test.

---

## Organizacja katalogu `tests`

Prosty wariant:

```text
projekt/
    app.py
    math_utils.py
    tests/
        test_math_utils.py
        test_app.py
```

Bardziej rozbudowany wariant:

```text
projekt/
    src/
        app/
            __init__.py
            services.py
            validators.py
    tests/
        unit/
            test_services.py
            test_validators.py
        integration/
            test_api.py
```

Dla małych projektów prostsza wersja wystarcza.

---

## Co powinien testować dobry test jednostkowy

Dobry test jednostkowy powinien:

- sprawdzać jedną rzecz,
- mieć jasną nazwę,
- być szybki,
- dawać czytelny sygnał przy błędzie,
- nie zależeć od internetu, bazy i innych niestabilnych rzeczy, jeśli nie musi.

Przykład dobrej nazwy:

```python
def test_parse_int_zwraca_none_dla_niepoprawnego_tekstu():
    ...
```

Po samej nazwie wiadomo, co testujesz.

---

## Co powinien testować dobry test integracyjny

Dobry test integracyjny powinien:

- sprawdzać współpracę realnych części systemu,
- nie być zbyt szeroki bez potrzeby,
- skupiać się na realnym scenariuszu użytkowym,
- nadal dawać w miarę czytelny sygnał, co nie działa.

To nie ma być test "wszystkiego naraz".

---

## Typowe błędy początkujących

- testowanie tylko najłatwiejszych przypadków,
- brak testów wyjątków i wartości granicznych,
- pisanie testów zależnych od kolejności wykonania,
- zbyt ogólne nazwy testów,
- testy z dużą ilością niepotrzebnego setupu,
- mieszanie kilku tematów w jednym teście,
- ręczne sprawdzanie programu zamiast budowania automatycznych testów.

---

## Praktyczna ściąga

### Prosty test

```python
def test_dodaj():
    assert dodaj(2, 3) == 5
```

### Test wyjątku

```python
with pytest.raises(ValueError):
    parse_int("abc")
```

### Uruchomienie wszystkich testów

```bash
pytest
```

### Uruchomienie jednego pliku

```bash
pytest tests/test_utils.py
```

### Cichy tryb

```bash
pytest -q
```

---

## Ćwiczenia

1. Napisz prostą funkcję `odejmij(a, b)` i test dla niej.
2. Napisz funkcję `czy_dodatnia(n)` i przetestuj trzy przypadki: dodatni, zero, ujemny.
3. Napisz funkcję `dziel(a, b)` i test sprawdzający wyjątek dla dzielenia przez zero.
4. Uruchom cały katalog testów przez `pytest`.
5. Celowo zepsuj jedną asercję i przeanalizuj raport błędu.
6. Zbuduj prostą strukturę `tests/` dla małego projektu.
7. Rozdziel dwa testy na jednostkowy i integracyjny.
8. Zmień nazwy swoich testów tak, by mówiły dokładnie o zachowaniu.

---

## Najważniejsze do zapamiętania

- Test to kod, który sprawdza inny kod.
- `pytest` używa zwykłego `assert`, ale daje lepsze raporty.
- Testuj nie tylko poprawne przypadki, ale też błędy i wartości graniczne.
- Test jednostkowy sprawdza mały fragment logiki.
- Test integracyjny sprawdza współpracę elementów.
- Dobry test powinien być czytelny, mały i dawać jasny sygnał przy awarii.
