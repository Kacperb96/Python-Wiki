# `black` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `black`](#czym-jest-black)
3. [Po co używać formattera](#po-co-używać-formattera)
4. [Jak działa `black`](#jak-działa-black)
5. [Podstawowe komendy](#podstawowe-komendy)
6. [Przykład przed i po](#przykład-przed-i-po)
7. [Konfiguracja](#konfiguracja)
8. [Relacja z `ruff`](#relacja-z-ruff)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczna ściąga](#praktyczna-ściąga)
11. [Ćwiczenia](#ćwiczenia)
12. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

`black` to automatyczny formatter kodu Python.

Jego główny cel jest prosty:

usunąć spory o styl i zapewnić jednolity wygląd kodu w całym projekcie.

---

## Czym jest `black`

To narzędzie, które bierze kod i formatuje go według jasno określonych zasad.

Najważniejsze jest to, że nie zostawia zbyt dużo miejsca na ręczne dyskusje typu:

- gdzie złamać linię,
- ile spacji wstawić,
- jak ustawić nawiasy.

To właśnie jest jego siła.

---

## Po co używać formattera

Formatter pomaga:

- utrzymać spójny styl,
- skrócić code review,
- zmniejszyć liczbę kosmetycznych poprawek,
- skupić uwagę na logice zamiast na wyglądzie kodu.

W zespole to bardzo duża oszczędność czasu.

---

## Jak działa `black`

Najczęściej po prostu uruchamiasz go na pliku albo całym projekcie.

Efekt:

- długie linie są łamane według reguł,
- odstępy są porządkowane,
- kod wygląda jednolicie.

---

## Podstawowe komendy

Sprawdzenie i formatowanie projektu:

```bash
black .
```

Sprawdzenie bez zapisu zmian:

```bash
black . --check
```

To drugie jest bardzo przydatne w CI.

---

## Przykład przed i po

### Przed

```python
def dodaj( a,b ): return a+b
```

### Po

```python
def dodaj(a, b):
    return a + b
```

Przykładowy output `black . --check` przy niepoprawnym formacie:

```text
would reformat app.py

Oh no! 💥 💔 💥
1 file would be reformatted.
```

Przykładowy output po realnym formatowaniu:

```text
reformatted app.py

All done! ✨ 🍰 ✨
1 file reformatted.
```

---

## Konfiguracja

Najczęściej w `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ["py312"]
```

Zwykle konfiguracja `black` jest mała, bo narzędzie celowo ogranicza liczbę opcji.

To też jest zaleta.

---

## Relacja z `ruff`

Bardzo częsty duet:

- `black` formatuje kod,
- `ruff` pilnuje jakości i części reguł stylistycznych.

W części projektów rolę formatowania może przejąć `ruff format`, ale warto rozumieć klasyczny model z `black`, bo nadal jest bardzo popularny.

---

## Typowe błędy początkujących

- ręczne poprawianie stylu zamiast użycia formattera,
- kłócenie się z narzędziem o drobiazgi,
- brak spójnego formattera w całym zespole,
- mieszanie kilku formatterów bez planu.

---

## Praktyczna ściąga

### Formatowanie

```bash
black .
```

### Tylko sprawdzenie

```bash
black . --check
```

### Minimalna konfiguracja

```toml
[tool.black]
line-length = 88
target-version = ["py312"]
```

---

## Ćwiczenia

1. Przygotuj celowo brzydko zapisany fragment kodu i przepuść go przez `black`.
2. Uruchom `black . --check` i zobacz, co zgłasza.
3. Dodaj minimalną konfigurację `black` do `pyproject.toml`.
4. Wyjaśnij własnymi słowami, czemu formatter skraca code review.
5. Porównaj rolę `black` i `ruff`.

---

## Najważniejsze do zapamiętania

- `black` automatycznie formatuje kod.
- Jego celem jest spójność, a nie dyskusja o stylu.
- Dobrze działa lokalnie, w `pre-commit` i w CI.
- Współpracuje z `ruff`, ale ma inną główną rolę.
