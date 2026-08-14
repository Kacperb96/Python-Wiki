# Repozytorium i warstwa danych w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co wydzielać warstwę danych](#po-co-wydzielać-warstwę-danych)
3. [Czym jest repozytorium](#czym-jest-repozytorium)
4. [Repozytorium a ORM](#repozytorium-a-orm)
5. [Logika biznesowa a dostęp do danych](#logika-biznesowa-a-dostęp-do-danych)
6. [Testowalność](#testowalność)
7. [Kiedy ten wzorzec ma sens](#kiedy-ten-wzorzec-ma-sens)
8. [Typowe błędy początkujących](#typowe-błędy-początkujących)
9. [Praktyczne przykłady](#praktyczne-przykłady)
10. [Dobre praktyki](#dobre-praktyki)
11. [Podsumowanie](#podsumowanie)
12. [Mini ściąga](#mini-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

W małych projektach łatwo pisać zapytania bezpośrednio tam, gdzie są potrzebne.

W większych systemach szybko zaczyna to boleć.

Dlatego warto rozumieć ideę warstwy danych i wzorca repozytorium.

---

## Po co wydzielać warstwę danych

Bo to pomaga:

- oddzielić logikę biznesową od bazy,
- ograniczyć chaos zapytań rozrzuconych po projekcie,
- uprościć testy,
- poprawić utrzymanie kodu.

---

## Czym jest repozytorium

Repozytorium to warstwa lub obiekt odpowiedzialny za dostęp do danych.

Zamiast wszędzie pisać:

- SQL,
- zapytania ORM,
- szczegóły sesji,

możesz mieć jedno miejsce, które to organizuje.

---

## Repozytorium a ORM

ORM nie rozwiązuje automatycznie problemu architektury.

Nadal możesz mieć chaotyczny kod, jeśli logika i dostęp do danych są wymieszane w wielu miejscach.

Repozytorium pomaga to uporządkować.

---

## Logika biznesowa a dostęp do danych

To bardzo ważne rozróżnienie.

Logika biznesowa powinna odpowiadać na pytania typu:

- czy użytkownik może coś zrobić,
- jak obliczyć wynik,
- jaka reguła obowiązuje.

Warstwa danych powinna odpowiadać:

- jak pobrać rekord,
- jak zapisać zmiany,
- jak znaleźć obiekt po kryteriach.

---

## Testowalność

To jedna z największych zalet takiego podziału.

Jeśli logika biznesowa nie zna szczegółów bazy, łatwiej ją testować niezależnie.

---

## Kiedy ten wzorzec ma sens

Najbardziej:

- w większych aplikacjach,
- w projektach zespołowych,
- tam, gdzie logika biznesowa jest istotna,
- tam, gdzie chcesz mieć porządną architekturę.

---

## Typowe błędy początkujących

- wrzucanie zapytań do endpointów,
- wrzucanie logiki biznesowej do modeli ORM,
- brak jednej odpowiedzialności klas i modułów,
- zbyt ciężkie repozytoria robiące wszystko naraz.

---

## Praktyczne przykłady

### Mentalny podział

- endpoint odbiera request,
- serwis biznesowy podejmuje decyzję,
- repozytorium pobiera lub zapisuje dane.

### Przykład roli repozytorium

- `get_user_by_id`
- `save_order`
- `list_active_products`

---

## Dobre praktyki

- oddzielaj warstwę HTTP, biznesową i danych,
- nie rozlewaj szczegółów bazy po całym projekcie,
- projektuj repozytoria wokół potrzeb domeny,
- nie przesadzaj z abstrakcją w bardzo małym projekcie.

---

## Podsumowanie

Repozytorium i wydzielona warstwa danych to ważny krok w stronę bardziej profesjonalnej architektury backendu Python.

Nie zawsze muszą być bardzo rozbudowane, ale warto rozumieć ich sens.

---

## Mini ściąga

Najważniejsze:

- repozytorium porządkuje dostęp do danych,
- logika biznesowa nie powinna znać wszystkich szczegółów bazy,
- ten podział poprawia testowalność i utrzymanie kodu.

---

## Ćwiczenia

1. Wyjaśnij, czym jest repozytorium.
2. Wyjaśnij, czemu nie warto pisać zapytań bezpośrednio w endpointach.
3. Podaj przykład metody repozytorium.
4. Wyjaśnij, jak ten wzorzec poprawia testowalność.
5. Wskaż przypadek, gdy nie trzeba przesadzać z tą abstrakcją.

---

## Przykładowe rozwiązania

### 1. Repozytorium

To warstwa odpowiedzialna za pobieranie i zapisywanie danych.

### 2. Czemu nie w endpointach

Bo prowadzi to do chaosu i mocnego związania warstwy HTTP z bazą.

### 3. Metoda

Na przykład `get_user_by_email`.

### 4. Testowalność

Bo logikę biznesową można testować bez realnej bazy lub z prostszymi zamiennikami.

### 5. Kiedy nie przesadzać

W bardzo małym projekcie lub jednorazowym narzędziu, gdzie dodatkowa warstwa tylko zaciemni kod.
