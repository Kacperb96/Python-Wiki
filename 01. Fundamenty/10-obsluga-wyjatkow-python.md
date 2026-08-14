# Obsługa wyjątków w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym są wyjątki](#czym-są-wyjątki)
3. [Po co w ogóle obsługiwać wyjątki](#po-co-w-ogóle-obsługiwać-wyjątki)
4. [Błąd składni a wyjątek](#błąd-składni-a-wyjątek)
5. [Jak wygląda wyjątek w Pythonie](#jak-wygląda-wyjątek-w-pythonie)
6. [Najczęstsze wyjątki](#najczęstsze-wyjątki)
7. [Blok `try except`](#blok-try-except)
8. [Obsługa konkretnego wyjątku](#obsługa-konkretnego-wyjątku)
9. [Obsługa wielu wyjątków](#obsługa-wielu-wyjątków)
10. [Przechwytywanie obiektu wyjątku](#przechwytywanie-obiektu-wyjątku)
11. [Blok `else`](#blok-else)
12. [Blok `finally`](#blok-finally)
13. [Pełna konstrukcja `try except else finally`](#pełna-konstrukcja-try-except-else-finally)
14. [Podnoszenie wyjątków przez `raise`](#podnoszenie-wyjątków-przez-raise)
15. [Tworzenie własnych wyjątków](#tworzenie-własnych-wyjątków)
16. [Hierarchia wyjątków](#hierarchia-wyjątków)
17. [Wyjątki a funkcje](#wyjątki-a-funkcje)
18. [Wyjątki przy pracy z plikami](#wyjątki-przy-pracy-z-plikami)
19. [Wyjątki przy `input()` i konwersji typów](#wyjątki-przy-input-i-konwersji-typów)
20. [Kiedy używać `if`, a kiedy `try except`](#kiedy-używać-if-a-kiedy-try-except)
21. [Czego nie robić przy wyjątkach](#czego-nie-robić-przy-wyjątkach)
22. [Typowe błędy początkujących](#typowe-błędy-początkujących)
23. [Praktyczne przykłady](#praktyczne-przykłady)
24. [Dobre praktyki](#dobre-praktyki)
25. [Podsumowanie](#podsumowanie)
26. [Mini ściąga](#mini-ściąga)
27. [Ćwiczenia](#ćwiczenia)
28. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

W prawdziwych programach nie wszystko zawsze działa idealnie.

Użytkownik może:

- wpisać złą wartość,
- podać nieistniejący plik,
- spróbować dzielić przez zero,
- wykonać operację na złym typie danych.

Jeśli program nie jest na to przygotowany, po prostu się zatrzyma i pokaże błąd.

Właśnie po to istnieje **obsługa wyjątków**.

---

## Czym są wyjątki

Wyjątek to informacja o tym, że podczas działania programu wydarzył się błąd.

```python
print(10 / 0)
```

Ten kod spowoduje:

```python
ZeroDivisionError
```

Przykładowy efekt:

```python
ZeroDivisionError: division by zero
```

Wyjątek pojawia się **w czasie działania programu**, a nie na etapie pisania składni.

---

## Po co w ogóle obsługiwać wyjątki

Bez obsługi wyjątków program w razie błędu zwykle kończy działanie.

```python
liczba = int(input("Podaj liczbe: "))
print(liczba * 2)
```

Jeśli użytkownik wpisze `"abc"`, program się wywali.

Ale można zareagować kontrolowanie:

```python
try:
    liczba = int(input("Podaj liczbe: "))
    print(liczba * 2)
except ValueError:
    print("To nie byla poprawna liczba")
```

Jeśli użytkownik wpisze:

```python
abc
```

to output będzie:

```python
To nie byla poprawna liczba
```

---

## Błąd składni a wyjątek

### Błąd składni

Kod jest źle zapisany:

```python
# if 5 > 3
#     print("ok")
```

Python nie uruchomi programu.

### Wyjątek

Kod jest zapisany poprawnie, ale w czasie działania coś poszło źle:

```python
print(10 / 0)
```

---

## Jak wygląda wyjątek w Pythonie

Kiedy Python pokazuje wyjątek, zwykle widzisz:

- typ błędu,
- komunikat,
- miejsce, w którym problem się pojawił.

Przykład:

```python
liczby = [1, 2, 3]
print(liczby[10])
```

Pojawi się coś w stylu:

```python
IndexError: list index out of range
```

---

## Najczęstsze wyjątki

Na początku najczęściej spotkasz:

- `ZeroDivisionError`
- `ValueError`
- `TypeError`
- `NameError`
- `IndexError`
- `KeyError`
- `FileNotFoundError`
- `AttributeError`
- `ImportError`
- `ModuleNotFoundError`
- `UnboundLocalError`

Przykłady:

```python
# 10 / 0
# int("abc")
# "5" + 5
# print(nie_ma_mnie)
# [1, 2][5]
# {"a": 1}["b"]
```

---

## Blok `try except`

To podstawowa konstrukcja do obsługi wyjątków.

```python
try:
    kod_ryzykowny
except:
    reakcja_na_blad
```

Ale gołe `except:` zwykle nie jest dobrą praktyką. Lepiej łapać konkretny wyjątek.

---

## Obsługa konkretnego wyjątku

```python
try:
    liczba = int(input("Podaj liczbe: "))
except ValueError:
    print("To nie jest liczba")
```

Jeśli użytkownik wpisze:

```python
xyz
```

to output będzie:

```python
To nie jest liczba
```

To dużo lepsze niż łapanie wszystkiego, bo dokładnie wiadomo, na jaki problem reagujesz.

---

## Obsługa wielu wyjątków

Możesz obsługiwać kilka wyjątków osobno:

```python
try:
    a = int(input())
    b = int(input())
    print(a / b)
except ValueError:
    print("To nie byla liczba")
except ZeroDivisionError:
    print("Nie dziel przez zero")
```

Jeśli użytkownik wpisze:

```python
10
0
```

to output będzie:

```python
Nie dziel przez zero
```

Możesz też złapać kilka typów razem:

```python
except (ValueError, TypeError):
    print("Bledne dane")
```

---

## Przechwytywanie obiektu wyjątku

Możesz dostać sam obiekt błędu:

```python
try:
    int("abc")
except ValueError as e:
    print(e)
```

Output:

```python
invalid literal for int() with base 10: 'abc'
```

To przydatne, gdy chcesz zobaczyć dokładniejszy komunikat.

---

## Blok `else`

`else` wykona się tylko wtedy, gdy w `try` nie było wyjątku.

```python
try:
    liczba = int(input())
except ValueError:
    print("Bledna liczba")
else:
    print("OK:", liczba)
```

Jeśli użytkownik wpisze:

```python
7
```

to output będzie:

```python
OK: 7
```

To pomaga rozdzielać logikę sukcesu od logiki błędu.

---

## Blok `finally`

`finally` wykona się zawsze, niezależnie od tego, czy był wyjątek.

```python
try:
    print("proba")
finally:
    print("to wykona sie zawsze")
```

Output:

```python
proba
to wykona sie zawsze
```

Przydaje się do sprzątania zasobów.

---

## Pełna konstrukcja `try except else finally`

```python
try:
    liczba = int(input())
except ValueError:
    print("Bledne dane")
else:
    print("Sukces")
finally:
    print("Koniec")
```

Jeśli użytkownik wpisze:

```python
5
```

to output będzie:

```python
Sukces
Koniec
```

Nie zawsze potrzebujesz wszystkich części, ale dobrze rozumieć ich role.

---

## Podnoszenie wyjątków przez `raise`

Możesz sam zgłosić wyjątek:

```python
wiek = -5

if wiek < 0:
    raise ValueError("Wiek nie moze byc ujemny")
```

To przydatne, gdy chcesz wymusić poprawność danych.

---

## Tworzenie własnych wyjątków

Na tym etapie wystarczy wiedzieć, że można tworzyć własne klasy wyjątków:

```python
class MyError(Exception):
    pass
```

Na początku zwykle częściej będziesz korzystać z gotowych wyjątków wbudowanych.

---

## Hierarchia wyjątków

Wyjątki mają hierarchię klas.

To ważne dlatego, że:

- można łapać bardziej konkretne wyjątki,
- można też łapać szersze kategorie.

Na początku najważniejsza praktyczna lekcja brzmi:

- łap jak najbardziej konkretny wyjątek,
- nie zaczynaj od zbyt szerokiego `except Exception`.

---

## Wyjątki a funkcje

Funkcja może:

- sama obsłużyć wyjątek,
- zwrócić `None`,
- przepuścić wyjątek wyżej.

Przykład:

```python
def parse_int(tekst):
    try:
        return int(tekst)
    except ValueError:
        return None
```

To bardzo typowy wzorzec.

---

## Wyjątki przy pracy z plikami

```python
try:
    with open("brak.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("Nie ma takiego pliku")
```

Jeśli plik nie istnieje, output będzie:

```python
Nie ma takiego pliku
```

To jeden z najczęstszych praktycznych przykładów poza `input()`.

---

## Wyjątki przy `input()` i konwersji typów

To chyba najczęstszy pierwszy kontakt z wyjątkami:

```python
try:
    liczba = int(input("Podaj liczbe: "))
except ValueError:
    print("To nie byla liczba")
```

Jeśli użytkownik wpisze:

```python
abc
```

to output będzie:

```python
To nie byla liczba
```

Tu od razu widać sens obsługi błędnych danych użytkownika.

---

## Kiedy używać `if`, a kiedy `try except`

To bardzo ważne pytanie.

`if`:

- gdy łatwo możesz sprawdzić warunek z góry.

`try except`:

- gdy operacja sama może się nie udać i to ona najlepiej "wie", czy wystąpił błąd.

Przykład:

```python
if b != 0:
    print(a / b)
```

vs

```python
try:
    print(a / b)
except ZeroDivisionError:
    print("Zero")
```

Oba podejścia mogą mieć sens zależnie od kontekstu.

---

## Czego nie robić przy wyjątkach

- nie używaj gołego `except:` bez potrzeby,
- nie ukrywaj błędów bez komunikatu,
- nie łap wyjątków, których nie rozumiesz,
- nie używaj wyjątków do zwykłego sterowania programem tam, gdzie prosty `if` byłby czytelniejszy.

Zły przykład:

```python
try:
    cos()
except:
    pass
```

To chowa problem i utrudnia debugowanie.

---

## Typowe błędy początkujących

- łapanie wszystkich wyjątków naraz,
- brak rozróżnienia między różnymi typami błędów,
- mylenie `print()` błędu z jego obsługą,
- brak zwracania sensownej wartości z funkcji po błędzie,
- używanie `except:` bez świadomości konsekwencji.

---

## Praktyczne przykłady

### Bezpieczne dzielenie

```python
def bezpieczne_dzielenie(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
```

Przykład:

```python
print(bezpieczne_dzielenie(10, 2))
print(bezpieczne_dzielenie(10, 0))
```

Output:

```python
5.0
None
```

### Wielokrotna próba wpisania liczby

```python
while True:
    try:
        liczba = int(input("Podaj liczbe: "))
        print("OK")
        break
    except ValueError:
        print("Sprobuj jeszcze raz")
```

### Plik

```python
try:
    with open("dane.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("Brak pliku")
```

---

## Dobre praktyki

- łap konkretne wyjątki,
- pisz czytelne komunikaty błędów,
- używaj `else`, gdy poprawia czytelność,
- używaj `finally`, gdy trzeba coś posprzątać,
- nie ukrywaj błędów bez potrzeby,
- projektuj funkcje tak, żeby było jasne, co zwracają po błędzie.

---

## Podsumowanie

Obsługa wyjątków pozwala pisać programy, które nie rozpadają się przy pierwszym błędzie.

Najważniejsze rzeczy do opanowania:

- `try`, `except`, `else`, `finally`,
- różne typy wyjątków,
- `raise`,
- różnica między sprawdzaniem warunku a przechwytywaniem błędu.

---

## Mini ściąga

```python
try:
    x = int(input())
except ValueError:
    print("Bledna liczba")
else:
    print("OK")
finally:
    print("Koniec")
```

---

## Ćwiczenia

1. Obsłuż `ValueError` przy `int(input())`.
2. Obsłuż `ZeroDivisionError` przy dzieleniu.
3. Napisz `parse_int()`, które zwraca `None` przy błędzie.
4. Użyj `raise` dla błędnego wieku.
5. Napisz pętlę pytającą o liczbę aż do skutku.

---

## Przykładowe rozwiązania

### 1. `ValueError`

```python
try:
    x = int(input())
except ValueError:
    print("To nie liczba")
```

### 2. `ZeroDivisionError`

```python
try:
    print(a / b)
except ZeroDivisionError:
    print("Zero")
```

### 3. `parse_int`

```python
def parse_int(tekst):
    try:
        return int(tekst)
    except ValueError:
        return None
```

### 4. `raise`

```python
if wiek < 0:
    raise ValueError("Zly wiek")
```

### 5. Pętla

```python
while True:
    try:
        x = int(input())
        break
    except ValueError:
        print("Sprobuj jeszcze raz")
```

---

## Antywzorce i pułapki z życia

### Antywzorzec 1: gołe `except`

```python
try:
    cos()
except:
    print("Blad")
```

To zwykle zły pomysł, bo łapiesz zbyt szeroko i tracisz informację, co naprawdę się wydarzyło.

### Antywzorzec 2: chowanie błędów przez `pass`

```python
try:
    int("abc")
except ValueError:
    pass
```

Program dalej działa, ale błąd został ukryty. To utrudnia debugowanie i może prowadzić do jeszcze większych problemów później.

### Antywzorzec 3: używanie wyjątków tam, gdzie prosty `if` jest czytelniejszy

```python
try:
    if b == 0:
        raise ZeroDivisionError
    print(a / b)
except ZeroDivisionError:
    print("Zero")
```

Tu prostszy byłby zwykły warunek `if b == 0`.

---

## Mini case study

Załóżmy, że budujesz konsolowy formularz wieku użytkownika.

Chcesz:

- pobrać wiek,
- upewnić się, że to liczba,
- upewnić się, że nie jest ujemna.

To oznacza dwa różne typy problemów:

- zły format danych, np. `"abc"` -> `ValueError`,
- zła wartość logiczna, np. `-5` -> Twój własny warunek i ewentualnie `raise ValueError`.

Przykład:

```python
while True:
    try:
        wiek = int(input("Wiek: "))
        if wiek < 0:
            raise ValueError("Wiek nie moze byc ujemny")
        break
    except ValueError as e:
        print(e)
```

To bardzo dobry przykład pokazujący, że wyjątki i zwykła walidacja często współpracują ze sobą.

---

## Mini projekt po rozdziale

Zbuduj plik `safe_input_app.py`, który:

- pyta użytkownika o imię, wiek i dwie liczby,
- obsługuje błędy konwersji,
- bezpiecznie dzieli liczby,
- przy błędach nie wywala programu, tylko prosi o poprawę danych,
- na końcu wypisuje podsumowanie.

To zadanie scala:

- `try/except`,
- `raise`,
- pętle,
- walidację,
- odpowiedzialne komunikaty błędów.
