# `argparse` w Pythonie

## Wprowadzenie

`argparse` służy do budowania programów uruchamianych z terminala z argumentami i opcjami.

To bardzo praktyczne, gdy chcesz zrobić:

- skrypt do analizy pliku,
- prosty importer danych,
- narzędzie administracyjne,
- mini CLI do projektu,
- program wywoływany w pipeline albo cronie.

Bez `argparse` początkujący często robią coś takiego:

```python
import sys

filename = sys.argv[1]
```

To działa tylko w najprostszym przypadku i szybko robi się kruche.

## Najprostszy przykład

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name")

args = parser.parse_args()
print(f"Witaj {args.name}")
```

Uruchomienie:

```bash
python app.py Anna
```

Output:

```text
Witaj Anna
```

## Co daje `argparse`

Największe plusy:

- automatyczne parsowanie argumentów,
- automatyczne `--help`,
- lepsze komunikaty błędów,
- jawny opis interfejsu programu,
- obsługa flag, opcji i wartości domyślnych.

## `--help`

To jedna z największych zalet.

Jeśli masz:

```python
import argparse

parser = argparse.ArgumentParser(description="Prosty kalkulator")
parser.add_argument("x", type=int)
parser.add_argument("y", type=int)

args = parser.parse_args()
print(args.x + args.y)
```

to:

```bash
python app.py --help
```

da output w stylu:

```text
usage: app.py [-h] x y

Prosty kalkulator

positional arguments:
  x
  y

options:
  -h, --help  show this help message and exit
```

## Argumenty pozycyjne

To argumenty wymagane według pozycji:

```python
parser.add_argument("input_file")
parser.add_argument("output_file")
```

Przykład użycia:

```bash
python app.py input.csv output.json
```

## Opcje nazwane

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, default=8000)

args = parser.parse_args()
print(args.port)
```

Uruchomienie bez opcji:

```bash
python app.py
```

Output:

```text
8000
```

Uruchomienie z opcją:

```bash
python app.py --port 9000
```

Output:

```text
9000
```

## Flagi logiczne

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--debug", action="store_true")

args = parser.parse_args()
print(args.debug)
```

Uruchomienie:

```bash
python app.py
```

Output:

```text
False
```

Uruchomienie:

```bash
python app.py --debug
```

Output:

```text
True
```

## Typy argumentów

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--workers", type=int, default=4)

args = parser.parse_args()
print(args.workers)
```

Jeśli użytkownik poda zły typ:

```bash
python app.py --workers abc
```

Output w stylu:

```text
error: argument --workers: invalid int value: 'abc'
```

To bardzo wygodne, bo nie musisz wszystkiego ręcznie walidować od zera.

## `choices`

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--mode", choices=["dev", "prod"], default="dev")

args = parser.parse_args()
print(args.mode)
```

Uruchomienie:

```bash
python app.py --mode prod
```

Output:

```text
prod
```

Zły wybór:

```bash
python app.py --mode test
```

Output w stylu:

```text
error: argument --mode: invalid choice: 'test' (choose from 'dev', 'prod')
```

## Własne nazwy i pomoc

```python
import argparse

parser = argparse.ArgumentParser(description="Importer CSV do JSON")
parser.add_argument("input_file", help="Ścieżka do pliku wejściowego CSV")
parser.add_argument("--pretty", action="store_true", help="Ładne formatowanie JSON")
```

To od razu poprawia używalność programu.

## Mini case study: prosty analizator pliku

```python
import argparse

parser = argparse.ArgumentParser(description="Policz linie w pliku")
parser.add_argument("path")
parser.add_argument("--show-empty", action="store_true")

args = parser.parse_args()

with open(args.path, encoding="utf-8") as f:
    lines = f.readlines()

if args.show_empty:
    print(len(lines))
else:
    print(sum(1 for line in lines if line.strip()))
```

Przykład:

```bash
python app.py notes.txt
```

Output:

```text
12
```

## `argparse` vs ręczne `sys.argv`

### `sys.argv`

Lepsze tylko wtedy, gdy:

- skrypt jest bardzo mały,
- ma 1 prosty argument,
- chcesz pokazać absolutne minimum.

### `argparse`

Lepsze, gdy:

- program ma być używalny,
- ma opcje i flagi,
- chcesz sensowne błędy i `--help`,
- budujesz CLI trochę bardziej na serio.

## Typowe błędy początkujących

### 1. Ręczne parsowanie wszystkiego przez `sys.argv`

Da się, ale szybko robi się nieczytelne.

### 2. Brak `type=...`

Wtedy wszystkie wartości trafiają jako stringi i później kod robi się bardziej kruchy.

### 3. Brak `help`

Program działa, ale jest mało przyjazny dla użytkownika.

### 4. Zbyt wiele argumentów bez sensownej struktury

Jeśli CLI robi się duże, trzeba myśleć też o organizacji komend i subkomend.

## Dobre praktyki

- dodawaj `description`,
- dodawaj `help`,
- używaj `type=...`,
- używaj `choices`, gdy zestaw wartości jest zamknięty,
- dawaj sensowne wartości domyślne,
- nie buduj chaotycznego interfejsu CLI.

## Szybka ściąga

Najczęściej przydatne:

- `ArgumentParser()`
- `add_argument()`
- `parse_args()`
- `action="store_true"`
- `type=int`
- `default=...`
- `choices=[...]`

## Zadania

1. Zbuduj prosty program przyjmujący imię jako argument pozycyjny.
2. Dodaj opcję `--port` z wartością domyślną.
3. Dodaj flagę `--debug`.
4. Dodaj `choices` dla trybu `dev/prod`.
5. Napisz mini CLI, które liczy linie w pliku.
