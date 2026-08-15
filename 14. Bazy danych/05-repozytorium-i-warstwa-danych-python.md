# Repozytorium i warstwa danych w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co wydzielać warstwę danych](#po-co-wydzielać-warstwę-danych)
3. [Czym jest repozytorium](#czym-jest-repozytorium)
4. [Repozytorium a ORM](#repozytorium-a-orm)
5. [Logika biznesowa a dostęp do danych](#logika-biznesowa-a-dostęp-do-danych)
6. [Testowalność](#testowalność)
7. [Kiedy ten wzorzec ma sens](#kiedy-ten-wzorzec-ma-sens)
8. [Przykład mentalny](#przykład-mentalny)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczna ściąga](#praktyczna-ściąga)
11. [Ćwiczenia](#ćwiczenia)
12. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

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
- poprawić utrzymanie kodu,
- zmniejszyć zależność reszty systemu od szczegółów ORM albo SQL.

---

## Czym jest repozytorium

Repozytorium to warstwa albo obiekt odpowiedzialny za dostęp do danych.

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

To ważne:

repozytorium nie jest konkurencją dla ORM.

To raczej sposób zorganizowania użycia ORM w projekcie.

---

## Logika biznesowa a dostęp do danych

To bardzo ważne rozróżnienie.

Logika biznesowa powinna odpowiadać na pytania typu:

- czy użytkownik może coś zrobić,
- jak obliczyć wynik,
- jaka reguła obowiązuje,
- co się ma wydarzyć w systemie.

Warstwa danych powinna odpowiadać:

- jak pobrać rekord,
- jak zapisać zmiany,
- jak znaleźć obiekt po kryteriach.

---

## Testowalność

To jedna z największych zalet takiego podziału.

Jeśli logika biznesowa nie zna szczegółów bazy, łatwiej ją testować niezależnie.

Możesz podmienić repozytorium na:

- fake,
- mock,
- in-memory implementację.

To bardzo pomaga w sensownym testowaniu aplikacji.

---

## Kiedy ten wzorzec ma sens

Najbardziej:

- w większych aplikacjach,
- w projektach zespołowych,
- tam, gdzie logika biznesowa jest istotna,
- tam, gdzie chcesz mieć porządną architekturę.

W bardzo małym projekcie może być zbyt ciężki, jeśli wprowadza abstrakcję bez realnej potrzeby.

---

## Przykład mentalny

Dobry podział wygląda tak:

- endpoint odbiera request,
- serwis biznesowy podejmuje decyzję,
- repozytorium pobiera lub zapisuje dane.

Przykłady metod repozytorium:

- `get_user_by_id`,
- `get_user_by_email`,
- `save_order`,
- `list_active_products`.

To jest dużo czytelniejsze niż zapytania rozlane po endpointach.

---

## Typowe błędy początkujących

- wrzucanie zapytań do endpointów,
- wrzucanie logiki biznesowej do modeli ORM,
- brak jednej odpowiedzialności klas i modułów,
- zbyt ciężkie repozytoria robiące wszystko naraz,
- tworzenie abstrakcji tak ogólnej, że przestaje mówić coś o domenie.

---

## Praktyczna ściąga

### Repozytorium pomaga

- porządkować dostęp do danych,
- ukrywać szczegóły ORM i bazy,
- poprawiać testowalność,
- wzmacniać architekturę.

### Ale pamiętaj

- nie każdy mały projekt potrzebuje rozbudowanego wzorca,
- abstrahuj tyle, ile naprawdę daje wartość.

---

## Ćwiczenia

1. Wyjaśnij, czym jest repozytorium.
2. Wyjaśnij, czemu nie warto pisać zapytań bezpośrednio w endpointach.
3. Podaj przykład metody repozytorium.
4. Wyjaśnij różnicę między logiką biznesową a warstwą danych.
5. Wyjaśnij, czemu repozytorium poprawia testowalność.

---

## Najważniejsze do zapamiętania

- Repozytorium porządkuje dostęp do danych.
- Logika biznesowa nie powinna znać wszystkich szczegółów bazy.
- ORM nie zastępuje architektury.
- Ten podział poprawia czytelność, testowalność i utrzymanie kodu.
