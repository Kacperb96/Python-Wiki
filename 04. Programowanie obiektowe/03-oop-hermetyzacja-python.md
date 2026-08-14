# Hermetyzacja w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest hermetyzacja](#czym-jest-hermetyzacja)
3. [Po co stosuje się hermetyzację](#po-co-stosuje-się-hermetyzację)
4. [Python a prywatność](#python-a-prywatność)
5. [Atrybut publiczny](#atrybut-publiczny)
6. [Atrybut z pojedynczym podkreśleniem](#atrybut-z-pojedynczym-podkreśleniem)
7. [Name mangling i podwójne podkreślenie](#name-mangling-i-podwójne-podkreślenie)
8. [Czy to naprawdę prywatne](#czy-to-naprawdę-prywatne)
9. [Gettery i settery](#gettery-i-settery)
10. [`@property`](#property)
11. [Walidacja danych przez hermetyzację](#walidacja-danych-przez-hermetyzację)
12. [Ukrywanie szczegółów implementacji](#ukrywanie-szczegółów-implementacji)
13. [Hermetyzacja a bezpieczeństwo kodu](#hermetyzacja-a-bezpieczeństwo-kodu)
14. [Typowe błędy początkujących](#typowe-błędy-początkujących)
15. [Praktyczne przykłady](#praktyczne-przykłady)
16. [Dobre praktyki](#dobre-praktyki)
17. [Podsumowanie](#podsumowanie)
18. [Mini ściąga](#mini-ściąga)
19. [Ćwiczenia](#ćwiczenia)
20. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Hermetyzacja to jeden z filarów OOP.

Najprościej:

chodzi o to, żeby:

- kontrolować dostęp do danych,
- ukrywać niepotrzebne szczegóły,
- chronić obiekt przed błędnym użyciem.

W Pythonie hermetyzacja działa trochę inaczej niż w wielu innych językach.

Nie ma tu sztywnego systemu `private`, `protected`, `public` w tym samym sensie jak np. w Javie czy C++.

Ale są bardzo ważne konwencje i mechanizmy.

---

## Czym jest hermetyzacja

Hermetyzacja oznacza łączenie danych i logiki ich obsługi tak, by z zewnątrz nie dało się łatwo psuć wnętrza obiektu.

Przykład:

jeśli obiekt reprezentuje konto bankowe, to nie chcesz, by ktoś dowolnie ustawiał stan konta bez kontroli.

Lepiej mieć metodę:

```python
wplac()
```

niż pozwalać na całkowicie swobodną zmianę wszystkiego.

---

## Po co stosuje się hermetyzację

Główne powody:

- ochrona spójności danych,
- walidacja wartości,
- uproszczenie użycia klasy,
- ukrycie szczegółów implementacji.

---

## Python a prywatność

Python stawia bardziej na:

- konwencję,
- odpowiedzialność programisty,
- czytelność,

niż na twarde blokady.

To znaczy:

Python nie mówi "tego absolutnie nie wolno dotknąć",
ale raczej:

"tego nie powinieneś dotykać, chyba że naprawdę wiesz, co robisz"

---

## Atrybut publiczny

To zwykły atrybut:

```python
class Osoba:
    def __init__(self, imie):
        self.imie = imie
```

Można go odczytywać i zmieniać z zewnątrz:

```python
o = Osoba("Ania")
print(o.imie)
o.imie = "Anna"
```

---

## Atrybut z pojedynczym podkreśleniem

Przykład:

```python
self._saldo
```

To konwencja znacząca:

"to jest wewnętrzne, nie używaj tego bez potrzeby"

To nie blokuje dostępu technicznie, ale daje ważny sygnał.

---

## Name mangling i podwójne podkreślenie

Przykład:

```python
self.__sekret
```

Python stosuje wtedy tzw. name mangling, czyli zmienia wewnętrznie nazwę atrybutu.

To utrudnia przypadkowy dostęp i przypadkowe nadpisanie w klasach pochodnych.

---

## Czy to naprawdę prywatne

Nie w sensie absolutnym.

W Pythonie nadal można dostać się do takiego atrybutu, jeśli bardzo chcesz.

Dlatego:

- pojedyncze `_` to konwencja,
- podwójne `__` to mechanizm utrudniający kolizje i przypadkowe użycie,
- ale nie jest to "żelazna ściana".

---

## Gettery i settery

To metody służące do kontrolowanego odczytu i zapisu danych.

Przykład:

```python
class Konto:
    def __init__(self):
        self._saldo = 0

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, wartosc):
        if wartosc < 0:
            raise ValueError("Saldo nie moze byc ujemne")
        self._saldo = wartosc
```

---

## `@property`

W Pythonie częściej niż klasyczne gettery/settery używa się `@property`.

Przykład:

```python
class Konto:
    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, wartosc):
        if wartosc < 0:
            raise ValueError("Saldo nie moze byc ujemne")
        self._saldo = wartosc
```

Teraz można pisać:

```python
konto.saldo = 100
print(konto.saldo)
```

ale nadal mieć kontrolę.

---

## Walidacja danych przez hermetyzację

To jedno z najważniejszych zastosowań.

Przykład:

```python
class Osoba:
    def __init__(self, wiek):
        self.wiek = wiek

    @property
    def wiek(self):
        return self._wiek

    @wiek.setter
    def wiek(self, wartosc):
        if wartosc < 0:
            raise ValueError("Wiek nie moze byc ujemny")
        self._wiek = wartosc
```

---

## Ukrywanie szczegółów implementacji

Hermetyzacja pomaga też ukrywać to, jak klasa działa w środku.

Użytkownik klasy powinien wiedzieć:

- jak jej używać,

ale niekoniecznie:

- jak dokładnie jest zrobiona wewnątrz.

---

## Hermetyzacja a bezpieczeństwo kodu

Hermetyzacja pomaga:

- ograniczać przypadkowe błędy,
- pilnować poprawnych danych,
- budować bardziej przewidywalne obiekty.

To nie chodzi o paranoję, tylko o dobrą organizację i bezpieczeństwo logiki.

---

## Typowe błędy początkujących

### 1. Myślenie, że `_x` jest naprawdę prywatne

To głównie konwencja.

### 2. Nadużywanie getterów i setterów bez potrzeby

Python lubi prostotę.

### 3. Brak walidacji tam, gdzie jest potrzebna

### 4. Przesadne ukrywanie wszystkiego

Nie wszystko musi być "prawie prywatne".

---

## Praktyczne przykłady

### Konto z walidacją

```python
class Konto:
    def __init__(self, saldo=0):
        self.saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, wartosc):
        if wartosc < 0:
            raise ValueError("Saldo nie moze byc ujemne")
        self._saldo = wartosc
```

### Wewnętrzne pole

```python
class Silnik:
    def __init__(self):
        self._temperatura = 20
```

### Podwójne podkreślenie

```python
class Test:
    def __init__(self):
        self.__sekret = 123
```

---

## Dobre praktyki

### Używaj `_nazwa` dla rzeczy wewnętrznych

### Używaj `@property`, gdy potrzebujesz walidacji lub kontrolowanego dostępu

### Nie komplikuj, jeśli zwykły publiczny atrybut wystarcza

### Ukrywaj to, co naprawdę powinno być ukryte

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- hermetyzacja to kontrola dostępu do danych i ukrywanie szczegółów,
- Python opiera się bardziej na konwencjach niż twardych blokadach,
- `_nazwa` oznacza "wewnętrzne",
- `__nazwa` uruchamia name mangling,
- `@property` to bardzo ważne narzędzie do eleganckiej kontroli danych.

---

## Mini ściąga

```python
class Konto:
    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo
```

---

## Ćwiczenia

### Ćwiczenie 1

Utwórz klasę `Osoba` z walidowanym wiekiem przez `@property`.

### Ćwiczenie 2

Utwórz klasę z atrybutem `_sekret`.

### Ćwiczenie 3

Utwórz klasę z `__kod`.

---

## Przykładowe rozwiązania

### Ćwiczenie 1

```python
class Osoba:
    def __init__(self, wiek):
        self.wiek = wiek

    @property
    def wiek(self):
        return self._wiek

    @wiek.setter
    def wiek(self, wartosc):
        if wartosc < 0:
            raise ValueError("Wiek nie moze byc ujemny")
        self._wiek = wartosc
```

### Ćwiczenie 2

```python
class Test:
    def __init__(self):
        self._sekret = 10
```

### Ćwiczenie 3

```python
class Test:
    def __init__(self):
        self.__kod = 1234
```
