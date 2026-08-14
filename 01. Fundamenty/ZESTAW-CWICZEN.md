# Zestaw ćwiczeń praktycznych — 01. Fundamenty

Ćwiczenia są ułożone od najłatwiejszych do trudniejszych. Ich celem nie jest tylko "odhaczenie materiału", ale zmuszenie Cię do samodzielnego użycia tematów z działu.

Najlepiej:

- nie przeskakiwać od razu do końca,
- pisać kod samodzielnie bez kopiowania,
- uruchamiać każdy przykład,
- poprawiać własne błędy zamiast od razu patrzeć na rozwiązanie.

---

## Poziom 1 — podstawy zmiennych, typów i tekstu

1. Napisz program, który tworzy zmienne `imie`, `wiek`, `miasto` i wypisuje je w czytelnej formie.
2. Utwórz zmienne typów `int`, `float`, `str`, `bool` i wypisz ich typ przez `type()`.
3. Wczytaj od użytkownika dwie liczby i wypisz ich sumę, różnicę, iloczyn i iloraz.
4. Napisz program, który dla jednej liczby sprawdzi, czy jest dodatnia, ujemna czy równa zero.
5. Utwórz string z imieniem użytkownika i wypisz komunikat powitalny przez f-string.
6. Wczytaj tekst od użytkownika i wypisz go:
   - małymi literami,
   - wielkimi literami,
   - bez spacji z początku i końca.
7. Napisz program, który sprawdza, czy podana liczba jest parzysta.
8. Wypisz liczby od 1 do 20 przez pętlę `for`.
9. Wypisz liczby od 20 do 1 przez pętlę `while`.
10. Dla podanej liczby wypisz tabliczkę mnożenia od 1 do 10.

---

## Poziom 2 — warunki, truthy/falsy, porównania

11. Napisz program, który sprawdza, czy podany napis jest pusty.
12. Przygotuj listę i sprawdź warunkiem `if`, czy jest pusta, bez porównywania do `[]`.
13. Napisz funkcję, która zwraca `None`, jeśli liczba jest ujemna, a samą liczbę, jeśli jest nieujemna.
14. Pokaż różnicę między `is None` i `== None` na małym przykładzie.
15. Utwórz dwie listy o tej samej zawartości i pokaż różnicę między `==` i `is`.
16. Napisz przykład, w którym `0` jest poprawną wartością, ale zwykłe `if not x` może wprowadzać w błąd.
17. Przygotuj listę z wartościami truthy i falsy i policz, ile jest jednych i drugich.

---

## Poziom 3 — unpacking i funkcje wbudowane

18. Rozpakuj krotkę `("Anna", 29, "Krakow")` do trzech zmiennych.
19. Użyj extended unpacking, by z listy `[1, 2, 3, 4, 5]` wydzielić pierwszy element, środek i ostatni element.
20. Użyj `enumerate()` do wypisania numeru i wartości każdego elementu listy.
21. Użyj `zip()` do połączenia list `imiona` i `punkty`, a potem wypisz wynik w pętli.
22. Użyj `sorted()` do posortowania listy stringów po długości.
23. Napisz program, który używa `any()` do sprawdzenia, czy na liście wyników jest choć jedna wartość dodatnia.
24. Napisz program, który używa `all()` do sprawdzenia, czy wszystkie liczby na liście są dodatnie.
25. Użyj unpackingu przy wywołaniu funkcji z listy albo krotki.

---

## Poziom 4 — małe funkcje i logika

26. Napisz funkcję `czy_pelnoletni(wiek)`, która zwraca `True` albo `False`.
27. Napisz funkcję `normalizuj_nazwe(tekst)`, która usuwa zbędne spacje i zamienia tekst na małe litery.
28. Napisz funkcję `bezpieczne_dzielenie(a, b)`, która zwraca wynik dzielenia, a przy dzieleniu przez zero zwraca `None`.
29. Napisz funkcję, która przyjmuje listę liczb i zwraca:
   - największą,
   - najmniejszą,
   - średnią.
30. Napisz funkcję `parse_int(tekst)`, która próbuje zamienić string na `int`, a przy błędzie zwraca `None`.

---

## Poziom 5 — wyjątki i walidacja danych

31. Napisz program, który pyta użytkownika o liczbę tak długo, aż poda poprawny `int`.
32. Napisz program, który pobiera dwie liczby i bezpiecznie obsługuje:
   - zły tekst,
   - dzielenie przez zero.
33. Napisz program, który pobiera od użytkownika zdanie i liczy:
   - liczbę znaków,
   - liczbę słów,
   - liczbę znaków bez spacji.
34. Napisz program, który sprawdza, czy dane słowo jest palindromem.
35. Napisz prosty system logowania do konsoli:
   - użytkownik ma 3 próby podania poprawnego hasła,
   - po 3 błędach program kończy działanie.

---

## Poziom 6 — większe zadania

36. Napisz funkcję, która analizuje listę danych wejściowych i zwraca słownik z podsumowaniem:
   - liczba elementów,
   - liczba elementów truthy,
   - liczba elementów falsy.
37. Zbuduj mini program „rejestr ocen”:
   - dodawanie ocen,
   - liczenie średniej,
   - informacja, czy wszystkie oceny są zaliczone.
38. Napisz program, który pobiera dane użytkownika, waliduje wiek i pokazuje komunikaty przez f-stringi.
39. Napisz program, w którym świadomie użyjesz lokalnych i globalnych zmiennych, a potem wyjaśnisz, co się dzieje.

---

## Poziom 7 — zadania przekrojowe

40. Napisz program rejestracji użytkownika, który:
   - pobiera imię, wiek i miasto,
   - normalizuje tekst,
   - sprawdza poprawność wieku,
   - obsługuje błędne dane przez `try/except`,
   - pokazuje wynik przez f-string.
41. Napisz prosty kalkulator konsolowy:
   - pyta o dwie liczby,
   - pyta o operator,
   - używa `if/elif/else`,
   - obsługuje błędne wejście.
42. Napisz program analizy hasła:
   - sprawdza długość,
   - sprawdza, czy zawiera cyfry,
   - sprawdza, czy po `strip()` coś zostaje,
   - wypisuje wynik walidacji.
43. Napisz program, który pobiera kilka liczb od użytkownika i na końcu wypisuje:
   - największą,
   - najmniejszą,
   - liczbę dodatnich,
   - informację, czy wszystkie są różne od zera.
44. Zbuduj prosty formularz konsolowy, w którym użytkownik podaje dane tak długo, aż wpisze poprawny zestaw informacji.

---

## Zadanie końcowe

45. Zbuduj tekstowe „centrum użytkownika”, które:
   - pobiera dane użytkownika,
   - waliduje wiek,
   - normalizuje imię i miasto,
   - pokazuje komunikaty przez f-stringi,
   - obsługuje błędy wejścia,
   - wykorzystuje funkcje pomocnicze,
   - używa warunków, pętli i wyjątków.

Jeśli zrobisz to samodzielnie i rozumiesz każdą część rozwiązania, to fundamenty są naprawdę mocno opanowane.
