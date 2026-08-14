# Dekoratory używane w frameworkach: FastAPI, Flask, pytest

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Dlaczego frameworki lubią dekoratory](#dlaczego-frameworki-lubią-dekoratory)
3. [Ogólna idea frameworkowego dekoratora](#ogólna-idea-frameworkowego-dekoratora)
4. [FastAPI](#fastapi)
5. [Flask](#flask)
6. [pytest](#pytest)
7. [Dekorator jako rejestracja](#dekorator-jako-rejestracja)
8. [Dekorator jako opis zachowania](#dekorator-jako-opis-zachowania)
9. [Dekoratory frameworkowe a zwykłe dekoratory](#dekoratory-frameworkowe-a-zwykłe-dekoratory)
10. [Najczęstsze wzorce](#najczęstsze-wzorce)
11. [Typowe błędy początkujących](#typowe-błędy-początkujących)
12. [Praktyczne przykłady](#praktyczne-przykłady)
13. [Dobre praktyki](#dobre-praktyki)
14. [Podsumowanie](#podsumowanie)
15. [Mini ściąga](#mini-ściąga)

---

## Wprowadzenie

Jeśli wejdziesz w świat frameworków Pythona, bardzo szybko zobaczysz dekoratory wszędzie.

Najczęściej:

- w web frameworkach,
- w testach,
- w narzędziach do walidacji i routingu.

Frameworki używają dekoratorów, bo to bardzo elegancki sposób oznaczania funkcji specjalną rolą.

---

## Dlaczego frameworki lubią dekoratory

Bo dekorator pozwala:

- zarejestrować funkcję,
- opisać ją metadanymi,
- owinąć ją dodatkową logiką,
- połączyć definicję funkcji z jej rolą w frameworku.

To bardzo czytelne.

---

## Ogólna idea frameworkowego dekoratora

W wielu frameworkach dekorator nie tylko opakowuje funkcję.

Często robi też coś jeszcze:

- zapisuje ją w rejestrze,
- wiąże z adresem URL,
- oznacza jako test,
- przypisuje dodatkowe informacje.

---

## FastAPI

W FastAPI dekoratory są bardzo ważne przy definiowaniu endpointów.

Przykład:

```python
@app.get("/users")
def get_users():
    return ["Ania", "Bartek"]
```

To oznacza:

- funkcja obsługuje żądanie `GET`,
- pod adresem `"/users"`.

Framework rejestruje tę funkcję jako endpoint.

Czyli dekorator nie tylko owija funkcję, ale też mówi frameworkowi:

"ta funkcja obsługuje konkretną trasę".

---

## Flask

W Flask działa to bardzo podobnie:

```python
@app.route("/")
def home():
    return "Hello"
```

albo:

```python
@app.get("/items")
def items():
    return "Items"
```

Dekorator łączy funkcję z trasą.

To dlatego po uruchomieniu aplikacji framework wie, którą funkcję wywołać dla danego adresu.

---

## pytest

W `pytest` dekoratory często służą do:

- oznaczania testów,
- parametryzacji,
- markerów.

Przykład:

```python
@pytest.mark.slow
def test_big_thing():
    ...
```

albo:

```python
@pytest.mark.parametrize("a,b,wynik", [
    (1, 2, 3),
    (2, 3, 5),
])
def test_dodaj(a, b, wynik):
    assert a + b == wynik
```

To pokazuje, że dekorator może dodawać nie tylko logikę, ale też opis testu.

W `pytest` dekorator bardzo często nie zmienia samego zachowania funkcji w prosty sposób, tylko przekazuje informacje do silnika testów.

---

## Dekorator jako rejestracja

To bardzo częsty wzorzec frameworkowy.

Funkcja jest:

- zapisana w jakimś rejestrze,
- oznaczona metadanymi,
- odnajdywana później przez framework.

To ważne, bo pomaga zrozumieć, że frameworkowy dekorator często działa szerzej niż zwykły wrapper.

Uproszczona symulacja:

```python
routes = {}

def route(path):
    def dekorator(f):
        routes[path] = f
        return f
    return dekorator

@route("/hello")
def hello():
    return "Hello"

print(routes["/hello"]())
```

Wynik:

```python
Hello
```

---

## Dekorator jako opis zachowania

Czasem dekorator mówi:

- „ta funkcja to endpoint”,
- „ta funkcja to test slow”,
- „ta funkcja ma być cache’owana”,
- „ta funkcja ma specjalne uprawnienia”.

To bardzo deklaratywny styl programowania.

Zamiast pisać osobno:

- "dodaj tę funkcję do rejestru",
- "oznacz ją jako endpoint",
- "połącz ją z trasą",

opisujesz to bezpośrednio nad definicją funkcji.

---

## Dekoratory frameworkowe a zwykłe dekoratory

### Zwykły dekorator

Najczęściej owija funkcję i zmienia jej zachowanie.

### Frameworkowy dekorator

Często dodatkowo:

- rejestruje funkcję,
- zapisuje metadane,
- integruje ją z całym systemem frameworka.

---

## Najczęstsze wzorce

- routing,
- parametryzacja testów,
- rejestracja handlerów,
- autoryzacja,
- walidacja,
- cache.

---

## Typowe błędy początkujących

- myślenie, że dekorator frameworkowy tylko wypisuje coś przed funkcją,
- brak zrozumienia, że dekorator może rejestrować funkcję w systemie,
- kopiowanie dekoratorów bez rozumienia ich roli,
- mylenie kolejności wielu dekoratorów.

---

## Praktyczne przykłady

### FastAPI

```python
@app.get("/ping")
def ping():
    return {"status": "ok"}
```

Efekt praktyczny:

żądanie `GET /ping` trafi do funkcji `ping`.

### Flask

```python
@app.route("/hello")
def hello():
    return "Hello"
```

Efekt praktyczny:

wejście na trasę `/hello` uruchomi funkcję `hello`.

### pytest

```python
@pytest.mark.parametrize("x", [1, 2, 3])
def test_positive(x):
    assert x > 0
```

Efekt praktyczny:

`pytest` uruchomi ten test kilka razy, podstawiając kolejne wartości `x`.

### Uproszczony własny przykład rejestracji

```python
commands = {}

def command(name):
    def dekorator(f):
        commands[name] = f
        return f
    return dekorator

@command("start")
def start():
    return "Program uruchomiony"

print(commands["start"]())
```

Wynik:

```python
Program uruchomiony
```

---

## Dobre praktyki

- czytaj dokumentację konkretnego frameworka,
- rozumiej, co dekorator robi poza samym wrapperem,
- nie traktuj wszystkich dekoratorów frameworkowych jak zwykłych dekoratorów użytkownika,
- zwracaj uwagę na kolejność dekoratorów.

Praktyczna zasada:

w frameworkach pytaj nie tylko "co ten dekorator robi z funkcją?",

ale też "co rejestruje, opisuje albo przekazuje do systemu?".

Druga praktyczna zasada:

jeśli nie rozumiesz frameworkowego dekoratora, spróbuj najpierw wyobrazić go sobie jako:

- wpis do słownika,
- dopisanie metadanych,
- prosty mechanizm rejestracji funkcji.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- frameworki bardzo często używają dekoratorów,
- dekorator może służyć do rejestracji funkcji, nie tylko jej owinięcia,
- w FastAPI i Flask dekoratory często definiują routing,
- w pytest dekoratory często opisują i konfigurują testy.

Najważniejsze do zapamiętania:

- frameworkowy dekorator bardzo często działa szerzej niż zwykły wrapper,
- może budować rejestr, routing albo konfigurację testów,
- dlatego dekoratory są tak ważne w nowoczesnym Pythonie.

---

## Mini ściąga

### FastAPI

```python
@app.get("/path")
```

### Flask

```python
@app.route("/path")
```

### pytest

```python
@pytest.mark.parametrize(...)
@pytest.mark.slow
```
