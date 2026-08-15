# Alembic w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest Alembic](#czym-jest-alembic)
3. [Po co potrzebne są migracje](#po-co-potrzebne-są-migracje)
4. [Relacja z SQLAlchemy](#relacja-z-sqlalchemy)
5. [Migracje schematu](#migracje-schematu)
6. [Wersjonowanie bazy](#wersjonowanie-bazy)
7. [Praca zespołowa a migracje](#praca-zespołowa-a-migracje)
8. [Przykład mentalny zmiany schematu](#przykład-mentalny-zmiany-schematu)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczna ściąga](#praktyczna-ściąga)
11. [Ćwiczenia](#ćwiczenia)
12. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

Gdy aplikacja zaczyna żyć, schema bazy danych przestaje być stała.

Właśnie wtedy pojawia się potrzeba migracji, a w ekosystemie SQLAlchemy bardzo ważnym narzędziem jest Alembic.

---

## Czym jest Alembic

Alembic to narzędzie do zarządzania migracjami bazy danych.

Pomaga śledzić zmiany schematu w czasie.

Najprościej:

jeśli kod projektu się zmienia i modele się zmieniają, baza też musi zmieniać się w sposób kontrolowany.

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

SQLAlchemy opisuje modele i pracę z bazą, a Alembic pomaga przenosić schemat do kolejnych wersji.

To znów ważne rozróżnienie:

- SQLAlchemy opisuje i obsługuje warstwę danych,
- Alembic zarządza ewolucją schematu.

---

## Migracje schematu

Migracja to uporządkowany zestaw zmian w strukturze bazy.

Przykładowo:

- dodanie tabeli `users`,
- dodanie kolumny `email`,
- zmiana indeksu,
- usunięcie nieużywanej kolumny.

To wszystko powinno być wersjonowane tak samo jak kod aplikacji.

---

## Wersjonowanie bazy

To bardzo ważna idea.

Tak jak wersjonujesz kod, tak samo powinieneś wersjonować schemat bazy.

Dzięki temu da się:

- odtworzyć stan środowiska,
- wdrożyć zmiany przewidywalnie,
- pracować zespołowo bez chaosu,
- uruchomić projekt na nowym środowisku.

---

## Praca zespołowa a migracje

Bez migracji zespół bardzo szybko wpada w problemy typu:

- "u mnie działa",
- "moja baza wygląda inaczej",
- "na produkcji brakuje kolumny",
- "na stagingu mamy starszy schemat".

Alembic pomaga uniknąć takiego chaosu.

---

## Przykład mentalny zmiany schematu

Wyobraź sobie, że do tabeli `users` chcesz dodać kolumnę `is_active`.

To nie jest tylko zmiana w modelu Pythona.

To także zmiana struktury samej bazy.

Bez migracji możesz mieć sytuację, w której:

- kod oczekuje nowej kolumny,
- ale baza jeszcze jej nie ma.

I wtedy aplikacja zaczyna się wysypywać.

---

## Typowe błędy początkujących

- ręczne zmienianie bazy bez migracji,
- traktowanie migracji jako zbędnej formalności,
- brak rozumienia, że schemat to część kodu projektu,
- ignorowanie kolejności i spójności zmian,
- poprawianie czegoś ręcznie na produkcji bez odtworzenia tego w migracjach.

---

## Praktyczna ściąga

### Migracje pomagają

- wersjonować schemat,
- wdrażać zmiany przewidywalnie,
- utrzymywać zgodność środowisk,
- pracować zespołowo.

### Ważny mentalny model

Model w kodzie i struktura bazy muszą iść razem.

---

## Ćwiczenia

1. Wyjaśnij, czym jest migracja bazy.
2. Wyjaśnij, po co wersjonować schemat.
3. Podaj przykład zmiany wymagającej migracji.
4. Wyjaśnij, czemu ręczne zmiany w bazie są ryzykowne.
5. Wyjaśnij relację Alembic i SQLAlchemy.

---

## Najważniejsze do zapamiętania

- Alembic zarządza migracjami schematu bazy.
- Schemat bazy powinien być wersjonowany tak samo jak kod.
- Migracje są kluczowe dla wdrożeń i pracy zespołowej.
- Ręczne zmiany bez migracji bardzo szybko prowadzą do chaosu środowisk.
