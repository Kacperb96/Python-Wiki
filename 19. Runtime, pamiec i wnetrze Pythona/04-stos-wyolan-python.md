# Stos wywołań w Pythonie

## O co chodzi

Stos wywołań to model pokazujący, jak interpreter śledzi aktywne wywołania funkcji.

Za każdym razem, gdy wywołujesz funkcję:

- interpreter wchodzi do nowej ramki wykonania,
- pamięta lokalne zmienne,
- pamięta, skąd wrócić,
- wykonuje kod funkcji,
- a po zakończeniu schodzi z tej ramki.

To właśnie intuicyjnie tworzy stos wywołań.

## Najprostsza intuicja

Wyobraź sobie talerze układane jeden na drugim.

- nowa funkcja = nowy talerz na wierzchu,
- powrót z funkcji = zdjęcie talerza z wierzchu.

To daje intuicję LIFO:

- last in, first out.

## Prosty przykład

```python
def c():
    print("w c")


def b():
    print("w b")
    c()


def a():
    print("w a")
    b()


a()
```

Output:

```python
w a
w b
w c
```

Ale pod maską interpreter przechodzi przez kolejne warstwy wywołań.

## Co jest na stosie

W uproszczeniu każda aktywna funkcja ma swoją ramkę wykonania, zawierającą m.in.:

- lokalne zmienne,
- informacje o miejscu wykonania,
- kontekst powrotu.

Nie musisz znać wszystkich szczegółów implementacji, ale warto rozumieć, że każda aktywna funkcja zajmuje własne miejsce na stosie.

## Rekurencja a stos wywołań

To bardzo praktyczne połączenie.

Jeśli funkcja wywołuje samą siebie, kolejne wywołania też dokładają ramki na stos.

Przykład:

```python
def countdown(n: int) -> None:
    print(n)
    if n == 0:
        return
    countdown(n - 1)


countdown(3)
```

Output:

```python
3
2
1
0
```

Każde wywołanie tworzy nową ramkę.

## Recursion limit

Python ma limit głębokości rekurencji.

To zabezpieczenie przed nieskończonym albo zbyt głębokim schodzeniem po stosie.

Jeśli rekurencja jest zbyt głęboka, dostaniesz błąd typu:

```text
RecursionError: maximum recursion depth exceeded
```

To bardzo praktyczny komunikat, który bez zrozumienia stosu wywołań może wydawać się tajemniczy.

## Dlaczego to ma znaczenie

Zrozumienie stosu pomaga przy:

- debugowaniu tracebacków,
- rozumieniu rekurencji,
- analizie błędów,
- rozumieniu zakresu życia lokalnych zmiennych,
- myśleniu o przepływie programu.

## Traceback jako ślad stosu

Gdy pojawia się wyjątek, traceback pokazuje ścieżkę wywołań, która doprowadziła do błędu.

To w praktyce bardzo często zapis tego, co działo się na stosie wywołań.

Dlatego umiejętność czytania tracebacka jest bezpośrednio związana ze zrozumieniem stosu.

## Lokalny stan funkcji

Każde wywołanie funkcji ma swój własny lokalny kontekst.

To właśnie dlatego ta sama funkcja może zostać wywołana wiele razy i za każdym razem mieć własne lokalne wartości.

To szczególnie ważne przy rekurencji.

## Kiedy ta wiedza ma sens praktycznie

Szczególnie gdy:

- debugujesz wyjątki,
- czytasz tracebacki,
- używasz rekurencji,
- rozumiesz przepływ wykonania przez wiele warstw funkcji,
- analizujesz, skąd wzięła się konkretna wartość lub błąd.

## Typowe błędy początkujących

- brak rozumienia, że każda funkcja ma własną ramkę wykonania,
- traktowanie tracebacka jak losowej ściany tekstu,
- używanie rekurencji bez świadomości limitu,
- brak intuicji, czemu lokalne zmienne "znikają" po zakończeniu funkcji.

## Szybka ściąga

- stos wywołań śledzi aktywne wywołania funkcji,
- każda aktywna funkcja ma własną ramkę,
- rekurencja dokłada kolejne ramki,
- traceback pokazuje ślad prowadzący do błędu,
- zrozumienie stosu pomaga debugować kod.

## Ćwiczenia

1. Napisz trzy funkcje wywołujące się po kolei i opisz intuicyjnie stos.
2. Zrób prostą rekurencję i opisz, co dzieje się na kolejnych poziomach.
3. Wyjaśnij, skąd bierze się `RecursionError`.
4. Weź prosty traceback i opisz go własnymi słowami.
5. Wskaż, czemu każda funkcja ma własne lokalne zmienne.

## Najważniejsze do zapamiętania

- Stos wywołań to model aktywnych funkcji w programie.
- Każde wywołanie funkcji tworzy własną ramkę.
- Rekurencja bezpośrednio korzysta ze stosu i może go przepełnić.
- Traceback jest praktycznym śladem stosu przy błędzie.
- Zrozumienie stosu bardzo pomaga w debugowaniu i czytaniu kodu.
