# Dekoratory w Pythonie — od prostych po zaawansowane

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym są dekoratory](#czym-są-dekoratory)
3. [Po co używa się dekoratorów](#po-co-używa-się-dekoratorów)
4. [Skąd bierze się ten mechanizm](#skąd-bierze-się-ten-mechanizm)
5. [Funkcje jako obiekty](#funkcje-jako-obiekty)
6. [Closures](#closures)
7. [Najprostszy dekorator](#najprostszy-dekorator)
8. [Składnia `@`](#składnia-)
9. [Dekoratory z argumentami](#dekoratory-z-argumentami)
10. [Dekoratory klasowe](#dekoratory-klasowe)
11. [`functools.wraps`](#functoolswraps)
12. [Wbudowane dekoratory](#wbudowane-dekoratory)
13. [Dekoratory we frameworkach](#dekoratory-we-frameworkach)
14. [Kiedy dekoratory mają sens](#kiedy-dekoratory-mają-sens)
15. [Kiedy dekorator to przesada](#kiedy-dekorator-to-przesada)
16. [Typowe błędy początkujących](#typowe-błędy-początkujących)
17. [Dobre praktyki](#dobre-praktyki)
18. [Podsumowanie](#podsumowanie)

---

## Wprowadzenie

Dekoratory to jeden z najbardziej charakterystycznych mechanizmów Pythona.

Pozwalają:

- modyfikować zachowanie funkcji,
- dodawać logowanie,
- kontrolować dostęp,
- mierzyć czas działania,
- cache’ować wyniki,
- rejestrować endpointy i testy,

bez zmieniania samego kodu funkcji w środku.

To bardzo potężne narzędzie, ale początkującym często wydaje się magiczne.

W praktyce dekoratory są zbudowane z kilku prostych pomysłów:

- funkcje są obiektami,
- funkcja może zwracać funkcję,
- funkcja wewnętrzna może pamiętać kontekst zewnętrzny.

---

## Czym są dekoratory

Najprościej:

**dekorator to coś, co bierze funkcję i zwraca nową funkcję o rozszerzonym zachowaniu.**

Przykład idei:

```python
def dekorator(f):
    def wrapper():
        print("Przed")
        f()
        print("Po")
    return wrapper
```

Jeśli udekorujesz funkcję, dostaniesz nową wersję tej funkcji.

---

## Po co używa się dekoratorów

Dekoratory są przydatne wtedy, gdy chcesz powtarzalnie dodać jakieś zachowanie do wielu funkcji.

Na przykład:

- logowanie wywołań,
- sprawdzanie uprawnień,
- walidację argumentów,
- mierzenie czasu,
- cache,
- rejestrację funkcji.

To pozwala oddzielić:

- główną logikę funkcji,
- dodatkowe zachowanie techniczne.

---

## Skąd bierze się ten mechanizm

Cały temat dekoratorów opiera się na trzech fundamentach:

1. funkcje są obiektami,
2. funkcje mogą być przekazywane jako argumenty,
3. funkcje mogą zwracać inne funkcje.

Do tego dochodzą closures i składnia `@`.

---

## Funkcje jako obiekty

W Pythonie funkcja jest obiektem.

To znaczy, że można:

- przypisać ją do zmiennej,
- przekazać ją jako argument,
- zwrócić ją z innej funkcji.

Przykład:

```python
def przywitaj():
    print("Czesc")

f = przywitaj
f()
```

To bardzo ważny fundament dekoratorów.

---

## Closures

Closure to funkcja wewnętrzna, która pamięta zmienne z funkcji zewnętrznej.

Przykład:

```python
def zewnetrzna():
    tekst = "Python"

    def wewnetrzna():
        print(tekst)

    return wewnetrzna
```

To właśnie closure pozwala dekoratorowi „owinąć” funkcję i nadal mieć do niej dostęp.

---

## Najprostszy dekorator

```python
def dekorator(f):
    def wrapper():
        print("Start")
        f()
        print("Koniec")
    return wrapper
```

Można użyć tak:

```python
def hello():
    print("Hello")

hello = dekorator(hello)
hello()
```

---

## Składnia `@`

To tylko wygodniejszy zapis.

Zamiast:

```python
hello = dekorator(hello)
```

piszesz:

```python
@dekorator
def hello():
    print("Hello")
```

To robi dokładnie to samo.

---

## Dekoratory z argumentami

Czasem dekorator sam ma przyjmować dodatkowe ustawienia.

Na przykład:

```python
@powtorz(3)
def hello():
    print("Hello")
```

Wtedy potrzebujesz dodatkowego poziomu funkcji:

- funkcja przyjmuje argument dekoratora,
- zwraca właściwy dekorator,
- dekorator zwraca wrapper.

---

## Dekoratory klasowe

Dekoratorem nie musi być tylko funkcja.

Może być też obiekt klasy implementujący `__call__`.

To przydaje się, gdy dekorator ma mieć własny stan i bardziej rozbudowaną logikę.

---

## `functools.wraps`

Bez `wraps` dekorator psuje część metadanych funkcji:

- nazwę,
- docstring,
- informacje introspekcyjne.

Dlatego bardzo często poprawny dekorator wygląda tak:

```python
from functools import wraps

def dekorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper
```

---

## Wbudowane dekoratory

Najważniejsze przykłady:

- `@property`
- `@staticmethod`
- `@classmethod`
- `@functools.lru_cache`

To dekoratory, z którymi spotkasz się bardzo często.

---

## Dekoratory we frameworkach

W frameworkach dekoratory są wszędzie.

Przykłady:

- FastAPI: endpointy,
- Flask: routing,
- pytest: markery, fixture’y.

Tam dekorator często nie tylko „owija funkcję”, ale też ją rejestruje albo opisuje dla frameworka.

---

## Kiedy dekoratory mają sens

Gdy:

- chcesz dodać wspólne zachowanie do wielu funkcji,
- chcesz oddzielić logikę biznesową od technicznej,
- chcesz mieć elegancki i wielokrotnego użytku mechanizm.

---

## Kiedy dekorator to przesada

Gdy:

- logika jest jednorazowa,
- wrapper robi się bardzo złożony,
- czytelność spada,
- prostsza funkcja wyższego rzędu wystarczyłaby w zupełności.

---

## Typowe błędy początkujących

- brak zrozumienia, że dekorator zwraca funkcję,
- mylenie dekoratora z wynikiem działania funkcji,
- brak `*args, **kwargs`,
- brak `functools.wraps`,
- trudność z dekoratorami z argumentami.

---

## Dobre praktyki

- zaczynaj od bardzo prostych dekoratorów,
- używaj `@wraps`,
- nie komplikuj dekoratora bez potrzeby,
- testuj dekoratory osobno,
- rozdzielaj dekoratory o różnych odpowiedzialnościach.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- dekorator bierze funkcję i zwraca nową funkcję,
- działa dzięki temu, że funkcje są obiektami,
- closures i wrapper są sercem dekoratorów,
- składnia `@` to tylko skrót,
- `functools.wraps` to bardzo ważna dobra praktyka,
- dekoratory są bardzo często używane także w frameworkach.
