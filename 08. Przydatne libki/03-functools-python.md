# `functools` w Pythonie

## Wprowadzenie

`functools` zawiera narzędzia wspierające pracę z funkcjami, dekoratorami i cache.

Nie wszystko z tego modułu jest używane codziennie, ale kilka elementów jest bardzo praktycznych:

- `partial`,
- `wraps`,
- `lru_cache`,
- `cached_property`.

## Kiedy `functools` ma sens

Używaj go, gdy:

- chcesz dodać cache do czystej funkcji,
- piszesz dekorator i chcesz zachować metadane funkcji,
- tworzysz wygodniejszą funkcję z częścią argumentów ustawioną z góry,
- pracujesz w stylu funkcyjnym albo z callbackami.

## Kiedy prostszy kod wygrywa

Jeśli `partial()` albo `reduce()` robią kod mniej czytelnym niż zwykła funkcja lub pętla, to wybierz prostszy wariant.

## `partial`

Pozwala stworzyć nową funkcję z częścią argumentów już ustawioną.

```python
from functools import partial

def potega(x, y):
    return x ** y

kwadrat = partial(potega, y=2)
print(kwadrat(5))
```

Output:

```python
25
```

### Kiedy `partial()` ma sens

- gdy konfigurujesz callback,
- gdy chcesz stworzyć czytelniejszą, wyspecjalizowaną funkcję,
- gdy unikasz powtarzania tych samych argumentów.

### Kiedy lepsza jest zwykła funkcja

```python
def kwadrat(x):
    return x ** 2
```

To bywa prostsze i czytelniejsze niż `partial()` w małych przypadkach.

## `reduce`

Redukuje sekwencję do jednej wartości.

```python
from functools import reduce

result = reduce(lambda a, b: a + b, [1, 2, 3, 4])
print(result)
```

Output:

```python
10
```

### Ale uwaga

W praktyce często czytelniejsze będzie:

```python
print(sum([1, 2, 3, 4]))
```

`reduce()` warto znać, ale nie trzeba go nadużywać.

## `wraps`

Jeśli piszesz dekorator, używaj `wraps`.

```python
from functools import wraps

def loguj(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Wywolanie {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

To zachowuje metadane funkcji, np. nazwę i docstring.

## `lru_cache`

Bardzo praktyczny cache wyników funkcji.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(10))
```

Output:

```python
55
```

### Kiedy `lru_cache` ma sens

- gdy funkcja jest czysta,
- gdy te same argumenty pojawiają się wielokrotnie,
- gdy obliczenia są kosztowne.

### Kiedy nie używać

- gdy funkcja ma efekty uboczne,
- gdy wynik zależy od zmieniającego się stanu zewnętrznego,
- gdy cache może niepotrzebnie zużywać pamięć.

## `cached_property`

Oblicza wartość raz na instancję i potem ją zapamiętuje.

```python
from functools import cached_property

class Report:
    @cached_property
    def result(self):
        print("Licze wynik")
        return 42

r = Report()
print(r.result)
print(r.result)
```

Output:

```python
Licze wynik
42
42
```

Widzisz, komunikat pojawia się tylko raz.

## `functools` vs prostszy Python

### Gdy biblioteka wygrywa

- cache dla kosztownej funkcji,
- dekorator z `wraps`,
- `cached_property` dla drogiego obliczenia w obiekcie.

### Gdy prostszy kod wygrywa

- `sum()` zamiast `reduce()` dla zwykłego sumowania,
- normalna funkcja zamiast przesadnie wymyślnego `partial()`,
- brak dekoratora, jeśli zwykła funkcja wystarczy.

## Typowe błędy początkujących

- brak `wraps` w dekoratorze,
- używanie `reduce()` tam, gdzie prostsza funkcja wbudowana jest czytelniejsza,
- dodawanie cache do funkcji z efektami ubocznymi,
- brak świadomości kosztu pamięci przy cache,
- traktowanie `functools` jak obowiązkowego stylu zamiast zestawu narzędzi.

## Mini scenariusz praktyczny

Masz funkcję, która parsuje i liczy coś kosztownego dla tych samych danych wejściowych. `lru_cache` może dać ogromny zysk.

Masz dekorator logujący. `wraps` powinno być standardem.

Masz prostą funkcję kwadrat. Zwykła definicja może być lepsza niż `partial()`.

## Dobre praktyki

- `wraps` traktuj jako standard w dekoratorach,
- cache stosuj świadomie,
- nie używaj `reduce()` tylko po to, żeby wyglądać bardziej funkcyjnie,
- wybieraj rozwiązanie czytelniejsze dla człowieka,
- pamiętaj, że moduł ma upraszczać pracę, nie ją zaciemniać.

## Szybka ściąga

Najczęściej przydatne:

- `partial()` — wiąże część argumentów,
- `wraps` — zachowuje metadane dekorowanej funkcji,
- `lru_cache` — cache'uje wyniki,
- `cached_property` — liczy raz na instancję,
- `reduce()` — redukuje sekwencję do jednej wartości.

## Ćwiczenia

1. Zrób `kwadrat` przez `partial()` i zwykłą funkcję, a potem porównaj.
2. Napisz dekorator z `wraps`.
3. Dodaj `lru_cache` do Fibonacciego.
4. Napisz klasę z `cached_property`.
5. Pokaż przykład, gdzie `sum()` jest lepsze niż `reduce()`.

## Najważniejsze do zapamiętania

- `functools` daje bardzo praktyczne narzędzia do funkcji i dekoratorów.
- `wraps` i `lru_cache` to jedne z najważniejszych elementów modułu.
- `partial()` bywa wygodne, ale nie zawsze jest czytelniejsze niż zwykła funkcja.
- `reduce()` warto znać, ale często prostszy Python jest lepszy.
- Używaj `functools` wtedy, gdy realnie upraszcza kod.
