# `pyproject.toml` — zaawansowanie w Pythonie

## O co chodzi z `pyproject.toml`

`pyproject.toml` to dziś centralny plik konfiguracyjny nowoczesnego projektu Python.

To tutaj bardzo często opisujesz:

- metadata projektu,
- zależności,
- backend builda,
- konfigurację narzędzi,
- wymagania wersji Pythona,
- entry points,
- extras.

To jeden z najważniejszych plików w bardziej dojrzałym projekcie.

## Dlaczego ten plik jest tak ważny

Dawniej konfiguracja projektu była porozrzucana po wielu miejscach:

- `setup.py`,
- `setup.cfg`,
- `requirements.txt`,
- osobne pliki dla narzędzi.

Nowoczesny Python mocno przeszedł w kierunku jednego, bardziej uporządkowanego punktu konfiguracji.

`pyproject.toml` nie rozwiązuje wszystkiego automatycznie, ale bardzo porządkuje projekt.

## Minimalny przykład

```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "moj-projekt"
version = "0.1.0"
description = "Przykladowa paczka Python"
readme = "README.md"
requires-python = ">=3.11"
dependencies = []
```

To już jest sensowny start.

## Co oznacza `[build-system]`

Ta sekcja mówi, jak budować projekt.

Przykład:

```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"
```

Znaczenie:

- `requires` — jakie narzędzia są potrzebne do builda,
- `build-backend` — jaki backend realizuje build.

To nie są zwykłe zależności runtime. To zależności potrzebne do samego procesu budowy paczki.

## Co oznacza `[project]`

To sekcja z metadanymi projektu.

Najczęściej trafiają tu:

- `name`,
- `version`,
- `description`,
- `readme`,
- `requires-python`,
- `dependencies`,
- `authors`,
- `license`,
- `classifiers`.

## Ważne pola praktyczne

### `name`

Nazwa paczki publikowanej i instalowanej.

```toml
name = "moj-projekt"
```

### `version`

Wersja projektu.

```toml
version = "0.1.0"
```

### `requires-python`

Jedno z najważniejszych pól.

```toml
requires-python = ">=3.11"
```

To mówi użytkownikowi i narzędziom, jaka wersja Pythona jest wspierana.

### `dependencies`

Zależności runtime.

```toml
dependencies = [
  "requests>=2.32",
  "pydantic>=2.0",
]
```

To są pakiety potrzebne do działania projektu, a nie do developmentu lokalnego.

## Przykład bardziej praktyczny

```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "text-tools"
version = "0.1.0"
description = "Narzedzia do pracy z tekstem"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
  "click>=8.1",
]

[project.optional-dependencies]
dev = [
  "pytest>=8.0",
  "ruff>=0.6",
]
```

Tu już widać projekt, który:

- ma zależność runtime,
- ma osobne zależności developerskie,
- ma jasno określoną wersję Pythona.

## `pyproject.toml` a konfiguracja narzędzi

W tym samym pliku często trzyma się też konfigurację narzędzi, np.:

- Ruff,
- Black,
- pytest,
- mypy,
- coverage.

Przykład:

```toml
[tool.ruff]
line-length = 88

[tool.pytest.ini_options]
addopts = "-q"
```

To bardzo wygodne, bo projekt ma mniej rozproszonych plików konfiguracyjnych.

## Kiedy to ma sens

`pyproject.toml` ma sens praktycznie zawsze, gdy projekt:

- ma być instalowalny,
- ma mieć zależności,
- ma być budowany jako paczka,
- ma korzystać z nowoczesnego tooling-u.

W małych skryptach jednoplikowych to nie zawsze jest konieczne, ale od pewnego poziomu staje się naturalnym standardem.

## Czego nie mieszać

Bardzo ważne rozróżnienie:

- zależności runtime,
- zależności dev,
- zależności builda.

To są różne rzeczy.

### Runtime

Potrzebne użytkownikowi do działania projektu.

### Dev

Potrzebne Tobie do pracy nad projektem.

### Build-system

Potrzebne do zbudowania paczki.

Mylenie tych warstw robi szybko bałagan.

## Typowe błędy początkujących

- brak `requires-python`,
- wrzucanie wszystkich narzędzi do `dependencies`,
- brak rozróżnienia extras i runtime,
- kopiowanie cudzych konfiguracji bez rozumienia,
- nieaktualne lub sprzeczne pola metadanych,
- traktowanie `pyproject.toml` jak magicznego pliku, który sam wszystko załatwia.

## `pyproject.toml` vs stary styl

Dobrze znać historyczny kontekst, ale w nowym kodzie najczęściej warto iść w nowoczesne podejście.

Nie znaczy to, że starsze projekty są złe. Po prostu będziesz jeszcze spotykał repo, które opierają się bardziej na `setup.py` lub `setup.cfg`.

## Mini checklista dobrego `pyproject.toml`

- Czy projekt ma nazwę?
- Czy ma wersję?
- Czy ma `requires-python`?
- Czy runtime dependencies są oddzielone od dev tools?
- Czy build backend jest jawnie określony?
- Czy konfiguracja narzędzi jest spójna?

## Szybka ściąga

Najważniejsze sekcje:

- `[build-system]`
- `[project]`
- `[project.optional-dependencies]`
- `[tool.<nazwa_narzedzia>]`

## Ćwiczenia

1. Napisz minimalny `pyproject.toml` dla małego projektu.
2. Dodaj `requires-python` i dwie zależności runtime.
3. Dodaj sekcję `dev` w optional dependencies.
4. Dodaj prostą konfigurację Ruff albo pytest.
5. Wskaż, które pola są naprawdę obowiązkowe, a które tylko bardzo przydatne.

## Najważniejsze do zapamiętania

- `pyproject.toml` to dziś centralny plik konfiguracji nowoczesnego projektu Python.
- Łączy metadata projektu, build i często konfigurację narzędzi.
- Trzeba rozróżniać build, runtime i dev dependencies.
- `requires-python` to jedno z najważniejszych pól praktycznych.
- Dobry `pyproject.toml` porządkuje projekt i ułatwia jego dalszy rozwój.
