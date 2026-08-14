# `json` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest JSON](#czym-jest-json)
3. [Po co używać modułu `json`](#po-co-używać-modułu-json)
4. [`dumps()` i `loads()`](#dumps-i-loads)
5. [`dump()` i `load()`](#dump-i-load)
6. [Python a typy JSON](#python-a-typy-json)
7. [Ładny zapis przez `indent`](#ładny-zapis-przez-indent)
8. [Obsługa znaków narodowych](#obsługa-znaków-narodowych)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczne przykłady](#praktyczne-przykłady)
11. [Dobre praktyki](#dobre-praktyki)
12. [Podsumowanie](#podsumowanie)
13. [Mini ściąga](#mini-ściąga)
14. [Ćwiczenia](#ćwiczenia)
15. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`json` to standardowy moduł Pythona do pracy z formatem JSON.

JSON jest bardzo popularny przy:

- API,
- plikach konfiguracyjnych,
- wymianie danych,
- zapisie prostych struktur.

---

## Czym jest JSON

JSON to tekstowy format danych.

Przykład:

```json
{"name": "Anna", "age": 30}
```

Jest czytelny dla ludzi i wygodny dla programów.

---

## Po co używać modułu `json`

Moduł `json` pozwala:

- zamienić obiekty Pythona na JSON,
- wczytać JSON do struktur Pythona,
- zapisywać dane do plików,
- czytać dane z plików.

---

## `dumps()` i `loads()`

`dumps()` zamienia obiekt Pythona na string JSON:

```python
import json

dane = {"name": "Anna", "age": 30}
tekst = json.dumps(dane)
print(tekst)
```

Wynik:

```python
{"name": "Anna", "age": 30}
```

`loads()` robi odwrotnie:

```python
obiekt = json.loads(tekst)
print(obiekt)
```

Wynik:

```python
{'name': 'Anna', 'age': 30}
```

---

## `dump()` i `load()`

Do pracy z plikami:

```python
import json

dane = {"name": "Anna", "age": 30}

with open("user.json", "w", encoding="utf-8") as f:
    json.dump(dane, f)
```

Odczyt:

```python
with open("user.json", "r", encoding="utf-8") as f:
    dane = json.load(f)
```

Po odczycie `dane` będzie zwykłym obiektem Pythona, np. słownikiem.

---

## Python a typy JSON

Najczęstsze mapowanie:

- `dict` -> obiekt JSON,
- `list` -> tablica JSON,
- `str` -> string,
- `int`, `float` -> liczby,
- `True`, `False` -> `true`, `false`,
- `None` -> `null`.

---

## Ładny zapis przez `indent`

```python
import json

dane = {"name": "Anna", "skills": ["Python", "SQL"]}
print(json.dumps(dane, indent=2))
```

To bardzo pomaga przy debugowaniu i plikach konfiguracyjnych.

Wynik:

```python
{
  "name": "Anna",
  "skills": [
    "Python",
    "SQL"
  ]
}
```

---

## Obsługa znaków narodowych

Domyślnie JSON może escapować znaki.

Jeśli chcesz czytelny polski tekst:

```python
import json

dane = {"miasto": "Łódź"}
print(json.dumps(dane, ensure_ascii=False))
```

Wynik:

```python
{"miasto": "Łódź"}
```

---

## Typowe błędy początkujących

- mylenie `dump()` z `dumps()`,
- mylenie `load()` z `loads()`,
- brak `encoding="utf-8"` przy plikach,
- próba serializacji obiektów niestandardowych bez dodatkowej obsługi.

### 5. Zakładanie, że każdy obiekt Pythona da się od razu zapisać do JSON

Na przykład obiekty własnych klas zwykle wymagają dodatkowej konwersji.

---

## Praktyczne przykłady

### Zapis konfiguracji

```python
import json

config = {"debug": True, "port": 8000}

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=2)
```

Efekt w pliku:

```json
{
  "debug": true,
  "port": 8000
}
```

### Odczyt JSON z tekstu

```python
import json

tekst = '{"name": "Jan", "age": 25}'
dane = json.loads(tekst)
print(dane["name"])
```

Wynik:

```python
Jan
```

---

## Dobre praktyki

- do debugowania używaj `indent`,
- przy polskim tekście ustawiaj `ensure_ascii=False`,
- waliduj strukturę po wczytaniu, jeśli dane przychodzą z zewnątrz,
- pamiętaj, że nie każdy obiekt Pythona da się łatwo zapisać do JSON.

Praktyczna zasada:

zawsze myśl osobno:

- czy pracujesz na stringu JSON,
- czy na pliku JSON.

---

## Podsumowanie

`json` to jeden z najczęściej używanych modułów w codziennej pracy.

Warto swobodnie rozróżniać:

- string vs plik,
- `dumps` vs `dump`,
- `loads` vs `load`.

Najważniejsze do zapamiętania:

- `dumps` i `loads` działają na stringach,
- `dump` i `load` działają na plikach,
- `indent` i `ensure_ascii=False` bardzo poprawiają praktyczną użyteczność JSON-a.

---

## Mini ściąga

```python
import json

tekst = json.dumps({"x": 1}, indent=2)
dane = json.loads(tekst)
```

Najważniejsze:

- `dumps()` i `loads()` działają na stringach,
- `dump()` i `load()` działają na plikach,
- `indent` poprawia czytelność,
- `ensure_ascii=False` pomaga przy polskich znakach.

---

## Ćwiczenia

1. Zamień słownik na string JSON.
2. Wczytaj JSON ze stringa.
3. Zapisz listę użytkowników do pliku JSON.
4. Odczytaj dane z pliku JSON.
5. Wypisz JSON w ładnym formacie.

---

## Przykładowe rozwiązania

### 1. Słownik na JSON

```python
import json

print(json.dumps({"name": "Ola"}))
```

### 2. JSON ze stringa

```python
import json

print(json.loads('{"x": 10}'))
```

### 3. Zapis listy

```python
import json

users = [{"name": "Ala"}, {"name": "Jan"}]

with open("users.json", "w", encoding="utf-8") as f:
    json.dump(users, f, ensure_ascii=False, indent=2)
```

### 4. Odczyt pliku

```python
import json

with open("users.json", "r", encoding="utf-8") as f:
    print(json.load(f))
```

### 5. Ładny format

```python
import json

print(json.dumps({"a": 1, "b": 2}, indent=2))
```
