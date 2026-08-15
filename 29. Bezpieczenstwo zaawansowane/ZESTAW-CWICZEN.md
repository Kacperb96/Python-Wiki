# Zestaw cwiczen praktycznych - 29. Bezpieczenstwo zaawansowane

Ten zestaw ma sprawdzić, czy rozumiesz nie tylko słowa, ale też praktyczne decyzje bezpieczeństwa.

## Poziom 1 - Podstawy

### Zadanie 1

Wyjaśnij własnymi słowami:

- czemu dane wejściowe są nieufne,
- czemu frontend nie jest granicą bezpieczeństwa,
- czemu "wewnętrzne narzędzie" też może mieć poważne luki.

### Zadanie 2

Podaj po dwa przykłady:

- walidacji technicznej,
- walidacji biznesowej,
- danych, których nie wolno logować.

### Zadanie 3

Wyjaśnij różnicę między:

- uwierzytelnianiem,
- autoryzacją,
- własnością zasobu.

## Poziom 2 - Analiza przypadków

### Zadanie 4

Masz system, który przechowuje hasła jako zwykłe stringi w bazie.

Opisz:

- co jest tu źle,
- jakie ryzyko to tworzy,
- jak powinien wyglądać poprawny kierunek naprawy.

### Zadanie 5

Masz taki kod:

```python
username = input("Login: ")
query = f"SELECT * FROM users WHERE username = '{username}'"
```

Wyjaśnij:

- co jest tu ryzykowne,
- jak to poprawić,
- czemu sama ręczna "sanityzacja" stringa nie jest dobrym rozwiązaniem.

### Zadanie 6

Masz upload plików, w którym ścieżka zapisu zależy bezpośrednio od nazwy od użytkownika.

Opisz:

- co może pójść źle,
- jak zmienić projekt,
- jakie dodatkowe kontrole dodać.

### Zadanie 7

Masz endpoint logowania bez żadnych limitów prób.

Wyjaśnij:

- co to umożliwia,
- jak pomógłby rate limiting,
- co jeszcze poza samym limitem warto monitorować.

## Poziom 3 - Myślenie projektowe

### Zadanie 8

Zaprojektuj bezpieczniejsze logowanie zdarzeń w systemie użytkowników.

Uwzględnij:

- jakie eventy warto logować,
- jakich danych unikać,
- co maskować,
- jakie zdarzenia powinny podnosić alert.

### Zadanie 9

Masz endpoint:

`GET /invoices/{invoice_id}`

Użytkownik powinien widzieć tylko własne faktury.

Rozpisz:

1. co trzeba sprawdzić,
2. gdzie początkujący robią błąd,
3. co może się stać, jeśli sprawdzisz tylko "czy user jest zalogowany".

### Zadanie 10

Masz projekt, w którym:

- sekrety siedzą w kodzie,
- pełne payloady trafiają do logów,
- jedna rola admina ma praktycznie wszystko,
- zależności nie były aktualizowane od dawna.

Rozpisz plan naprawy krok po kroku.

## Poziom 4 - Zadanie przekrojowe

### Zadanie 11

Przygotuj checklistę bezpieczeństwa dla małej aplikacji Python.

Minimum 15 punktów.

Powinna obejmować:

- hasła,
- input,
- SQL,
- upload plików,
- kontrolę dostępu,
- sekrety,
- logi,
- zależności.

### Zadanie 12

Opisz mini incydent:

- token wyciekł do logów,
- logi były wysyłane do zewnętrznego systemu,
- część użytkowników zgłasza nietypowe działania kont.

Masz rozpisać:

1. objaw,
2. ryzyko,
3. pierwsze działania,
4. rotację i ograniczenie szkód,
5. analizę przyczyny,
6. działania zapobiegawcze na przyszłość.

### Zadanie 13

Zaprojektuj mini moduł "bezpiecznego API" w Pythonie.

Opisz:

- walidację wejścia,
- ochronę haseł,
- kontrolę dostępu,
- limity nadużyć,
- bezpieczne logowanie,
- obsługę sekretów,
- podejście do zależności.

Jeżeli potrafisz dobrze rozwiązać większość tych zadań, to znaczy, że masz już naprawdę sensowną bazę bezpieczeństwa aplikacyjnego w Pythonie.
