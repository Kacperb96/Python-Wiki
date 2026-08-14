# SQL dla Pythonowca — podstawy

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co Pythonowcowi SQL](#po-co-pythonowcowi-sql)
3. [Tabela, wiersz, kolumna](#tabela-wiersz-kolumna)
4. [`SELECT`](#select)
5. [`INSERT`](#insert)
6. [`UPDATE`](#update)
7. [`DELETE`](#delete)
8. [`WHERE`, `ORDER BY`, `LIMIT`](#where-order-by-limit)
9. [Klucz główny](#klucz-główny)
10. [JOIN — po co istnieje](#join--po-co-istnieje)
11. [Typowe błędy początkujących](#typowe-błędy-początkujących)
12. [Praktyczne przykłady](#praktyczne-przykłady)
13. [Dobre praktyki](#dobre-praktyki)
14. [Podsumowanie](#podsumowanie)
15. [Mini ściąga](#mini-ściąga)
16. [Ćwiczenia](#ćwiczenia)
17. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Nawet jeśli korzystasz z ORM, jako profesjonalny Pythonowiec musisz znać podstawy SQL.

Bez tego trudno:

- dobrze rozumieć bazę,
- debugować zapytania,
- projektować warstwę danych,
- rozumieć wydajność.

---

## Po co Pythonowcowi SQL

Bo większość realnych aplikacji prędzej czy później dotyka bazy danych.

Znajomość SQL daje przewagę nawet wtedy, gdy używasz warstwy abstrakcji.

---

## Tabela, wiersz, kolumna

Tabela przechowuje dane.

Wiersz to pojedynczy rekord.

Kolumna opisuje pole, np.:

- `id`
- `name`
- `email`

---

## `SELECT`

Pobieranie danych:

```sql
SELECT id, name FROM users;
```

To najczęściej używana operacja.

---

## `INSERT`

Dodawanie rekordu:

```sql
INSERT INTO users (name, email)
VALUES ('Anna', 'anna@example.com');
```

---

## `UPDATE`

Aktualizacja:

```sql
UPDATE users
SET email = 'nowy@example.com'
WHERE id = 1;
```

---

## `DELETE`

Usuwanie:

```sql
DELETE FROM users
WHERE id = 1;
```

---

## `WHERE`, `ORDER BY`, `LIMIT`

Filtrowanie:

```sql
SELECT * FROM users WHERE active = 1;
```

Sortowanie:

```sql
SELECT * FROM users ORDER BY created_at DESC;
```

Ograniczenie:

```sql
SELECT * FROM users LIMIT 10;
```

---

## Klucz główny

`PRIMARY KEY` identyfikuje rekord jednoznacznie.

Najczęściej jest to `id`.

To bardzo ważny element modelu danych.

---

## JOIN — po co istnieje

`JOIN` łączy dane z kilku tabel.

Na przykład:

- użytkownicy,
- zamówienia,
- produkty.

Bez zrozumienia joinów trudno budować realne systemy.

---

## Typowe błędy początkujących

- brak `WHERE` przy `UPDATE` lub `DELETE`,
- brak rozumienia relacji między tabelami,
- traktowanie ORM jak zamiennika myślenia o SQL,
- ignorowanie sortowania i limitowania wyników.

---

## Praktyczne przykłady

### Pobranie jednego użytkownika

```sql
SELECT id, name, email
FROM users
WHERE id = 1;
```

### Najnowsze rekordy

```sql
SELECT *
FROM orders
ORDER BY created_at DESC
LIMIT 5;
```

---

## Dobre praktyki

- ucz się SQL równolegle z Pythonem backendowym,
- zawsze myśl, co robi `WHERE`,
- rozumiej, skąd biorą się rekordy po joinie,
- nie polegaj wyłącznie na ORM bez znajomości podstaw.

---

## Podsumowanie

SQL to nie opcjonalny dodatek, tylko ważna kompetencja backendowego Pythonowca.

Nawet podstawowa swoboda w SQL bardzo poprawia jakość pracy z danymi.

---

## Mini ściąga

Najważniejsze:

- `SELECT` pobiera,
- `INSERT` dodaje,
- `UPDATE` zmienia,
- `DELETE` usuwa,
- `WHERE` filtruje,
- `ORDER BY` sortuje,
- `LIMIT` ogranicza wynik.

---

## Ćwiczenia

1. Napisz `SELECT` pobierający `id` i `name` z tabeli `users`.
2. Napisz `INSERT` dodający użytkownika.
3. Napisz `UPDATE` zmieniający email użytkownika.
4. Napisz `DELETE` usuwający rekord po `id`.
5. Napisz `SELECT` z `ORDER BY` i `LIMIT`.

---

## Przykładowe rozwiązania

### 1. `SELECT`

```sql
SELECT id, name FROM users;
```

### 2. `INSERT`

```sql
INSERT INTO users (name) VALUES ('Ola');
```

### 3. `UPDATE`

```sql
UPDATE users SET email = 'ola@example.com' WHERE id = 1;
```

### 4. `DELETE`

```sql
DELETE FROM users WHERE id = 1;
```

### 5. Sortowanie i limit

```sql
SELECT * FROM users ORDER BY id DESC LIMIT 5;
```
