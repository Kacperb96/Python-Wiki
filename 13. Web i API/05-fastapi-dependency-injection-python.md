# FastAPI w Pythonie — dependency injection

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest dependency injection](#czym-jest-dependency-injection)
3. [Po co FastAPI używa zależności](#po-co-fastapi-używa-zależności)
4. [`Depends`](#depends)
5. [Typowe zastosowania](#typowe-zastosowania)
6. [Zależności a testowalność](#zależności-a-testowalność)
7. [Zależności a autoryzacja](#zależności-a-autoryzacja)
8. [Zależności a baza danych](#zależności-a-baza-danych)
9. [Przykład z outputem](#przykład-z-outputem)
10. [Typowe błędy początkujących](#typowe-błędy-początkujących)
11. [Praktyczna ściąga](#praktyczna-ściąga)
12. [Ćwiczenia](#ćwiczenia)
13. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

Dependency injection w FastAPI to mechanizm, który bardzo pomaga utrzymać porządek w większych aplikacjach.

Pozwala dostarczać potrzebne zależności do endpointów w kontrolowany sposób.

---

## Czym jest dependency injection

W uproszczeniu:

zamiast tworzyć wszystko ręcznie w środku funkcji, deklarujesz, czego potrzebujesz, a framework dostarcza Ci tę wartość.

To poprawia:

- testowalność,
- czytelność,
- separację odpowiedzialności.

---

## Po co FastAPI używa zależności

Bo endpointy często potrzebują:

- aktualnego użytkownika,
- sesji bazy danych,
- konfiguracji,
- wspólnej logiki requestowej,
- walidacji tokenu.

Zależności pozwalają obsłużyć to elegancko i powtarzalnie.

---

## `Depends`

Podstawowy mechanizm FastAPI:

```python
from fastapi import Depends
```

Przykład:

```python
from fastapi import Depends, FastAPI

app = FastAPI()


def get_settings():
    return {"debug": True}


@app.get("/info")
def info(settings=Depends(get_settings)):
    return settings
```

Mentalny model:

endpoint deklaruje, czego potrzebuje, a framework dostarcza tę wartość.

---

## Typowe zastosowania

Najczęściej dependency injection używa się do:

- sesji bazy danych,
- autoryzacji,
- wspólnej logiki requestowej,
- konfiguracji per request.

---

## Zależności a testowalność

To bardzo duża zaleta.

Jeśli zależność jest jawna i wydzielona, dużo łatwiej:

- podmienić ją w testach,
- zamockować,
- kontrolować zachowanie endpointu.

To jeden z powodów, dla których DI jest tak przydatne w backendzie.

---

## Zależności a autoryzacja

FastAPI bardzo często wykorzystuje zależności do pobierania aktualnego użytkownika albo sprawdzania uprawnień.

To naturalny wzorzec, bo endpoint może po prostu zadeklarować:

- potrzebuję aktualnego użytkownika,
- potrzebuję administratora,
- potrzebuję poprawnego tokenu.

---

## Zależności a baza danych

Bardzo częsty przypadek:

endpoint potrzebuje sesji bazy danych.

Lepiej dostać ją przez zależność niż tworzyć ją ręcznie w każdej funkcji.

To ogranicza chaos i ułatwia testy.

---

## Przykład z outputem

```python
from fastapi import Depends, FastAPI

app = FastAPI()


def get_settings():
    return {"debug": True, "env": "dev"}


@app.get("/info")
def info(settings=Depends(get_settings)):
    return settings
```

Przykładowa odpowiedź HTTP:

```json
{"debug": true, "env": "dev"}
```

To prosty przykład, ale dobrze pokazuje mechanikę działania.

---

## Typowe błędy początkujących

- tworzenie wszystkiego bezpośrednio w endpointach,
- brak wydzielonych zależności,
- zbyt ciężkie zależności robiące wiele rzeczy naraz,
- mieszanie DI z globalnym stanem bez planu,
- traktowanie zależności jak miejsca na całą logikę biznesową.

---

## Praktyczna ściąga

### Prosta zależność

```python
def get_settings():
    return {"debug": True}
```

### Użycie

```python
def info(settings=Depends(get_settings)):
    return settings
```

### Typowe wzorce

- `get_db`,
- `get_current_user`,
- `get_settings`.

---

## Ćwiczenia

1. Napisz zależność `get_settings`.
2. Dodaj ją do prostego endpointu.
3. Napisz uproszczoną zależność `get_current_user`.
4. Zastanów się, jakie obiekty w backendzie warto dostarczać przez `Depends`.
5. Wyjaśnij własnymi słowami, czemu DI poprawia testowalność.

---

## Najważniejsze do zapamiętania

- Dependency injection pomaga utrzymać porządek w backendzie.
- FastAPI używa `Depends`, żeby dostarczać potrzebne obiekty do endpointów.
- DI poprawia testowalność, czytelność i separację odpowiedzialności.
- Najczęstsze zastosowania to użytkownik, baza i konfiguracja.
