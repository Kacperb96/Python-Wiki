# `mypy` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `mypy`](#czym-jest-mypy)
3. [Po co używać `mypy`](#po-co-używać-mypy)
4. [Relacja z `typing`](#relacja-z-typing)
5. [Jakie błędy pomaga łapać](#jakie-błędy-pomaga-łapać)
6. [Konfiguracja w `pyproject.toml`](#konfiguracja-w-pyprojecttoml)
7. [Tryb `strict`](#tryb-strict)
8. [Typowe błędy początkujących](#typowe-błędy-początkujących)
9. [Praktyczne przykłady](#praktyczne-przykłady)
10. [Dobre praktyki](#dobre-praktyki)
11. [Podsumowanie](#podsumowanie)
12. [Mini ściąga](#mini-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`mypy` to narzędzie do statycznej analizy typów w Pythonie.

Pomaga wykrywać błędy jeszcze przed uruchomieniem programu.

---

## Czym jest `mypy`

`mypy` czyta adnotacje typów i sprawdza, czy kod jest z nimi spójny.

Na przykład może wykryć, że:

- funkcja miała zwracać `int`, a zwraca `str`,
- przekazujesz zły typ argumentu,
- próbujesz użyć `None` tam, gdzie nie powinno go być.

---

## Po co używać `mypy`

Bo w większych projektach znacząco pomaga:

- wcześniej łapać regresje,
- poprawiać czytelność API,
- lepiej współpracować zespołowo,
- spokojniej refaktoryzować kod.

---

## Relacja z `typing`

`typing` daje adnotacje.

`mypy` daje narzędzie, które potrafi te adnotacje sprawdzić.

Jedno bez drugiego ma mniejszą wartość.

---

## Jakie błędy pomaga łapać

Na przykład:

- zły typ argumentu,
- zły typ zwracany,
- brak obsługi `None`,
- niespójne struktury danych,
- błędy przy refaktoryzacji.

---

## Konfiguracja w `pyproject.toml`

```toml
[tool.mypy]
python_version = "3.12"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
```

To dobry kierunek na bardziej profesjonalny projekt.

---

## Tryb `strict`

`strict = true` to mocniejszy reżim sprawdzania.

Nie zawsze warto włączać go od pierwszej minuty w starym projekcie, ale w nowych projektach bardzo często jest sensownym celem.

---

## Typowe błędy początkujących

- oczekiwanie, że `mypy` zastąpi testy,
- zalewanie kodu `Any`,
- ignorowanie błędów typów zamiast ich zrozumienia,
- brak spójności adnotacji w publicznych funkcjach.

---

## Praktyczne przykłady

### Błąd typu zwracanego

```python
def dodaj(a: int, b: int) -> int:
    return "wynik"
```

To powinno zostać zgłoszone jako błąd.

### Błąd argumentu

```python
def policz(x: int) -> int:
    return x * 2

policz("abc")
```

---

## Dobre praktyki

- typuj publiczne funkcje i kluczowe modele danych,
- nie uciekaj zbyt szybko do `Any`,
- w nowych projektach rozważ mocniejszą konfigurację,
- używaj `mypy` razem z testami i lintingiem.

---

## Podsumowanie

`mypy` jest bardzo ważnym narzędziem profesjonalnego Pythona.

Nie zastępuje testów, ale świetnie uzupełnia workflow jakościowy i zwiększa bezpieczeństwo refaktoryzacji.

---

## Mini ściąga

Przykład:

```python
def hello(name: str) -> str:
    return f"Hi {name}"
```

Przykładowa konfiguracja:

```toml
[tool.mypy]
python_version = "3.12"
strict = true
```

Najważniejsze:

- `mypy` sprawdza zgodność typów,
- działa na adnotacjach,
- najlepiej używać go regularnie, a nie od święta.

---

## Ćwiczenia

1. Dodaj typy do prostej funkcji sumującej.
2. Pokaż przykład błędnego typu zwracanego.
3. Pokaż przykład błędnego argumentu funkcji.
4. Dodaj prostą konfigurację `mypy` do `pyproject.toml`.
5. Wyjaśnij, czemu `Any` osłabia korzyści typowania.

---

## Przykładowe rozwiązania

### 1. Typy funkcji

```python
def dodaj(a: int, b: int) -> int:
    return a + b
```

### 2. Zły typ zwracany

```python
def f() -> int:
    return "x"
```

### 3. Zły argument

```python
def podwoj(x: int) -> int:
    return x * 2

podwoj("abc")
```

### 4. Konfiguracja

```toml
[tool.mypy]
python_version = "3.12"
disallow_untyped_defs = true
```

### 5. `Any`

Bo wyłącza część ochrony, którą normalnie dają adnotacje i checker typów.
