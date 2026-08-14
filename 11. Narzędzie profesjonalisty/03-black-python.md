# `black` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `black`](#czym-jest-black)
3. [Po co używać formattera](#po-co-używać-formattera)
4. [Jak działa `black`](#jak-działa-black)
5. [Konfiguracja](#konfiguracja)
6. [Relacja z `ruff`](#relacja-z-ruff)
7. [Typowe błędy początkujących](#typowe-błędy-początkujących)
8. [Praktyczne przykłady](#praktyczne-przykłady)
9. [Dobre praktyki](#dobre-praktyki)
10. [Podsumowanie](#podsumowanie)
11. [Mini ściąga](#mini-ściąga)
12. [Ćwiczenia](#ćwiczenia)
13. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`black` to automatyczny formatter kodu Python.

Jego główny cel to usunięcie sporów o styl i zapewnienie jednolitego wyglądu kodu w całym projekcie.

---

## Czym jest `black`

To narzędzie, które bierze kod i formatuje go według jasno określonych zasad.

Nie daje dużo miejsca na ręczne dyskusje o stylu.

To właśnie jest jego siła.

---

## Po co używać formattera

Formatter pomaga:

- utrzymać spójny styl,
- skrócić code review,
- zmniejszyć liczbę kosmetycznych poprawek,
- skupić się na logice zamiast na spacjach i łamaniach linii.

---

## Jak działa `black`

Zwykle uruchamiasz go na plikach lub całym projekcie.

Efekt:

- kod wygląda spójnie,
- długie linie są łamane według reguł,
- nawiasy i odstępy są porządkowane automatycznie.

---

## Konfiguracja

W `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ["py312"]
```

Najczęściej konfiguracja jest mała, bo `black` celowo ogranicza liczbę opcji.

---

## Relacja z `ruff`

`black` i `ruff` często działają razem:

- `black` formatuje kod,
- `ruff` pilnuje jakości i części reguł stylu.

W nowoczesnych projektach to bardzo częsty duet.

---

## Typowe błędy początkujących

- ręczne poprawianie stylu zamiast użycia formattera,
- kłócenie się z formatterem o drobiazgi,
- brak spójnego narzędzia w całym zespole,
- mieszanie wielu formatterów bez potrzeby.

---

## Praktyczne przykłady

### Przed

```python
def dodaj( a,b ): return a+b
```

### Po

```python
def dodaj(a, b):
    return a + b
```

### Konfiguracja

```toml
[tool.black]
line-length = 88
```

---

## Dobre praktyki

- używaj formattera automatycznie,
- uruchamiaj go przed commitem lub w `pre-commit`,
- nie walcz ze stylem narzędzia bez ważnego powodu,
- trzymaj jedną spójną konfigurację dla całego projektu.

---

## Podsumowanie

`black` to jedno z najprostszych i najbardziej opłacalnych narzędzi jakościowych w Pythonie.

Pozwala przenieść rozmowę ze stylu kodu na jakość rozwiązania.

---

## Mini ściąga

```toml
[tool.black]
line-length = 88
target-version = ["py312"]
```

Najważniejsze:

- `black` formatuje kod automatycznie,
- zmniejsza spory o styl,
- dobrze współpracuje z `ruff`,
- zwykle ma małą konfigurację.

---

## Ćwiczenia

1. Wyjaśnij, po co zespołowi formatter.
2. Dodaj minimalną konfigurację `black` do `pyproject.toml`.
3. Wskaż przykład kodu, który formatter uprości.
4. Wyjaśnij relację `black` i `ruff`.
5. Podaj argument, dlaczego formatter skraca code review.

---

## Przykładowe rozwiązania

### 1. Po co formatter

Żeby automatycznie utrzymywać spójny styl kodu i nie tracić czasu na kosmetykę.

### 2. Konfiguracja

```toml
[tool.black]
line-length = 88
```

### 3. Uproszczenie

```python
def f( a,b ): return a+b
```

### 4. Relacja

`black` formatuje, a `ruff` lintuje i wykrywa problemy jakościowe.

### 5. Code review

Bo reviewer nie musi komentować spacji, łamania linii i podobnych drobiazgów.
