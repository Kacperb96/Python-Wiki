# Zestaw ćwiczeń praktycznych — 10. Testowanie

## Poziom 1 — podstawy pytest

1. Napisz pierwszy test sprawdzający wynik funkcji `dodaj()`.
2. Napisz test dla funkcji `jest_parzysta()`.
3. Napisz test dla funkcji `normalizuj_email()`.
4. Zgrupuj kilka testów w jednym pliku testowym.
5. Napisz test dla funkcji rzucającej wyjątek.

## Poziom 2 — lepszy pytest

6. Użyj `parametrize` do przetestowania kilku przypadków jednej funkcji.
7. Napisz fixture zwracającą przykładowego użytkownika.
8. Użyj fixture w kilku testach.
9. Napisz test dla błędnych danych wejściowych.
10. Napisz test dla granicznych wartości argumentu.

## Poziom 3 — mocking

11. Zamockuj funkcję wysyłającą mail.
12. Zamockuj klienta HTTP w serwisie integracyjnym.
13. Zamockuj repozytorium w serwisie biznesowym.
14. Sprawdź, czy mock został wywołany z odpowiednimi argumentami.

## Poziom 4 — coverage i Hypothesis

15. Uruchom coverage dla małego modułu i sprawdź, czego brakuje.
16. Dopisz testy tak, by zwiększyć coverage krytycznej funkcji.
17. Napisz test property-based dla funkcji, która powinna być przemienna, np. dodawanie.
18. Napisz test property-based dla funkcji normalizującej string.

## Poziom 5 — integracja i architektura testów

19. Napisz test dla serwisu, który korzysta z repozytorium i walidatora.
20. Napisz test integracyjny dla prostego endpointu API.
21. Napisz test sprawdzający scenariusz błędny i poprawny dla tej samej operacji.
22. Rozdziel testy jednostkowe od integracyjnych.

## Zadanie końcowe

23. Weź mały projekt z repo i zbuduj dla niego sensowny pakiet testów:
   - testy jednostkowe,
   - testy z parametryzacją,
   - testy wyjątków,
   - mocking zależności,
   - coverage,
   - przynajmniej 1 test property-based.
