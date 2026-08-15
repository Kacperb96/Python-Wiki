# Deskryptory w Pythonie

## Wprowadzenie

Deskryptory to jeden z tych tematów, które brzmią groźnie, a potem okazuje się, że ich sens da się wytłumaczyć całkiem praktycznie.

Najprostsza intuicja jest taka:

`deskryptor to obiekt, który przejmuje kontrolę nad dostępem do atrybutu`

Zamiast zwykłego:

- odczytu,
- zapisu,
- usuwania,

możesz wstawić własną logikę.

I właśnie dlatego deskryptory są ważne, bo pod spodem są blisko takich rzeczy jak:

- `property`,
- walidacja pól,
- ORM-y,
- część bardziej zaawansowanego modelu obiektowego Pythona.

## Najpierw najważniejsze pytanie

Po co w ogóle się tym interesować?

Bo deskryptor pozwala zrobić takie rzeczy jak:

- pilnowanie poprawności danych,
- logowanie dostępu do atrybutu,
- leniwe wyliczanie wartości,
- współdzielenie tej samej logiki pola między wieloma klasami.

Jeżeli patrzysz na to pytaniem:

`czy to tylko teoria?`

to odpowiedź brzmi:

`nie, to mechanizm stojący bardzo blisko praktycznych narzędzi`

## Najprostszy mentalny model

Masz zwykły atrybut:

```python
user.name
```

Przy prostym modelu Python zwykle czyta wartość z obiektu.

Ale jeśli `name` jest deskryptorem, to Python może zamiast prostego odczytu wywołać:

```python
descriptor.__get__(instance, owner)
```

I analogicznie przy zapisie:

```python
user.name = "Anna"
```

Python może zamiast zwykłego podstawienia wywołać:

```python
descriptor.__set__(instance, value)
```

To właśnie jest cała magia: `obiekt atrybutu` steruje zachowaniem dostępu.

## Trzy najważniejsze metody

Deskryptory używają zwykle:

- `__get__`
- `__set__`
- `__delete__`

Nie zawsze wszystkich naraz.

### `__get__(self, instance, owner)`

Obsługuje odczyt atrybutu.

### `__set__(self, instance, value)`

Obsługuje zapis atrybutu.

### `__delete__(self, instance)`

Obsługuje `del obj.attr`.

## Najprostszy deskryptor tylko do odczytu

Zacznijmy od banalnego przykładu.

```python
class TylkoDoOdczytu:
    def __get__(self, instance, owner):
        return 42


class Test:
    wartosc = TylkoDoOdczytu()


t = Test()
print(t.wartosc)
```

Output:

```python
42
```

Co tu się stało?

- `wartosc` nie jest zwykłą liczbą,
- `wartosc` jest obiektem `TylkoDoOdczytu`,
- przy `t.wartosc` Python wywołuje `__get__`.

## Ważny detal: dostęp przez klasę

Zobaczmy to:

```python
class TylkoDoOdczytu:
    def __get__(self, instance, owner):
        print("instance =", instance)
        print("owner =", owner)
        return 42


class Test:
    wartosc = TylkoDoOdczytu()


t = Test()
print(t.wartosc)
print(Test.wartosc)
```

Przy dostępie przez instancję:

- `instance` to obiekt `t`,
- `owner` to klasa `Test`.

Przy dostępie przez klasę:

- `instance` może być `None`,
- `owner` nadal wskazuje klasę.

To ważne, bo wiele dobrych deskryptorów obsługuje oba przypadki sensownie.

## Pierwszy naprawdę praktyczny przykład: walidacja

To klasyczny use case deskryptora.

```python
class DodatniaLiczba:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Musi byc dodatnia")
        instance.__dict__[self.name] = value


class Produkt:
    cena = DodatniaLiczba()

    def __init__(self, cena):
        self.cena = cena


p = Produkt(100)
print(p.cena)
```

Output:

```python
100
```

A teraz błąd:

```python
p = Produkt(-5)
```

Output:

```python
ValueError: Musi byc dodatnia
```

To już jest realna wartość: masz wspólną, wielorazową logikę walidacji pola.

## Co robi `__set_name__`

To bardzo przydatna metoda.

```python
def __set_name__(self, owner, name):
    self.name = name
```

Python wywołuje ją wtedy, gdy klasa jest tworzona.

Dzięki temu deskryptor dowiaduje się:

- w jakiej klasie siedzi,
- pod jaką nazwą został przypisany.

Czyli w przykładzie:

