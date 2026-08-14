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
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczne przykłady](#praktyczne-przykłady)
11. [Dobre praktyki](#dobre-praktyki)
12. [Podsumowanie](#podsumowanie)
13. [Mini ściąga](#mini-ściąga)
14. [Ćwiczenia](#ćwiczenia)
15. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

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

---

## N+1 a ORM

To klasyczny problem właśnie dla ORM-ów.

Wygoda pracy na relacjach nie zwalnia z myślenia o tym, ile zapytań naprawdę trafia do bazy.

---

## Przykład mentalny

Pobierasz 100 użytkowników.

Potem w pętli dla każdego użytkownika pobierasz jego zamówienia.

Efekt:

- 1 zapytanie po użytkowników,
- 100 kolejnych po zamówienia.

---

## Jak rozpoznawać problem

Sygnały:

- endpoint działa wolno przy większej liczbie rekordów,
- logi bazy pokazują bardzo dużo podobnych zapytań,
- wydajność spada nieproporcjonalnie do wielkości danych.

---

## Jak ograniczać N+1

Najczęściej przez:

- świadome ładowanie relacji,
- łączenie zapytań,
- planowanie dostępu do danych,
- analizę wygenerowanego SQL.

---

## Typowe błędy początkujących

- ślepa wiara, że ORM "sam to ogarnie",
- brak patrzenia na liczbę zapytań,
- testowanie tylko na małych danych,
- brak świadomości kosztu iteracji po relacjach.

---

## Praktyczne przykłady

### Klasyczny przypadek

- lista zamówień,
- dla każdego zamówienia odczyt klienta,
- dla każdego klienta odczyt adresu.

Taki kod może bardzo szybko generować lawinę zapytań.

### Jak myśleć lepiej

Zastanów się wcześniej:

- jakie dane naprawdę będą potrzebne,
- które relacje warto pobrać razem.

---

## Dobre praktyki

- monitoruj liczbę zapytań,
- rozumiej relacje i sposób ich ładowania,
- testuj na danych zbliżonych do realnych,
- patrz nie tylko na elegancję kodu ORM, ale też na skutki wydajnościowe.

---

## Podsumowanie

Problem N+1 to jedna z najważniejszych praktycznych pułapek pracy z ORM.

Każdy backendowy Pythonowiec powinien umieć go rozpoznawać i ograniczać.

---

## Mini ściąga

Najważniejsze:

- N+1 = jedno zapytanie główne i wiele dodatkowych,
- często wynika z nieświadomej pracy z relacjami,
- uderza w wydajność,
- trzeba patrzeć na realną liczbę zapytań.

---

## Ćwiczenia

1. Wyjaśnij, czym jest problem N+1.
2. Podaj przykład z relacją użytkownik-zamówienia.
3. Wyjaśnij, czemu problem może być niewidoczny przy małej liczbie danych.
4. Wskaż 2 sposoby myślenia, które pomagają ograniczać N+1.
5. Wyjaśnij, czemu ORM nie zwalnia z myślenia o SQL i wydajności.

---

## Przykładowe rozwiązania

### 1. N+1

To sytuacja, gdy po jednym zapytaniu głównym system wykonuje kolejne N podobnych zapytań dla każdego rekordu.

### 2. Przykład

Pobranie listy użytkowników i osobne pobieranie zamówień każdego z nich w pętli.

### 3. Małe dane

Bo przy kilku rekordach koszt jest mały, ale przy setkach lub tysiącach gwałtownie rośnie.

### 4. Jak ograniczać

- planować pobranie relacji,
- monitorować liczbę zapytań.

### 5. ORM a SQL

Bo wygodny kod ORM może generować bardzo nieefektywne zapytania, jeśli nie patrzysz na skutki.
