# Funkcje w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co używać funkcji](#po-co-używać-funkcji)
3. [Definiowanie funkcji](#definiowanie-funkcji)
4. [Parametry i argumenty](#parametry-i-argumenty)
5. [`return` kontra `print`](#return-kontra-print)
6. [Wartości domyślne](#wartości-domyślne)
7. [Argumenty pozycyjne i nazwane](#argumenty-pozycyjne-i-nazwane)
8. [Funkcje bez jawnego `return`](#funkcje-bez-jawnego-return)
9. [Jedna odpowiedzialność funkcji](#jedna-odpowiedzialność-funkcji)
10. [Nazewnictwo funkcji](#nazewnictwo-funkcji)
11. [Typowe pułapki początkujących](#typowe-pułapki-początkujących)
12. [Praktyczne przykłady](#praktyczne-przykłady)
13. [Dobre praktyki](#dobre-praktyki)
14. [Podsumowanie](#podsumowanie)
15. [Mini ściąga](#mini-ściąga)
16. [Ćwiczenia](#ćwiczenia)
17. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Funkcje są jednym z najważniejszych narzędzi do organizowania kodu.

Pozwalają:

- unikać duplikacji,
- nadawać nazwę logice,
- rozbijać problem na mniejsze części,
- łatwiej testować kod,
- pisać programy, które da się rozwijać.

Bez funkcji większy skrypt bardzo szybko zamienia się w bałagan.

---

## Po co używać funkcji

Funkcja pozwala zamknąć pewien fragment logiki pod sensowną nazwą.

Zamiast powtarzać kilka linijek w różnych miejscach:

```python
imie = input("Podaj imie: ").strip().capitalize()
```

możesz zrobić:

```python
def normalizuj_imie(imie):
    return imie.strip().capitalize()
```

Wtedy:

- kod jest krótszy,
- łatwiej go czytać,
- łatwiej poprawić jedno miejsce niż pięć kopii.

---

## Definiowanie funkcji

Podstawowa składnia:

```python
def przywitaj():
    print("Czesc")
```

Wywołanie:

```python
przywitaj()
```

Funkcja nie wykonuje się w momencie definicji. Definicja tylko mówi Pythonowi:

"zapamiętaj ten kawałek logiki pod tą nazwą".

---

## Parametry i argumenty

```python
def przywitaj(imie):
    print(f"Czesc, {imie}")

przywitaj("Anna")
```

Tutaj:

- `imie` to parametr,
- `"Anna"` to argument.

Możesz mieć więcej parametrów:

```python
def dodaj(a, b):
    return a + b
```

---

## `return` kontra `print`

To jedna z najważniejszych rzeczy do zrozumienia.

`print()`:

- tylko wypisuje coś na ekran,
- nie zwraca użytecznego wyniku do dalszego przetwarzania.

`return`:

- oddaje wartość z funkcji,
- pozwala użyć wyniku dalej.

Przykład:

```python
def dodaj(a, b):
    return a + b

wynik = dodaj(2, 3)
print(wynik)
```

Output:

```python
5
```

W praktyce funkcje obliczeniowe zwykle powinny zwracać dane, a nie tylko je wypisywać.

---

## Wartości domyślne

Możesz ustawić parametr domyślny:

```python
def powitaj(imie="swiecie"):
    return f"Czesc, {imie}"
```

Wywołania:

```python
print(powitaj())
print(powitaj("Ola"))
```

Output:

```python
Czesc, swiecie
Czesc, Ola
```

To wygodne, gdy pewien argument bywa opcjonalny.

---

## Argumenty pozycyjne i nazwane

Pozycyjne:

```python
def utworz_uzytkownika(imie, wiek):
    return f"{imie}, {wiek}"

utworz_uzytkownika("Anna", 30)
```

Nazwane:

```python
utworz_uzytkownika(imie="Anna", wiek=30)
```

Argumenty nazwane poprawiają czytelność, zwłaszcza gdy parametrów jest więcej.

---

## Funkcje bez jawnego `return`

Jeśli funkcja nie ma jawnego `return`, zwraca `None`.

```python
def hello():
    print("czesc")

wynik = hello()
print(wynik)
```

Output:

```python
czesc
None
```

To ważne, bo początkujący często zakładają, że jeśli coś się wypisało, to funkcja "zwróciła tekst". To nieprawda.

---

## Jedna odpowiedzialność funkcji

Dobra funkcja zwykle robi jedną rzecz.

Lepsze:

```python
def parse_age(text):
    return int(text)

def is_adult(age):
    return age >= 18
```

niż jedna wielka funkcja, która:

- pobiera dane,
- waliduje je,
- wypisuje komunikaty,
- zapisuje stan,
- liczy wynik.

Małe funkcje łatwiej:

- testować,
- czytać,
- wykorzystywać ponownie.

---

## Nazewnictwo funkcji

Nazwa funkcji powinna mówić, co ona robi.

Dobre nazwy:

- `calculate_total`
- `normalize_email`
- `is_even`
- `parse_int`

Słabe nazwy:

- `do_it`
- `fun1`
- `handle_data`

Jeśli nazwa jest niejasna, to zwykle znak, że API funkcji też będzie niejasne.

---

## Typowe pułapki początkujących

- mylenie `print()` z `return`,
- zbyt duże funkcje,
- nieczytelne nazwy,
- upychanie zbyt wielu odpowiedzialności do jednej funkcji,
- brak zwracania wyniku do dalszej pracy,
- tworzenie funkcji, która tylko owija jedną oczywistą linię bez zysku w czytelności.

---

## Praktyczne przykłady

### Pole prostokąta

```python
def pole_prostokata(a, b):
    return a * b
```

### Sprawdzenie parzystości

```python
def jest_parzysta(n):
    return n % 2 == 0
```

### Średnia z listy

```python
def policz_srednia(liczby):
    return sum(liczby) / len(liczby)
```

### Normalizacja imienia

```python
def formatuj_imie(imie="nieznajomy"):
    return imie.strip().capitalize()
```

---

## Dobre praktyki

- funkcja powinna mieć czytelną nazwę,
- jeśli liczy wynik, zwykle powinna używać `return`,
- jedna funkcja powinna mieć jedną główną odpowiedzialność,
- używaj argumentów nazwanych, gdy poprawiają czytelność,
- nie rób funkcji zbyt sprytnych kosztem prostoty.

---

## Podsumowanie

Funkcje to podstawa organizowania kodu.

Najważniejsze rzeczy do opanowania:

- różnica między `print()` i `return`,
- parametry i argumenty,
- wartości domyślne,
- małe, czytelne funkcje,
- sensowne nazewnictwo.

---

## Mini ściąga

```python
def dodaj(a, b):
    return a + b

def powitaj(imie="swiecie"):
    return f"Czesc, {imie}"

def jest_parzysta(n):
    return n % 2 == 0
```

---

## Ćwiczenia

1. Napisz funkcję `dodaj(a, b)`.
2. Napisz funkcję `powitaj(imie)`.
3. Napisz funkcję `pole_prostokata(a, b)`.
4. Napisz funkcję z argumentem domyślnym.
5. Napisz funkcję liczącą średnią z listy.

---

## Przykładowe rozwiązania

### 1. `dodaj`

```python
def dodaj(a, b):
    return a + b
```

### 2. `powitaj`

```python
def powitaj(imie):
    return f"Witaj {imie}"
```

### 3. `pole_prostokata`

```python
def pole_prostokata(a, b):
    return a * b
```

### 4. Argument domyślny

```python
def formatuj_imie(imie="nieznajomy"):
    return imie.strip().capitalize()
```

### 5. Średnia

```python
def policz_srednia(lista):
    return sum(lista) / len(lista)
```
