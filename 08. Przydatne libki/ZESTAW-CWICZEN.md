# Zestaw ćwiczeń praktycznych — 08. Przydatne libki

## Poziom 1 — `re`

1. Znajdź pierwszą liczbę w tekście.
2. Znajdź wszystkie liczby w tekście.
3. Sprawdź, czy string ma format `ABC-123`.
4. Zamień wszystkie cyfry na `*`.
5. Wyciągnij rok, miesiąc i dzień z daty.

## Poziom 2 — `itertools`

6. Połącz kilka list przez `chain()`.
7. Pobierz pierwsze 10 elementów z `count()`.
8. Wygeneruj wszystkie pary z dwóch list przez `product()`.
9. Wygeneruj wszystkie kombinacje 2-elementowe.
10. Użyj `groupby()` na posortowanych danych.

## Poziom 3 — `functools`

11. Użyj `partial()` do utworzenia funkcji `kwadrat`.
12. Użyj `reduce()` do policzenia sumy listy.
13. Napisz dekorator z `wraps`.
14. Dodaj `lru_cache` do funkcji Fibonacciego.
15. Użyj `cached_property` w małej klasie.

## Poziom 4 — `collections`

16. Użyj `Counter` do policzenia słów w tekście.
17. Użyj `defaultdict(list)` do grupowania rekordów.
18. Użyj `deque` do zbudowania kolejki.
19. Użyj `ChainMap` do nałożenia dwóch konfiguracji.
20. Użyj `namedtuple` do opisu punktu lub użytkownika.

## Poziom 5 — `typing` i `dataclasses`

21. Dodaj typy do kilku prostych funkcji.
22. Utwórz `TypedDict` dla obiektu JSON użytkownika.
23. Użyj `Literal` dla trybu `dev/prod`.
24. Zbuduj `dataclass` `User` z kilkoma polami.
25. Dodaj `default_factory` do listy tagów.
26. Dodaj `__post_init__` z prostą walidacją.

## Zadanie końcowe

27. Zbuduj mini moduł przetwarzania zamówień:
   - walidacja tekstu przez `re`,
   - grupowanie danych przez `defaultdict`,
   - analiza częstości przez `Counter`,
   - typowanie funkcji,
   - `dataclass` dla modelu danych,
   - `cached_property` albo `partial` w sensownym miejscu.
