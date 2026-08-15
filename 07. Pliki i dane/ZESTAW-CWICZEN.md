# Zestaw ćwiczeń praktycznych — 07. Pliki i dane

## Poziom 1 — pliki tekstowe

1. Zapisz prosty tekst do pliku.
2. Odczytaj cały plik i wypisz zawartość.
3. Dopisz nową linię do istniejącego pliku.
4. Wypisz plik linia po linii.
5. Zlicz liczbę linii w pliku tekstowym.
6. Zlicz liczbę słów w pliku tekstowym.
7. Wczytaj plik i zapisz jego zawartość wielkimi literami do nowego pliku.
8. Połącz zawartość dwóch plików tekstowych w trzeci plik.

## Poziom 2 — tryby plików i bezpieczna praca

9. Pokaż różnicę między trybami `r`, `w`, `a`.
10. Napisz skrypt, który tworzy plik tylko wtedy, gdy jeszcze nie istnieje.
11. Sprawdź, co się stanie przy próbie otwarcia nieistniejącego pliku do odczytu.
12. Dodaj obsługę `FileNotFoundError`.
13. Napisz funkcję bezpiecznie odczytującą plik i zwracającą `None` przy błędzie.
14. Napisz funkcję zapisującą listę stringów do pliku po jednej linii.
15. Napisz funkcję kopiującą plik tekstowy.

## Poziom 3 — kodowanie i bajty

16. Zapisz do pliku polskie znaki i odczytaj je poprawnie przez `utf-8`.
17. Pokaż użycie `encode()` i `decode()`.
18. Sprawdź typ obiektu po `encode()` i po zwykłym stringu.
19. Zapisz tekst jako bajty do pliku binarnego.
20. Odczytaj plik binarny i zdekoduj go do tekstu.
21. Celowo użyj złego kodowania i zobacz, jaki błąd może się pojawić.
22. Napisz krótki przykład pokazujący różnicę między `str` i `bytes`.

## Poziom 4 — ścieżki i katalogi

23. Utwórz ścieżkę do pliku przez `pathlib.Path`.
24. Utwórz katalog `raporty/2026` przez `pathlib`.
25. Sprawdź, czy dany plik istnieje.
26. Znajdź wszystkie pliki `.md` w katalogu przez `glob()`.
27. Wypisz wszystkie pliki i katalogi w wybranym folderze.
28. Zmień rozszerzenie pliku przez `Path.with_suffix()`.
29. Zbuduj skrypt, który tworzy katalog, jeśli go nie ma.
30. Użyj `os.getenv()` do odczytu wartości środowiskowej.

## Poziom 5 — pliki binarne i operacje systemowe

31. Zapisz kilka bajtów do pliku binarnego.
32. Odczytaj plik binarny i wypisz surowe bajty.
33. Skopiuj plik binarny do nowej lokalizacji.
34. Sprawdź rozmiar pliku przez `os.path.getsize()` albo `Path.stat()`.
35. Napisz skrypt wypisujący nazwy i rozmiary plików w katalogu.
36. Napisz skrypt czyszczący pusty katalog testowy.

## Poziom 6 — JSON

37. Zapisz słownik do pliku JSON.
38. Wczytaj JSON z pliku i odczytaj wybrane pole.
39. Zapisz listę słowników do pliku JSON z ładnym formatowaniem.
40. Odczytaj JSON i wypisz dane użytkowników w czytelnej formie.
41. Napisz funkcję konwertującą dane Pythona do JSON stringa.
42. Napisz funkcję parsującą JSON string do obiektu Pythona.
43. Obsłuż błąd niepoprawnego JSON-a.

## Poziom 7 — CSV i konfiguracja

44. Zapisz listę użytkowników do CSV.
45. Odczytaj CSV przez `csv.reader`.
46. Odczytaj CSV przez `csv.DictReader`.
47. Zapisz CSV przez `csv.DictWriter`.
48. Utwórz prosty plik INI i odczytaj go przez `configparser`.
49. Pobierz z INI nazwę sekcji i kilka kluczy.
50. Połącz konfigurację z pliku INI z wartością z `os.getenv()`.

## Poziom 8 — XML i SQLite

51. Utwórz prosty XML i odczytaj z niego tekst elementu.
52. Odczytaj z XML atrybut wybranego elementu.
53. Utwórz bazę `sqlite3` i tabelę `users`.
54. Dodaj kilka rekordów do tabeli.
55. Odczytaj rekordy i wypisz je.
56. Wyszukaj rekord po parametrze zapytania.
57. Zaktualizuj rekord w tabeli.
58. Usuń rekord z tabeli.
59. Napisz zapytanie z `WHERE` i parametrem.
60. Zamknij połączenie z bazą poprawnie nawet przy błędzie.

## Poziom 9 — zadania przekrojowe

61. Napisz skrypt, który czyta plik tekstowy i zapisuje raport JSON z podstawowymi statystykami.
62. Napisz skrypt, który konwertuje CSV do JSON.
63. Napisz skrypt, który czyta XML i zapisuje wybrane dane do CSV.
64. Napisz prostą konfigurację aplikacji, która pobiera część ustawień z INI, a część z env vars.
65. Napisz program, który trzyma dane użytkowników w SQLite i pozwala:

- dodać użytkownika,
- wypisać użytkowników,
- wyszukać użytkownika po imieniu.

66. Napisz skrypt, który przechodzi po katalogu i zapisuje listę plików do JSON.
67. Napisz skrypt, który znajduje wszystkie pliki `.txt` i scala ich treść do jednego raportu.

## Zadanie końcowe

68. Zbuduj mini narzędzie „importer danych”:

- czyta dane z JSON, CSV albo XML,
- normalizuje je,
- zapisuje do SQLite,
- korzysta z `pathlib`,
- dba o kodowanie,
- obsługuje błędy plików i błędne dane.

Pokaż przy tym, że rozumiesz:

- tryby otwierania plików,
- różnicę między tekstem i bajtami,
- ścieżki i katalogi,
- podstawowe formaty danych,
- bezpieczne użycie SQLite,
- obsługę błędów podczas pracy z plikami i danymi.

## Dodatkowe zadania — `tempfile` i serializacja modeli

69. Utwórz plik tymczasowy przez `TemporaryFile()` i odczytaj jego zawartość.
70. Użyj `NamedTemporaryFile()` i wypisz jego ścieżkę.
71. Utwórz katalog tymczasowy przez `TemporaryDirectory()` i zapisz tam plik przez `pathlib`.
72. Zbuduj `dataclass` `User` i zamień ją na słownik przez `asdict()`.
73. Zbuduj model `Order` z `Enum` statusu i przygotuj JSON-friendly payload.
74. Odczytaj JSON i zamień string statusu z powrotem na `Enum`.
