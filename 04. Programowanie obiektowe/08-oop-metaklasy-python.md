# Metaklasy w Pythonie

## Wprowadzenie

Metaklasy to jeden z najbardziej zaawansowanych tematów w Pythonie.

I od razu najuczciwsza rzecz:

`większość programistów Pythona bardzo rzadko musi pisać własne metaklasy`

Ale warto rozumieć:

- czym one są,
- po co istnieją,
- gdzie naprawdę mają sens,
- i czemu nie trzeba ich wciskać do zwykłego kodu aplikacyjnego.

## Najkrótsza intuicja

Zwykła klasa tworzy obiekty.

Metaklasa tworzy klasy.

Czyli:

- `Pies` tworzy obiekty typu `Pies`,
- a sama klasa `Pies` też jest obiektem,
- i ten obiekt został utworzony przez metaklasę.

W Pythonie domyślną metaklasą jest:

`type`

## Najpierw ważny fundament

Zanim metaklasy zaczną mieć sens, trzeba dobrze rozumieć:

- klasy,
- obiekty,
- dziedziczenie,
- magic methods,
- `type`.

Bo metaklasy to już poziom wyżej niż zwykłe OOP.

## Klasa też jest obiektem

To jest absolutny fundament tego tematu.

```python
class Pies:
    pass


print(type(Pies))
```

Output:

```python
<class 'type'>
```

To znaczy, że:

- `Pies` nie jest tylko "definicją",
- `Pies` jest obiektem,
- i ten obiekt ma typ `type`.

## Co to znaczy w praktyce

Tak jak:

```python
azor = Pies()
```

tworzy obiekt `azor` z klasy `Pies`,

tak:

```python
class Pies:
    pass
```

w praktyce tworzy obiekt-klasę `Pies`, a robi to domyślna metaklasa `type`.

## `type` jako metaklasa

`type` jest wyjątkowe, bo:

- jest klasą,
- tworzy klasy,
- można używać go także jawnie.

## Dynamiczne tworzenie klasy przez `type`

```python
Pies = type("Pies", (), {})

print(Pies)
print(type(Pies))
```

Output:

```python
<class '__main__.Pies'>
<class 'type'>
```

To pokazuje, że zwykła definicja klasy i wywołanie `type(...)` są ze sobą głęboko powiązane.

## `type` z atrybutami

```python
Pies = type("Pies", (), {"gatunek": "pies"})

print(Pies.gatunek)
```

Output:

```python
pies
```

To nie jest najczytelniejszy styl pisania klas, ale świetnie pokazuje, że:

`klasa to też obiekt tworzony przez mechanizm`

## Czym jest metaklasa

Metaklasa to klasa, która steruje tworzeniem klas.

Najprościej:

- zwykła klasa steruje tworzeniem instancji,
- metaklasa steruje tworzeniem samej klasy.

Czyli jeśli zwykła klasa odpowiada za:

```python
obj = MyClass()
```

to metaklasa odpowiada poziom wyżej za to, jak powstaje `MyClass`.

## Najprostsza własna metaklasa

```python
class Meta(type):
    pass
```

To już jest własna metaklasa, bo dziedziczy po `type`.

Można jej użyć tak:

```python
class MojaKlasa(metaclass=Meta):
    pass
```

## Pierwszy praktyczny efekt: log przy tworzeniu klasy

```python
class Meta(type):
    def __new__(mcls, name, bases, namespace):
        print(f"Tworze klase: {name}")
        return super().__new__(mcls, name, bases, namespace)


class User(metaclass=Meta):
    pass
```

Output:

```python
Tworze klase: User
```

To bardzo ważne, bo pokazuje moment działania metaklasy:

`nie przy tworzeniu instancji, tylko przy tworzeniu klasy`

## `__new__` w metaklasie

To najważniejsze miejsce do pracy z metaklasą.

```python
def __new__(mcls, name, bases, namespace):
    ...
```

Tu dostajesz:

- `name` — nazwę klasy,
- `bases` — klasy bazowe,
- `namespace` — słownik z definicją klasy.

Możesz więc:

- coś sprawdzić,
- coś dopisać,
- coś zablokować,
- zmodyfikować klasę zanim zostanie utworzona.

## Najbardziej praktyczna intuicja

Metaklasa jest jak:

`fabryka klas`

Nie tworzy bezpośrednio `user = User()`.

