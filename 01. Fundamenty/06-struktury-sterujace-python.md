# Struktury sterujące w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym są struktury sterujące](#czym-są-struktury-sterujące)
3. [Dlaczego są tak ważne](#dlaczego-są-tak-ważne)
4. [Bloki kodu i wcięcia](#bloki-kodu-i-wcięcia)
5. [Instrukcja `if`](#instrukcja-if)
6. [Instrukcja `if else`](#instrukcja-if-else)
7. [Instrukcja `if elif else`](#instrukcja-if-elif-else)
8. [Zagnieżdżone warunki](#zagnieżdżone-warunki)
9. [Operatory w warunkach](#operatory-w-warunkach)
10. [Skrócone wyrażenie warunkowe](#skrócone-wyrażenie-warunkowe)
11. [Najczęstsze błędy w `if`](#najczęstsze-błędy-w-if)
12. [Pętle w Pythonie](#pętle-w-pythonie)
13. [Pętla `for`](#pętla-for)
14. [Funkcja `range()`](#funkcja-range)
15. [Pętla `for` na napisach, listach i słownikach](#pętla-for-na-napisach-listach-i-słownikach)
16. [Pętla `while`](#pętla-while)
17. [Pętle nieskończone](#pętle-nieskończone)
18. [Instrukcje `break`, `continue`, `pass`](#instrukcje-break-continue-pass)
19. [Sekcja `else` w pętlach](#sekcja-else-w-pętlach)
20. [Pętle zagnieżdżone](#pętle-zagnieżdżone)
21. [Instrukcja `match case`](#instrukcja-match-case)
22. [Kiedy używać `match case`](#kiedy-używać-match-case)
23. [Porównanie `if elif else` i `match case`](#porównanie-if-elif-else-i-match-case)
24. [Typowe błędy początkujących](#typowe-błędy-początkujących)
25. [Praktyczne przykłady](#praktyczne-przykłady)
26. [Dobre praktyki](#dobre-praktyki)
27. [Podsumowanie](#podsumowanie)
28. [Mini ściąga](#mini-ściąga)
29. [Ćwiczenia](#ćwiczenia)
30. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Struktury sterujące to elementy programu, które decydują:

- czy jakiś fragment kodu ma się wykonać,
- ile razy ma się wykonać,
- którą drogą ma pójść program.

Bez struktur sterujących program wykonywałby linie kodu tylko od góry do dołu, zawsze tak samo.

To właśnie dzięki nim program zaczyna "reagować".

---

## Czym są struktury sterujące

Najprościej:

- `if` sprawdza warunek,
- `for` powtarza coś po elementach albo określoną liczbę razy,
- `while` powtarza coś tak długo, jak warunek jest prawdziwy,
- `match case` wybiera jedną z wielu opcji.

Przykład:

```python
wiek = 20

if wiek >= 18:
    print("Jestes pelnoletni")
```

---

## Dlaczego są tak ważne

Bez struktur sterujących nie dałoby się wygodnie zrobić rzeczy takich jak:

- logowanie użytkownika,
- sprawdzanie poprawności hasła,
- przetwarzanie wielu elementów listy,
- pytanie użytkownika aż poda poprawne dane,
- wybór opcji z menu,
- reagowanie na wpisaną komendę.

---

## Bloki kodu i wcięcia

W Pythonie bardzo ważne są **wcięcia**.

To one pokazują, które linie należą do danego bloku kodu.

```python
if 5 > 3:
    print("To sie wykona")
    print("To tez")

print("To juz poza if")
```

Standardowo używa się 4 spacji.

Nie mieszaj spacji i tabulatorów.

---

## Instrukcja `if`

`if` służy do sprawdzania warunku.

```python
liczba = 10

if liczba > 0:
    print("Liczba jest dodatnia")
```

Output:

```python
Liczba jest dodatnia
```

Jeśli warunek jest `True`, blok się wykona.
Jeśli warunek jest `False`, blok zostanie pominięty.

---

## Instrukcja `if else`

`else` oznacza "w przeciwnym razie".

```python
liczba = -5

if liczba > 0:
    print("Dodatnia")
else:
    print("Niedodatnia")
```

Output:

```python
Niedodatnia
```

Masz dwie ścieżki programu.

---

## Instrukcja `if elif else`

Gdy masz więcej niż dwie możliwości, używasz `elif`.

```python
liczba = 0

if liczba > 0:
    print("Dodatnia")
elif liczba == 0:
    print("Zero")
else:
    print("Ujemna")
```

Output:

```python
Zero
```

Python sprawdza warunki od góry do dołu i zatrzymuje się na pierwszym pasującym.

---

## Zagnieżdżone warunki

Możesz umieszczać `if` wewnątrz `if`.

```python
wiek = 20
ma_bilet = True

if wiek >= 18:
    if ma_bilet:
        print("Mozesz wejsc")
```

Output:

```python
Mozesz wejsc
```

To działa, ale zbyt głębokie zagnieżdżenia szybko psują czytelność.

---

## Operatory w warunkach

W warunkach używa się:

- porównań,
- `and`,
- `or`,
- `not`,
- truthy/falsy.

Przykład:

```python
if wiek >= 18 and ma_dokument:
    print("OK")
```

---

## Skrócone wyrażenie warunkowe

Możesz zapisać prosty warunek w jednej linii:

```python
status = "pelnoletni" if wiek >= 18 else "niepelnoletni"
```

To wygodne przy bardzo prostych przypadkach, ale nie warto nadużywać.

---

## Najczęstsze błędy w `if`

- brak dwukropka,
- złe wcięcia,
- użycie `=` zamiast `==`,
- za bardzo skomplikowane warunki w jednej linii,
- mylenie `if x` z `if x is None`.

---

## Pętle w Pythonie

Pętle służą do powtarzania kodu.

Najważniejsze:

- `for`
- `while`

---

## Pętla `for`

`for` przechodzi po elementach jakiejś sekwencji albo po zakresie liczb.

```python
for i in range(5):
    print(i)
```

Output:

```python
0
1
2
3
4
```

To bardzo częsta pętla.

---

## Funkcja `range()`

`range()` tworzy zakres liczb.

```python
print(list(range(5)))
print(list(range(1, 6)))
print(list(range(0, 10, 2)))
```

Output:

```python
[0, 1, 2, 3, 4]
[1, 2, 3, 4, 5]
[0, 2, 4, 6, 8]
```

Najważniejsze formy:

- `range(stop)`
- `range(start, stop)`
- `range(start, stop, step)`

---

## Pętla `for` na napisach, listach i słownikach

Na stringu:

```python
for znak in "Python":
    print(znak)
```

Output:

```python
P
y
t
h
o
n
```

Na liście:

```python
for liczba in [1, 2, 3]:
    print(liczba)
```

Output:

```python
1
2
3
```

Na słowniku:

```python
for klucz in {"a": 1, "b": 2}:
    print(klucz)
```

Output może wyglądać tak:

```python
a
b
```

albo w innej kolejności, jeśli struktura danych albo kontekst programu to zmieni.

---

## Pętla `while`

`while` działa tak długo, jak warunek jest prawdziwy.

```python
x = 3

while x > 0:
    print(x)
    x -= 1
```

Output:

```python
3
2
1
```

To bardzo przydatne, gdy nie znasz z góry liczby powtórzeń.

---

## Pętle nieskończone

Jeśli warunek `while` nigdy nie stanie się `False`, pętla będzie działać bez końca.

```python
# while True:
#     print("nieskonczone")
```

Pętle nieskończone bywają celowe, ale zwykle trzeba mieć w środku `break`.

---

## Instrukcje `break`, `continue`, `pass`

### `break`

Przerywa pętlę całkowicie.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

Output:

```python
0
1
2
3
4
```

### `continue`

Pomija bieżącą iterację i przechodzi do następnej.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

Output:

```python
0
1
3
4
```

### `pass`

Nic nie robi.

Przydaje się jako tymczasowy pusty blok.

```python
if True:
    pass
```

---

## Sekcja `else` w pętlach

Python ma też `else` dla pętli.

```python
for i in range(3):
    print(i)
else:
    print("Koniec petli")
```

Output:

```python
0
1
2
Koniec petli
```

W praktyce ten mechanizm istnieje, ale na początku nie jest używany bardzo często.

Warto wiedzieć, że:

- `else` wykona się po normalnym zakończeniu pętli,
- jeśli pętla zostanie przerwana przez `break`, `else` się nie wykona.

---

## Pętle zagnieżdżone

Możesz mieć pętlę w pętli:

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

Output:

```python
0 0
0 1
1 0
1 1
2 0
2 1
```

To jest potrzebne np. do:

- tabliczek,
- pracy na siatkach,
- porównań wielu elementów.

Ale zbyt głębokie zagnieżdżenia pogarszają czytelność.

---

## Instrukcja `match case`

Od Pythona 3.10 istnieje `match case`.

Przykład:

```python
komenda = "start"

match komenda:
    case "start":
        print("Start")
    case "stop":
        print("Stop")
    case _:
        print("Nieznana komenda")
```

Output:

```python
Start
```

To coś w rodzaju bardziej uporządkowanego wyboru jednej z wielu opcji.

---

## Kiedy używać `match case`

Ma sens, gdy:

- porównujesz jedną wartość z wieloma możliwymi wariantami,
- budujesz menu komend,
- masz kilka jasno rozdzielonych przypadków.

Nie ma sensu używać go wszędzie na siłę.

---

## Porównanie `if elif else` i `match case`

`if elif else`:

- bardziej uniwersalne,
- dobre dla ogólnych warunków.

`match case`:

- lepsze przy wyborze jednego wariantu z wielu,
- bywa czytelniejsze przy komendach i prostych stanach.

---

## Typowe błędy początkujących

- złe wcięcia,
- zapomniany dwukropek,
- nieskończona pętla `while`,
- brak aktualizacji zmiennej sterującej w `while`,
- za bardzo zagnieżdżony kod,
- warunki, których nie da się łatwo przeczytać.

---

## Praktyczne przykłady

### Tabliczka mnożenia

```python
liczba = 5
for i in range(1, 11):
    print(liczba * i)
```

### 3 próby logowania

```python
proby = 3

while proby > 0:
    haslo = input("Haslo: ")
    if haslo == "python":
        print("OK")
        break
    proby -= 1
```

### Proste menu

```python
opcja = input("Wybierz: ")

match opcja:
    case "1":
        print("Dodawanie")
    case "2":
        print("Usuwanie")
    case _:
        print("Nieznana opcja")
```

---

## Dobre praktyki

- pilnuj wcięć,
- upraszczaj warunki,
- unikaj bardzo głębokich zagnieżdżeń,
- używaj `for`, gdy iterujesz po sekwencji,
- używaj `while`, gdy warunek zakończenia jest dynamiczny,
- używaj `break` i `continue` świadomie.

---

## Podsumowanie

Struktury sterujące to serce logiki programu.

Najważniejsze rzeczy do opanowania:

- `if`, `elif`, `else`,
- `for`, `while`,
- `break`, `continue`, `pass`,
- `range()`,
- podstawy `match case`.

---

## Mini ściąga

```python
if x > 0:
    print("plus")
elif x == 0:
    print("zero")
else:
    print("minus")

for i in range(5):
    print(i)

while x > 0:
    x -= 1
```

---

## Ćwiczenia

1. Sprawdź, czy liczba jest dodatnia, ujemna czy zero.
2. Wypisz liczby od 1 do 10 przez `for`.
3. Wypisz liczby od 10 do 1 przez `while`.
4. Zrób prosty kalkulator z `if elif else`.
5. Zrób proste menu przez `match case`.

---

## Przykładowe rozwiązania

### 1. Liczba

```python
if x > 0:
    print("dodatnia")
elif x == 0:
    print("zero")
else:
    print("ujemna")
```

### 2. `for`

```python
for i in range(1, 11):
    print(i)
```

### 3. `while`

```python
x = 10
while x > 0:
    print(x)
    x -= 1
```

### 4. Kalkulator

```python
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
```

### 5. `match case`

```python
match opcja:
    case "1":
        print("start")
    case _:
        print("brak")
```

---

## Antywzorce i pułapki z życia

### Antywzorzec 1: zbyt głębokie zagnieżdżenia

```python
if user:
    if user["active"]:
        if user["age"] >= 18:
            print("OK")
```

To jeszcze działa, ale szybko robi się trudne do czytania.

Często lepiej:

```python
if not user:
    return

if not user["active"]:
    return

if user["age"] < 18:
    return
```

To podejście nazywa się czasem guard clauses i bardzo poprawia czytelność.

### Antywzorzec 2: `while True` bez jasnego wyjścia

```python
while True:
    print("dziala")
```

Taka pętla bez `break` albo innego warunku końca szybko staje się błędem logicznym.

### Antywzorzec 3: zbyt sprytny warunek

```python
if (a and b) or (c and not d) and e:
    ...
```

Jeśli sam musisz patrzeć na to kilka sekund, to znaczy, że warto uprościć logikę albo rozbić warunek na zmienne pomocnicze.

---

## Mini case study

Załóżmy, że tworzysz prosty system logowania:

Chcesz:

- dać użytkownikowi 3 próby,
- zatrzymać program po sukcesie,
- zakończyć po 3 błędach.

To oznacza, że musisz połączyć:

- `while`,
- `if`,
- licznik prób,
- `break`.

Przykład:

```python
proby = 3

while proby > 0:
    haslo = input("Haslo: ")

    if haslo == "python":
        print("Zalogowano")
        break

    proby -= 1
    print("Bledne haslo")
else:
    print("Koniec prob")
```

To bardzo dobry przykład tego, że struktury sterujące nie istnieją osobno. W realnym kodzie zwykle łączysz kilka z nich naraz.

---

## Mini projekt po rozdziale

Zbuduj konsolowe menu:

- `1` dodawanie,
- `2` odejmowanie,
- `3` mnożenie,
- `4` wyjście.

Wymagania:

- użyj pętli `while`,
- użyj `match case` albo `if elif else`,
- po błędnej opcji pokaż komunikat i wróć do menu,
- zakończ program dopiero po wybraniu opcji wyjścia.

To małe zadanie scala:

- warunki,
- pętle,
- `break`,
- logikę wyboru ścieżki programu.
