# Profilowanie w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co profilować kod](#po-co-profilować-kod)
3. [Najważniejsza zasada: nie zgaduj](#najważniejsza-zasada-nie-zgaduj)
4. [Czym różni się timing od profilowania](#czym-różni-się-timing-od-profilowania)
5. [`timeit`](#timeit)
6. [Przykład `timeit` z outputem](#przykład-timeit-z-outputem)
7. [Jak uczciwie porównywać dwa rozwiązania](#jak-uczciwie-porównywać-dwa-rozwiązania)
8. [`cProfile`](#cprofile)
9. [Przykład `cProfile` z outputem](#przykład-cprofile-z-outputem)
10. [Jak czytać kolumny w `cProfile`](#jak-czytać-kolumny-w-cprofile)
11. [`line_profiler`](#line_profiler)
12. [Kiedy używać którego narzędzia](#kiedy-używać-którego-narzędzia)
13. [Typowe pułapki wydajnościowe](#typowe-pułapki-wydajnościowe)
14. [Praktyczny workflow profilowania](#praktyczny-workflow-profilowania)
15. [Typowe błędy początkujących](#typowe-błędy-początkujących)
16. [Praktyczna ściąga](#praktyczna-ściąga)
17. [Ćwiczenia](#ćwiczenia)
18. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

Profilowanie to mierzenie wydajności kodu.

Chodzi o to, żeby ustalić:

- co działa wolno,
- ile czasu zajmuje dana operacja,
- która funkcja jest wąskim gardłem,
- czy optymalizacja naprawdę coś poprawiła.

W Pythonie bardzo często używa się:

- `timeit`,
- `cProfile`,
- `line_profiler`.

---

## Po co profilować kod

Bez pomiaru łatwo optymalizować niewłaściwe miejsce.

Programista często myśli:

- „na pewno ta pętla jest problemem”,
- „na pewno `append()` jest wolny”,
- „na pewno ten fragment trzeba przepisać”.

A potem okazuje się, że prawdziwy problem leży gdzie indziej.

Profilowanie pozwala podejmować decyzje na podstawie danych, a nie przeczucia.

---

## Najważniejsza zasada: nie zgaduj

To jedna z najważniejszych zasad profesjonalnej pracy z wydajnością.

Najpierw mierz, dopiero potem optymalizuj.

Jeśli nie zmierzyłeś:

- nie wiesz, czy problem naprawdę istnieje,
- nie wiesz, gdzie jest problem,
- nie wiesz, czy Twoja poprawka cokolwiek dała.

---

## Czym różni się timing od profilowania

### Timing

Mierzy łączny czas wykonania fragmentu kodu.

Pytanie, na które odpowiada:

ile to trwa?

### Profilowanie

Rozbija czas na części.

Pytania, na które odpowiada:

- która funkcja jest wolna,
- ile razy została wywołana,
- gdzie dokładnie znika czas.

---

## `timeit`

`timeit` służy do mierzenia małych fragmentów kodu.

Bardzo dobrze nadaje się do:

- porównywania dwóch krótkich rozwiązań,
- mikrobenchmarków,
- sprawdzania, czy zapis A jest szybszy od zapisu B.

Przykład:

```python
import timeit

wynik = timeit.timeit("sum(range(100))", number=10000)
print(wynik)
```

Tu kod wykona się `10000` razy, a wynik będzie łącznym czasem.

---

## Przykład `timeit` z outputem

```python
import timeit

wynik = timeit.timeit("'-'.join(['a', 'b', 'c'])", number=100000)
print(wynik)
```

Przykładowy output:

```text
0.02843159200081229
```

Interpretacja:

- wykonanie całej operacji `100000` razy zajęło około `0.028` sekundy,
- pojedyncze wykonanie było więc bardzo szybkie.

Ważne:

ten wynik zależy od komputera, obciążenia systemu i środowiska.

Nie porównuj surowych liczb z cudzym komputerem.

---

## Jak uczciwie porównywać dwa rozwiązania

Najczęściej nie chodzi o samą liczbę sekund, tylko o porównanie wariantów.

Przykład:

```python
import timeit

join_time = timeit.timeit("'-'.join(['a', 'b', 'c'])", number=100000)
plus_time = timeit.timeit("'a' + '-' + 'b' + '-' + 'c'", number=100000)

print(join_time)
print(plus_time)
```

Przykładowy output:

```text
0.0284
0.0351
```

Wniosek:

w tym konkretnym teście `join()` było szybsze.

Ale ważniejsze od samego wyniku jest poprawne pytanie:

czy to ma znaczenie dla mojego programu?

Jeśli ten fragment wykonuje się raz, mikrooptymalizacja może być bez sensu.

---

## `cProfile`

`cProfile` daje szerszy obraz programu.

Pokazuje m.in.:

- które funkcje ile czasu zajmują,
- ile razy zostały wywołane,
- gdzie są główne koszty wykonania.

Przykład:

```python
import cProfile


def policz():
    total = 0
    for _ in range(10000):
        total += sum(range(100))
    return total


cProfile.run("policz()")
```

---

## Przykład `cProfile` z outputem

Przykładowy uproszczony output:

```text
         10004 function calls in 0.031 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.011    0.011    0.031    0.031 demo.py:4(policz)
    10000    0.019    0.000    0.019    0.000 {built-in method builtins.sum}
        1    0.000    0.000    0.031    0.031 <string>:1(<module>)
```

Jak to czytać:

- `policz()` została wywołana 1 raz,
- `sum()` została wywołana `10000` razy,
- większość czasu poszła właśnie w te wywołania.

---

## Jak czytać kolumny w `cProfile`

Najważniejsze kolumny:

### `ncalls`

Liczba wywołań funkcji.

### `tottime`

Czas spędzony wewnątrz samej funkcji, bez czasu funkcji wywołanych przez nią dalej.

### `cumtime`

Łączny czas funkcji razem z funkcjami, które ona wywołała.

### `percall`

Średni czas na jedno wywołanie.

Praktyczna wskazówka:

na początku najczęściej patrzysz na funkcje z największym `cumtime` i `tottime`.

---

## `line_profiler`

`line_profiler` mierzy czas na poziomie konkretnych linii w funkcji.

To narzędzie przydaje się wtedy, gdy:

- `cProfile` już pokazał wolną funkcję,
- chcesz wiedzieć, która dokładnie linia w niej spowalnia program.

To nie jest narzędzie ze standardowej biblioteki, ale warto znać samą ideę.

Przykładowy scenariusz:

1. `cProfile` wskazuje funkcję `przetworz_dane`,
2. uruchamiasz profiler liniowy,
3. widzisz, że 80% czasu idzie w jednej pętli albo jednej operacji.

---

## Kiedy używać którego narzędzia

### `timeit`

Używaj, gdy:

- porównujesz dwa małe fragmenty kodu,
- chcesz zrobić szybki mikrobenchmark,
- nie analizujesz całego programu.

### `cProfile`

Używaj, gdy:

- chcesz zrozumieć większy obraz,
- nie wiesz jeszcze, która funkcja jest problemem,
- potrzebujesz analizy wywołań funkcji.

### `line_profiler`

Używaj, gdy:

- znasz już podejrzaną funkcję,
- chcesz zejść do poziomu linii,
- potrzebujesz bardzo precyzyjnej diagnozy.

---

## Typowe pułapki wydajnościowe

- optymalizacja bez pomiaru,
- skupienie na mikrodetalach zamiast na dużym problemie,
- porównywanie wyników z różnych warunków,
- ignorowanie algorytmu i złożoności obliczeniowej,
- mierzenie bardzo małej próbki i wyciąganie wielkich wniosków.

Przykład:

Jeśli masz zły algorytm o słabej złożoności, to kosmetyczna poprawa jednej linijki nic nie da.

---

## Praktyczny workflow profilowania

Dobry schemat pracy wygląda tak:

1. zauważ problem wydajności,
2. odtwórz go na miarodajnym przykładzie,
3. użyj `cProfile`, żeby znaleźć wolne funkcje,
4. jeśli trzeba, użyj `timeit` do porównania małych wariantów,
5. jeśli trzeba, użyj narzędzia liniowego,
6. wprowadź zmianę,
7. zmierz ponownie,
8. porównaj wynik przed i po.

Najważniejsze są kroki `przed` i `po`.

Bez nich nie wiesz, czy naprawdę coś poprawiłeś.

---

## Typowe błędy początkujących

- mylenie `timeit` z pełnym profilerem,
- mierzenie czegoś raz i uznawanie wyniku za pewny,
- wybieranie „szybszego” wariantu kosztem czytelności bez realnego zysku,
- brak ponownego pomiaru po zmianach,
- optymalizowanie kodu, który wcale nie jest wąskim gardłem.

---

## Praktyczna ściąga

### Szybki pomiar małego fragmentu

```python
import timeit
print(timeit.timeit("sum(range(100))", number=10000))
```

### Profil całej funkcji

```python
import cProfile
cProfile.run("moja_funkcja()")
```

### Pytania, które warto sobie zadać

- Co dokładnie mierzę?
- Czy wynik jest powtarzalny?
- Czy ten fragment naprawdę ma znaczenie dla całego programu?
- Czy po zmianie program faktycznie działa szybciej?

---

## Ćwiczenia

1. Użyj `timeit`, aby zmierzyć czas `sum(range(100))`.
2. Porównaj przez `timeit` dwa sposoby łączenia tekstu: `join()` i `+`.
3. Napisz funkcję z pętlą i uruchom ją przez `cProfile.run(...)`.
4. Odczytaj z outputu `cProfile`, która funkcja miała największy `cumtime`.
5. Zmień kod tak, aby zmniejszyć liczbę wywołań jednej funkcji, i porównaj wynik.
6. Zastanów się, czy optymalizacja poprawiła tylko mikrobenchmark, czy cały scenariusz programu.
7. Wybierz fragment własnego projektu i opisz, czy bardziej pasuje tam `timeit`, czy `cProfile`.
8. Własnymi słowami wyjaśnij różnicę między `tottime` i `cumtime`.
9. Podaj przykład sytuacji, w której optymalizacja byłaby przedwczesna.
10. Napisz krótką notatkę: „najpierw mierz, potem poprawiaj” i wyjaśnij, dlaczego to ważne.

---

## Najważniejsze do zapamiętania

- `timeit` mierzy małe fragmenty kodu.
- `cProfile` pokazuje, które funkcje zużywają czas.
- `line_profiler` schodzi do poziomu konkretnej linii.
- Najpierw szukasz problemu, potem dopiero optymalizujesz.
- Wynik pomiaru ma sens tylko wtedy, gdy wiesz, co dokładnie mierzysz.
- Dobra optymalizacja to taka, którą da się potwierdzić pomiarem przed i po zmianie.
