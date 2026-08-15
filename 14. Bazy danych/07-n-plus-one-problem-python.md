# Problem N+1 w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest problem N+1](#czym-jest-problem-n1)
3. [Skąd bierze się ten problem](#skąd-bierze-się-ten-problem)
4. [Dlaczego jest groźny](#dlaczego-jest-groźny)
5. [N+1 a ORM](#n1-a-orm)
6. [Przykład mentalny](#przykład-mentalny)
7. [Jak rozpoznawać problem](#jak-rozpoznawać-problem)
8. [Jak ograniczać N+1](#jak-ograniczać-n1)
9. [Przykład efektu wydajnościowego](#przykład-efektu-wydajnościowego)
10. [Typowe błędy początkujących](#typowe-błędy-początkujących)
11. [Praktyczna ściąga](#praktyczna-ściąga)
12. [Ćwiczenia](#ćwiczenia)
13. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

Problem N+1 to jeden z najczęstszych wydajnościowych problemów przy pracy z ORM.

Jest bardzo częsty i często niewidoczny na pierwszy rzut oka.

---

## Czym jest problem N+1

To sytuacja, w której:

- robisz jedno zapytanie po listę obiektów,
- a potem dla każdego obiektu wykonuje się kolejne zapytanie po dane powiązane.

W efekcie zamiast 1 lub 2 zapytań masz:

- 1 zapytanie główne,
- plus N dodatkowych zapytań.

---

## Skąd bierze się ten problem

Najczęściej z leniwego ładowania relacji i nieświadomego iterowania po obiektach powiązanych.

ORM może to robić "wygodnie", ale koszt bywa bardzo duży.

---

## Dlaczego jest groźny

Bo:

- wydajność spada,
- liczba zapytań gwałtownie rośnie,
- aplikacja zaczyna działać wolno pod obciążeniem,
- problem może nie być widoczny przy małej liczbie rekordów.

To właśnie czyni go tak zdradliwym.

---

## N+1 a ORM

To klasyczny problem właśnie dla ORM-ów.

Wygoda pracy na relacjach nie zwalnia z myślenia o tym, ile zapytań naprawdę trafia do bazy.

Ładny kod obiektowy nie oznacza jeszcze dobrego kodu wydajnościowo.

---

## Przykład mentalny

Pobierasz 100 użytkowników.

Potem w pętli dla każdego użytkownika pobierasz jego zamówienia.

Efekt:

- 1 zapytanie po użytkowników,
- 100 kolejnych po zamówienia.

To właśnie klasyczny przykład N+1.

---

## Jak rozpoznawać problem

Sygnały:

- endpoint działa wolno przy większej liczbie rekordów,
- logi bazy pokazują bardzo dużo podobnych zapytań,
- wydajność spada nieproporcjonalnie do wielkości danych,
- kod wygląda niewinnie, ale aplikacja robi lawinę zapytań.

---

## Jak ograniczać N+1

Najczęściej przez:

- świadome ładowanie relacji,
- łączenie zapytań,
- planowanie dostępu do danych,
- analizę wygenerowanego SQL,
- patrzenie w logi i profilowanie warstwy danych.

---

## Przykład efektu wydajnościowego

Na małych danych możesz nie zauważyć problemu.

Dla 5 rekordów różnica bywa mała.

Dla 500 albo 5000 rekordów liczba zapytań i czas odpowiedzi potrafią eksplodować.

Dlatego N+1 jest tak groźne właśnie w realnych systemach, a nie w mikroprzykładach.

---

## Typowe błędy początkujących

- ślepa wiara, że ORM "sam to ogarnie",
- brak patrzenia na liczbę zapytań,
- testowanie tylko na małych danych,
- brak świadomości kosztu iteracji po relacjach,
- skupianie się wyłącznie na czytelności kodu bez patrzenia na skutki wykonania.

---

## Praktyczna ściąga

### N+1 oznacza zwykle

- jedno zapytanie główne,
- wiele podobnych zapytań dodatkowych.

### Gdzie patrzeć

- logi SQL,
- czas odpowiedzi endpointów,
- liczbę zapytań dla relacji.

### Najważniejsza intuicja

ORM nie zwalnia z myślenia o tym, ile razy pytasz bazę.

---

## Ćwiczenia

1. Wyjaśnij, czym jest problem N+1.
2. Rozpisz prosty scenariusz, w którym się pojawia.
3. Wyjaśnij, czemu na małych danych może być niewidoczny.
4. Opisz, jak rozpoznać go po logach albo zachowaniu endpointu.
5. Wyjaśnij, czemu ORM nie zwalnia z myślenia o liczbie zapytań.

---

## Najważniejsze do zapamiętania

- N+1 to klasyczny problem wydajnościowy przy pracy z ORM.
- Najczęściej bierze się z nieświadomego dostępu do relacji.
- Problem rośnie razem ze skalą danych.
- Żeby go zauważyć, trzeba patrzeć na realne zapytania i wydajność, a nie tylko na wygląd kodu.
