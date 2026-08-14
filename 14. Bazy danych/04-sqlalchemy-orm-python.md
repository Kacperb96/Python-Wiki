# SQLAlchemy ORM w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest ORM](#czym-jest-orm)
3. [Czym jest SQLAlchemy ORM](#czym-jest-sqlalchemy-orm)
4. [Po co używać ORM](#po-co-używać-orm)
5. [Modele](#modele)
6. [Sesja](#sesja)
7. [CRUD w ORM](#crud-w-orm)
8. [Relacje](#relacje)
9. [ORM a SQL](#orm-a-sql)
10. [Typowe błędy początkujących](#typowe-błędy-początkujących)
11. [Praktyczne przykłady](#praktyczne-przykłady)
12. [Dobre praktyki](#dobre-praktyki)
13. [Podsumowanie](#podsumowanie)
14. [Mini ściąga](#mini-ściąga)
15. [Ćwiczenia](#ćwiczenia)
16. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

SQLAlchemy ORM pozwala pracować z bazą danych przez modele obiektowe Pythona.

To jeden z najważniejszych elementów backendowego ekosystemu Python.

---

## Czym jest ORM

ORM, czyli Object-Relational Mapping, mapuje tabele i rekordy bazy na obiekty i klasy.

Zamiast myśleć tylko w kategoriach wierszy, pracujesz też na modelach domenowych.

---

## Czym jest SQLAlchemy ORM

To warstwa SQLAlchemy umożliwiająca:

- definiowanie modeli,
- pracę przez sesję,
- zapisywanie i odczytywanie obiektów,
- modelowanie relacji.

---

## Po co używać ORM

ORM pomaga:

- pisać bardziej obiektowy kod,
- wygodniej modelować domenę,
- lepiej integrować warstwę danych z logiką aplikacji.

Ale nie zwalnia z rozumienia SQL.

---

## Modele

Model ORM zwykle reprezentuje tabelę.

Przykład mentalny:

- klasa `User`,
- tabela `users`,
- instancja `User` jako jeden rekord.

---

## Sesja

Sesja zarządza cyklem życia obiektów i komunikacją z bazą na poziomie ORM.

To bardzo ważny element całego modelu pracy.

---

## CRUD w ORM

Najczęstsze operacje:

- create,
- read,
- update,
- delete.

ORM upraszcza je przez pracę na obiektach.

---

## Relacje

Jedna z największych zalet ORM to modelowanie relacji:

- one-to-many,
- many-to-one,
- many-to-many.

To bardzo ważne w realnych aplikacjach biznesowych.

---

## ORM a SQL

To kluczowy temat.

ORM daje wygodę, ale pod spodem nadal działa SQL.

Jeśli nie rozumiesz SQL, łatwo:

- pisać nieefektywne zapytania,
- źle modelować relacje,
- mieć problemy wydajnościowe.

---

## Typowe błędy początkujących

- traktowanie ORM jako magii,
- brak rozumienia sesji,
- brak rozumienia relacji,
- ignorowanie wygenerowanego SQL,
- projektowanie modeli bez myślenia o danych i wydajności.

---

## Praktyczne przykłady

### Model użytkownika

Mentalnie:

- klasa `User`,
- pola `id`, `name`, `email`,
- zapis przez sesję.

### Relacja

Na przykład:

- `User` ma wiele `Order`,
- `Order` należy do jednego `User`.

---

## Dobre praktyki

- ucz się ORM razem z SQL,
- rozumiej, czym zarządza sesja,
- projektuj modele z myślą o domenie i danych,
- nie ukrywaj całej logiki aplikacji w modelach bez refleksji.

---

## Podsumowanie

SQLAlchemy ORM to bardzo ważne narzędzie profesjonalnego backendu Python.

Daje wygodę, ale największą wartość daje wtedy, gdy towarzyszy mu dobra znajomość SQL i modelu danych.

---

## Mini ściąga

Najważniejsze:

- ORM mapuje klasy na tabele,
- sesja zarządza pracą z obiektami,
- relacje są jednym z głównych powodów używania ORM,
- SQL nadal pozostaje ważny.

---

## Ćwiczenia

1. Wyjaśnij, czym jest ORM.
2. Wyjaśnij rolę sesji.
3. Wskaż przykład relacji one-to-many.
4. Wyjaśnij, czemu ORM nie zwalnia ze znajomości SQL.
5. Wskaż błąd, który może wyniknąć z traktowania ORM jak magii.

---

## Przykładowe rozwiązania

### 1. ORM

To mapowanie świata relacyjnej bazy danych na obiekty i klasy Pythona.

### 2. Sesja

Zarządza cyklem życia obiektów i komunikacją z bazą.

### 3. One-to-many

Jeden użytkownik ma wiele zamówień.

### 4. Czemu znać SQL

Bo pod spodem ORM i tak generuje zapytania SQL, które trzeba rozumieć.

### 5. Błąd

Można nieświadomie tworzyć bardzo nieefektywne zapytania i nie rozumieć, skąd biorą się problemy.
