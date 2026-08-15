# Docker compose python

## O czym jest ten rozdział

Gdy projekt ma więcej niż jeden element, sam pojedynczy `docker run` szybko przestaje wystarczać.

Bardzo szybko pojawia się zestaw typu:

- aplikacja webowa,
- baza danych,
- broker wiadomości,
- worker,
- scheduler.

Uruchamianie tego wszystkiego ręcznie osobnymi komendami staje się męczące i podatne na błędy.

Tu wchodzi `docker compose`.

## Najprostsza intuicja docker compose

`docker compose` pozwala opisać kilka współpracujących usług w jednym miejscu i uruchamiać je jako spójny zestaw.

Najprościej:

- nie myślisz już o jednym kontenerze,
- myślisz o lokalnym środowisku złożonym z wielu usług.

## Co zwykle opisuje compose

Plik compose zwykle zawiera:

- listę usług,
- obrazy albo sposób budowania,
- porty,
- volumes,
- environment variables,
- zależności między usługami,
- czasem sieci i profile.

## Przykład intuicyjny

Masz projekt z:

- `web`,
- `db`,
- `redis`,
- `worker`.

Zamiast uruchamiać wszystko osobno, możesz mieć jeden plik opisujący cały układ.

## Minimalny przykład

```yaml
services:
  web:
    build: .
    command: python app.py
    ports:
      - "8000:8000"

  db:
    image: postgres:16
    environment:
      POSTGRES_DB: app
      POSTGRES_USER: app
      POSTGRES_PASSWORD: secret

  redis:
    image: redis:7

  worker:
    build: .
    command: celery -A app worker -l info
```

To nie jest pełna konfiguracja produkcyjna, ale dobrze pokazuje model myślenia.

## Co daje compose w praktyce

Compose pomaga, gdy chcesz:

- szybko podnieść całe środowisko lokalne,
- utrzymać spójną konfigurację usług,
- dać zespołowi łatwy start projektu,
- testować interakcje między komponentami,
- ograniczyć chaos ręcznego odpalania wielu procesów.

## `build` a `image`

To bardzo podstawowe, ale ważne rozróżnienie.

### `build`

Mówi, że obraz ma zostać zbudowany z lokalnego Dockerfile.

### `image`

Mówi, że używasz gotowego obrazu.

Przykład:

- `web` i `worker` często budują się z lokalnego kodu,
- `postgres` albo `redis` często lecą z gotowego obrazu.

## Compose nie jest tym samym co produkcyjna orkiestracja

To ważna intuicja.

Compose jest świetne do:

- developmentu,
- lokalnych testów integracyjnych,
- prostszych środowisk.

Ale nie należy automatycznie zakładać, że lokalny plik compose jest pełnym odpowiednikiem dojrzałego środowiska produkcyjnego.

To bardziej narzędzie do wygodnego spięcia usług niż pełna strategia platformowa.

## Ports, volumes, env: trzy bardzo ważne rzeczy

### Ports

Pozwalają wystawić usługę na zewnątrz hosta.

Przykład:

```yaml
ports:
  - "8000:8000"
```

### Volumes

Pomagają przechowywać dane albo montować kod.

Przykład:

- baza może trzymać dane w volume,
- lokalny kod może być podmontowany do dev-containera.

### Environment

Pozwala przekazać konfigurację bez twardego wpisywania jej w kod.

## Before/after

### Bez compose

- kilka ręcznych komend,
- łatwo pominąć jedną usługę,
- trudniej onboardować nową osobę,
- lokalne środowisko bywa chaotyczne.

### Z compose

- jeden opis usług,
- prostszy start,
- bardziej przewidywalny lokalny układ,
- łatwiej myśleć o systemie jako zestawie współpracujących komponentów.

## Mini case study: FastAPI + Postgres + Redis + Celery

Masz aplikację webową, worker Celery, Redis jako broker/cache i Postgresa jako bazę.

### Słabszy model

Każda osoba w zespole odpala to po swojemu.

Efekt:

- różnice środowisk,
- trudniejszy onboarding,
- trudniej odtwarzać błędy.

### Lepszy model

Compose definiuje cały lokalny układ.

Efekt:

- łatwiej zacząć,
- łatwiej odtworzyć flow,
- łatwiej testować integrację między usługami.

## Częste pułapki

### 1. Trzymanie w compose sekretów produkcyjnych

To zły kierunek.

### 2. Zakładanie, że `depends_on` rozwiązuje pełną gotowość usług

To częsty błąd intuicyjny.

To, że kontener się uruchomił, nie znaczy jeszcze, że usługa jest gotowa do pracy.

### 3. Jeden gigantyczny plik do wszystkiego

Czasem lepiej świadomie rozdzielać konfigurację albo profile niż wrzucać każdy możliwy wariant do jednego bałaganu.

### 4. Mieszanie potrzeb dev i prod bez jasnych zasad

To bardzo szybko tworzy chaos konfiguracyjny.

## `depends_on`: ważna ostrożność

`depends_on` pomaga w kolejności startu kontenerów, ale nie daje gwarancji, że aplikacja docelowa jest już gotowa przyjmować połączenia.

To ważna praktyczna pułapka.

## Co Pythonowiec powinien rozumieć

Dobrze, żebyś umiał:

- myśleć o aplikacji jako o zestawie usług, a nie tylko jednym procesie,
- rozumieć rolę compose w local dev i integracjach,
- odróżniać `build` i `image`,
- wiedzieć, do czego służą ports, volumes i env,
- nie mylić wygodnego lokalnego składu usług z pełnym production orchestration.

## Output myślowy

### Bez compose

- więcej ręcznej pracy,
- mniej powtarzalności,
- większy chaos przy kilku usługach.

### Z compose

- łatwiej wystartować cały system,
- łatwiej onboardować ludzi,
- łatwiej myśleć o integracji komponentów,
- ale nadal trzeba uważać na różnice między dev i prod.

## Najważniejsze do zapamiętania

- `docker compose` opisuje zestaw współpracujących usług.
- Bardzo dobrze sprawdza się w local dev i środowiskach integracyjnych.
- Nie jest automatycznie pełnym odpowiednikiem dojrzałej orkiestracji produkcyjnej.
- `build`, `image`, `ports`, `volumes` i `environment` to podstawowe elementy praktyczne.
- `depends_on` nie oznacza jeszcze pełnej gotowości usługi.

## Ćwiczenia

1. Wyjaśnij własnymi słowami, po co używa się `docker compose`.
2. Opisz różnicę między `build` i `image`.
3. Rozpisz prosty skład usług dla aplikacji web + db + worker.
4. Wyjaśnij, czemu `depends_on` nie rozwiązuje całego problemu startu usług.
5. Podaj trzy korzyści z używania compose w lokalnym środowisku zespołowym.
