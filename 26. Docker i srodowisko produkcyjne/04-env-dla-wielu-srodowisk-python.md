# Env dla wielu srodowisk python

## O czym jest ten rozdział

Bardzo wiele problemów produkcyjnych nie bierze się z samego kodu aplikacji, tylko z różnic konfiguracji między środowiskami.

Na początku projekt często działa tak:

- lokalnie masz `.env`,
- ręcznie ustawiasz kilka zmiennych,
- na serwerze ktoś wpisuje coś inaczej,
- worker ma inne wartości niż web,
- staging zachowuje się inaczej niż prod.

To właśnie miejsce, gdzie trzeba zacząć myśleć świadomie o środowiskach i konfiguracji.

## Najprostsza intuicja

Aplikacja powinna zmieniać zachowanie przez konfigurację środowiska, a nie przez ręczne przerabianie kodu dla każdego wdrożenia.

Najprościej:

- kod jest możliwie ten sam,
- różnią się zmienne środowiskowe i ustawienia uruchomieniowe.

## Typowe środowiska

Najczęściej spotkasz przynajmniej:

- `dev`,
- `test`,
- `staging`,
- `prod`.

Każde z nich może różnić się:

- bazą danych,
- brokerem,
- poziomem logowania,
- debugiem,
- sekretem aplikacji,
- endpointami usług zewnętrznych,
- zasobami sprzętowymi.

## Co zwykle trafia do environment variables

Bardzo często do env trafiają rzeczy takie jak:

- `DATABASE_URL`,
- `REDIS_URL`,
- `BROKER_URL`,
- `SECRET_KEY`,
- `DEBUG`,
- `LOG_LEVEL`,
- `APP_ENV`.

Najważniejsza intuicja:

- env powinien trzymać konfigurację,
- nie sam kod logiki biznesowej.

## Minimalny przykład w Pythonie

```python
import os

app_env = os.getenv("APP_ENV", "dev")
debug = os.getenv("DEBUG", "false").lower() == "true"

a = {
    "app_env": app_env,
    "debug": debug,
}
print(a)
```

Przykładowy output dla środowiska developerskiego:

```text
{'app_env': 'dev', 'debug': False}
```

Najważniejsze:

- ten sam kod może działać różnie zależnie od przekazanych zmiennych.

## `.env`: wygoda, ale nie wszystko

W developmentcie plik `.env` bywa bardzo wygodny.

Pomaga szybko ustawić:

- URL bazy,
- tryb debug,
- lokalne dane logowania do usług testowych.

Ale trzeba pamiętać:

- `.env` w lokalnym dev to nie jest jeszcze pełna strategia zarządzania konfiguracją dla produkcji.

## Before/after

### Słabszy model

- wartości wpisane na sztywno w kodzie,
- ręczne przerabianie ustawień dla każdego środowiska,
- brak jednego modelu konfiguracji.

### Lepszy model

- kod czyta konfigurację z env,
- wartości różnią się między środowiskami bez zmiany kodu,
- zespół wie, które zmienne są obowiązkowe i co oznaczają.

## Sekrety: bardzo ważna ostrożność

Sekrety typu:

- `SECRET_KEY`,
- hasła do bazy,
- tokeny API,
- klucze prywatne,

nie powinny być wpisywane na stałe w repo ani w Dockerfile.

To bardzo ważna zasada.

## Częsty błąd

```python
DATABASE_URL = "postgres://admin:haslo@localhost/app"
```

To zły kierunek, bo:

- trudno zmienić środowisko,
- rośnie ryzyko wycieku,
- konfiguracja miesza się z kodem.

## Lepszy kierunek

```python
DATABASE_URL = os.getenv("DATABASE_URL")
```

A wartość przychodzi z zewnątrz.

## Różnice między dev i prod

W `dev` możesz mieć:

- debug włączony,
- głośniejsze logi,
- lokalny broker,
- lokalną bazę.

W `prod` zwykle chcesz:

- debug wyłączony,
- bezpieczniejsze ustawienia,
- prawdziwe sekrety z bezpiecznego źródła,
- kontrolę nad logowaniem i obserwowalnością.

To nie są drobne różnice. To bardzo ważna część dojrzałości systemu.

## Walidacja konfiguracji

To bardzo dobra praktyka.

Aplikacja powinna umieć jasno powiedzieć na starcie, że brakuje kluczowej konfiguracji.

Przykład intuicyjny:

```python
import os


def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required env var: {name}")
    return value
```

To lepsze niż ciche odpalanie aplikacji z `None` w krytycznym miejscu.

## Spójność między web, worker i scheduler

W projektach z wieloma procesami trzeba pamiętać, że:

- web,
- worker,
- scheduler,

często potrzebują części wspólnej konfiguracji i części własnej.

Jeśli worker ma inną konfigurację brokera albo inny `APP_ENV` niż web, system zaczyna zachowywać się dziwnie.

## Najczęstsze pułapki

### 1. Inne env dla różnych procesów bez świadomości

To prowadzi do trudnych do zrozumienia błędów.

### 2. Trzymanie sekretów w repo

To klasyczny błąd bezpieczeństwa.

### 3. Brak dokumentacji wymaganych zmiennych

Nowa osoba albo pipeline nie wie, co musi ustawić.

### 4. Mieszanie konfiguracji developerskiej z produkcyjną

Potem staging i prod są nieprzewidywalne.

### 5. Brak walidacji na starcie

Aplikacja odpala się, ale psuje się dopiero później, w mniej oczywistym miejscu.

## Mini case study: web działa, worker nie działa

Objaw:

- web uruchamia się poprawnie,
- worker nie może połączyć się z brokerem.

Możliwe przyczyny:

- worker ma inną `BROKER_URL`,
- worker czyta inne `.env`,
- zmienna nie została przekazana do jednego z procesów,
- nazwa hosta działa lokalnie, ale nie działa w sieci kontenerów.

To klasyczny problem środowiskowy, niekoniecznie problem kodu.

## Co Pythonowiec powinien rozumieć

Dobrze, żebyś umiał:

- oddzielać konfigurację od kodu,
- rozumieć rolę env vars w różnych środowiskach,
- nie trzymać sekretów w repo ani obrazie,
- walidować kluczową konfigurację na starcie,
- myśleć o spójności konfiguracji między usługami.

## Output myślowy

### Słaba konfiguracja środowisk

- działa lokalnie przypadkiem,
- zachowanie między dev i prod rozjeżdża się,
- worker i web mogą widzieć świat inaczej.

### Lepsza konfiguracja środowisk

- kod jest bardziej przenośny,
- środowiska różnią się kontrolowanie,
- błędy konfiguracji wychodzą szybciej i czytelniej.

## Najważniejsze do zapamiętania

- Konfiguracja powinna przychodzić z zewnątrz, nie być wpisana w kod.
- Environment variables to podstawowy mechanizm rozdzielania środowisk.
- Sekrety nie powinny trafiać do repo ani obrazu.
- Web, worker i scheduler muszą mieć spójną konfigurację tam, gdzie to potrzebne.
- Walidacja env na starcie oszczędza dużo czasu przy debugowaniu.

## Ćwiczenia

1. Wyjaśnij własnymi słowami, czemu konfiguracja nie powinna być wpisana na stałe w kodzie.
2. Wypisz pięć typowych environment variables w projekcie Pythonowym.
3. Opisz ryzyko trzymania sekretów w repo.
4. Napisz prostą funkcję walidującą wymagane env vars.
5. Rozpisz różnice konfiguracji między `dev` i `prod` dla weba i workera.
