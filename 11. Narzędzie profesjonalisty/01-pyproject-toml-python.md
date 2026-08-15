# `pyproject.toml` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co istnieje `pyproject.toml`](#po-co-istnieje-pyprojecttoml)
3. [Dlaczego to centralny plik projektu](#dlaczego-to-centralny-plik-projektu)
4. [Podstawowa struktura](#podstawowa-struktura)
5. [Sekcja `build-system`](#sekcja-build-system)
6. [Sekcja `project`](#sekcja-project)
7. [Zależności runtime i dev](#zależności-runtime-i-dev)
8. [Konfiguracja narzędzi](#konfiguracja-narzędzi)
9. [Przykład pełniejszego pliku](#przykład-pełniejszego-pliku)
10. [Jak czytać taki plik w praktyce](#jak-czytać-taki-plik-w-praktyce)
11. [Typowe błędy początkujących](#typowe-błędy-początkujących)
12. [Praktyczna ściąga](#praktyczna-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

`pyproject.toml` to centralny plik konfiguracyjny nowoczesnego projektu Python.

Bardzo często jest to pierwsze miejsce, do którego zagląda programista w nowym repozytorium.

W jednym miejscu możesz znaleźć:

- metadane projektu,
- zależności,
- sposób budowania,
- konfigurację narzędzi jakościowych.

---

## Po co istnieje `pyproject.toml`

Ten plik porządkuje projekt.

Zamiast trzymać ustawienia w wielu losowych miejscach, możesz mieć jedno główne źródło prawdy.

To pomaga w:

- onboardingu,
- utrzymaniu projektu,
- automatyzacji,
- pracy zespołowej,
- budowaniu pakietów i narzędzi.

---

## Dlaczego to centralny plik projektu

W nowoczesnym workflow wiele rzeczy kręci się wokół `pyproject.toml`.

To tu często trafiają ustawienia dla:

- `ruff`,
- `black`,
- `mypy`,
- `pytest`,
- narzędzi do zarządzania zależnościami.

Dzięki temu zamiast polować na konfigurację po różnych plikach, masz ją w jednym miejscu.

---

## Podstawowa struktura

Minimalny przykład:

```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "moj-projekt"
version = "0.1.0"
description = "Przykladowy projekt Python"
requires-python = ">=3.12"
dependencies = []
```

To już daje podstawowy szkielet nowoczesnego projektu.

---

## Sekcja `build-system`

Ta sekcja mówi, jak projekt ma być budowany.

Przykład:

```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"
```

Najprostsza interpretacja:

- jakie narzędzia są potrzebne do budowy pakietu,
- jaki backend ma obsłużyć budowanie projektu.

W wielu projektach początkujący nie muszą od razu rozumieć wszystkiego o build backendach, ale warto wiedzieć, że ta sekcja istnieje i jest ważna.

---

## Sekcja `project`

To serce opisu projektu.

Przykład:

```toml
[project]
name = "raporty-cli"
version = "0.1.0"
description = "Narzędzie CLI do generowania raportow"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
  "httpx>=0.28",
  "pydantic>=2.0",
]
```

To mówi m.in.:

- jak nazywa się projekt,
- jaką ma wersję,
- jakiej wersji Pythona wymaga,
- jakie ma zależności runtime.

---

## Zależności runtime i dev

To bardzo ważne rozróżnienie.

### Runtime

To biblioteki potrzebne do działania aplikacji.

```toml
dependencies = [
  "httpx>=0.28",
  "pydantic>=2.0",
]
```

### Dev

To narzędzia potrzebne do pracy nad projektem.

```toml
[project.optional-dependencies]
dev = [
  "pytest",
  "ruff",
  "mypy",
]
```

To rozróżnienie pomaga utrzymać porządek.

Nie chcesz mieszać bibliotek runtime z narzędziami developerskimi.

---

## Konfiguracja narzędzi

Jedna z największych zalet `pyproject.toml` to możliwość trzymania ustawień wielu narzędzi w jednym miejscu.

Przykład:

```toml
[tool.ruff]
line-length = 88

[tool.black]
line-length = 88

'target-version' = ['py312']
```

Lepszy, poprawny zapis:

```toml
[tool.black]
line-length = 88
target-version = ["py312"]
```

Przykład dla `pytest`:

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
```

Przykład dla `mypy`:

```toml
[tool.mypy]
python_version = "3.12"
strict = true
```

---

## Przykład pełniejszego pliku

```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "raporty-cli"
version = "0.1.0"
description = "Narzędzie CLI do raportow"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
  "httpx>=0.28",
  "pydantic>=2.0",
]

[project.optional-dependencies]
dev = [
  "pytest",
  "ruff",
  "mypy",
]

[tool.ruff]
line-length = 88

[tool.ruff.lint]
select = ["E", "F", "I"]

[tool.black]
line-length = 88
target-version = ["py312"]

[tool.mypy]
python_version = "3.12"
strict = true

[tool.pytest.ini_options]
testpaths = ["tests"]
```

---

## Jak czytać taki plik w praktyce

Jeśli otwierasz obce repo, patrz kolejno:

1. jaka jest wymagana wersja Pythona,
2. jakie są zależności,
3. czy są osobne zależności dev,
4. jakie są ustawienia lintingu, formatowania i testów,
5. czy konfiguracja jest spójna.

To często daje bardzo szybki obraz dojrzałości projektu.

---

## Typowe błędy początkujących

- brak `requires-python`,
- mieszanie runtime i dev dependencies,
- kopiowanie ogromnych konfiguracji bez zrozumienia,
- rozrzucanie ustawień po wielu plikach bez powodu,
- traktowanie `pyproject.toml` jako magicznego pliku zamiast jako świadomie projektowanej konfiguracji.

---

## Praktyczna ściąga

### Minimalny szkielet

```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "moj-projekt"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = []
```

### Co tam zwykle trafia

- metadane projektu,
- zależności,
- ustawienia narzędzi,
- konfiguracja testów i jakości.

---

## Ćwiczenia

1. Napisz minimalny `pyproject.toml` dla małego projektu.
2. Dodaj `requires-python`.
3. Dodaj dwie zależności runtime.
4. Dodaj grupę `dev` z `pytest`, `ruff`, `mypy`.
5. Dodaj konfigurację `ruff` i `black`.
6. Dodaj konfigurację `pytest` wskazującą katalog `tests`.
7. Wyjaśnij własnymi słowami, dlaczego trzymanie konfiguracji w jednym miejscu jest wygodne.

---

## Najważniejsze do zapamiętania

- `pyproject.toml` to centralny plik nowoczesnego projektu Python.
- Może opisywać zarówno projekt, jak i narzędzia wokół niego.
- Warto rozdzielać zależności runtime i dev.
- Dobrze uporządkowany `pyproject.toml` bardzo poprawia czytelność i powtarzalność projektu.
