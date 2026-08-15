# 14. Bazy danych

To jest dział o bazodanowej warstwie backendowego Pythona.

Tutaj wchodzisz w obszar, bez którego większość realnych aplikacji bardzo szybko przestaje istnieć jako coś użytecznego.

Bo prawdziwe systemy zwykle muszą:

- przechowywać dane,
- odczytywać dane,
- aktualizować dane,
- zachowywać spójność,
- składać logikę biznesową z operacji na bazie,
- dbać o wydajność i porządek architektoniczny.

To dział, który spina backend z trwałością danych.

---

## Co powinieneś rozumieć po tym dziale

Po przerobieniu całego folderu powinieneś rozumieć:

- podstawy SQL,
- czym są tabele, rekordy, kolumny i relacje,
- po co są transakcje,
- czym różni się SQLAlchemy Core od ORM,
- jak działa sesja ORM,
- po co wydzielać repozytoria i warstwę danych,
- czym są migracje i po co istnieje Alembic,
- czym jest problem N+1 i dlaczego jest groźny.

---

## Dlaczego ten dział jest ważny

Backend bez bazy danych bardzo często jest tylko demonstracją.

Prawdziwa aplikacja zwykle:

- zapisuje użytkowników,
- przechowuje zamówienia,
- odczytuje konfigurację,
- buduje raporty,
- aktualizuje stan systemu,
- pilnuje spójności biznesowej.

Jeśli ta warstwa jest słaba, to nawet dobry web/API szybko zaczynają się psuć.

---

## Jak czytać ten dział

Najlepiej iść po kolei:

1. [01-sql-dla-pythonowca.md](/home/kacper/Desktop/Python_naprawiony/14.%20Bazy%20danych/01-sql-dla-pythonowca.md)
2. [02-transakcje-w-bazach-python.md](/home/kacper/Desktop/Python_naprawiony/14.%20Bazy%20danych/02-transakcje-w-bazach-python.md)
3. [03-sqlalchemy-core-python.md](/home/kacper/Desktop/Python_naprawiony/14.%20Bazy%20danych/03-sqlalchemy-core-python.md)
4. [04-sqlalchemy-orm-python.md](/home/kacper/Desktop/Python_naprawiony/14.%20Bazy%20danych/04-sqlalchemy-orm-python.md)
5. [05-repozytorium-i-warstwa-danych-python.md](/home/kacper/Desktop/Python_naprawiony/14.%20Bazy%20danych/05-repozytorium-i-warstwa-danych-python.md)
6. [06-alembic-python.md](/home/kacper/Desktop/Python_naprawiony/14.%20Bazy%20danych/06-alembic-python.md)
7. [07-n-plus-one-problem-python.md](/home/kacper/Desktop/Python_naprawiony/14.%20Bazy%20danych/07-n-plus-one-problem-python.md)

Ta kolejność ma sens, bo:

- najpierw rozumiesz sam język SQL,
- potem uczysz się myśleć o spójności danych,
- potem przechodzisz do narzędzi Pythona,
- a na końcu do architektury i wydajności.

---

## Jak pracować z tym działem

Najlepszy sposób nauki:

1. przeczytaj jeden plik,
2. przepisz przykłady,
3. przewiduj wynik zapytania albo efekt operacji,
4. uruchom przykład,
5. zrób własny wariant,
6. dopiero potem przejdź do ćwiczeń.

W bazach danych samo czytanie bardzo łatwo daje złudzenie zrozumienia.

Najwięcej daje samodzielne pisanie zapytań i myślenie o danych.

---

## Na co szczególnie uważać

Najczęstsze pułapki:

- używanie ORM bez rozumienia SQL,
- ignorowanie transakcji,
- mieszanie logiki biznesowej z dostępem do danych,
- brak migracji schematu,
- brak myślenia o liczbie zapytań,
- traktowanie bazy jak „magicznego magazynu”, a nie systemu z własnymi zasadami i kosztami.

---

## Po czym poznać, że temat zaczyna siedzieć

Dobry znak, jeśli potrafisz:

- napisać podstawowe `SELECT`, `INSERT`, `UPDATE`, `DELETE`,
- wyjaśnić, po co jest `WHERE`, `JOIN`, `LIMIT`,
- wskazać operację, która wymaga transakcji,
- rozróżnić SQLAlchemy Core i ORM,
- opisać rolę sesji ORM,
- wyjaśnić sens repozytorium,
- powiedzieć, po co potrzebne są migracje,
- rozpoznać ryzyko problemu N+1.

---

## Co ten dział daje w praktyce

Po opanowaniu tego folderu dużo lepiej poradzisz sobie z:

- budową backendów z bazą danych,
- czytaniem kodu SQLAlchemy,
- projektowaniem warstwy danych,
- diagnozowaniem problemów wydajnościowych,
- utrzymaniem spójności danych.

To bardzo praktyczny i bardzo zawodowy dział.

---

## Ćwiczenia

Do tego działu masz też [ZESTAW-CWICZEN.md](/home/kacper/Desktop/Python_naprawiony/14.%20Bazy%20danych/ZESTAW-CWICZEN.md).

Najlepiej:

- najpierw zrobić SQL i transakcje,
- potem Core i ORM,
- dopiero później repozytoria, Alembic i N+1.

---

## Co dalej

Po tym dziale naturalny następny krok to:

- [15. Architektura i jakość kodu](/home/kacper/Desktop/Python_naprawiony/15.%20Architektura%20i%20jako%C5%9B%C4%87%20kodu)
- a równolegle bardzo sensownie też [16. Bezpieczeństwo](/home/kacper/Desktop/Python_naprawiony/16.%20Bezpiecze%C5%84stwo)

Bo właśnie tam warstwa danych zaczyna łączyć się z większą architekturą i odpowiedzialnością produkcyjną.
