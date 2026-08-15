# Analiza tracebacków w Pythonie

## O co chodzi

Traceback to nie jest losowa ściana tekstu.

To ślad prowadzący do miejsca, w którym program się wywrócił.

Jeśli umiesz czytać traceback, masz bardzo silne narzędzie debugowania.

## Co zwykle zawiera traceback

Najczęściej zobaczysz:

- sekwencję wywołań,
- pliki i numery linii,
- nazwy funkcji,
- końcowy typ wyjątku,
- komunikat błędu.

To w praktyce zapis drogi, którą program przeszedł do momentu błędu.

## Najważniejsza zasada

Czytaj traceback od końca, ale rozumiej go jako całość.

### Końcówka tracebacka mówi zwykle:

- jaki wyjątek wystąpił,
- na czym polega problem lokalnie.

### Wcześniejsze linie pokazują:

- jak program do tego miejsca doszedł.

## Prosty przykład

```python
def divide(a: int, b: int) -> float:
    return a / b


def run() -> None:
    print(divide(10, 0))


run()
```

Traceback będzie wyglądał mniej więcej tak:

```text
Traceback (most recent call last):
  File "main.py", line 8, in <module>
    run()
  File "main.py", line 5, in run
    print(divide(10, 0))
  File "main.py", line 2, in divide
    return a / b
ZeroDivisionError: division by zero
```

## Jak to czytać

### Końcówka

```text
ZeroDivisionError: division by zero
```

To mówi, co się stało.

### Linia tuż nad tym

```text
File "main.py", line 2, in divide
    return a / b
```

To mówi, gdzie błąd wystąpił bezpośrednio.

### Wyższe linie

Pokazują, skąd to wywołanie przyszło.

## Najczęstszy błąd początkujących

Patrzenie tylko na ostatnią linię wyjątku bez spojrzenia na ścieżkę dojścia.

Albo odwrotnie:

- czytanie tracebacka od góry jak zwykłego loga i gubienie sensu.

## Traceback a objaw vs przyczyna

To bardzo ważne.

Traceback pokazuje miejsce awarii, ale nie zawsze od razu pokazuje prawdziwą przyczynę biznesową albo logiczną.

Przykład:

- wyjątek wybuchł w funkcji walidującej,
- ale prawdziwa przyczyna jest w tym, że wcześniej ktoś przekazał zły typ danych.

Dlatego traceback to punkt wejścia do debugowania, a nie zawsze pełna odpowiedź.

## Przykład z kilkoma warstwami

```python
def parse_age(text: str) -> int:
    return int(text)


def build_user(age_text: str) -> dict:
    return {"age": parse_age(age_text)}


def handler() -> None:
    user = build_user("abc")
    print(user)


handler()
```

Traceback będzie wyglądał mniej więcej tak:

```text
Traceback (most recent call last):
  File "main.py", line 11, in <module>
    handler()
  File "main.py", line 7, in handler
    user = build_user("abc")
  File "main.py", line 4, in build_user
    return {"age": parse_age(age_text)}
  File "main.py", line 2, in parse_age
    return int(text)
ValueError: invalid literal for int() with base 10: 'abc'
```

## Co tu widzisz

- problem końcowy: `ValueError`,
- bezpośrednia awaria: `int(text)`,
- przepływ dojścia: `handler -> build_user -> parse_age`.

To już jest bardzo cenna mapa problemu.

## Bardziej złożony traceback 1: błąd głęboko w serwisie

Wyobraź sobie taki przepływ:

```python
def get_discount(user: dict) -> int:
    return user["discount"]


def calculate_total(user: dict, price: int) -> int:
    discount = get_discount(user)
    return price - discount


def place_order(payload: dict) -> int:
    user = payload["user"]
    price = payload["price"]
    return calculate_total(user, price)


def endpoint() -> None:
    payload = {"user": {"name": "Anna"}, "price": 100}
    print(place_order(payload))


endpoint()
```

Przykładowy traceback:

```text
Traceback (most recent call last):
  File "main.py", line 17, in <module>
    endpoint()
  File "main.py", line 14, in endpoint
    print(place_order(payload))
  File "main.py", line 10, in place_order
    return calculate_total(user, price)
  File "main.py", line 6, in calculate_total
    discount = get_discount(user)
  File "main.py", line 2, in get_discount
    return user["discount"]
KeyError: 'discount'
```

### Jak to czytać

- miejsce awarii: `user["discount"]`,
- pytanie nie brzmi tylko "jak obsłużyć KeyError",
- ważniejsze pytanie brzmi: czemu użytkownik nie ma pola `discount`.

### Możliwe przyczyny

