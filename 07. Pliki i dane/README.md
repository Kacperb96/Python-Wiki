# 07. Pliki i dane

To jest jeden z najbardziej praktycznych działów w całym Pythonie.

Tutaj wchodzą rzeczy, które naprawdę pojawiają się bardzo często:

- czytanie plików,
- zapisywanie danych,
- obsługa kodowania,
- praca na ścieżkach,
- JSON, CSV, XML,
- konfiguracja,
- prosta baza danych SQLite.

Po przerobieniu tego folderu powinieneś umieć:

- pracować z `open()`,
- rozumieć `utf-8`,
- rozróżniać tekst i bajty,
- używać `pathlib` i `os`,
- pracować z `json`, `csv`, `configparser`, XML,
- korzystać z `sqlite3`,
- pracować z plikami tymczasowymi,
- rozumieć serializację modeli danych do JSON.

## Po co w ogóle ten dział

Bardzo dużo prawdziwych programów nie polega tylko na liczeniu w pamięci.

One muszą:

- odczytać dane z pliku,
- zapisać raport,
- wczytać konfigurację,
- przetworzyć CSV albo JSON,
- znaleźć pliki w katalogach,
- zapisać coś do bazy.

Dlatego ten dział jest mocno „codzienny”.

To nie jest teoria dla teorii.

To są rzeczy, które realnie przydają się w skryptach, aplikacjach, automatyzacji i pracy zawodowej.

## Jak czytać ten dział

Najlepiej iść po kolei:

1. `01-open-read-write-python.md`
2. `02-encoding-utf8-python.md`
3. `03-pliki-binarne-python.md`
4. `04-pathlib-python.md`
5. `05-os-python.md`
6. `06-json-python.md`
7. `07-csv-python.md`
8. `08-configparser-python.md`
9. `09-xml-etree-python.md`
10. `10-sqlite3-python.md`
11. `11-tempfile-python.md`
12. `12-serializacja-modeli-dataclass-enum-json-python.md`

Ta kolejność ma sens, bo:

- najpierw uczysz się podstaw pracy z plikami,
- potem dochodzi kodowanie,
- potem ścieżki i system plików,
- potem formaty danych,
- potem prosta baza danych,
- a na końcu bardziej praktyczne tematy: pliki tymczasowe i serializacja modeli.

## Na co szczególnie uważać

Najczęstsze pułapki w tym dziale:

- zapominanie o `encoding="utf-8"`,
- mylenie tekstu i bajtów,
- używanie złego trybu pliku, np. `r`, `w`, `a`, `rb`, `wb`,
- budowanie ścieżek ręcznie jako stringów zamiast użycia `pathlib`,
- nadpisanie pliku przez przypadek,
- brak obsługi błędów odczytu albo błędnych danych,
- w SQL składanie zapytań stringiem zamiast użycia parametrów.

To jest dział, gdzie bardzo łatwo „napisać coś, co działa u mnie”, ale mniej łatwo napisać coś naprawdę porządnie.

## Po czym poznać, że temat zaczyna siedzieć

Dobry znak, jeśli potrafisz:

- bez stresu otworzyć plik w dobrym trybie,
- odczytać dane tekstowe i binarne,
- wyjaśnić różnicę między `str` i `bytes`,
- używać `Path(...)` zamiast ręcznego sklejania ścieżek,
- zapisać i odczytać JSON oraz CSV,
- użyć `sqlite3` z prostym `SELECT` i `INSERT`,
- przewidzieć, kiedy może wyskoczyć błąd pliku, kodowania albo parsowania.

## Jak najlepiej ćwiczyć

W tym dziale bardzo pomaga praktyka „mały plik -> mały skrypt -> wynik”.

Najlepszy rytm nauki:

1. utwórz mały plik testowy,
2. napisz krótki kod,
3. zobacz wynik,
4. celowo zepsuj coś i zobacz błąd,
5. popraw kod tak, by był odporniejszy.

To szczególnie pomaga przy:

- kodowaniu,
- JSON i CSV,
- ścieżkach,
- SQLite,
- plikach binarnych.

## Uczciwa ocena startowa tego folderu

Na ten moment ten dział ma dobry zakres tematów i sensowną strukturę, ale jeszcze nie ma poziomu dopracowania folderów `05` i `06`.

Najbardziej brakuje tu:

- mocniejszego `README`,
- większego zestawu ćwiczeń,
- większej liczby przykładów z outputem,
- większej liczby scenariuszy praktycznych i typowych błędów.

To jest dobry fundament, ale jeszcze nie końcowy poziom.

Co dalej:

- po dopracowaniu tego działu można spokojnie przejść do `08. Przydatne libki`,
- albo do `09. Narzędzia`, jeśli chcesz iść bardziej w stronę pracy profesjonalnej.
