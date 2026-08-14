# Transakcje w bazach danych w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest transakcja](#czym-jest-transakcja)
3. [Po co potrzebne są transakcje](#po-co-potrzebne-są-transakcje)
4. [`commit` i `rollback`](#commit-i-rollback)
5. [Spójność danych](#spójność-danych)
6. [Typowe sytuacje biznesowe](#typowe-sytuacje-biznesowe)
7. [Transakcje a ORM](#transakcje-a-orm)
8. [Typowe błędy początkujących](#typowe-błędy-początkujących)
9. [Praktyczne przykłady](#praktyczne-przykłady)
10. [Dobre praktyki](#dobre-praktyki)
11. [Podsumowanie](#podsumowanie)
12. [Mini ściąga](#mini-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Transakcje to jedna z najważniejszych podstaw pracy z bazą danych.

Bez ich zrozumienia łatwo uszkodzić spójność danych nawet wtedy, gdy sam kod "wygląda dobrze".

---

## Czym jest transakcja

Transakcja to grupa operacji, które powinny zostać wykonane:

- wszystkie razem,
- albo żadna.

To bardzo ważne przy zmianach w danych.

---

## Po co potrzebne są transakcje

Bo wiele operacji biznesowych składa się z kilku kroków.

Na przykład:

- pobranie środków,
- zapis przelewu,
- aktualizacja salda.

Jeśli jeden krok się uda, a drugi nie, bez transakcji możesz zostawić dane w złym stanie.

---

## `commit` i `rollback`

`commit`:

- zatwierdza zmiany.

`rollback`:

- cofa zmiany z bieżącej transakcji.

To podstawowe pojęcia, które trzeba rozumieć przy pracy z bazą.

---

## Spójność danych

Transakcje chronią spójność systemu.

Bez nich łatwo o sytuacje, w których część danych została zapisana, a część nie.

---

## Typowe sytuacje biznesowe

Transakcje są bardzo ważne przy:

- zamówieniach,
- płatnościach,
- rezerwacjach,
- zmianie stanów magazynowych,
- wielu powiązanych zapisach.

---

## Transakcje a ORM

ORM nie usuwa potrzeby rozumienia transakcji.

Pod spodem nadal trzeba wiedzieć:

- kiedy zatwierdzasz zmiany,
- kiedy wycofujesz operację,
- jaki jest zakres jednostki pracy.

---

## Typowe błędy początkujących

- myślenie, że każdy zapis jest automatycznie bezpieczny,
- brak `rollback` przy błędach,
- brak myślenia o kilku operacjach jako jednej jednostce biznesowej,
- rozdzielanie logicznie jednej operacji na wiele niekontrolowanych zapisów.

---

## Praktyczne przykłady

### Przykład biznesowy

Utworzenie zamówienia i zmniejszenie stanu magazynowego powinny być spójne.

Jeśli jedna część się nie powiedzie, całość nie powinna zostać częściowo zapisana.

### `sqlite3`

```python
conn.commit()
conn.rollback()
```

---

## Dobre praktyki

- myśl transakcyjnie o operacjach biznesowych,
- grupuj powiązane zapisy w jedną jednostkę,
- przy błędach przewiduj cofnięcie,
- rozumiej, gdzie kończy się transakcja.

---

## Podsumowanie

Transakcje to fundament bezpiecznej pracy z danymi.

Bez nich nawet poprawny składniowo kod może prowadzić do bardzo złych stanów biznesowych.

---

## Mini ściąga

Najważniejsze:

- transakcja = wszystko albo nic,
- `commit` zatwierdza,
- `rollback` cofa,
- transakcje chronią spójność danych.

---

## Ćwiczenia

1. Wyjaśnij, czym jest transakcja.
2. Wyjaśnij różnicę między `commit` i `rollback`.
3. Podaj przykład operacji wymagającej transakcji.
4. Wyjaśnij, czemu kilka zapisów może tworzyć jedną jednostkę biznesową.
5. Wyjaśnij, czemu ORM nie zwalnia z rozumienia transakcji.

---

## Przykładowe rozwiązania

### 1. Transakcja

To grupa operacji, które mają zostać wykonane razem albo wcale.

### 2. `commit` vs `rollback`

`commit` zapisuje zmiany, a `rollback` je cofa.

### 3. Przykład

Założenie zamówienia i zmniejszenie stanu magazynowego.

### 4. Jednostka biznesowa

Bo z punktu widzenia domeny wszystkie te kroki opisują jedną operację użytkownika.

### 5. ORM

Bo pod spodem nadal istnieje baza i mechanika transakcji, którą trzeba świadomie kontrolować.
