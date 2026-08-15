# Wieloprocesowość w Pythonie — `multiprocessing`

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co używać wielu procesów](#po-co-używać-wielu-procesów)
3. [Proces a wątek](#proces-a-wątek)
4. [Kiedy `multiprocessing` ma sens](#kiedy-multiprocessing-ma-sens)
5. [Dlaczego procesy omijają problem GIL](#dlaczego-procesy-omijają-problem-gil)
6. [Podstawy modułu `multiprocessing`](#podstawy-modułu-multiprocessing)
7. [`Process`](#process)
8. [`Queue` i `Pool`](#queue-i-pool)
9. [Przykład z outputem](#przykład-z-outputem)
10. [Pułapki platformowe i `if __name__ == "__main__"`](#pułapki-platformowe-i-if-__name__--__main__)
11. [Kiedy nie używać procesów](#kiedy-nie-używać-procesów)
12. [Typowe błędy początkujących](#typowe-błędy-początkujących)
13. [Praktyczna ściąga](#praktyczna-ściąga)
14. [Ćwiczenia](#ćwiczenia)
15. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

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

## `Queue` i `Pool`

### `Queue`

To prosty sposób komunikacji między procesami.

### `Pool`

Pozwala wygodnie rozdzielać wiele podobnych zadań między kilka procesów.

To bardzo praktyczne, gdy masz listę danych do przeliczenia.

---

## Przykład z outputem

```python
from multiprocessing import Process, Queue


def policz_kwadrat(x, q):
    q.put(x * x)


if __name__ == "__main__":
    q = Queue()
    p = Process(target=policz_kwadrat, args=(5, q))
    p.start()
    p.join()
    print(q.get())
```

Przykładowy output:

```text
25
```

To pokazuje prosty przepływ:

- proces wykonuje pracę,
- wynik trafia do kolejki,
- proces główny go odbiera.

---

## Pułapki platformowe i `if __name__ == "__main__"`

To bardzo ważne.

Przy `multiprocessing` często musisz chronić punkt wejścia programu:

```python
if __name__ == "__main__":
    ...
```

Bez tego na części systemów możesz dostać bardzo dziwne zachowanie albo zapętlenie tworzenia procesów.

To nie jest drobiazg, tylko ważna reguła praktyczna.

---

## Kiedy nie używać procesów

Procesy nie są zawsze najlepsze.

Nie warto ich używać, gdy:

- problem jest prosty i krótkotrwały,
- narzut tworzenia procesów przewyższa zysk,
- zadanie jest głównie I/O-bound,
- prostsze rozwiązanie async albo wątkowe wystarczy.

---

## Typowe błędy początkujących

- używanie procesów do każdego problemu współbieżności,
- brak `if __name__ == "__main__"`,
- brak zrozumienia kosztu kopiowania i serializacji danych,
- oczekiwanie współdzielonej pamięci jak w wątkach,
- zbyt małe zadania, dla których narzut procesów jest nieopłacalny.

---

## Praktyczna ściąga

### Jeden proces

```python
p = Process(target=praca)
p.start()
p.join()
```

### Wynik przez `Queue`

```python
q = Queue()
```

### Kiedy warto

- CPU-bound,
- wiele rdzeni,
- odizolowane zadania.

---

## Ćwiczenia

1. Uruchom jedną funkcję w osobnym procesie.
2. Przekaż wynik przez `Queue`.
3. Użyj `Pool` do policzenia kwadratów kilku liczb.
4. Dodaj ochronę `if __name__ == "__main__"`.
5. Wyjaśnij własnymi słowami, czemu procesy pomagają przy CPU-bound.

---

## Najważniejsze do zapamiętania

- `multiprocessing` jest szczególnie przydatne przy CPU-bound.
- Procesy omijają problem GIL przez osobne interpretery.
- Są cięższe od wątków i mają większy narzut.
- `Queue` i `Pool` to bardzo praktyczne narzędzia tego modułu.
- `if __name__ == "__main__"` jest tu bardzo ważne.
