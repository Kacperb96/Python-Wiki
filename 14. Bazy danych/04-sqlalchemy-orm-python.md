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
10. [Przykład mentalny](#przykład-mentalny)
11. [Typowe błędy początkujących](#typowe-błędy-początkujących)
12. [Praktyczna ściąga](#praktyczna-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

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

To bardzo wygodne, ale nadal trzeba rozumieć, że pod spodem działa SQL.

---

## Po co używać ORM

ORM pomaga:

- pisać bardziej obiektowy kod,
- wygodniej modelować domenę,
- lepiej integrować warstwę danych z logiką aplikacji,
- szybciej budować wiele typowych operacji CRUD.

Ale nie zwalnia z rozumienia SQL.

---

## Modele

Model ORM zwykle reprezentuje tabelę.

Przykład mentalny:

- klasa `User`,
- tabela `users`,
- instancja `User` jako jeden rekord.

To bardzo wygodny sposób myślenia w warstwie aplikacyjnej.

---

## Sesja

Sesja zarządza cyklem życia obiektów i komunikacją z bazą na poziomie ORM.

To bardzo ważny element całego modelu pracy.

Najprościej:

- sesja wie, jakie obiekty zostały zmienione,
- kiedy trzeba je zapisać,
- kiedy trzeba zsynchronizować stan z bazą.

---

## CRUD w ORM

Najczęstsze operacje:

- create,
- read,
- update,
- delete.

ORM upraszcza je przez pracę na obiektach.

Mentalnie:

- tworzysz obiekt,
- dodajesz go do sesji,
- zatwierdzasz zmiany,
- odczytujesz obiekty przez zapytania ORM.

---

## Relacje

Jedna z największych zalet ORM to modelowanie relacji:

- one-to-many,
- many-to-one,
- many-to-many.

To bardzo ważne w realnych aplikacjach biznesowych.

Na przykład:

- `User` ma wiele `Order`,
- `Order` należy do jednego `User`.

---

## ORM a SQL

To kluczowy temat.

ORM daje wygodę, ale pod spodem nadal działa SQL.

Jeśli nie rozumiesz SQL, łatwo:

- pisać nieefektywne zapytania,
- źle modelować relacje,
- mieć problemy wydajnościowe,
- nie rozumieć problemów takich jak N+1.

---

## Przykład mentalny

Masz model `User`.

Tworzysz:

- obiekt `User(name="Anna")`,
- dodajesz go do sesji,
- robisz `commit`,
- rekord trafia do tabeli `users`.

To wygląda obiektowo, ale pod spodem wciąż stoi operacja SQL.

---

## Typowe błędy początkujących

- traktowanie ORM jako magii,
- brak rozumienia sesji,
- brak rozumienia relacji,
- ignorowanie wygenerowanego SQL,
- projektowanie modeli bez myślenia o danych i wydajności,
- wrzucanie zbyt dużo logiki do modeli ORM bez refleksji.

---

## Praktyczna ściąga

### ORM pomaga, gdy chcesz

- pracować na modelach obiektowych,
- wygodnie modelować relacje,
- budować CRUD w bardziej obiektowym stylu.

### Ale pamiętaj

- ORM nie usuwa SQL,
- ORM nie usuwa potrzeby rozumienia wydajności,
- sesja i relacje są kluczowe.

---

## Ćwiczenia

1. Wyjaśnij, czym jest ORM.
2. Wyjaśnij rolę sesji.
3. Opisz relację `User -> Orders`.
4. Wyjaśnij własnymi słowami, czemu ORM nie zwalnia ze znajomości SQL.
5. Podaj przykład błędu, który może wyniknąć z bezrefleksyjnej pracy z ORM.

---

## Najważniejsze do zapamiętania

- SQLAlchemy ORM mapuje bazę na obiekty Pythona.
- Modele i sesja to centralne elementy tego podejścia.
- Relacje są ogromną zaletą ORM, ale wymagają rozumienia.
- ORM daje wygodę, ale nie zastępuje myślenia o SQL i wydajności.
