# Rate limiting i abuse protection python

Nie każdy problem bezpieczeństwa wygląda jak "włamanie".

Czasem problemem jest zwykłe nadużycie:

- za dużo prób logowania,
- spam requestami,
- masowe zgadywanie kodów lub tokenów,
- nadmierne obciążenie endpointu,
- automatyczne scrapowanie danych.

Tu właśnie wchodzi `rate limiting` i szerzej rozumiane `abuse protection`.

## 1. Co to jest rate limiting

To ograniczenie liczby operacji w czasie.

Przykłady:

- maksymalnie 5 prób logowania w 10 minut,
- maksymalnie 100 requestów na minutę z jednego klucza API,
- maksymalnie 10 resetów hasła na godzinę dla jednego konta.

## 2. Po co to w ogóle robić

Rate limiting pomaga:

- utrudnić brute force,
- ograniczyć automatyczne nadużycia,
- chronić kosztowne endpointy,
- chronić system przed przeciążeniem,
- chronić użytkowników i zasoby.

## 3. Gdzie rate limiting ma sens

Szczególnie przy:

- logowaniu,
- resetach hasła,
- endpointach wysyłających SMS/e-mail,
- drogich operacjach wyszukiwania,
- publicznych API,
- generowaniu raportów,
- endpointach narażonych na scraping.

## 4. Co ograniczać

To zależy od systemu.

Można limitować po:

- IP,
- użytkowniku,
- kluczu API,
- sesji,
- kombinacji kilku cech.

Każde podejście ma plusy i minusy.

## 5. Czego rate limiting nie rozwiązuje sam

To nie jest pełne bezpieczeństwo.

Nie rozwiązuje sam:

- błędów autoryzacji,
- wycieku danych,
- złej walidacji wejścia,
- luk logicznych,
- problemów z uprawnieniami.

To mechanizm ograniczający tempo i skalę nadużycia, a nie naprawa całego systemu.

## 6. Częste błędy

- brak limitów na logowanie,
- zbyt łagodne limity tam, gdzie atak jest tani,
- zbyt agresywne limity psujące legalnym użytkownikom pracę,
- brak osobnych limitów dla kosztownych operacji,
- brak monitorowania, kiedy limit faktycznie jest trafiany.

## 7. Dobry komunikat i obserwowalność

Jeśli limit zadziała, system powinien:

- zwrócić czytelny komunikat,
- ewentualnie poinformować, kiedy można spróbować ponownie,
- zalogować zdarzenie,
- umożliwić monitoring takich przypadków.

Pseudo-output:

```text
status: 429 Too Many Requests
message: Sprobuj ponownie za 60 sekund
```

## 8. Abuse protection szerzej

Poza samym rate limitingiem liczy się też:

- wykrywanie nietypowych wzorców,
- captcha lub podobne mechanizmy tam, gdzie to sensowne,
- monitoring anomalii,
- blokady czasowe,
- alerty bezpieczeństwa,
- rozdzielenie limitów per typ operacji.

## Zadania

1. Wyjaśnij, po co daje się rate limiting na logowanie.
2. Podaj trzy miejsca w aplikacji, gdzie rate limiting ma duży sens.
3. Opisz, czemu zbyt agresywny limit też może być problemem.
