# Pakiety w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest pakiet](#czym-jest-pakiet)
3. [Pakiet a moduł](#pakiet-a-moduł)
4. [Rola `__init__.py`](#rola-__init__py)
5. [Importy w pakietach](#importy-w-pakietach)
6. [Importy bezwzględne i względne](#importy-bezwzględne-i-względne)
7. [Po co używać pakietów](#po-co-używać-pakietów)
8. [Przykładowa struktura](#przykładowa-struktura)
9. [Jak myśleć o podziale na pakiety](#jak-myśleć-o-podziale-na-pakiety)
10. [Typowe pułapki początkujących](#typowe-pułapki-początkujących)
11. [Praktyczne przykłady](#praktyczne-przykłady)
12. [Dobre praktyki](#dobre-praktyki)
13. [Podsumowanie](#podsumowanie)
14. [Mini ściąga](#mini-ściąga)
15. [Ćwiczenia](#ćwiczenia)
16. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Gdy projekt rośnie, same moduły przestają wystarczać. Wtedy pojawiają się pakiety.

Pakiet porządkuje moduły w katalogi tematyczne i pozwala budować sensowniejszą strukturę projektu.

To naturalny krok pomiędzy "mam kilka plików" a "mam projekt, który da się rozwijać bez chaosu".

---

## Czym jest pakiet

Pakiet to katalog grupujący moduły Pythona.

Najczęściej zawiera plik `__init__.py`.

Przykład:

```text
app/
    __init__.py
    users.py
    utils.py
```

Pakiet może też zawierać podpakiety.

---

## Pakiet a moduł

Moduł:

- pojedynczy plik `.py`

Pakiet:

- katalog z modułami i ewentualnie podpakietami

To ważne rozróżnienie, bo większy projekt zwykle składa się z wielu modułów zebranych w pakiety.

---

## Rola `__init__.py`

`__init__.py`:

- oznacza pakiet,
- może być pusty,
- może też wystawiać wybrane elementy pakietu na zewnątrz.

Przykład:

```python
from .users import create_user
```

Wtedy użytkownik pakietu może importować prościej.

Na początku często `__init__.py` jest pusty i to też jest okej.

---

## Importy w pakietach

Przykład:

```python
from app.users import create_user
```

albo wewnątrz pakietu:

```python
from .utils import normalize_name
```

Takie importy od razu pokazują strukturę projektu.

---

## Importy bezwzględne i względne

### Import bezwzględny

```python
from app.users import create_user
```

Pokazuje ścieżkę od poziomu pakietu.

### Import względny

```python
from .utils import normalize_name
```

Mówi:

"zaimportuj coś z tego samego pakietu".

Na początku najważniejsze jest zrozumienie, że oba podejścia istnieją i mają sens w różnych kontekstach.

### Kiedy który jest wygodny

Import bezwzględny:

- bywa czytelniejszy z zewnątrz pakietu,
- jasno pokazuje ścieżkę.

Import względny:

- bywa wygodny wewnątrz pakietu,
- skraca zapis,
- pokazuje, że zależność jest lokalna dla danego pakietu.

---

## Po co używać pakietów

Pakiety pomagają:

- rozdzielić odpowiedzialności,
- grupować powiązane moduły,
- uniknąć jednego ogromnego katalogu z plikami,
- przygotować projekt do rozwoju i testowania.

---

## Przykładowa struktura

```text
app/
    __init__.py
    main.py
    users.py
    utils.py
```

W większych projektach pojawiają się też podpakiety, np.:

- `services/`
- `repositories/`
- `api/`

Na przykład:

```text
app/
    __init__.py
    api/
        __init__.py
        routes.py
    services/
        __init__.py
        users.py
```

---

## Jak myśleć o podziale na pakiety

Dobry pakiet zwykle grupuje rzeczy, które należą do jednego obszaru odpowiedzialności.

Przykłady:

- `users/` dla logiki użytkowników,
- `payments/` dla płatności,
- `validators/` dla walidacji,
- `services/` dla logiki usługowej.

Nie chodzi o to, żeby robić dużo katalogów na siłę. Chodzi o to, żeby struktura pomagała się odnaleźć.

Złe pytanie:

- "jak zrobić projekt bardziej profesjonalnie?"

Lepsze pytanie:

- "jak podzielić pliki tak, żeby po miesiącu łatwo było znaleźć właściwe miejsce?"

---

## Co daje `__init__.py` w praktyce

Załóżmy taką strukturę:

```text
app/
    __init__.py
    users.py
```

`users.py`:

```python
def create_user(name):
    return {"name": name}
```

`__init__.py`:

```python
from .users import create_user
```

Teraz możesz zrobić:

```python
from app import create_user

print(create_user("Ania"))
```

Output:

```python
{'name': 'Ania'}
```

Czyli `__init__.py` może uprościć publiczne API pakietu.

---

## Typowe pułapki początkujących

- wrzucanie całego projektu do jednego katalogu bez struktury,
- brak `__init__.py` tam, gdzie materiał chce ćwiczyć klasyczny pakiet,
- nieczytelne importy między modułami,
- mieszanie kodu startowego i logiki pakietu,
- zbyt wczesne dzielenie projektu na dziesiątki katalogów bez realnej potrzeby,
- próba uruchamiania przypadkowego pliku z wnętrza pakietu bez zrozumienia ścieżek importu.

---

## Praktyczne przykłady

### Prosty pakiet `app`

`app/utils.py`

```python
def normalize_name(name):
    return name.strip().capitalize()
```

`app/users.py`

```python
from .utils import normalize_name

def create_user(name):
    return {"name": normalize_name(name)}
```

Jeśli wywołasz:

```python
print(create_user("  aNNa  "))
```

to output będzie:

```python
{'name': 'Anna'}
```

`app/__init__.py`

```python
from .users import create_user
```

I wtedy:

```python
from app import create_user

print(create_user("  kasia "))
```

Output:

```python
{'name': 'Kasia'}
```

### Pakiet z podpakietem

```text
shop/
    __init__.py
    products/
        __init__.py
        service.py
```

To pokazuje, że pakiet może mieć kolejne warstwy organizacji.

---

## Dobre praktyki

- grupuj moduły według odpowiedzialności,
- nie rób pakietów tylko po to, żeby były zaawansowane,
- dbaj o czytelne importy,
- trzymaj prosty, przewidywalny układ katalogów,
- rozwijaj strukturę stopniowo wraz z projektem,
- używaj `__init__.py` świadomie, a nie mechanicznie.

---

## Podsumowanie

Pakiety to naturalny kolejny krok po modułach.

Pozwalają budować projekty, które są czytelne nie tylko w jednym pliku, ale w całej strukturze katalogów.

Najważniejsze rzeczy do zapamiętania:

- moduł to plik,
- pakiet to katalog z modułami,
- `__init__.py` może oznaczać pakiet i upraszczać jego API,
- importy bezwzględne i względne mają różne zastosowania.

---

## Mini ściąga

```text
app/
    __init__.py
    users.py
    utils.py
```

```python
from .utils import normalize_name
from app.users import create_user
from app import create_user
```

---

## Ćwiczenia

1. Utwórz pakiet `app`.
2. Dodaj `users.py`, `utils.py`, `__init__.py`.
3. Zrób import względny wewnątrz pakietu.
4. Wystaw funkcję przez `__init__.py`.
5. Utwórz prosty podpakiet i opisz jego rolę.
3. Zaimportuj funkcję z `utils.py` do `users.py`.
4. Dodaj import w `__init__.py`, który wystawi jedną funkcję pakietu.

---

## Przykładowe rozwiązania

### 1. Struktura

```text
app/
    __init__.py
    users.py
    utils.py
```

### 2. `utils.py`

```python
def normalize_name(name):
    return name.strip().capitalize()
```

### 3. `users.py`

```python
from .utils import normalize_name

def create_user(name):
    return {"name": normalize_name(name)}
```

### 4. `__init__.py`

```python
from .users import create_user
```
