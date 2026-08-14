# Zagnieżdżone Comprehensions w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym są zagnieżdżone comprehensions](#czym-są-zagnieżdżone-comprehensions)
3. [Dlaczego ten temat bywa trudny](#dlaczego-ten-temat-bywa-trudny)
4. [Najpierw zwykła comprehension](#najpierw-zwykła-comprehension)
5. [Dwie pętle w jednej comprehension](#dwie-pętle-w-jednej-comprehension)
6. [Jak czytać zagnieżdżoną comprehension](#jak-czytać-zagnieżdżoną-comprehension)
7. [Tworzenie kombinacji elementów](#tworzenie-kombinacji-elementów)
8. [Spłaszczanie listy list](#spłaszczanie-listy-list)
9. [Macierze i zagnieżdżone listy](#macierze-i-zagnieżdżone-listy)
10. [Warunki w zagnieżdżonych comprehensions](#warunki-w-zagnieżdżonych-comprehensions)
11. [If else w zagnieżdżonych comprehensions](#if-else-w-zagnieżdżonych-comprehensions)
12. [Zagnieżdżone dict comprehensions](#zagnieżdżone-dict-comprehensions)
13. [Zagnieżdżone set comprehensions](#zagnieżdżone-set-comprehensions)
14. [Kiedy używać](#kiedy-używać)
15. [Kiedy nie używać](#kiedy-nie-używać)
16. [Typowe błędy początkujących](#typowe-błędy-początkujących)
17. [Praktyczne przykłady](#praktyczne-przykłady)
18. [Dobre praktyki](#dobre-praktyki)
19. [Podsumowanie](#podsumowanie)
20. [Mini ściąga](#mini-ściąga)
21. [Ćwiczenia](#ćwiczenia)
22. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Zagnieżdżone comprehensions to bardziej zaawansowana wersja zwykłych comprehensions.

Pozwalają wykonywać operacje, które normalnie wymagałyby:

- pętli w pętli,
- pracy na listach zagnieżdżonych,
- tworzenia kombinacji elementów,
- spłaszczania danych.

To bardzo przydatne narzędzie, ale łatwo przesadzić i napisać kod, który jest bardziej zagmatwany niż pomocny.

Dlatego w tym poradniku skupimy się nie tylko na składni, ale też na tym, jak to czytać i kiedy ma to sens.

---

## Czym są zagnieżdżone comprehensions

To comprehensions, w których występuje więcej niż jedna pętla `for`, albo comprehension znajduje się wewnątrz innej comprehension.

Przykład:

```python
pary = [(x, y) for x in [1, 2, 3] for y in [10, 20]]
print(pary)
```

To odpowiednik zwykłego kodu:

```python
pary = []

for x in [1, 2, 3]:
    for y in [10, 20]:
        pary.append((x, y))
```

---

## Dlaczego ten temat bywa trudny

Bo składnia jest krótka, ale logika może być wielopoziomowa.

Początkujący często widzą:

```python
[... for x in ... for y in ...]
```

i nie wiedzą:

- która pętla jest pierwsza,
- skąd bierze się dana zmienna,
- kiedy działa warunek,
- czy wynik jest listą płaską, czy listą list.

Dlatego najlepiej zawsze tłumaczyć sobie taki zapis przez zwykłe pętle.

---

## Najpierw zwykła comprehension

Zanim przejdziesz do zagnieżdżonych wersji, przypomnijmy prosty schemat:

```python
[wyrazenie for x in kolekcja]
```

Zagnieżdżona wersja rozszerza ten pomysł.

---

## Dwie pętle w jednej comprehension

Ogólny schemat:

```python
[wyrazenie for x in kolekcja1 for y in kolekcja2]
```

Przykład:

```python
wynik = [(x, y) for x in [1, 2] for y in ["a", "b"]]
print(wynik)
```

Wynik:

```python
[(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
```

### Jak to działa

Najpierw Python bierze `x = 1`, a potem dla tego `x` przechodzi po wszystkich `y`.
Potem bierze `x = 2` i znowu przechodzi po wszystkich `y`.

---

## Jak czytać zagnieżdżoną comprehension

Bardzo dobra zasada:

czytaj ją od lewej do prawej, ale logikę pętli rozpisuj jak zwykły `for`.

Przykład:

```python
[(x, y) for x in [1, 2] for y in [10, 20]]
```

czytaj tak:

1. dla każdego `x` w `[1, 2]`,
2. dla każdego `y` w `[10, 20]`,
3. dodaj `(x, y)` do wyniku.

---

## Tworzenie kombinacji elementów

To jedno z najczęstszych zastosowań.

Przykład:

```python
kolory = ["czerwony", "zielony"]
rozmiary = ["S", "M", "L"]

kombinacje = [(kolor, rozmiar) for kolor in kolory for rozmiar in rozmiary]
print(kombinacje)
```

To bardzo wygodne przy generowaniu wszystkich par, układów albo możliwych wariantów.

---

## Spłaszczanie listy list

To kolejne bardzo ważne zastosowanie.

Mamy:

```python
lista_list = [[1, 2], [3, 4], [5, 6]]
```

Chcemy dostać:

```python
[1, 2, 3, 4, 5, 6]
```

Można tak:

```python
splaszczona = [element for podlista in lista_list for element in podlista]
print(splaszczona)
```

### Odpowiednik zwykłej pętli

```python
splaszczona = []

for podlista in lista_list:
    for element in podlista:
        splaszczona.append(element)
```

---

## Macierze i zagnieżdżone listy

Zagnieżdżone comprehensions są często używane przy pracy z macierzami.

Przykład:

```python
macierz = [
    [1, 2, 3],
    [4, 5, 6]
]

podwojona = [[x * 2 for x in wiersz] for wiersz in macierz]
print(podwojona)
```

Wynik:

```python
[[2, 4, 6], [8, 10, 12]]
```

Tutaj mamy comprehension wewnątrz comprehension.

---

## Warunki w zagnieżdżonych comprehensions

Można dodawać warunki filtrowania.

Przykład:

```python
pary = [(x, y) for x in [1, 2, 3] for y in [10, 20, 30] if x + y > 22]
print(pary)
```

Warunek odnosi się do aktualnych wartości `x` i `y`.

### Spłaszczanie z filtrem

```python
lista_list = [[1, 2], [3, 4], [5, 6]]
parzyste = [x for podlista in lista_list for x in podlista if x % 2 == 0]
print(parzyste)
```

---

## If else w zagnieżdżonych comprehensions

Można też użyć wyrażenia warunkowego.

Przykład:

```python
macierz = [[1, 2], [3, 4]]
etykiety = [["parzysta" if x % 2 == 0 else "nieparzysta" for x in wiersz] for wiersz in macierz]
print(etykiety)
```

To działa, ale przy bardziej skomplikowanych przypadkach może już robić się mało czytelne.

---

## Zagnieżdżone dict comprehensions

Też są możliwe, choć rzadziej spotykane.

Przykład:

```python
macierz = [[1, 2], [3, 4]]
slownik = {i: {j: wartosc for j, wartosc in enumerate(wiersz)} for i, wiersz in enumerate(macierz)}
print(slownik)
```

To przykład bardziej zaawansowany.

Na początku ważniejsze jest zrozumienie samej idei niż zapamiętywanie takich form.

---

## Zagnieżdżone set comprehensions

Można też budować zbiory na podstawie zagnieżdżonych danych.

Przykład:

```python
lista_list = [[1, 2], [2, 3], [3, 4]]
unikalne = {x for podlista in lista_list for x in podlista}
print(unikalne)
```

Wynik:

```python
{1, 2, 3, 4}
```

To bardzo wygodny sposób spłaszczenia i jednoczesnego usunięcia duplikatów.

---

## Kiedy używać

Zagnieżdżone comprehensions są dobrym wyborem, gdy:

- masz prostą pętlę w pętli,
- chcesz spłaszczyć listę list,
- generujesz kombinacje,
- logika nadal mieści się w czytelnej formie.

---

## Kiedy nie używać

Nie używaj ich, gdy:

- zapis robi się trudny do zrozumienia,
- jest wiele warunków,
- jest kilka poziomów zagnieżdżeń,
- potrzebujesz debugować każdy krok,
- ktoś czytający kod będzie musiał długo zgadywać, co się dzieje.

W takich przypadkach zwykłe pętle są często lepsze.

---

## Typowe błędy początkujących

### 1. Mylenie kolejności pętli

To bardzo częsty problem.

### 2. Nierozumienie, czy wynik ma być listą płaską czy listą list

To zależy od miejsca comprehension i od struktury wyrażenia.

### 3. Robienie zbyt skomplikowanych zapisów

Krótki zapis może być trudniejszy niż zwykła pętla.

### 4. Złe miejsce warunku `if`

Warunek na końcu filtruje wynik, a nie zastępuje `if else`.

### 5. Zbyt szybkie przechodzenie do wersji zagnieżdżonych bez zrozumienia zwykłych comprehensions

Najpierw trzeba dobrze czuć prosty schemat.

---

## Praktyczne przykłady

### Wszystkie pary liczb

```python
pary = [(x, y) for x in [1, 2, 3] for y in [4, 5]]
print(pary)
```

### Spłaszczona lista

```python
lista_list = [[1, 2], [3, 4], [5, 6]]
wynik = [x for podlista in lista_list for x in podlista]
print(wynik)
```

### Tylko liczby dodatnie ze złożonej struktury

```python
lista_list = [[-1, 2], [3, -4], [5, 0]]
wynik = [x for podlista in lista_list for x in podlista if x > 0]
print(wynik)
```

### Podwojona macierz

```python
macierz = [[1, 2], [3, 4]]
wynik = [[x * 2 for x in wiersz] for wiersz in macierz]
print(wynik)
```

---

## Dobre praktyki

### Zawsze umiej rozpisać comprehension na zwykłe pętle

To najlepszy test, czy rozumiesz kod.

### Nie rób więcej niż 2 poziomy, jeśli nie jest to naprawdę potrzebne

Potem czytelność zwykle mocno spada.

### Używaj sensownych nazw

`wiersz`, `element`, `kolor`, `rozmiar` są lepsze niż same `x`, `y`, `z`, jeśli kontekst jest bardziej złożony.

### Jeśli zapis męczy wzrok, wróć do zwykłej pętli

To bardzo dobra praktyczna zasada.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- zagnieżdżone comprehensions odpowiadają pętlom w pętlach,
- można ich używać do kombinacji, spłaszczania i pracy na macierzach,
- warunki i `if else` nadal działają, ale zwiększają złożoność zapisu,
- trzeba bardzo uważać na czytelność,
- jeśli kod robi się zbyt złożony, zwykła pętla będzie lepsza.

Jeśli dobrze opanujesz ten temat, zyskasz bardzo wygodne narzędzie do pracy na danych zagnieżdżonych.

---

## Mini ściąga

### Dwie pętle

```python
[wyrazenie for x in a for y in b]
```

### Spłaszczanie

```python
[x for podlista in lista_list for x in podlista]
```

### Z warunkiem

```python
[x for podlista in lista_list for x in podlista if x > 0]
```

### Lista list

```python
[[x * 2 for x in wiersz] for wiersz in macierz]
```

---

## Ćwiczenia

### Ćwiczenie 1

Utwórz listę wszystkich par `(x, y)` dla `x` od 1 do 3 i `y` od 10 do 12.

### Ćwiczenie 2

Spłaszcz listę:

```python
[[1, 2], [3, 4], [5, 6]]
```

### Ćwiczenie 3

Z listy list wybierz tylko liczby parzyste.

### Ćwiczenie 4

Utwórz nową macierz, w której każdy element oryginalnej macierzy zostanie pomnożony przez 3.

### Ćwiczenie 5

Z dwóch list:

```python
kolory = ["czerwony", "zielony"]
rozmiary = ["S", "M"]
```

utwórz wszystkie kombinacje.

---

## Przykładowe rozwiązania

### Ćwiczenie 1

```python
pary = [(x, y) for x in range(1, 4) for y in range(10, 13)]
print(pary)
```

### Ćwiczenie 2

```python
lista_list = [[1, 2], [3, 4], [5, 6]]
wynik = [x for podlista in lista_list for x in podlista]
print(wynik)
```

### Ćwiczenie 3

```python
lista_list = [[1, 2], [3, 4], [5, 6]]
parzyste = [x for podlista in lista_list for x in podlista if x % 2 == 0]
print(parzyste)
```

### Ćwiczenie 4

```python
macierz = [[1, 2], [3, 4]]
wynik = [[x * 3 for x in wiersz] for wiersz in macierz]
print(wynik)
```

### Ćwiczenie 5

```python
kolory = ["czerwony", "zielony"]
rozmiary = ["S", "M"]
kombinacje = [(kolor, rozmiar) for kolor in kolory for rozmiar in rozmiary]
print(kombinacje)
```

---

## Na koniec

Najlepiej uczyć się zagnieżdżonych comprehensions przez tłumaczenie ich na zwykłe pętle `for`.

Warto:

1. brać prosty przykład,
2. zapisać go jako zwykłe pętle,
3. przepisać do comprehension,
4. porównać oba zapisy.

To najszybciej buduje intuicję, co dokładnie dzieje się w takim kodzie.
