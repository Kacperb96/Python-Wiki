# Wieloprocesowość w Pythonie — `multiprocessing`

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co używać wielu procesów](#po-co-używać-wielu-procesów)
3. [Proces a wątek](#proces-a-wątek)
4. [Kiedy `multiprocessing` ma sens](#kiedy-multiprocessing-ma-sens)
5. [Dlaczego procesy omijają problem GIL](#dlaczego-procesy-omijają-problem-gil)
6. [Podstawy modułu `multiprocessing`](#podstawy-modułu-multiprocessing)
7. [`Process`](#process)
8. [`start()` i `join()`](#start-i-join)
9. [Przekazywanie danych do procesu](#przekazywanie-danych-do-procesu)
10. [`Queue` i `Pipe`](#queue-i-pipe)
11. [Współdzielenie stanu](#współdzielenie-stanu)
12. [`Pool`](#pool)
13. [`map()` w puli procesów](#map-w-puli-procesów)
14. [Pułapki platformowe i `if __name__ == '__main__'`](#pułapki-platformowe-i-if-__name__--__main__)
15. [Typowe błędy początkujących](#typowe-błędy-początkujących)
16. [Praktyczne przykłady](#praktyczne-przykłady)
17. [Dobre praktyki](#dobre-praktyki)
18. [Podsumowanie](#podsumowanie)
19. [Mini ściąga](#mini-ściąga)
20. [Ćwiczenia](#ćwiczenia)
21. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Wieloprocesowość polega na uruchamianiu wielu niezależnych procesów.

W Pythonie najczęściej używa się do tego modułu `multiprocessing`.

To ważne narzędzie, gdy problem dotyczy:

- ciężkich obliczeń,
- wykorzystania wielu rdzeni CPU,
- odseparowania pracy,
- izolacji awarii.

---

## Po co używać wielu procesów

Jeśli program wykonuje kosztowne obliczenia, jeden proces może nie wystarczać.

Procesy pozwalają:

- rozłożyć pracę na wiele rdzeni,
- ominąć ograniczenia GIL,
- zwiększyć przepustowość zadań CPU-bound.

---

## Proces a wątek

Proces:

- ma własną pamięć,
- jest mocniej odizolowany,
- jest cięższy w tworzeniu.

Wątek:

- współdzieli pamięć w procesie,
- jest lżejszy,
- łatwiej o problemy synchronizacyjne.

Procesy są zwykle bezpieczniejsze izolacyjnie, ale droższe.

---

## Kiedy `multiprocessing` ma sens

Najczęściej przy:

- obróbce danych,
- liczeniu statystyk,
- przetwarzaniu obrazów,
- kompresji,
- analizie CPU-bound,
- wszędzie tam, gdzie wiele rdzeni naprawdę pomoże.

---

## Dlaczego procesy omijają problem GIL

Każdy proces ma własny interpreter Pythona i własny GIL.

Dlatego kilka procesów może naprawdę wykonywać kod równolegle na wielu rdzeniach.

To główny powód, dla którego `multiprocessing` jest ważne przy CPU-bound.

---

## Podstawy modułu `multiprocessing`

Najprostszy import:

```python
import multiprocessing
```

Podobnie jak w `threading`, możesz tworzyć obiekty procesu i nimi zarządzać.

---

## `Process`

Przykład:

```python
from multiprocessing import Process

def praca():
    print("proces dziala")

if __name__ == "__main__":
    p = Process(target=praca)
    p.start()
    p.join()
```

---

## `start()` i `join()`

`start()` uruchamia proces.

`join()` czeka na jego zakończenie.

To podstawowy mechanizm kontroli życia procesu.

---

## Przekazywanie danych do procesu

Podobnie jak przy wątkach możesz przekazać argumenty:

```python
from multiprocessing import Process

def powitaj(imie):
    print(f"Czesc, {imie}")

if __name__ == "__main__":
    p = Process(target=powitaj, args=("Anna",))
    p.start()
    p.join()
```

Trzeba pamiętać, że dane są kopiowane lub serializowane, a nie współdzielone w prosty sposób jak we wątkach.

---

## `Queue` i `Pipe`

To podstawowe sposoby komunikacji między procesami.

### `Queue`

Bezpieczna kolejka do przekazywania danych.

```python
from multiprocessing import Process, Queue

def worker(q):
    q.put("wynik")

if __name__ == "__main__":
    q = Queue()
    p = Process(target=worker, args=(q,))
    p.start()
    print(q.get())
    p.join()
```

### `Pipe`

Dwukierunkowy kanał komunikacji między dwoma procesami.

---

## Współdzielenie stanu

Procesy z natury nie współdzielą pamięci tak łatwo jak wątki.

To zaleta i wada jednocześnie.

Można używać:

- `Value`,
- `Array`,
- managerów,
- kolejek,

ale zwykle warto preferować przekazywanie komunikatów zamiast skomplikowanego wspólnego stanu.

---

## `Pool`

Jeśli masz wiele podobnych zadań, bardzo wygodna jest pula procesów.

```python
from multiprocessing import Pool

def kwadrat(x):
    return x * x

if __name__ == "__main__":
    with Pool(4) as pool:
        wyniki = pool.map(kwadrat, [1, 2, 3, 4])
        print(wyniki)
```

---

## `map()` w puli procesów

`pool.map()` działa podobnie do zwykłego `map()`, ale rozdziela pracę pomiędzy procesy.

To bardzo wygodny punkt wejścia do prostego parallel computingu w Pythonie.

---

## Pułapki platformowe i `if __name__ == '__main__'`

To sekcja obowiązkowa.

Przy `multiprocessing` bardzo ważne jest:

```python
if __name__ == "__main__":
    ...
```

Bez tego na części systemów można dostać błędy lub zapętlenie tworzenia procesów.

Trzeba to traktować jako standard.

---

## Typowe błędy początkujących

- brak bloku `if __name__ == "__main__":`,
- używanie procesów do bardzo małych zadań, gdzie narzut zjada korzyść,
- przekazywanie trudnych do serializacji obiektów,
- nadmierne współdzielenie stanu,
- mylenie przypadków dla `threading` i `multiprocessing`.

---

## Praktyczne przykłady

### Dwa procesy

```python
from multiprocessing import Process
import time

def praca(nazwa):
    for i in range(3):
        print(nazwa, i)
        time.sleep(0.5)

if __name__ == "__main__":
    p1 = Process(target=praca, args=("A",))
    p2 = Process(target=praca, args=("B",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
```

### Kolejka wyników

```python
from multiprocessing import Process, Queue

def policz_kwadrat(x, q):
    q.put(x * x)

if __name__ == "__main__":
    q = Queue()
    procesy = [Process(target=policz_kwadrat, args=(i, q)) for i in range(5)]

    for p in procesy:
        p.start()

    wyniki = [q.get() for _ in procesy]

    for p in procesy:
        p.join()

    print(wyniki)
```

---

## Dobre praktyki

- używaj procesów do CPU-bound,
- pilnuj narzutu uruchamiania i komunikacji,
- preferuj `Pool` przy wielu podobnych zadaniach,
- przekazuj dane prostymi strukturami,
- ograniczaj wspólny stan na rzecz komunikatów.

---

## Podsumowanie

`multiprocessing` jest podstawowym narzędziem do prawdziwej równoległości w Pythonie.

Największy sens ma przy zadaniach obliczeniowych, gdzie:

- wątki nie pomagają przez GIL,
- async nie rozwiązuje problemu,
- wiele rdzeni może realnie skrócić czas wykonania.

---

## Mini ściąga

```python
from multiprocessing import Process

def praca():
    print("dzialam")

if __name__ == "__main__":
    p = Process(target=praca)
    p.start()
    p.join()
```

Pamiętaj:

- procesy są dobre do CPU-bound,
- `Queue` służy do komunikacji,
- `Pool` upraszcza wiele podobnych zadań,
- każdy proces ma własną pamięć,
- `if __name__ == "__main__":` jest bardzo ważne.

---

## Ćwiczenia

1. Uruchom jedną funkcję w osobnym procesie.
2. Uruchom dwa procesy z różnymi argumentami.
3. Przekaż wynik z procesu do procesu głównego przez `Queue`.
4. Użyj `Pool`, aby policzyć kwadraty listy liczb.
5. Porównaj mentalnie, czy dane zadanie lepiej pasuje do `threading` czy `multiprocessing`.

---

## Przykładowe rozwiązania

### 1. Jeden proces

```python
from multiprocessing import Process

def hello():
    print("hello z procesu")

if __name__ == "__main__":
    p = Process(target=hello)
    p.start()
    p.join()
```

### 2. Dwa procesy

```python
from multiprocessing import Process

def wypisz(x):
    print(x)

if __name__ == "__main__":
    p1 = Process(target=wypisz, args=("A",))
    p2 = Process(target=wypisz, args=("B",))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
```

### 3. `Queue`

```python
from multiprocessing import Process, Queue

def licz(x, q):
    q.put(x * 2)

if __name__ == "__main__":
    q = Queue()
    p = Process(target=licz, args=(5, q))
    p.start()
    print(q.get())
    p.join()
```

### 4. `Pool`

```python
from multiprocessing import Pool

def kwadrat(x):
    return x * x

if __name__ == "__main__":
    with Pool(4) as pool:
        print(pool.map(kwadrat, [1, 2, 3, 4, 5]))
```

### 5. Dobór narzędzia

Jeśli zadanie:

- dużo czeka na sieć lub pliki, zwykle pasują wątki albo async,
- intensywnie liczy, zwykle lepiej pasują procesy.
