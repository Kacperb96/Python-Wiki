# Jakość testów i pokrycie kodu — `coverage.py`

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest pokrycie kodu](#czym-jest-pokrycie-kodu)
3. [Po co mierzyć coverage](#po-co-mierzyć-coverage)
4. [Czego coverage nie gwarantuje](#czego-coverage-nie-gwarantuje)
5. [Podstawowe użycie `coverage.py`](#podstawowe-użycie-coveragepy)
6. [`coverage run`](#coverage-run)
7. [`coverage report`](#coverage-report)
8. [`coverage html`](#coverage-html)
9. [Pokrycie linii i pokrycie gałęzi](#pokrycie-linii-i-pokrycie-gałęzi)
10. [Przykładowy raport i jego interpretacja](#przykładowy-raport-i-jego-interpretacja)
11. [Jak podnosić jakość testów, a nie tylko procent](#jak-podnosić-jakość-testów-a-nie-tylko-procent)
12. [Typowe pułapki](#typowe-pułapki)
13. [Typowe błędy początkujących](#typowe-błędy-początkujących)
14. [Praktyczna ściąga](#praktyczna-ściąga)
15. [Ćwiczenia](#ćwiczenia)
16. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

Samo to, że masz testy, nie znaczy jeszcze, że testujesz dobrze.

Dlatego często mierzy się:

- jaka część kodu została wykonana podczas testów,
- które linie w ogóle nie są dotykane,
- czy testy obejmują różne gałęzie logiki.

Do tego służy między innymi `coverage.py`.

---

## Czym jest pokrycie kodu

Pokrycie kodu to informacja o tym, jaka część kodu została wykonana przez testy.

Najczęściej mówi się o:

- pokryciu linii,
- pokryciu gałęzi.

Jeśli jakaś linia nie została wykonana ani razu, to najpewniej nie masz testu, który do niej dochodzi.

---

## Po co mierzyć coverage

Coverage pomaga:

- znaleźć nieprzetestowane miejsca,
- zobaczyć martwe albo zapomniane ścieżki kodu,
- lepiej kierować pracą nad testami,
- pilnować, czy nowy moduł w ogóle jest obejmowany testami.

To bardzo przydatny wskaźnik pomocniczy.

---

## Czego coverage nie gwarantuje

To bardzo ważne:

wysoki coverage nie oznacza automatycznie dobrych testów.

Możesz mieć:

- 100% pokrycia,
- a mimo to słabe asercje,
- pominięte edge case'y,
- pomylone wymagania,
- źle testowaną logikę.

Coverage mówi tylko, że kod został wykonany.

Nie mówi, czy został sensownie sprawdzony.

---

## Podstawowe użycie `coverage.py`

Typowy przepływ wygląda tak:

1. uruchamiasz testy przez `coverage`,
2. generujesz raport,
3. sprawdzasz, czego brakuje,
4. dopisujesz testy,
5. mierzysz ponownie.

---

## `coverage run`

Najczęstsza komenda:

```bash
coverage run -m pytest
```

To uruchamia testy i zbiera dane o pokryciu.

Jeśli projekt ma już testy, to zwykle jest pierwszy krok.

---

## `coverage report`

Raport tekstowy:

```bash
coverage report
```

Przykładowy output:

```text
Name                Stmts   Miss  Cover
---------------------------------------
app.py                 20      2    90%
validators.py          15      5    67%
services.py            30      0   100%
---------------------------------------
TOTAL                  65      7    89%
```

Jak to czytać:

- `Stmts` to liczba instrukcji,
- `Miss` to liczba niepokrytych,
- `Cover` to procent pokrycia.

W tym przykładzie najsłabszy jest moduł `validators.py`.

---

## `coverage html`

Możesz wygenerować raport HTML:

```bash
coverage html
```

Przykładowy output:

```text
Wrote HTML report to htmlcov/index.html
```

To bardzo wygodna forma, bo można kolorami zobaczyć:

- zielone linie pokryte,
- czerwone linie niepokryte.

---

## Pokrycie linii i pokrycie gałęzi

### Pokrycie linii

Mówi, czy dana linia została wykonana.

### Pokrycie gałęzi

Mówi, czy zostały wykonane różne warianty przepływu, np. `if` i `else`.

Przykład:

```python
def okresl_znak(x: int) -> str:
    if x > 0:
        return "plus"
    else:
        return "minus-lub-zero"
```

Jeśli testujesz tylko `x = 5`, to:

- linia z `if` jest pokryta,
- ale gałąź `else` już nie.

Dlatego samo pokrycie linii czasem daje zbyt optymistyczny obraz.

---

## Przykładowy raport i jego interpretacja

Załóżmy funkcję:

```python
def klasyfikuj_wiek(wiek: int) -> str:
    if wiek < 0:
        raise ValueError("Wiek nie moze byc ujemny")
    if wiek < 18:
        return "niepelnoletni"
    return "pelnoletni"
```

Jeśli testujesz tylko `10` i `20`, możesz mieć częściowe pokrycie.

Ale bez testu dla `-1` nadal nie sprawdzasz ważnej ścieżki błędu.

Właśnie dlatego coverage ma sens dopiero razem z myśleniem o przypadkach.

---

## Jak podnosić jakość testów, a nie tylko procent

Lepsze pytania niż "jak dobić do 100%":

- które scenariusze są naprawdę ważne biznesowo,
- które wyjątki nie są sprawdzane,
- które warunki logiczne mają tylko połowę testów,
- czy testy sprawdzają wynik, a nie tylko wykonanie kodu,
- czy brak pokrycia nie wskazuje na słaby design kodu.

Czasem niższy coverage z bardzo sensownymi testami jest lepszy niż sztuczne 100% bez wartości.

---

## Typowe pułapki

- gonienie za procentem zamiast za jakością,
- pisanie testów tylko po to, żeby wykonać linię,
- ignorowanie nieprzetestowanych wyjątków,
- nieuwzględnianie wartości granicznych,
- traktowanie coverage jako jedynego wskaźnika jakości.

Coverage jest mapą pomocniczą, nie ostatecznym sędzią.

---

## Typowe błędy początkujących

- myślenie, że 100% coverage oznacza brak błędów,
- brak analizy raportu moduł po module,
- patrzenie tylko na wynik `TOTAL`,
- dopisywanie pustych albo słabych testów tylko dla statystyki,
- brak sprawdzania gałęzi błędnych i wyjątków.

---

## Praktyczna ściąga

### Zbierz dane o pokryciu

```bash
coverage run -m pytest
```

### Raport tekstowy

```bash
coverage report
```

### Raport HTML

```bash
coverage html
```

### Najważniejsze pytania

- Które moduły są najsłabiej pokryte?
- Które ważne warunki nie mają testów?
- Czy testy sprawdzają także ścieżki błędne?
- Czy coverage ujawnia zbyt trudny do testowania kod?

---

## Ćwiczenia

1. Uruchom `coverage run -m pytest` dla małego projektu.
2. Wygeneruj `coverage report` i wskaż najsłabszy moduł.
3. Dopisz testy dla jednej niepokrytej funkcji.
4. Zmierz coverage ponownie i porównaj wynik.
5. Dodaj test dla wyjątku i sprawdź, czy raport się poprawił.
6. Wymyśl przykład, w którym coverage jest wysokie, ale testy nadal są słabe.
7. Opisz własnymi słowami różnicę między pokryciem linii a pokryciem gałęzi.
8. Zastanów się, czy brak pokrycia wynika z braku testów, czy z nieczytelnego designu kodu.

---

## Najważniejsze do zapamiętania

- Coverage pokazuje, jaka część kodu została wykonana przez testy.
- To bardzo przydatny wskaźnik pomocniczy.
- Wysoki coverage nie gwarantuje dobrych testów.
- Najważniejsze są sensowne scenariusze, nie sam procent.
- Szczególnie pilnuj ścieżek błędnych, wyjątków i wartości granicznych.
- Coverage ma największą wartość wtedy, gdy łączysz go z realnym myśleniem o jakości testów.