- payload ma zły kształt,
- wcześniejsza walidacja nie działa,
- kontrakt między warstwami jest niepełny,
- pole powinno być opcjonalne, ale kod tego nie uwzględnia.

## Bardziej złożony traceback 2: `NoneType` w dalszej warstwie

```python
def find_user(user_id: int) -> dict | None:
    if user_id == 1:
        return {"name": "Anna"}
    return None


def format_user_name(user: dict) -> str:
    return user["name"].upper()


def handler(user_id: int) -> str:
    user = find_user(user_id)
    return format_user_name(user)


print(handler(2))
```

Przykładowy traceback:

```text
Traceback (most recent call last):
  File "main.py", line 14, in <module>
    print(handler(2))
  File "main.py", line 11, in handler
    return format_user_name(user)
  File "main.py", line 7, in format_user_name
    return user["name"].upper()
TypeError: 'NoneType' object is not subscriptable
```

### Co tu jest ważne

Błąd wybucha w `format_user_name`, ale prawdziwy problem może siedzieć wcześniej:

- `find_user()` zwróciło `None`,
- `handler()` nie sprawdził tego przypadku,
- kontrakt między funkcjami był niepełny.

### Dobra lekcja

Miejsce eksplozji to nie zawsze najlepsze miejsce poprawki.

Czasem poprawka powinna wejść warstwę wyżej.

## Bardziej złożony traceback 3: błąd opakowany przez kilka warstw

W prawdziwych systemach bywa tak, że:

- jedna warstwa łapie wyjątek,
- opakowuje go,
- rzuca dalej z innym komunikatem.

To może utrudniać diagnozę, jeśli patrzysz tylko na ostatni wyjątek.

Wtedy szczególnie ważne jest:

- czytać cały łańcuch,
- rozumieć wcześniejsze ramki,
- sprawdzić, czy nie zgubiono oryginalnego kontekstu błędu.

## Checklist czytania tracebacka

1. Jaki jest końcowy typ wyjątku?
2. Na której linii bezpośrednio wybuchło?
3. Jakie funkcje prowadziły do tego miejsca?
4. Czy miejsce awarii jest też źródłem przyczyny?
5. Jakie dane weszły do tej ścieżki?
6. Czy problem siedzi niżej, czy wyżej w przepływie?

## Traceback i duże repo

W większym systemie traceback jest często najlepszym punktem wejścia do obcego kodu.

Zamiast czytać całe repo, możesz:

1. znaleźć końcowe miejsce awarii,
2. zobaczyć kilka ramek wyżej,
3. ustalić przepływ danych,
4. zawęzić obszar analizy.

To bardzo praktyczny sposób pracy.

## Typowe błędy początkujących

- panika na widok długiego tracebacka,
- czytanie go bez planu,
- ignorowanie ramek pośrednich,
- naprawianie miejsca eksplozji bez sprawdzenia źródła danych,
- traktowanie tracebacka jak przypadkowej ściany tekstu.

## Mini case study

Masz błąd `KeyError` w głębokiej warstwie serwisu.

Na końcu traceback pokazuje miejsce, gdzie zabrakło klucza. Ale ważniejsze pytanie może brzmieć:

- kto wcześniej zbudował ten słownik,
- i dlaczego zrobił to w złym kształcie.

Czyli traceback prowadzi Cię do miejsca awarii, ale Ty dalej musisz myśleć o przepływie.

## Szybka ściąga

- czytaj traceback od końca, ale analizuj cały przepływ,
- ostatnia linia mówi, jaki wyjątek wystąpił,
- wcześniejsze linie pokazują drogę dojścia,
- miejsce awarii nie zawsze jest miejscem prawdziwej przyczyny,
- traceback to świetny punkt startu do wejścia w obcy kod.

## Ćwiczenia

1. Napisz prosty program z `ZeroDivisionError` i opisz traceback.
2. Napisz przykład `ValueError` przechodzącego przez 3 funkcje.
3. Wskaż różnicę między miejscem eksplozji a źródłem problemu.
4. Weź traceback i opisz, od którego fragmentu zacząłbyś debugowanie.
5. Wymyśl przypadek, gdzie poprawka nie powinna być w ostatniej funkcji tracebacka.

## Najważniejsze do zapamiętania

- Traceback to mapa dojścia do błędu.
- Ostatnia linia mówi, co się stało, ale nie zawsze wyjaśnia pełną przyczynę.
- Trzeba patrzeć zarówno na miejsce awarii, jak i na przepływ prowadzący do niej.
- W dużym repo traceback bardzo pomaga zawęzić problem.
- Umiejętność czytania tracebacków to jedna z podstaw prawdziwego debugowania.
