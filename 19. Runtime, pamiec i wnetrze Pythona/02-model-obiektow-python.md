# Model obiektów w Pythonie

## O co chodzi

Jedna z najważniejszych rzeczy do zrozumienia w Pythonie brzmi:

- zmienna nie "zawiera" wartości w prostym sensie,
- nazwa jest dowiązana do obiektu.

To bardzo wpływa na zrozumienie:

- mutowalności,
- aliasowania,
- przekazywania argumentów,
- porównań `is` i `==`,
- zachowania list, słowników i własnych obiektów.

## Najprostsza intuicja

Masz obiekt i masz nazwę.

Nazwa to etykieta wskazująca na obiekt.

Przykład:

```python
numbers = [1, 2, 3]
```

Tu `numbers` to nazwa, a lista `[1, 2, 3]` to obiekt.

## Dwie nazwy do tego samego obiektu

```python
a = [1, 2, 3]
b = a

print(a)
print(b)
print(a is b)
```

Output:

```python
[1, 2, 3]
[1, 2, 3]
True
```

To oznacza, że `a` i `b` wskazują na ten sam obiekt.

## Co z tego wynika

Jeśli obiekt jest mutowalny, zmiana przez jedną nazwę będzie widoczna przez drugą.

```python
a = [1, 2, 3]
b = a
b.append(4)

print(a)
print(b)
```

Output:

```python
[1, 2, 3, 4]
[1, 2, 3, 4]
```

To nie są dwie listy. To jedna lista z dwiema nazwami.

## Eksperyment 1: aliasowanie krok po kroku

```python
a = ["python"]
print("start a:", a)

b = a
print("po b = a")
print("a is b:", a is b)

b.append("runtime")
print("po b.append(...)")
print("a:", a)
print("b:", b)
```

Output:

```python
start a: ['python']
po b = a
a is b: True
po b.append(...)
a: ['python', 'runtime']
b: ['python', 'runtime']
```

To jeden z najważniejszych eksperymentów w całym Pythonie. Jak on naprawdę siedzi, to masa późniejszych tematów robi się prostsza.

## Obiekt, tożsamość i wartość

W praktyce warto odróżniać:

- wartość,
- tożsamość obiektu,
- nazwę wskazującą na obiekt.

### `==`

Porównuje zwykle wartości.

### `is`

Sprawdza, czy to dokładnie ten sam obiekt.

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

Dwie różne listy mogą mieć tę samą zawartość, ale nie być tym samym obiektem.

## Eksperyment 2: identyczna wartość, inny obiekt

```python
x = {"name": "Jan"}
y = {"name": "Jan"}

print("x == y:", x == y)
print("x is y:", x is y)
```

Output:

```python
x == y: True
x is y: False
```

To często tłumaczy dziwne błędy w kodzie, gdzie ktoś używa `is` zamiast `==`.

## Wszystko jest obiektem

To klasyczna cecha Pythona.

Obiektem są:

- liczby,
- stringi,
- listy,
- funkcje,
- klasy,
- instancje klas.

To bardzo wpływa na styl języka i jego elastyczność.

## Argumenty funkcji a obiekty

To kolejny bardzo praktyczny punkt.

Gdy przekazujesz argument do funkcji, przekazujesz referencję do obiektu.

Przykład z listą:

```python
def add_item(items):
    items.append("x")


data = []
add_item(data)
print(data)
```

Output:

```python
['x']
```

Funkcja operuje na tym samym obiekcie listy.

## Rebinding vs mutacja

To bardzo ważne rozróżnienie.

### Mutacja

Zmienia istniejący obiekt.

```python
items.append(4)
```

### Rebinding

Podstawia nazwę pod inny obiekt.

```python
items = [1, 2, 3]
```

To nie to samo.

## Eksperyment 3: mutacja vs rebinding

```python
def mutate(items: list[int]) -> None:
    items.append(99)


def rebind(items: list[int]) -> None:
    items = [0, 0, 0]
    print("wewnątrz rebind:", items)


data = [1, 2, 3]
mutate(data)
print("po mutate:", data)

rebind(data)
print("po rebind:", data)
```

Output:

```python
po mutate: [1, 2, 3, 99]
wewnątrz rebind: [0, 0, 0]
po rebind: [1, 2, 3, 99]
```

To bardzo ważny eksperyment. `mutate()` zmienia obiekt, a `rebind()` tylko podstawia lokalną nazwę `items` pod nowy obiekt.

## Dlaczego ten model jest tak ważny

Bo bez niego trudno dobrze rozumieć:

- kopiowanie,
- mutowalność,
- aliasowanie,
- działanie argumentów,
- zachowanie obiektów własnych klas.

To jest fundament głębszego rozumienia Pythona.

## Mini case study: "czemu funkcja zmieniła mi listę?"

Kod:

```python
def prepare(names: list[str]) -> None:
    names.sort()


users = ["Zenon", "Anna", "Marek"]
prepare(users)
print(users)
```

Output:

```python
['Anna', 'Marek', 'Zenon']
```

Ktoś może się zdziwić:

- "przecież nic nie zwracałem, czemu wynik się zmienił?"

Wyjaśnienie runtime:

- przekazałeś referencję do tej samej listy,
- `sort()` mutuje obiekt w miejscu,
- więc po wyjściu z funkcji nadal widzisz tę samą, ale już zmienioną listę.

## Typowe błędy początkujących

- traktowanie nazwy jak pudełka z wartością,
- brak świadomości, że dwie nazwy mogą wskazywać na ten sam obiekt,
- mylenie mutacji z przypisaniem,
- nadużywanie `is` zamiast `==`,
- zdziwienie, że funkcja zmienia listę przekazaną jako argument.

## Szybka ściąga

- nazwa wskazuje na obiekt,
- wiele nazw może wskazywać na ten sam obiekt,
- `==` porównuje wartości,
- `is` sprawdza tożsamość,
- mutacja i rebinding to nie to samo.

## Ćwiczenia

1. Napisz przykład dwóch nazw wskazujących na ten sam obiekt.
2. Pokaż różnicę między `==` i `is`.
3. Napisz funkcję mutującą listę przekazaną jako argument.
4. Pokaż przykład rebindingu bez mutacji oryginalnego obiektu.
5. Wyjaśnij własnymi słowami, czym jest aliasowanie.

## Najważniejsze do zapamiętania

- W Pythonie nazwy są dowiązaniami do obiektów.
- Jedna zmienna nie musi oznaczać jednego "własnego pudełka".
- Mutowalność i aliasowanie są bezpośrednio związane z modelem obiektów.
- `is` i `==` odpowiadają na różne pytania.
- To jest jedna z najbardziej praktycznych rzeczy do zrozumienia w całym języku.
