# Alembic w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest Alembic](#czym-jest-alembic)
3. [Po co potrzebne są migracje](#po-co-potrzebne-są-migracje)
4. [Relacja z SQLAlchemy](#relacja-z-sqlalchemy)
5. [Migracje schematu](#migracje-schematu)
6. [Wersjonowanie bazy](#wersjonowanie-bazy)
7. [Praca zespołowa a migracje](#praca-zespołowa-a-migracje)
8. [Typowe błędy początkujących](#typowe-błędy-początkujących)
9. [Praktyczne przykłady](#praktyczne-przykłady)
10. [Dobre praktyki](#dobre-praktyki)
11. [Podsumowanie](#podsumowanie)
12. [Mini ściąga](#mini-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Gdy aplikacja zaczyna żyć, schema bazy danych przestaje być stała.

Właśnie wtedy pojawia się potrzeba migracji, a w ekosystemie SQLAlchemy bardzo ważnym narzędziem jest Alembic.

---

## Czym jest Alembic

Alembic to narzędzie do zarządzania migracjami bazy danych.

Pomaga śledzić zmiany schematu w czasie.

---

## Po co potrzebne są migracje

Bo w realnym projekcie schema się zmienia:

- dodajesz kolumnę,
- zmieniasz tabelę,
- wprowadzasz relacje,
- usuwasz stare elementy modelu danych.

Trzeba to robić kontrolowanie, a nie ręcznie "na wyczucie".

---

## Relacja z SQLAlchemy

Alembic bardzo często działa obok SQLAlchemy.

SQLAlchemy opisuje modele i pracę z bazą, a Alembic pomaga przenosić schema do kolejnych wersji.

---

## Migracje schematu

Migracja to uporządkowany zestaw zmian w strukturze bazy.

Przykładowo:

- dodanie tabeli `users`,
- dodanie kolumny `email`,
- zmiana indeksu.

---

## Wersjonowanie bazy

To bardzo ważna idea.

Tak jak wersjonujesz kod, tak samo powinieneś wersjonować schema bazy.

Dzięki temu da się:

- odtworzyć stan środowiska,
- wdrożyć zmiany przewidywalnie,
- pracować zespołowo bez chaosu.

---

## Praca zespołowa a migracje

Bez migracji zespół bardzo szybko wpada w problemy typu:

- "u mnie działa",
- "moja baza wygląda inaczej",
- "na produkcji brakuje kolumny".

Alembic pomaga uniknąć takiego chaosu.

---

## Typowe błędy początkujących

- ręczne zmienianie bazy bez migracji,
- traktowanie migracji jako zbędnej formalności,
- brak rozumienia, że schema to część kodu projektu,
- ignorowanie kolejności i spójności zmian.

---

## Praktyczne przykłady

### Przykładowe zmiany

- dodanie kolumny `is_active`,
- nowa tabela `orders`,
- zmiana typu kolumny.

### Gdzie to pomaga

- lokalnie,
- na stagingu,
- na produkcji,
- w onboardingu nowej osoby do projektu.

---

## Dobre praktyki

- traktuj migracje jako część kodu,
- nie zmieniaj schematu ręcznie poza kontrolowanym procesem,
- utrzymuj porządek w historii migracji,
- rozumiej, co robi każda zmiana w bazie.

---

## Podsumowanie

Alembic to bardzo ważne narzędzie profesjonalnej pracy z bazą danych w Pythonie.

Bez migracji większy projekt backendowy bardzo szybko zaczyna się rozjeżdżać.

---

## Mini ściąga

Najważniejsze:

- Alembic zarządza migracjami,
- migracje wersjonują schema bazy,
- to kluczowe dla wdrożeń i pracy zespołowej.

---

## Ćwiczenia

1. Wyjaśnij, czym jest migracja bazy.
2. Wyjaśnij, po co wersjonować schema.
3. Podaj przykład zmiany wymagającej migracji.
4. Wyjaśnij, czemu ręczne zmiany w bazie są ryzykowne.
5. Wyjaśnij relację Alembic i SQLAlchemy.

---

## Przykładowe rozwiązania

### 1. Migracja

To kontrolowana zmiana struktury bazy danych zapisana jako część projektu.

### 2. Po co wersjonować

Żeby środowiska miały spójny schema i dało się bezpiecznie wdrażać zmiany.

### 3. Przykład

Dodanie kolumny `email` do tabeli `users`.

### 4. Czemu ręczne zmiany są ryzykowne

Bo łatwo rozjechać środowiska i stracić kontrolę nad historią zmian.

### 5. Relacja

SQLAlchemy opisuje modele i pracę z bazą, a Alembic obsługuje zmiany schematu.
