# `enumerate`, `zip`, `sorted`, `any`, `all` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co znać te funkcje](#po-co-znać-te-funkcje)
3. [`enumerate()`](#enumerate)
4. [`zip()`](#zip)
5. [`sorted()`](#sorted)
6. [`sorted()` kontra `list.sort()`](#sorted-kontra-listsort)
7. [Stabilność sortowania](#stabilność-sortowania)
8. [`any()`](#any)
9. [`all()`](#all)
10. [Puste iterowalne w `any()` i `all()`](#puste-iterowalne-w-any-i-all)
11. [Jak te funkcje łączą się z idiomami Pythona](#jak-te-funkcje-łączą-się-z-idiomami-pythona)
12. [Typowe pułapki początkujących](#typowe-pułapki-początkujących)
13. [Praktyczne przykłady](#praktyczne-przykłady)
14. [Dobre praktyki](#dobre-praktyki)
15. [Podsumowanie](#podsumowanie)
16. [Mini ściąga](#mini-ściąga)
17. [Ćwiczenia](#ćwiczenia)
18. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Te funkcje są małe, ale bardzo praktyczne. Bardzo często pojawiają się w prawdziwym kodzie.

Jeśli je dobrze opanujesz, Twój kod będzie:

- krótszy,
- czytelniejszy,
- bardziej idiomatyczny,
- mniej ręczny.

---

## Po co znać te funkcje

Bo pozwalają zastąpić:

- ręczne liczniki,
- pętle po indeksach,
- chaotyczne sklejanie list,
- rozwlekłe warunki.

To są narzędzia codziennego użytku w Pythonie.

---

## `enumerate()`

`enumerate()` pozwala iterować po elementach wraz z ich numerem.

```python
slowa = ["a", "b", "c"]

for i, slowo in enumerate(slowa):
    print(i, slowo)
```

Możesz ustawić start:

```python
for i, slowo in enumerate(slowa, start=1):
    print(i, slowo)
```

Output:

```python
1 a
2 b
3 c
```

To zwykle lepsze niż ręczne zarządzanie licznikiem.

---

## `zip()`

`zip()` łączy kilka iterowalnych obiektów element po elemencie.

```python
imiona = ["Anna", "Jan"]
wieki = [30, 25]

for imie, wiek in zip(imiona, wieki):
    print(imie, wiek)
```

Ważne:

- `zip()` kończy się na najkrótszej kolekcji,
- możesz go używać w pętlach,
- możesz zamienić wynik na listę przez `list(zip(...))`.

Przykład:

```python
print(list(zip([1, 2, 3], ["a", "b"])))
```

Output:

```python
[(1, 'a'), (2, 'b')]
```

---

## `sorted()`

`sorted()` zwraca nową posortowaną listę.

```python
liczby = [3, 1, 2]
print(sorted(liczby))
print(liczby)
```

Output:

```python
[1, 2, 3]
[3, 1, 2]
```

Możesz sortować:

- rosnąco,
- malejąco przez `reverse=True`,
- po kluczu przez `key=...`.

```python
slowa = ["python", "a", "programowanie"]
print(sorted(slowa, key=len))
print(sorted(slowa, reverse=True))
```

---

## `sorted()` kontra `list.sort()`

To bardzo ważna różnica.

`sorted()`:

- działa na różnych iterowalnych obiektach,
- zwraca nową listę,
- nie zmienia oryginału.

`lista.sort()`:

- działa tylko na listach,
- sortuje w miejscu,
- zwraca `None`.

Przykład:

```python
liczby = [3, 1, 2]
wynik = sorted(liczby)
print(liczby)
print(wynik)
```

Output:

```python
[3, 1, 2]
[1, 2, 3]
```

```python
liczby = [3, 1, 2]
wynik = liczby.sort()
print(liczby)
print(wynik)
```

Output:

```python
[1, 2, 3]
None
```

To drugi przykład bardzo często myli początkujących.

---

## Stabilność sortowania

Python sortuje stabilnie.

To znaczy: jeśli dwa elementy mają ten sam klucz sortowania, zachowują wzajemną kolejność z wejścia.

To brzmi technicznie, ale bywa bardzo przydatne przy wieloetapowym sortowaniu.

Na tym etapie wystarczy wiedzieć, że `sorted()` jest przewidywalne i dobrze zaprojektowane.

---

## `any()`

`any()` zwraca `True`, jeśli przynajmniej jeden element jest truthy.

```python
print(any([False, False, True]))
```

Przydaje się też z warunkiem:

```python
liczby = [-3, -1, 4]
print(any(x > 0 for x in liczby))
```

To pyta:

"czy istnieje choć jeden element spełniający warunek?"

---

## `all()`

`all()` zwraca `True`, jeśli wszystkie elementy są truthy.

```python
print(all([True, True, True]))
```

Z warunkiem:

```python
liczby = [2, 4, 6]
print(all(x % 2 == 0 for x in liczby))
```

To pyta:

"czy każdy element spełnia warunek?"

---

## Puste iterowalne w `any()` i `all()`

To ważny edge case.

```python
print(any([]))
print(all([]))
```

Output:

```python
False
True
```

Wynik:

- `any([])` to `False`
- `all([])` to `True`

To może wydawać się dziwne, ale wynika z logicznej definicji tych funkcji.

W praktyce oznacza to, że czasem przed użyciem `all()` warto się zastanowić, czy pusta lista powinna być traktowana jako "wszystko spełnia warunek".

---

## Jak te funkcje łączą się z idiomami Pythona

To ważna część stylu języka:

- `enumerate()` zamiast ręcznego licznika,
- `zip()` zamiast synchronizowania indeksów,
- `sorted(..., key=...)` zamiast pisania własnej logiki sortowania,
- `any()` i `all()` zamiast flag ustawianych w pętli.

To właśnie sprawia, że kod jest bardziej pythonowy.

---

## Typowe pułapki początkujących

- używanie `range(len(...))` tam, gdzie lepsze jest `enumerate()`,
- zapominanie, że `zip()` ucina do najkrótszej sekwencji,
- mylenie `sorted()` z `sort()`,
- używanie `any(lista)` wtedy, gdy chodzi o `any(x > 0 for x in lista)`,
- używanie `all(lista)` bez zrozumienia truthy/falsy,
- brak świadomości, że `list.sort()` zwraca `None`.

---

## Praktyczne przykłady

### Numerowanie listy

```python
produkty = ["chleb", "mleko", "ser"]
for nr, produkt in enumerate(produkty, start=1):
    print(nr, produkt)
```

### Łączenie imion i punktów

```python
imiona = ["Ania", "Bartek"]
punkty = [10, 15]

for imie, punkt in zip(imiona, punkty):
    print(f"{imie} ma {punkt} punktow")
```

### Sortowanie po długości

```python
slowa = ["dom", "samochod", "kot"]
print(sorted(slowa, key=len))
```

### Czy istnieje liczba dodatnia

```python
liczby = [-2, -1, 0, 5]
print(any(x > 0 for x in liczby))
```

### Czy wszystkie liczby są dodatnie

```python
liczby = [1, 2, 3]
print(all(x > 0 for x in liczby))
```

---

## Dobre praktyki

- używaj `enumerate()` do numerowania,
- używaj `zip()` do łączenia odpowiadających sobie danych,
- używaj `sorted(..., key=...)`, gdy chcesz czytelnie opisać sposób sortowania,
- przy `any()` i `all()` jasno pokazuj warunek,
- nie komplikuj prostych pętli ręcznym zarządzaniem indeksem.

---

## Podsumowanie

Te funkcje są małe, ale bardzo wzmacniają czytelność kodu.

Jeśli dobrze je rozumiesz, szybciej przechodzisz od "kod działa" do "kod wygląda jak Python".

---

## Mini ściąga

```python
for i, x in enumerate(lista, start=1):
    print(i, x)

for a, b in zip(lista1, lista2):
    print(a, b)

print(sorted(lista, key=len))
print(any(x > 0 for x in liczby))
print(all(x > 0 for x in liczby))
```

---

## Ćwiczenia

1. Użyj `enumerate()` do wypisania numerów i wartości listy.
2. Użyj `zip()` do połączenia dwóch list i wypisz wszystkie pary.
3. Posortuj listę słów po długości.
4. Sprawdź `any()`, czy istnieje liczba ujemna.
5. Sprawdź `all()`, czy wszystkie liczby są parzyste.
6. Pokaż różnicę między `sorted()` i `.sort()`.

---

## Przykładowe rozwiązania

### 1. `enumerate()`

```python
for i, x in enumerate(["a", "b", "c"], start=1):
    print(i, x)
```

### 2. `zip()`

```python
for imie, punkt in zip(["Ania", "Jan"], [10, 20]):
    print(imie, punkt)
```

### 3. `sorted()`

```python
slowa = ["python", "a", "kod"]
print(sorted(slowa, key=len))
```

### 4. `any()`

```python
liczby = [1, 2, -3]
print(any(x < 0 for x in liczby))
```

### 5. `all()`

```python
liczby = [2, 4, 6]
print(all(x % 2 == 0 for x in liczby))
```

### 6. `sort()`

```python
liczby = [3, 1, 2]
print(sorted(liczby))
liczby.sort()
print(liczby)
```
