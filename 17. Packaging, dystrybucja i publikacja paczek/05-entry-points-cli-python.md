# Entry points i CLI w Pythonie

## O co chodzi

Nie każda paczka Python ma być tylko biblioteką importowaną w kodzie.

Część projektów ma być uruchamiana jako komenda w terminalu.

Właśnie tu wchodzą entry points, które pozwalają z paczki zrobić wygodne CLI.

## Biblioteka vs CLI

### Biblioteka

Użytkownik robi coś w stylu:

```python
from text_tools import clean_text
```

### CLI

Użytkownik robi coś w stylu:

```bash
text-tools --input dane.txt
```

Oba modele są wartościowe. Czasem jedna paczka wspiera oba jednocześnie.

## Co to jest entry point

To deklaracja mówiąca, że po instalacji paczki ma powstać komenda terminalowa, która wywołuje konkretną funkcję Pythona.

Przykład w `pyproject.toml`:

```toml
[project.scripts]
text-tools = "text_tools.cli:main"
```

To oznacza:

- komenda użytkownika: `text-tools`,
- moduł: `text_tools.cli`,
- funkcja startowa: `main`.

## Przykładowa implementacja

Plik `text_tools/cli.py`:

```python
def main() -> None:
    print("Uruchomiono CLI")
```

Po instalacji użytkownik może odpalić:

```bash
text-tools
```

Przykładowy output:

```text
Uruchomiono CLI
```

## Dlaczego to jest lepsze niż ręczne skrypty

Entry points są wygodne, bo:

- instalują się razem z paczką,
- są standardowym mechanizmem,
- nie trzeba ręcznie kopiować plików wykonywalnych,
- użytkownik dostaje naturalną komendę.

## `python -m` a entry point

To dwa różne style uruchamiania.

### `python -m`

```bash
python -m text_tools
```

Dobre, gdy:

- chcesz uruchomić moduł jako program,
- nie potrzebujesz osobnej nazwy komendy,
- projekt jest bardziej developerski.

### Entry point CLI

```bash
text-tools
```

Dobre, gdy:

- chcesz wygodnego narzędzia dla użytkownika końcowego,
- paczka ma działać jak pełnoprawna komenda.

## Jak wygląda sensowny punkt startowy

Funkcja `main()` powinna zwykle:

- przyjąć argumenty,
- uruchomić logikę aplikacji,
- być możliwie cienka,
- nie zawierać całego świata w jednym miejscu.

Lepszy styl:

- `main()` odpowiada za wejście,
- logika biznesowa siedzi w innych funkcjach/modułach.

## Przykład prostego CLI

```python
import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    args = parser.parse_args()
    print(f"Witaj {args.name}")
```

Uruchomienie:

```bash
text-tools Jan
```

Output:

```text
Witaj Jan
```

## Kiedy to ma sens

Entry points mają sens, gdy tworzysz:

- narzędzie terminalowe,
- generator plików,
- migrator danych,
- mini util do codziennej pracy,
- bibliotekę, która ma też tryb CLI.

Nie musisz robić CLI do każdej paczki. Ale warto umieć to zrobić porządnie.

## Typowe błędy początkujących

- zbyt gruba funkcja `main()`,
- mieszanie logiki aplikacji z parsowaniem argumentów,
- brak obsługi błędów w CLI,
- niejasna nazwa komendy,
- brak `--help` albo słabe komunikaty dla użytkownika.

## Mini checklista CLI

- Czy nazwa komendy jest sensowna?
- Czy `main()` jest cienka?
- Czy argumenty są czytelne?
- Czy użytkownik ma sensowny `--help`?
- Czy błędy są zrozumiałe?

## Szybka ściąga

- `[project.scripts]` — deklaracja komend,
- `nazwa = "modul:fukcja"` — mapowanie komendy na funkcję,
- CLI powinno być cienką warstwą wejścia,
- logika powinna siedzieć głębiej w kodzie.

## Ćwiczenia

1. Zrób prostą komendę `hello-name` przez entry point.
2. Dodaj argument pozycyjny do CLI.
3. Dodaj `--help`.
4. Rozdziel warstwę CLI od właściwej logiki.
5. Porównaj `python -m` i entry point dla małego projektu.

## Najważniejsze do zapamiętania

- Entry points pozwalają z paczki zrobić wygodne CLI.
- Użytkownik dostaje komendę terminalową instalowaną razem z projektem.
- Dobrze zaprojektowane CLI ma cienką warstwę wejścia.
- `python -m` i entry points rozwiązują podobne, ale nie identyczne potrzeby.
- Nie każda paczka musi być CLI, ale warto znać ten mechanizm.
