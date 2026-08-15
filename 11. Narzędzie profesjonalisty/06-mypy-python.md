# `mypy` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `mypy`](#czym-jest-mypy)
3. [Po co używać `mypy`](#po-co-używać-mypy)
4. [Relacja z `typing`](#relacja-z-typing)
5. [Jakie błędy pomaga łapać](#jakie-błędy-pomaga-łapać)
6. [Podstawowe komendy](#podstawowe-komendy)
7. [Przykładowy output](#przykładowy-output)
8. [Konfiguracja w `pyproject.toml`](#konfiguracja-w-pyprojecttoml)
9. [Tryb `strict`](#tryb-strict)
10. [Typowe błędy początkujących](#typowe-błędy-początkujących)
11. [Praktyczna ściąga](#praktyczna-ściąga)
12. [Ćwiczenia](#ćwiczenia)
13. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

`mypy` to narzędzie do statycznej analizy typów w Pythonie.

Pomaga wykrywać błędy jeszcze przed uruchomieniem programu.

To bardzo wartościowe szczególnie wtedy, gdy projekt zaczyna rosnąć.

---

## Czym jest `mypy`

`mypy` czyta adnotacje typów i sprawdza, czy kod jest z nimi spójny.

Na przykład może wykryć, że:

- funkcja miała zwracać `int`, a zwraca `str`,
- przekazujesz zły typ argumentu,
- próbujesz użyć `None` tam, gdzie nie powinno go być.

---

## Po co używać `mypy`

Bo w większych projektach pomaga:

- wcześniej łapać regresje,
- poprawiać czytelność API,
- spokojniej refaktoryzować kod,
- szybciej zauważać niespójności między modułami.

To nie zastępuje testów, ale bardzo dobrze je uzupełnia.

---

## Relacja z `typing`

`typing` daje adnotacje.

`mypy` daje narzędzie, które potrafi te adnotacje sprawdzić.

Jedno bez drugiego ma mniejszą wartość:

- same typy bez sprawdzania łatwo zignorować,
- samo sprawdzanie bez adnotacji ma ograniczony zasięg.

---

## Jakie błędy pomaga łapać

Przykłady:

- zły typ argumentu,
- zły typ zwracany,
- brak obsługi `None`,
- niespójne struktury danych,
- błędy po refaktoryzacji.

To są problemy, które w dynamicznym języku łatwo przegapić.

---

## Podstawowe komendy

Sprawdzenie projektu:

```bash
mypy .
```

Sprawdzenie konkretnego modułu:

```bash
mypy app.py
```

To najprostszy punkt wejścia.

---

## Przykładowy output

Kod:

```python
def dodaj(a: int, b: int) -> int:
    return "wynik"


wynik = dodaj("2", 3)
```

Przykładowy output:

```text
app.py:2: error: Incompatible return value type (got "str", expected "int")  [return-value]
app.py:5: error: Argument 1 to "dodaj" has incompatible type "str"; expected "int"  [arg-type]
Found 2 errors in 1 file (checked 1 source file)
```

To bardzo czytelny sygnał:

- masz zły typ zwracany,
- i zły typ argumentu.

---

## Konfiguracja w `pyproject.toml`

Przykład:

```toml
[tool.mypy]
python_version = "3.12"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
```

To sensowny kierunek dla bardziej profesjonalnego projektu.

---

## Tryb `strict`

`strict = true` włącza mocniejszy reżim sprawdzania.

Przykład:

```toml
[tool.mypy]
python_version = "3.12"
strict = true
```

W nowych projektach to często bardzo dobry cel.

W starszym projekcie lepiej czasem dojść do tego etapami.

---

## Typowe błędy początkujących

- oczekiwanie, że `mypy` zastąpi testy,
- zalewanie kodu `Any`,
- ignorowanie błędów typów zamiast ich zrozumienia,
- brak typów w publicznych funkcjach,
- włączanie zbyt ostrej konfiguracji bez planu w istniejącym bałaganie.

---

## Praktyczna ściąga

### Sprawdzenie projektu

```bash
mypy .
```

### Prosta konfiguracja

```toml
[tool.mypy]
python_version = "3.12"
strict = true
```

### Pamiętaj

- `mypy` nie uruchamia kodu,
- sprawdza zgodność typów,
- bardzo pomaga przy refaktoryzacji.

---

## Ćwiczenia

1. Napisz funkcję z błędnym typem zwracanym i sprawdź raport `mypy`.
2. Przekaż zły typ argumentu i zobacz, czy zostanie zgłoszony.
3. Dodaj minimalną konfigurację `mypy` do `pyproject.toml`.
4. Wyjaśnij własnymi słowami, czym różni się `typing` od `mypy`.
5. Zastanów się, czemu `mypy` nie zastępuje testów.

---

## Najważniejsze do zapamiętania

- `mypy` statycznie sprawdza zgodność typów.
- Pomaga łapać błędy przed uruchomieniem programu.
- Najlepiej działa razem z adnotacjami z `typing`.
- Uzupełnia testy i linting, ale ich nie zastępuje.
- W nowych projektach warto rozważyć mocniejszą konfigurację.
