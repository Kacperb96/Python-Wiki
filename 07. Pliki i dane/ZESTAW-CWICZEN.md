# Zestaw ćwiczeń praktycznych — 07. Pliki i dane

## Poziom 1 — pliki tekstowe

1. Zapisz prosty tekst do pliku.
2. Odczytaj cały plik i wypisz zawartość.
3. Dopisz nową linię do istniejącego pliku.
4. Wypisz plik linia po linii.
5. Zlicz liczbę linii w pliku tekstowym.

## Poziom 2 — kodowanie i ścieżki

6. Zapisz do pliku polskie znaki i odczytaj je poprawnie.
7. Pokaż użycie `encode()` i `decode()`.
8. Utwórz ścieżkę do pliku przez `pathlib`.
9. Utwórz katalog `raporty/2026` przez `pathlib`.
10. Znajdź wszystkie pliki `.md` w katalogu przez `glob()`.
11. Użyj `os.getenv()` do odczytu wartości środowiskowej.

## Poziom 3 — formaty danych

12. Zapisz słownik do pliku JSON.
13. Wczytaj JSON z pliku i odczytaj wybrane pole.
14. Zapisz listę użytkowników do CSV.
15. Odczytaj CSV przez `DictReader`.
16. Utwórz prosty plik INI i odczytaj go przez `configparser`.
17. Utwórz prosty XML i odczytaj z niego atrybut oraz tekst elementu.

## Poziom 4 — pliki binarne i SQLite

18. Zapisz kilka bajtów do pliku binarnego.
19. Skopiuj plik binarny do nowej lokalizacji.
20. Utwórz bazę `sqlite3` i tabelę `users`.
21. Dodaj kilka rekordów do tabeli.
22. Odczytaj rekordy i wypisz je.
23. Wyszukaj rekord po parametrze zapytania.

## Poziom 5 — praktyczne zadania z danymi

24. Napisz skrypt, który czyta plik tekstowy i zapisuje raport JSON z podstawowymi statystykami.
25. Napisz skrypt, który konwertuje CSV do JSON.
26. Napisz skrypt, który czyta XML i zapisuje wybrane dane do CSV.
27. Napisz prostą konfigurację aplikacji, która pobiera część ustawień z INI, a część z env vars.
28. Napisz program, który trzyma dane użytkowników w SQLite i pozwala:
   - dodać użytkownika,
   - wypisać użytkowników,
   - wyszukać użytkownika po imieniu.

## Zadanie końcowe

29. Zbuduj mini narzędzie „importer danych”:
   - czyta dane z JSON, CSV albo XML,
   - normalizuje je,
   - zapisuje do SQLite,
   - korzysta z `pathlib`,
   - dba o kodowanie,
   - obsługuje błędy plików i błędne dane.
