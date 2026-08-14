# Kompendium Python — ścieżka nauki

To repozytorium jest ułożone jako pełna ścieżka nauki Pythona: od podstaw języka, przez struktury danych i narzędzia, aż po backend, bazy danych, architekturę i bezpieczeństwo.

Najlepiej czytać katalogi po kolei od `01` do `16`.

Każdy dział ma własny `README.md`, który tłumaczy:

- od czego zacząć,
- co powinieneś umieć po danym dziale,
- co czytać dalej.

---

## Jak korzystać z tego repo

Jeśli uczysz się od zera:

1. Zacznij od `01. Fundamenty`
2. Idź kolejno przez `02`, `03`, `04`...
3. Nie przeskakuj zbyt wcześnie do backendu, baz i architektury bez mocnych podstaw

Jeśli wracasz do tematu:

- używaj tego repo jak mapy i referencji
- wchodź do konkretnego katalogu według obszaru, który chcesz odświeżyć

---

## Pełna ścieżka 01–16

### [01. Fundamenty](/home/kacper/Desktop/Python/01.%20Fundamenty/README.md)

Start całej nauki.

Znajdziesz tu:

- typy danych,
- stringi,
- operatory,
- struktury sterujące,
- `None`,
- truthy/falsy,
- unpacking,
- podstawowe funkcje wbudowane,
- zasięg zmiennych,
- wyjątki.

### [02. Moduły, funkcje i organizacja kodu](/home/kacper/Desktop/Python/02.%20Moduły,%20funkcje%20i%20organizacja%20kodu/README.md)

Przejście od pojedynczych instrukcji do świadomie budowanego kodu.

Znajdziesz tu:

- funkcje,
- `*args` i `**kwargs`,
- `lambda`,
- moduły,
- importy,
- pakiety,
- `if __name__ == "__main__"`,
- organizację projektu.

### [03. Kolekcje](/home/kacper/Desktop/Python/03.%20Kolekcje/README.md)

Praca na danych i strukturach wbudowanych.

Znajdziesz tu:

- listy,
- tuple,
- dict,
- set,
- comprehensions,
- generatory,
- mutowalność,
- kopiowanie,
- `Counter`, `defaultdict`, `deque`, `ChainMap`.

### [04. Programowanie obiektowe](/home/kacper/Desktop/Python/04.%20Programowanie%20obiektowe/README.md)

OOP od podstaw do bardziej zaawansowanych elementów.

Znajdziesz tu:

- klasy i obiekty,
- `__init__`,
- atrybuty,
- hermetyzację,
- dziedziczenie,
- polimorfizm,
- kompozycję,
- magic methods,
- metaklasy.

### [05. Dekoratory](/home/kacper/Desktop/Python/05.%20Dekoratory/README.md)

Najpierw funkcje jako obiekty, potem closures i dekoratory krok po kroku.

Znajdziesz tu:

- closures,
- proste dekoratory,
- dekoratory z argumentami,
- `functools.wraps`,
- dekoratory klasowe,
- dekoratory w frameworkach.

### [06. Zaawansowane elementy](/home/kacper/Desktop/Python/06.%20Zaawansowane%20elementy/README.md)

Tematy bardziej techniczne i pogłębiające rozumienie języka.

Znajdziesz tu:

- iteratory,
- generatory,
- context managery,
- programowanie funkcyjne,
- deskryptory,
- `__slots__`,
- model pamięci CPythona.

### [07. Pliki i dane](/home/kacper/Desktop/Python/07.%20Pliki%20i%20dane/README.md)

Bardzo praktyczny dział o danych i operacjach wejścia/wyjścia.

Znajdziesz tu:

- `open()`,
- `utf-8`,
- pliki binarne,
- `pathlib`,
- `os`,
- `json`,
- `csv`,
- `configparser`,
- XML,
- `sqlite3`.

### [08. Przydatne libki](/home/kacper/Desktop/Python/08.%20Przydatne%20libki/README.md)

Najbardziej praktyczne biblioteki wspierające codzienny kod.

