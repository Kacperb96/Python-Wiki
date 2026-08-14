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

---

## Dekorator jako rejestracja

To bardzo częsty wzorzec frameworkowy.

Funkcja jest:

- zapisana w jakimś rejestrze,
- oznaczona metadanymi,
- odnajdywana później przez framework.

To ważne, bo pomaga zrozumieć, że frameworkowy dekorator często działa szerzej niż zwykły wrapper.

---

## Dekorator jako opis zachowania

Czasem dekorator mówi:

- „ta funkcja to endpoint”,
- „ta funkcja to test slow”,
- „ta funkcja ma być cache’owana”,
- „ta funkcja ma specjalne uprawnienia”.

To bardzo deklaratywny styl programowania.

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

### Flask

```python
@app.route("/hello")
def hello():
    return "Hello"
```

### pytest

```python
@pytest.mark.parametrize("x", [1, 2, 3])
def test_positive(x):
    assert x > 0
```

---

## Dobre praktyki

- czytaj dokumentację konkretnego frameworka,
- rozumiej, co dekorator robi poza samym wrapperem,
- nie traktuj wszystkich dekoratorów frameworkowych jak zwykłych dekoratorów użytkownika,
- zwracaj uwagę na kolejność dekoratorów.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- frameworki bardzo często używają dekoratorów,
- dekorator może służyć do rejestracji funkcji, nie tylko jej owinięcia,
- w FastAPI i Flask dekoratory często definiują routing,
- w pytest dekoratory często opisują i konfigurują testy.

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
