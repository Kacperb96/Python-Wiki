# Case study: FastAPI + Postgres + Redis + Celery w kontenerach

## Po co ten plik

Ten plik spina cały folder 26 w jedną praktyczną całość.

Nie chodzi już o osobne pojęcia typu:

- Dockerfile,
- compose,
- env,
- obrazy,
- web i worker,

ale o odpowiedź na pytanie:

- jak to wszystko wygląda razem w jednym sensownym projekcie?

## Mini system

Załóżmy projekt złożony z:

- `web` na FastAPI,
- `db` na Postgresie,
- `redis` jako broker/cache,
- `worker` Celery,
- `scheduler` do zadań okresowych.

To bardzo typowy praktyczny układ w Pythonie.

## Cele architektoniczne

Chcemy osiągnąć:

- przewidywalny local dev,
- spójny artefakt uruchomieniowy,
- rozdzielone role procesów,
- łatwiejszy onboarding,
- sensowny start do środowiska produkcyjnego.

## Podział usług

### `web`

- wystawia API,
- przyjmuje requesty,
- zapisuje dane,
- publikuje zadania do workera.

### `db`

- trzyma stan aplikacji.

### `redis`

- pośredniczy dla Celery albo pełni rolę cache.

### `worker`

- wykonuje zadania asynchroniczne,
- wysyła maile,
- generuje raporty,
- robi integracje poboczne.

### `scheduler`

- uruchamia zadania okresowe.

## Jeden obraz, kilka ról

Najczęstszy dojrzały model jest taki:

- masz jeden sensowny obraz aplikacji,
- uruchamiasz z niego kilka ról przez różne komendy.

Przykład:

- `web`: `uvicorn app.main:app --host 0.0.0.0 --port 8000`
- `worker`: `celery -A app.celery_app worker -l info`
- `scheduler`: `celery -A app.celery_app beat -l info`

To bardzo praktyczne, bo:

- utrzymujesz jedną bazę zależności,
- łatwiej pilnujesz zgodności wersji,
- różne role nadal są rozdzielone.

## Przykładowy szkic compose

```yaml
services:
  web:
    build: .
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000
    ports:
      - "8000:8000"
    environment:
      APP_ENV: dev
      DATABASE_URL: postgresql://app:secret@db:5432/app
      REDIS_URL: redis://redis:6379/0
    depends_on:
      - db
      - redis

  worker:
    build: .
    command: celery -A app.celery_app worker -l info
    environment:
      APP_ENV: dev
      DATABASE_URL: postgresql://app:secret@db:5432/app
      REDIS_URL: redis://redis:6379/0
    depends_on:
      - db
      - redis

  scheduler:
    build: .
    command: celery -A app.celery_app beat -l info
    environment:
      APP_ENV: dev
      DATABASE_URL: postgresql://app:secret@db:5432/app
      REDIS_URL: redis://redis:6379/0
    depends_on:
      - db
      - redis

  db:
    image: postgres:16
    environment:
      POSTGRES_DB: app
      POSTGRES_USER: app
      POSTGRES_PASSWORD: secret

  redis:
    image: redis:7
```

To nie jest pełna konfiguracja produkcyjna, ale bardzo dobrze pokazuje układ myślenia.

## Co tu jest najważniejsze

### Spójność env

Web, worker i scheduler muszą rozumieć ten sam świat tam, gdzie to potrzebne.

Jeśli web używa jednej bazy, a worker innej, system może zachowywać się absurdalnie.

### Rozdzielenie ról

Każda rola ma osobną komendę i własne logi.

### Przewidywalność lokalnego startu

Nowa osoba w zespole może postawić cały system jednym poleceniem zamiast 20 ręcznych kroków.

## Przykład flow biznesowego

Załóżmy endpoint:

```text
POST /orders
```

Flow:

1. `web` zapisuje zamówienie do `db`,
2. publikuje task do `worker`,
3. zwraca odpowiedź użytkownikowi,
4. `worker` wysyła mail i aktualizuje CRM,
5. `scheduler` w nocy uruchamia raport dzienny.

