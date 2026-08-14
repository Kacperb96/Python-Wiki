# Zestaw ćwiczeń praktycznych — 14. Bazy danych

## Poziom 1 — SQL

1. Napisz `SELECT` pobierający dwa pola z tabeli.
2. Napisz `INSERT` dodający rekord.
3. Napisz `UPDATE` z `WHERE`.
4. Napisz `DELETE` z `WHERE`.
5. Napisz `SELECT` z `ORDER BY` i `LIMIT`.
6. Zaprojektuj prostą tabelę `users`.

## Poziom 2 — transakcje

7. Opisz operację biznesową, która wymaga transakcji.
8. Napisz prosty przykład z `sqlite3`, gdzie po błędzie trzeba zrobić `rollback`.
9. Pokaż, co może pójść źle bez transakcji przy dwóch powiązanych zapisach.

## Poziom 3 — SQLAlchemy Core

10. Zdefiniuj prostą tabelę przez SQLAlchemy Core.
11. Zbuduj zapytanie `select`.
12. Zbuduj zapytanie `insert`.
13. Zbuduj zapytanie `update`.
14. Zbuduj zapytanie `delete`.

## Poziom 4 — SQLAlchemy ORM

15. Zdefiniuj model ORM `User`.
16. Zdefiniuj model ORM `Order`.
17. Zaprojektuj relację `User -> Orders`.
18. Dodaj prosty zapis przez sesję.
19. Odczytaj rekord przez ORM.
20. Zaktualizuj rekord przez ORM.

## Poziom 5 — architektura danych

21. Zbuduj proste repozytorium `UserRepository`.
22. Dodaj metody:
   - `get_by_id`
   - `get_by_email`
   - `save`
   - `delete`
23. Oddziel logikę biznesową od repozytorium.
24. Zaprojektuj migrację dodającą kolumnę `is_active`.
25. Opisz, jak wykryć problem N+1 w prostym endpointzie.

## Zadanie końcowe

26. Zbuduj mini warstwę danych dla systemu zamówień:
   - modele SQLAlchemy,
   - transakcje,
   - repozytoria,
   - scenariusz wymagający `commit` i `rollback`,
   - przykład potencjalnego N+1 i jego opis,
   - szkic migracji Alembic.
