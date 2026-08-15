# Benchmarking w Pythonie

## O co chodzi

Benchmarking to mierzenie wydajności kodu w sposób możliwie uczciwy i powtarzalny.

Nie chodzi o:

- "wydaje mi się, że to jest szybsze",
- jednorazowe odpalenie kodu,
- patrzenie na czas z jednego przebiegu,
- porównywanie wyników bez kontroli warunków.

Chodzi o to, żeby naprawdę sprawdzić, które rozwiązanie jest szybsze i o ile.

## Najważniejsza zasada

Nie zgaduj. Mierz.

To jest fundament całego działu performance.

## Dlaczego benchmarki są potrzebne

Bardzo często intuicja programisty bywa myląca.

Kod, który wygląda na bardziej sprytny, nie zawsze jest szybszy. Kod, który wygląda prosto, czasem okazuje się bardzo wydajny.

Bez pomiaru łatwo:

- poprawić nie ten fragment co trzeba,
- pogorszyć czytelność bez realnego zysku,
- uwierzyć w fałszywy mit wydajnościowy.

## Co mierzyć

Najczęściej mierzymy:

- czas wykonania,
- liczbę powtórzeń,
- czas średni lub minimalny,
- czas porównawczy dwóch podejść.

Czasem później dojdzie też pamięć, ale benchmarking najczęściej zaczyna się od czasu.

## Prosty benchmark — zła wersja

```python
import time

start = time.time()
result = [x * 2 for x in range(1000000)]
end = time.time()

print(end - start)
```

To może dać jakiś wynik, ale nie jest to jeszcze dobry benchmark.

Dlaczego?

- tylko jeden przebieg,
- brak powtórzeń,
- wynik może zależeć od losowych czynników systemowych,
- trudno porównać warianty uczciwie.

## Lepsze podejście: `timeit`

Do prostych benchmarków Python daje bardzo dobre narzędzie: `timeit`.

```python
import timeit

code = "[x * 2 for x in range(100000)]"
result = timeit.timeit(code, number=100)
print(result)
```

Output będzie liczbowy, np.:

```python
0.42
```

Dokładna wartość zależy od maszyny i środowiska.

## Porównanie dwóch rozwiązań

```python
import timeit

list_comp = timeit.timeit("[x * 2 for x in range(100000)]", number=100)
manual_loop = timeit.timeit(
    """
result = []
for x in range(100000):
    result.append(x * 2)
""",
    number=100,
)

print("list comprehension:", list_comp)
print("manual loop:", manual_loop)
```

Przykładowy output:

```python
list comprehension: 0.41
manual loop: 0.53
```

Interpretacja:

- list comprehension wygrało,
- ale nie dlatego, że "pętle są złe",
- tylko dlatego, że w tym konkretnym zadaniu i na tej maszynie to rozwiązanie było szybsze.

## Benchmark 1: łączenie stringów

```python
import timeit

join_time = timeit.timeit('"".join(["a", "b", "c"] * 1000)', number=10000)
plus_time = timeit.timeit(
    'result = ""\nfor x in ["a", "b", "c"] * 1000:\n    result += x',
    number=10000,
)

print("join:", join_time)
print("plus w pętli:", plus_time)
```

Przykładowy output:

```python
join: 0.62
plus w pętli: 1.94
```

Interpretacja:

- `join()` jest wyraźnie lepsze do łączenia wielu fragmentów tekstu,
- zysk jest na tyle duży, że to nie jest kosmetyka,
- to dobry przykład sytuacji, gdzie idiom Pythona jest też wydajniejszy.

## Benchmark 2: membership w liście vs secie

```python
import timeit

setup = """
items_list = list(range(100000))
items_set = set(items_list)
target = 99999
"""

list_time = timeit.timeit("target in items_list", setup=setup, number=5000)
set_time = timeit.timeit("target in items_set", setup=setup, number=5000)

print("list membership:", list_time)
print("set membership:", set_time)
```

Przykładowy output:

```python
list membership: 3.80
set membership: 0.0019
```

Interpretacja:

