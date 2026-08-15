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
9. [Klucz główny i klucz obcy](#klucz-główny-i-klucz-obcy)
10. [JOIN — po co istnieje](#join--po-co-istnieje)
11. [Przykład z outputem](#przykład-z-outputem)
12. [Typowe błędy początkujących](#typowe-błędy-początkujących)
13. [Praktyczna ściąga](#praktyczna-ściąga)
14. [Ćwiczenia](#ćwiczenia)
15. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

Nawet jeśli korzystasz z ORM, jako profesjonalny Pythonowiec musisz znać podstawy SQL.

Bez tego trudno:

- dobrze rozumieć bazę,
- debugować zapytania,
- projektować warstwę danych,
- rozumieć wydajność,
- czytać logi i wygenerowany SQL.

---

## Po co Pythonowcowi SQL

Bo większość realnych aplikacji prędzej czy później dotyka bazy danych.

Znajomość SQL daje przewagę nawet wtedy, gdy używasz warstwy abstrakcji.

ORM może pomóc pisać kod, ale nie zastąpi rozumienia, co naprawdę dzieje się po stronie bazy.

---

## Tabela, wiersz, kolumna

Tabela przechowuje dane.

Wiersz to pojedynczy rekord.

Kolumna opisuje pole, np.:

- `id`,
- `name`,
- `email`.

To najprostszy mentalny model relacyjnej bazy danych.

---

## `SELECT`

Pobieranie danych:

```sql
SELECT id, name FROM users;
```

To najczęściej używana operacja.

Jeśli chcesz wszystkie kolumny:

```sql
SELECT * FROM users;
```

Ale w praktyce często lepiej pobierać tylko to, czego naprawdę potrzebujesz.

---

## `INSERT`

Dodawanie rekordu:

```sql
INSERT INTO users (name, email)
VALUES ('Anna', 'anna@example.com');
```

To tworzy nowy rekord w tabeli `users`.

---

## `UPDATE`

Aktualizacja:

```sql
UPDATE users
SET email = 'nowy@example.com'
WHERE id = 1;
```

To bardzo ważne:

`WHERE` decyduje, które rekordy zmieniasz.

---

## `DELETE`

Usuwanie:

```sql
DELETE FROM users
WHERE id = 1;
```

Tak samo jak przy `UPDATE`, brak `WHERE` może mieć bardzo niebezpieczny skutek.

---

## `WHERE`, `ORDER BY`, `LIMIT`

### Filtrowanie

```sql
SELECT * FROM users WHERE active = 1;
```

### Sortowanie

```sql
SELECT * FROM users ORDER BY created_at DESC;
```

### Ograniczenie wyniku

```sql
SELECT * FROM users LIMIT 10;
```

To bardzo codzienne elementy praktycznej pracy z SQL.

---

## Klucz główny i klucz obcy

### Klucz główny

`PRIMARY KEY` identyfikuje rekord jednoznacznie.

Najczęściej jest to `id`.

### Klucz obcy

`FOREIGN KEY` łączy jedną tabelę z drugą.

Na przykład `orders.user_id` może wskazywać na `users.id`.

To podstawa relacji w bazie.

---

## JOIN — po co istnieje

`JOIN` łączy dane z kilku tabel.

Na przykład masz:

- tabelę `users`,
- tabelę `orders`.

I chcesz zobaczyć zamówienia razem z nazwą użytkownika.

Przykład:

```sql
SELECT users.name, orders.total
FROM users
JOIN orders ON users.id = orders.user_id;
```

Bez zrozumienia joinów trudno budować realne systemy.

---

## Przykład z outputem

Zapytanie:

```sql
SELECT id, name FROM users ORDER BY id;
```

Przykładowy wynik:

```text
1 | Anna
2 | Jan
3 | Marek
```

To oczywiście uproszczona reprezentacja, ale dobrze pokazuje efekt działania `SELECT`.

---

## Typowe błędy początkujących

- brak `WHERE` przy `UPDATE` lub `DELETE`,
- brak rozumienia relacji między tabelami,
- traktowanie ORM jak zamiennika myślenia o SQL,
- ignorowanie sortowania i limitowania wyników,
- pobieranie wszystkich kolumn i wszystkich rekordów bez potrzeby.

---

## Praktyczna ściąga

### Najczęstsze operacje

```sql
SELECT ...
INSERT INTO ...
UPDATE ...
DELETE FROM ...
```

### Najczęstsze dodatki

- `WHERE`,
- `ORDER BY`,
- `LIMIT`,
- `JOIN`.

### Ważna zasada

Przed `UPDATE` i `DELETE` zawsze upewnij się, że warunek `WHERE` jest poprawny.

---

## Ćwiczenia

1. Napisz `SELECT` pobierający dwa pola z tabeli.
2. Napisz `INSERT` dodający rekord.
3. Napisz `UPDATE` z `WHERE`.
4. Napisz `DELETE` z `WHERE`.
5. Napisz `SELECT` z `ORDER BY` i `LIMIT`.
6. Wyjaśnij różnicę między kluczem głównym i obcym.
7. Wyjaśnij, po co istnieje `JOIN`.

---

## Najważniejsze do zapamiętania

- SQL to fundament pracy z bazą danych, nawet jeśli używasz ORM.
- `SELECT`, `INSERT`, `UPDATE`, `DELETE` to absolutna podstawa.
- `WHERE`, `ORDER BY`, `LIMIT` i `JOIN` bardzo często pojawiają się w realnym kodzie.
- Klucz główny identyfikuje rekord, a klucz obcy łączy tabele.
- Brak zrozumienia SQL bardzo szybko mści się w backendzie.
