# Testowanie w Pythonie — podstawy, testy jednostkowe, integracyjne i `pytest`

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co w ogóle pisać testy](#po-co-w-ogóle-pisać-testy)
3. [Czym jest test](#czym-jest-test)
4. [Testy jednostkowe](#testy-jednostkowe)
5. [Testy integracyjne](#testy-integracyjne)
6. [Różnica między testem jednostkowym a integracyjnym](#różnica-między-testem-jednostkowym-a-integracyjnym)
7. [Dlaczego `pytest` jest tak popularny](#dlaczego-pytest-jest-tak-popularny)
8. [Jak wygląda najprostszy test w `pytest`](#jak-wygląda-najprostszy-test-w-pytest)
9. [Konwencja nazw plików i funkcji testowych](#konwencja-nazw-plików-i-funkcji-testowych)
10. [Asercje w `pytest`](#asercje-w-pytest)
11. [Uruchamianie testów](#uruchamianie-testów)
12. [Struktura katalogu testów](#struktura-katalogu-testów)
13. [Co powinien testować test jednostkowy](#co-powinien-testować-test-jednostkowy)
14. [Co powinien testować test integracyjny](#co-powinien-testować-test-integracyjny)
15. [Najczęstsze błędy początkujących](#najczęstsze-błędy-początkujących)
16. [Praktyczne przykłady](#praktyczne-przykłady)
17. [Dobre praktyki](#dobre-praktyki)
18. [Podsumowanie](#podsumowanie)
19. [Mini ściąga](#mini-ściąga)
20. [Ćwiczenia](#ćwiczenia)
21. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Testowanie to jeden z najważniejszych elementów programowania.

Nie chodzi tylko o „sprawdzenie, czy działa”.

Testy pomagają:

- wychwytywać błędy,
- bezpiecznie rozwijać kod,
- szybciej refaktoryzować,
- zyskiwać pewność, że zmiana niczego nie zepsuła.

W Pythonie najczęściej spotkasz:

- testy jednostkowe,
- testy integracyjne,
- framework `pytest`.

---

## Po co w ogóle pisać testy

Bez testów często działa taki scenariusz:

1. coś zmieniasz,
2. naprawiasz jeden problem,
3. przypadkiem psujesz coś innego,
4. odkrywasz to dopiero dużo później.

Testy zmniejszają to ryzyko.

To nie znaczy, że testy gwarantują brak błędów.
Ale bardzo zwiększają bezpieczeństwo pracy nad kodem.

---

## Czym jest test

Test to fragment kodu, który sprawdza, czy inny kod zachowuje się zgodnie z oczekiwaniem.

Przykład:

```python
def dodaj(a, b):
    return a + b

def test_dodaj():
    assert dodaj(2, 3) == 5
```

Tutaj test sprawdza, czy `dodaj(2, 3)` daje `5`.

---

## Testy jednostkowe

Test jednostkowy sprawdza mały, pojedynczy fragment programu.

Najczęściej:

- jedną funkcję,
- jedną metodę,
- jedną małą klasę,
- jedną regułę logiki.

To test małej jednostki kodu, zwykle w izolacji.

### Przykład

```python
def czy_pelnoletni(wiek):
    return wiek >= 18

def test_czy_pelnoletni():
    assert czy_pelnoletni(20) is True
    assert czy_pelnoletni(15) is False
```

---

## Testy integracyjne

Test integracyjny sprawdza współpracę kilku elementów razem.

Na przykład:

- funkcja + baza danych,
- endpoint API + logika aplikacji,
- zapis pliku + odczyt pliku,
- kilka modułów działających wspólnie.

To już nie jest test „jednej małej rzeczy”, tylko większej całości.

---

## Różnica między testem jednostkowym a integracyjnym

### Test jednostkowy

- mały zakres,
- szybki,
- zwykle w izolacji,
- łatwiejszy do znalezienia źródła błędu.

### Test integracyjny

- większy zakres,
- sprawdza współpracę elementów,
- bywa wolniejszy,
- lepiej pokazuje, czy system działa jako całość.

Najczęściej potrzebujesz obu rodzajów testów.

---

## Dlaczego `pytest` jest tak popularny

`pytest` jest bardzo lubiany, bo:

- ma prostą składnię,
- pozwala pisać testy naturalnie,
- ma świetny system fixture’ów,
- dobrze raportuje błędy,
- ma ogromny ekosystem pluginów.

To obecnie jeden z najpopularniejszych sposobów testowania w Pythonie.

---

## Jak wygląda najprostszy test w `pytest`

```python
def dodaj(a, b):
    return a + b

def test_dodaj():
    assert dodaj(2, 3) == 5
```

To już jest pełnoprawny test `pytest`.

---

## Konwencja nazw plików i funkcji testowych

Najczęściej:

- pliki nazywa się `test_*.py`
- funkcje testowe też zaczynają się od `test_`

Przykłady:

- `test_math.py`
- `test_users.py`
- `def test_login(): ...`

Dzięki temu `pytest` łatwo znajduje testy automatycznie.

---

## Asercje w `pytest`

Najprostszy zapis:

```python
assert wynik == oczekiwany
```

To bardzo wygodne, bo `pytest` potrafi dobrze pokazać różnicę między wynikiem a oczekiwaniem.

### Przykład

```python
def test_kwadrat():
    assert 3 * 3 == 9
```

---

## Uruchamianie testów

Najczęściej z terminala:

```bash
pytest
```

albo tylko konkretnego pliku:

```bash
pytest test_math.py
```

albo konkretnego testu:

```bash
pytest test_math.py::test_dodaj
```

---

## Struktura katalogu testów

Popularne układy:

```text
projekt/
    app.py
    test_app.py
```

albo:

```text
projekt/
    app/
    tests/
        test_app.py
```

Drugi wariant bywa wygodniejszy w większych projektach.

---

## Co powinien testować test jednostkowy

Przede wszystkim:

- logikę funkcji,
- przypadki typowe,
- przypadki graniczne,
- błędne dane, jeśli funkcja ma je obsługiwać.

### Przykłady przypadków

- poprawne dane,
- zero,
- pusty string,
- pusta lista,
- liczba ujemna,
- wyjątek.

---

## Co powinien testować test integracyjny

Przede wszystkim to, czy elementy programu dobrze współpracują.

Na przykład:

- czy zapis do bazy działa razem z odczytem,
- czy endpoint HTTP wywołuje poprawną logikę,
- czy dane przechodzą poprawnie przez kilka warstw programu.

---

## Najczęstsze błędy początkujących

### 1. Testowanie wszystkiego ręcznie przez `print()`

To nie jest jeszcze sensowny system testów.

### 2. Pisanie zbyt dużych testów jednostkowych

Test jednostkowy powinien dotyczyć małej rzeczy.

### 3. Brak przypadków brzegowych

### 4. Mieszanie testów jednostkowych i integracyjnych bez rozróżnienia

### 5. Zbyt ogólne nazwy testów

Na przykład:

```python
def test1():
    ...
```

To nic nie mówi.

---

## Praktyczne przykłady

### Prosta funkcja i test

```python
def dodaj(a, b):
    return a + b

def test_dodaj():
    assert dodaj(2, 3) == 5
```

### Test kilku przypadków

```python
def czy_pusty(tekst):
    return tekst == ""

def test_czy_pusty():
    assert czy_pusty("") is True
    assert czy_pusty("abc") is False
```

### Prosty test integracyjny ideowo

```python
def zapisz_i_odczytaj(repo, user):
    repo.save(user)
    return repo.get(user.id)
```

Tu test integracyjny sprawdzałby współpracę kilku elementów razem.

---

## Dobre praktyki

### Utrzymuj testy proste i czytelne

### Nadawaj testom opisowe nazwy

Na przykład:

```python
def test_dodaj_zwraca_sume_dwoch_liczb():
    ...
```

### Testuj przypadki typowe i brzegowe

### Nie bój się pisać wielu małych testów

To zwykle lepsze niż jeden ogromny test.

### Rozdzielaj testy jednostkowe i integracyjne

Choćby logicznie, a najlepiej też katalogami lub nazwami.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- testy jednostkowe sprawdzają małe fragmenty kodu,
- testy integracyjne sprawdzają współpracę elementów,
- `pytest` to bardzo popularne i wygodne narzędzie,
- podstawą testu jest dobra asercja,
- dobre testy są małe, czytelne i opisowe.

---

## Mini ściąga

```python
def test_nazwa():
    assert funkcja(...) == ...
```

```bash
pytest
pytest test_app.py
pytest test_app.py::test_nazwa
```

---

## Ćwiczenia

### Ćwiczenie 1

Napisz funkcję `odejmij(a, b)` i test dla niej.

### Ćwiczenie 2

Napisz funkcję sprawdzającą, czy liczba jest parzysta, i testy dla kilku przypadków.

### Ćwiczenie 3

Przygotuj plik `test_math.py` z kilkoma testami.

---

## Przykładowe rozwiązania

### Ćwiczenie 1

```python
def odejmij(a, b):
    return a - b

def test_odejmij():
    assert odejmij(5, 2) == 3
```

### Ćwiczenie 2

```python
def czy_parzysta(x):
    return x % 2 == 0

def test_czy_parzysta():
    assert czy_parzysta(2) is True
    assert czy_parzysta(3) is False
    assert czy_parzysta(0) is True
```
