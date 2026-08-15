# Zestaw ćwiczeń praktycznych — 14. Bazy danych

Ćwiczenia są ułożone od rozumienia samego SQL do bardziej architektonicznego myślenia o warstwie danych.

Najlepiej robić je po kolei.

---

## Poziom 1 — SQL

1. Napisz `SELECT` pobierający dwa pola z tabeli.
2. Napisz `INSERT` dodający rekord.
3. Napisz `UPDATE` z `WHERE`.
4. Napisz `DELETE` z `WHERE`.
5. Napisz `SELECT` z `ORDER BY` i `LIMIT`.
6. Zaprojektuj prostą tabelę `users`.
7. Napisz zapytanie wybierające tylko aktywnych użytkowników.
8. Napisz zapytanie sortujące użytkowników malejąco po dacie utworzenia.
9. Wyjaśnij własnymi słowami, czemu `UPDATE` bez `WHERE` bywa groźne.

---

## Poziom 2 — relacje i JOIN

10. Zaprojektuj dwie tabele: `users` i `orders`.
11. Wskaż, gdzie powinien być klucz główny.
12. Wskaż, gdzie powinien być klucz obcy.
13. Opisz relację użytkownik -> zamówienia.
14. Napisz mentalnie prosty `JOIN`, który łączy użytkownika z jego zamówieniami.
15. Wyjaśnij, po co w ogóle istnieje `JOIN`.

---

## Poziom 3 — transakcje

16. Opisz operację biznesową, która wymaga transakcji.
17. Napisz prosty przykład z `sqlite3`, gdzie po błędzie trzeba zrobić `rollback`.
18. Pokaż, co może pójść źle bez transakcji przy dwóch powiązanych zapisach.
19. Rozpisz mentalnie scenariusz: utworzenie zamówienia + zmniejszenie stanu magazynowego.
20. Wyjaśnij, czemu to jedna jednostka biznesowa.

---

## Poziom 4 — SQLAlchemy Core

21. Zdefiniuj prostą tabelę przez SQLAlchemy Core.
22. Zbuduj zapytanie `select`.
23. Zbuduj zapytanie `insert`.
24. Zbuduj zapytanie `update`.
25. Zbuduj zapytanie `delete`.
26. Wyjaśnij własnymi słowami, czym SQLAlchemy Core różni się od ręcznie pisanego SQL i od ORM.

---

## Poziom 5 — SQLAlchemy ORM

27. Zdefiniuj model ORM `User`.
28. Zdefiniuj model ORM `Order`.
29. Zaprojektuj relację `User -> Orders`.
30. Dodaj prosty zapis przez sesję.
31. Odczytaj rekord przez ORM.
32. Zaktualizuj rekord przez ORM.
33. Usuń rekord przez ORM.
34. Wyjaśnij własnymi słowami, czym zarządza sesja ORM.

---

## Poziom 6 — architektura warstwy danych

35. Zbuduj proste repozytorium `UserRepository`.
36. Dodaj metody:

- `get_by_id`,
- `get_by_email`,
- `save`,
- `delete`.

37. Oddziel logikę biznesową od repozytorium.
38. Wskaż przykład rzeczy, która należy do serwisu biznesowego, a nie do repozytorium.
39. Wyjaśnij, czemu zapytania bezpośrednio w endpointach szybko robią bałagan.

---

## Poziom 7 — migracje i utrzymanie schematu

40. Zaprojektuj migrację dodającą kolumnę `is_active`.
41. Opisz, czemu schemat bazy powinien być wersjonowany.
42. Wyjaśnij, po co projektowi Alembic.
43. Podaj przykład zmiany w modelu danych, która wymaga migracji.
44. Wyjaśnij, czemu ręczne zmiany w bazie produkcyjnej są ryzykowne.

---

## Poziom 8 — wydajność i N+1

45. Opisz, czym jest problem N+1.
46. Rozpisz prosty scenariusz, w którym się pojawia.
47. Wyjaśnij, czemu problem może nie być widoczny na małej liczbie rekordów.
48. Opisz, jak rozpoznać N+1 po logach albo zachowaniu endpointu.
49. Wyjaśnij, czemu ORM nie zwalnia z myślenia o liczbie zapytań.

---

## Zadanie końcowe

50. Zbuduj mini warstwę danych dla systemu zamówień obejmującą:

- modele SQLAlchemy,
- transakcje,
- repozytoria,
- scenariusz wymagający `commit` i `rollback`,
- przykład potencjalnego N+1 i jego opis,
- szkic migracji Alembic.

51. Opisz krótko:

- jakie są tabele,
- jakie relacje między nimi istnieją,
- gdzie kończy się logika biznesowa, a zaczyna warstwa danych,
- gdzie w tym systemie najłatwiej o błąd wydajnościowy albo spójnościowy.

---

## Jak pracować z tym zestawem

Najlepiej:

1. najpierw zrobić SQL i transakcje,
2. potem przejść do Core i ORM,
3. dopiero później wejść w repozytoria, migracje i N+1,
4. zadanie końcowe potraktować jak mini-projekt warstwy danych.
