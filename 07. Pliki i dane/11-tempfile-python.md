# `tempfile` w Pythonie

## Wprowadzenie

`tempfile` służy do bezpiecznej pracy z plikami i katalogami tymczasowymi.

To bardzo praktyczne, gdy:

- tworzysz plik "na chwilę",
- przetwarzasz dane pośrednie,
- piszesz testy,
- generujesz raport, który zaraz znika,
- chcesz uniknąć ręcznego zarządzania dziwnymi nazwami typu `tmp123.txt`.

## Dlaczego nie robić tego ręcznie

Początkujący często piszą coś takiego:

```python
path = "/tmp/moj_plik.txt"
```

Problem:

- nazwa może kolidować z innym procesem,
- plik może już istnieć,
- łatwo zrobić bałagan,
- sprzątanie po sobie bywa zapomniane.

## Najprostszy plik tymczasowy

```python
import tempfile

with tempfile.TemporaryFile(mode="w+t", encoding="utf-8") as f:
    f.write("Hello")
    f.seek(0)
    print(f.read())
```

Output:

```text
Hello
```

To plik tymczasowy, który żyje tylko w czasie działania bloku.

## `NamedTemporaryFile`

Czasem potrzebujesz prawdziwej ścieżki do pliku.

```python
import tempfile

with tempfile.NamedTemporaryFile(mode="w+t", encoding="utf-8") as f:
    print(f.name)
    f.write("test")
    f.seek(0)
    print(f.read())
```

Output w stylu:

```text
/tmp/tmpabcd1234
test
```

To bardzo wygodne, gdy inna część programu albo biblioteka oczekuje ścieżki pliku.

## Katalog tymczasowy

```python
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as tmpdir:
    path = Path(tmpdir) / "report.txt"
    path.write_text("raport", encoding="utf-8")
    print(path.exists())
    print(path.read_text(encoding="utf-8"))
```

Output:

```text
True
raport
```

Po wyjściu z bloku katalog tymczasowy znika.

## Po co to jest tak przydatne w testach

W testach bardzo często chcesz:

- utworzyć plik,
- zapisać coś,
- uruchomić funkcję,
- sprawdzić wynik,
- i nie zostawić śmieci na dysku.

`tempfile` świetnie to rozwiązuje.

## Mini case study: konwersja pliku

Załóżmy, że:

- pobierasz dane,
- zapisujesz wynik pośredni do pliku,
- przetwarzasz go,
- a potem nie chcesz, żeby ten plik został na dysku na zawsze.

Właśnie tu `tempfile` ma bardzo sens.

## Typowe błędy początkujących

### 1. Ręczne nazwy w `/tmp`

To bywa kruche i niepotrzebnie ryzykowne.

### 2. Brak sprzątania

Po kilku uruchomieniach zostają śmieciowe pliki.

### 3. Mylenie pliku tymczasowego z trwałym plikiem projektu

Plik tymczasowy ma zwykle żyć krótko.

## Dobre praktyki

- używaj `with`,
- używaj `TemporaryDirectory()` do całych katalogów roboczych,
- używaj `NamedTemporaryFile`, gdy potrzebujesz ścieżki,
- nie zapisuj trwałych danych w `tempfile`, jeśli mają przetrwać.

## Zadania

1. Utwórz plik tymczasowy i zapisz do niego tekst.
2. Użyj `NamedTemporaryFile` i wypisz jego ścieżkę.
3. Utwórz katalog tymczasowy i zapisz tam plik przez `pathlib`.
4. Opisz, czemu `tempfile` jest lepsze niż ręczne `"/tmp/moj_plik.txt"`.
