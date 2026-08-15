# Debugowanie w Pythonie — `pdb`, `breakpoint()`

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co debugować](#po-co-debugować)
3. [Debugowanie a `print`](#debugowanie-a-print)
4. [`breakpoint()`](#breakpoint)
5. [Czym jest `pdb`](#czym-jest-pdb)
6. [Jak działa debugger](#jak-działa-debugger)
7. [Najczęstsze komendy `pdb`](#najczęstsze-komendy-pdb)
8. [Przechodzenie krok po kroku](#przechodzenie-krok-po-kroku)
9. [Podgląd zmiennych](#podgląd-zmiennych)
10. [Wyjście z debuggera](#wyjście-z-debuggera)
11. [Kiedy `breakpoint()` jest wygodniejsze](#kiedy-breakpoint-jest-wygodniejsze)
12. [Kiedy używać debuggera zamiast printów](#kiedy-używać-debuggera-zamiast-printów)
13. [Typowe błędy początkujących](#typowe-błędy-początkujących)
14. [Praktyczne przykłady](#praktyczne-przykłady)
15. [Dobre praktyki](#dobre-praktyki)
16. [Podsumowanie](#podsumowanie)
17. [Mini ściąga](#mini-ściąga)
18. [Ćwiczenia](#ćwiczenia)
19. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Debugowanie to umiejętność znajdowania i rozumienia błędów.

To jedna z najważniejszych kompetencji programisty.

W Pythonie masz kilka prostych, bardzo przydatnych narzędzi:

- `print()` jako bardzo podstawowy sposób,
- `breakpoint()`,
- `pdb`.

W praktyce warto umieć korzystać przynajmniej z `breakpoint()` i podstaw `pdb`.

---

## Po co debugować

Bo błędy nie znikną same.

Debugowanie pomaga odpowiedzieć na pytania:

- jaka jest wartość zmiennej,
- gdzie program skręca w złą ścieżkę,
- która funkcja daje niepoprawny wynik,
- dlaczego wyjątek się pojawia.

---

## Debugowanie a `print`

`print()` jest szybkie i proste.

Ale:

- zaśmieca kod,
- daje mało kontroli,
- nie pozwala wygodnie przechodzić po wykonaniu krok po kroku.

Debugger pozwala wejść głębiej.

---

## `breakpoint()`

Od Pythona 3.7 masz bardzo wygodne:

```python
breakpoint()
```

To najprostszy sposób wejścia do debuggera.

Przykład:

```python
def dodaj(a, b):
    breakpoint()
    return a + b
```

Po dojściu programu do tej linii wejdziesz do debuggera.

---

## Czym jest `pdb`

`pdb` to standardowy debugger Pythona.

Można go używać:

- przez `breakpoint()`,
- przez `import pdb; pdb.set_trace()`,
- przez uruchamianie skryptu z debuggerem.

---

## Jak działa debugger

Debugger zatrzymuje wykonanie programu w wybranym miejscu.

Potem możesz:

- oglądać zmienne,
- iść linia po linii,
- wchodzić do funkcji,
- wychodzić z funkcji,
- kontynuować program.

---

## Najczęstsze komendy `pdb`

Najważniejsze:

- `n` — next
- `s` — step
- `c` — continue
- `p x` — print `x`
- `l` — list
- `q` — quit

To już wystarcza do wielu prostych przypadków.

---

## Przechodzenie krok po kroku

### `n`

Idź do następnej linii w tej samej funkcji.

### `s`

Wejdź do wywoływanej funkcji.

### `c`

Kontynuuj do kolejnego breakpointa lub końca.

---

## Podgląd zmiennych

Możesz wpisać:

```python
p nazwa_zmiennej
```

albo nawet uruchamiać proste wyrażenia.

To bardzo pomaga zrozumieć stan programu w danym miejscu.

Przykład:

jeśli zatrzymasz program w funkcji:

```python
def policz(a, b):
    breakpoint()
    wynik = a + b
    return wynik
```

możesz w debuggerze wpisać:

```text
(Pdb) p a
2
(Pdb) p b
3
```

---

## Wyjście z debuggera

Najczęściej:

```python
q
```

Trzeba pamiętać, że to zwykle przerywa program.

---

## Kiedy `breakpoint()` jest wygodniejsze

Prawie zawsze w prostym codziennym użyciu.

Jest:

- krótkie,
- czytelne,
- nowoczesne,
- wygodniejsze niż ręczne `pdb.set_trace()`.

---

## Kiedy używać debuggera zamiast printów

Gdy:

- błąd jest trudniejszy,
- chcesz zobaczyć wiele wartości w jednym miejscu,
- musisz przejść przez kod krok po kroku,
- problem dotyczy kilku funkcji naraz.

---

## Typowe błędy początkujących

- zostawianie `breakpoint()` w commitowanym kodzie,
- używanie tylko printów nawet przy trudnych błędach,
- nieznajomość podstawowych komend `pdb`,
- panika po wejściu do debuggera.

### 5. Wychodzenie z debuggera bez zrozumienia stanu programu

Debugger daje wartość tylko wtedy, gdy naprawdę patrzysz na zmienne i przepływ wykonania.

---

## Praktyczne przykłady

```python
def policz(a, b):
    breakpoint()
    wynik = a + b
    return wynik
```

Przykładowy przebieg:

```text
(Pdb) p a
2
(Pdb) p b
3
(Pdb) n
(Pdb) p wynik
5
(Pdb) c
```

### Starszy styl

```python
import pdb

def policz(a, b):
    pdb.set_trace()
    return a + b
```

---

## Dobre praktyki

- używaj `breakpoint()` do lokalnego debugowania,
- usuwaj breakpointy przed finalnym commitem,
- zaczynaj od prostych komend `n`, `s`, `p`, `c`,
- jeśli problem jest mały, `print()` czasem nadal wystarczy.

Praktyczna zasada:

najpierw ustal, czego chcesz się dowiedzieć, a dopiero potem wchodź do debuggera. Wtedy szybciej znajdziesz problem.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- `breakpoint()` to najwygodniejszy sposób wejścia do debuggera,
- `pdb` pozwala analizować program krok po kroku,
- debugger daje dużo więcej niż `print()`,
- debugowanie to podstawowa umiejętność programisty.

Najważniejsze do zapamiętania:

- `print()` pokazuje stan na chwilę,
- debugger pozwala zatrzymać program i naprawdę go obejrzeć,
- kilka podstawowych komend `pdb` wystarcza do bardzo wielu realnych problemów.

---

## Mini ściąga

```python
breakpoint()
```

### Komendy

- `n`
- `s`
- `c`
- `p zmienna`
- `q`

---

## Ćwiczenia

### Ćwiczenie 1

Dodaj `breakpoint()` do prostej funkcji i sprawdź wartość argumentów.

### Ćwiczenie 2

Przejdź przez funkcję krok po kroku komendą `n`.

### Ćwiczenie 3

Wejdź do wywoływanej funkcji przez `s`.

---

## Przykładowe rozwiązania

```python
def dodaj(a, b):
    breakpoint()
    return a + b
```
