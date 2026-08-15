# 29. Bezpieczenstwo zaawansowane

Ten folder domyka bardzo ważny obszar praktycznego Pythona: pisanie kodu, który nie tylko działa, ale też nie robi oczywistych błędów bezpieczeństwa.

To nie jest folder o "hakowaniu", tylko o:

- myśleniu defensywnym,
- ograniczaniu ryzyka,
- rozpoznawaniu typowych luk,
- unikaniu wzorców, które później kończą się incydentem.

W Pythonie wiele rzeczy da się zrobić szybko i wygodnie. Problem w tym, że część z tych wygodnych dróg bywa bardzo niebezpieczna:

- budowanie SQL przez f-stringi,
- wykonywanie poleceń z inputem użytkownika,
- upload plików bez kontroli,
- logowanie sekretów,
- zbyt szerokie uprawnienia,
- ślepe zaufanie bibliotekom i zależnościom.

Ten folder ma nauczyć Cię patrzenia na kod pytaniem:

`czy to jest tylko wygodne, czy też bezpieczne?`

## Co powinieneś umieć po tym folderze

Po solidnym przerobieniu tego działu powinieneś:

- rozumieć, czemu dane wejściowe są nieufne,
- wiedzieć, jak bezpiecznie myśleć o hasłach i ich przechowywaniu,
- rozróżniać podstawowe klasy problemów web security, takie jak `CSRF`, `XSS` i `SSRF`,
- rozumieć ryzyka związane z uploadem plików,
- wiedzieć, po co jest rate limiting i ochrona przed abuse,
- rozumieć model uprawnień i kontrolę dostępu,
- wiedzieć, jak postępować z sekretami i zależnościami,
- umieć rozpoznać częste antywzorce bezpieczeństwa w kodzie Pythona.

## Jak czytać ten folder

Najlepiej iść w tej kolejności:

1. `01` hashowanie haseł
2. `02` `CSRF`, `XSS`, `SSRF`
3. `03` bezpieczny upload plików
4. `04` rate limiting i abuse protection
5. `05` permissions model
6. `06` sekrety w chmurze
7. `07` dependency security
8. `ZESTAW-CWICZEN.md`

To daje sensowny porządek: od danych i użytkownika, przez aplikację webową, aż po bezpieczeństwo operacyjne i zależności.

## Ważna zasada

Bezpieczeństwo rzadko polega na jednej "magicznej" funkcji.

Najczęściej liczy się zestaw zdrowych decyzji:

- walidacja wejścia,
- bezpieczne API,
- brak zaufania do klienta,
- kontrola dostępu,
- ograniczenie uprawnień,
- sensowne logi,
- dobre zarządzanie sekretami,
- ostrożność przy bibliotekach.

## Jak korzystać z tego folderu

Kiedy czytasz przykład, nie pytaj tylko:

`czy rozumiem ten kod?`

Pytaj też:

- co tu może pójść źle?
- gdzie jest granica zaufania?
- co kontroluje użytkownik?
- czy ten mechanizm ogranicza ryzyko, czy tylko wygląda bezpiecznie?

To właśnie odróżnia "kod działa" od "kod jest dojrzały".
