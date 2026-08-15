# Dokumentowanie kodu w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co dokumentować kod](#po-co-dokumentować-kod)
3. [Czym jest docstring](#czym-jest-docstring)
4. [Docstring modułu](#docstring-modułu)
5. [Docstring funkcji](#docstring-funkcji)
6. [Docstring klasy i metody](#docstring-klasy-i-metody)
7. [Jak pisać dobry docstring](#jak-pisać-dobry-docstring)
8. [Type hints](#type-hints)
9. [Najczęstsze typy i adnotacje](#najczęstsze-typy-i-adnotacje)
10. [Docstrings i type hints razem](#docstrings-i-type-hints-razem)
11. [Styl dokumentowania](#styl-dokumentowania)
12. [Dokumentowanie wyjątków i zachowania](#dokumentowanie-wyjątków-i-zachowania)
13. [Dokumentowanie modułów użytkowych](#dokumentowanie-modułów-użytkowych)
14. [Sphinx](#sphinx)
15. [Automatyczne generowanie dokumentacji](#automatyczne-generowanie-dokumentacji)
16. [Typowe błędy początkujących](#typowe-błędy-początkujących)
17. [Praktyczna ściąga](#praktyczna-ściąga)
18. [Ćwiczenia](#ćwiczenia)
19. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

Dobry kod to nie tylko kod, który działa.

Dobry kod to też kod, który:

- da się zrozumieć po miesiącu,
- da się łatwo użyć z innego pliku,
- da się przekazać innej osobie,
- nie wymaga zgadywania, co robi funkcja albo klasa.

Dokumentowanie kodu w Pythonie zwykle opiera się na trzech rzeczach:

- dobrych nazwach,
- docstringach,
- type hints.

W większych projektach dochodzą też narzędzia takie jak Sphinx.

---

## Po co dokumentować kod

Po kilku tygodniach nawet własny kod potrafi wyglądać obco.

Dokumentacja pomaga:

- szybciej wrócić do projektu,
- zrozumieć API modułu,
- ograniczyć liczbę pomyłek,
- skrócić czas wdrożenia nowej osoby,
- łatwiej testować i utrzymywać kod.

Jeśli funkcja ma nietrywialne zachowanie, to sama nazwa zwykle nie wystarcza.

---

## Czym jest docstring

Docstring to tekst umieszczony na początku modułu, funkcji, klasy albo metody.

Przykład:

```python
def dodaj(a, b):
    """Zwraca sumę dwóch liczb."""
    return a + b
```

To nie jest zwykły komentarz.

Docstring jest częścią obiektu i można go odczytać np. przez `help()` albo atrybut `.__doc__`.

Przykład:

```python
def dodaj(a, b):
    """Zwraca sumę dwóch liczb."""
    return a + b

print(dodaj.__doc__)
help(dodaj)
```

Przykładowy output `print(dodaj.__doc__)`:

```text
Zwraca sumę dwóch liczb.
```

Fragment uproszczonego outputu `help(dodaj)`:

```text
Help on function dodaj:

dodaj(a, b)
    Zwraca sumę dwóch liczb.
```

---

## Docstring modułu

Na samej górze pliku możesz opisać cały moduł.

```python
"""Moduł zawiera funkcje pomocnicze do operacji na tekstach."""


def wyczysc_tekst(tekst: str) -> str:
    return tekst.strip().lower()
```

Docstring modułu powinien odpowiadać na pytanie:

co znajduje się w tym pliku i do czego służy?

---

## Docstring funkcji

Dobry docstring funkcji powinien wyjaśniać:

- co robi funkcja,
- jakie przyjmuje argumenty,
- co zwraca,
- czy rzuca wyjątki,
- czy ma jakieś ważne ograniczenia.

Przykład prosty:

```python
def pole_prostokata(a: float, b: float) -> float:
    """Zwraca pole prostokąta o bokach a i b."""
    return a * b
```

Przykład bardziej praktyczny:

```python
def parse_int(tekst: str) -> int | None:
    """Próbuje zamienić tekst na int.

    Zwraca liczbę całkowitą, jeśli konwersja się powiedzie.
    Jeśli tekst nie reprezentuje poprawnej liczby, zwraca None.
    """
    try:
        return int(tekst)
    except ValueError:
        return None
```

Taki docstring daje dużo więcej informacji niż sama nazwa funkcji.

---

## Docstring klasy i metody

Klasa też powinna mieć opis.

```python
class BankAccount:
    """Proste konto bankowe przechowujące saldo użytkownika."""

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """Dodaje środki do konta."""
        self.balance += amount
```

Docstring klasy opisuje cały byt.

Docstring metody opisuje konkretne zachowanie tej metody.

---

## Jak pisać dobry docstring

Dobry docstring jest:

- krótki, ale konkretny,
- praktyczny,
- zgodny z realnym zachowaniem funkcji,
- aktualny.

Słaby docstring:

```python
def dodaj(a, b):
    """Ta funkcja coś dodaje."""
```

Lepszy:

```python
def dodaj(a: int, b: int) -> int:
    """Zwraca sumę dwóch liczb całkowitych."""
```

Jeszcze lepszy, jeśli zachowanie nie jest oczywiste:

```python
def podziel(a: float, b: float) -> float | None:
    """Zwraca wynik dzielenia a przez b.

    Gdy b jest równe 0, funkcja zwraca None zamiast rzucać wyjątek.
    """
```

---

## Type hints

Type hints to adnotacje typów.

Przykład:

```python
def powitaj(imie: str) -> str:
    return f"Witaj {imie}"
```

Tu od razu widać:

- argument `imie` powinien być `str`,
- funkcja zwraca `str`.

Ważne:

Python zwykle nie wymusza tych typów w czasie działania.

One pomagają przede wszystkim:

- ludziom,
- edytorowi,
- narzędziom statycznej analizy.

---

## Najczęstsze typy i adnotacje

### Proste typy

```python
x: int = 5
nazwa: str = "Python"
czy_aktywny: bool = True
cena: float = 19.99
```

### Kolekcje

```python
def policz_sume(liczby: list[int]) -> int:
    return sum(liczby)
```

```python
def policz_wystapienia(slowa: tuple[str, ...]) -> int:
    return len(slowa)
```

```python
def zwroc_punkty() -> dict[str, int]:
    return {"Anna": 10, "Jan": 7}
```

### Wartość opcjonalna

```python
def znajdz_uzytkownika(user_id: int) -> str | None:
    ...
```

To znaczy: funkcja może zwrócić `str` albo `None`.

### Brak zwracanej wartości

```python
def wypisz_komunikat(tekst: str) -> None:
    print(tekst)
```

---

## Docstrings i type hints razem

To bardzo ważne: one się nie wykluczają.

### Type hints

Mówią głównie:

- jakie dane wchodzą,
- jakie dane wychodzą.

### Docstring

Mówi:

- co funkcja robi,
- jakie są reguły działania,
- jakie są wyjątki,
- kiedy zwraca szczególne wartości.

Przykład połączenia obu:

```python
def bezpieczne_dzielenie(a: float, b: float) -> float | None:
    """Zwraca wynik dzielenia a przez b.

    Jeśli b == 0, funkcja zwraca None.
    """
    if b == 0:
        return None
    return a / b
```

To jest dużo czytelniejsze niż sama implementacja bez opisu.

---

## Styl dokumentowania

W praktyce warto trzymać się kilku zasad:

- publiczne funkcje i klasy dokumentuj prawie zawsze,
- prywatne, trywialne helpery nie zawsze potrzebują pełnego docstringu,
- jeśli kod jest oczywisty, nie opisuj banałów,
- jeśli zachowanie może zaskakiwać, opisz je wyraźnie.

Przykład niepotrzebnego banału:

```python
def increment(x: int) -> int:
    """Zwiększa x o 1."""
    return x + 1
```

To jeszcze może przejść, ale jeśli cały projekt ma pełno takich opisów, dokumentacja zaczyna przeszkadzać zamiast pomagać.

---

## Dokumentowanie wyjątków i zachowania

Jeśli funkcja:

- zwraca `None` w nietypowej sytuacji,
- rzuca wyjątek,
- modyfikuje argument,
- zapisuje do pliku,
- wykonuje zapytanie do sieci,

warto to wyraźnie napisać.

Przykład:

```python
def wczytaj_plik(sciezka: str) -> str:
    """Wczytuje zawartość pliku tekstowego.

    Raises:
        FileNotFoundError: Gdy plik nie istnieje.
    """
    with open(sciezka, "r", encoding="utf-8") as f:
        return f.read()
```

Nawet jeśli nie używasz formalnego stylu `Raises`, sama informacja o wyjątkach jest bardzo cenna.

---

## Dokumentowanie modułów użytkowych

W projektach Pythona często masz moduły typu:

- `utils.py`
- `validators.py`
- `parsers.py`
- `config.py`

Takie moduły łatwo zamieniają się w worki na przypadkowy kod.

Docstring modułu pomaga od razu zrozumieć jego rolę.

Przykład:

```python
"""Narzędzia do walidacji danych wejściowych użytkownika.

Moduł zawiera funkcje sprawdzające e-mail, hasło i numer telefonu.
"""
```

---

## Sphinx

Sphinx to popularne narzędzie do generowania dokumentacji projektu.

Może budować dokumentację z:

- plików tekstowych,
- struktury projektu,
- docstringów.

W praktyce Sphinx jest często używany w bibliotekach i większych projektach.

Nie musisz go umieć perfekcyjnie na początku, ale warto wiedzieć, do czego służy.

---

## Automatyczne generowanie dokumentacji

Duża zaleta dobrych docstringów jest taka, że dokumentację można z nich generować automatycznie.

To oznacza:

- mniej ręcznego przepisywania wiedzy,
- mniejsze ryzyko rozjazdu dokumentacji z kodem,
- lepszą spójność projektu.

Jeśli funkcja ma sensowne nazwy, type hints i dobry docstring, to już budujesz bardzo solidną bazę pod dokumentację.

---

## Typowe błędy początkujących

- brak dokumentacji w publicznych funkcjach,
- docstringi nic nie mówiące,
- opisy niezgodne z realnym działaniem funkcji,
- brak type hints tam, gdzie bardzo pomagają,
- nadmierne opisywanie banałów,
- traktowanie dokumentacji jak czegoś „na później”.

---

## Praktyczna ściąga

### Prosty docstring funkcji

```python
def dodaj(a: int, b: int) -> int:
    """Zwraca sumę dwóch liczb całkowitych."""
    return a + b
```

### Funkcja z opisem nietypowego zachowania

```python
def parse_int(tekst: str) -> int | None:
    """Zamienia tekst na int albo zwraca None, jeśli to niemożliwe."""
    ...
```

### Docstring klasy

```python
class User:
    """Reprezentuje użytkownika systemu."""
```

### Odczyt docstringu

```python
print(dodaj.__doc__)
help(dodaj)
```

---

## Ćwiczenia

1. Dodaj docstring do funkcji `powitaj(imie)`.
2. Napisz funkcję `pole_kola(r)` z type hints i krótkim docstringiem.
3. Napisz funkcję `parse_float(tekst)`, która zwraca `float | None`, i opisz to w docstringu.
4. Utwórz klasę `Car` z docstringiem klasy i metodą `start()` z własnym docstringiem.
5. Napisz docstring modułu dla pliku z funkcjami walidującymi dane.
6. Wypisz `.__doc__` dla własnej funkcji.
7. Użyj `help()` dla własnej klasy i zobacz, jak Python pokazuje dokumentację.
8. Przerób jedną starą funkcję w projekcie tak, aby miała i type hints, i docstring.
9. Zapisz własnymi słowami różnicę między komentarzem, docstringiem i type hint.
10. Wskaż trzy miejsca, w których dokumentacja naprawdę pomaga bardziej niż sam kod.

---

## Najważniejsze do zapamiętania

- Docstring opisuje zachowanie i sposób użycia.
- Type hints opisują typy danych.
- Najlepszy efekt daje połączenie dobrych nazw, docstringów i type hints.
- Dokumentacja ma pomagać, a nie produkować szum.
- Jeśli funkcja ma nietypowe zachowanie, opisz je wyraźnie.
- Dobrze udokumentowany kod łatwiej rozwijać, testować i poprawiać.