Znajdziesz tu:

- `re`,
- `itertools`,
- `functools`,
- `collections`,
- `typing`,
- `dataclasses`.

### [09. Narzędzia](/home/kacper/Desktop/Python/09.%20Narz%C4%99dzia/README.md)

Warsztat codziennej pracy programisty.

Znajdziesz tu:

- środowiska wirtualne,
- zależności,
- git,
- dokumentowanie kodu,
- logging,
- debugowanie,
- profilowanie,
- `subprocess`.

### [10. Testowanie](/home/kacper/Desktop/Python/10.%20Testowanie/README.md)

Od podstaw testów do technik bardziej profesjonalnych.

Znajdziesz tu:

- podstawy `pytest`,
- zaawansowany `pytest`,
- mocking,
- coverage,
- testy oparte na właściwościach.

### [11. Narzędzie profesjonalisty](/home/kacper/Desktop/Python/11.%20Narz%C4%99dzie%20profesjonalisty/README.md)

Nowoczesny workflow projektu Python.

Znajdziesz tu:

- `pyproject.toml`,
- `ruff`,
- `black`,
- `isort`,
- `pre-commit`,
- `mypy`,
- `poetry`,
- `uv`,
- `Makefile`,
- GitHub Actions,
- `tox`,
- `nox`.

### [12. Asynchroniczność i wielowątkowość](/home/kacper/Desktop/Python/12.%20Asynchroniczno%C5%9B%C4%87%20i%20wielow%C4%85tkowo%C5%9B%C4%87/README.md)

Współbieżność i praca z wieloma zadaniami.

Znajdziesz tu:

- `async` i `await`,
- `asyncio`,
- async HTTP,
- `threading`,
- `multiprocessing`,
- RabbitMQ,
- Celery,
- Kafka.

### [13. Web i API](/home/kacper/Desktop/Python/13.%20Web%20i%20API/README.md)

Wejście w backend i projektowanie API.

Znajdziesz tu:

- HTTP i REST,
- `Pydantic`,
- FastAPI,
- routing,
- dependency injection,
- autoryzację,
- obsługę błędów,
- testowanie API.

### [14. Bazy danych](/home/kacper/Desktop/Python/14.%20Bazy%20danych/README.md)

Warstwa danych backendowego Pythona.

Znajdziesz tu:

- SQL,
- transakcje,
- SQLAlchemy Core,
- SQLAlchemy ORM,
- repozytoria,
- Alembic,
- problem N+1.

### [15. Architektura i jakość kodu](/home/kacper/Desktop/Python/15.%20Architektura%20i%20jako%C5%9B%C4%87%20kodu/README.md)

Dział o tym, jak budować kod, który da się utrzymać i rozwijać.

Znajdziesz tu:

- code smells,
- refaktoryzację,
- architekturę warstwową,
- separację logiki biznesowej,
- dependency injection,
- SOLID,
- wzorce projektowe.

### [16. Bezpieczeństwo](/home/kacper/Desktop/Python/16.%20Bezpiecze%C5%84stwo/README.md)

Końcowy dział spinający bezpieczne myślenie o systemach Python.

Znajdziesz tu:

- podstawy bezpieczeństwa,
- walidację danych,
- sekrety i env vars,
- bezpieczne `subprocess`,
- SQL injection,
- command injection,
- path traversal,
- bezpieczną serializację.

---

## Sugerowany sposób nauki

Najbardziej naturalna ścieżka:

1. `01` -> `02` -> `03`
2. `04` -> `05` -> `06`
3. `07` -> `08` -> `09`
4. `10` -> `11`
5. `12`
6. `13` -> `14`
7. `15` -> `16`

---

## Cel końcowy

Po przejściu całej ścieżki powinieneś mieć bardzo mocną bazę do:

- pisania dobrego kodu Python,
- pracy backendowej,
- budowy API,
- pracy z bazami danych,
- testowania,
- używania profesjonalnych narzędzi,
- rozumienia architektury i bezpieczeństwa.
