# Dokumentowanie kodu w Pythonie — docstrings, type hints, Sphinx

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co dokumentować kod](#po-co-dokumentować-kod)
3. [Czym jest docstring](#czym-jest-docstring)
4. [Docstring funkcji](#docstring-funkcji)
5. [Docstring klasy](#docstring-klasy)
6. [Docstring modułu](#docstring-modułu)
7. [Co pisać w docstringu](#co-pisać-w-docstringu)
8. [Type hints](#type-hints)
9. [Po co używać type hints](#po-co-używać-type-hints)
10. [Type hints a czytelność](#type-hints-a-czytelność)
11. [Docstrings a type hints](#docstrings-a-type-hints)
12. [Sphinx](#sphinx)
13. [Po co używać Sphinx](#po-co-używać-sphinx)
14. [Automatyczne generowanie dokumentacji](#automatyczne-generowanie-dokumentacji)
15. [Dokumentowanie API biblioteki](#dokumentowanie-api-biblioteki)
16. [Typowe błędy początkujących](#typowe-błędy-początkujących)
17. [Praktyczne przykłady](#praktyczne-przykłady)
18. [Dobre praktyki](#dobre-praktyki)
19. [Podsumowanie](#podsumowanie)
20. [Mini ściąga](#mini-ściąga)
21. [Ćwiczenia](#ćwiczenia)
22. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Dobry kod to nie tylko kod, który działa.

To też kod, który:

- da się zrozumieć,
- da się utrzymać,
- da się przekazać innym,
- da się łatwo używać po kilku miesiącach.

Właśnie dlatego dokumentowanie kodu jest tak ważne.

Najważniejsze elementy to:

- docstrings,
- type hints,
- narzędzia do generowania dokumentacji, np. Sphinx.

---

## Po co dokumentować kod

Bo z czasem nawet własny kod staje się „kodem obcym”.

Dokumentacja pomaga:

- szybciej wrócić do projektu,
- wdrożyć inną osobę,
- zrozumieć API modułu lub klasy,
- ograniczyć liczbę pytań i nieporozumień.

---

## Czym jest docstring

Docstring to tekst umieszczony na początku:

- modułu,
- funkcji,
- klasy,
- metody.

Przykład:

```python
def dodaj(a, b):
    """Zwraca sumę dwóch liczb."""
    return a + b
```

To podstawowy sposób dokumentowania kodu w Pythonie.

---

## Docstring funkcji

Dobry docstring funkcji powinien wyjaśniać:

- co robi funkcja,
- co przyjmuje,
- co zwraca,
- czasem jakie są wyjątki lub ważne uwagi.

---

## Docstring klasy

Docstring klasy opisuje:

- do czego służy klasa,
- jaki reprezentuje byt,
- jak jej używać.

---

## Docstring modułu

To opis całego pliku modułu.

Może zawierać:

- cel modułu,
- przegląd zawartości,
- ważne informacje użytkowe.

---

## Co pisać w docstringu

Najważniejsze:

- cel,
- zachowanie,
- znaczenie argumentów,
- ważne ograniczenia.

Nie opisuj rzeczy oczywistych, jeśli kod już to jasno pokazuje.

---

## Type hints

Type hints to adnotacje typów.

Przykład:

```python
def dodaj(a: int, b: int) -> int:
    return a + b
```

To nie wymusza typów w czasie wykonania, ale bardzo poprawia czytelność i współpracę z narzędziami.

---

## Po co używać type hints

Bo pomagają:

- lepiej rozumieć API,
- wychwytywać błędy narzędziami statycznymi,
- szybciej orientować się, jakie dane przepływają przez kod.

---

## Type hints a czytelność

W dobrym kodzie type hints bardzo poprawiają orientację.

Na przykład od razu widać:

- czy funkcja zwraca listę,
- czy może `None`,
- czy przyjmuje słownik,
- czy argument jest opcjonalny.

---

## Docstrings a type hints

To nie są rzeczy konkurujące.

### Type hints

Mówią:

- jakie są typy.

### Docstring

Mówi:

- co funkcja robi i jak jej używać.

Najlepszy efekt daje połączenie obu.

---

## Sphinx

Sphinx to popularne narzędzie do generowania dokumentacji projektu.

Może budować dokumentację na podstawie:

- plików `.rst`,
- docstringów,
- struktury kodu.

Jest bardzo popularny w bibliotekach Pythona.

---

## Po co używać Sphinx

Bo pozwala budować profesjonalną, spójną dokumentację projektu.

Szczególnie przydaje się, gdy:

- tworzysz bibliotekę,
- masz większy projekt,
- chcesz publikować dokumentację.

---

## Automatyczne generowanie dokumentacji

Dzięki narzędziom takim jak Sphinx część dokumentacji można budować automatycznie z docstringów.

To bardzo praktyczne, bo:

- nie dublujesz wiedzy w wielu miejscach,
- zmniejszasz ryzyko rozjazdu dokumentacji i kodu.

---

## Dokumentowanie API biblioteki

Jeśli piszesz moduł albo bibliotekę, dokumentacja publicznych funkcji i klas jest bardzo ważna.

To właśnie ją najczęściej czytają inni użytkownicy projektu.

---

## Typowe błędy początkujących

- brak docstringów w ważnych funkcjach,
- pisanie bezużytecznych docstringów typu „ta funkcja coś robi”,
- brak type hints tam, gdzie byłyby bardzo pomocne,
- traktowanie dokumentacji jako czegoś opcjonalnego w większym projekcie.

---

## Praktyczne przykłady

### Funkcja

```python
def dodaj(a: int, b: int) -> int:
    """Zwraca sumę dwóch liczb całkowitych."""
    return a + b
```

### Klasa

```python
class Konto:
    """Reprezentuje proste konto z saldem."""

    def __init__(self, saldo: float) -> None:
        self.saldo = saldo
```

### Moduł

```python
"""Narzędzia do podstawowych obliczeń matematycznych."""
```

---

## Dobre praktyki

- dokumentuj publiczne API,
- używaj type hints w nowym kodzie,
- pisz docstringi zwięzłe, ale konkretne,
- nie dokumentuj rzeczy oczywistych bez potrzeby,
- aktualizuj dokumentację razem z kodem.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- docstrings opisują działanie kodu,
- type hints opisują typy,
- Sphinx pomaga generować profesjonalną dokumentację,
- dobra dokumentacja bardzo zwiększa jakość projektu.

---

## Mini ściąga

```python
def f(x: int) -> int:
    """Opis funkcji."""
    return x
```

### Kluczowe narzędzia

- docstrings
- type hints
- Sphinx

---

## Ćwiczenia

### Ćwiczenie 1

Dodaj docstring do własnej funkcji.

### Ćwiczenie 2

Dodaj type hints do funkcji przyjmującej listę liczb.

### Ćwiczenie 3

Napisz krótki docstring klasy `Osoba`.

---

## Przykładowe rozwiązania

```python
def suma(liczby: list[int]) -> int:
    """Zwraca sumę listy liczb całkowitych."""
    return sum(liczby)
```