```python
class Produkt:
    cena = DodatniaLiczba()
```

`self.name` stanie się `"cena"`.

To pozwala później zapisywać dane np. do:

```python
instance.__dict__["cena"]
```

## Dlaczego używamy `instance.__dict__`

To jest miejsce, gdzie zwykła instancja przechowuje swoje atrybuty.

Przykład:

```python
class User:
    def __init__(self):
        self.name = "Anna"


u = User()
print(u.__dict__)
```

Output:

```python
{'name': 'Anna'}
```

Deskryptor bardzo często:

- nie trzyma danych "w sobie",
- tylko steruje tym, jak dane lądują w `instance.__dict__`.

To ważne, bo jeden deskryptor jest zwykle współdzielony przez wszystkie instancje klasy.

## Ważna pułapka: gdzie nie trzymać wartości

Zły pomysł:

```python
class ZlyDeskryptor:
    def __set__(self, instance, value):
        self.value = value
```

Dlaczego zły?

Bo `self` to sam deskryptor, czyli współdzielony obiekt na poziomie klasy.

Skutek:

- różne instancje zaczynają nadpisywać sobie dane,
- wartości nie są per-obiekt.

Lepsza intuicja:

`deskryptor zarządza danymi instancji, ale nie powinien przechowywać ich wspólnie dla wszystkich obiektów`

## Deskryptor logujący dostęp

```python
class LogowanyAtrybut:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        print(f"Odczyt pola: {self.name}")
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(f"Zapis pola: {self.name} = {value}")
        instance.__dict__[self.name] = value


class User:
    name = LogowanyAtrybut()

    def __init__(self, name):
        self.name = name


u = User("Anna")
print(u.name)
```

Output:

```python
Zapis pola: name = Anna
Odczyt pola: name
Anna
```

To bardzo fajny przykład, bo dokładnie widać moment przejęcia kontroli.

## Deskryptory a `property`

To bardzo ważne połączenie.

`property` jest w praktyce gotowym, wygodnym deskryptorem.

Przykład:

```python
class Temperature:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError("Za malo")
        self._value = new_value
```

To jest zwykle lepsze niż pisanie własnego deskryptora, jeśli:

- masz jedną klasę,
- jedno pole,
- prostą walidację.

## Kiedy `property` wystarczy

Jeśli chcesz:

- kontrolować jedno pole,
- dodać prostą walidację,
- poprawić ergonomię jednej klasy,

to `property` zwykle będzie czytelniejsze.

## Kiedy deskryptor daje przewagę

Jeśli chcesz:

- użyć tej samej logiki w wielu klasach,
- mieć wielokrotne pola o wspólnym zachowaniu,
- budować bardziej ogólny mechanizm.

Przykład:

- `PositiveInt`,
- `NonEmptyString`,
- `EmailField`,
- `ValidatedPrice`.

Wtedy deskryptor zaczyna wygrywać nad wielokrotnym kopiowaniem `property`.

## Deskryptor danych i niedanych

To ważne rozróżnienie.

### Deskryptor danych

Ma `__set__` albo `__delete__`.

### Deskryptor niedanych

Ma tylko `__get__`.

To wpływa na priorytet przy wyszukiwaniu atrybutów.

W praktyce początkująco-średniej najważniejsze jest:

- deskryptor danych ma silniejszą kontrolę nad atrybutem,
- deskryptor niedanych jest "lżejszy".

## Eksperyment: deskryptor danych vs niedanych

Najlepiej zobaczyć to na bardzo konkretnym przykładzie.

### Deskryptor niedanych

Ma tylko `__get__`.

```python
class NonDataDescriptor:
    def __get__(self, instance, owner):
        return "wartosc z deskryptora"


class Test:
    pole = NonDataDescriptor()


t = Test()
print(t.pole)

t.__dict__["pole"] = "wartosc z instancji"
print(t.pole)
```

Output:

```python
wartosc z deskryptora
wartosc z instancji
```

Tutaj zwykły atrybut instancji może "przykryć" deskryptor niedanych.

### Deskryptor danych

Ma `__set__` albo `__delete__`.

```python
class DataDescriptor:
    def __get__(self, instance, owner):
        return "wartosc z deskryptora danych"

    def __set__(self, instance, value):
        instance.__dict__["_pole"] = value


class Test:
    pole = DataDescriptor()


t = Test()
t.__dict__["pole"] = "wartosc z instancji"
print(t.pole)
```

Output:

