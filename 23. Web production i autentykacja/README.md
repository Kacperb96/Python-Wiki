# 23. Web production i autentykacja

Ten folder zbiera tematy, które pojawiają się bardzo szybko, gdy Python wychodzi poza ćwiczenia i zaczyna obsługiwać prawdziwe API albo aplikację webową.

To nie jest dział o jednym frameworku. To dział o pojęciach i decyzjach, które przewijają się niezależnie od tego, czy pracujesz we Flasku, FastAPI, Django czy własnej architekturze.

## Cel folderu

Po przerobieniu tego działu powinieneś:

- rozumieć różnicę między sesją, cookie, tokenem i JWT,
- wiedzieć, kiedy sesje są prostsze i bezpieczniejsze niż tokeny,
- rozumieć, po co istnieje OAuth2 i gdzie ludzie mylą go z logowaniem,
- umieć odróżnić access token od refresh tokena,
- rozumieć podstawy autoryzacji: role, uprawnienia, scope'y,
- wiedzieć, po co istnieje rate limiting,
- rozumieć, czym naprawdę jest CORS i dlaczego middleware ma znaczenie produkcyjne,
- umieć spojrzeć na auth jako na cały przepływ systemowy, a nie pojedynczy temat.

## Jak czytać ten dział

Najlepiej iść po kolei:

1. `01-sesje-i-cookies-python.md`
2. `02-jwt-python.md`
3. `03-oauth2-podstawy-praktyczne-python.md`
4. `04-refresh-tokeny-python.md`
5. `05-role-i-uprawnienia-python.md`
6. `06-rate-limiting-python.md`
7. `07-cors-i-middleware-python.md`
8. `08-case-study-mini-backend-auth-python.md`
9. `09-testy-i-bledy-produkcjne-auth-python.md`
10. `ZESTAW-CWICZEN.md`

Ta kolejność ma sens, bo najpierw budujesz intuicję o stanie użytkownika, potem o tokenach, potem o autoryzacji i bezpieczeństwie całego flow, a na końcu spinasz to w większy case study i testowanie.

## Jak myśleć o tym folderze

Najważniejsze pytania, które warto sobie zadawać podczas nauki:

- gdzie jest stan użytkownika,
- kto potwierdza tożsamość użytkownika,
- kto decyduje, co wolno zrobić,
- jak długo dane uwierzytelniające są ważne,
- co się stanie po kradzieży tokena albo cookie,
- jak backend broni się przed nadużyciami,
- jak cały flow zachowuje się po błędzie, wylogowaniu albo wygaśnięciu tokena.

## Najczęstsze pomyłki początkujących

- mylenie uwierzytelniania z autoryzacją,
- traktowanie JWT jako "zawsze lepszego" rozwiązania,
- wrzucanie w token zbyt wielu danych,
- przechowywanie wrażliwych danych po stronie klienta,
- brak rozróżnienia między access tokenem i refresh tokenem,
- brak myślenia o wylogowaniu, wygaszaniu sesji i unieważnianiu tokenów,
- traktowanie CORS jako mechanizmu bezpieczeństwa backendu,
- brak limitowania requestów do logowania i endpointów wrażliwych,
- skupienie się tylko na tokenie zamiast na całym systemie auth.

## Co tutaj jest najważniejsze praktycznie

W realnym projekcie liczą się nie tylko definicje, ale przede wszystkim decyzje:

- czy wybrać sesję czy token,
- czy token ma być trzymany w `HttpOnly cookie`,
- jak ustawić czas życia tokenów,
- jak zorganizować role i uprawnienia,
- jak ograniczać spam i brute force,
- jak ustawić middleware i nagłówki,
- jak testować cały flow od logowania do autoryzacji endpointów,
- jak diagnozować błędy `401`, `403`, problemy z CORS i wygasaniem sesji.

## Jak ten dział łączy się z resztą repo

Ten folder dobrze łączy się z wcześniejszymi działami o:

- funkcjach i modułach,
- wyjątkach,
- debugowaniu,
- testowaniu,
- projektowaniu API,
- jakości kodu.

Tutaj teoria z wcześniejszych folderów zaczyna naprawdę pracować w praktycznym systemie.

## Po czym poznasz, że temat rozumiesz

Po przeczytaniu plików powinieneś umieć własnymi słowami odpowiedzieć:

- czym różni się uwierzytelnianie od autoryzacji,
- kiedy wybrałbyś sesje zamiast JWT,
- jak wygląda typowy flow access + refresh token,
- co chroni `HttpOnly`, `Secure` i `SameSite`,
- czym różni się rola od pojedynczego uprawnienia,
- czemu rate limiting nie jest tylko "optymalizacją",
- dlaczego CORS nie naprawia problemów bezpieczeństwa backendu,
- jak zaprojektować prosty backend auth od logowania do wylogowania,
- co i na jakim poziomie testować w auth flow,
- jak debugować częste problemy produkcyjne w autentykacji.

## Docelowy efekt

Po opanowaniu tego folderu nie będziesz jeszcze ekspertem od bezpieczeństwa aplikacji webowych, ale będziesz mieć bardzo sensowny i praktyczny fundament do pracy z prawdziwymi backendami w Pythonie.
