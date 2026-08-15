# Referencje i garbage collection w Pythonie

## O co chodzi

Żeby dobrze rozumieć pamięć w Pythonie, trzeba rozumieć dwa pojęcia:

- referencje,
- garbage collection.

Python zarządza pamięcią automatycznie, ale to nie znaczy, że programista może całkowicie przestać o niej myśleć.

W praktyce warto rozumieć:

- kiedy obiekt nadal żyje,
- kiedy może zostać usunięty,
- skąd biorą się pewne problemy z pamięcią,
- czemu czasem obiekty trzymają się dłużej niż byśmy chcieli.

## Czym jest referencja

Referencja to po prostu odwołanie do obiektu.

Jeśli nazwa zmiennej wskazuje na obiekt, to jest to jedna z referencji do tego obiektu.

```python
a = [1, 2, 3]
b = a
```

Tutaj lista ma co najmniej dwie referencje:

- przez `a`,
- przez `b`.

## Dlaczego to ważne

Dopóki do obiektu istnieją referencje, obiekt nadal może być potrzebny programowi.

Jeśli referencje znikną, interpreter może odzyskać pamięć.

## Prosty przykład intuicyjny

```python
a = [1, 2, 3]
b = a

del a
print(b)
```

Output:

```python
[1, 2, 3]
```

Usunięcie jednej nazwy nie usuwa obiektu, jeśli istnieją jeszcze inne referencje.

## Eksperyment 1: kilka referencji krok po kroku

```python
data = ["A", "B"]
ref1 = data
ref2 = data

print("start:", data)

del ref1
print("po del ref1:", ref2)

ref2.append("C")
print("po mutacji przez ref2:", data)
```

Output:

```python
start: ['A', 'B']
po del ref1: ['A', 'B']
po mutacji przez ref2: ['A', 'B', 'C']
```

To pokazuje, że liczy się obiekt i liczba aktywnych odwołań do niego, a nie pojedyncza nazwa.

## Liczenie referencji — intuicja

CPython używa m.in. mechanizmu reference counting.

W uproszczeniu:

- obiekt ma licznik referencji,
- gdy licznik spada do zera, obiekt może zostać zwolniony.

To daje bardzo praktyczny model myślenia, choć nie trzeba od razu znać wszystkich detali implementacyjnych.

## Garbage collection

Reference counting nie rozwiązuje wszystkiego.

Problemem są cykle referencji.

Na przykład:

- obiekt A wskazuje na B,
- obiekt B wskazuje na A.

Jeśli nic z zewnątrz już do nich nie prowadzi, same siebie nadal trzymają przy życiu.

Tu właśnie wchodzi garbage collector, który pomaga wykrywać takie sytuacje.

## Intuicja cyklu

Wyobraź sobie dwa obiekty, które nawzajem się pamiętają.

Program już ich nie potrzebuje, ale one nadal wskazują na siebie.

Bez dodatkowego mechanizmu nie byłoby łatwo odzyskać tej pamięci.

## Eksperyment 2: intuicja cyklu referencji

```python
a = {}
b = {}

a["other"] = b
b["other"] = a

print(a)
print(b)
```

Przykładowy output:

```python
{'other': {'other': {...}}}
{'other': {'other': {...}}}
```

To nie pokazuje wszystkiego o garbage collectorze, ale bardzo dobrze buduje intuicję, czym jest wzajemne trzymanie się obiektów.

## Czy trzeba się tym przejmować codziennie

Nie przy każdym małym skrypcie.

Ale warto rozumieć temat, gdy:

- masz długowieczne procesy,
- pracujesz z dużą ilością danych,
- widzisz dziwne zużycie pamięci,
- tworzysz złożone struktury obiektów,
- debugujesz wycieki pamięci lub nieoczekiwane utrzymywanie obiektów.

## `del` nie znaczy "usuń obiekt z pamięci natychmiast"

To bardzo ważne.

`del a` usuwa dowiązanie nazwy `a`, a nie gwarantuje natychmiastowego fizycznego usunięcia obiektu z pamięci.

To, czy obiekt zniknie, zależy od tego, czy istnieją jeszcze inne referencje.

## Mutowalność i referencje

Temat referencji bardzo łączy się z mutowalnością.

Jeśli wiele nazw wskazuje na ten sam mutowalny obiekt, to:

- zmiana przez jedną nazwę,
- będzie widoczna przez inne.

To nie tylko kwestia modelu obiektów, ale też praktycznego zarządzania stanem programu.

## Mini case study: "usunąłem zmienną, a dane nadal istnieją"

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

Dziwne zachowanie?

Nie, jeśli patrzysz przez runtime:

- `del items` usunął nazwę `items`,
- ale obiekt listy nadal ma referencję przez `backup`,
- więc nadal żyje.

## Mini case study: "czemu pamięć nie spada od razu?"

W długim procesie możesz czasem zauważyć, że po usunięciu obiektów pamięć nie zachowuje się tak intuicyjnie, jak oczekiwałeś.

Jednym z powodów może być:

- nadal istnieją referencje,
- masz cykle,
- interpreter i alokator pamięci pracują według własnych zasad,
- problem nie polega na samym `del`, tylko na tym, że obiekt nadal jest osiągalny.

To właśnie typ wiedzy, który oddziela intuicję "usunąłem nazwę" od realnego modelu pamięci.

## Typowe błędy początkujących

- mylenie usunięcia nazwy z usunięciem obiektu,
- brak świadomości wielu referencji do tego samego obiektu,
- przekonanie, że garbage collection "magicznie naprawi wszystko",
- ignorowanie problemów z pamięcią w długowiecznych procesach,
- brak rozumienia cykli referencji.

## Kiedy ta wiedza ma sens praktycznie

Szczególnie przy:

- większych strukturach danych,
- cache,
- obiektach wzajemnie powiązanych,
- serwerach i workerach żyjących długo,
- analizie zużycia pamięci.

## Szybka ściąga

- referencja to odwołanie do obiektu,
- obiekt żyje tak długo, jak długo ktoś do niego prowadzi,
- `del` usuwa nazwę, nie gwarantuje natychmiastowego usunięcia obiektu,
- garbage collector pomaga m.in. przy cyklach referencji,
- pamięć w Pythonie jest automatyczna, ale warto rozumieć jej model.

## Ćwiczenia

1. Pokaż przykład dwóch referencji do tej samej listy.
2. Usuń jedną nazwę i sprawdź, czy obiekt nadal jest dostępny przez drugą.
3. Wyjaśnij własnymi słowami, czemu `del` nie zawsze usuwa obiekt.
4. Opisz intuicyjnie, czym jest cykl referencji.
5. Wskaż sytuację projektową, w której wiedza o referencjach pomaga uniknąć błędu.

## Najważniejsze do zapamiętania

- Pamięć w Pythonie opiera się na referencjach do obiektów.
- Obiekt nie znika tylko dlatego, że zniknęła jedna nazwa.
- Reference counting i garbage collection rozwiązują różne części problemu zarządzania pamięcią.
- Cykle referencji są ważnym powodem istnienia garbage collectora.
- Rozumienie referencji bardzo pomaga w debugowaniu mutowalności i problemów z pamięcią.