```python
wartosc z deskryptora danych
```

To właśnie pokazuje praktyczną różnicę:

- deskryptor niedanych można łatwiej przykryć,
- deskryptor danych ma wyższy priorytet.

## Jak Python szuka atrybutu

Pełne reguły są bardziej techniczne, ale uproszczona intuicja jest taka:

1. Python sprawdza mechanizmy klasy, w tym deskryptory.
2. Potem patrzy na dane instancji.
3. Potem szuka dalej w klasach bazowych.

To właśnie dlatego deskryptor może przechwycić odczyt lub zapis zanim dojdzie do zwykłego pobrania wartości.

## Deskryptory a ORM-y

W ORM-ach pola modelu często nie są zwykłymi atrybutami.

Pod odczytem:

```python
user.email
```

może stać:

- walidacja,
- lazy loading,
- mapowanie na kolumnę,
- śledzenie zmian,
- integracja z bazą.

To jeden z powodów, dla których deskryptory są tak istotne w bardziej zaawansowanym Pythonie.

## Przykład z `__delete__`

Ta metoda pojawia się rzadziej, ale dobrze wiedzieć, po co istnieje.

```python
class PoleZUsuwaniem:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print(f"Usuwam pole: {self.name}")
        del instance.__dict__[self.name]


class User:
    email = PoleZUsuwaniem()


u = User()
u.email = "anna@example.com"
print(u.email)
del u.email
print(u.__dict__)
```

Output:

```python
anna@example.com
Usuwam pole: email
{}
```

To przydaje się wtedy, gdy:

- chcesz logować usuwanie,
- chcesz kontrolować cleanup,
- chcesz zablokować usuwanie albo dodać własne reguły.

## Mini case study: walidacja wielu pól

Załóżmy, że chcesz mieć wiele pól dodatnich:

```python
class Product:
    price = DodatniaLiczba()
    quantity = DodatniaLiczba()
```

Bez deskryptora pewnie pisałbyś:

- osobne `property`,
- osobną walidację dla każdego pola,
- dużo powtarzalnego kodu.

Z deskryptorem:

- logika walidacji jest współdzielona,
- klasy są krótsze,
- intencja jest czytelna.

To jest bardzo praktyczny argument za deskryptorami.

## Typowe błędy początkujących

### 1. Nauka deskryptorów bez `property`

Jeśli nie rozumiesz `property`, deskryptory będą wyglądać jak magia.

### 2. Trzymanie danych w samym deskryptorze

To bardzo częsty błąd i zwykle prowadzi do współdzielenia danych między instancjami.

### 3. Używanie deskryptora tam, gdzie zwykła metoda lub `property` są prostsze

To overengineering.

### 4. Brak obsługi `instance is None`

Przy dostępie przez klasę może to być ważne.

## Kiedy deskryptor ma sens

- wspólna walidacja dla wielu pól,
- mechanizm biblioteczny,
- głębsze zrozumienie modelu obiektowego,
- bardziej zaawansowane narzędzia i frameworki.

## Kiedy deskryptor jest przesadą

- jedna klasa,
- jedno pole,
- jedna prosta walidacja,
- brak potrzeby wielokrotnego użycia.

Wtedy `property` prawie zawsze będzie czytelniejsze.

## Dobre praktyki

- zaczynaj od `property`,
- przechodź do deskryptora dopiero, gdy logika ma być współdzielona,
- przechowuj dane instancji w `instance.__dict__`,
- używaj `__set_name__`,
- nie komplikuj kodu bez realnego zysku.

## Szybka ściąga

Najważniejsze rzeczy:

- `__get__`
- `__set__`
- `__delete__`
- `__set_name__`
- `instance.__dict__`
- `property` jako prostszy kuzyn deskryptora
- deskryptor danych ma wyższy priorytet niż zwykły wpis w instancji
- deskryptor niedanych można przykryć atrybutem instancji

## Zadania

1. Napisz deskryptor tylko do odczytu zwracający stałą wartość.
2. Napisz deskryptor walidujący, że liczba jest dodatnia.
3. Użyj tego deskryptora w klasie `Product`.
4. Zrób eksperyment pokazujący różnicę między deskryptorem danych i niedanych.
5. Napisz deskryptor obsługujący `del obj.attr`.
4. Napisz deskryptor logujący odczyt i zapis pola.
5. Wyjaśnij różnicę między `property` a własnym deskryptorem.
6. Opisz sytuację, w której deskryptor daje realną przewagę nad `property`.
