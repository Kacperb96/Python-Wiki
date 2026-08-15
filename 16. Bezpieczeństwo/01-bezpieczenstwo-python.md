# Bezpieczeństwo w Pythonie — podstawy

## O co chodzi w tym rozdziale

Bezpieczeństwo w programowaniu to nie jest temat tylko dla pentesterów albo ludzi od infrastruktury.

Programista Pythona też codziennie podejmuje decyzje, które wpływają na bezpieczeństwo aplikacji.

Przykłady:

- czy ufasz danym wejściowym,
- czy poprawnie walidujesz payload z API,
- czy nie trzymasz sekretów w kodzie,
- czy nie sklejasz SQL,
- czy bezpiecznie korzystasz z plików i poleceń systemowych,
- czy użytkownik może zrobić tylko to, co powinien.

Ten rozdział daje ogólny model myślenia, który będzie potrzebny w całym folderze.

## Najważniejsza zmiana myślenia

Początkujący programista często pyta:

- czy kod działa?

Bardziej doświadczony pyta też:

- czy kod da się łatwo zepsuć,
- czy ktoś może go nadużyć,
- czy błędne dane zrobią bałagan,
- czy użytkownik może uzyskać za dużo.

W bezpieczeństwie chodzi właśnie o to drugie spojrzenie.

## Co to znaczy, że dane są nieufne

Nieufne dane to wszystkie dane, które przychodzą z zewnątrz i nad którymi aplikacja nie ma pełnej kontroli.

To mogą być:

- dane z formularza,
- JSON z requestu HTTP,
- parametr URL,
- nazwa pliku,
- dane z CLI,
- dane z zewnętrznego API,
- zawartość pliku CSV,
- nagłówki HTTP,
- dane z kolejki,
- dane z bazy, jeśli wcześniej mogły zostać skażone.

To bardzo ważne: „dane z naszej bazy” też nie zawsze są w 100% zaufane, jeśli kiedyś weszły do niej z inputu użytkownika.

## Najczęstsze obszary ryzyka

W praktyce aplikacje Python najczęściej mają problemy w kilku miejscach.

### 1. Walidacja danych

Aplikacja przyjmuje dane w złym typie, złym formacie albo z niedozwoloną wartością.

### 2. Sekrety i konfiguracja

Hasła, tokeny albo klucze API trafiają do repo lub logów.

### 3. Baza danych

Zapytania są składane ręcznie i otwierają drogę do SQL injection.

### 4. Operacje systemowe

Kod uruchamia polecenia przez `subprocess` w sposób ryzykowny.

### 5. Pliki i ścieżki

Użytkownik może wpłynąć na odczyt pliku spoza dozwolonego katalogu.

### 6. Uprawnienia

Użytkownik jest zalogowany, ale może wykonać operację, której nie powinien móc wykonać.

## Bezpieczeństwo a poprawność

To nie to samo.

Kod może być funkcjonalnie poprawny i jednocześnie niebezpieczny.

### Przykład

```python
def get_user_file(filename):
    with open(f"uploads/{filename}", "r", encoding="utf-8") as f:
        return f.read()
```

Funkcjonalnie to działa.

Jeśli podasz:

```python
get_user_file("raport.txt")
```

to program odczyta plik.

Ale jeśli podasz:

```python
get_user_file("../../etc/passwd")
```

to funkcjonalnie dalej „działa”, tylko robi coś bardzo niebezpiecznego.

To właśnie różnica między:

- działa,
- działa bezpiecznie.

## Najważniejsze zasady na start

### Zasada 1: nie ufaj inputowi

Nawet jeśli dane pochodzą z twojego frontendu.

Frontend:

- można obejść,
- można podrobić request,
- może mieć błąd,
- może zostać zastąpiony innym klientem.

### Zasada 2: ograniczaj uprawnienia

Kod powinien mieć tylko taki dostęp, jaki jest naprawdę potrzebny.

### Zasada 3: nie trzymaj sekretów w kodzie

Sekrety trzymaj poza repo, najczęściej w env vars lub menedżerze sekretów.

### Zasada 4: używaj bezpieczniejszych interfejsów

Przykłady:

- parametryzowane SQL zamiast sklejanych stringów,
- lista argumentów w `subprocess.run()` zamiast `shell=True`,
- jawny katalog bazowy przy pracy z plikami.

### Zasada 5: myśl o nadużyciu, nie tylko o poprawnym użyciu

Nie pytaj tylko: „jak użytkownik ma używać tej funkcji?”

Pytaj też:

