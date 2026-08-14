# `sqlite3` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest SQLite](#czym-jest-sqlite)
3. [Po co znać `sqlite3`](#po-co-znać-sqlite3)
4. [Połączenie z bazą](#połączenie-z-bazą)
5. [Cursor i zapytania](#cursor-i-zapytania)
6. [Tworzenie tabeli](#tworzenie-tabeli)
7. [INSERT i SELECT](#insert-i-select)
8. [Parametryzacja zapytań](#parametryzacja-zapytań)
9. [`commit()` i zapis zmian](#commit-i-zapis-zmian)
10. [Typowe błędy początkujących](#typowe-błędy-początkujących)
11. [Praktyczne przykłady](#praktyczne-przykłady)
12. [Dobre praktyki](#dobre-praktyki)
13. [Podsumowanie](#podsumowanie)
14. [Mini ściąga](#mini-ściąga)
15. [Ćwiczenia](#ćwiczenia)
16. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`sqlite3` to wbudowany moduł Pythona do pracy z bazą SQLite.

To świetny punkt wejścia do nauki pracy z bazami danych bez instalowania osobnego serwera.

---

## Czym jest SQLite

SQLite to lekka baza danych zapisywana zwykle w pojedynczym pliku.

Jest bardzo wygodna do:

- nauki,
- małych aplikacji,
- prototypów,
- lokalnych narzędzi.

---

## Po co znać `sqlite3`

Bo uczy podstaw pracy z bazą:

- połączenie,
- zapytania SQL,
- zapis danych,
- odczyt danych,
- parametryzacja.

To świetna baza pod dalszą naukę SQLAlchemy i większych baz.

---

## Połączenie z bazą

```python
import sqlite3

conn = sqlite3.connect("app.db")
```

To tworzy lub otwiera plik bazy danych.

---

## Cursor i zapytania

```python
cursor = conn.cursor()
```

Kursor służy do wykonywania zapytań SQL.

---

## Tworzenie tabeli

```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
""")
```

---

## INSERT i SELECT

Wstawianie:

```python
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Anna",))
```

Odczyt:

```python
cursor.execute("SELECT id, name FROM users")
rows = cursor.fetchall()
print(rows)
```

---

## Parametryzacja zapytań

To bardzo ważne.

Używaj parametrów:

```python
cursor.execute("SELECT * FROM users WHERE name = ?", ("Anna",))
```

Nie sklejaj SQL ręcznie ze stringów użytkownika.

---

## `commit()` i zapis zmian

Po zmianach w danych zwykle trzeba zatwierdzić transakcję:

```python
conn.commit()
```

Na końcu warto też zamknąć połączenie:

```python
conn.close()
```

---

## Typowe błędy początkujących

- brak `commit()`,
- ręczne sklejanie zapytań SQL,
- brak zamknięcia połączenia,
- mieszanie logiki aplikacji i SQL bez porządku.

---

## Praktyczne przykłady

### Prosta baza użytkowników

```python
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
""")

cursor.execute("INSERT INTO users (name) VALUES (?)", ("Ola",))
conn.commit()
```

### Odczyt danych

```python
cursor.execute("SELECT id, name FROM users")
for row in cursor.fetchall():
    print(row)
```

---

## Dobre praktyki

- ucz się parametryzowanych zapytań od początku,
- jawnie zarządzaj `commit`,
- utrzymuj porządek między warstwą bazy i logiką aplikacji,
- traktuj SQLite jako świetne narzędzie nauki i małych projektów.

---

## Podsumowanie

`sqlite3` to bardzo dobry pierwszy krok w stronę pracy z bazami danych w Pythonie.

Daje praktyczne zrozumienie SQL i przygotowuje pod bardziej zaawansowane narzędzia.

---

## Mini ściąga

```python
import sqlite3

conn = sqlite3.connect("app.db")
cursor = conn.cursor()
cursor.execute("SELECT 1")
conn.close()
```

Najważniejsze:

- `connect()` otwiera bazę,
- `cursor()` wykonuje zapytania,
- `commit()` zapisuje zmiany,
- używaj parametrów `?` zamiast sklejania SQL.

---

## Ćwiczenia

1. Utwórz bazę `app.db`.
2. Utwórz tabelę `users`.
3. Dodaj jednego użytkownika.
4. Odczytaj wszystkich użytkowników.
5. Wyszukaj użytkownika po imieniu przez parametr zapytania.

---

## Przykładowe rozwiązania

### 1. Baza

```python
import sqlite3

conn = sqlite3.connect("app.db")
```

### 2. Tabela

```python
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
```

### 3. Dodanie użytkownika

```python
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Anna",))
conn.commit()
```

### 4. Odczyt

```python
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())
```

### 5. Parametr

```python
cursor.execute("SELECT * FROM users WHERE name = ?", ("Anna",))
print(cursor.fetchall())
```