Ona bierze definicję klasy `User` i decyduje:

- czy wolno ją utworzyć,
- jak ją zmodyfikować,
- czy dodać jej coś automatycznie.

## Walidacja klasy przez metaklasę

To jeden z nielicznych naprawdę dobrych przykładów dla początkująco-średniego poziomu.

```python
class RequireSave(type):
    def __new__(mcls, name, bases, namespace):
        if name != "BaseModel" and "save" not in namespace:
            raise TypeError(f"Klasa {name} musi miec metode save")
        return super().__new__(mcls, name, bases, namespace)


class BaseModel(metaclass=RequireSave):
    pass


class User(BaseModel):
    def save(self):
        print("save user")
```

To przejdzie poprawnie.

Ale:

```python
class Product(BaseModel):
    pass
```

da błąd w stylu:

```text
TypeError: Klasa Product musi miec metode save
```

To jest dobry przykład, bo pokazuje realną wartość:

- kontrakt,
- walidacja definicji,
- ochrona architektury.

## Automatyczne dopisywanie atrybutu

```python
class AddTagMeta(type):
    def __new__(mcls, name, bases, namespace):
        namespace["tag"] = name.lower()
        return super().__new__(mcls, name, bases, namespace)


class Order(metaclass=AddTagMeta):
    pass


print(Order.tag)
```

Output:

```python
order
```

To pokazuje, że metaklasa może coś dopisywać automatycznie do klasy.

## `__init__` w metaklasie

Metaklasa może też robić logikę po utworzeniu klasy:

```python
class Meta(type):
    def __init__(cls, name, bases, namespace):
        print(f"Init metaklasy dla {name}")
        super().__init__(name, bases, namespace)
```

Ale na poziomie nauki najważniejsze jest zrozumienie `__new__`.

To tam zwykle najczytelniej widać sens działania metaklasy.

## `__call__` w metaklasie

To bardziej zaawansowany temat.

Metaklasa może też przejąć to, co dzieje się przy:

```python
User()
```

czyli przy tworzeniu instancji klasy.

To znaczy, że może sterować:

- sposobem tworzenia obiektów,
- singletonem,
- dodatkowymi logami,
- kontrolą instancjonowania.

Przykład ideowy:

```python
class Meta(type):
    def __call__(cls, *args, **kwargs):
        print(f"Tworze instancje {cls.__name__}")
        return super().__call__(*args, **kwargs)
```

To już jednak poziom bardziej “zrozumieć, że się da” niż codzienna praktyka.

## Metaklasa a dekorator klasy

To bardzo ważne porównanie.

Jeśli chcesz:

- lekko zmodyfikować klasę,
- dodać prosty atrybut,
- opakować definicję klasy,

to często dekorator klasy jest prostszy i czytelniejszy.

Metaklasa ma sens dopiero wtedy, gdy naprawdę chcesz kontrolować proces tworzenia klasy głębiej.

## Kiedy metaklasa ma sens

Najczęściej w:

- frameworkach,
- bibliotekach,
- rejestracji klas,
- walidacji kontraktów klas,
- zaawansowanej architekturze, gdzie wiele klas ma być tworzone według ścisłych reguł.

## Kiedy metaklasa jest złym pomysłem

Najczęściej wtedy, gdy:

- chcesz tylko "zrobić coś bardziej zaawansowanego",
- zwykły dekorator klasy wystarcza,
- zwykła klasa bazowa wystarcza,
- problem jest mały,
- zespół będzie potem przeklinał czytelność rozwiązania.

To bardzo ważna zasada:

`metaklasa ma rozwiązywać realny problem, nie być popisem`

## Metaklasy a klasy abstrakcyjne

Warto wiedzieć, że `ABC` też działa przy użyciu własnych mechanizmów metaklasowych.

Nie musisz tego znać głęboko na start, ale to kolejny sygnał, że:

`metaklasy nie są egzotycznym dodatkiem; one siedzą pod ważnymi narzędziami Pythona`

## Typowe błędy początkujących

### 1. Próba użycia metaklasy do zwykłej walidacji obiektu

Jeśli chcesz kontrolować instancję, zwykła klasa, `property`, deskryptor lub `__init__` są zwykle lepsze.

### 2. Mieszanie poziomów abstrakcji

Metaklasa działa na poziomie klasy, nie zwykłego obiektu.

### 3. Używanie metaklasy bez zrozumienia `type`

