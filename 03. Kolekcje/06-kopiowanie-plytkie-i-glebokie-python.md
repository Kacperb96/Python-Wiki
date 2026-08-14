# Kopiowanie Płytkie i Głębokie w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Dlaczego kopiowanie jest ważne](#dlaczego-kopiowanie-jest-ważne)
3. [Przypisanie to nie kopiowanie](#przypisanie-to-nie-kopiowanie)
4. [Obiekty i referencje](#obiekty-i-referencje)
5. [Kopia płytka](#kopia-płytka)
6. [Kopia głęboka](#kopia-głęboka)
7. [`copy.copy()`](#copycopy)
8. [`copy.deepcopy()`](#copydeepcopy)
9. [Kopie list](#kopie-list)
10. [Kopie słowników](#kopie-słowników)
11. [Kopie zbiorów](#kopie-zbiorów)
12. [Struktury zagnieżdżone](#struktury-zagnieżdżone)
13. [Kiedy płytka kopia wystarcza](#kiedy-płytka-kopia-wystarcza)
14. [Kiedy potrzebna jest głęboka kopia](#kiedy-potrzebna-jest-głęboka-kopia)
15. [Pułapki przy kopiowaniu](#pułapki-przy-kopiowaniu)
16. [Kopiowanie a wydajność](#kopiowanie-a-wydajność)
17. [Typowe błędy początkujących](#typowe-błędy-początkujących)
18. [Praktyczne przykłady](#praktyczne-przykłady)
19. [Dobre praktyki](#dobre-praktyki)
20. [Podsumowanie](#podsumowanie)
21. [Mini ściąga](#mini-ściąga)
22. [Ćwiczenia](#ćwiczenia)
23. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Temat kopiowania w Pythonie jest bardzo ważny, bo łatwo popełnić błąd:

- myśleć, że masz kopię danych,
- a w rzeczywistości mieć tylko drugą nazwę tego samego obiektu.

To szczególnie ważne przy:

- listach,
- słownikach,
- zbiorach,
- strukturach zagnieżdżonych.

W tym poradniku omówimy:

- czym różni się przypisanie od kopiowania,
- czym jest kopia płytka,
- czym jest kopia głęboka,
- jak działają `copy.copy()` i `copy.deepcopy()`.

---

## Dlaczego kopiowanie jest ważne

Jeśli nie rozumiesz kopiowania, możesz przypadkiem:

- zmienić oryginalne dane, myśląc że modyfikujesz kopię,
- zepsuć dane wejściowe do funkcji,
- wprowadzić trudne do znalezienia błędy.

To jeden z tematów, który robi ogromną różnicę między "kod działa" a "kod jest przewidywalny".

---

## Przypisanie to nie kopiowanie

To absolutna podstawa.

Przykład:

```python
a = [1, 2, 3]
b = a

b.append(4)

print(a)
print(b)
```

Wynik:

```python
[1, 2, 3, 4]
[1, 2, 3, 4]
```

### Dlaczego tak się stało

Bo:

```python
b = a
```

nie tworzy kopii.
Tworzy tylko drugą nazwę wskazującą na ten sam obiekt.

---

## Obiekty i referencje

W Pythonie zmienne to nazwy wskazujące na obiekty.

Jeśli zrobisz:

```python
a = [1, 2, 3]
b = a
```

to:

- `a` wskazuje na listę,
- `b` też wskazuje na tę samą listę.

Dlatego zmiana przez `b` jest widoczna przez `a`.

---

## Kopia płytka

Kopia płytka tworzy nowy obiekt zewnętrzny, ale jego elementy wewnętrzne nadal mogą wskazywać na te same obiekty co oryginał.

Najprościej:

- zewnętrzna struktura jest nowa,
- wnętrze może być współdzielone.

Przykład:

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)
```

`b` to nowa lista, ale wewnętrzne listy są wspólne.

---

## Kopia głęboka

Kopia głęboka tworzy nowy obiekt i rekurencyjnie kopiuje też zagnieżdżone obiekty.

Najprościej:

- nowa jest struktura zewnętrzna,
- nowe są też obiekty w środku.

Przykład:

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
```

Teraz zmiana wnętrza `b` nie wpływa na `a`.

---

## `copy.copy()`

Służy do płytkiej kopii.

```python
import copy

a = [1, 2, 3]
b = copy.copy(a)
```

Przy prostej liście działa tak, jak zwykle chcesz:

```python
b.append(4)
print(a)
print(b)
```

Wynik:

```python
[1, 2, 3]
[1, 2, 3, 4]
```

Ale przy strukturach zagnieżdżonych trzeba uważać.

---

## `copy.deepcopy()`

Służy do głębokiej kopii.

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
```

Potem:

```python
b[0].append(99)
print(a)
print(b)
```

Wynik:

```python
[[1, 2], [3, 4]]
[[1, 2, 99], [3, 4]]
```

Oryginał nie został zmieniony.

---

## Kopie list

### Prosta lista

```python
a = [1, 2, 3]
b = a.copy()
```

albo:

```python
b = a[:]
```

albo:

```python
b = list(a)
```

### Lista zagnieżdżona

```python
a = [[1, 2], [3, 4]]
b = a.copy()

b[0].append(99)
print(a)
```

To zmieni też `a`, bo kopia była płytka.

---

## Kopie słowników

### Płytka kopia

```python
a = {"x": 1, "y": 2}
b = a.copy()
```

### Problem przy zagnieżdżeniu

```python
a = {"dane": {"x": 1}}
b = a.copy()

b["dane"]["x"] = 99
print(a)
```

Oryginał też się zmieni.

### Głęboka kopia

```python
import copy

b = copy.deepcopy(a)
```

---

## Kopie zbiorów

Zwykły zbiór można kopiować przez:

```python
a = {1, 2, 3}
b = a.copy()
```

Ponieważ zwykły `set` nie zawiera mutowalnych list czy słowników jako elementów, temat jest zwykle prostszy niż przy listach i słownikach.

---

## Struktury zagnieżdżone

To najważniejsze miejsce, gdzie różnica między płytką a głęboką kopią staje się widoczna.

Przykład:

```python
a = {
    "uczen": {
        "imie": "Ania",
        "oceny": [5, 4, 3]
    }
}
```

Jeśli zrobisz:

```python
b = a.copy()
```

to zmiana:

```python
b["uczen"]["oceny"].append(6)
```

wpłynie też na `a`.

Tu właśnie potrzebujesz `deepcopy()`.

---

## Kiedy płytka kopia wystarcza

Płytka kopia jest dobra, gdy:

- struktura nie jest zagnieżdżona,
- elementy wewnętrzne są niemutowalne,
- świadomie wiesz, że współdzielenie wnętrza nie przeszkadza.

Przykład:

```python
a = [1, 2, 3]
b = a.copy()
```

To najczęściej w zupełności wystarczy.

---

## Kiedy potrzebna jest głęboka kopia

Użyj `deepcopy()`, gdy:

- masz listy list,
- słowniki zawierają listy lub inne słowniki,
- dane są zagnieżdżone,
- chcesz pełnej niezależności kopii od oryginału.

---

## Pułapki przy kopiowaniu

### 1. `a = b` to nie kopia

To tylko drugie odniesienie do tego samego obiektu.

### 2. `.copy()` nie zawsze wystarcza

Przy strukturach zagnieżdżonych robi tylko kopię płytką.

### 3. `[:]` też jest płytkie

Nie rozwiązuje problemu zagnieżdżeń.

### 4. `deepcopy()` jest bezpieczniejsze, ale cięższe

Może być wolniejsze i bardziej kosztowne pamięciowo.

---

## Kopiowanie a wydajność

To ważne w praktyce.

### Płytka kopia

- zwykle szybsza,
- zwykle lżejsza,
- dobra dla prostych struktur.

### Głęboka kopia

- wolniejsza,
- bardziej kosztowna,
- ale daje pełną niezależność.

Nie zawsze trzeba robić `deepcopy()`.
Warto używać jej wtedy, gdy naprawdę jest potrzebna.

---

## Typowe błędy początkujących

### 1. Zakładanie, że przypisanie tworzy kopię

To najczęstszy błąd.

### 2. Używanie `.copy()` przy zagnieżdżonych strukturach i oczekiwanie pełnej niezależności

To nie zadziała tak, jak się wielu osobom wydaje.

### 3. Nadużywanie `deepcopy()`

Nie zawsze jest potrzebna.

### 4. Brak testu po kopiowaniu

Warto sprawdzić, czy zmiana kopii rzeczywiście nie wpływa na oryginał.

---

## Praktyczne przykłady

### Przypisanie

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```

### Płytka kopia listy

```python
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)
print(b)
```

### Płytka kopia listy zagnieżdżonej

```python
a = [[1, 2], [3, 4]]
b = a.copy()
b[0].append(99)
print(a)
print(b)
```

### Głęboka kopia

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0].append(99)
print(a)
print(b)
```

### Słownik zagnieżdżony

```python
import copy

a = {"dane": {"x": 1}}
b = copy.deepcopy(a)
b["dane"]["x"] = 99
print(a)
print(b)
```

---

## Dobre praktyki

### Zawsze rozróżniaj przypisanie od kopiowania

To podstawa.

### Dla prostych struktur używaj płytkiej kopii

Jest prostsza i lżejsza.

### Dla struktur zagnieżdżonych rozważ `deepcopy()`

Zwłaszcza gdy dane mają być w pełni niezależne.

### Testuj zachowanie po zmianie kopii

To najszybszy sposób sprawdzenia, czy wybrałeś właściwy rodzaj kopii.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- przypisanie to nie kopiowanie,
- kopia płytka tworzy nową strukturę zewnętrzną, ale wnętrze może być wspólne,
- kopia głęboka kopiuje także zagnieżdżone obiekty,
- `copy.copy()` robi płytką kopię,
- `copy.deepcopy()` robi głęboką kopię,
- przy prostych strukturach płytka kopia zwykle wystarcza,
- przy zagnieżdżonych danych często potrzebna jest kopia głęboka.

Jeśli dobrze opanujesz ten temat, unikniesz bardzo wielu trudnych i mylących błędów.

---

## Mini ściąga

### Przypisanie

```python
b = a
```

### Płytka kopia

```python
import copy
b = copy.copy(a)
```

### Głęboka kopia

```python
import copy
b = copy.deepcopy(a)
```

### Krótsze kopie listy

```python
b = a.copy()
b = a[:]
b = list(a)
```

---

## Ćwiczenia

### Ćwiczenie 1

Sprawdź, co się stanie po:

```python
a = [1, 2, 3]
b = a
```

i modyfikacji `b`.

### Ćwiczenie 2

Zrób płytką kopię listy i sprawdź, czy zmiana kopii wpływa na oryginał.

### Ćwiczenie 3

Powtórz to samo dla listy zagnieżdżonej.

### Ćwiczenie 4

Użyj `copy.deepcopy()` na liście zagnieżdżonej i porównaj wynik.

### Ćwiczenie 5

Zrób przykład ze słownikiem zawierającym listę.

---

## Przykładowe rozwiązania

### Ćwiczenie 1

```python
a = [1, 2, 3]
b = a
b.append(4)

print(a)
print(b)
```

### Ćwiczenie 2

```python
a = [1, 2, 3]
b = a.copy()
b.append(4)

print(a)
print(b)
```

### Ćwiczenie 3

```python
a = [[1, 2], [3, 4]]
b = a.copy()
b[0].append(99)

print(a)
print(b)
```

### Ćwiczenie 4

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0].append(99)

print(a)
print(b)
```

### Ćwiczenie 5

```python
import copy

a = {"oceny": [5, 4, 3]}
b = copy.deepcopy(a)
b["oceny"].append(6)

print(a)
print(b)
```

---

## Na koniec

Najlepiej uczyć się kopiowania przez małe eksperymenty.

Warto:

1. stworzyć prostą listę,
2. przypisać ją do drugiej zmiennej,
3. zrobić płytką kopię,
4. zrobić głęboką kopię,
5. porównać zachowanie przy zmianach.

Właśnie wtedy różnica staje się naprawdę intuicyjna.
