# Transakcje w bazach danych w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest transakcja](#czym-jest-transakcja)
3. [Po co potrzebne są transakcje](#po-co-potrzebne-są-transakcje)
4. [`commit` i `rollback`](#commit-i-rollback)
5. [Spójność danych](#spójność-danych)
6. [Typowe sytuacje biznesowe](#typowe-sytuacje-biznesowe)
7. [Przykład z `sqlite3`](#przykład-z-sqlite3)
8. [Przykład mentalny "wszystko albo nic"](#przykład-mentalny-wszystko-albo-nic)
9. [Transakcje a ORM](#transakcje-a-orm)
10. [Typowe błędy początkujących](#typowe-błędy-początkujących)
11. [Praktyczna ściąga](#praktyczna-ściąga)
12. [Ćwiczenia](#ćwiczenia)
13. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

Transakcje to jedna z najważniejszych podstaw pracy z bazą danych.

Bez ich zrozumienia łatwo uszkodzić spójność danych nawet wtedy, gdy sam kod wygląda poprawnie.

---

## Czym jest transakcja

Transakcja to grupa operacji, które powinny zostać wykonane:

- wszystkie razem,
- albo żadna.

To bardzo ważne przy zmianach w danych.

---

## Po co potrzebne są transakcje

Bo wiele operacji biznesowych składa się z kilku kroków.

Na przykład:

- pobranie środków z konta A,
- dopisanie środków do konta B,
- zapis przelewu do historii.

Jeśli jeden krok się uda, a kolejny nie, bez transakcji możesz zostawić dane w złym stanie.

---

## `commit` i `rollback`

`commit`:

- zatwierdza zmiany.

`rollback`:

- cofa zmiany z bieżącej transakcji.

To podstawowe pojęcia, które trzeba rozumieć przy pracy z bazą.

---

## Spójność danych

Transakcje chronią spójność systemu.

Bez nich łatwo o sytuacje, w których część danych została zapisana, a część nie.

To szczególnie groźne przy operacjach biznesowych obejmujących kilka tabel albo kilka rekordów.

---

## Typowe sytuacje biznesowe

Transakcje są bardzo ważne przy:

- zamówieniach,
- płatnościach,
- rezerwacjach,
- zmianie stanów magazynowych,
- wielu powiązanych zapisach.

Właśnie tam zasada "wszystko albo nic" ma największy sens.

---

## Przykład z `sqlite3`

```python
import sqlite3

conn = sqlite3.connect("shop.db")

try:
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET stock = stock - 1 WHERE id = 1")
    cursor.execute("INSERT INTO orders(user_id, product_id) VALUES (1, 1)")
    conn.commit()
except Exception:
    conn.rollback()
    raise
finally:
    conn.close()
```

Tu jeśli druga operacja się nie powiedzie, cofnięta zostanie też pierwsza.

---

## Przykład mentalny "wszystko albo nic"

Wyobraź sobie:

1. zmniejszasz stan magazynowy,
2. próbujesz utworzyć zamówienie,
3. zapis zamówienia się wywala.

Bez transakcji możesz zostać z:

- mniejszym stanem magazynowym,
- ale bez samego zamówienia.

To już jest błąd biznesowy, nie tylko techniczny.

---

## Transakcje a ORM

ORM nie usuwa potrzeby rozumienia transakcji.

Pod spodem nadal trzeba wiedzieć:

- kiedy zatwierdzasz zmiany,
- kiedy wycofujesz operację,
- jaki jest zakres jednostki pracy.

To, że pracujesz na obiektach, nie znaczy, że spójność danych "robi się sama".

---

## Typowe błędy początkujących

- myślenie, że każdy zapis jest automatycznie bezpieczny,
- brak `rollback` przy błędach,
- brak myślenia o kilku operacjach jako jednej jednostce biznesowej,
- rozdzielanie logicznie jednej operacji na wiele niekontrolowanych zapisów.

---

## Praktyczna ściąga

### Najważniejsza zasada

Transakcja = wszystko albo nic.

### Kluczowe operacje

```python
conn.commit()
conn.rollback()
```

### Gdzie szczególnie pamiętać

- płatności,
- zamówienia,
- rezerwacje,
- stany magazynowe.

---

## Ćwiczenia

1. Wyjaśnij, czym jest transakcja.
2. Wyjaśnij różnicę między `commit` i `rollback`.
3. Podaj przykład operacji wymagającej transakcji.
4. Wyjaśnij, czemu kilka zapisów może tworzyć jedną jednostkę biznesową.
5. Rozpisz scenariusz, w którym brak transakcji psuje spójność danych.

---

## Najważniejsze do zapamiętania

- Transakcja chroni spójność danych.
- `commit` zatwierdza zmiany, a `rollback` je cofa.
- W operacjach biznesowych często kilka zapisów tworzy jedną całość.
- ORM nie zwalnia z rozumienia transakcji.
- Brak myślenia transakcyjnego bardzo szybko prowadzi do realnych błędów biznesowych.
