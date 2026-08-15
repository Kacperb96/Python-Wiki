# Sekrety i zmienne środowiskowe w Pythonie

## Czym są sekrety

Sekrety to dane, które dają dostęp do systemów, zasobów albo uprzywilejowanych operacji.

Przykłady:

- hasło do bazy danych,
- token API,
- klucz do podpisywania JWT,
- sekret integracyjny,
- hasło do SMTP,
- credentiale do chmury,
- prywatne klucze.

Jeśli takie dane wyciekną, skutki mogą być bardzo poważne.

## Najgorszy nawyk: sekret w kodzie

### Zły przykład

```python
DB_PASSWORD = "super_tajne_haslo"
API_TOKEN = "abc123sekret"
JWT_SECRET = "moj-super-secret"
```

Na pierwszy rzut oka to wygodne.

W praktyce to bardzo zły pomysł, bo sekret może trafić do:

- repozytorium,
- historii commitów,
- screenshotów,
- logów,
- cudzych forków,
- kopii lokalnych innych osób.

Nawet jeśli później usuniesz taki sekret z pliku, on może nadal istnieć w historii gita.

## Dlaczego env vars są lepsze

Zmienne środowiskowe pozwalają oddzielić:

- kod aplikacji,
- od wrażliwej konfiguracji.

Dzięki temu:

- nie trzymasz sekretów w repo,
- możesz mieć inne wartości dla dev/staging/prod,
- łatwiej zarządzać konfiguracją między środowiskami,
- ograniczasz ryzyko przypadkowego wycieku.

## Podstawowy odczyt env var

```python
import os

api_token = os.getenv("API_TOKEN")
print(api_token)
```

Jeśli zmienna istnieje, dostaniesz jej wartość.

Jeśli nie istnieje, wynik będzie `None`.

### Możliwy output

```python
sk_test_123456
```

albo:

```python
None
```

## Kiedy `None` jest problemem

Jeśli dana zmienna jest obowiązkowa, ciche `None` może prowadzić do trudnych błędów.

Lepsze podejście:

```python
import os

api_token = os.getenv("API_TOKEN")
if not api_token:
    raise RuntimeError("Brak API_TOKEN w zmiennych srodowiskowych")
```

Teraz aplikacja zatrzyma się od razu i jasno pokaże problem.

## Wartość domyślna

Czasem env var nie jest sekretem i można dać sensowny fallback.

```python
import os

app_env = os.getenv("APP_ENV", "development")
print(app_env)
```

Output, jeśli zmienna nie istnieje:

```python
development
```

To dobre np. dla:

- nazwy środowiska,
- poziomu logowania,
- flagi debug.

To nie jest dobre dla krytycznych sekretów.

## `.env` i `.env.example`

W wielu projektach lokalnie używa się pliku `.env`.

Przykład:

```text
API_TOKEN=twoj_token
DB_PASSWORD=twoje_haslo
APP_ENV=development
```

Ale bardzo ważne:

- prawdziwego `.env` zwykle nie wrzucamy do repo,
- do repo można dodać `.env.example`.

### Przykład `.env.example`

```text
API_TOKEN=
DB_PASSWORD=
APP_ENV=development
```

To pokazuje, jakie zmienne są potrzebne, ale nie ujawnia prawdziwych wartości.

## Co powinno być sekretem

Najczęściej sekretem są dane, które:

- dają dostęp,
- umożliwiają podpisywanie lub uwierzytelnianie,
- pozwalają wykonywać uprzywilejowane operacje,
- otwierają integracje z zewnętrznymi systemami.

Przykłady:

- hasła,
- tokeny,
- klucze prywatne,
- connection stringi z hasłem,
- sekrety do usług płatniczych.

## Co zwykle nie musi być sekretem

Nie każda konfiguracja jest sekretem.

Zwykle nie muszą nim być:

- numer portu,
- nazwa środowiska,
- publiczny host API,
- feature flag bez znaczenia bezpieczeństwa.

To nadal konfiguracja, ale niekoniecznie wrażliwa.

## Typowe błędy początkujących

- sekret wpisany w `.py`,
- wrzucenie `.env` do repo,
- logowanie tokenu do konsoli,
- brak sprawdzenia, czy krytyczna zmienna istnieje,
- używanie tego samego sekretu wszędzie,
- mylenie przykładowej konfiguracji z prawdziwą.

## Nie loguj sekretów

### Zły przykład

```python
print(f"Uruchamiam z tokenem: {api_token}")
```

To wygodne podczas debugowania, ale bardzo ryzykowne.

Logi:

- mogą trafić do plików,
- mogą zostać wysłane do zewnętrznego systemu,
- mogą być czytane przez osoby, które nie powinny znać sekretów.

### Lepszy kierunek

```python
print("Uruchamiam aplikacje, token zostal zaladowany")
```

Jeśli musisz logować stan, loguj fakt istnienia sekretu, nie jego treść.

## Środowiska: dev, staging, production

To normalne, że każde środowisko ma inne wartości:

- inne hasło do bazy,
- inny token,
- inny endpoint API,
- inny poziom logowania.

Właśnie dlatego sekrety i konfiguracja nie powinny być zaszyte w kodzie.

## Co robić, gdy sekret wyciekł

Jeśli sekret trafił do repo lub logów, samo usunięcie go z pliku nie wystarczy.

Trzeba zwykle:

- uznać go za skompromitowany,
- wygenerować nowy,
- unieważnić stary,
- sprawdzić, gdzie mógł zostać skopiowany,
- poprawić proces, który dopuścił do wycieku.

## Checklista pracy z sekretami

- Czy sekret nie jest w kodzie?
- Czy prawdziwy `.env` nie trafia do repo?
- Czy aplikacja jasno zgłasza brak wymaganej zmiennej?
- Czy logi nie pokazują sekretów?
- Czy dev/staging/prod mają oddzielne wartości?

## Szybka ściąga

Dobre praktyki:

- trzymaj sekrety poza kodem,
- używaj env vars lub menedżera sekretów,
- nie loguj prawdziwych wartości,
- dokumentuj wymagane zmienne przez `.env.example`,
- traktuj wyciek sekretu poważnie i rotuj go.

## Ćwiczenia

1. Napisz funkcję odczytującą `DB_PASSWORD` i zgłaszającą błąd, jeśli zmiennej brakuje.
2. Przygotuj przykładowy `.env.example` dla małej aplikacji webowej.
3. Wypisz 5 danych konfiguracyjnych i zaznacz, które są sekretami.
4. Pokaż zły przykład logowania sekretu i popraw go.
5. Opisz, co robisz po wycieku tokenu do repo.

## Najważniejsze do zapamiętania

- Sekrety nie powinny być trzymane w kodzie ani w repo.
- Env vars są prostym i bardzo praktycznym sposobem dostarczania wrażliwej konfiguracji.
- Krytyczne zmienne powinny być jawnie sprawdzane przy starcie aplikacji.
- Logowanie sekretów to również wyciek.
- Jeśli sekret wyciekł, trzeba go rotować, a nie tylko usuwać z pliku.
