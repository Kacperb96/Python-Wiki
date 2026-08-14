# Klasy, obiekty, metody w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest programowanie obiektowe](#czym-jest-programowanie-obiektowe)
3. [Czym jest klasa](#czym-jest-klasa)
4. [Czym jest obiekt](#czym-jest-obiekt)
5. [Klasa a obiekt](#klasa-a-obiekt)
6. [Tworzenie pierwszej klasy](#tworzenie-pierwszej-klasy)
7. [Tworzenie obiektów](#tworzenie-obiektów)
8. [Czym jest metoda](#czym-jest-metoda)
9. [`self` w metodach](#self-w-metodach)
10. [Wywoływanie metod](#wywoływanie-metod)
11. [Stan obiektu](#stan-obiektu)
12. [Zachowanie obiektu](#zachowanie-obiektu)
13. [Wiele obiektów tej samej klasy](#wiele-obiektów-tej-samej-klasy)
14. [Dlaczego klasy są przydatne](#dlaczego-klasy-są-przydatne)
15. [Klasa jako własny typ danych](#klasa-jako-własny-typ-danych)
16. [Typowe błędy początkujących](#typowe-błędy-początkujących)
17. [Praktyczne przykłady](#praktyczne-przykłady)
18. [Dobre praktyki](#dobre-praktyki)
19. [Podsumowanie](#podsumowanie)
20. [Mini ściąga](#mini-ściąga)
21. [Ćwiczenia](#ćwiczenia)
22. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Programowanie obiektowe, czyli OOP, to jeden z najważniejszych sposobów organizowania kodu.

Pozwala myśleć o programie nie tylko jako o:

- funkcjach,
- zmiennych,
- instrukcjach,

ale jako o współpracujących ze sobą **obiektach**.

W Pythonie obiektowość jest bardzo naturalna, bo praktycznie wszystko jest obiektem:

- liczby,
- stringi,
- listy,
- słowniki,
- funkcje,
- klasy.

Ten poradnik jest pierwszym krokiem do zrozumienia OOP:

- czym jest klasa,
- czym jest obiekt,
- czym jest metoda,
- jak to wszystko działa razem.

---

## Czym jest programowanie obiektowe

Najprościej:

programowanie obiektowe to styl pisania kodu, w którym łączysz:

- dane,
- zachowanie tych danych

w jedną całość.

Przykład:

zamiast trzymać osobno:

- nazwę samochodu,
- prędkość samochodu,
- funkcję przyspieszającą samochód,

możesz mieć obiekt `Samochod`, który ma:

- swoje dane,
- swoje metody.

To daje bardziej uporządkowany kod.

---

## Czym jest klasa

Klasa to **przepis** albo **szablon** na tworzenie obiektów.

Przykład z życia:

- klasa to projekt domu,
- obiekt to konkretny zbudowany dom.

W Pythonie klasę definiujesz słowem kluczowym:

```python
class Osoba:
    pass
```

To najprostsza możliwa klasa.

---

## Czym jest obiekt

Obiekt to konkretna instancja klasy.

Przykład:

```python
class Osoba:
    pass

ania = Osoba()
bartek = Osoba()
```

Tutaj:

- `Osoba` to klasa,
- `ania` i `bartek` to obiekty tej klasy.

Każdy obiekt może mieć własny stan.

---

## Klasa a obiekt

To bardzo ważne rozróżnienie.

### Klasa

Opisuje, jak mają wyglądać obiekty.

### Obiekt

To konkretny egzemplarz utworzony na podstawie klasy.

Przykład:

```python
class Pies:
    pass

pies1 = Pies()
pies2 = Pies()
```

`pies1` i `pies2` są różnymi obiektami, mimo że pochodzą z tej samej klasy.

---

## Tworzenie pierwszej klasy

Przykład klasy z metodą:

```python
class Pies:
    def szczekaj(self):
        print("Hau hau!")
```

Tutaj:

- `Pies` to klasa,
- `szczekaj` to metoda.

Jeśli utworzysz obiekt i wywołasz metodę:

```python
azor = Pies()
azor.szczekaj()
```

to output będzie:

```python
Hau hau!
```

---

## Tworzenie obiektów

Obiekt tworzy się przez wywołanie klasy:

```python
azor = Pies()
```

Teraz można wywołać metodę:

```python
azor.szczekaj()
```

Output:

```python
Hau hau!
```

---

## Czym jest metoda

Metoda to funkcja zdefiniowana wewnątrz klasy.

Najczęściej opisuje zachowanie obiektu.

Przykład:

```python
class Kalkulator:
    def dodaj(self, a, b):
        return a + b
```

Metody bardzo często korzystają z danych obiektu.

```python
k = Kalkulator()
print(k.dodaj(2, 3))
```

Output:

```python
5
```

---

## `self` w metodach

`self` to jeden z najważniejszych elementów OOP w Pythonie.

Najprościej:

`self` oznacza:

**ten konkretny obiekt, na którym pracuje metoda**

Przykład:

```python
class Pies:
    def przedstaw_sie(self):
        print("Jestem psem")
```

`self` pojawia się jako pierwszy parametr metody instancji.

### Ważne

Przy wywołaniu:

```python
azor.przedstaw_sie()
```

Python sam przekazuje `azor` jako `self`.

To znaczy, że:

```python
azor.przedstaw_sie()
```

jest w przybliżeniu równoważne:

```python
Pies.przedstaw_sie(azor)
```

---

## Wywoływanie metod

Metodę najczęściej wywołujesz przez obiekt:

```python
azor.szczekaj()
```

W praktyce Python tłumaczy to mniej więcej jak:

```python
Pies.szczekaj(azor)
```

Na początek wystarczy pamiętać:

- w definicji piszesz `self`,
- przy wywołaniu go nie podajesz ręcznie.

To bardzo częsty błąd początkujących, że próbują wywołać metodę z ręcznie dopisanym `self`.

---

## Stan obiektu

Stan obiektu to jego dane.

Na przykład pies może mieć:

- imię,
- wiek,
- kolor.

Obiekt osoby może mieć:

- imię,
- nazwisko,
- wiek.

To dane należące do konkretnego egzemplarza.

Przykład:

```python
class Pies:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

azor = Pies("Azor", 4)
print(azor.imie)
print(azor.wiek)
```

Output:

```python
Azor
4
```

---

## Zachowanie obiektu

Zachowanie obiektu to to, co potrafi zrobić.

Na przykład:

- samochód może przyspieszać,
- konto bankowe może wpłacać pieniądze,
- użytkownik może się zalogować,
- pies może szczekać.

W klasie takie zachowania zapisuje się jako metody.

To bardzo ważne rozróżnienie:

- atrybuty opisują stan,
- metody opisują zachowanie.

---

## Wiele obiektów tej samej klasy

Przykład:

```python
class Kot:
    def miaucz(self):
        print("Miau")

kot1 = Kot()
kot2 = Kot()
```

To dwa różne obiekty.

Mogą należeć do tej samej klasy, ale być oddzielnymi egzemplarzami.

```python
kot1.miaucz()
kot2.miaucz()
```

Output:

```python
Miau
Miau
```

---

## Dlaczego klasy są przydatne

Bo pozwalają:

- grupować dane i zachowania,
- porządkować kod,
- modelować rzeczywiste obiekty albo pojęcia,
- unikać chaosu w większych programach,
- łatwiej rozbudowywać projekt.

To właśnie moment, w którym kod zaczyna przypominać model problemu, a nie tylko serię niezależnych instrukcji.

---

## Klasa jako własny typ danych

Kiedy tworzysz klasę, tworzysz własny typ danych.

Przykład:

```python
class Samochod:
    pass

auto = Samochod()
print(type(auto))
```

To bardzo ważne:

Python pozwala Ci budować własne typy, a nie tylko używać wbudowanych.

Output:

```python
<class '__main__.Samochod'>
```

---

## Typowe błędy początkujących

### 1. Mylenie klasy z obiektem

### 2. Zapominanie o `self`

### 3. Ręczne przekazywanie `self` przy wywołaniu

### 4. Myślenie, że każda metoda musi coś zwracać

Nie musi. Czasem metoda tylko coś robi.

### 5. Traktowanie klas jak zbędnej komplikacji

W małych programach tak bywa, ale w większych projektach klasy bardzo pomagają.

### 6. Robienie klasy bez sensownego modelu

Czasem lepsza będzie zwykła funkcja i prosty słownik niż sztuczna klasa.

---

## Praktyczne przykłady

### Prosta klasa

```python
class Lampa:
    def wlacz(self):
        print("Lampa wlaczona")

lampa = Lampa()
lampa.wlacz()
```

Output:

```python
Lampa wlaczona
```

### Klasa z dwiema metodami

```python
class Drzwi:
    def otworz(self):
        print("Drzwi otwarte")

    def zamknij(self):
        print("Drzwi zamkniete")
```

### Wiele obiektów

```python
class Konto:
    def pokaz_typ(self):
        print("To jest konto")

k1 = Konto()
k2 = Konto()

k1.pokaz_typ()
k2.pokaz_typ()
```

Output:

```python
To jest konto
To jest konto
```

---

## Dobre praktyki

### Nadawaj klasom nazwy w stylu `PascalCase`

Na przykład:

```python
class KontoBankowe:
    ...
```

### Nadawaj metodom nazwy małymi literami

Na przykład:

```python
def oblicz_sume(self):
    ...
```

### Nie twórz klasy bez potrzeby

Ale też nie bój się klas, gdy dane i zachowania naturalnie do siebie pasują.

Na początku warto pytać:

"czy ta klasa reprezentuje sensowny obiekt w moim programie?"

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- klasa to szablon,
- obiekt to instancja klasy,
- metoda to funkcja wewnątrz klasy,
- `self` oznacza konkretny obiekt,
- klasy pomagają łączyć dane i zachowanie w jedną całość.

To fundament całego OOP w Pythonie.

Najważniejsze do zapamiętania:

- klasa opisuje,
- obiekt istnieje,
- atrybuty przechowują stan,
- metody opisują zachowanie.

---

## Mini ściąga

```python
class Pies:
    def szczekaj(self):
        print("Hau")

azor = Pies()
azor.szczekaj()
```

---

## Ćwiczenia

### Ćwiczenie 1

Utwórz klasę `Kot` z metodą `miaucz`.

### Ćwiczenie 2

Utwórz dwa obiekty tej klasy i wywołaj metodę na obu.

### Ćwiczenie 3

Utwórz klasę `Przycisk` z metodami `wcisnij` i `pusc`.

---

## Przykładowe rozwiązania

### Ćwiczenie 1

```python
class Kot:
    def miaucz(self):
        print("Miau")
```

### Ćwiczenie 2

```python
kot1 = Kot()
kot2 = Kot()

kot1.miaucz()
kot2.miaucz()
```

### Ćwiczenie 3

```python
class Przycisk:
    def wcisnij(self):
        print("Klik")

    def pusc(self):
        print("Puszczono")
```

---

## Na koniec

Najlepiej uczyć się klas przez modelowanie prostych rzeczy:

1. zwierzę,
2. samochód,
3. konto,
4. gracz,
5. produkt.

Właśnie wtedy zaczyna być widać, po co klasy naprawdę istnieją.
