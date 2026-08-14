# `configparser` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest `configparser`](#czym-jest-configparser)
3. [Po co używać plików konfiguracyjnych](#po-co-używać-plików-konfiguracyjnych)
4. [Format INI](#format-ini)
5. [Odczyt konfiguracji](#odczyt-konfiguracji)
6. [Sekcje i klucze](#sekcje-i-klucze)
7. [Zapis konfiguracji](#zapis-konfiguracji)
8. [Typowe błędy początkujących](#typowe-błędy-początkujących)
9. [Praktyczne przykłady](#praktyczne-przykłady)
10. [Dobre praktyki](#dobre-praktyki)
11. [Podsumowanie](#podsumowanie)
12. [Mini ściąga](#mini-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`configparser` to moduł do pracy z prostymi plikami konfiguracyjnymi w stylu INI.

To przydatne w mniejszych narzędziach i skryptach.

---

## Czym jest `configparser`

Pozwala:

- czytać konfigurację,
- zapisywać konfigurację,
- pracować z sekcjami i kluczami.

---

## Po co używać plików konfiguracyjnych

Bo nie wszystko powinno być zahardkodowane w kodzie.

Konfiguracja pozwala oddzielić:

- logikę programu,
- ustawienia środowiska,
- parametry działania.

---

## Format INI

Przykład:

```ini
[app]
debug = true
port = 8000
```

To prosty i czytelny format.

---

## Odczyt konfiguracji

```python
import configparser

config = configparser.ConfigParser()
config.read("settings.ini", encoding="utf-8")

print(config["app"]["port"])
```

---

## Sekcje i klucze

Sekcje grupują ustawienia:

```ini
[database]
host = localhost
port = 5432
```

W Pythonie:

```python
host = config["database"]["host"]
```

---

## Zapis konfiguracji

```python
import configparser

config = configparser.ConfigParser()
config["app"] = {"debug": "true", "port": "8000"}

with open("settings.ini", "w", encoding="utf-8") as f:
    config.write(f)
```

---

## Typowe błędy początkujących

- trzymanie wszystkiego w kodzie zamiast w konfiguracji,
- oczekiwanie, że wartości będą automatycznie typami innymi niż string,
- brak sprawdzania, czy sekcja i klucz istnieją,
- używanie `configparser` tam, gdzie lepiej pasuje JSON lub env vars.

---

## Praktyczne przykłady

### Prosta konfiguracja aplikacji

```ini
[app]
name = Raporty
debug = true
```

### Odczyt

```python
import configparser

config = configparser.ConfigParser()
config.read("app.ini", encoding="utf-8")
print(config["app"]["name"])
```

---

## Dobre praktyki

- używaj `configparser` do prostych konfiguracji,
- pamiętaj, że wiele wartości czytasz jako tekst,
- rozważ, czy dany projekt lepiej pasuje do INI, JSON czy env vars,
- trzymaj konfigurację poza kodem logiki.

---

## Podsumowanie

`configparser` to proste i praktyczne narzędzie do konfiguracji w mniejszych projektach Python.

Warto je znać, nawet jeśli w większych systemach częściej pojawią się inne podejścia.

---

## Mini ściąga

```python
import configparser

config = configparser.ConfigParser()
config.read("settings.ini", encoding="utf-8")
```

Najważniejsze:

- pracuje z plikami INI,
- używa sekcji i kluczy,
- dobrze sprawdza się w prostych konfiguracjach.

---

## Ćwiczenia

1. Utwórz plik INI z sekcją `app`.
2. Odczytaj wartość `port`.
3. Dodaj sekcję `database`.
4. Zapisz konfigurację z poziomu Pythona.
5. Wyjaśnij, kiedy lepiej użyć env vars zamiast pliku INI.

---

## Przykładowe rozwiązania

### 1. Plik INI

```ini
[app]
port = 8000
```

### 2. Odczyt

```python
print(config["app"]["port"])
```

### 3. `database`

```ini
[database]
host = localhost
```

### 4. Zapis

```python
config["app"] = {"debug": "true"}
```

### 5. Kiedy env vars

Gdy ustawienia zależą od środowiska wdrożeniowego albo zawierają sekrety.
