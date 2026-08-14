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
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczne przykłady](#praktyczne-przykłady)
11. [Dobre praktyki](#dobre-praktyki)
12. [Podsumowanie](#podsumowanie)
13. [Mini ściąga](#mini-ściąga)
14. [Ćwiczenia](#ćwiczenia)
15. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Dependency injection w FastAPI to jeden z mechanizmów, który bardzo pomaga utrzymać porządek w większych aplikacjach.

Pozwala dostarczać potrzebne zależności do endpointów w kontrolowany sposób.

---

## Czym jest dependency injection

W uproszczeniu:

zamiast tworzyć wszystko ręcznie w środku funkcji, przekazujesz lub dostarczasz potrzebne obiekty z zewnątrz.

To poprawia:

- testowalność,
- czytelność,
- separację odpowiedzialności.

---

## Po co FastAPI używa zależności

Bo endpointy często potrzebują:

- aktualnego użytkownika,
- połączenia lub sesji bazy,
- konfiguracji,
- walidacji tokenu.

Zależności pozwalają obsłużyć to elegancko.

---

## `Depends`

Podstawowy mechanizm FastAPI:

```python
from fastapi import Depends
```

Przykład mentalny:

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

---

## Zależności a autoryzacja

FastAPI często wykorzystuje zależności do pobierania aktualnego użytkownika lub sprawdzania uprawnień.

To naturalny i czytelny wzorzec.

---

## Zależności a baza danych

Bardzo częsty przypadek:

endpoint potrzebuje sesji bazy danych.

Lepiej dostać ją przez zależność niż tworzyć "na dziko" w każdej funkcji.

---

## Typowe błędy początkujących

- tworzenie wszystkiego bezpośrednio w endpointach,
- brak wydzielonych zależności,
- zbyt ciężkie zależności robiące wiele rzeczy naraz,
- mieszanie DI z globalnym stanem bez planu.

---

## Praktyczne przykłady

### Prosta zależność

```python
from fastapi import Depends, FastAPI

app = FastAPI()

def get_settings():
    return {"debug": True}

@app.get("/info")
def info(settings=Depends(get_settings)):
    return settings
```

### Mentalny wzorzec

- `get_db`
- `get_current_user`
- `get_settings`

---

## Dobre praktyki

- utrzymuj zależności małe i czytelne,
- używaj ich do współdzielonych potrzeb,
- nie pakuj całej logiki biznesowej do funkcji zależności,
- projektuj je tak, by łatwo było je podmieniać w testach.

---

## Podsumowanie

Dependency injection w FastAPI to bardzo praktyczny mechanizm, który pomaga budować czystsze i bardziej testowalne API.

W większych aplikacjach to jedna z rzeczy, które naprawdę robią różnicę.

---

## Mini ściąga

```python
from fastapi import Depends
```

Najważniejsze:

- zależności dostarczają wspólne obiekty lub logikę,
- `Depends` jest podstawowym mechanizmem,
- DI poprawia testowalność i organizację kodu.

---

## Ćwiczenia

1. Wyjaśnij, czym jest dependency injection.
2. Podaj przykład zależności dla sesji bazy.
3. Podaj przykład zależności dla aktualnego użytkownika.
4. Wyjaśnij, czemu DI poprawia testowalność.
5. Wyjaśnij, czemu nie warto tworzyć sesji bazy osobno w każdym endpointzie.

---

## Przykładowe rozwiązania

### 1. DI

To sposób dostarczania potrzebnych obiektów i usług z zewnątrz zamiast tworzenia ich ręcznie w środku funkcji.

### 2. Sesja bazy

Na przykład funkcja `get_db`, która zwraca sesję.

### 3. Użytkownik

Na przykład funkcja `get_current_user`.

### 4. Testowalność

Bo zależności łatwiej podmieniać i mockować.

### 5. Czemu nie tworzyć w każdym endpointzie

Bo prowadzi to do duplikacji i gorszej kontroli nad cyklem życia zasobów.
