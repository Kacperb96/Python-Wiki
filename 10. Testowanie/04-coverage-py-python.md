# Jakość testów i pokrycie kodu — `coverage.py`

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest pokrycie kodu](#czym-jest-pokrycie-kodu)
3. [Po co mierzyć pokrycie](#po-co-mierzyć-pokrycie)
4. [Czego pokrycie nie gwarantuje](#czego-pokrycie-nie-gwarantuje)
5. [Czym jest `coverage.py`](#czym-jest-coveragepy)
6. [Podstawowe użycie](#podstawowe-użycie)
7. [`coverage run`](#coverage-run)
8. [`coverage report`](#coverage-report)
9. [`coverage html`](#coverage-html)
10. [Pokrycie linii a jakość testów](#pokrycie-linii-a-jakość-testów)
11. [Pokrycie gałęzi](#pokrycie-gałęzi)
12. [Interpretacja raportu](#interpretacja-raportu)
13. [Typowe pułapki myślenia o coverage](#typowe-pułapki-myślenia-o-coverage)
14. [Jak podnosić jakość testów, a nie tylko procent](#jak-podnosić-jakość-testów-a-nie-tylko-procent)
15. [Typowe błędy początkujących](#typowe-błędy-początkujących)
16. [Praktyczne przykłady](#praktyczne-przykłady)
17. [Dobre praktyki](#dobre-praktyki)
18. [Podsumowanie](#podsumowanie)
19. [Mini ściąga](#mini-ściąga)
20. [Ćwiczenia](#ćwiczenia)
21. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Samo posiadanie testów jeszcze nie znaczy, że testujesz dobrze.

Dlatego często mierzy się:

- ile kodu zostało wykonane przez testy,
- które miejsca w kodzie nie są w ogóle dotykane,
- gdzie mogą być luki w testach.

Do tego służy między innymi `coverage.py`.

---

## Czym jest pokrycie kodu

Pokrycie kodu to informacja o tym, jaka część kodu została wykonana podczas testów.

Najczęściej mówi się o:

- pokryciu linii,
- pokryciu gałęzi.

---

## Po co mierzyć pokrycie

Bo pomaga zobaczyć:

- które fragmenty kodu nie są testowane,
- gdzie brakuje testów,
- czy nowy moduł jest w ogóle obejmowany przez testy.

To dobre narzędzie pomocnicze.

---

## Czego pokrycie nie gwarantuje

To bardzo ważne:

wysokie pokrycie nie oznacza automatycznie dobrych testów.

Możesz mieć:

- 100% coverage,
- a mimo to słabe asercje,
- pominięte ważne scenariusze,
- błędy logiczne.

Coverage to wskaźnik pomocniczy, nie ostateczna prawda.

---

## Czym jest `coverage.py`

To bardzo popularne narzędzie do mierzenia pokrycia kodu w Pythonie.

Najczęściej używa się go razem z testami uruchamianymi przez `pytest`.

---

## Podstawowe użycie

Typowy przepływ:

1. uruchamiasz testy przez `coverage`,
2. generujesz raport.

---

## `coverage run`

Przykład:

```bash
coverage run -m pytest
```

To uruchamia testy i zbiera dane o pokryciu.

---

## `coverage report`

Raport tekstowy:

```bash
coverage report
```

Pokazuje między innymi:

- liczbę linii,
- liczbę pokrytych,
- procent pokrycia.

---

## `coverage html`

Możesz wygenerować raport HTML:

```bash
coverage html
```

To bardzo wygodne, bo można zobaczyć kolorowo:

- które linie były wykonane,
- które nie były.

---

## Pokrycie linii a jakość testów

Jeśli linia została wykonana, to nie znaczy jeszcze, że była dobrze przetestowana.

Na przykład:

- mogłeś tylko „przejść” przez kod,
- ale nie sprawdzić poprawnego wyniku.

Dlatego coverage trzeba łączyć z myśleniem o jakości testów.

---

## Pokrycie gałęzi

To bardziej szczegółowy poziom.

Jeśli masz:

```python
if warunek:
    ...
else:
    ...
```

to dobre testy powinny przejść:

- przez `if`,
- przez `else`.

Samo uruchomienie jednej ścieżki może nie wystarczyć.

---

## Interpretacja raportu

Najważniejsze pytania:

- które pliki mają niski coverage,
- które krytyczne ścieżki są nietestowane,
- czy brakuje testów dla wyjątków i edge case’ów.

Nie chodzi o ślepe patrzenie w procent.

---

## Typowe pułapki myślenia o coverage

### 1. „Mam 90%, więc jest świetnie”

Niekoniecznie.

### 2. „Mam niski procent, więc wszystko jest złe”

Też nie zawsze.

### 3. Gonienie za wynikiem zamiast za realną jakością testów

To bardzo częsty problem.

---

## Jak podnosić jakość testów, a nie tylko procent

Warto pytać:

- czy testuję przypadki błędów,
- czy testuję warunki brzegowe,
- czy testuję wyjątki,
- czy testuję ważne ścieżki biznesowe,
- czy asercje są sensowne.

---

## Typowe błędy początkujących

- skupienie tylko na procentach,
- brak rozróżnienia linii i gałęzi,
- ignorowanie nietestowanych ścieżek wyjątków,
- pisanie pustych albo mało wartościowych testów tylko po to, by podnieść coverage.

---

## Praktyczne przykłady

### Uruchomienie

```bash
coverage run -m pytest
coverage report
```

### HTML

```bash
coverage html
```

### Przykład logiczny

Jeśli funkcja ma:

```python
if x > 0:
    return "plus"
else:
    return "minus lub zero"
```

to dobre pokrycie powinno obejmować obie gałęzie.

---

## Dobre praktyki

### Traktuj coverage jako narzędzie pomocnicze

### Pilnuj jakości asercji

### Patrz szczególnie na ważne ścieżki logiki i błędy

### Staraj się testować także wyjątki i warunki graniczne

### Używaj raportu HTML, bo jest bardzo czytelny

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- coverage pokazuje, jaka część kodu została wykonana przez testy,
- `coverage.py` to popularne narzędzie do mierzenia pokrycia,
- wysoki coverage nie gwarantuje dobrych testów,
- coverage warto łączyć z myśleniem o jakości scenariuszy testowych.

---

## Mini ściąga

```bash
coverage run -m pytest
coverage report
coverage html
```

### Ważna zasada

coverage to wskaźnik pomocniczy, nie cel sam w sobie.

---

## Ćwiczenia

### Ćwiczenie 1

Uruchom testy przez `coverage run -m pytest`.

### Ćwiczenie 2

Wygeneruj raport tekstowy.

### Ćwiczenie 3

Wymyśl funkcję z `if/else` i zastanów się, jakie testy są potrzebne, by pokryć obie gałęzie.

---

## Przykładowe rozwiązania

### Ćwiczenie 1

```bash
coverage run -m pytest
```

### Ćwiczenie 2

```bash
coverage report
```

### Ćwiczenie 3

```python
def znak(x):
    if x > 0:
        return "plus"
    return "zero lub minus"
```

Potrzebujesz testu dla liczby dodatniej i dla niedodatniej.