To prawie zawsze kończy się tylko kopiowaniem kodu bez rozumienia.

### 4. Tworzenie zbyt skomplikowanej architektury

Jeśli musisz długo tłumaczyć, po co ta metaklasa istnieje, to może nie powinna istnieć.

## Mini case study

Masz bibliotekę, w której wszystkie modele pluginów muszą:

- mieć atrybut `plugin_name`,
- implementować metodę `run`,
- zostać zarejestrowane przy definicji klasy.

To jest właśnie typ problemu, w którym metaklasa może mieć sens.

Ale w zwykłej aplikacji CRUD:

raczej nie.

## Pełniejszy case study: rejestracja pluginów

To jest jeden z najbardziej klasycznych przypadków, gdzie metaklasa naprawdę ma sens.

Chcemy, żeby:

- każda klasa pluginu rejestrowała się automatycznie,
- każda miała `plugin_name`,
- każda implementowała metodę `run`.

```python
class PluginMeta(type):
    registry = {}

    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)

        if name != "BasePlugin":
            if "plugin_name" not in namespace:
                raise TypeError(f"{name} musi miec plugin_name")
            if "run" not in namespace:
                raise TypeError(f"{name} musi implementowac run()")

            mcls.registry[cls.plugin_name] = cls

        return cls


class BasePlugin(metaclass=PluginMeta):
    pass


class EmailPlugin(BasePlugin):
    plugin_name = "email"

    def run(self):
        return "Wysylam email"


class SmsPlugin(BasePlugin):
    plugin_name = "sms"

    def run(self):
        return "Wysylam sms"


print(PluginMeta.registry)
print(PluginMeta.registry["email"]().run())
```

Output:

```python
{'email': <class '__main__.EmailPlugin'>, 'sms': <class '__main__.SmsPlugin'>}
Wysylam email
```

To jest już bardzo praktyczny wzorzec:

- klasy same się rejestrują,
- framework może je później odnajdywać po nazwie,
- kontrakt jest pilnowany przy definicji klasy, nie dopiero w runtime dużo później.

## Metaklasa vs `__init_subclass__`

To bardzo ważne porównanie, bo często metaklasa nie jest jedyną opcją.

`__init_subclass__` działa przy tworzeniu klas potomnych i bywa prostsze.

```python
class BasePlugin:
    registry = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls.__name__ != "BasePlugin":
            if not hasattr(cls, "plugin_name"):
                raise TypeError("Brak plugin_name")
            BasePlugin.registry[cls.plugin_name] = cls


class CsvPlugin(BasePlugin):
    plugin_name = "csv"
```

To rozwiązanie bywa lepsze, gdy:

- nie potrzebujesz pełnej mocy metaklasy,
- chcesz tylko reagować na tworzenie podklas,
- zależy Ci na prostszym kodzie.

## Kiedy wybrać `__init_subclass__`, a kiedy metaklasę

Wybierz `__init_subclass__`, gdy:

- chcesz rejestrować podklasy,
- chcesz robić lekką walidację klas potomnych,
- nie musisz głęboko sterować procesem tworzenia klasy.

Wybierz metaklasę, gdy:

- musisz kontrolować tworzenie klasy bardzo wcześnie,
- chcesz działać na poziomie `type`,
- budujesz bardziej frameworkowy mechanizm,
- potrzebujesz wspólnego zachowania dla wielu klas w sposób bardziej systemowy.

## Dobre praktyki

- najpierw rozważ zwykłą klasę,
- potem dekorator klasy,
- potem klasę abstrakcyjną,
- dopiero na końcu metaklasę,
- używaj jej tylko przy realnym zysku architektonicznym.

## Szybka ściąga

Najważniejsze rzeczy:

- domyślna metaklasa to `type`,
- klasa jest obiektem,
- metaklasa tworzy klasy,
- najczęściej pracujesz w `__new__`,
- metaklasy służą głównie frameworkom, bibliotekom i bardzo świadomej architekturze.

## Zadania

1. Sprawdź `type()` dla zwykłej klasy.
2. Utwórz klasę dynamicznie przez `type`.
3. Napisz prostą metaklasę wypisującą nazwę tworzonej klasy.
4. Napisz metaklasę, która wymaga obecności konkretnej metody w klasie.
5. Opisz własnymi słowami, kiedy metaklasa ma sens, a kiedy to przesada.
