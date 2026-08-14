# CPython i model pamięci w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest CPython](#czym-jest-cpython)
3. [Dlaczego warto znać model pamięci](#dlaczego-warto-znać-model-pamięci)
4. [Obiekty i referencje](#obiekty-i-referencje)
5. [Referencje a zmienne](#referencje-a-zmienne)
6. [GIL](#gil)
7. [Co GIL robi naprawdę](#co-gil-robi-naprawdę)
8. [Garbage collector](#garbage-collector)
9. [Reference counting](#reference-counting)
10. [Cykle referencji](#cykle-referencji)
11. [Interning stringów](#interning-stringów)
12. [Mutowalność i efekty uboczne](#mutowalność-i-efekty-uboczne)
13. [Model pamięci a kopiowanie](#model-pamięci-a-kopiowanie)
14. [Model pamięci a wydajność](#model-pamięci-a-wydajność)
15. [Typowe błędy początkujących](#typowe-błędy-początkujących)
16. [Praktyczne przykłady](#praktyczne-przykłady)
17. [Dobre praktyki](#dobre-praktyki)
18. [Podsumowanie](#podsumowanie)
19. [Mini ściąga](#mini-ściąga)
20. [Ćwiczenia](#ćwiczenia)
21. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Większość ludzi, mówiąc „Python”, ma na myśli **CPython**, czyli najpopularniejszą implementację Pythona.

To ważne, bo część zachowań praktycznych:

- pamięć,
- GIL,
- garbage collector,
- reference counting,
- interning stringów

wiąże się właśnie z implementacją CPythona.

To temat bardziej techniczny, ale bardzo pomaga zrozumieć:

- efekty uboczne,
- kopiowanie,
- wydajność,
- zachowanie obiektów.

---

## Czym jest CPython

CPython to referencyjna, najpopularniejsza implementacja języka Python napisana głównie w C.

Są też inne implementacje:

- PyPy,
- Jython,
- IronPython,

ale w praktyce najczęściej spotkasz właśnie CPython.

---

## Dlaczego warto znać model pamięci

Bo wiele zachowań Pythona lepiej wtedy rozumiesz:

- dlaczego `a = b` nie kopiuje,
- dlaczego lista może zmienić się „gdzie indziej”,
- skąd bierze się GIL,
- jak działa usuwanie obiektów,
- czemu niektóre stringi wydają się współdzielone.

---

## Obiekty i referencje

W Pythonie zmienne nie przechowują danych „w środku” jak pudełko.

Bardziej poprawnie:

zmienna przechowuje **referencję** do obiektu.

Przykład:

```python
a = [1, 2, 3]
b = a
```

`a` i `b` wskazują na ten sam obiekt listy.

---

## Referencje a zmienne

To bardzo ważne.

### Typ niemutowalny

```python
a = 10
b = a
b = 20
```

Nie zmieniasz `10`, tylko przypisujesz `b` do nowego obiektu.

### Typ mutowalny

```python
a = [1, 2]
b = a
b.append(3)
```

Tu zmieniasz ten sam obiekt.

---

## GIL

GIL to:

**Global Interpreter Lock**

To mechanizm w CPythonie, który sprawia, że w danym momencie tylko jeden wątek Pythona wykonuje kod bajtowy Pythona.

To bardzo znany temat.

---

## Co GIL robi naprawdę

Najprościej:

GIL upraszcza zarządzanie pamięcią i bezpieczeństwo działania interpretera, ale ogranicza równoległe wykonywanie kodu CPU-bound w wielu wątkach.

To nie znaczy, że wątki są bezużyteczne.

Wątki nadal mają sens np. przy:

- I/O,
- sieci,
- oczekiwaniu na dysk,
- oczekiwaniu na odpowiedź.

Ale przy czysto obliczeniowych zadaniach GIL bywa ograniczeniem.

---

## Garbage collector

Garbage collector to mechanizm usuwania obiektów, które nie są już potrzebne.

W CPythonie działa to głównie przez:

- reference counting,
- oraz dodatkowy garbage collector do cykli referencji.

---

## Reference counting

CPython liczy, ile referencji wskazuje na dany obiekt.

Jeśli liczba referencji spadnie do zera, obiekt może zostać usunięty.

To bardzo ważna część modelu pamięci CPythona.

---

## Cykle referencji

Problem pojawia się wtedy, gdy obiekty wskazują na siebie nawzajem.

Przykład idei:

- obiekt A wskazuje na B,
- obiekt B wskazuje na A.

Mimo że nic „z zewnątrz” ich już nie używa, reference counting sam może nie wystarczyć.

Właśnie dlatego CPython ma dodatkowy garbage collector do wykrywania takich cykli.

---

## Interning stringów

Python czasem współdzieli niektóre stringi, szczególnie krótkie i często używane.

To nazywa się interning.

Ma to sens wydajnościowy:

- mniejsze zużycie pamięci,
- szybsze porównania w pewnych przypadkach.

Ale nie warto opierać logiki programu na szczegółach interningu.

Dlatego do porównywania wartości używaj:

```python
==
```

a nie:

```python
is
```

z wyjątkiem np. `None`.

---

## Mutowalność i efekty uboczne

To bardzo silnie wiąże się z modelem pamięci.

Jeśli wiele nazw wskazuje na ten sam mutowalny obiekt, zmiana w jednym miejscu może być widoczna gdzie indziej.

Przykład:

```python
a = [1, 2]
b = a
b.append(3)
print(a)
```

To klasyczny efekt uboczny wynikający z modelu referencji.

---

## Model pamięci a kopiowanie

Skoro zmienne przechowują referencje, to:

```python
b = a
```

nie kopiuje obiektu.

Dlatego trzeba świadomie używać:

- płytkiej kopii,
- głębokiej kopii.

---

## Model pamięci a wydajność

Ten temat ma znaczenie dla:

- tworzenia ogromnej liczby obiektów,
- mutowalnych struktur,
- współbieżności,
- pracy na dużych danych.

Nie trzeba obsesyjnie optymalizować od pierwszego dnia, ale dobrze wiedzieć, co dzieje się pod spodem.

---

## Typowe błędy początkujących

- mylenie zmiennej z samym obiektem,
- używanie `is` zamiast `==`,
- brak zrozumienia efektów ubocznych mutowalnych obiektów,
- oczekiwanie pełnej równoległości CPU-bound w wielu wątkach,
- brak świadomości, że CPython ma swoją konkretną implementację.

---

## Praktyczne przykłady

### Referencje

```python
a = [1, 2]
b = a
b.append(3)
print(a)
```

### Niemutowalność

```python
a = 10
b = a
b = 20
print(a)
```

### `is` i `==`

```python
a = [1, 2]
b = [1, 2]

print(a == b)
print(a is b)
```

### `None`

```python
x = None
if x is None:
    print("Brak wartosci")
```

---

## Dobre praktyki

- pamiętaj, że zmienne wskazują na obiekty,
- używaj `==` do porównań wartości,
- używaj `is None` dla `None`,
- uważaj na mutowalne obiekty współdzielone między nazwami,
- nie wyciągaj zbyt daleko idących wniosków z detali implementacyjnych, jeśli nie są potrzebne.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- CPython to najpopularniejsza implementacja Pythona,
- zmienne przechowują referencje do obiektów,
- GIL ogranicza równoległe wykonywanie kodu CPU-bound w wątkach,
- garbage collector i reference counting odpowiadają za zarządzanie pamięcią,
- interning stringów istnieje, ale nie powinno się na nim opierać logiki,
- mutowalność i współdzielenie referencji prowadzą do efektów ubocznych.

---

## Mini ściąga

### Ważne pojęcia

- CPython
- GIL
- reference counting
- garbage collector
- interning
- mutowalność

### Ważne reguły

- `a = b` to nie kopia
- `==` porównuje wartości
- `is` sprawdza tożsamość
- `is None` jest poprawnym stylem

---

## Ćwiczenia

### Ćwiczenie 1

Pokaż na przykładzie, że `a = b` nie kopiuje listy.

### Ćwiczenie 2

Porównaj `==` i `is` na dwóch listach o tej samej zawartości.

### Ćwiczenie 3

Pokaż różnicę między zachowaniem typu mutowalnego i niemutowalnego po przypisaniu.

---

## Przykładowe rozwiązania

```python
a = [1, 2]
b = a
b.append(3)
print(a)
```

```python
a = [1, 2]
b = [1, 2]
print(a == b)
print(a is b)
```
