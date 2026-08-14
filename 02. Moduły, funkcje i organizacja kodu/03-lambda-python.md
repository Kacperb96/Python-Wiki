# `lambda` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `lambda`](#czym-jest-lambda)
3. [Po co istnieje `lambda`](#po-co-istnieje-lambda)
4. [Składnia](#składnia)
5. [Najczęstsze zastosowania](#najczęstsze-zastosowania)
6. [`lambda` w `sorted()`](#lambda-w-sorted)
7. [`lambda` w `map()` i `filter()`](#lambda-w-map-i-filter)
8. [Kiedy `lambda` ma sens](#kiedy-lambda-ma-sens)
9. [Kiedy zwykłe `def` jest lepsze](#kiedy-zwykłe-def-jest-lepsze)
10. [Czy `lambda` jest bardziej profesjonalna](#czy-lambda-jest-bardziej-profesjonalna)
11. [Typowe pułapki początkujących](#typowe-pułapki-początkujących)
12. [Praktyczne przykłady](#praktyczne-przykłady)
13. [Dobre praktyki](#dobre-praktyki)
14. [Podsumowanie](#podsumowanie)
15. [Mini ściąga](#mini-ściąga)
16. [Ćwiczenia](#ćwiczenia)
17. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`lambda` to mała anonimowa funkcja zapisywana w jednej linii.

Jest przydatna, ale łatwa do nadużycia.

Na początku warto zrozumieć nie tylko jak jej używać, ale też kiedy jej nie używać.

To ważne, bo wielu początkujących zaczyna traktować `lambda` jako coś bardziej zaawansowanego i przez to lepszego. W praktyce bardzo często zwykłe `def` jest czytelniejsze.

---

## Czym jest `lambda`

Przykład:

```python
lambda x: x * 2
```

To funkcja bez nazwy.

Odpowiednik:

```python
def podwoj(x):
    return x * 2
```

Najważniejsza różnica nie polega na tym, co ta funkcja robi, tylko jak ją zapisujesz i w jakim kontekście używasz.

---

## Po co istnieje `lambda`

Po to, żeby szybko przekazać bardzo małą funkcję tam, gdzie potrzebujesz jej tylko lokalnie.

Najczęściej:

- `key=` w sortowaniu,
- proste `map()`,
- proste `filter()`,
- małe callbacki.

To nie jest narzędzie do budowania dużej logiki biznesowej.

---

## Składnia

```python
lambda argumenty: wyrazenie
```

Ważne:

- `lambda` zawiera jedno wyrażenie,
- nie nadaje się do długiej logiki,
- nie zastępuje normalnego projektowania funkcji.

Nie napiszesz sensownie w `lambda`:

- wielu instrukcji,
- kilku kroków po kolei,
- czytelnych warunków wielolinijkowych.

---

## Najczęstsze zastosowania

### Sortowanie

```python
dane = [("Anna", 30), ("Jan", 25)]
print(sorted(dane, key=lambda x: x[1]))
```

Output:

```python
[('Jan', 25), ('Anna', 30)]
```

### `map()`

```python
liczby = [1, 2, 3]
print(list(map(lambda x: x * x, liczby)))
```

Output:

```python
[1, 4, 9]
```

### `filter()`

```python
liczby = [1, 2, 3, 4]
print(list(filter(lambda x: x % 2 == 0, liczby)))
```

Output:

```python
[2, 4]
```

---

## `lambda` w `sorted()`

To chyba najczęstszy i najbardziej naturalny przypadek użycia.

```python
osoby = [("Anna", 30), ("Jan", 25), ("Ola", 28)]
wynik = sorted(osoby, key=lambda osoba: osoba[1])
print(wynik)
```

Output:

```python
[('Jan', 25), ('Ola', 28), ('Anna', 30)]
```

Tutaj `lambda osoba: osoba[1]` mówi:

"do sortowania użyj drugiego elementu każdej krotki".

To jest krótkie, lokalne i czytelne. Właśnie w takich miejscach `lambda` ma najwięcej sensu.

---

## `lambda` w `map()` i `filter()`

`map()`:

```python
liczby = [1, 2, 3, 4]
kwadraty = list(map(lambda x: x ** 2, liczby))
print(kwadraty)
```

Output:

```python
[1, 4, 9, 16]
```

`filter()`:

```python
liczby = [1, 2, 3, 4]
parzyste = list(filter(lambda x: x % 2 == 0, liczby))
print(parzyste)
```

Na początku warto jednak wiedzieć, że w Pythonie często czytelniejsze od `map()` i `filter()` bywają:

- zwykłe pętle,
- list comprehensions.

Np.:

```python
kwadraty = [x ** 2 for x in liczby]
```

bywa czytelniejsze niż `map(lambda ...)`.

---

## Kiedy `lambda` ma sens

Gdy funkcja jest:

- bardzo krótka,
- oczywista,
- używana tylko w jednym miejscu,
- czytelna od razu bez dodatkowych wyjaśnień.

To kluczowe: `lambda` ma skracać kod bez psucia zrozumiałości.

---

## Kiedy zwykłe `def` jest lepsze

Jeśli logika:

- jest dłuższa,
- ma nazwę, która poprawia czytelność,
- będzie używana wielokrotnie,
- wymaga komentarza,
- wymaga testów,

to zwykłe `def` jest lepszym wyborem.

Przykład:

```python
def czy_uzytkownik_aktywny_i_pelnoletni(user):
    return user["active"] and user["age"] >= 18
```

To jest czytelniejsze niż zbyt rozbudowana `lambda`.

---

## Czy `lambda` jest bardziej profesjonalna

Nie.

To ważna rzecz do odczarowania.

`lambda` nie jest:

- bardziej zaawansowana,
- bardziej zawodowa,
- bardziej elegancka z definicji.

Jest po prostu krótkim narzędziem do specyficznego zastosowania.

Profesjonalny kod to taki, który jest czytelny i przewidywalny. Czasem będzie tam `lambda`, a czasem zwykłe `def`.

---

## Typowe pułapki początkujących

- używanie `lambda` tam, gdzie zwykła funkcja byłaby dużo czytelniejsza,
- próba pisania zbyt dużej logiki w jednej linijce,
- traktowanie `lambda` jako bardziej profesjonalnego zamiennika `def`,
- wpychanie `lambda` do kodu tylko dlatego, że "krócej wygląda".

---

## Praktyczne przykłady

### Sortowanie po wieku

```python
osoby = [("Anna", 30), ("Jan", 25), ("Ola", 28)]
wynik = sorted(osoby, key=lambda osoba: osoba[1])
print(wynik)
```

### Kwadraty liczb

```python
liczby = [1, 2, 3, 4]
kwadraty = list(map(lambda x: x ** 2, liczby))
print(kwadraty)
```

### Filtrowanie dodatnich

```python
liczby = [-2, 0, 3, 5]
dodatnie = list(filter(lambda x: x > 0, liczby))
print(dodatnie)
```

Output:

```python
[3, 5]
```

### Przykład, gdzie `def` jest lepsze

```python
def policz_wynik_studenta(student):
    return student["egzamin"] * 0.7 + student["projekt"] * 0.3
```

Tu nazwa funkcji niesie informację. Sama `lambda` by to ukrywała.

---

## Dobre praktyki

- używaj `lambda` tylko do bardzo małych rzeczy,
- jeśli logika ma nazwę i znaczenie, zwykle wybierz `def`,
- nie staraj się być sprytniejszy niż czytelność kodu,
- jeśli `lambda` robi się trudna do przeczytania, to zwykle znak, że już nie jest dobrym wyborem.

---

## Podsumowanie

`lambda` jest narzędziem pomocniczym, a nie zamiennikiem dla normalnych funkcji.

Najlepiej sprawdza się tam, gdzie mała funkcja jest potrzebna tylko raz i od razu widać, co robi.

---

## Mini ściąga

```python
sorted(dane, key=lambda x: x[1])
list(map(lambda x: x * x, liczby))
list(filter(lambda x: x > 0, liczby))
```

---

## Ćwiczenia

1. Posortuj listę krotek po drugim elemencie przez `lambda`.
2. Zamień listę liczb na kwadraty przez `map()` i `lambda`.
3. Odfiltruj liczby dodatnie przez `filter()` i `lambda`.
4. Napisz przykład, gdzie `def` będzie czytelniejsze niż `lambda`.

---

## Przykładowe rozwiązania

### 1. Sortowanie

```python
dane = [("Anna", 30), ("Jan", 25)]
print(sorted(dane, key=lambda x: x[1]))
```

### 2. Kwadraty

```python
liczby = [1, 2, 3]
print(list(map(lambda x: x ** 2, liczby)))
```

### 3. Dodatnie

```python
liczby = [-2, 0, 5]
print(list(filter(lambda x: x > 0, liczby)))
```

### 4. Lepsze `def`

```python
def normalizuj_email(email):
    return email.strip().lower()
```

Tu zwykłe `def` jest lepsze, bo funkcja ma sensowną nazwę i może być używana wielokrotnie.