To pokazuje, jak kontenery odzwierciedlają role architektury aplikacji.

## Local dev vs bardziej produkcyjne myślenie

### Local dev

- możesz montować kod,
- możesz mieć hot reload,
- możesz mieć prostsze logi,
- wygoda iteracji jest ważna.

### Produkcyjne myślenie

- obraz ma być gotowym artefaktem,
- role mają być przewidywalne,
- debug nie powinien być domyślnie włączony,
- konfiguracja ma być bardziej kontrolowana.

To ten sam system, ale inne priorytety.

## Gdzie najłatwiej popełnić błędy

### Błąd 1

Jeden kontener robi wszystko naraz.

Skutek:

- trudniejsza obserwowalność,
- trudniejsze skalowanie,
- większy chaos restartów.

### Błąd 2

Różne env dla weba i workera bez świadomości.

Skutek:

- lokalnie web działa, worker nie,
- albo zadania trafiają nie tam, gdzie trzeba.

### Błąd 3

Za ciężki obraz wspólny dla wszystkich ról.

Skutek:

- wolniejsze buildy,
- wolniejsze wdrożenia,
- większa powierzchnia ataku.

### Błąd 4

Myślenie, że `depends_on` rozwiązuje gotowość usług.

Skutek:

- kontener startuje, ale usługa jeszcze nie jest gotowa,
- aplikacja sypie się przy starcie.

## Healthcheck: po co jest ważny

W takim systemie przydaje się myślenie:

- czy web naprawdę wystartował,
- czy baza naprawdę przyjmuje połączenia,
- czy worker żyje,
- czy scheduler nie padł po cichu.

Healthcheck nie rozwiązuje wszystkiego, ale daje lepszą widoczność stanu usług.

## Before/after

### Słabszy układ

- ręczny start usług,
- różna konfiguracja na różnych maszynach,
- jedna nieczytelna rola kontenera,
- trudny onboarding.

### Dojrzalszy układ

- jasno opisane usługi,
- wspólny sensowny obraz,
- osobne role uruchomieniowe,
- łatwiejsze odtworzenie środowiska,
- lepsza baza pod dalsze wdrożenie.

## Jak dobrać poziomy testów do takiego środowiska

### Unit

Testuj:

- walidację env,
- logikę budowania konfiguracji,
- rozdzielenie ról uruchomieniowych w kodzie.

### Integration

Testuj:

- web + db,
- worker + broker,
- scheduler + publikowane zadania,
- podstawowy start lokalnego układu usług.

### E2E

Testuj:

- użytkownik tworzy zamówienie,
- worker wykonuje zadanie,
- dane trafiają do bazy,
- cały flow przechodzi przez kontenery tak, jak w realnym uruchomieniu.

## Co ten case study pokazuje

Najważniejsza lekcja:

- Docker i compose nie są osobnym światem obok aplikacji,
- one są częścią sposobu, w jaki architektura naprawdę działa w praktyce.

To dlatego rozdział ról, env, obrazu i sposobu startu trzeba projektować razem.

## Najważniejsze do zapamiętania

- Jeden projekt może mieć kilka ról uruchomieniowych opartych o wspólny obraz.
- Web, worker i scheduler powinny być rozdzielone logicznie i operacyjnie.
- Compose świetnie spina lokalny układ wielu usług.
- Spójność env i sposób startu są krytyczne.
- Case study pokazuje, że środowisko uruchomieniowe jest częścią architektury systemu.

## Ćwiczenia

1. Rozpisz własną wersję układu `web + db + broker + worker + scheduler`.
2. Wskaż, które env vars muszą być wspólne dla wszystkich ról.
3. Opisz, które role skalowałbyś niezależnie i dlaczego.
4. Wymyśl dwa miejsca, gdzie healthcheck byłby szczególnie ważny.
5. Opisz, jak uprościłbyś onboarding nowej osoby w takim projekcie.
