# Dockerfile dobre praktyki python

## O czym jest ten rozdział

Sam fakt, że projekt ma `Dockerfile`, jeszcze niewiele znaczy.

Możesz mieć Dockerfile, który:

- działa lokalnie,
- ale buduje się wolno,
- tworzy ogromny obraz,
- trzyma sekrety,
- uruchamia wszystko jako `root`,
- utrudnia cache,
- miesza development i produkcję.

Dlatego ważne jest nie tylko "mieć Dockerfile", ale mieć Dockerfile sensowny.

## Najprostsza intuicja dobrego Dockerfile

Dobry Dockerfile powinien być możliwie:

- przewidywalny,
- czytelny,
- mały,
- bezpieczny,
- szybki w budowaniu,
- dopasowany do sposobu uruchamiania aplikacji.

## Zły i lepszy przykład

### Słabszy wariant

```dockerfile
FROM python:3.12
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

To może działać, ale ma kilka problemów:

- kopiuje cały projekt zbyt wcześnie,
- gorzej wykorzystuje cache warstw,
- może wrzucać niepotrzebne pliki,
- bazowy obraz może być cięższy niż potrzeba.

### Lepszy wariant

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

To nadal nie jest pełna wersja produkcyjna, ale już jest bardziej sensowna.

## Dlaczego kolejność instrukcji ma znaczenie

Docker buduje obraz warstwami.

To oznacza, że zmiana jednej instrukcji może unieważnić cache dla kolejnych.

Jeśli zrobisz:

```dockerfile
COPY . .
RUN pip install -r requirements.txt
```

To każda zmiana w kodzie może wymuszać ponowną instalację zależności.

Jeśli najpierw kopiujesz plik zależności, a dopiero potem kod, cache działa lepiej.

To bardzo ważna praktyka.

## Cache: intuicja

Jeśli `requirements.txt` się nie zmienił, Docker może użyć wcześniejszej warstwy z zainstalowanymi zależnościami.

Efekt:

- szybszy build,
- mniej niepotrzebnej pracy.

## `--no-cache-dir` przy pip

To częsta drobna dobra praktyka.

```dockerfile
RUN pip install --no-cache-dir -r requirements.txt
```

Najprostsza intuicja:

- nie trzymasz niepotrzebnego cache pip wewnątrz finalnego obrazu,
- obraz jest trochę lżejszy.

## `.dockerignore`: bardzo ważna rzecz

To temat, który łatwo przeoczyć.

Jeśli nie masz `.dockerignore`, możesz przypadkiem wrzucić do kontekstu budowania:

- `.git`,
- `.venv`,
- cache,
- pliki testowe,
- artefakty builda,
- lokalne sekrety,
- duże niepotrzebne katalogi.

To spowalnia build i zwiększa bałagan.

## Przykład `.dockerignore`

```text
.git
.venv
__pycache__
.pytest_cache
.env
node_modules
*.pyc
```

Najważniejsza intuicja:

- do obrazu i do kontekstu budowania powinno trafiać tylko to, co naprawdę potrzebne.

## Uruchamianie jako `root`

To częsty domyślny błąd.

Jeśli kontener działa jako `root`, ryzyko bezpieczeństwa rośnie.

Lepsza praktyka to użycie mniej uprzywilejowanego użytkownika tam, gdzie to sensowne.

Nie zawsze jest to najprostsze na start, ale to bardzo dobra praktyka produkcyjna.

## Sekrety w Dockerfile: zły pomysł

Nigdy nie chcesz robić czegoś w stylu:

```dockerfile
ENV SECRET_KEY=super-secret
```

albo kopiować do obrazu lokalnych plików z sekretami.

Sekrety powinny być dostarczane z zewnątrz, a nie wypiekane w obraz.

## Multi-stage build: intuicja

Czasem chcesz osobno:

- budować artefakty,
- a osobno przygotować lekki obraz runtime.

To jest intuicja multi-stage build.

Przykład:

- w pierwszym etapie instalujesz narzędzia buildowe,
- w drugim trzymasz tylko to, co potrzebne do uruchomienia.

To często daje:

- lżejszy obraz,
- mniejszą powierzchnię ataku,
- czystsze środowisko runtime.

## Before/after

### Słabszy Dockerfile

- kopiuje wszystko za wcześnie,
- nie używa `.dockerignore`,
- działa jako `root`,
- miesza build i runtime,
- trzyma niepotrzebne rzeczy w obrazie.

### Lepszy Dockerfile

- dobrze wykorzystuje cache,
- ma ograniczony kontekst budowania,
- jest lżejszy,
- świadomie zarządza użytkownikiem i środowiskiem,
- jest bardziej przewidywalny.

## Mini case study: projekt z FastAPI i Celery

Masz projekt z:

- webem,
- workerem,
- schedulerm,
- wspólnym kodem aplikacyjnym.

### Słaby model

- ciężki jeden obraz z całym śmietnikiem projektu,
- długi build,
- brak `.dockerignore`,
- zależności instalowane od nowa prawie za każdym razem.

### Lepszy model

- wspólna sensowna baza obrazu,
- uporządkowany cache,
- ograniczony kontekst,
- różne komendy startowe dla różnych ról.

To dużo dojrzalsze podejście.

## Co Pythonowiec powinien rozumieć

Dobrze, żebyś umiał:

- patrzeć na Dockerfile nie tylko jak na listę poleceń, ale jak na projekt artefaktu runtime,
- rozumieć, czemu kolejność instrukcji wpływa na build,
- wiedzieć, po co jest `.dockerignore`,
- nie wrzucać sekretów do obrazu,
- odróżniać prosty demo-Dockerfile od czegoś bardziej sensownego produkcyjnie.

## Output myślowy

### Naiwny Dockerfile

- działa, ale jest ciężki i mało bezpieczny,
- build bywa wolny,
- z czasem staje się kłopotliwy.

### Dojrzalszy Dockerfile

- lepiej wykorzystuje warstwy,
- szybciej się buduje,
- zawiera mniej śmieci,
- lepiej nadaje się do dalszego wdrażania.

## Najważniejsze do zapamiętania

- Dobry Dockerfile to nie tylko działający Dockerfile.
- Kolejność instrukcji wpływa na cache i szybkość budowania.
- `.dockerignore` jest bardzo ważny.
- Nie wkładaj sekretów do obrazu.
- Myśl o obrazie jako o artefakcie runtime, który ma być mały, przewidywalny i sensownie bezpieczny.

## Ćwiczenia

1. Wyjaśnij własnymi słowami, czemu kolejność `COPY` i `RUN pip install` ma znaczenie.
2. Podaj pięć rzeczy, które często warto umieścić w `.dockerignore`.
3. Opisz ryzyko uruchamiania kontenera jako `root`.
4. Wytłumacz, czemu sekrety nie powinny trafiać do Dockerfile.
5. Rozpisz, czym różni się naiwny Dockerfile od bardziej dojrzałego produkcyjnie.
