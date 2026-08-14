# Closures w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest closure](#czym-jest-closure)
3. [Funkcja wewnętrzna](#funkcja-wewnętrzna)
4. [Pamiętanie zmiennych zewnętrznych](#pamiętanie-zmiennych-zewnętrznych)
5. [Najprostszy przykład closure](#najprostszy-przykład-closure)
6. [Po co closures są potrzebne](#po-co-closures-są-potrzebne)
7. [Closures a dekoratory](#closures-a-dekoratory)
8. [Closures a funkcje fabrykujące](#closures-a-funkcje-fabrykujące)
9. [Closures a `nonlocal`](#closures-a-nonlocal)
10. [Typowe błędy początkujących](#typowe-błędy-początkujących)
11. [Praktyczne przykłady](#praktyczne-przykłady)
12. [Dobre praktyki](#dobre-praktyki)
13. [Podsumowanie](#podsumowanie)
14. [Mini ściąga](#mini-ściąga)
15. [Ćwiczenia](#ćwiczenia)
16. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Closure to bardzo ważny mechanizm w Pythonie.

To właśnie on sprawia, że:

- funkcja może pamiętać dane zewnętrzne,
- da się budować dekoratory,
- da się tworzyć funkcje „konfigurowane” innymi funkcjami.

Na początku temat może wydawać się dziwny, ale sama idea jest prosta.

---

## Czym jest closure

Closure to funkcja wewnętrzna, która:

- została zwrócona albo używana poza miejscem definicji,
- nadal pamięta zmienne z funkcji zewnętrznej.

---

## Funkcja wewnętrzna

Przykład:

```python
def zewnetrzna():
    def wewnetrzna():
        print("Hello")
    return wewnetrzna
```

Tu `wewnetrzna` jest funkcją wewnętrzną.

---

## Pamiętanie zmiennych zewnętrznych

Najważniejsza część:

```python
def zewnetrzna():
    tekst = "Python"

    def wewnetrzna():
        print(tekst)

    return wewnetrzna
```

Mimo że `zewnetrzna()` się skończy, funkcja zwrócona nadal „pamięta” `tekst`.

---

## Najprostszy przykład closure

```python
def mnoznik(n):
    def pomnoz(x):
        return x * n
    return pomnoz

razy2 = mnoznik(2)
razy3 = mnoznik(3)

print(razy2(5))
print(razy3(5))
```

Tutaj:

- `razy2` pamięta `n = 2`,
- `razy3` pamięta `n = 3`.

---

## Po co closures są potrzebne

Najczęściej do:

- dekoratorów,
- funkcji konfigurowanych,
- trzymania stanu bez klasy,
- budowania małych, eleganckich mechanizmów.

---

## Closures a dekoratory

Dekorator bardzo często działa właśnie dzięki closure:

- wrapper jest funkcją wewnętrzną,
- pamięta dekorowaną funkcję,
- może ją później wywołać.

---

## Closures a funkcje fabrykujące

To bardzo dobre zastosowanie.

Przykład:

```python
def przywitanie(prefix):
    def wewnetrzna(imie):
        print(prefix, imie)
    return wewnetrzna
```

Możesz zrobić:

```python
czesc = przywitanie("Czesc")
dzien_dobry = przywitanie("Dzien dobry")
```

---

## Closures a `nonlocal`

Jeśli chcesz zmieniać zmienną z funkcji zewnętrznej, używasz `nonlocal`.

Przykład:

```python
def licznik():
    x = 0

    def zwieksz():
        nonlocal x
        x += 1
        return x

    return zwieksz
```

To bardzo klasyczny przykład.

---

## Typowe błędy początkujących

- mylenie closure z samą funkcją zagnieżdżoną,
- brak zrozumienia, że funkcja pamięta zmienne,
- brak `nonlocal`, gdy chcesz zmieniać stan,
- zbyt szybkie przechodzenie do trudnych przykładów.

---

## Praktyczne przykłady

```python
def dodajnik(n):
    def dodaj(x):
        return x + n
    return dodaj

plus5 = dodajnik(5)
print(plus5(10))
```

```python
def licznik():
    x = 0

    def krok():
        nonlocal x
        x += 1
        return x

    return krok
```

---

## Dobre praktyki

- zaczynaj od prostych przykładów,
- traktuj closure jako „funkcję z pamięcią”,
- używaj `nonlocal` świadomie,
- nie komplikuj tam, gdzie klasa byłaby czytelniejsza.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- closure to funkcja, która pamięta zmienne z zewnętrznego zakresu,
- bardzo często występuje w dekoratorach,
- pozwala budować funkcje konfigurowane i funkcje ze stanem.

---

## Mini ściąga

```python
def outer(x):
    def inner(y):
        return x + y
    return inner
```

---

## Ćwiczenia

### Ćwiczenie 1

Napisz funkcję tworzącą mnożnik.

### Ćwiczenie 2

Napisz closure, które liczy kolejne wywołania.

---

## Przykładowe rozwiązania

```python
def mnoznik(n):
    def f(x):
        return x * n
    return f
```
