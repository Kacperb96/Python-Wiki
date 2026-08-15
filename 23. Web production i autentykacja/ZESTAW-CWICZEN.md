# Zestaw ćwiczeń praktycznych — 23. Web production i autentykacja

Te ćwiczenia mają zmusić Cię nie tylko do pamiętania definicji, ale do podejmowania decyzji projektowych.

## Poziom 1

1. Napisz własnymi słowami różnicę między cookie, sesją i JWT.
2. Rozpisz flow logowania opartego o sesję krok po kroku.
3. Rozpisz flow logowania opartego o access token i refresh token.
4. Wytłumacz, czym różni się uwierzytelnianie od autoryzacji.
5. Podaj po trzy przykłady roli i uprawnienia w systemie zamówień.

## Poziom 2

1. Zaprojektuj prosty model autoryzacji dla aplikacji z rolami `admin`, `support`, `customer`.
2. Napisz funkcję `has_permission(role, permission)` i przetestuj ją na kilku przykładach.
3. Zasymuluj prosty rate limiting: maksymalnie 3 requesty na użytkownika.
4. Napisz pseudokod endpointu `/refresh`, który odświeża access token na podstawie refresh tokena.
5. Wypisz bezpieczniejsze ustawienia cookie dla sesji i wyjaśnij, po co są potrzebne.

## Poziom 3

1. Porównaj sesje i JWT dla trzech typów systemów:
   - klasyczna aplikacja webowa,
   - publiczne API,
   - system z wieloma usługami.
2. Opisz ryzyka wynikające z trzymania zbyt wielu danych w JWT.
3. Zaprojektuj limity dla endpointów:
   - `/login`,
   - `/reset-password`,
   - `/reports/export`.
4. Opisz przypadek, w którym sama rola nie wystarcza i trzeba brać pod uwagę właściciela zasobu.
5. Wyjaśnij, czemu CORS nie rozwiązuje problemu autoryzacji backendu.

## Zadania praktyczne z kodem

1. Zaimplementuj prosty magazyn sesji jako słownik w Pythonie i funkcje:
   - `login(user_id)`,
   - `get_current_user(session_id)`,
   - `logout(session_id)`.
2. Zaimplementuj prostą walidację payloadu tokena z polem `exp`.
3. Napisz dekorator lub wrapper, który sprawdza, czy użytkownik ma dane uprawnienie przed wykonaniem funkcji.
4. Napisz prostą symulację middleware logującego request i response.
5. Zaimplementuj najprostszy rate limiter oparty o liczenie requestów.

## Większe zadania projektowe

1. Zbuduj pseudokod albo prosty szkic modułu auth z endpointami:
   - `POST /login`,
   - `POST /refresh`,
   - `POST /logout`,
   - `GET /me`.
2. Rozpisz, gdzie w tym module użyjesz:
   - access tokena,
   - refresh tokena,
   - cookie,
   - middleware,
   - rate limitingu.
3. Zaprojektuj mapę ról i uprawnień dla systemu `orders`.
4. Rozpisz trzy testy unitowe, trzy integracyjne i dwa E2E dla auth flow.
5. Opisz dwa realistyczne błędy produkcyjne, które mogą pojawić się w takim systemie.

## Zadanie końcowe

Zaprojektuj mini backend dla modułu `orders` i odpowiedz pisemnie na pytania:

1. Czy użyłbyś sesji czy JWT i dlaczego?
2. Gdzie trzymałbyś access token albo `session_id`?
3. Czy potrzebujesz refresh tokena?
4. Jakie role i uprawnienia miałby system?
5. Które endpointy dostałyby rate limiting?
6. Czy frontend wymaga konfiguracji CORS?
7. Jakie 2-3 middleware dodałbyś na start?
8. Jakie trzy testy byłyby najważniejsze na początek?
9. Jak wyglądałaby strategia wylogowania użytkownika?
10. Jakie dwa błędy produkcyjne przewidujesz jako najbardziej prawdopodobne?

## Dodatkowe zadanie myślowe

Masz aplikację z frontendem na `https://app.example.com` i backendem na `https://api.example.com`.

Odpowiedz:

1. Czy to ten sam origin?
2. Czy CORS ma tu znaczenie?
3. Jakie ryzyka bezpieczeństwa dalej istnieją mimo poprawnej konfiguracji CORS?
4. Kiedy lepsze byłyby sesje, a kiedy tokeny?
5. Co może pójść źle przy refresh tokenie trzymanym w cookie?

## Zadanie debuggingowe

Użytkownicy zgłaszają: "po kilkunastu minutach aplikacja czasem wyrzuca mnie do logowania".

Odpowiedz krok po kroku:

1. Jakie są pierwsze hipotezy?
2. Co sprawdzisz po stronie backendu?
3. Co sprawdzisz po stronie klienta?
4. Jakie logi byłyby tu najbardziej pomocne?
5. Jak odróżnisz problem z access tokenem od problemu z refreshem albo CORS?

## Najważniejszy cel tych ćwiczeń

Po zrobieniu tego zestawu powinieneś nie tylko znać słowa typu `JWT`, `refresh token`, `CORS` czy `rate limiting`, ale rozumieć:

- po co istnieją,
- jakie rozwiązują problemy,
- jakie mają ograniczenia,
- kiedy naprawdę warto ich użyć,
- jak składają się w jeden prawdziwy system auth.
