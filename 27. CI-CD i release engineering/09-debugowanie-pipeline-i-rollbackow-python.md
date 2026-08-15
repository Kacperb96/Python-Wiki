# Debugowanie pipeline i rollbackow python

## Po co ten plik

W praktyce prawie każdy zespół prędzej czy później widzi sytuacje typu:

- pipeline jest czerwony i nie wiadomo czemu,
- build przechodzi, ale release się psuje,
- staging działa, a produkcja nie,
- deployment trzeba cofnąć,
- changelog albo tag nie zgadzają się z rzeczywistością.

Ten plik zbiera najbardziej praktyczne problemy i sposób myślenia o ich diagnozie.

## Najczęstsze klasy problemów

Najczęściej trafisz na problemy typu:

- failing lint albo typecheck,
- testy przechodzą lokalnie, ale nie przechodzą w CI,
- build artefaktu pada mimo zielonych testów,
- pipeline PR jest zielony, ale pipeline tagowy pada,
- opublikowany artefakt nie odpowiada tagowi,
- staging dostaje inny artefakt niż prod,
- rollback jest niejasny albo ryzykowny.

## Problem 1: testy przechodzą lokalnie, ale nie w CI

### Pierwsze hipotezy

- lokalne środowisko różni się od CI,
- brakują env vars,
- inna wersja Pythona albo zależności,
- test opiera się na niestabilnym stanie lub czasie,
- kolejność testów wpływa na wynik.

### Co sprawdzić

1. wersję Pythona i zależności,
2. różnice env między lokalnym a CI,
3. czy test nie jest flaky,
4. czy test nie zakłada lokalnych plików lub usług,
5. czy pipeline uruchamia dokładnie to samo, co Ty lokalnie.

## Problem 2: lint i typecheck czerwone, choć "kod działa"

To bardzo typowy opór początkujących.

### Najważniejsza intuicja

Pipeline nie ocenia tylko tego, czy kod akurat uruchamia się lokalnie.

Ocena może dotyczyć też:

- standardu jakości,
- czytelności,
- spójności typów,
- bezpieczeństwa dalszych zmian.

Czyli czerwony typecheck może być realnym ostrzeżeniem o przyszłym błędzie, nawet jeśli demo lokalnie działa.

## Problem 3: build artefaktu pada, mimo że testy są zielone

### Możliwe przyczyny

- Dockerfile jest zły,
- brak pliku w artefakcie,
- zależność runtime nie jest uwzględniona,
- packaging jest niekompletny,
- testy nie sprawdzały etapu builda.

To bardzo ważna lekcja:

- testy i build chronią przed innymi klasami problemów.

## Problem 4: pipeline PR zielony, pipeline releasowy czerwony

To też bardzo częste.

### Możliwe przyczyny

- pipeline releasowy robi więcej niż PR-owy,
- publikuje artefakt,
- używa innych sekretów lub registry,
- odpala dodatkowe kroki związane z tagiem,
- wymaga poprawnej wersji albo changelogu.

### Wniosek

Trzeba rozumieć, że różne pipeline'y mają różne role i mogą ujawniać inne klasy problemów.

## Problem 5: nie wiadomo, co naprawdę jest na produkcji

To bardzo poważny sygnał słabości procesu.

### Możliwe przyczyny

- brak spójnych tagów,
- release i deployment nie są jednoznacznie powiązane,
- artefakty są nadpisywane,
- changelog nie odpowiada realnej wersji,
- deployment odbył się bokiem poza oficjalnym procesem.

### Co powinno być możliwe

W dojrzałym procesie powinieneś móc szybko odpowiedzieć:

- jaki tag jest na produkcji,
- jaki commit za nim stoi,
- jaki artefakt został wdrożony,
- kiedy to się stało.

## Problem 6: staging działa, produkcja nie działa

### Pierwsze hipotezy

- środowiska różnią się bardziej, niż powinny,
- prod ma inną konfigurację,
- migracja była niepełna,
- zależność środowiskowa jest inna,
- staging nie był wystarczająco podobny do produkcji.

### Najważniejsza intuicja

Staging ma sens wtedy, gdy realnie zmniejsza niepewność przed prodem.

Jeśli jest zbyt inne, jego wartość mocno spada.

## Rollback: jak o nim myśleć

Rollback to nie tylko przycisk "cofnij".

To świadomy plan odpowiedzi na złą wersję.

Trzeba wiedzieć:

