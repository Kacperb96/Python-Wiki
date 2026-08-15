# Zestaw ćwiczeń praktycznych — 16. Bezpieczeństwo

To nie jest dział, który warto "tylko przeczytać".

Najlepiej potraktować te ćwiczenia jak trening myślenia o ryzyku. W wielu zadaniach nie chodzi wyłącznie o napisanie kodu, ale o rozpoznanie:

- gdzie jest podatność,
- dlaczego jest groźna,
- jak ją ograniczyć,
- jak wygląda bezpieczniejsza wersja.

## Poziom 1 — myślenie bezpieczeństwem

1. Wypisz co najmniej 8 miejsc, z których do aplikacji mogą wejść nieufne dane.
2. Podaj 5 przykładów sekretów, których nie powinno być na sztywno w repo.
3. Wyjaśnij własnymi słowami różnicę między błędem funkcjonalnym a błędem bezpieczeństwa.
4. Weź prostą aplikację CLI albo API i wskaż w niej punkty wejścia, miejsca zapisu danych i miejsca ryzyka.
5. Opisz, czemu „działa poprawnie” nie oznacza jeszcze „jest bezpieczne”.

## Poziom 2 — walidacja danych

6. Napisz funkcję walidującą wiek: liczba całkowita, brak wartości ujemnych, sensowny górny limit.
7. Napisz walidację payloadu użytkownika zawierającego `name`, `email`, `age`.
8. Rozdziel walidację techniczną i walidację biznesową na jednym przykładzie.
9. Pokaż przykład, gdzie frontend waliduje dane, ale backend i tak musi zrobić to ponownie.
10. Napisz funkcję, która odrzuca puste stringi po `strip()`.
11. Zaprojektuj walidację listy ID przekazanej przez użytkownika.

## Poziom 3 — sekrety i konfiguracja

12. Odczytaj `API_TOKEN` z env var i obsłuż sytuację, gdy go brakuje.
13. Przygotuj `.env.example` dla małej aplikacji webowej.
14. Wypisz, które dane powinny być w env vars, a które nie wymagają takiego traktowania.
15. Opisz ryzyko wrzucenia prawdziwego `.env` do repozytorium.
16. Pokaż, jak oddzielić konfigurację developerską od produkcyjnej bez hardkodowania haseł.

## Poziom 4 — subprocess i command injection

17. Napisz bezpieczniejsze wywołanie `subprocess.run()` z listą argumentów.
18. Pokaż niebezpieczny przykład z `shell=True` i danymi od użytkownika.
19. Przerób ryzykowny kod budujący polecenie przez f-string na bezpieczniejszą wersję.
20. Wyjaśnij, kiedy `shell=True` naprawdę zwiększa ryzyko.
21. Pokaż przykład whitelisty dozwolonych komend lub argumentów.

## Poziom 5 — SQL injection

22. Napisz przykład podatnego zapytania SQL składanego przez string.
23. Popraw to zapytanie przy użyciu parametryzacji.
24. Wyjaśnij, dlaczego escaping ręczny nie jest dobrą strategią obrony.
25. Pokaż przykład filtrowania po `user_id`, który najpierw waliduje typ, a potem używa parametrów.
26. Opisz, co może zrobić atakujący, jeśli aplikacja ma podatne logowanie do bazy.

## Poziom 6 — path traversal i operacje na plikach

27. Pokaż przykład endpointu lub funkcji pobierającej plik po nazwie od użytkownika.
28. Wyjaśnij, jak może wyglądać atak typu path traversal.
29. Zaprojektuj bezpieczniejszą wersję ograniczoną do jednego katalogu bazowego.
30. Zastanów się, czy lepiej ufać ścieżce od użytkownika, czy mapować identyfikator pliku na ścieżkę po stronie serwera.
31. Pokaż przykład walidacji rozszerzeń plików i nazw plików.

## Poziom 7 — serializacja i nieufne dane

32. Wyjaśnij, czemu `pickle` nie powinien być używany do nieufnych danych z zewnątrz.
33. Zaprojektuj bezpieczniejszy przepływ: `JSON -> parse -> walidacja -> użycie`.
34. Porównaj `pickle` i `json` pod kątem bezpieczeństwa.
35. Pokaż przykład danych wejściowych, które są poprawnym JSON-em, ale nadal wymagają walidacji.
36. Opisz, czemu sam format danych nie gwarantuje bezpieczeństwa.

## Poziom 8 — mini audyt

37. Weź mały projekt Python i wypisz wszystkie miejsca wejścia danych.
38. Sprawdź, czy są tam sekrety w kodzie lub w repo.
39. Sprawdź, czy gdzieś są operacje na plikach, SQL albo `subprocess`.
40. Ułóż listę 5 najważniejszych poprawek bezpieczeństwa od najbardziej pilnych.

## Zadanie końcowe

41. Zrób mini audyt bezpieczeństwa małego projektu Python i przygotuj krótką notatkę:

- gdzie wchodzi input,
- co trzeba walidować,
- gdzie są sekrety,
- czy jest ryzyko SQL injection,
- czy jest ryzyko command injection,
- czy jest ryzyko path traversal,
- czy występuje niebezpieczna serializacja,
- jakie poprawki wdrożyłbyś najpierw,
- które ryzyka mają największy wpływ,
- czego jeszcze nie da się ocenić bez szerszego kontekstu systemu.

## Jak pracować z tym zestawem

Jeśli chcesz wyciągnąć z tego folderu maksimum, pracuj tak:

1. najpierw spróbuj samodzielnie wykryć problem,
2. potem napisz wersję podatną,
3. następnie popraw ją,
4. na końcu opisz własnymi słowami, co dokładnie było ryzykiem i dlaczego poprawka pomaga.

W bezpieczeństwie samo "to działa" nigdy nie wystarcza. Trzeba jeszcze umieć uzasadnić, czemu dane rozwiązanie jest bezpieczniejsze.
