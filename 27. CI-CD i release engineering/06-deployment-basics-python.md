# Deployment basics python

## O czym jest ten rozdział

W pewnym momencie każda sensowna ścieżka CI/CD dochodzi do najważniejszego pytania:

- jak bezpiecznie uruchomić nową wersję systemu w konkretnym środowisku?

To właśnie deployment.

Deployment to nie jest tylko techniczny moment "wrzuć nowy kod".

To proces, który wpływa na:

- dostępność systemu,
- ryzyko błędów,
- możliwość rollbacku,
- bezpieczeństwo zmian,
- komfort operacyjny zespołu.

## Najprostsza intuicja

Deployment to moment, w którym przygotowany artefakt zostaje wdrożony do konkretnego środowiska.

Najprościej:

- masz gotową wersję,
- masz gotowy artefakt,
- uruchamiasz go w środowisku docelowym.

To może być:

- staging,
- produkcja,
- środowisko testowe,
- środowisko wewnętrzne.

## Deployment to nie build

To trzeba rozróżniać bardzo jasno.

Build odpowiada na pytanie:

- czy potrafimy stworzyć artefakt?

Deployment odpowiada na pytanie:

- czy potrafimy uruchomić ten artefakt w konkretnym środowisku?

Możesz mieć poprawny build i zły deployment.

## Deployment to nie release

Release mówi:

- ta wersja jest gotowa i oznaczona.

Deployment mówi:

- ta wersja została uruchomiona gdzieś konkretnie.

To nadal nie to samo.

## Co zwykle musi być gotowe przed deploymentem

Najczęściej potrzebujesz:

- poprawnego artefaktu,
- przejścia quality gates,
- wersji, którą można wskazać jednoznacznie,
- wiedzy, do jakiego środowiska wdrażasz,
- sensownego planu rollbacku albo przynajmniej planu reakcji.

## Deployment staging vs deployment prod

To dwa bardzo różne momenty procesu.

### Staging

Często służy do:

- ostatniej walidacji,
- sprawdzenia integracji,
- porównania z produkcyjnym układem,
- redukcji ryzyka przed produkcją.

### Produkcja

To już moment o dużo większej odpowiedzialności.

Tu liczy się bardziej:

- bezpieczeństwo procesu,
- obserwowalność,
- możliwość szybkiej reakcji,
- ograniczanie wpływu błędów na użytkowników.

## Najprostszy model deploymentu

Uproszczony model może wyglądać tak:

1. wybierasz artefakt wersji `v1.4.0`,
2. wdrażasz go na staging,
3. weryfikujesz działanie,
4. wdrażasz ten sam artefakt na produkcję.

To bardzo zdrowa praktyka, bo:

- nie budujesz czegoś nowego pomiędzy staging i prod,
- promujesz ten sam artefakt dalej.

## Dlaczego to ważne

Jeśli dla staging i prod budujesz osobne artefakty z różnych momentów, łatwo tracisz przewidywalność.

Lepsza praktyka:

- jeden artefakt,
- wiele środowisk,
- różna konfiguracja, ale ten sam rdzeń wersji.

## Before/after

### Słabszy model

- wdrożenie jest ręczne i mało powtarzalne,
- nie wiadomo dokładnie, co trafiło na środowisko,
- rollback jest niejasny.

### Lepszy model

- deployment ma jasne wejścia i warunki,
- wiadomo, jaki artefakt jest wdrażany,
- proces jest bardziej powtarzalny,
- zespół wie, jak reagować na problemy.

## Rollback: po co o nim myśleć

Rollback to temat, który początkujący często pomijają aż do pierwszej poważnej awarii.

Najprościej:

- jeśli nowa wersja robi problem,
- chcesz wiedzieć, jak wrócić do poprzedniej działającej wersji.

Nie zawsze rollback jest prosty, szczególnie przy zmianach danych i migracjach, ale trzeba o nim myśleć z wyprzedzeniem.

## Deployment a migracje bazy

To bardzo ważny praktyczny temat.

Jeśli nowa wersja wymaga migracji:

- trzeba wiedzieć, kiedy migracja jest wykonywana,
- czy jest zgodna z rolloutem aplikacji,
- czy rollback aplikacji nie wejdzie w konflikt z nowym schematem danych.

To pokazuje, że deployment to nie tylko podmiana obrazu albo paczki.

## Mini case study: backend webowy

Masz backend FastAPI jako obraz Dockera.

Deployment wygląda tak:

1. pipeline buduje obraz `v2.1.0`,
2. obraz trafia do registry,
3. staging pobiera i uruchamia ten obraz,
4. po walidacji produkcja dostaje ten sam obraz.

To bardzo zdrowy model podstawowy.

## Mini case study: nieudany deployment

Objaw:

- build przeszedł,
- ale po wdrożeniu API zwraca błędy.

Możliwe przyczyny:

- brak zgodności env,
- brak migracji,
- zła konfiguracja sekretów,
- zależność środowiskowa niegotowa,
- artefakt jest poprawny, ale środowisko nie jest gotowe na jego uruchomienie.

To pokazuje, że deployment ma własny obszar ryzyka niezależny od samego pipeline'u buildowego.

## Co Pythonowiec powinien rozumieć

Dobrze, żebyś umiał:

- odróżniać build, release i deployment,
- myśleć o deploymentach jako o procesie środowiskowym, nie tylko technicznym pushu,
- rozumieć sens stagingu,
- wiedzieć, czemu ten sam artefakt powinien przechodzić dalej między środowiskami,
- pamiętać o rollbacku i migracjach.

## Output myślowy

### Chaotyczny deployment

- trudno powiedzieć, co jest wdrożone,
- rollback jest niejasny,
- środowiska rozjeżdżają się.

### Dojrzalszy deployment

- wiadomo, jaki artefakt idzie gdzie,
- staging i prod są sensownymi etapami procesu,
- zespół ma lepszą kontrolę nad ryzykiem.

## Najważniejsze do zapamiętania

- Deployment to uruchomienie konkretnego artefaktu w konkretnym środowisku.
- Build, release i deployment to trzy różne rzeczy.
- Staging i prod mają różne role w procesie.
- Warto promować ten sam artefakt między środowiskami.
- Rollback i migracje bazy to część myślenia o deploymentach, nie temat poboczny.

## Ćwiczenia

1. Wyjaśnij własnymi słowami różnicę między buildem, release'em i deploymentem.
2. Opisz, czemu staging jest wartościowym etapem przed produkcją.
3. Rozpisz prosty deployment flow dla backendu w obrazie Dockera.
4. Wytłumacz, czemu rollback trzeba planować zanim pojawi się awaria.
5. Opisz ryzyko wdrożenia nowej wersji bez myślenia o migracjach bazy.
