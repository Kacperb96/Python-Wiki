# Organizacja projektu Python

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co organizować projekt](#po-co-organizować-projekt)
3. [Typowe elementy projektu](#typowe-elementy-projektu)
4. [Kod aplikacji, testy i konfiguracja](#kod-aplikacji-testy-i-konfiguracja)
5. [Rola `README.md` i `pyproject.toml`](#rola-readmemd-i-pyprojecttoml)
6. [Przykładowa struktura](#przykładowa-struktura)
7. [Jak unikać chaosu](#jak-unikać-chaosu)
8. [Jak podzielić mały projekt na pliki](#jak-podzielić-mały-projekt-na-pliki)
9. [Granice odpowiedzialności modułów](#granice-odpowiedzialności-modułów)
10. [Kiedy projekt jest za bardzo rozdrobniony](#kiedy-projekt-jest-za-bardzo-rozdrobniony)
11. [Typowe pułapki początkujących](#typowe-pułapki-początkujących)
12. [Praktyczne przykłady](#praktyczne-przykłady)
13. [Dobre praktyki](#dobre-praktyki)
14. [Podsumowanie](#podsumowanie)
15. [Mini ściąga](#mini-ściąga)
16. [Ćwiczenia](#ćwiczenia)
17. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Dobra organizacja projektu odróżnia jednorazowy skrypt od kodu, który da się rozwijać.

Nawet mały projekt zyskuje, gdy:

- pliki mają sensowny podział,
- wiadomo, gdzie jest logika,
- wiadomo, gdzie są testy,
- wiadomo, jak uruchomić program.

To nie jest temat tylko dla dużych firmowych repozytoriów. Dobre nawyki organizacyjne są przydatne już od bardzo małych projektów.

---

## Po co organizować projekt

Bo uporządkowany projekt:

- łatwiej rozwijać,
- łatwiej testować,
- łatwiej czytać po czasie,
- łatwiej przekazać komuś innemu.

To nie jest formalność. To realna oszczędność czasu.

---

## Typowe elementy projektu

W praktyce często znajdziesz:

- katalog z kodem aplikacji,
- katalog `tests`,
- `README.md`,
- `pyproject.toml`,
- `.gitignore`.

Na tym etapie wystarczy dobrze rozumieć rolę tych elementów.

---

## Kod aplikacji, testy i konfiguracja

Warto oddzielać:

- kod produkcyjny,
- testy,
- konfigurację narzędzi,
- pliki pomocnicze.

Nie mieszaj wszystkiego w jednym katalogu bez struktury.

Dobry projekt nie musi być duży. Ma być czytelny.

---

## Rola `README.md` i `pyproject.toml`

`README.md`:

- tłumaczy, czym jest projekt,
- mówi jak go uruchomić,
- daje szybki onboarding.

`pyproject.toml`:

- zbiera konfigurację projektu i narzędzi,
- wróci mocniej w dalszych działach.

Jeśli ktoś wchodzi do repo po raz pierwszy, `README.md` jest jego pierwszym przewodnikiem.

---

## Przykładowa struktura

```text
my_project/
    README.md
    app/
        __init__.py
        main.py
        utils.py
    tests/
        test_utils.py
```

To już dużo lepszy punkt wyjścia niż jeden ogromny plik ze wszystkim.

---

## Jak unikać chaosu

Najważniejsze zasady:

- rozdzielaj odpowiedzialności,
- nie trzymaj całej logiki w `main.py`,
- grupuj powiązane rzeczy razem,
- nie twórz zbyt wielu plików bez potrzeby,
- ale też nie pakuj wszystkiego do jednego modułu.

To zawsze szukanie sensownego środka.

---

## Jak podzielić mały projekt na pliki

Dobry pierwszy podział wygląda zwykle tak:

- `main.py` albo `cli.py` do uruchamiania programu,
- `validators.py` do walidacji,
- `storage.py` do pracy z danymi,
- `utils.py` tylko wtedy, gdy naprawdę są tam małe, wspólne funkcje,
- `tests/` na testy.

W praktyce warto zadawać sobie pytanie:

"czy ten plik ma jedną główną odpowiedzialność?"

Jeśli odpowiedź brzmi "robi trochę wszystkiego", to zwykle znak, że struktura wymaga poprawy.

---

## Granice odpowiedzialności modułów

Przykład sensownego podziału:

- `main.py` uruchamia program,
- `validators.py` sprawdza dane,
- `storage.py` zapisuje i odczytuje dane,
- `users.py` zawiera logikę użytkowników.

Przykład słabego podziału:

- `main.py` pobiera dane,
- waliduje,
- zapisuje do pliku,
- liczy wyniki,
- drukuje raport,
- obsługuje wszystkie komendy.

To działa na początku, ale bardzo źle się rozwija.

---

## Kiedy projekt jest za bardzo rozdrobniony

To też ważna pułapka.

Nie każdy projekt musi mieć:

- 12 katalogów,
- 20 modułów,
- 8 poziomów zagnieżdżenia.

Jeśli projekt ma 100 linijek, to zbyt agresywna architektura może tylko utrudniać życie.

Dobra organizacja to nie maksymalna liczba plików. To sensowny podział.

---

## Typowe pułapki początkujących

- jeden plik z całym projektem,
- brak katalogu `tests`,
- brak `README.md`,
- nazwy plików, które nic nie mówią,
- mieszanie kodu startowego, logiki i danych w jednym miejscu,
- zbyt szybkie przejście z jednego pliku do nadmiernie rozdrobnionej struktury.

---

## Praktyczne przykłady

### Mini aplikacja

```text
task_manager/
    README.md
    app/
        __init__.py
        main.py
        storage.py
        validators.py
    tests/
        test_validators.py
```

Taka struktura już daje porządek:

- `main.py` uruchamia program,
- `storage.py` trzyma logikę zapisu lub danych,
- `validators.py` trzyma walidację,
- `tests/` to miejsce na testy.

### Zły przykład

```text
project/
    everything.py
```

albo z drugiej strony:

```text
project/
    app/
        core/
            services/
                helpers/
                    misc/
```

gdy projekt jest mikroskopijny.

---

## Dobre praktyki

- zaczynaj od prostej struktury,
- rozdzielaj logikę od punktu wejścia,
- utrzymuj czytelne nazwy plików i katalogów,
- dodawaj `README.md` nawet do małych projektów ćwiczeniowych,
- rozwijaj strukturę wraz z rozwojem projektu, nie na ślepo z góry,
- traktuj strukturę katalogów jako narzędzie do czytelności, a nie ozdobę.

---

## Podsumowanie

Organizacja projektu nie jest dodatkiem. To część jakości kodu.

Jeśli od początku uczysz się porządku, później dużo łatwiej wejść w prawdziwe projekty.

Najważniejsze pytanie brzmi nie:

"ile mam plików?"

tylko:

"czy łatwo znaleźć, gdzie jest dana odpowiedzialność?"

---

## Mini ściąga

```text
project/
    README.md
    app/
        __init__.py
        main.py
    tests/
```

Najważniejsze:

- rozdzielaj kod, testy i konfigurację,
- nie wrzucaj wszystkiego do jednego pliku,
- dbaj o czytelny punkt wejścia programu,
- nie rozdrabniaj projektu bardziej, niż wymaga tego jego skala.

---

## Ćwiczenia

1. Zrób prostą strukturę projektu z `app/`, `tests/`, `README.md`.
2. Przenieś walidację do osobnego modułu.
3. Zbuduj mały CLI z funkcją `main()`.
4. Weź prosty projekt w jednym pliku i rozbij go na sensowne moduły.
5. Pokaż przykład zbyt przesadnie rozdrobnionej struktury i uprość ją.

---

## Przykładowe rozwiązania

### 1. Struktura

```text
my_app/
    README.md
    app/
        __init__.py
        main.py
        validators.py
    tests/
```

### 2. `validators.py`

```python
def is_valid_age(age):
    return age >= 0
```

### 3. `main.py`

```python
def main():
    print("start")

if __name__ == "__main__":
    main()
```

### 4. Rozbicie

Wyodrębnij np.:

- `main.py`
- `validators.py`
- `storage.py`
- `tests/`

---

## Antywzorce i pułapki z życia

### Antywzorzec 1: projekt jednoplikowy, który już dawno przestał być mały

Jeśli plik ma kilkaset linii i miesza:

- wejście użytkownika,
- walidację,
- zapis danych,
- logikę obliczeń,
- raportowanie,

to zwykle pora na podział.

### Antywzorzec 2: nadmierna architektura dla mikroskopijnego projektu

Jeśli prosty kalkulator ma 12 katalogów i 20 plików, to architektura zaczyna przeszkadzać zamiast pomagać.

### Antywzorzec 3: brak miejsca na testy i opis uruchomienia

Projekt bez `tests/` i `README.md` może działać, ale jest dużo trudniejszy do utrzymania i przekazania komuś innemu.

---

## Mini case study

Masz projekt `task_manager`, który zaczynał jako:

```text
task_manager.py
```

Z czasem dochodzi:

- walidacja danych,
- zapisywanie do pliku,
- kilka komend CLI,
- formatowanie wyjścia.

Dobry moment na podział:

```text
task_manager/
    README.md
    app/
        __init__.py
        main.py
        storage.py
        validators.py
        formatters.py
    tests/
```

Taki podział nie jest "na pokaz". On ułatwia znalezienie właściwego miejsca dla nowej logiki.

---

## Mini projekt po rozdziale

Zaprojektuj od zera mały projekt `student_manager` z plikami:

- `main.py`
- `validators.py`
- `storage.py`
- `reports.py`
- `README.md`
- `tests/`

Zastanów się przed pisaniem kodu:

- co należy do punktu wejścia,
- co należy do walidacji,
- co należy do pracy z danymi,
- co należy do prezentacji wyniku.

To ćwiczenie bardzo dobrze domyka temat organizacji projektu, bo zmusza do świadomego podziału odpowiedzialności jeszcze przed kodowaniem.
