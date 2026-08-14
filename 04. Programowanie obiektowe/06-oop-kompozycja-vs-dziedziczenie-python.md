# Kompozycja vs Dziedziczenie w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Dlaczego to zagadnienie jest ważne](#dlaczego-to-zagadnienie-jest-ważne)
3. [Czym jest dziedziczenie](#czym-jest-dziedziczenie)
4. [Czym jest kompozycja](#czym-jest-kompozycja)
5. [Relacja "jest rodzajem"](#relacja-jest-rodzajem)
6. [Relacja "ma w sobie"](#relacja-ma-w-sobie)
7. [Kiedy używać dziedziczenia](#kiedy-używać-dziedziczenia)
8. [Kiedy używać kompozycji](#kiedy-używać-kompozycji)
9. [Dlaczego kompozycja bywa lepsza](#dlaczego-kompozycja-bywa-lepsza)
10. [Pułapki złego dziedziczenia](#pułapki-złego-dziedziczenia)
11. [Kompozycja w praktyce](#kompozycja-w-praktyce)
12. [Dziedziczenie w praktyce](#dziedziczenie-w-praktyce)
13. [Łączenie obu podejść](#łączenie-obu-podejść)
14. [Projektowe pytania pomocnicze](#projektowe-pytania-pomocnicze)
15. [Typowe błędy początkujących](#typowe-błędy-początkujących)
16. [Praktyczne przykłady](#praktyczne-przykłady)
17. [Dobre praktyki](#dobre-praktyki)
18. [Podsumowanie](#podsumowanie)
19. [Mini ściąga](#mini-ściąga)
20. [Ćwiczenia](#ćwiczenia)
21. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

To jeden z najważniejszych tematów projektowych w OOP.

Wielu początkujących za szybko sięga po dziedziczenie, bo wydaje się najbardziej "obiektowe".

Tymczasem bardzo często lepszym rozwiązaniem jest **kompozycja**.

To temat ważny nie tylko technicznie, ale też projektowo.

---

## Dlaczego to zagadnienie jest ważne

Bo wybór między:

- dziedziczeniem
- kompozycją

wpływa na:

- czytelność kodu,
- elastyczność,
- możliwość rozbudowy,
- ryzyko błędów,
- łatwość testowania.

---

## Czym jest dziedziczenie

Dziedziczenie to relacja:

**A jest rodzajem B**

Przykład:

- pies jest rodzajem zwierzęcia,
- rower jest rodzajem pojazdu.

W kodzie:

```python
class Zwierze:
    pass

class Pies(Zwierze):
    pass
```

To ma sens, bo pies naprawdę jest rodzajem zwierzęcia.

---

## Czym jest kompozycja

Kompozycja to relacja:

**A ma w sobie B**

Przykład:

- samochód ma silnik,
- komputer ma procesor,
- sklep ma koszyk.

W kodzie:

```python
class Silnik:
    pass

class Samochod:
    def __init__(self):
        self.silnik = Silnik()
```

Tutaj `Samochod` nie jest rodzajem `Silnik`.

On po prostu ma silnik jako swoją część.

---

## Relacja "jest rodzajem"

To sygnał, że dziedziczenie może mieć sens.

Przykłady:

- `Pies` jest rodzajem `Zwierze`,
- `Student` jest rodzajem `Osoba`,
- `Kwadrat` jest rodzajem `Figura`.

---

## Relacja "ma w sobie"

To sygnał, że kompozycja często jest lepsza.

Przykłady:

- `Samochod` ma `Silnik`,
- `Dom` ma `Drzwi`,
- `Gra` ma `Plansze`,
- `Sklep` ma `Koszyk`.

---

## Kiedy używać dziedziczenia

Gdy:

- istnieje naturalna relacja "jest rodzajem",
- klasa pochodna logicznie jest specjalnym przypadkiem klasy bazowej,
- współdzielone zachowanie naprawdę jest wspólne i sensowne.

---

## Kiedy używać kompozycji

Gdy:

- obiekt składa się z innych obiektów,
- chcesz łączyć zachowania bez sztucznej hierarchii,
- zależy Ci na większej elastyczności,
- relacja "jest rodzajem" nie jest naturalna.

---

## Dlaczego kompozycja bywa lepsza

Bo:

- jest luźniej powiązana,
- łatwiej wymieniać części,
- łatwiej testować,
- zmiany w jednej klasie mniej psują inne,
- unika się dziwnych i sztucznych hierarchii.

To dlatego często mówi się:

**prefer composition over inheritance**

czyli:

**często lepiej wybierać kompozycję niż dziedziczenie**

---

## Pułapki złego dziedziczenia

Jeśli użyjesz dziedziczenia tam, gdzie nie ma prawdziwej relacji "jest rodzajem", powstają problemy.

Na przykład:

czy `Silnik` jest rodzajem `Samochod`?

Nie.

Więc dziedziczenie byłoby tu złym pomysłem.

---

## Kompozycja w praktyce

Przykład:

```python
class Silnik:
    def uruchom(self):
        print("Silnik uruchomiony")

class Samochod:
    def __init__(self):
        self.silnik = Silnik()

    def start(self):
        self.silnik.uruchom()
        print("Samochod rusza")
```

To bardzo naturalna kompozycja.

Przykład użycia:

```python
auto = Samochod()
auto.start()
```

Wynik:

```python
Silnik uruchomiony
Samochod rusza
```

---

## Dziedziczenie w praktyce

Przykład:

```python
class Zwierze:
    def jedz(self):
        print("Jem")

class Pies(Zwierze):
    def szczekaj(self):
        print("Hau")
```

Tu dziedziczenie ma sens.

Przykład użycia:

```python
pies = Pies()
pies.jedz()
pies.szczekaj()
```

Wynik:

```python
Jem
Hau
```

---

## Łączenie obu podejść

W prawdziwych programach często używa się obu.

Na przykład:

- `Pies` dziedziczy po `Zwierze`,
- ale jednocześnie `Pies` może mieć obiekt `Obroza`.

To całkowicie normalne.

---

## Projektowe pytania pomocnicze

Warto zadać sobie pytanie:

### Czy A naprawdę jest rodzajem B?

Jeśli tak, dziedziczenie może mieć sens.

### Czy A raczej zawiera B?

Jeśli tak, zwykle lepsza będzie kompozycja.

---

## Typowe błędy początkujących

### 1. Nadużywanie dziedziczenia

### 2. Budowanie sztucznych hierarchii

### 3. Ignorowanie kompozycji jako prostszego rozwiązania

### 4. Mylenie "używa" z "jest"

To bardzo częsty błąd projektowy.

---

## Praktyczne przykłady

### Dobre dziedziczenie

```python
class Osoba:
    def przedstaw_sie(self):
        print("Jestem osoba")

class Student(Osoba):
    def ucz_sie(self):
        print("Ucze sie")
```

Przykład użycia:

```python
s = Student()
s.przedstaw_sie()
s.ucz_sie()
```

Wynik:

```python
Jestem osoba
Ucze sie
```

### Dobra kompozycja

```python
class Klawiatura:
    def pisz(self):
        print("Pisze")

class Komputer:
    def __init__(self):
        self.klawiatura = Klawiatura()
```

Przykład użycia:

```python
komputer = Komputer()
komputer.klawiatura.pisz()
```

Wynik:

```python
Pisze
```

### Inny przykład kompozycji

```python
class Adres:
    def __init__(self, miasto):
        self.miasto = miasto

class Firma:
    def __init__(self, nazwa, adres):
        self.nazwa = nazwa
        self.adres = adres
```

---

## Dobre praktyki

### Najpierw pytaj: "jest rodzajem" czy "ma w sobie"

### Nie używaj dziedziczenia tylko dlatego, że brzmi bardziej zaawansowanie

### W wielu przypadkach kompozycja daje bardziej elastyczny kod

### Gdy hierarchia zaczyna robić się dziwna, zatrzymaj się i przemyśl model

### Praktyczna zasada

Jeśli możesz uczciwie powiedzieć "A jest rodzajem B", rozważ dziedziczenie.

Jeśli bardziej pasuje zdanie "A ma B" albo "A używa B", zwykle lepsza będzie kompozycja.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- dziedziczenie opisuje relację "jest rodzajem",
- kompozycja opisuje relację "ma w sobie",
- kompozycja często daje większą elastyczność,
- dziedziczenie warto stosować tylko wtedy, gdy naprawdę pasuje semantycznie,
- to jedno z najważniejszych pytań projektowych w OOP.

Najważniejszy test:

spróbuj wypowiedzieć relację na głos.

Jeśli brzmi naturalnie jako "jest rodzajem", dziedziczenie może być dobre.

Jeśli brzmi naturalnie jako "ma w sobie" albo "korzysta z", wybierz kompozycję.

---

## Mini ściąga

### Dziedziczenie

```python
class Pies(Zwierze):
    ...
```

### Kompozycja

```python
class Samochod:
    def __init__(self):
        self.silnik = Silnik()
```

---

## Ćwiczenia

### Ćwiczenie 1

Zaprojektuj przykład poprawnego dziedziczenia.

### Ćwiczenie 2

Zaprojektuj przykład poprawnej kompozycji.

### Ćwiczenie 3

Dla par:

- samochód / silnik
- pies / zwierzę
- firma / adres

określ, gdzie pasuje dziedziczenie, a gdzie kompozycja.

---

## Przykładowe rozwiązania

### Ćwiczenie 1

```python
class Figura:
    pass

class Kolo(Figura):
    pass
```

### Ćwiczenie 2

```python
class Silnik:
    pass

class Samochod:
    def __init__(self):
        self.silnik = Silnik()
```

### Ćwiczenie 3

- samochód / silnik -> kompozycja
- pies / zwierzę -> dziedziczenie
- firma / adres -> kompozycja
