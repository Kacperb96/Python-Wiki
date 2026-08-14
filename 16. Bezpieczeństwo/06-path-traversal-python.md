# Path traversal w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest path traversal](#czym-jest-path-traversal)
3. [Skąd bierze się problem](#skąd-bierze-się-problem)
4. [Niebezpieczne wejście użytkownika](#niebezpieczne-wejście-użytkownika)
5. [Przykładowy scenariusz ataku](#przykładowy-scenariusz-ataku)
6. [Jak się bronić](#jak-się-bronić)
7. [`pathlib` i bezpieczniejsze podejście](#pathlib-i-bezpieczniejsze-podejście)
8. [Typowe błędy początkujących](#typowe-błędy-początkujących)
9. [Praktyczne przykłady](#praktyczne-przykłady)
10. [Dobre praktyki](#dobre-praktyki)
11. [Podsumowanie](#podsumowanie)
12. [Mini ściąga](#mini-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Path traversal to błąd bezpieczeństwa związany z niekontrolowanym dostępem do plików poza dozwolonym katalogiem.

W Pythonie łatwo go popełnić, gdy ścieżki buduje się bezmyślnie z danych użytkownika.

---

## Czym jest path traversal

To sytuacja, gdy użytkownik potrafi wskazać ścieżkę wychodzącą poza przewidziany katalog.

Na przykład przez fragmenty typu:

- `../`
- `..\\`

---

## Skąd bierze się problem

Najczęściej z kodu, który robi coś w stylu:

- bierze nazwę pliku od użytkownika,
- dokleja ją do katalogu bazowego,
- otwiera plik bez sprawdzenia.

---

## Niebezpieczne wejście użytkownika

Jeśli użytkownik może podać nazwę pliku, nie można zakładać, że poda wyłącznie bezpieczne wartości.

To znowu klasyczna zasada:

input jest nieufny.

---

## Przykładowy scenariusz ataku

Aplikacja ma udostępniać pliki z katalogu `uploads/`.

Użytkownik zamiast `raport.pdf` podaje:

```text
../../sekrety.txt
```

Jeśli aplikacja nie sprawdza ścieżki, może odczytać coś spoza `uploads/`.

---

## Jak się bronić

Najważniejsze:

- nie ufaj ścieżkom od użytkownika,
- canonicalizuj i sprawdzaj ścieżki,
- ograniczaj dostęp do ustalonego katalogu bazowego,
- waliduj dozwolone nazwy i formaty.

---

## `pathlib` i bezpieczniejsze podejście

`pathlib` pomaga pracować czytelniej, ale sam z siebie nie rozwiązuje wszystkiego.

Trzeba nadal sprawdzić, czy wynikowa ścieżka naprawdę mieści się w dozwolonym katalogu.

---

## Typowe błędy początkujących

- proste sklejanie stringów ścieżek,
- brak sprawdzenia katalogu bazowego,
- założenie, że "użytkownik poda tylko nazwę pliku",
- brak whitelisty dla akceptowalnych nazw i rozszerzeń.

---

## Praktyczne przykłady

### Ryzykowny wzorzec

```python
sciezka = "uploads/" + user_input
```

### Lepszy kierunek

- użyj katalogu bazowego,
- znormalizuj ścieżkę,
- sprawdź, czy końcowa ścieżka nadal leży w dozwolonym miejscu.

---

## Dobre praktyki

- nie traktuj ścieżki użytkownika jako zaufanej,
- trzymaj jawny katalog bazowy,
- stosuj walidację nazw,
- minimalizuj liczbę miejsc, które mają dostęp do systemu plików.

---

## Podsumowanie

Path traversal to prosty do popełnienia, ale bardzo ważny błąd bezpieczeństwa.

Dobra kontrola ścieżek jest obowiązkowa wszędzie tam, gdzie użytkownik wpływa na dostęp do plików.

---

## Mini ściąga

Najważniejsze:

- nie ufaj nazwom plików od użytkownika,
- nie sklejaj ścieżek bez kontroli,
- sprawdzaj, czy końcowa ścieżka nie wychodzi poza dozwolony katalog.

---

## Ćwiczenia

1. Wyjaśnij, czym jest path traversal.
2. Podaj przykład niebezpiecznego inputu.
3. Wyjaśnij, czemu `../` jest groźne.
4. Wyjaśnij, jak ograniczyć dostęp do katalogu bazowego.
5. Wyjaśnij, czemu `pathlib` pomaga, ale nie załatwia wszystkiego.

---

## Przykładowe rozwiązania

### 1. Path traversal

To możliwość wyjścia poza dozwolony katalog przy dostępie do plików.

### 2. Niebezpieczny input

`../../hasla.txt`

### 3. Czemu `../`

Bo pozwala cofać się po drzewie katalogów.

### 4. Ograniczenie

Przez sprawdzenie, czy wynikowa ścieżka nadal należy do ustalonego katalogu bazowego.

### 5. `pathlib`

Bo poprawia czytelność pracy ze ścieżkami, ale nadal trzeba robić walidację i kontrole bezpieczeństwa.