- jak może ją źle użyć,
- jak może ją obejść,
- co się stanie przy danych złośliwych lub absurdalnych.

## Autentykacja a autoryzacja

To dwa różne pojęcia.

### Autentykacja

Odpowiada na pytanie:

- kim jesteś?

Przykład:

- logowanie loginem i hasłem,
- token JWT,
- sesja użytkownika.

### Autoryzacja

Odpowiada na pytanie:

- co wolno ci zrobić?

Przykład:

- czy użytkownik A może usunąć zasób użytkownika B,
- czy zwykły user może wejść do panelu admina,
- czy można odczytać dany raport.

Bardzo częsty błąd: aplikacja poprawnie rozpoznaje użytkownika, ale źle ogranicza jego uprawnienia.

## Przykład myślenia o ryzyku

Wyobraź sobie endpoint:

```python
POST /orders
```

Na pierwszy rzut oka to tylko tworzenie zamówienia. Ale bezpieczeństwo każe zapytać:

- czy pola są walidowane,
- czy użytkownik może podać cudzy `user_id`,
- czy kwota nie jest ujemna,
- czy dane nie trafiają bezpiecznie do bazy,
- czy logi nie zapiszą danych wrażliwych,
- czy użytkownik nie może złożyć 1000 requestów naraz.

To pokazuje, że bezpieczeństwo bardzo często jest po prostu uważniejszym projektowaniem.

## Typowe błędy początkujących

- hardkodowanie tokenów i haseł,
- brak walidacji danych wejściowych,
- sklejanie SQL przez f-string,
- używanie `shell=True` bez potrzeby,
- ufanie ścieżkom od użytkownika,
- logowanie wrażliwych danych,
- brak sprawdzania uprawnień,
- przekonanie, że „to tylko lokalne narzędzie”.

## Mini przykład: dobra i zła wersja

### Zła wersja

```python
API_TOKEN = "sekretny-token"
query = f"SELECT * FROM users WHERE email = '{email}'"
subprocess.run(f"echo {filename}", shell=True)
```

Problemy:

- sekret w kodzie,
- ryzyko SQL injection,
- ryzyko command injection.

### Lepsza wersja

```python
import os
import sqlite3
import subprocess

api_token = os.getenv("API_TOKEN")

conn = sqlite3.connect("app.db")
cur = conn.cursor()
cur.execute("SELECT * FROM users WHERE email = ?", (email,))

subprocess.run(["echo", filename], check=True)
```

To nie rozwiązuje wszystkiego, ale już ustawia kod na dużo bezpieczniejszym torze.

## Checklista bezpieczeństwa dla małego projektu

Przy dowolnym małym projekcie Python przejdź przez takie pytania:

- Skąd wchodzą dane do systemu?
- Czy są walidowane?
- Czy w kodzie są sekrety?
- Czy gdzieś składam SQL ręcznie?
- Czy używam `subprocess` z danymi od użytkownika?
- Czy użytkownik wpływa na ścieżki plików?
- Czy sprawdzam uprawnienia użytkownika?
- Czy logi nie wyciekają danych wrażliwych?

## Szybka ściąga

Bezpieczeństwo na poziomie programisty to głównie dobre nawyki:

- nie ufaj inputowi,
- waliduj wcześnie,
- trzymaj sekrety poza kodem,
- nie sklejaj SQL,
- ostrożnie używaj `subprocess`,
- kontroluj ścieżki plików,
- odróżniaj autentykację od autoryzacji.

## Ćwiczenia

1. Wypisz 10 źródeł nieufnych danych w typowej aplikacji Python.
2. Wyjaśnij różnicę między „błąd funkcjonalny” a „błąd bezpieczeństwa”.
3. Podaj przykład sytuacji, w której użytkownik jest poprawnie zalogowany, ale nie powinien móc wykonać danej operacji.
4. Znajdź w swoim kodzie przykład miejsca, gdzie input trafia do dalszej logiki bez walidacji.
5. Zrób krótką checklistę bezpieczeństwa dla własnego mini projektu.

## Najważniejsze do zapamiętania

- Bezpieczeństwo zaczyna się od sposobu myślenia, nie od jednej biblioteki.
- Input z zewnątrz jest nieufny.
- Kod może działać poprawnie funkcjonalnie i jednocześnie być niebezpieczny.
- Najczęstsze ryzyka w Pythonie to walidacja, sekrety, SQL, `subprocess`, pliki i uprawnienia.
- Dobre bezpieczeństwo to zwykle zbiór prostych, konsekwentnych nawyków.
