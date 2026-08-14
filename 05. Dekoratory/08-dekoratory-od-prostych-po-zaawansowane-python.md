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

Przykład użycia:

```python
def hello():
    print("Hello")

hello = dekorator(hello)
hello()
```

Wynik:

```python
Przed
Hello
Po
```

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

Wynik:

```python
Czesc
```

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

Przykład użycia:

```python
f = zewnetrzna()
f()
```

Wynik:

```python
Python
```

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

Wynik:

```python
Start
Hello
Koniec
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

Czyli:

```python
@dekorator
```

to tylko krótszy zapis dla:

```python
hello = dekorator(hello)
```

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

To warto czytać tak:

1. konfiguracja,
2. dekorowanie funkcji,
3. wykonanie wrappera przy wywołaniu.

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

Przykład użycia:

```python
@dekorator
def hello():
    """Przykladowa funkcja."""
    print("Hello")

print(hello.__name__)
print(hello.__doc__)
```

Wynik:

```python
hello
Przykladowa funkcja.
```

---

## Wbudowane dekoratory

Najważniejsze przykłady:

- `@property`
- `@staticmethod`
- `@classmethod`
- `@functools.lru_cache`

To dekoratory, z którymi spotkasz się bardzo często.

Najczęściej:

- `@property` zmienia metodę w kontrolowany atrybut,
- `@staticmethod` daje metodę bez `self`,
- `@classmethod` daje metodę pracującą na klasie,
- `@lru_cache` zapamiętuje wyniki funkcji.

---

## Dekoratory we frameworkach

W frameworkach dekoratory są wszędzie.

Przykłady:

- FastAPI: endpointy,
- Flask: routing,
- pytest: markery, fixture’y.

Tam dekorator często nie tylko „owija funkcję”, ale też ją rejestruje albo opisuje dla frameworka.

To ogromnie ważna różnica:

własny dekorator często zmienia wykonanie funkcji,

a frameworkowy dekorator bardzo często dodatkowo zapisuje ją w jakimś systemie.

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

### 6. Brak zrozumienia kolejności wielu dekoratorów

Przy kilku dekoratorach łatwo zgubić, który działa pierwszy przy dekorowaniu, a który przy wywołaniu.

### 7. Próba uczenia się dekoratorów bez zrozumienia funkcji jako obiektów

Wtedy cały temat wygląda jak zbiór sztuczek, a nie logiczny mechanizm.

---

## Praktyczne przykłady

### Logowanie wywołania

```python
from functools import wraps

def loguj(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print("Wywolanie:", f.__name__)
        return f(*args, **kwargs)
    return wrapper

@loguj
def dodaj(a, b):
    return a + b

print(dodaj(2, 3))
```

Wynik:

```python
Wywolanie: dodaj
5
```

### Powtarzanie funkcji

```python
def powtorz(n):
    def dekorator(f):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                f(*args, **kwargs)
        return wrapper
    return dekorator

@powtorz(3)
def hello():
    print("Hello")

hello()
```

Wynik:

```python
Hello
Hello
Hello
```

### Kolejność dekoratorów

```python
def d1(f):
    def wrapper():
        print("d1 przed")
        f()
        print("d1 po")
    return wrapper

def d2(f):
    def wrapper():
        print("d2 przed")
        f()
        print("d2 po")
    return wrapper

@d1
@d2
def hello():
    print("Hello")

hello()
```

Wynik:

```python
d1 przed
d2 przed
Hello
d2 po
d1 po
```

---

## Dobre praktyki

- zaczynaj od bardzo prostych dekoratorów,
- używaj `@wraps`,
- nie komplikuj dekoratora bez potrzeby,
- testuj dekoratory osobno,
- rozdzielaj dekoratory o różnych odpowiedzialnościach.

Praktyczna zasada:

jeśli nie umiesz rozpisać dekoratora ręcznie jako:

```python
funkcja = dekorator(funkcja)
```

to znaczy, że warto jeszcze cofnąć się o krok i uprościć przykład.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- dekorator bierze funkcję i zwraca nową funkcję,
- działa dzięki temu, że funkcje są obiektami,
- closures i wrapper są sercem dekoratorów,
- składnia `@` to tylko skrót,
- `functools.wraps` to bardzo ważna dobra praktyka,
- dekoratory są bardzo często używane także w frameworkach.

Najważniejsze do zapamiętania:

- dekoratory nie są magią, tylko połączeniem funkcji jako obiektów, closures i wrappera,
- najpierw warto umieć prosty dekorator, potem dekorator z argumentami, a dopiero później bardziej zaawansowane odmiany,
- jeśli rozumiesz ręczne `f = dekorator(f)`, to rozumiesz serce całego tematu.
