# Web worker scheduler python

## O czym jest ten rozdział

W bardziej realnym projekcie Pythonowym bardzo szybko okazuje się, że aplikacja to nie jeden proces.

Często masz przynajmniej:

- web,
- worker,
- scheduler.

I bardzo ważne jest zrozumienie, że to nie są tylko różne komendy startowe, ale różne role w systemie.

## Najprostsza intuicja

### Web

Obsługuje requesty użytkowników albo API.

### Worker

Wykonuje pracę w tle.

### Scheduler

Uruchamia zadania okresowe albo planowane.

Najprościej:

- web odpowiada na ruch,
- worker robi asynchroniczne zadania,
- scheduler pilnuje zadań czasowych.

## Dlaczego warto je rozdzielać

Jeśli wszystko uruchomisz jako jeden proces albo jeden nieczytelny zestaw komend, zaczynają się problemy:

- trudniej skalować role niezależnie,
- trudniej diagnozować awarie,
- ciężej zarządzać zasobami,
- jeden typ pracy może szkodzić drugiemu.

Rozdzielenie ról daje dużo większą kontrolę.

## Web: co robi

Web zwykle:

- słucha na porcie,
- przyjmuje requesty,
- rozmawia z bazą,
- zwraca odpowiedzi,
- czasem publikuje zadania do workera.

Najważniejsza intuicja:

- web powinien być zoptymalizowany pod responsywność i przewidywalność request-response.

## Worker: co robi

Worker zwykle:

- nie wystawia portu użytkownikowi,
- odbiera zadania z kolejki,
- robi cięższą albo opóźnioną pracę,
- może wykonywać retry,
- może działać niezależnie od tempa ruchu na webie.

Najważniejsze:

- worker nie powinien być mylony z webem tylko dlatego, że korzysta z tego samego kodu aplikacji.

## Scheduler: co robi

Scheduler uruchamia zadania okresowe.

Przykłady:

- nocny raport,
- synchronizacja stanów,
- czyszczenie starych danych,
- przypomnienia mailowe,
- publikacja cyklicznych jobów.

To również osobna rola systemowa.

## Jeden obraz, różne komendy

Bardzo częsty model wygląda tak:

- masz jeden wspólny obraz aplikacji,
- uruchamiasz z niego różne kontenery z różnymi komendami.

Przykład myślowy:

- `web` startuje `gunicorn` albo `uvicorn`,
- `worker` startuje `celery worker`,
- `scheduler` startuje `celery beat` albo inny mechanizm planowania.

To bardzo praktyczny wzorzec.

## Dlaczego to ma sens

Masz wspólny kod i zależności, ale osobne role uruchomieniowe.

Korzyści:

- mniejszy chaos,
- łatwiejsza spójność wersji,
- niezależne skalowanie,
- łatwiejsza obserwowalność.

## Before/after

### Słabszy model

- jeden kontener próbuje robić wszystko,
- kilka procesów odpalanych "jakoś" w środku,
- trudniej restartować i diagnozować rolę osobno,
- zasoby mieszają się bez kontroli.

### Lepszy model

- osobny kontener web,
- osobny worker,
- osobny scheduler,
- wspólny obraz lub wspólna baza obrazu,
- jasne role i osobne logi.

## Mini przykład compose-owy

```yaml
services:
  web:
    build: .
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000

  worker:
    build: .
    command: celery -A app.celery_app worker -l info

  scheduler:
    build: .
    command: celery -A app.celery_app beat -l info
```

Najważniejsza intuicja:

- ten sam kod,
- trzy różne role operacyjne.

## Skalowanie ról

To ogromna zaleta rozdzielenia.

Możesz potrzebować:

- więcej instancji weba przy dużym ruchu API,
- więcej workerów przy dużym backlogu zadań,
- tylko jednego schedulera.

Gdy role są rozdzielone, da się je skalować niezależnie.

## Zasoby i profile pracy

Web, worker i scheduler często mają różne profile użycia zasobów.

### Web

- liczy się responsywność,
- czasem więcej połączeń,
- inne wzorce CPU i pamięci.

### Worker

- może wykonywać cięższe zadania,
- bywa bardziej CPU-bound lub IO-bound zależnie od zadań.

### Scheduler

- zwykle ma mniejsze obciążenie ciągłe,
- ale jest krytyczny dla uruchamiania zadań czasowych.

To kolejny argument za rozdziałem.

## Częste pułapki

### 1. Wrzucenie wszystkiego do jednego kontenera

Na początku bywa kuszące, ale zwykle szybko zaczyna boleć.

### 2. Inna konfiguracja weba i workera bez świadomości

Jeśli używają innych URL-i, innych env albo innych wersji kodu, system może zachowywać się dziwnie.

### 3. Brak obserwowalności osobno dla ról

Jeśli logi i metryki mieszają się w jeden szum, trudno diagnozować problemy.

### 4. Dublowanie schedulera

Niektóre role powinny być pojedyncze albo uruchamiane bardzo świadomie.

To ważne szczególnie przy zadaniach okresowych.

## Mini case study: mail i raporty

Masz system zamówień.

### Web

- przyjmuje nowe zamówienie,
- zwraca odpowiedź.

### Worker

- wysyła maile,
- generuje PDF,
- synchronizuje CRM.

### Scheduler

- uruchamia nocne raporty i czyszczenie starych danych.

To bardzo naturalny i dojrzały podział.

## Co Pythonowiec powinien rozumieć

Dobrze, żebyś umiał:

- odróżnić rolę weba, workera i schedulera,
- rozumieć, czemu ich rozdzielenie ułatwia skalowanie i utrzymanie,
- myśleć o obrazie jako wspólnej bazie dla różnych ról,
- pilnować spójności konfiguracji między procesami,
- nie robić z jednego kontenera worka na wszystko.

## Output myślowy

### Wszystko w jednym

- mniej plików na start,
- ale szybko robi się nieczytelnie i mało operacyjnie.

### Role rozdzielone

- łatwiejsze skalowanie,
- prostsze logowanie i restartowanie,
- większa przewidywalność systemu.

## Najważniejsze do zapamiętania

- Web, worker i scheduler to różne role systemowe.
- Często warto uruchamiać je jako osobne kontenery.
- Ten sam obraz może obsługiwać różne role przez różne komendy startowe.
- Rozdzielenie ról daje lepszą skalowalność i utrzymanie.
- Trzeba pilnować spójności konfiguracji i unikać mieszania wszystkiego w jednym procesie.

## Ćwiczenia

1. Wyjaśnij własnymi słowami rolę weba, workera i schedulera.
2. Opisz, czemu jeden kontener do wszystkiego szybko staje się problematyczny.
3. Rozpisz przykładowe komendy startowe dla trzech ról w projekcie FastAPI + Celery.
4. Podaj dwa powody, dla których web i worker skalują się inaczej.
5. Wymyśl przykład zadania, które powinno należeć do schedulera, a nie do weba.
