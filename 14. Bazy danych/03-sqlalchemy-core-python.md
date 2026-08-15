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
9. [Przykład mentalny](#przykład-mentalny)
10. [Kiedy Core jest dobrym wyborem](#kiedy-core-jest-dobrym-wyborem)
11. [Typowe błędy początkujących](#typowe-błędy-początkujących)
12. [Praktyczna ściąga](#praktyczna-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

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

### Core

- bliżej SQL,
- bardziej jawne zapytania,
- mniej obiektowego mapowania.

### ORM

- bliżej obiektów Pythona,
- wygodne modele i sesje,
- wyższy poziom abstrakcji.

Warto znać oba poziomy.

---

## Po co znać Core

Bo pomaga:

- lepiej rozumieć SQLAlchemy,
- pisać bardziej jawne zapytania,
- budować warstwę danych tam, gdzie ORM byłby zbyt ciężki,
- zachować bliższy kontakt z SQL.

---

## Engine

`Engine` reprezentuje połączenie z bazą na poziomie konfiguracji i komunikacji.

To jeden z podstawowych elementów SQLAlchemy.

Przykład mentalny:

- wskazujesz, z jaką bazą chcesz rozmawiać,
- na jakim adresie,
- przez jaki sterownik.

---

## Tabela i metadane

W Core często definiujesz tabele jawnie.

To daje dużą kontrolę nad strukturą danych i zapytaniami.

Mentalnie pracujesz na obiektach reprezentujących tabelę i jej kolumny.

---

## INSERT, SELECT, UPDATE, DELETE

Core pozwala budować te operacje przez obiekty i wyrażenia zamiast ręcznego składania stringów SQL.

To zwiększa bezpieczeństwo i czytelność.

Przykładowy mentalny model:

- `insert(users)`
- `select(users)`
- `update(users)`
- `delete(users)`

---

## Wykonywanie zapytań

Zwykle:

1. tworzysz engine,
2. definiujesz metadane i tabele,
3. otwierasz połączenie,
4. wykonujesz zapytanie,
5. odbierasz wynik.

To bardziej jawny model niż typowa praca przez ORM.

---

## Przykład mentalny

Pracujesz na obiektach reprezentujących:

- tabelę `users`,
- kolumnę `users.c.name`,
- zapytanie `select(users)`.

To bardzo wygodne, bo nadal jesteś blisko SQL, ale nie składasz wszystkiego jako surowych stringów.

---

## Kiedy Core jest dobrym wyborem

Na przykład:

- w prostszych warstwach dostępu do danych,
- przy bardziej złożonych zapytaniach,
- gdy chcesz być bliżej SQL niż ORM,
- gdy nie potrzebujesz pełnego modelu obiektowego.

---

## Typowe błędy początkujących

- używanie ORM bez rozumienia Core i SQL,
- brak rozumienia różnicy między tabelą a modelem ORM,
- traktowanie Core jak dziwnej, niepotrzebnej warstwy,
- uciekanie od SQL za wszelką cenę.

---

## Praktyczna ściąga

### Core jest dobry, gdy chcesz

- jawnych zapytań,
- większej kontroli,
- mniejszej abstrakcji niż ORM.

### Core nie oznacza

- ręcznego lepienia wszystkiego stringami SQL.

To nadal wygodne i nowoczesne API do budowania zapytań.

---

## Ćwiczenia

1. Wyjaśnij różnicę między Core i ORM.
2. Opisz rolę `Engine`.
3. Wytłumacz, na czym mentalnie pracujesz w SQLAlchemy Core.
4. Podaj przykład sytuacji, w której Core może być lepszy od ORM.
5. Wyjaśnij własnymi słowami, czemu znajomość Core pomaga lepiej rozumieć SQLAlchemy.

---

## Najważniejsze do zapamiętania

- SQLAlchemy Core jest bliżej SQL niż ORM.
- Daje dużą kontrolę nad tabelami i zapytaniami.
- Warto znać go nawet wtedy, gdy później głównie używasz ORM.
- Core pomaga zachować równowagę między wygodą biblioteki a zrozumieniem bazy.
