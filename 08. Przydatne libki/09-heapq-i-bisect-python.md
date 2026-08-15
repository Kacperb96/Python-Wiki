# `heapq` i `bisect` w Pythonie

## Wprowadzenie

To są dwa bardzo praktyczne moduły standardowej biblioteki, o których mówi się rzadziej niż o `collections` czy `itertools`, a szkoda.

### `heapq`

Pomaga pracować z kopcem, czyli strukturą danych przydatną wtedy, gdy często chcesz:

- szybko pobierać najmniejszy element,
- utrzymywać kolejkę priorytetową,
- wybierać top-N elementów.

### `bisect`

Pomaga pracować z posortowaną listą:

- szybko znaleźć miejsce wstawienia,
- wstawić element bez ręcznego szukania,
- robić proste wyszukiwanie binarne na danych uporządkowanych.

## Część 1 — `heapq`

## Najprostszy heap

```python
import heapq

numbers = [5, 1, 9, 3]
heapq.heapify(numbers)

print(numbers)
```

Output:

```python
[1, 3, 9, 5]
```

To ważne:

Po `heapify()` lista nie staje się "normalnie posortowaną listą".

Ona staje się kopcem, czyli strukturą, w której:

- najmniejszy element jest na początku,
- reszta spełnia własność kopca,
- ale całość nie musi wyglądać jak pełne sortowanie.

## Pobieranie najmniejszego elementu

```python
import heapq

numbers = [5, 1, 9, 3]
heapq.heapify(numbers)

print(heapq.heappop(numbers))
print(numbers)
```

Output:

```python
1
[3, 5, 9]
```

## Dodawanie nowego elementu

```python
import heapq

numbers = [1, 3, 9, 5]
heapq.heapify(numbers)
heapq.heappush(numbers, 2)

print(numbers)
print(heapq.heappop(numbers))
```

Output:

```python
[1, 2, 9, 5, 3]
1
```

## Kolejka priorytetowa

To jeden z najpraktyczniejszych use case'ów.

```python
import heapq

tasks = []

heapq.heappush(tasks, (2, "odpisz na mail"))
heapq.heappush(tasks, (1, "napraw blad produkcyjny"))
heapq.heappush(tasks, (3, "zrob raport"))

print(heapq.heappop(tasks))
print(heapq.heappop(tasks))
print(heapq.heappop(tasks))
```

Output:

```python
(1, 'napraw blad produkcyjny')
(2, 'odpisz na mail')
(3, 'zrob raport')
```

Mniejsza liczba oznacza wyższy priorytet.

## `nsmallest()` i `nlargest()`

To bardzo wygodne, gdy nie chcesz budować całego kopca ręcznie.

```python
import heapq

numbers = [10, 4, 8, 1, 7, 3]

print(heapq.nsmallest(3, numbers))
print(heapq.nlargest(2, numbers))
```

Output:

```python
[1, 3, 4]
[10, 8]
```

To bardzo przydatne przy:

- rankingach,
- top wynikach,
- najtańszych ofertach,
- najwolniejszych requestach.

## Kiedy `heapq` ma sens

Najbardziej wtedy, gdy:

- wielokrotnie pobierasz najmniejszy element,
- chcesz utrzymywać stale mały ranking,
- budujesz kolejkę priorytetową,
- nie potrzebujesz za każdym razem pełnego sortowania całej listy.

## Kiedy zwykłe `sorted()` jest lepsze

Jeśli chcesz po prostu:

- raz posortować dane,
- przejść po całości,
- nie modyfikować dynamicznie struktury,

to `sorted()` często będzie prostsze.

## Część 2 — `bisect`

`bisect` działa na posortowanych listach.

## Szukanie miejsca wstawienia

```python
import bisect

numbers = [1, 3, 5, 7]

index = bisect.bisect_left(numbers, 4)
print(index)
```

Output:

```python
2
```

To znaczy:

- `4` powinno wylądować na pozycji `2`,
- czyli między `3` a `5`.

## `bisect_left()` vs `bisect_right()`

Przykład:

```python
import bisect

numbers = [1, 2, 2, 2, 5]

print(bisect.bisect_left(numbers, 2))
print(bisect.bisect_right(numbers, 2))
```

Output:

```python
1
4
```

To bardzo ważne:

- `bisect_left()` daje miejsce przed lewą granicą wartości,
- `bisect_right()` daje miejsce za prawą granicą wartości.

## Wstawianie z zachowaniem sortowania

```python
import bisect

numbers = [1, 3, 5, 7]
bisect.insort(numbers, 4)

print(numbers)
```

Output:

```python
[1, 3, 4, 5, 7]
```

To bardzo wygodne, gdy:

- chcesz utrzymywać listę stale posortowaną,
- regularnie dodajesz elementy,
- nie chcesz sortować całej listy od nowa po każdej operacji.

## Praktyczny przykład progu

```python
import bisect

thresholds = [10, 20, 50, 100]
value = 37

position = bisect.bisect_left(thresholds, value)
print(position)
```

Output:

```python
2
```

To może znaczyć np.:

- `37` wpada między próg `20` a `50`,
- czyli pasuje do określonego przedziału.

## Kiedy `bisect` ma sens

Najbardziej wtedy, gdy:

- dane są już posortowane,
- chcesz szybko znaleźć miejsce dla nowej wartości,
- utrzymujesz rosnącą listę wyników, progów, dat albo rankingów.

## Typowe błędy początkujących

### 1. Używanie `bisect` na nieposortowanej liście

To psuje sens całego narzędzia.

### 2. Mylenie kopca z pełnym sortowaniem

`heapq` nie daje po prostu "ładnie posortowanej listy".

### 3. Używanie `heapq` tam, gdzie wystarczy `sorted()`

Jeśli zadanie jest jednorazowe i proste, `sorted()` zwykle wygra czytelnością.

### 4. Brak zrozumienia `left` vs `right`

To bardzo częsta pułapka przy duplikatach.

## Mini case study

Masz ranking wyników graczy.

### Zadanie 1

Chcesz utrzymywać top 3 wyników:

```python
import heapq

scores = [120, 80, 200, 150, 90]
print(heapq.nlargest(3, scores))
```

Output:

```python
[200, 150, 120]
```

### Zadanie 2

Masz listę progów punktowych i chcesz szybko sprawdzić, gdzie wpada nowy wynik:

```python
import bisect

thresholds = [100, 200, 300, 400]
score = 250

print(bisect.bisect_left(thresholds, score))
```

Output:

```python
2
```

## Dobre praktyki

- używaj `heapq` do kolejek priorytetowych i top-N,
- używaj `bisect` tylko na posortowanych listach,
- nie komplikuj kodu tymi narzędziami, jeśli zwykły `sorted()` i indeksowanie wystarczają,
- pamiętaj, że te moduły są bardzo praktyczne, ale dość wyspecjalizowane.

## Szybka ściąga

Najczęściej przydatne:

- `heapq.heapify()`
- `heapq.heappush()`
- `heapq.heappop()`
- `heapq.nsmallest()`
- `heapq.nlargest()`
- `bisect_left()`
- `bisect_right()`
- `insort()`

## Zadania

1. Zbuduj prostą kolejkę priorytetową przez `heapq`.
2. Pobierz 3 najmniejsze liczby z listy.
3. Pobierz 2 największe liczby z listy.
4. Użyj `bisect_left()` dla listy z duplikatami.
5. Użyj `insort()` do wstawienia elementu do posortowanej listy.
6. Opisz, kiedy lepszy będzie `heapq`, a kiedy zwykłe `sorted()`.
