# Zestaw ćwiczeń praktycznych — 24. Bazy danych zaawansowane

Te ćwiczenia mają pomóc Ci przejść od samych pojęć do decyzji projektowych i diagnozowania realnych problemów z bazą.

## Poziom 1

1. Wyjaśnij własnymi słowami, po co istnieje indeks i czemu nie jest darmowy.
2. Podaj przykład tabeli, w której indeks na `email` ma sens, a indeks na `is_active` może nie dawać tak dużo.
3. Wytłumacz różnicę między normalizacją i denormalizacją.
4. Opisz prosty przykład lost update.
5. Wyjaśnij, czym deadlock różni się od zwykłego wolnego query.

## Poziom 2

1. Zaprojektuj prosty model danych dla systemu zamówień w wersji bardziej znormalizowanej.
2. Wskaż dwa miejsca, gdzie w tym samym systemie mogłaby mieć sens świadoma denormalizacja.
3. Rozpisz przykład transakcji, w której dwa requesty mogą wejść sobie w drogę.
4. Porównaj offset pagination i keyset pagination dla listy zamówień.
5. Opisz, jakie ryzyka niesie soft delete, jeśli zespół zapomina o filtrowaniu rekordów.

## Poziom 3

1. Zaprojektuj plan optymalizacji endpointu:
   - `GET /users/42/orders`,
   - z filtrem po statusie,
   - z sortowaniem po `created_at`.
2. Opisz, jak ograniczyć ryzyko deadlocków w systemie przelewów między kontami.
3. Zaprojektuj prosty audit log dla zmian statusu zamówienia.
4. Wypisz pięć pytań, które zadałbyś przed dodaniem nowego indeksu.
5. Opisz, które query i zachowania bazy monitorowałbyś w produkcji w pierwszej kolejności.

## Zadania praktyczne z kodem

1. Napisz prostą symulację magazynu danych w Pythonie i pokaż przykład problemu lost update.
2. Napisz prostą funkcję paginacji po liście w stylu offset oraz drugą w stylu cursor/keyset.
3. Zaimplementuj prosty model soft delete w Pythonie z polem `deleted_at`.
4. Napisz szkic funkcji `has_permission_to_restore(record)` dla rekordu usuniętego logicznie.
5. Zrób prostą symulację audit logu jako listy zdarzeń.

## Większe zadania projektowe

1. Zaprojektuj bazę dla modułu `orders`, która obsłuży:
   - listę zamówień,
   - historię zmian statusu,
   - usuwanie logiczne,
   - szybkie filtrowanie po użytkowniku i statusie.
2. Opisz, które kolumny rozważyłbyś do indeksowania i dlaczego.
3. Zaprojektuj strategię paginacji dla:
   - panelu admina,
   - publicznego API,
   - feedu najnowszych zdarzeń.
4. Rozpisz, gdzie w systemie mogą pojawić się konflikty współbieżności.
5. Opisz, jakie wzorce kodu aplikacyjnego pomogą ograniczyć koszt pracy z bazą.

## Zadanie końcowe

Wyobraź sobie, że masz backend obsługujący sklep internetowy.

Odpowiedz pisemnie:

1. Jakie tabele byłyby podstawowe?
2. Gdzie dałbyś indeksy na start?
3. Czy zastosowałbyś soft delete, a jeśli tak, to gdzie?
4. Jak wyglądałaby historia zmian zamówienia?
5. Jakiego typu paginacji użyłbyś dla listy zamówień klienta?
6. Gdzie widzisz ryzyko deadlocków albo konfliktów współbieżności?
7. Jakie trzy zasady pracy z bazą narzuciłbyś zespołowi od początku?

## Zadanie debuggingowe

Masz objaw:

- lista zamówień zaczęła bardzo zwalniać,
- dalsze strony są dużo wolniejsze niż pierwsze,
- czasem użytkownik widzi "przeskakujące" rekordy,
- support raportuje sporadyczne błędy przy równoczesnych zmianach statusu.

Odpowiedz krok po kroku:

1. Jakie są pierwsze hipotezy?
2. Czy problem bardziej pachnie indeksem, paginacją, współbieżnością czy wszystkim naraz?
3. Jakie query sprawdziłbyś najpierw?
4. Co logowałbyś i mierzył?
5. Jakie poprawki wdrażałbyś najpierw, a jakie później?

## Zadanie przekrojowe

Na podstawie pliku `08-case-study-orders-baza-python.md` zaprojektuj własną wersję modułu `orders` i odpowiedz:

1. Jakie query byłyby hot pathem?
2. Które indeksy wspierałyby listę zamówień użytkownika?
3. Czy lista supportu używałaby offset czy keyset pagination?
4. Jak przechowywałbyś historię statusów?
5. Gdzie zastosowałbyś soft delete, a gdzie twarde usuwanie?
6. Jak skróciłbyś transakcję zmiany statusu?
7. Jakie dwa testy integracyjne byłyby najważniejsze dla tego modułu?

## Najważniejszy cel tych ćwiczeń

Po zrobieniu tego zestawu powinieneś nie tylko znać słowa typu `indeks`, `deadlock`, `isolation level`, `soft delete` czy `keyset pagination`, ale rozumieć:

- po co istnieją,
- jakie problemy rozwiązują,
- jakie mają koszty,
- kiedy naprawdę warto ich użyć w projekcie Pythonowym,
- jak łączą się w jednym większym module danych.
