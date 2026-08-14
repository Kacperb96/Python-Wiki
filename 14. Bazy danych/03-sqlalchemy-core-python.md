# SQLAlchemy Core w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest SQLAlchemy Core](#czym-jest-sqlalchemy-core)
3. [Core a ORM](#core-a-orm)
4. [Po co znać Core](#po-co-znać-core)
5. [Engine](#engine)
6. [Tabela i metadane](#tabela-i-metadane)
7. [INSERT, SELECT, UPDATE, DELETE](#insert-select-update-delete)
8. [Wykonywanie zapytań](#wykonywanie-zapytań)
9. [Kiedy Core jest dobrym wyborem](#kiedy-core-jest-dobrym-wyborem)
10. [Typowe błędy początkujących](#typowe-błędy-początkujących)
11. [Praktyczne przykłady](#praktyczne-przykłady)
12. [Dobre praktyki](#dobre-praktyki)
13. [Podsumowanie](#podsumowanie)
14. [Mini ściąga](#mini-ściąga)
15. [Ćwiczenia](#ćwiczenia)
16. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

SQLAlchemy Core to niższy poziom pracy z bazą niż ORM, ale nadal bardzo wygodny i nowoczesny.

Pozwala budować zapytania programistycznie bez pełnego mapowania obiektowego.

---

## Czym jest SQLAlchemy Core

To warstwa SQLAlchemy skupiona na:

- tabelach,
- kolumnach,
- zapytaniach,
- połączeniach do bazy.

Nie pracujesz tu głównie na klasach domenowych jak w ORM.

---

## Core a ORM

Core:

- bliżej SQL,
- bardziej jawne zapytania,
- mniej obiektowego mapowania.

ORM:

- bliżej obiektów Pythona,
- wygodne modele i sesje,
- wyższy poziom abstrakcji.

Warto znać oba poziomy.

---

## Po co znać Core

Bo pomaga:

- lepiej rozumieć SQLAlchemy,
- pisać bardziej jawne zapytania,
- budować warstwę danych tam, gdzie ORM byłby zbyt ciężki.

---

## Engine

`Engine` reprezentuje połączenie z bazą na poziomie konfiguracji i komunikacji.

To jeden z podstawowych elementów SQLAlchemy.

---

## Tabela i metadane

W Core często definiujesz tabele jawnie.

To daje dużą kontrolę nad strukturą danych i zapytaniami.

---

## INSERT, SELECT, UPDATE, DELETE

Core pozwala budować te operacje przez obiekty i wyrażenia zamiast ręcznego składania stringów SQL.

To zwiększa bezpieczeństwo i czytelność.

---

## Wykonywanie zapytań

Zwykle:

- tworzysz engine,
- definiujesz metadane i tabele,
- otwierasz połączenie,
- wykonujesz zapytanie,
- odbierasz wynik.

---

## Kiedy Core jest dobrym wyborem

Na przykład:

- w prostszych warstwach dostępu do danych,
- przy bardziej złożonych zapytaniach,
- gdy chcesz być bliżej SQL niż ORM.

---

## Typowe błędy początkujących

- używanie ORM bez zrozumienia Core i SQL,
- brak rozumienia różnicy między tabelą a modelem ORM,
- traktowanie Core jak dziwnej, niepotrzebnej warstwy.

---

## Praktyczne przykłady

### Mentalny obraz

Pracujesz na obiektach reprezentujących:

- tabelę `users`,
- kolumnę `users.c.name`,
- zapytanie `select(users)`.

### Gdzie pasuje

- raporty,
- warstwa repozytorium,
- aplikacje z bardziej jawną kontrolą nad SQL.

---

## Dobre praktyki

- ucz się Core razem z podstawami SQL,
- rozumiej wygenerowane zapytania,
- nie uciekaj w abstrakcję bez potrzeby,
- wybieraj poziom narzędzia do potrzeb projektu.

---

## Podsumowanie

SQLAlchemy Core to bardzo wartościowa warstwa dla profesjonalnego Pythonowca pracującego z bazą.

Pozwala zachować dobrą równowagę między wygodą biblioteki a zrozumieniem SQL.

---

## Mini ściąga

Najważniejsze:

- Core pracuje na tabelach i zapytaniach,
- jest bliżej SQL niż ORM,
- dobrze pasuje do bardziej jawnej pracy z bazą.

---

## Ćwiczenia

1. Wyjaśnij różnicę między Core a ORM.
2. Wyjaśnij rolę `engine`.
3. Wskaż przypadek, w którym Core ma sens.
4. Wyjaśnij, po co znać Core nawet przy pracy z ORM.
5. Wskaż, czemu SQL nadal jest ważny przy SQLAlchemy.

---

## Przykładowe rozwiązania

### 1. Core vs ORM

Core jest bliżej SQL i tabel, a ORM bliżej klas i obiektów.

### 2. `engine`

To centralny punkt połączenia i komunikacji z bazą.

### 3. Gdzie ma sens

W warstwie raportowej albo przy bardziej jawnych zapytaniach.

### 4. Po co znać Core

Bo pomaga rozumieć, co naprawdę dzieje się pod spodem.

### 5. Czemu SQL ważny

Bo SQLAlchemy nie zwalnia z rozumienia zapytań i modelu danych.
