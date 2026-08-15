# 26. Docker i srodowisko produkcyjne

Ten folder jest o tym, jak przenieść aplikację Pythonową z poziomu "działa u mnie" na poziom bardziej przewidywalnego środowiska uruchomieniowego.

Na początku wiele projektów działa tak:

- lokalnie instalujesz zależności,
- uruchamiasz aplikację ręcznie,
- na innym komputerze coś już się różni,
- na serwerze brakuje biblioteki albo wersja środowiska jest inna.

To właśnie miejsce, w którym Docker i świadome przygotowanie środowiska zaczynają robić ogromną różnicę.

## Cel folderu

Po przerobieniu tego działu powinieneś:

- rozumieć, po co używa się Dockera w projektach Pythonowych,
- wiedzieć, jak wygląda sensowny `Dockerfile`,
- rozumieć, kiedy i po co używać `docker compose`,
- umieć zarządzać zmiennymi środowiskowymi dla różnych środowisk,
- wiedzieć, jak budować obrazy lżejsze i bezpieczniejsze,
- rozumieć rozdzielenie procesów typu web, worker, scheduler,
- wiedzieć, czym różni się środowisko developerskie od produkcyjnego,
- umieć myśleć o kontenerach jako o części architektury uruchomieniowej, a nie tylko modnym dodatku,
- rozumieć, jak cały projekt kontenerowy spina się w jeden działający układ usług.

## Jak czytać ten dział

Najlepiej iść po kolei:

1. `01-docker-dla-python-python.md`
2. `02-dockerfile-dobre-praktyki-python.md`
3. `03-docker-compose-python.md`
4. `04-env-dla-wielu-srodowisk-python.md`
5. `05-obrazy-lekkie-i-bezpieczne-python.md`
6. `06-web-worker-scheduler-python.md`
7. `07-dev-vs-prod-python.md`
8. `08-case-study-fastapi-postgres-redis-celery-python.md`
9. `09-debugowanie-buildow-i-healthcheckow-python.md`
10. `ZESTAW-CWICZEN.md`

Kolejność jest celowa: najpierw budujesz intuicję o samym kontenerze i obrazie, potem o składaniu usług, bezpieczeństwie i różnicach środowiskowych, a na końcu spinasz to w przekrojowy case study i praktykę debugowania.

## Jak myśleć o tym folderze

Najważniejsze pytania podczas nauki:

- co dokładnie pakuję do obrazu,
- co musi być w kontenerze, a czego nie powinno tam być,
- jak uruchomić aplikację przewidywalnie na różnych maszynach,
- jak rozdzielić usługi i procesy,
- jak nie mylić wygody developmentu z potrzebami produkcji,
- jak ograniczać rozmiar, ryzyko i chaos konfiguracyjny,
- jak debugować problemy startu usług i gotowości środowiska.

## Najczęstsze pomyłki początkujących

- traktowanie Dockera jako magicznego rozwiązania wszystkich problemów,
- wrzucanie całego projektu bezrefleksyjnie do obrazu,
- budowanie zbyt ciężkich obrazów,
- uruchamianie wszystkiego jako `root`,
- trzymanie sekretów bezpośrednio w obrazie,
- mieszanie ustawień dev i prod w jednym prostym pliku bez jasnych zasad,
- wrzucanie weba, workera i schedulera do jednego procesu bez planu,
- mylenie uruchomionego kontenera z gotową usługą.

## Co tutaj jest najważniejsze praktycznie

W realnym projekcie liczą się decyzje takie jak:

- co powinno znaleźć się w obrazie,
- jak zbudować sensowny `Dockerfile`,
- kiedy `compose` jest wygodne, a kiedy to tylko lokalny orchestration helper,
- jak przekazywać konfigurację przez environment variables,
- jak zmniejszyć obraz i ryzyko bezpieczeństwa,
- jak rozdzielać role kontenerów,
- jak przygotować projekt tak, żeby dev i prod nie były przypadkowo tym samym,
- jak diagnozować buildy, healthchecki, start usług i zależności.

## Jak ten dział łączy się z resztą repo

Ten folder bardzo mocno łączy się z wcześniejszymi działami o:

- webie i API,
- bazach danych,
- messagingu i workerach,
- CI/CD,
- bezpieczeństwie,
- obserwowalności,
- architekturze aplikacji.

To właśnie tutaj kod zaczyna spotykać się z realnym środowiskiem uruchomieniowym.

## Po czym poznasz, że temat rozumiesz

Po przerobieniu folderu powinieneś umieć odpowiedzieć:

- po co używać Dockera w projekcie Pythonowym,
- czym różni się obraz od kontenera,
- jak wygląda rozsądny `Dockerfile`,
- jakie są zagrożenia złej konfiguracji środowiska,
- kiedy warto rozdzielać web, worker i scheduler,
- czemu produkcja nie powinna być kopią środowiska dev 1:1,
- jak myśleć o rozmiarze obrazu, powierzchni ataku i przewidywalności uruchomienia,
- jak debugować problem "kontener działa, ale usługa nie".

## Docelowy efekt

Po opanowaniu tego folderu nie będziesz jeszcze specjalistą od platform engineeringu, ale będziesz mieć bardzo mocny praktyczny fundament do uruchamiania pythonowych aplikacji w bardziej profesjonalnym, przewidywalnym i bezpiecznym środowisku.