- do jakiej wersji wracamy,
- czy artefakt poprzedniej wersji jest dostępny,
- czy zmiany w danych nie utrudniają powrotu,
- czy rollback aplikacji nie gryzie się z migracją bazy.

## Kiedy rollback jest prostszy

Rollback jest prostszy, gdy:

- artefakty są wersjonowane jednoznacznie,
- wdrażasz ten sam artefakt między środowiskami,
- nie nadpisujesz historii,
- proces deploymentu jest przewidywalny.

## Kiedy rollback jest trudniejszy

Rollback robi się trudny, gdy:

- migracja danych jest nieodwracalna,
- nie wiadomo, jaki artefakt był wcześniej,
- wdrożenia były ręczne i słabo śledzone,
- konfiguracja zmieniała się poza kontrolą procesu.

## Mini case study: broken release notes

Objaw:

- changelog mówi o jednej poprawce,
- użytkownicy widzą też inne zmiany,
- zespół nie wie, skąd różnica.

### Możliwe przyczyny

- tag wskazuje zły commit,
- changelog nie został zsynchronizowany z rzeczywistym releasem,
- release został zrobiony z innej gałęzi niż zakładano,
- proces tagowania i publikacji nie był spójny.

To pokazuje, że dokumentacja releasu też jest częścią jakości procesu.

## Mini case study: rollback po błędzie na produkcji

Objaw:

- po deploymentcie rośnie liczba błędów 500,
- szybki rollback jest potrzebny.

Dojrzały proces powinien umożliwić:

1. identyfikację poprzedniej stabilnej wersji,
2. wskazanie konkretnego artefaktu,
3. szybki powrót,
4. potem analizę przyczyny na spokojnie.

Jeśli tego nie ma, rollback sam staje się dodatkowym źródłem stresu i chaosu.

## Co warto logować i śledzić w procesie

Przydają się rzeczy takie jak:

- status i czas etapów pipeline'u,
- identyfikator artefaktu,
- powiązanie tagu z buildem,
- wynik wdrożenia na staging i prod,
- historia ostatnich deploymentów,
- informacja, kto zatwierdził release albo deployment.

## Szybka checklista debugowania

Gdy coś nie działa w CI/CD, sprawdź po kolei:

1. który etap procesu się wyłożył,
2. czy to problem jakości kodu, buildu, publikacji czy deploymentu,
3. czy artefakt jest poprawny i jednoznacznie oznaczony,
4. czy staging i prod używają tego samego artefaktu,
5. czy tag, changelog i release opisują ten sam stan,
6. czy rollback jest możliwy i bezpieczny,
7. czy problem wynika z procesu, środowiska czy samego kodu.

## Flaky pipeline'y

Pipeline bywa czerwony nie zawsze z powodu złej zmiany.

Czasem problemem jest niestabilność procesu.

Przykłady:

- flaky testy,
- niestabilne zależności zewnętrzne,
- timeouty środowiskowe,
- zmienność środowiska CI.

To bardzo ważne, bo zespół szybko traci zaufanie do pipeline'u, jeśli czerwony kolor nic już realnie nie znaczy.

## Co ten plik pokazuje

Najważniejsza lekcja:

- dojrzały proces CI/CD to nie tylko automatyzacja szczęśliwej ścieżki,
- to także zdolność do diagnozowania, cofania i naprawiania problemów, gdy coś pójdzie źle.

## Najważniejsze do zapamiętania

- Czerwony pipeline może oznaczać bardzo różne klasy problemów i trzeba umieć je rozróżniać.
- Zielony PR pipeline nie gwarantuje poprawnego releasu ani deploymentu.
- Build, release notes, tag i deployment muszą pozostać spójne.
- Rollback trzeba planować zanim będzie potrzebny.
- Zaufanie do procesu rośnie tylko wtedy, gdy pipeline jest stabilny i diagnostyczny.

## Ćwiczenia

1. Rozpisz checklistę debugowania problemu "lokalnie testy zielone, w CI czerwone".
2. Podaj trzy przyczyny, dla których release może się zepsuć mimo zielonego pipeline'u PR.
3. Opisz, kiedy rollback jest prosty, a kiedy staje się trudny.
4. Zaprojektuj dwie metryki lub logi, które pomogłyby śledzić zdrowie procesu deploymentu.
5. Opisz, jak odróżniłbyś problem kodu od problemu procesu albo środowiska CI/CD.
