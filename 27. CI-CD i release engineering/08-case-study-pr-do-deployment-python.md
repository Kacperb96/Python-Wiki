# Case study: od PR do deploymentu w projekcie Pythonowym

## Po co ten plik

Ten plik spina cały folder 27 w jedną praktyczną całość.

Nie chodzi już o osobne pojęcia typu:

- pipeline,
- quality gates,
- release,
- changelog,
- deployment,

ale o odpowiedź na pytanie:

- jak to wszystko działa razem w jednym realnym procesie zespołowym?

## Mini projekt

Załóżmy backend FastAPI wdrażany jako obraz Dockera.

Projekt ma:

- testy,
- mypy,
- lint,
- obraz Dockera,
- staging,
- produkcję,
- worker do zadań backgroundowych.

Zespół chce wdrażać kilka razy w tygodniu bez chaosu.

## Cel procesu

Chcemy osiągnąć:

- przewidywalność,
- śledzalność zmian,
- niski koszt regresji,
- czytelny związek między kodem, wersją i wdrożeniem,
- możliwość szybkiego rollbacku lub hotfixu.

## Krok 1: powstaje pull request

Programista tworzy PR z nową zmianą.

Na tym etapie ważne są:

- review kodu,
- opis zmiany,
- gotowość testów,
- zgodność ze standardami projektu.

## Krok 2: uruchamia się pipeline PR

Pipeline odpala:

1. lint,
2. testy,
3. typecheck,
4. build artefaktu albo przynajmniej walidację budowania.

### Co ma dać ten etap

Ma odpowiedzieć:

- czy ta zmiana jest technicznie wystarczająco zdrowa, żeby w ogóle myśleć o merge?

## Krok 3: działają quality gates dla merge

Przykładowe gate'y:

- testy muszą być zielone,
- typecheck musi być zielony,
- build musi się udać,
- wymagane review musi być zakończone.

Dopiero wtedy PR może wejść do `main`.

To bardzo ważne, bo pipeline PR i gate merge'owy budują minimalne zaufanie do zmian.

## Krok 4: merge do `main`

Po merge projekt ma nadal pozostać w stanie releasowalnym.

To zdrowa praktyka.

Jeśli `main` po merge regularnie jest niestabilny, proces releasowy szybko traci sens.

## Krok 5: przygotowanie releasu

Zespół decyduje, że zmiany z `main` są gotowe do wydania.

Na tym etapie zwykle dzieje się:

- wybór wersji, np. `v1.8.0`,
- aktualizacja changelogu,
- potwierdzenie zakresu zmian.

## Krok 6: tagowanie wersji

Commit releasu dostaje tag, np.:

```text
v1.8.0
```

To bardzo ważny moment, bo od tej chwili:

- wersja ma jednoznaczną etykietę,
- pipeline może publikować artefakty dokładnie dla tego punktu historii,
- łatwo odtworzyć, z czego powstał release.

## Krok 7: publikacja artefaktów

Pipeline tagowy robi np.:

- build obrazu Dockera,
- tag obrazu wersją `v1.8.0`,
- push do registry,
- publikację release notes.

Najważniejsze:

- publikacja jest związana z tagiem,
- nie jest przypadkowym skutkiem losowego commita.

## Krok 8: deployment na staging

Ten sam artefakt trafia na staging.

Tu sprawdzasz:

- czy aplikacja wstaje,
- czy integracje działają,
- czy migracje są poprawne,
- czy najważniejsze flow nie są zepsute.

To jest ostatni moment, gdzie można wyłapać problemy przed produkcją przy mniejszym ryzyku.

## Krok 9: deployment na produkcję

Jeśli staging jest zdrowy, ten sam artefakt trafia na produkcję.

To bardzo ważne:

- staging i prod powinny dostać ten sam build,
- różnić się może konfiguracja środowiska, nie sam kod artefaktu.

## Krok 10: obserwacja po wdrożeniu

Po deploymentcie nie kończy się odpowiedzialność.

Trzeba obserwować:

- błędy aplikacji,
- zdrowie workerów,
- opóźnienia zadań,
- wzrost 5xx,
- regresje funkcjonalne,
- metryki biznesowe.

To bardzo ważna część dojrzałego procesu releasowego.

## Gdzie w tym procesie najłatwiej o błąd

### Błąd 1: zielony PR, ale brak sensownego builda release

Zmienna w środowisku release jest inna, obraz nie działa, a pipeline PR tego nie wykrywa.

### Błąd 2: merge i release są mylone

Zespół nie wie, czy każdy merge ma automatycznie oznaczać publiczny release.

### Błąd 3: staging nie dostaje tego samego artefaktu co prod

To osłabia cały sens walidacji stagingowej.

### Błąd 4: tag nie wskazuje dokładnie tego, co opublikowano

Wtedy śledzalność procesu spada.

## Mini case study: hotfix

Produkcja ma błąd krytyczny.

Dojrzały flow hotfixu może wyglądać tak:

1. przygotowujesz minimalną poprawkę,
2. odpalasz skrócony, ale nadal sensowny pipeline,
3. tagujesz wersję hotfixową, np. `v1.8.1`,
4. publikujesz artefakt,
5. wdrażasz go świadomie,
6. scalasz poprawkę z głównym nurtem zmian.

Najważniejsze:

- hotfix to nie powinien być całkowity chaos poza procesem,
- tylko kontrolowana ścieżka awaryjna.

## Mini case study: rollback

Nowa wersja `v1.8.0` po wdrożeniu robi problem.

Dojrzały proces powinien umożliwić:

- szybkie wskazanie poprzedniego dobrego artefaktu,
- wiedzę, jaki tag odpowiada poprzedniej stabilnej wersji,
- powrót do znanej wersji, jeśli to bezpieczne.

To pokazuje, po co cały ten porządek z wersjami i artefaktami istnieje.

## Jak dobrać poziomy testów w tym procesie

### Przed merge

- lint,
- unit tests,
- typecheck,
- część testów integracyjnych.

### Przed release

- pełniejsza walidacja buildu,
- ewentualnie dodatkowe integracje,
- sprawdzenie changelogu i wersji.

### Przed produkcją

- staging,
- smoke tests,
- obserwacja zdrowia wdrożenia.

To pokazuje, że różne etapy procesu mają różne zadania jakościowe.

## Co ten case study pokazuje

Najważniejsza lekcja:

- CI/CD to nie jest pojedynczy pipeline,
- to cała ścieżka od zmiany kodu do obserwowanego deploymentu.

I właśnie dlatego pipeline, quality gates, tagi, build, release i deployment trzeba rozumieć jako jedną całość.

## Najważniejsze do zapamiętania

- PR, merge, release i deployment to różne etapy jednego procesu.
- Tag powinien jednoznacznie wskazywać wersję releasu.
- Staging i prod powinny dostać ten sam artefakt.
- Hotfix i rollback muszą mieć swoje miejsce w procesie.
- Dojrzały proces nie kończy się na publikacji artefaktu, tylko obejmuje też obserwację po wdrożeniu.

## Ćwiczenia

1. Rozpisz własną wersję flow od PR do produkcji dla projektu Pythonowego.
2. Wskaż, które etapy procesu powinny być automatyczne, a które mogą wymagać decyzji człowieka.
3. Opisz, gdzie w tym flow dodasz quality gates.
4. Rozpisz osobną ścieżkę hotfixu.
5. Opisz, jak zapewnisz, że staging i prod dostają ten sam artefakt.
