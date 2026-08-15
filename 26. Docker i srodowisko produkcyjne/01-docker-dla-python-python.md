# Docker dla python python

## O czym jest ten rozdział

Docker bardzo często pojawia się w projektach Pythonowych w momencie, gdy zespół chce przestać polegać na szczęściu i lokalnych różnicach środowiska.

Na początku wiele problemów wygląda tak:

- u jednej osoby projekt działa,
- u drugiej brakuje biblioteki systemowej,
- na serwerze jest inna wersja Pythona,
- worker działa inaczej niż web,
- lokalne środowisko trudno powtórzyć.

Docker nie usuwa całej złożoności świata, ale bardzo pomaga ustandaryzować sposób uruchamiania aplikacji.

## Najprostsza intuicja Dockera

Docker pozwala zapakować aplikację razem z jej środowiskiem uruchomieniowym do obrazu, z którego później uruchamia się kontener.

Najprościej:

- obraz to przepis,
- kontener to uruchomiona instancja tego przepisu.

To bardzo ważna intuicja.

## Obraz a kontener

To dwa pojęcia, które trzeba odróżniać od razu.

### Obraz

Obraz to zbudowany artefakt zawierający:

- bazowy system,
- Pythona,
- zależności,
- pliki aplikacji,
- polecenie startowe.

### Kontener

Kontener to uruchomiony proces lub zestaw procesów oparty o ten obraz.

Najprościej:

- obraz jest czymś statycznym,
- kontener jest czymś działającym.

## Co Docker rozwiązuje w praktyce

Docker pomaga, gdy chcesz:

- mieć bardziej powtarzalne środowisko,
- łatwiej uruchamiać projekt na różnych maszynach,
- spakować aplikację z zależnościami,
- przewidywalnie odpalić web, worker albo scheduler,
- uprościć lokalny setup zespołu,
- przygotować artefakt do pipeline'u i wdrożenia.

## Co Docker nie rozwiązuje automatycznie

To bardzo ważne.

Docker nie naprawia sam z siebie:

- złej architektury,
- złego zarządzania konfiguracją,
- problemów bezpieczeństwa,
- ciężkich obrazów,
- złego podziału procesów,
- słabej obserwowalności.

Czyli Docker jest narzędziem, a nie magicznym lekarstwem.

## Minimalny przykład myślowy

Masz prostą aplikację Flask albo FastAPI.

Bez Dockera uruchomienie może zależeć od:

- lokalnej wersji Pythona,
- lokalnych bibliotek systemowych,
- lokalnych zmiennych środowiskowych,
- ręcznej konfiguracji.

Z Dockerem chcesz mieć model:

- buduję obraz,
- uruchamiam kontener,
- aplikacja startuje podobnie niezależnie od maszyny.

## Najprostszy przykład Dockerfile

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

To nie jest jeszcze najlepsza wersja produkcyjna, ale dobrze buduje intuicję.

## Co ten plik robi

### `FROM python:3.12-slim`

Bierze bazowy obraz z Pythonem.

### `WORKDIR /app`

Ustawia katalog roboczy wewnątrz obrazu.

### `COPY requirements.txt .`

Kopiuje plik zależności.

### `RUN pip install -r requirements.txt`

Instaluje zależności.

### `COPY . .`

Kopiuje kod aplikacji.

### `CMD [...]`

Mówi, jak uruchomić aplikację w kontenerze.

## Output myślowy

### Budowanie obrazu

```text
Docker reads Dockerfile
installs Python deps
copies app code
produces final image
```

### Uruchomienie kontenera

```text
container starts
app command runs
service begins listening
```

To właśnie jest podstawowy cykl pracy z Dockerem.

## Kiedy Docker ma sens szczególnie mocno

Docker bardzo często ma sens, gdy:

- projekt ma kilka usług,
- zespół pracuje na różnych systemach,
- aplikacja ma zależności systemowe,
- chcesz przewidywalnego wdrożenia,
- pracujesz z webem, bazą, brokerem i workerami.

## Kiedy Docker bywa przerostem formy

Przy bardzo małym, prostym skrypcie edukacyjnym może być po prostu dodatkową warstwą złożoności.

Ale w momencie, gdy projekt robi się bardziej realny, korzyść zwykle rośnie szybko.

## Najczęstsze pułapki

### 1. Mylenie obrazu z kontenerem

To jedna z najczęstszych podstawowych pomyłek.

### 2. Wrzucanie wszystkiego do obrazu bez refleksji

Potem obraz:

- jest ciężki,
- buduje się wolno,
- zawiera niepotrzebne pliki,
- ma większą powierzchnię ataku.

### 3. Trzymanie sekretów w obrazie

To zły pomysł.

Sekrety powinny być przekazywane inaczej, a nie "wypiekane" do obrazu.

### 4. Zakładanie, że lokalny kontener = gotowa produkcja

Między sensownym local dev a dobrą konfiguracją produkcyjną jest jeszcze sporo decyzji.

## Before/after

### Bez Dockera

- aplikacja zależy mocno od lokalnej maszyny,
- trudniej powtórzyć środowisko,
- onboarding nowej osoby bywa cięższy.

### Z Dockerem

- środowisko jest bardziej przewidywalne,
- łatwiej odtworzyć zależności,
- łatwiej spiąć kilka usług razem,
- ale rośnie odpowiedzialność za jakość obrazu i konfiguracji.

## Mini case study: web + worker

Masz aplikację webową i workera Celery.

Bez Dockera możesz mieć problem:

- inna wersja zależności w webie,
- inna konfiguracja w workerze,
- trudny lokalny start całego systemu.

Z Dockerem możesz zbudować wspólną bazę obrazu i przewidywalnie uruchamiać:

- kontener web,
- kontener worker.

To bardzo częsty praktyczny zysk.

## Co Pythonowiec powinien rozumieć

Dobrze, żebyś umiał:

- odróżnić obraz od kontenera,
- rozumieć, po co pakujesz zależności do obrazu,
- nie traktować Dockera jako celu samego w sobie,
- widzieć, kiedy pomaga w powtarzalności środowiska,
- wiedzieć, że dobra jakość konteneryzacji wymaga decyzji projektowych.

## Output myślowy

### Bez konteneryzacji

- działa lokalnie, ale bywa trudno przenieść środowisko,
- różnice między maszynami wychodzą szybko.

### Z konteneryzacją

- uruchomienie jest bardziej przewidywalne,
- zależności są bardziej zamknięte,
- ale trzeba dobrze zaprojektować obraz i sposób startu.

## Najważniejsze do zapamiętania

- Obraz to przepis, kontener to uruchomiona instancja.
- Docker pomaga w powtarzalności środowiska i wdrażaniu.
- Nie rozwiązuje automatycznie wszystkich problemów projektu.
- Jakość Dockera zależy od jakości Dockerfile i organizacji środowiska.
- To bardzo praktyczne narzędzie, szczególnie dla większych projektów Pythonowych.

## Ćwiczenia

1. Wyjaśnij własnymi słowami różnicę między obrazem i kontenerem.
2. Podaj trzy problemy projektowe, które Docker pomaga ograniczyć.
3. Wytłumacz, czemu Docker nie jest magicznym rozwiązaniem wszystkich problemów środowiskowych.
4. Rozpisz, co robi każda linijka prostego Dockerfile.
5. Opisz, czemu web i worker korzystające z podobnego obrazu to praktyczna zaleta.
