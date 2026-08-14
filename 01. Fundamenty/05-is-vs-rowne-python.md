# `is` vs `==` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Co robi `==`](#co-robi-)
3. [Co robi `is`](#co-robi-is)
4. [Równość a tożsamość](#równość-a-tożsamość)
5. [Przykłady na listach](#przykłady-na-listach)
6. [Przykłady na liczbach i stringach](#przykłady-na-liczbach-i-stringach)
7. [`None` i `is None`](#none-i-is-none)
8. [Własne obiekty i `__eq__`](#własne-obiekty-i-__eq__)
9. [Dlaczego czasem `is` wydaje się działać przypadkiem](#dlaczego-czasem-is-wydaje-się-działać-przypadkiem)
10. [Kiedy używać `==`](#kiedy-używać-)
11. [Kiedy używać `is`](#kiedy-używać-is)
12. [Typowe pułapki początkujących](#typowe-pułapki-początkujących)
13. [Praktyczne przykłady](#praktyczne-przykłady)
14. [Dobre praktyki](#dobre-praktyki)
15. [Podsumowanie](#podsumowanie)
16. [Mini ściąga](#mini-ściąga)
17. [Ćwiczenia](#ćwiczenia)
18. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`is` i `==` wyglądają podobnie, ale odpowiadają na dwa różne pytania.

- `==` pyta: "czy wartości są równe?"
- `is` pyta: "czy to dokładnie ten sam obiekt?"

To rozróżnienie jest bardzo ważne. Błędne użycie `is` potrafi dawać kod, który czasem działa, a czasem zachowuje się dziwnie.

---

## Co robi `==`

`==` sprawdza równość wartości.

```python
print([1, 2] == [1, 2])
print("abc" == "abc")
print(10 == 10)
```

To nie interesuje się tym, czy obiekty są w tym samym miejscu w pamięci. Liczy się znaczenie wartości.

---

## Co robi `is`

`is` sprawdza tożsamość obiektu.

```python
a = [1, 2]
b = a

print(a is b)
```

To pyta:

"czy `a` i `b` wskazują na dokładnie ten sam obiekt?"

---

## Równość a tożsamość

Dwa obiekty mogą być:

- równe wartościowo,
- ale różne jako obiekty.

Przykład:

```python
a = [1, 2]
b = [1, 2]

print(a == b)
print(a is b)
```

Wynik:

- `a == b` to `True`
- `a is b` to `False`

Output:

```python
True
False
```

---

## Przykłady na listach

To najlepszy typ do nauki tej różnicy:

```python
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

print(lista1 == lista2)
print(lista1 is lista2)
print(lista1 == lista3)
print(lista1 is lista3)
```

Output:

```python
True
False
True
True
```

`lista3 = lista1` nie tworzy kopii. To druga nazwa dla tego samego obiektu.

Jeśli zmienisz `lista3`, zmieni się też `lista1`.

---

## Przykłady na liczbach i stringach

Na prostych typach możesz czasem zobaczyć zaskakujące wyniki:

```python
a = 256
b = 256
print(a is b)
```

albo:

```python
x = "python"
y = "python"
print(x is y)
```

W niektórych środowiskach output może być:

```python
True
```

albo podobny wynik, ale nie wolno na tym polegać w logice programu.

Czasem zobaczysz `True`, ale nie wolno budować na tym logiki programu.

Dlaczego? Bo to może wynikać z wewnętrznych optymalizacji interpretera, a nie z gwarancji semantycznej, na której chcesz polegać.

---

## `None` i `is None`

Najważniejszy codzienny przypadek użycia `is`:

```python
if wynik is None:
    print("brak wartosci")
```

Jeśli `wynik = None`, output będzie:

```python
brak wartosci
```

To standardowa, zalecana forma.

Nie pisz zwykle:

```python
if wynik == None:
```

---

## Własne obiekty i `__eq__`

To bardziej zaawansowany, ale bardzo ważny niuans.

Obiekt może definiować własne zachowanie `==`.

Przykład:

```python
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

Wtedy dwa różne obiekty mogą być:

- `==` jako `True`,
- `is` jako `False`.

To jeszcze mocniej pokazuje, że `==` i `is` pytają o coś zupełnie innego.

---

## Dlaczego czasem `is` wydaje się działać przypadkiem

Początkujący często testują:

```python
print(1000 is 1000)
```

Taki przykład może w różnych kontekstach dawać wynik wyglądający na stabilny, ale nie należy traktować go jako podstawy do używania `is` dla liczb.

i na tej podstawie wyrabiają sobie zły nawyk.

Problem w tym, że wynik może zależeć od szczegółów implementacji, środowiska albo kontekstu utworzenia obiektów.

Najważniejsza zasada:

- do porównywania wartości używaj `==`,
- do sprawdzania `None` albo tożsamości obiektu używaj `is`.

---

## Kiedy używać `==`

Najczęściej:

- liczby,
- stringi,
- listy,
- słowniki,
- tuple,
- wyniki funkcji,
- obiekty, których zawartość chcesz porównać.

To jest domyślne narzędzie do codziennych porównań.

---

## Kiedy używać `is`

Najczęściej:

- przy porównaniu z `None`,
- gdy naprawdę chcesz sprawdzić, czy dwie nazwy wskazują na ten sam obiekt,
- czasem przy pojedynczych singletonach takich jak `None`.

W zwykłym kodzie aplikacyjnym `is` pojawia się dużo rzadziej niż `==`.

---

## Typowe pułapki początkujących

- używanie `is` do porównywania stringów,
- używanie `is` do porównywania liczb,
- używanie `== None` zamiast `is None`,
- brak zrozumienia, że przypisanie nie tworzy kopii obiektu,
- mylenie równości z tożsamością.

---

## Praktyczne przykłady

### Dwie równe listy

```python
a = [1, 2]
b = [1, 2]

print(a == b)
print(a is b)
```

Output:

```python
True
False
```

### Ta sama lista pod dwiema nazwami

```python
a = [1, 2]
b = a

print(a == b)
print(a is b)
```

Output:

```python
True
True
```

### Poprawne sprawdzenie `None`

```python
wynik = None

if wynik is None:
    print("brak wyniku")
```

Output:

```python
brak wyniku
```

---

## Dobre praktyki

- używaj `==` do porównywania wartości,
- używaj `is None` do sprawdzania braku wartości,
- nie używaj `is` do zwykłych porównań liczb i stringów,
- pamiętaj, że przypisanie obiektu mutowalnego nie tworzy kopii.

---

## Podsumowanie

Najkrócej:

- `==` porównuje wartość,
- `is` porównuje tożsamość.

Jeśli chcesz sprawdzić, czy coś jest `None`, użyj `is None`.
Jeśli chcesz sprawdzić, czy dwie wartości są sobie równe, użyj `==`.

---

## Mini ściąga

```python
a = [1, 2]
b = [1, 2]
c = a

print(a == b)
print(a is b)
print(a is c)

wynik = None
print(wynik is None)
```

Najważniejsze:

- `==` to równość wartości,
- `is` to tożsamość obiektu,
- `is None` to standard.

---

## Ćwiczenia

1. Utwórz dwie listy o tej samej zawartości i sprawdź `==` oraz `is`.
2. Utwórz trzecią zmienną wskazującą na pierwszą listę i sprawdź `is`.
3. Pokaż przykład poprawnego użycia `is None`.
4. Własnymi słowami opisz różnicę między równością a tożsamością.
5. Napisz prostą klasę i pokaż różnicę między `==` i `is`.

---

## Przykładowe rozwiązania

### 1. Dwie listy

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
```

### 2. Trzecia nazwa

```python
c = a
print(a is c)
```

### 3. `None`

```python
wynik = None

if wynik is None:
    print("brak wyniku")
```

### 4. Opis

`==` sprawdza, czy wartości są takie same, a `is`, czy to dokładnie ten sam obiekt.

### 5. Klasa

```python
class A:
    def __init__(self, x):
        self.x = x
```