- to nie jest mikrooptymalizacja,
- to jest różnica wynikająca z doboru struktury danych,
- jeśli często pytasz "czy element istnieje?", `set` bywa ogromnie lepszy niż `list`.

## Benchmark 3: lista vs generator przy sumowaniu

```python
import timeit

list_time = timeit.timeit("sum([x * 2 for x in range(100000)])", number=200)
gen_time = timeit.timeit("sum(x * 2 for x in range(100000))", number=200)

print("list comprehension:", list_time)
print("generator expression:", gen_time)
```

Przykładowy output:

```python
list comprehension: 0.88
generator expression: 1.03
```

Interpretacja:

- generator nie zawsze wygrywa czasowo,
- ale może wygrywać pamięciowo,
- dlatego sam czas to jeszcze nie cały obraz decyzji optymalizacyjnej.

To bardzo ważna lekcja: szybsze i lżejsze pamięciowo to nie zawsze to samo.

## Co może zafałszować benchmark

Bardzo dużo rzeczy:

- procesy działające w tle,
- różne obciążenie systemu,
- jednorazowe koszty startowe,
- cache,
- zbyt mała liczba powtórzeń,
- mierzenie czegoś z I/O zamiast czystej logiki,
- mieszanie benchmarku z debug printami.

## Benchmark z printem — antyprzykład

```python
import timeit

result = timeit.timeit(
    'for i in range(1000): print(i)',
    number=1,
)
print(result)
```

To fatalny benchmark do porównywania logiki Pythona, bo dominuje I/O do terminala, a nie sama pętla.

## Benchmarkuj to, co naprawdę chcesz porównać

Jeśli chcesz porównać dwa sposoby budowania listy, to benchmark powinien mierzyć właśnie to, a nie pół programu wokół.

## Mikrobenchmark vs realny scenariusz

To bardzo ważne rozróżnienie.

### Mikrobenchmark

Mierzy bardzo mały fragment kodu.

Przydatny, gdy:

- porównujesz 2 konkretne warianty,
- chcesz zrozumieć koszt drobnej operacji.

### Realny scenariusz

Mierzy zachowanie większego fragmentu systemu.

Przydatny, gdy:

- małe różnice nie mają znaczenia,
- chcesz wiedzieć, co naprawdę boli użytkownika albo proces.

## Kiedy benchmarking ma sens

Szczególnie gdy:

- masz dwa konkurencyjne rozwiązania,
- podejrzewasz hot spot,
- chcesz potwierdzić, czy zmiana coś dała,
- chcesz uniknąć optymalizacji na ślepo.

## Kiedy nie przesadzać

Nie benchmarkuj wszystkiego obsesyjnie.

Jeśli problemem jest np. zła architektura, duże I/O albo zły algorytm, mikrobenchmark jednej linijki może nie mieć większego znaczenia.

## Typowe błędy początkujących

- jeden przebieg i wyciąganie wielkich wniosków,
- mierzenie z printami,
- brak porównania do drugiej wersji,
- mylenie benchmarku z pełną analizą performance,
- wyciąganie ogólnych zasad z jednego małego testu.

## Szybka ściąga

- benchmarking służy do uczciwego porównywania wydajności,
- `timeit` to bardzo dobry punkt startowy,
- benchmark powinien być powtarzalny,
- nie benchmarkuj przypadkowych efektów ubocznych,
- pomiar jest lepszy niż intuicja.

## Ćwiczenia

1. Porównaj pętlę i list comprehension.
2. Porównaj dwa sposoby łączenia stringów.
3. Zrób benchmark z wieloma powtórzeniami.
4. Pokaż zły benchmark i wyjaśnij, co w nim jest nie tak.
5. Wskaż sytuację, gdzie mikrobenchmark nie wystarczy.

## Najważniejsze do zapamiętania

- Benchmarking to pomiar, nie zgadywanie.
- `timeit` jest świetnym narzędziem do prostych porównań.
- Jeden przebieg nie daje wiarygodnego obrazu.
- Benchmarki łatwo źle zrobić.
- Celem jest podejmowanie lepszych decyzji, a nie zbieranie losowych liczb.
