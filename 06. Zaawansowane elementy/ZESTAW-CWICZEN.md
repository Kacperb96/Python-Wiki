# Zestaw ćwiczeń praktycznych — 06. Zaawansowane elementy

## Poziom 1 — iteratory i generatory

1. Napisz generator zwracający liczby od 1 do `n`.
2. Napisz generator zwracający tylko liczby nieparzyste.
3. Napisz generator zwracający kolejne kwadraty liczb.
4. Utwórz własny iterator po zakresie od `start` do `end`.
5. Napisz funkcję, która przyjmuje iterator i wypisuje jego elementy.

## Poziom 2 — context managers

6. Użyj `with open(...)` do bezpiecznej pracy z plikiem.
7. Napisz własny context manager klasowy, który wypisuje „start” i „koniec”.
8. Napisz context manager, który mierzy czas wykonania bloku `with`.
9. Napisz context manager do tymczasowej zmiany wartości jakiejś flagi konfiguracyjnej.

## Poziom 3 — elementy funkcyjne

10. Użyj `map()` do przekształcenia listy liczb.
11. Użyj `filter()` do odfiltrowania tylko dodatnich liczb.
12. Użyj `reduce()` do policzenia iloczynu listy liczb.
13. Porównaj czytelność wersji funkcyjnej i zwykłej pętli dla tego samego problemu.

## Poziom 4 — deskryptory i `__slots__`

14. Napisz klasę z `__slots__` i sprawdź, co da się do niej przypisać.
15. Napisz prosty deskryptor walidujący, że przypisana liczba jest dodatnia.
16. Użyj tego deskryptora w klasie `Product`.
17. Napisz drugi deskryptor walidujący długość stringa.

## Poziom 5 — model pamięci i zachowanie obiektów

18. Pokaż na przykładzie, jak współdzielone referencje wpływają na mutowalne obiekty.
19. Zademonstruj, kiedy generator jest korzystniejszy od listy dla dużego zbioru danych.
20. Napisz mały eksperyment pokazujący różnicę pamięciową między listą i generatorem.

## Zadanie końcowe

21. Zbuduj mini pipeline przetwarzania danych:
   - generator źródłowy,
   - filtr,
   - transformacja,
   - context manager mierzący czas,
   - walidacja przez deskryptor w klasie modelującej rekord.
