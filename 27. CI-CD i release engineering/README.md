# 27. CI-CD i release engineering

Ten folder jest o tym, jak przejść od "kod działa lokalnie" do modelu, w którym zmiany są sprawdzane, budowane, wersjonowane i wdrażane w bardziej przewidywalny sposób.

Na początku wiele projektów działa tak:

- ktoś pisze kod,
- odpala testy lokalnie albo nie,
- ręcznie wrzuca zmiany na serwer,
- nikt do końca nie wie, co dokładnie weszło na produkcję i kiedy.

Przez jakiś czas to może działać.

Potem pojawiają się pytania:

- kto zepsuł build,
- czy testy naprawdę przeszły,
- co dokładnie weszło do releasu,
- jak odtworzyć wersję z wczoraj,
- jak robić wdrożenia bez chaosu,
- jak nie pomylić publikacji, tagu i deploymentu.

To właśnie świat CI/CD i release engineeringu.

## Cel folderu

Po przerobieniu tego działu powinieneś:

- rozumieć, po co istnieje pipeline `lint -> test -> typecheck -> build`,
- wiedzieć, jak wygląda sensowny workflow releasowy,
- rozumieć rolę changelogu i tagowania,
- wiedzieć, czym są quality gates i po co się je stosuje,
- rozumieć sens automatycznej publikacji artefaktów,
- znać podstawy deploymentu z perspektywy procesu, a nie konkretnej platformy,
- rozumieć, czym różnią się różne strategie releasów,
- umieć myśleć o wdrożeniu jako o kontrolowanym procesie inżynierskim, a nie ręcznej improwizacji,
- umieć spojrzeć na cały proces od PR do rollbacku jako jedną spójną ścieżkę dostarczania zmian.

## Jak czytać ten dział

Najlepiej iść po kolei:

1. `01-pipeline-lint-test-typecheck-build-python.md`
2. `02-release-workflow-python.md`
3. `03-changelog-i-tagowanie-python.md`
4. `04-quality-gates-python.md`
5. `05-automatyczna-publikacja-python.md`
6. `06-deployment-basics-python.md`
7. `07-strategia-releasow-python.md`
8. `08-case-study-pr-do-deployment-python.md`
9. `09-debugowanie-pipeline-i-rollbackow-python.md`
10. `ZESTAW-CWICZEN.md`

Kolejność jest celowa: najpierw budujesz intuicję o jakości zmian i pipeline'ie, potem o release flow, a na końcu o wdrożeniach, strategiach operacyjnych oraz debugowaniu realnych problemów procesu.

## Jak myśleć o tym folderze

Najważniejsze pytania podczas nauki:

- co musi zostać sprawdzone, zanim zmiana może wejść dalej,
- jak upewnić się, że wynik pipeline'u jest powtarzalny,
- jak powiązać commit, build, tag i release,
- kto i kiedy decyduje o wdrożeniu,
- jak zmniejszyć ryzyko releasu,
- jak sprawić, żeby proces nie zależał od pamięci jednej osoby,
- jak diagnozować awarie procesu, gdy pipeline albo deployment nie zachowują się tak, jak powinny.

## Najczęstsze pomyłki początkujących

- traktowanie CI jako miejsca tylko do odpalania testów,
- brak rozróżnienia między buildem, release'em i deploymentem,
- ręczne tagowanie i publikowanie bez spójnych zasad,
- zbyt luźne quality gates,
- brak wiedzy, która wersja jest naprawdę wdrożona,
- wrzucanie sekretów do pipeline'u bez planu,
- przekonanie, że automatyzacja bez procesu sama z siebie daje porządek,
- brak planu rollbacku i brak śledzalności artefaktów.

## Co tutaj jest najważniejsze praktycznie

W realnym projekcie liczą się decyzje takie jak:

- co powinno być obowiązkowym etapem pipeline'u,
- kiedy build ma się zatrzymać,
- jak wersjonować release,
- jak prowadzić changelog bez chaosu,
- co publikować automatycznie, a co wymaga świadomej decyzji,
- jak ograniczać ryzyko wdrożeń,
- jak zrobić proces, który jest przewidywalny także za pół roku,
- jak debugować sytuację, w której pipeline jest zielony, a wdrożenie i tak psuje system.

## Jak ten dział łączy się z resztą repo

Ten folder bardzo mocno łączy się z wcześniejszymi działami o:

- testowaniu,
- typowaniu,
- packagingu,
- Dockerze,
- bezpieczeństwie,
- obserwowalności,
- architekturze aplikacji.

To tutaj wiele wcześniejszych praktyk zamienia się w realny, powtarzalny proces dostarczania zmian.

## Po czym poznasz, że temat rozumiesz

Po przerobieniu folderu powinieneś umieć odpowiedzieć:

- jakie etapy powinny być w sensownym pipeline'ie,
- czym różni się release od deploymentu,
- po co istnieją tagi i changelog,
- kiedy pipeline powinien blokować merge albo publikację,
- jak automatyzować publikację bez utraty kontroli,
- jakie są podstawowe strategie releasów,
- jak budować proces, który wspiera zespół zamiast go spowalniać bez sensu,
- jak zdebugować czerwony pipeline, zły release albo potrzebę rollbacku.

## Docelowy efekt

Po opanowaniu tego folderu nie będziesz jeszcze specjalistą od platform engineeringu czy release managementu, ale będziesz mieć bardzo mocny praktyczny fundament do budowania sensownych pipeline'ów, release flow i wdrożeń w projektach Pythonowych.
