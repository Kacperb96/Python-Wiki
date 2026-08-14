# Bezpieczna serializacja w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest serializacja](#czym-jest-serializacja)
3. [Po co temat bezpieczeństwa](#po-co-temat-bezpieczeństwa)
4. [Formaty danych a ryzyko](#formaty-danych-a-ryzyko)
5. [JSON jako bezpieczniejszy wybór](#json-jako-bezpieczniejszy-wybór)
6. [Ryzyka przy deserializacji](#ryzyka-przy-deserializacji)
7. [`pickle` i ostrożność](#pickle-i-ostrożność)
8. [Zasada ograniczonego zaufania](#zasada-ograniczonego-zaufania)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczne przykłady](#praktyczne-przykłady)
11. [Dobre praktyki](#dobre-praktyki)
12. [Podsumowanie](#podsumowanie)
13. [Mini ściąga](#mini-ściąga)
14. [Ćwiczenia](#ćwiczenia)
15. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Serializacja to zamiana danych do formatu nadającego się do zapisu albo przesłania.

Sama w sobie jest normalną praktyką, ale przy deserializacji mogą pojawić się poważne ryzyka.

---

## Czym jest serializacja

To zapis obiektu lub danych do formatu takiego jak:

- JSON,
- XML,
- binarny format własny,
- inne reprezentacje.

Deserializacja to proces odwrotny.

---

## Po co temat bezpieczeństwa

Bo nie każdy format i nie każda biblioteka są równie bezpieczne dla danych z nieufnego źródła.

Deserializacja potrafi być niebezpiecznym punktem wejścia.

---

## Formaty danych a ryzyko

Niektóre formaty są bardziej deklaratywne i przewidywalne.

Inne mogą być bardziej ryzykowne, zwłaszcza gdy odtwarzają bardziej złożone obiekty.

---

## JSON jako bezpieczniejszy wybór

JSON zwykle jest dobrym i przewidywalnym wyborem dla wymiany danych.

Nadal wymaga walidacji treści, ale sam format jest zwykle bezpieczniejszy niż mechanizmy deserializujące arbitralne obiekty.

---

## Ryzyka przy deserializacji

Największy problem zaczyna się wtedy, gdy aplikacja ufa zewnętrznym danym i próbuje odtworzyć z nich złożone obiekty bez kontroli.

---

## `pickle` i ostrożność

`pickle` jest przydatny w pewnych kontrolowanych scenariuszach, ale nie powinno się go używać do nieufnych danych z zewnątrz.

To jeden z najważniejszych praktycznych komunikatów bezpieczeństwa w Pythonie.

---

## Zasada ograniczonego zaufania

Jeśli dane pochodzą z:

- internetu,
- użytkownika,
- zewnętrznego systemu,

to trzeba zakładać ograniczone zaufanie i wybierać bezpieczniejsze formaty oraz walidację.

---

## Typowe błędy początkujących

- używanie niebezpiecznej deserializacji dla nieufnych danych,
- brak walidacji po odczycie JSON lub XML,
- mylenie wygody z bezpieczeństwem,
- przekonanie, że "wewnętrzne dane" zawsze są bezpieczne.

---

## Praktyczne przykłady

### Bezpieczniejszy kierunek

- dane przychodzą jako JSON,
- są parsowane,
- potem walidowane przez model danych.

### Ryzykowny kierunek

- aplikacja odtwarza z zewnętrznego payloadu złożone obiekty bez odpowiedniej kontroli.

---

## Dobre praktyki

- dla danych z zewnątrz preferuj prostsze i przewidywalne formaty,
- waliduj dane po deserializacji,
- nie używaj ryzykownych mechanizmów do nieufnych źródeł,
- rozumiej, jaki kontrakt danych naprawdę przyjmujesz.

---

## Podsumowanie

Bezpieczna serializacja to temat bardziej praktyczny, niż się początkowo wydaje.

Zły wybór formatu lub zbyt duże zaufanie do wejścia potrafią stworzyć bardzo poważne problemy.

---

## Mini ściąga

Najważniejsze:

- serializacja i deserializacja to punkty wrażliwe,
- dla nieufnych danych preferuj prostsze formaty,
- waliduj dane po odczycie,
- ostrożnie traktuj mechanizmy odtwarzające złożone obiekty.

---

## Ćwiczenia

1. Wyjaśnij, czym jest serializacja.
2. Wyjaśnij, czemu deserializacja może być ryzykowna.
3. Wyjaśnij, czemu JSON bywa bezpieczniejszym wyborem.
4. Wyjaśnij, czemu `pickle` wymaga ostrożności.
5. Wyjaśnij, czemu walidacja po deserializacji nadal jest potrzebna.

---

## Przykładowe rozwiązania

### 1. Serializacja

To zamiana danych do formatu nadającego się do zapisu lub przesłania.

### 2. Ryzyko deserializacji

Bo aplikacja może zaufać niebezpiecznym lub niepoprawnym danym z zewnątrz.

### 3. JSON

Bo zwykle opisuje proste dane, a nie arbitralne obiekty wykonywalne.

### 4. `pickle`

Bo nie powinien być używany do nieufnych danych z zewnątrz.

### 5. Walidacja

Bo nawet poprawnie sparsowany format może zawierać błędne albo niezgodne biznesowo dane.
