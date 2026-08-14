# Zmienne i typy danych w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest zmienna](#czym-jest-zmienna)
3. [Jak tworzy się zmienne w Pythonie](#jak-tworzy-się-zmienne-w-pythonie)
4. [Zasady nazywania zmiennych](#zasady-nazywania-zmiennych)
5. [Przypisanie wartości](#przypisanie-wartości)
6. [Zmienne a obiekty](#zmienne-a-obiekty)
7. [Jak sprawdzić typ danych](#jak-sprawdzić-typ-danych)
8. [Najważniejsze typy danych w Pythonie](#najważniejsze-typy-danych-w-pythonie)
9. [Typ liczbowy `int`](#typ-liczbowy-int)
10. [Typ liczbowy `float`](#typ-liczbowy-float)
11. [Typ logiczny `bool`](#typ-logiczny-bool)
12. [Typ tekstowy `str`](#typ-tekstowy-str)
13. [Brak wartości: `NoneType`](#brak-wartości-nonetype)
14. [Typy sekwencyjne i kolekcje](#typy-sekwencyjne-i-kolekcje)
15. [Lista `list`](#lista-list)
16. [Krotka `tuple`](#krotka-tuple)
17. [Zbiór `set`](#zbiór-set)
18. [Słownik `dict`](#słownik-dict)
19. [Typy mutowalne i niemutowalne](#typy-mutowalne-i-niemutowalne)
20. [Rzutowanie typów](#rzutowanie-typów)
21. [Operatory i typy danych](#operatory-i-typy-danych)
22. [Porównywanie wartości i typów](#porównywanie-wartości-i-typów)
23. [Prawda i fałsz w Pythonie](#prawda-i-fałsz-w-pythonie)
24. [Kopiowanie danych i pułapki](#kopiowanie-danych-i-pułapki)
25. [Wejście od użytkownika i typy danych](#wejście-od-użytkownika-i-typy-danych)
26. [Typowe błędy początkujących](#typowe-błędy-początkujących)
27. [Dobre praktyki](#dobre-praktyki)
28. [Podsumowanie](#podsumowanie)
29. [Mini ściąga](#mini-ściąga)
30. [Ćwiczenia](#ćwiczenia)
31. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Zmienne i typy danych to absolutna podstawa programowania w Pythonie.

Jeśli dobrze zrozumiesz:

- czym jest zmienna,
- co to jest typ danych,
- jak Python przechowuje liczby, teksty i kolekcje,
- kiedy dane można zmieniać, a kiedy nie,

to dalsza nauka będzie dużo prostsza.

Ten temat wydaje się prosty, ale naprawdę wraca później wszędzie:

- w funkcjach,
- w kolekcjach,
- w obiektach,
- w błędach typu,
- w mutowalności,
- w pracy z API i plikami.

---

## Czym jest zmienna

Najprościej:

**zmienna to nazwa, pod którą przechowujesz jakąś wartość.**

Przykład:

```python
imie = "Kasia"
wiek = 25
```

Tutaj:

- `imie` to zmienna,
- `"Kasia"` to wartość typu tekstowego,
- `wiek` to zmienna,
- `25` to wartość typu liczbowego.

O zmiennej możesz myśleć jak o etykiecie przyklejonej do danych.

---

## Jak tworzy się zmienne w Pythonie

W Pythonie nie musisz wcześniej deklarować typu zmiennej.

To znaczy, że nie piszesz:

```python
int wiek = 25
```

jak w niektórych innych językach.

W Pythonie po prostu przypisujesz wartość:

```python
wiek = 25
```

Python sam rozpoznaje typ danych.

Przykłady:

```python
liczba = 10
cena = 19.99
imie = "Ola"
czy_aktywny = True
```

Ta cecha sprawia, że Python jest wygodny, ale jednocześnie wymaga od Ciebie pilnowania sensownych nazw i rozumienia, z jakim typem aktualnie pracujesz.

---

## Zasady nazywania zmiennych

Nazwy zmiennych powinny być czytelne i zgodne z zasadami Pythona.

### Dozwolone

```python
imie = "Adam"
wiek_uzytkownika = 30
liczba1 = 100
_ukryta = "sekret"
```

### Niedozwolone

```python
# 1imie = "Adam"
# moje-imie = "Adam"
# class = "A"
```

Powody:

- nazwa nie może zaczynać się od cyfry,
- myślnik `-` nie jest częścią nazwy zmiennej,
- nie wolno używać słów kluczowych języka.

### Dobre zasady

- używaj małych liter,
- oddzielaj słowa podkreśleniem: `moja_zmienna`,
- nadawaj sensowne nazwy,
- unikaj nazw typu `a`, `x`, `cos`, jeśli nie są naprawdę potrzebne.

### Dobre przykłady

```python
imie_uzytkownika = "Marek"
liczba_punktow = 87
cena_produktu = 49.99
```

### Złe przykłady

```python
a = "Marek"
x1 = 87
zzz = 49.99
```

Krótkie nazwy czasem są okej, ale głównie w bardzo małym, oczywistym kontekście, np. w matematyce:

```python
for i in range(10):
    print(i)
```

---

## Przypisanie wartości

Przypisanie oznacza związanie nazwy z wartością.

```python
x = 5
```

Znak `=` w Pythonie nie oznacza "jest równe" w sensie matematycznym.
Oznacza: **przypisz wartość po prawej do nazwy po lewej**.

### Zmiana wartości zmiennej

```python
punkty = 10
punkty = 20
```

Po drugiej linii zmienna `punkty` ma już wartość `20`.

### Przypisanie wielu zmiennych naraz

```python
a, b, c = 1, 2, 3
```

### Ta sama wartość do kilku zmiennych

```python
x = y = z = 0
```

To działa, ale przy typach mutowalnych trzeba uważać. Do tego wrócimy dalej.

---

## Zmienne a obiekty

To bardzo ważny temat.

W Pythonie zmienna nie jest samym "pudełkiem" z wartością.
Bardziej poprawnie:

**zmienna jest nazwą wskazującą na obiekt w pamięci.**

Przykład:

```python
a = 10
b = a
```

Tutaj:

- `a` wskazuje na wartość `10`,
- `b` też wskazuje na wartość `10`.

Przy typach niemutowalnych zwykle nie widać z tego problemu, ale przy listach i słownikach już tak:

```python
a = [1, 2]
b = a
b.append(3)

print(a)
print(b)
```

Obie nazwy wskazują na tę samą listę.

To jest jedna z najważniejszych rzeczy do zrozumienia przy pracy z Pythonem.

---

## Jak sprawdzić typ danych

Do sprawdzania typu używa się funkcji `type()`.

```python
print(type(10))
print(type(3.14))
print(type("Python"))
print(type(True))
```

Output:

```python
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

To bardzo przydatne na początku nauki i podczas debugowania.

W codziennym kodzie nie należy jednak bez potrzeby nadużywać ręcznego sprawdzania typów. Dużo częściej chcesz rozumieć zachowanie obiektu niż stale pytać o jego typ.

---

## Najważniejsze typy danych w Pythonie

Na tym etapie najważniejsze to:

- `int` - liczby całkowite,
- `float` - liczby zmiennoprzecinkowe,
- `bool` - wartości logiczne,
- `str` - tekst,
- `NoneType` - brak wartości,
- `list`,
- `tuple`,
- `set`,
- `dict`.

Nie musisz jeszcze znać wszystkiego o każdym z nich, ale powinieneś rozpoznawać, do czego służą.

---

## Typ liczbowy `int`

`int` to liczby całkowite:

```python
10
-3
0
```

Możesz wykonywać na nich działania:

```python
print(2 + 3)
print(10 - 4)
print(6 * 7)
```

Output:

```python
5
6
42
```

`int` jest bardzo często używany do:

- liczników,
- indeksów,
- wieku,
- liczby punktów,
- długości czegoś.

---

## Typ liczbowy `float`

`float` to liczby zmiennoprzecinkowe:

```python
3.14
0.5
-12.7
```

Przykład:

```python
cena = 19.99
waga = 72.5
```

Ważna uwaga:

`float` nie zawsze przechowuje liczby dziesiętne idealnie dokładnie. To normalne dla komputerów.

Na poziomie podstaw wystarczy pamiętać, że:

- do zwykłych obliczeń `float` jest okej,
- do bardzo precyzyjnych finansowych tematów używa się ostrożniejszych narzędzi.

---

## Typ logiczny `bool`

`bool` ma tylko dwie wartości:

- `True`
- `False`

Przykład:

```python
czy_pelnoletni = True
czy_ma_dlug = False
```

Wynik porównań zwykle też jest typu `bool`:

```python
print(5 > 3)
print(10 == 10)
```

Output:

```python
True
True
```

---

## Typ tekstowy `str`

`str` reprezentuje tekst:

```python
imie = "Anna"
miasto = "Krakow"
```

Stringi są:

- niemutowalne,
- sekwencyjne,
- bardzo często używane.

Pełny temat stringów rozwijamy w osobnym pliku:

- [02-stringi-i-f-stringi-python.md](/home/kacper/Desktop/Python/01.%20Fundamenty/02-stringi-i-f-stringi-python.md)

---

## Brak wartości: `NoneType`

`None` oznacza brak wartości.

```python
wynik = None
```

To nie jest ani `0`, ani pusty string, ani pusta lista.

Typ:

```python
print(type(None))
```

Output:

```python
<class 'NoneType'>
```

Temat ten jest bardzo ważny i rozwijany osobno w:

- [04-none-truthy-falsy-python.md](/home/kacper/Desktop/Python/01.%20Fundamenty/04-none-truthy-falsy-python.md)

---

## Typy sekwencyjne i kolekcje

Poza prostymi typami Python ma też typy przechowujące wiele elementów.

Najważniejsze na tym etapie:

- `list` - lista,
- `tuple` - krotka,
- `set` - zbiór,
- `dict` - słownik.

---

## Lista `list`

Lista jest uporządkowaną kolekcją elementów.

```python
liczby = [1, 2, 3]
imiona = ["Anna", "Jan", "Ola"]
```

Lista:

- zachowuje kolejność,
- jest mutowalna,
- może przechowywać różne typy danych.

```python
dane = [1, "tekst", True]
```

---

## Krotka `tuple`

Krotka wygląda podobnie do listy, ale jest niemutowalna.

```python
punkt = (10, 20)
```

Krotki często nadają się do:

- stałych zestawów danych,
- współrzędnych,
- zwracania kilku wartości z funkcji.

---

## Zbiór `set`

Zbiór przechowuje unikalne elementy.

```python
liczby = {1, 2, 3}
```

Przydaje się, gdy:

- chcesz usunąć duplikaty,
- chcesz szybko sprawdzać, czy coś należy do zbioru.

---

## Słownik `dict`

Słownik przechowuje pary klucz-wartość.

```python
uzytkownik = {
    "imie": "Anna",
    "wiek": 30,
}
```

Słownik jest bardzo ważny, bo często reprezentuje:

- rekord danych,
- konfigurację,
- odpowiedź z API,
- parametry programu.

---

## Typy mutowalne i niemutowalne

To jedna z najważniejszych klasyfikacji.

### Typy mutowalne

Można je zmieniać po utworzeniu.

Przykłady:

- `list`
- `dict`
- `set`

### Typy niemutowalne

Nie można ich zmieniać "w miejscu".

Przykłady:

- `int`
- `float`
- `bool`
- `str`
- `tuple`

To bardzo ważne, bo wpływa na:

- kopiowanie danych,
- działanie przypisań,
- przekazywanie obiektów do funkcji.

---

## Rzutowanie typów

Czasem chcesz zamienić jeden typ na inny.

Przykłady:

```python
print(int("5"))
print(float("3.14"))
print(str(123))
print(bool(1))
```

Output:

```python
5
3.14
123
True
```

To nazywa się rzutowaniem albo konwersją typu.

Ważne:

```python
int("abc")
```

spowoduje `ValueError`.

Nie każdą wartość da się bezpiecznie zamienić na dowolny typ.

---

## Operatory i typy danych

Operator może działać różnie zależnie od typu danych.

Przykład:

```python
print(2 + 3)
print("Ala" + " ma kota")
print([1, 2] + [3, 4])
```

Output:

```python
5
Ala ma kota
[1, 2, 3, 4]
```

Ten sam operator `+`:

- dodaje liczby,
- skleja stringi,
- łączy listy.

To bardzo ważna obserwacja: typ wpływa na zachowanie operacji.

---

## Porównywanie wartości i typów

Wartość:

```python
print(5 == 5)
```

Output:

```python
True
```

Typ:

```python
print(type(5) == int)
```

Output:

```python
True
```

To są różne pytania:

- "czy te wartości są równe?"
- "jakiego typu jest ten obiekt?"

Nie należy ich mylić.

---

## Prawda i fałsz w Pythonie

Nie tylko `True` i `False` mają sens logiczny.

Falsy są m.in.:

- `0`
- `0.0`
- `""`
- `[]`
- `{}`
- `None`

Truthy są np.:

- `1`
- `"tekst"`
- `[1, 2]`

To temat rozwinięty szerzej w:

- [04-none-truthy-falsy-python.md](/home/kacper/Desktop/Python/01.%20Fundamenty/04-none-truthy-falsy-python.md)

---

## Kopiowanie danych i pułapki

Przykład pułapki:

```python
a = [1, 2]
b = a
b.append(3)

print(a)
```

Output:

```python
[1, 2, 3]
```

To nie jest kopia. To druga nazwa dla tej samej listy.

Jeśli chcesz kopię listy:

```python
a = [1, 2]
b = a.copy()
```

Na tym etapie wystarczy rozumieć, że:

- przypisanie nie zawsze tworzy nowy obiekt,
- przy typach mutowalnych trzeba uważać.

---

## Wejście od użytkownika i typy danych

To bardzo ważne:

```python
wartosc = input("Podaj liczbe: ")
print(type(wartosc))
```

Jeśli użytkownik wpisze:

```python
123
```

to output będzie:

```python
<class 'str'>
```

`input()` zawsze zwraca `str`.

Jeśli chcesz liczbę:

```python
liczba = int(input("Podaj liczbe: "))
```

To jest jedna z najczęstszych pułapek początkujących.

---

## Typowe błędy początkujących

- mylenie `=` z `==`,
- oczekiwanie, że `input()` zwróci liczbę,
- brak rozróżnienia między typami mutowalnymi i niemutowalnymi,
- używanie nieczytelnych nazw zmiennych,
- mylenie `None` z pustymi wartościami,
- brak świadomości, że przypisanie obiektu mutowalnego nie tworzy kopii.

---

## Dobre praktyki

- nadawaj zmiennym czytelne nazwy,
- rozumiej, z jakim typem pracujesz,
- pamiętaj, że `input()` daje string,
- ostrożnie pracuj z typami mutowalnymi,
- używaj `type()` do nauki i debugowania,
- nie zgaduj działania kodu, uruchamiaj małe przykłady.

---

## Podsumowanie

Po tym materiale powinieneś rozumieć:

- czym jest zmienna,
- czym jest typ danych,
- jakie są najważniejsze typy w Pythonie,
- czym różnią się typy mutowalne i niemutowalne,
- dlaczego przypisanie i kopiowanie to nie to samo,
- dlaczego `input()` tak często prowadzi do błędów typów.

To są podstawy, bez których dalsza nauka Pythona będzie dużo trudniejsza.

---

## Mini ściąga

```python
x = 10
y = 3.14
name = "Anna"
active = True
nothing = None

print(type(x))
print(int("5"))
print(str(123))

lista = [1, 2, 3]
slownik = {"a": 1}
```

Najważniejsze:

- Python sam rozpoznaje typ przy przypisaniu,
- `input()` zwraca `str`,
- `list`, `dict`, `set` są mutowalne,
- `int`, `float`, `bool`, `str`, `tuple` są niemutowalne.

---

## Ćwiczenia

1. Utwórz zmienne `imie`, `wiek`, `miasto`, `czy_uczysz_sie`.
2. Wypisz typ każdej z nich.
3. Pokaż różnicę między przypisaniem liczby a przypisaniem listy.
4. Wczytaj liczbę od użytkownika i zamień ją na `int`.
5. Przygotuj listę i słownik z przykładowymi danymi.

---

## Przykładowe rozwiązania

### 1. Zmienne

```python
imie = "Jan"
wiek = 30
miasto = "Warszawa"
czy_uczysz_sie = True
```

### 2. Typy

```python
print(type(imie))
print(type(wiek))
print(type(miasto))
print(type(czy_uczysz_sie))
```

### 3. Liczba vs lista

```python
a = 10
b = a

lista1 = [1, 2]
lista2 = lista1
lista2.append(3)

print(a, b)
print(lista1, lista2)
```

### 4. `input()`

```python
liczba = int(input("Podaj liczbe: "))
print(liczba * 2)
```

Jeśli użytkownik wpisze:

```python
7
```

to output będzie:

```python
14
```

### 5. Kolekcje

```python
liczby = [1, 2, 3]
uzytkownik = {"imie": "Anna", "wiek": 30}
```

---

## Antywzorce i pułapki z życia

### Antywzorzec 1: zgadywanie typu zamiast jego rozumienia

```python
wartosc = input("Podaj liczbe: ")
print(wartosc + 10)
```

To się wywali, bo `input()` zwraca `str`.

Lepsze podejście:

```python
wartosc = int(input("Podaj liczbe: "))
print(wartosc + 10)
```

### Antywzorzec 2: przypadkowe współdzielenie listy

```python
a = [1, 2]
b = a
b.append(3)
```

Jeśli oczekiwałeś kopii, to logika programu będzie błędna.

### Antywzorzec 3: wrzucanie wszystkiego do jednego typu

```python
dane = ["Anna", "30", "True"]
```

To może działać chwilę, ale zwykle prowadzi do chaosu znaczeniowego. Lepiej świadomie rozumieć, który element jest tekstem, który liczbą, a który flagą logiczną.

---

## Mini case study

Załóżmy, że budujesz bardzo prosty formularz użytkownika:

```python
imie = input("Imie: ")
wiek = input("Wiek: ")
aktywny = input("Aktywny? ")
```

Jeśli zostawisz wszystko jako `str`, później pojawią się problemy:

- wieku nie porównasz sensownie z liczbą,
- flaga logiczna nie będzie prawdziwym `bool`,
- puste wartości mogą mylić się z brakiem danych.

Lepsza wersja:

```python
imie = input("Imie: ").strip()
wiek = int(input("Wiek: "))
aktywny = input("Aktywny? ").strip().lower() == "tak"
```

To prosty przykład, ale pokazuje ważną zasadę:

**dobre rozumienie typów danych od początku zmniejsza liczbę błędów w całym programie.**

---

## Mini projekt po rozdziale

Zbuduj plik `profil_uzytkownika.py`, który:

- pobiera imię, wiek i miasto,
- konwertuje wiek do `int`,
- przechowuje dane w słowniku,
- wypisuje typ każdej wartości,
- pokazuje, które obiekty są mutowalne, a które nie.

To małe zadanie bardzo dobrze scala:

- zmienne,
- typy danych,
- `input()`,
- słowniki,
- konwersję typów.
