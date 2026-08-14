# Set w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `set`](#czym-jest-set)
3. [Dlaczego set jest ważny](#dlaczego-set-jest-ważny)
4. [Najważniejsze cechy zbioru](#najważniejsze-cechy-zbioru)
5. [Jak utworzyć zbiór](#jak-utworzyć-zbiór)
6. [Pusty zbiór](#pusty-zbiór)
7. [Zbiór a duplikaty](#zbiór-a-duplikaty)
8. [Zbiór a kolejność elementów](#zbiór-a-kolejność-elementów)
9. [Typy danych w zbiorze](#typy-danych-w-zbiorze)
10. [Dodawanie elementów do zbioru](#dodawanie-elementów-do-zbioru)
11. [Usuwanie elementów ze zbioru](#usuwanie-elementów-ze-zbioru)
12. [Sprawdzanie obecności elementu](#sprawdzanie-obecności-elementu)
13. [Iterowanie po zbiorze](#iterowanie-po-zbiorze)
14. [Operacje matematyczne na zbiorach](#operacje-matematyczne-na-zbiorach)
15. [Suma zbiorów](#suma-zbiorów)
16. [Część wspólna zbiorów](#część-wspólna-zbiorów)
17. [Różnica zbiorów](#różnica-zbiorów)
18. [Różnica symetryczna](#różnica-symetryczna)
19. [Podzbiór i nadzbiór](#podzbiór-i-nadzbiór)
20. [Zbiory rozłączne](#zbiory-rozłączne)
21. [Metody zbiorów](#metody-zbiorów)
22. [Operacje modyfikujące zbiór](#operacje-modyfikujące-zbiór)
23. [Konwersja listy do zbioru](#konwersja-listy-do-zbioru)
24. [Usuwanie duplikatów przez `set`](#usuwanie-duplikatów-przez-set)
25. [`frozenset` - niemutowalny zbiór](#frozenset---niemutowalny-zbiór)
26. [Typowe błędy początkujących](#typowe-błędy-początkujących)
27. [Praktyczne przykłady](#praktyczne-przykłady)
28. [Dobre praktyki](#dobre-praktyki)
29. [Podsumowanie](#podsumowanie)
30. [Mini ściąga](#mini-ściąga)
31. [Ćwiczenia](#ćwiczenia)
32. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`set`, czyli zbiór, to bardzo przydatny typ danych w Pythonie.

Najlepiej sprawdza się wtedy, gdy:

- chcesz przechowywać unikalne elementy,
- nie interesują Cię duplikaty,
- chcesz szybko sprawdzać, czy coś istnieje,
- chcesz wykonywać operacje matematyczne na zbiorach.

To ostatnie jest szczególnie ważne, bo `set` bardzo dobrze odwzorowuje klasyczne działania znane z matematyki:

- suma zbiorów,
- część wspólna,
- różnica,
- różnica symetryczna,
- sprawdzanie podzbiorów i nadzbiorów.

W tym poradniku omówimy cały temat prostym językiem, z wieloma przykładami.

---

## Czym jest `set`

`set` to nieuporządkowany zbiór unikalnych elementów.

Najprościej:

**zbiór przechowuje elementy bez duplikatów.**

Przykład:

```python
liczby = {1, 2, 3, 4}
```

To jest zbiór czterech elementów.

### Co to oznacza w praktyce

- elementy nie mają indeksów jak lista,
- nie ma znaczenia kolejność,
- ten sam element nie może wystąpić więcej niż raz.

---

## Dlaczego set jest ważny

Zbiory są bardzo przydatne w wielu sytuacjach:

- usuwanie duplikatów z listy,
- porównywanie dwóch zestawów danych,
- sprawdzanie, co jest wspólne dla dwóch kolekcji,
- sprawdzanie, czego brakuje w jednej kolekcji względem drugiej,
- szybkie testowanie obecności elementu.

Przykład praktyczny:

```python
uczen_a = {"matematyka", "angielski", "informatyka"}
uczen_b = {"angielski", "biologia", "informatyka"}
```

Można łatwo sprawdzić:

- jakie przedmioty mają wspólne,
- jakie ma tylko jeden z nich,
- jakie ma drugi, a nie pierwszy.

---

## Najważniejsze cechy zbioru

### 1. Brak duplikatów

```python
liczby = {1, 2, 2, 3, 3, 3}
print(liczby)
```

Wynik:

```python
{1, 2, 3}
```

### 2. Brak indeksów

Nie możesz zrobić:

```python
liczby[0]
```

To da błąd.

### 3. Brak gwarantowanej kolejności

Zbiór nie zachowuje się jak lista.
Nie zakładaj, że elementy będą w konkretnej kolejności.

### 4. Elementy muszą być hashowalne

Najczęściej oznacza to, że muszą być niemutowalne.

Na przykład:

- `int` - tak,
- `str` - tak,
- `tuple` - zwykle tak,
- `list` - nie.

---

## Jak utworzyć zbiór

Najczęściej używa się nawiasów klamrowych:

```python
owoce = {"jablko", "banan", "gruszka"}
```

### Zbiór liczb

```python
liczby = {1, 2, 3, 4, 5}
```

### Zbiór tekstów

```python
kolory = {"czerwony", "zielony", "niebieski"}
```

---

## Pusty zbiór

To bardzo ważna pułapka.

Jeśli napiszesz:

```python
pusty = {}
```

to **nie** tworzysz pustego zbioru.
Tworzysz pusty słownik.

### Poprawnie:

```python
pusty = set()
```

### Sprawdzenie typu

```python
print(type({}))       # dict
print(type(set()))    # set
```

To jedna z najczęstszych pułapek przy nauce zbiorów.

---

## Zbiór a duplikaty

W zbiorze nie ma duplikatów.

Przykład:

```python
imiona = {"Ania", "Bartek", "Ania", "Celina"}
print(imiona)
```

`"Ania"` pojawi się tylko raz.

### Dlaczego to bywa przydatne

Bo można łatwo pozbyć się powtórzeń.

Przykład:

```python
liczby = [1, 2, 2, 3, 3, 4, 4, 4]
unikalne = set(liczby)
print(unikalne)
```

---

## Zbiór a kolejność elementów

Zbiór nie jest sekwencją uporządkowaną jak lista.

To oznacza, że:

- nie ma indeksów,
- nie możesz używać slicingu,
- nie powinieneś polegać na kolejności wypisywania.

Przykład:

```python
kolory = {"czerwony", "zielony", "niebieski"}
print(kolory)
```

Kolejność może wyglądać inaczej, niż wpisana w kodzie.

---

## Typy danych w zbiorze

Zbiór może zawierać tylko elementy hashowalne.

### Działa

```python
a = {1, 2, 3}
b = {"Ala", "Ola"}
c = {(1, 2), (3, 4)}
```

### Nie działa

```python
zly = {[1, 2], [3, 4]}
```

To da błąd, bo lista jest mutowalna i nie może być elementem zwykłego `set`.

### Można mieszać typy

```python
dane = {1, "Python", True}
```

Ale jak zwykle, czytelność bywa ważniejsza niż sama możliwość techniczna.

---

## Dodawanie elementów do zbioru

### `add()`

Dodaje jeden element.

```python
liczby = {1, 2, 3}
liczby.add(4)
print(liczby)
```

### Dodanie istniejącego elementu

```python
liczby.add(4)
```

Nic złego się nie stanie.
Zbiór po prostu nadal będzie miał `4` tylko raz.

### `update()`

Dodaje wiele elementów naraz.

```python
liczby = {1, 2, 3}
liczby.update([4, 5, 6])
print(liczby)
```

Można przekazać:

- listę,
- tuple,
- inny zbiór.

---

## Usuwanie elementów ze zbioru

### `remove()`

Usuwa element.

```python
liczby = {1, 2, 3}
liczby.remove(2)
print(liczby)
```

### Uwaga

Jeśli elementu nie ma, `remove()` da błąd `KeyError`.

### `discard()`

Też usuwa element, ale bez błędu, jeśli go nie ma.

```python
liczby.discard(10)
```

### `pop()`

Usuwa i zwraca jakiś element, ale ponieważ zbiór nie ma ustalonej kolejności, nie wiadomo dokładnie który.

```python
element = liczby.pop()
print(element)
```

### `clear()`

Usuwa wszystkie elementy.

```python
liczby.clear()
```

---

## Sprawdzanie obecności elementu

Operator `in` działa bardzo dobrze ze zbiorami.

```python
owoce = {"jablko", "banan", "gruszka"}

print("banan" in owoce)
print("kiwi" in owoce)
```

To jedna z praktycznych zalet `set`.

---

## Iterowanie po zbiorze

Po zbiorze można przechodzić pętlą `for`.

```python
kolory = {"czerwony", "zielony", "niebieski"}

for kolor in kolory:
    print(kolor)
```

### Uwaga

Nie zakładaj konkretnej kolejności wypisywania.

Jeśli potrzebujesz kolejności, możesz wcześniej posortować:

```python
for kolor in sorted(kolory):
    print(kolor)
```

---

## Operacje matematyczne na zbiorach

To najważniejsza część tematu.

Załóżmy:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
```

Na tych dwóch zbiorach można wykonywać działania podobne do matematyki.

Najważniejsze:

- suma,
- część wspólna,
- różnica,
- różnica symetryczna.

---

## Suma zbiorów

Suma zbiorów to wszystkie elementy z obu zbiorów, bez duplikatów.

### Operator `|`

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
```

Wynik:

```python
{1, 2, 3, 4, 5}
```

### Metoda `union()`

```python
print(a.union(b))
```

To daje ten sam efekt.

### Jak to rozumieć

Weź wszystko, co jest w `a` i wszystko, co jest w `b`, ale każdy element tylko raz.

---

## Część wspólna zbiorów

Część wspólna to elementy, które występują w obu zbiorach.

### Operator `&`

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a & b)
```

Wynik:

```python
{3, 4}
```

### Metoda `intersection()`

```python
print(a.intersection(b))
```

### Praktyczne znaczenie

To bardzo przydatne, gdy chcesz sprawdzić, co dwa zbiory mają wspólnego.

Na przykład:

- wspólne zainteresowania,
- wspólne przedmioty,
- wspólne identyfikatory,
- wspólne elementy w dwóch listach po zamianie na zbiory.

---

## Różnica zbiorów

Różnica pokazuje elementy, które są w jednym zbiorze, ale nie ma ich w drugim.

### Operator `-`

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a - b)
```

Wynik:

```python
{1, 2}
```

To elementy, które są w `a`, ale nie ma ich w `b`.

### W drugą stronę

```python
print(b - a)
```

Wynik:

```python
{5, 6}
```

### Metoda `difference()`

```python
print(a.difference(b))
```

### Ważne

Różnica nie jest symetryczna.

To znaczy:

```python
a - b
```

to nie to samo co:

```python
b - a
```

---

## Różnica symetryczna

Różnica symetryczna to elementy, które są w jednym albo w drugim zbiorze, ale nie w obu naraz.

### Operator `^`

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a ^ b)
```

Wynik:

```python
{1, 2, 5, 6}
```

### Metoda `symmetric_difference()`

```python
print(a.symmetric_difference(b))
```

### Jak to rozumieć

To elementy, które są "różne" między zbiorami.

---

## Podzbiór i nadzbiór

### Podzbiór

Zbiór `a` jest podzbiorem `b`, jeśli wszystkie elementy `a` są w `b`.

Przykład:

```python
a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))
```

Wynik:

```python
True
```

### Operator `<=`

```python
print(a <= b)
```

### Nadzbiór

Zbiór `b` jest nadzbiorem `a`, jeśli zawiera wszystkie elementy `a`.

```python
print(b.issuperset(a))
print(b >= a)
```

### Ścisły podzbiór i nadzbiór

```python
print(a < b)
print(b > a)
```

To oznacza podzbiór i nadzbiór bez równości.

---

## Zbiory rozłączne

Dwa zbiory są rozłączne, jeśli nie mają żadnych wspólnych elementów.

Przykład:

```python
a = {1, 2}
b = {3, 4}

print(a.isdisjoint(b))
```

Wynik:

```python
True
```

### Praktyczne znaczenie

To sposób na sprawdzenie, czy dwa zbiory nie nakładają się na siebie.

---

## Metody zbiorów

Najważniejsze metody:

- `add()`
- `update()`
- `remove()`
- `discard()`
- `pop()`
- `clear()`
- `union()`
- `intersection()`
- `difference()`
- `symmetric_difference()`
- `issubset()`
- `issuperset()`
- `isdisjoint()`

To właśnie one odpowiadają za codzienną pracę ze zbiorami.

---

## Operacje modyfikujące zbiór

Są też metody, które zmieniają zbiór "w miejscu".

### `intersection_update()`

Zostawia tylko część wspólną.

```python
a = {1, 2, 3, 4}
b = {3, 4, 5}

a.intersection_update(b)
print(a)
```

### `difference_update()`

Usuwa z `a` elementy, które są w `b`.

```python
a = {1, 2, 3, 4}
b = {3, 4}

a.difference_update(b)
print(a)
```

### `symmetric_difference_update()`

Zostawia tylko elementy różne.

```python
a = {1, 2, 3}
b = {3, 4, 5}

a.symmetric_difference_update(b)
print(a)
```

---

## Konwersja listy do zbioru

To bardzo częsty przypadek.

```python
liczby = [1, 2, 2, 3, 3, 4]
zbior = set(liczby)
print(zbior)
```

### Po co to robić

Najczęściej po to, żeby:

- usunąć duplikaty,
- robić operacje matematyczne na danych,
- szybciej sprawdzać obecność elementów.

---

## Usuwanie duplikatów przez `set`

Przykład:

```python
imiona = ["Ania", "Bartek", "Ania", "Celina", "Bartek"]
unikalne = set(imiona)
print(unikalne)
```

### Jeśli chcesz z powrotem listę

```python
lista_bez_duplikatow = list(set(imiona))
```

### Uwaga

Po takiej operacji kolejność elementów może być inna niż w oryginalnej liście.

To bardzo ważne.

---

## `frozenset` - niemutowalny zbiór

Python ma też `frozenset`, czyli niemutowalną wersję zbioru.

Przykład:

```python
a = frozenset([1, 2, 3])
print(a)
```

### Czego nie można robić

Nie można:

- dodawać elementów,
- usuwać elementów,
- modyfikować zbioru.

### Po co to istnieje

Na przykład po to, by:

- używać zbiorów jako elementów innych zbiorów,
- używać zbiorów jako kluczy słownika,
- zabezpieczyć dane przed zmianą.

---

## Typowe błędy początkujących

### 1. Mylenie `{}` z pustym `set`

`{}` to słownik, nie zbiór.

### 2. Próba indeksowania zbioru

```python
zbior[0]
```

To nie działa.

### 3. Zakładanie kolejności elementów

Zbiór nie działa jak lista.

### 4. Dodawanie listy do zbioru

```python
zbior.add([1, 2])
```

To da błąd, bo lista jest mutowalna.

### 5. Użycie `remove()` dla nieistniejącego elementu

To da `KeyError`.

### 6. Oczekiwanie, że `set` zachowa kolejność przy usuwaniu duplikatów

Nie zachowa.

### 7. Mylenie różnicy z różnicą symetryczną

`a - b` to nie to samo co `a ^ b`.

---

## Praktyczne przykłady

### Usuwanie duplikatów z listy

```python
liczby = [1, 2, 2, 3, 3, 4]
unikalne = set(liczby)
print(unikalne)
```

### Wspólne elementy dwóch list

```python
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

wspolne = set(a) & set(b)
print(wspolne)
```

### Elementy tylko w pierwszej liście

```python
tylko_w_a = set(a) - set(b)
print(tylko_w_a)
```

### Wszystkie unikalne elementy z obu list

```python
wszystkie = set(a) | set(b)
print(wszystkie)
```

### Sprawdzenie, czy dwa zbiory są rozłączne

```python
przedmioty_a = {"matematyka", "fizyka"}
przedmioty_b = {"biologia", "chemia"}

print(przedmioty_a.isdisjoint(przedmioty_b))
```

### Sprawdzenie podzbioru

```python
a = {1, 2}
b = {1, 2, 3, 4}

print(a <= b)
```

---

## Dobre praktyki

### Używaj `set`, gdy liczy się unikalność

To podstawowe zastosowanie.

### Używaj `set`, gdy potrzebujesz operacji matematycznych na kolekcjach

To jeden z największych powodów, dla których ten typ istnieje.

### Nie używaj `set`, gdy potrzebujesz zachować kolejność

Wtedy lepsza będzie lista albo inna struktura.

### Używaj `discard()` zamiast `remove()`, jeśli element może nie istnieć

To pozwala uniknąć niepotrzebnych błędów.

### Zamieniaj listy na `set`, gdy chcesz szybko porównywać kolekcje

To często upraszcza kod.

### Jeśli potrzebujesz kolejności po operacjach na zbiorach, posortuj wynik

```python
print(sorted(a | b))
```

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- `set` to zbiór unikalnych elementów,
- zbiór nie ma indeksów i nie gwarantuje kolejności,
- pusty zbiór tworzy się przez `set()`,
- `add()` i `update()` dodają elementy,
- `remove()`, `discard()`, `pop()`, `clear()` usuwają elementy,
- najważniejsze operacje matematyczne to suma, część wspólna, różnica i różnica symetryczna,
- `|`, `&`, `-`, `^` to bardzo ważne operatory zbiorów,
- `set` świetnie nadaje się do usuwania duplikatów i porównywania kolekcji,
- `frozenset` to niemutowalna wersja zbioru.

Jeśli dobrze opanujesz `set`, będziesz bardzo sprawnie rozwiązywać wiele problemów związanych z unikalnością danych i porównywaniem kolekcji.

---

## Mini ściąga

### Tworzenie zbioru

```python
zbior = {1, 2, 3}
```

### Pusty zbiór

```python
pusty = set()
```

### Dodawanie i usuwanie

```python
zbior.add(4)
zbior.update([5, 6])
zbior.remove(2)
zbior.discard(10)
zbior.pop()
zbior.clear()
```

### Operacje matematyczne

```python
a | b   # suma
a & b   # czesc wspolna
a - b   # roznica
a ^ b   # roznica symetryczna
```

### Metody

```python
a.union(b)
a.intersection(b)
a.difference(b)
a.symmetric_difference(b)
a.issubset(b)
a.issuperset(b)
a.isdisjoint(b)
```

### Konwersja

```python
set([1, 2, 2, 3])
list(set([1, 2, 2, 3]))
```

---

## Ćwiczenia

### Ćwiczenie 1

Utwórz zbiór liczb i:

- dodaj nowy element,
- usuń jeden element,
- sprawdź, czy liczba `5` jest w zbiorze.

### Ćwiczenie 2

Dla zbiorów:

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
```

oblicz:

- sumę,
- część wspólną,
- różnicę `a - b`,
- różnicę `b - a`,
- różnicę symetryczną.

### Ćwiczenie 3

Z listy z duplikatami utwórz zbiór bez powtórzeń.

### Ćwiczenie 4

Sprawdź, czy zbiór `{1, 2}` jest podzbiorem `{1, 2, 3, 4}`.

### Ćwiczenie 5

Sprawdź, czy zbiory `{1, 2}` i `{3, 4}` są rozłączne.

### Ćwiczenie 6

Utwórz `frozenset` i sprawdź, co się stanie, gdy spróbujesz coś do niego dodać.

---

## Przykładowe rozwiązania

### Ćwiczenie 1

```python
liczby = {1, 2, 3, 4}

liczby.add(5)
liczby.remove(2)

print(5 in liczby)
print(liczby)
```

### Ćwiczenie 2

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)
print(a & b)
print(a - b)
print(b - a)
print(a ^ b)
```

### Ćwiczenie 3

```python
lista = [1, 2, 2, 3, 3, 4]
zbior = set(lista)
print(zbior)
```

### Ćwiczenie 4

```python
print({1, 2}.issubset({1, 2, 3, 4}))
print({1, 2} <= {1, 2, 3, 4})
```

### Ćwiczenie 5

```python
print({1, 2}.isdisjoint({3, 4}))
```

### Ćwiczenie 6

```python
a = frozenset([1, 2, 3])

# a.add(4)  # blad, bo frozenset jest niemutowalny
print(a)
```

---

## Na koniec

Najlepszy sposób nauki `set` to praktyka na porównywaniu różnych kolekcji.

Warto:

1. tworzyć zbiory z list zawierających duplikaty,
2. ćwiczyć `|`, `&`, `-`, `^`,
3. sprawdzać różnicę między `remove()` i `discard()`,
4. testować podzbiory i zbiory rozłączne,
5. porównywać zachowanie `set` i `list`.

Wtedy bardzo szybko staje się jasne, dlaczego zbiory są tak wygodnym narzędziem w Pythonie.
