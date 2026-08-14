# `pyproject.toml` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co istnieje `pyproject.toml`](#po-co-istnieje-pyprojecttoml)
3. [Co zwykle trafia do `pyproject.toml`](#co-zwykle-trafia-do-pyprojecttoml)
4. [Minimalny przykład](#minimalny-przykład)
5. [Metadane projektu](#metadane-projektu)
6. [Zależności](#zależności)
7. [Konfiguracja narzędzi](#konfiguracja-narzędzi)
8. [Dlaczego to ważne zawodowo](#dlaczego-to-ważne-zawodowo)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczne przykłady](#praktyczne-przykłady)
11. [Dobre praktyki](#dobre-praktyki)
12. [Podsumowanie](#podsumowanie)
13. [Mini ściąga](#mini-ściąga)
14. [Ćwiczenia](#ćwiczenia)
15. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`pyproject.toml` to centralny plik konfiguracyjny nowoczesnego projektu Python.

W praktyce bardzo często jest to pierwsze miejsce, do którego zagląda profesjonalista w nowym repozytorium.

---

## Po co istnieje `pyproject.toml`

Ten plik porządkuje projekt w jednym miejscu.

Może opisywać:

- metadane pakietu,
- zależności,
- backend budowania,
- konfigurację narzędzi takich jak `ruff`, `black`, `mypy`, `pytest`.

---

## Co zwykle trafia do `pyproject.toml`

Najczęściej:

- nazwa projektu,
- wersja,
- wymagany Python,
- dependencies,
- opcjonalne dependencies,
- ustawienia narzędzi developerskich.

---

## Minimalny przykład

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

---

## Metadane projektu

Sekcja `[project]` opisuje pakiet.

Przykład:

```toml
[project]
name = "moj-projekt"
version = "0.1.0"
description = "Narzędzie CLI do raportów"
readme = "README.md"
requires-python = ">=3.12"
```

To ważne przy budowaniu, publikacji i utrzymaniu projektu.

---

## Zależności

Możesz opisać biblioteki potrzebne aplikacji:

```toml
[project]
dependencies = [
  "httpx>=0.28",
  "pydantic>=2.0",
]
```

Opcjonalne zestawy:

```toml
[project.optional-dependencies]
dev = [
  "pytest",
  "ruff",
  "mypy",
]
```

---

## Konfiguracja narzędzi

To jedna z największych zalet `pyproject.toml`.

Przykład:

```toml
[tool.ruff]
line-length = 88

[tool.pytest.ini_options]
testpaths = ["tests"]
```

Dzięki temu konfiguracja projektu nie jest rozrzucona po wielu plikach bez potrzeby.

---

## Dlaczego to ważne zawodowo

W zawodowych projektach liczy się:

- powtarzalność,
- czytelna konfiguracja,
- łatwe onboardowanie,
- jedno źródło prawdy dla narzędzi.

`pyproject.toml` bardzo w tym pomaga.

---

## Typowe błędy początkujących

- trzymanie konfiguracji w wielu przypadkowych plikach bez planu,
- brak sekcji `requires-python`,
- mieszanie zależności produkcyjnych i developerskich,
- kopiowanie konfiguracji bez rozumienia.

---

## Praktyczne przykłady

### Projekt aplikacyjny

```toml
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "api-service"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
  "fastapi",
  "uvicorn",
]

[project.optional-dependencies]
dev = ["pytest", "ruff", "mypy"]
```

### Konfiguracja narzędzi

```toml
[tool.ruff]
line-length = 100

[tool.mypy]
python_version = "3.12"
strict = true
```

---

## Dobre praktyki

- traktuj `pyproject.toml` jako centrum konfiguracji projektu,
- rozdzielaj zależności runtime od `dev`,
- jawnie ustawiaj wersję Pythona,
- konfiguruj tu narzędzia, jeśli to wspierają.

---

## Podsumowanie

`pyproject.toml` to jeden z najważniejszych plików nowoczesnego projektu Python.

Jeśli chcesz pracować profesjonalnie, musisz swobodnie rozumieć jego rolę i podstawową strukturę.

---

## Mini ściąga

```toml
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "app"
version = "0.1.0"
requires-python = ">=3.12"
```

Najważniejsze:

- `[build-system]` mówi, jak budować projekt,
- `[project]` opisuje pakiet,
- `[tool.*]` służy do konfiguracji narzędzi.

---

## Ćwiczenia

1. Napisz minimalny `pyproject.toml` dla prostego projektu.
2. Dodaj `requires-python`.
3. Dodaj zależność `httpx`.
4. Dodaj grupę `dev` z `pytest` i `ruff`.
5. Dodaj prostą konfigurację `mypy`.

---

## Przykładowe rozwiązania

### 1. Minimalny plik

```toml
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "demo"
version = "0.1.0"
```

### 2. Wersja Pythona

```toml
[project]
requires-python = ">=3.12"
```

### 3. Zależność

```toml
[project]
dependencies = ["httpx>=0.28"]
```

### 4. `dev`

```toml
[project.optional-dependencies]
dev = ["pytest", "ruff"]
```

### 5. `mypy`

```toml
[tool.mypy]
strict = true
```
