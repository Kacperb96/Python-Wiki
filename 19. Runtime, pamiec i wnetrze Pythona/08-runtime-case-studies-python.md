# Runtime case studies w Pythonie

## Po co ten plik

Ten plik spina kilka tematów z folderu 19 w jedną praktyczną całość.

Nie chodzi tu o nowe definicje, tylko o odpowiedź na pytanie:

- jak runtime tłumaczy dziwne zachowania kodu?

To jest bardzo ważny etap nauki. Kiedy zaczynasz umieć wyjaśnić takie sytuacje bez zgadywania, to znaczy, że folder naprawdę zaczął siedzieć.

## Case study 1: "zmieniłem jedną listę, a druga też się zmieniła"

Kod:

```python
a = [1, 2]
b = a
b.append(3)

print(a)
print(b)
```

Output:

```python
[1, 2, 3]
[1, 2, 3]
```

### Intuicja początkującego

- "chyba Python skopiował listę dziwnie"

### Wyjaśnienie runtime

- `a` i `b` wskazują na ten sam obiekt,
- `append()` mutuje obiekt w miejscu,
- więc obie nazwy pokazują tę samą zmienioną listę.

### Najważniejsza lekcja

To problem modelu obiektów i aliasowania, a nie żadna magia list.

## Case study 2: "usunąłem zmienną, ale dane nadal żyją"

Kod:

```python
items = [1, 2, 3]
backup = items

del items
print(backup)
```

Output:

```python
[1, 2, 3]
```

### Intuicja początkującego

- "przecież usunąłem listę"

### Wyjaśnienie runtime

- usunąłeś nazwę `items`,
- ale nie usunąłeś obiektu,
- bo nadal istnieje referencja `backup`.

### Najważniejsza lekcja

`del` działa na dowiązaniu nazwy, nie na obiekcie w absolutnym sensie.

## Case study 3: "funkcja nie zwracała nic, a i tak zmieniła dane"

Kod:

```python
def prepare(data: list[int]) -> None:
    data.append(99)


numbers = [1, 2, 3]
prepare(numbers)
print(numbers)
```

Output:

```python
[1, 2, 3, 99]
```

### Intuicja początkującego

- "przecież funkcja nic nie zwróciła"

### Wyjaśnienie runtime

- funkcja dostała referencję do tej samej listy,
- wykonała mutację na obiekcie,
- brak `return` nie ma tu znaczenia.

### Najważniejsza lekcja

Brak wartości zwracanej nie oznacza braku skutków ubocznych.

## Case study 4: "dziwny print pojawia się przy starcie programu"

Kod modułu `config.py`:

```python
print("Laduje konfiguracje")
DEBUG = True
```

Kod `main.py`:

```python
import config
print("Start aplikacji")
```

Output:

```python
Laduje konfiguracje
Start aplikacji
```

### Intuicja początkującego

- "skąd ten print?"

### Wyjaśnienie runtime

- import wykonuje kod modułu,
- print jest na poziomie globalnym pliku,
- więc uruchamia się od razu przy imporcie.

### Najważniejsza lekcja

Import to wykonanie kodu modułu, a nie tylko deklaracja zależności.

## Case study 5: "drugi import nic nie zrobił"

Kod:

```python
import tools
import tools
print("dalej")
```

Przykładowy output, jeśli `tools` ma `print` na poziomie modułu:

```python
Pierwsze ladowanie tools
dalej
```

### Intuicja początkującego

- "czemu drugi import nie uruchomił modułu jeszcze raz?"

### Wyjaśnienie runtime

- Python cache'uje załadowane moduły,
- drugi import korzysta z już istniejącego obiektu modułu.

### Najważniejsza lekcja

Import system ma pamięć i nie jest naiwnym kopiowaniem pliku za każdym razem.

## Case study 6: "rekurencja nagle wybuchła błędem"

Kod:

```python
def loop(n: int) -> None:
    print(n)
    loop(n + 1)


loop(1)
```

Kończy się błędem w stylu:

```text
RecursionError: maximum recursion depth exceeded
```

### Intuicja początkującego

- "czemu Python sam tego nie kontynuuje?"

### Wyjaśnienie runtime

- każde wywołanie dokłada nową ramkę na stos,
- stos nie może rosnąć bez końca,
- interpreter ma limit głębokości rekurencji.

### Najważniejsza lekcja

Rekurencja nie jest darmowa. Każde wywołanie ma koszt runtime.

## Case study 7: "wątki nie przyspieszyły obliczeń"

Scenariusz:

- dwa wątki wykonują intensywne liczenie CPU-bound w czystym Pythonie,
- przyspieszenie jest mniejsze niż oczekiwano.

### Intuicja początkującego

- "mam dwa wątki, to powinno być dwa razy szybciej"

### Wyjaśnienie runtime

- w CPythonie działa GIL,
- kod Python CPU-bound w wielu wątkach nie skaluje się tak jak natywna równoległość wielu rdzeni.

### Najważniejsza lekcja

Najpierw rozpoznaj, czy problem jest CPU-bound czy I/O-bound.

## Case study 8: "ten sam Python, a inne zachowanie wydajnościowe"

Scenariusz:

- program działa poprawnie na dwóch interpreterach,
- ale wydajność się różni.

### Intuicja początkującego

- "przecież to ten sam język"

### Wyjaśnienie runtime

- język to jedno,
- implementacja interpretera to drugie,
- CPython i PyPy mogą różnić się charakterystyką wykonania.

### Najważniejsza lekcja

Nie wszystko, co przypisujesz Pythonowi, jest cechą języka jako takiego. Część rzeczy wynika z konkretnej implementacji.

## Jak pracować z takimi dziwnymi przypadkami

Gdy kod zachowuje się dziwnie, warto przejść taką checklistę:

1. Czy problem dotyczy nazw czy obiektów?
2. Czy to mutacja czy rebinding?
3. Czy nadal istnieją referencje do obiektu?
4. Czy kod wykonał się przy imporcie?
5. Czy problem dotyczy stosu wywołań?
6. Czy to ograniczenie runtime CPythona?
7. Czy mówimy o języku, czy o konkretnej implementacji?

## Szybka ściąga

Najczęstsze dziwne zachowania runtime wynikają z:

- aliasowania,
- mutowalności,
- referencji,
- skutków ubocznych importu,
- stosu wywołań,
- GIL,
- różnic między implementacjami interpretera.

## Ćwiczenia

1. Weź każdy case study i wyjaśnij go własnymi słowami bez patrzenia na odpowiedź.
2. Napisz własny przykład "dziwnego zachowania" z mutacją listy.
3. Napisz własny przykład skutku ubocznego przy imporcie.
4. Opisz przypadek, w którym GIL tłumaczy zachowanie programu.
5. Zrób jedną osobistą checklistę debugowania problemów runtime.

## Najważniejsze do zapamiętania

- Dużo dziwnych zachowań Pythona da się spokojnie wyjaśnić przez model runtime.
- Najczęściej chodzi o obiekty, referencje, mutacje, import albo stos wywołań.
- Gdy rozumiesz te mechanizmy, Python przestaje wyglądać jak magia.
- Umiejętność tłumaczenia takich przypadków to znak realnego zrozumienia języka.
