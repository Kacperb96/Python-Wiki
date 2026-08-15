# 25. Messaging i systemy rozproszone

Ten folder jest o tym, co dzieje się, gdy aplikacja przestaje być jednym prostym requestem do jednej bazy i zaczyna rozmawiać z innymi procesami, workerami, kolejkami i usługami.

Na początku wiele systemów działa synchronicznie:

- request przychodzi,
- backend robi wszystko od razu,
- odpowiedź wraca.

W pewnym momencie to przestaje wystarczać.

Pojawiają się pytania:

- co zrobić, gdy zadanie trwa długo,
- jak odciążyć request-response,
- jak wysłać pracę do workera,
- co jeśli wiadomość dojdzie dwa razy,
- co jeśli worker padnie w połowie,
- skąd biorą się duble i niespójności,
- jak bezpiecznie publikować zdarzenia między usługami.

To właśnie świat messagingu i systemów rozproszonych.

## Cel folderu

Po przerobieniu tego działu powinieneś:

- rozumieć różnicę między synchronicznym wywołaniem a komunikacją przez kolejkę,
- wiedzieć, czym są broker, producer, consumer i worker,
- rozumieć, po co istnieją retry i czemu bez idempotencji są niebezpieczne,
- wiedzieć, czym jest eventual consistency i skąd bierze się opóźniona spójność,
- rozumieć praktyczne użycie Celery,
- znać podstawową intuicję RabbitMQ i Kafki,
- wiedzieć, po co istnieje outbox pattern,
- umieć rozpoznawać najczęstsze pułapki systemów opartych o wiadomości,
- umieć spojrzeć na messaging jako na cały przepływ: stan, event, consumer, retry i debugging razem.

## Jak czytać ten dział

Najlepiej iść po kolei:

1. `01-kolejki-i-brokery-python.md`
2. `02-retry-i-idempotencja-python.md`
3. `03-eventual-consistency-python.md`
4. `04-celery-glebiej-python.md`
5. `05-rabbitmq-python.md`
6. `06-kafka-python.md`
7. `07-outbox-pattern-python.md`
8. `08-case-study-orders-event-driven-python.md`
9. `09-testy-i-debugowanie-messaging-python.md`
10. `ZESTAW-CWICZEN.md`

Ta kolejność ma sens, bo najpierw budujesz intuicję o samym modelu komunikacji, potem o niezawodności, potem o konkretnych narzędziach i wzorcach projektowych, a na końcu spinasz to w większy case study i praktykę testowania oraz debugowania.

## Jak myśleć o tym folderze

Najważniejsze pytania podczas nauki:

- co dzieje się, gdy nie mogę zrobić wszystkiego synchronicznie,
- kto wysyła wiadomość,
- kto ją odbiera,
- co jeśli wiadomość zginie albo dojdzie dwa razy,
- czy system nadal jest spójny, jeśli część rzeczy dzieje się później,
- gdzie kończy się wygoda asynchroniczności, a zaczyna złożoność rozproszona,
- jak testować i diagnozować opóźnienia, duble i częściowe awarie.

## Najczęstsze pomyłki początkujących

- myślenie, że kolejka "magicznie rozwiązuje skalowanie",
- brak idempotencji przy retry,
- zakładanie, że wiadomość wykona się dokładnie raz,
- brak rozumienia, że eventual consistency jest normalnym skutkiem rozproszenia,
- używanie ciężkiego brokera bez jasnej potrzeby,
- brak rozróżnienia między zadaniami backgroundowymi a event-driven komunikacją między usługami,
- publikowanie eventu bez gwarancji, że stan w bazie i event są spójne,
- skupienie się na samym publish zamiast na całym lifecycle wiadomości.

## Co tutaj jest najważniejsze praktycznie

W realnym projekcie liczą się decyzje takie jak:

- czy to powinno być synchroniczne czy asynchroniczne,
- czy potrzebujesz kolejki z workerami czy raczej strumienia zdarzeń,
- jak obsłużyć ponowne próby,
- jak zapobiec dubelkom,
- jak zaprojektować bezpieczny consumer,
- jak pogodzić bazę danych z publikacją eventów,
- jak diagnozować system, w którym rzeczy dzieją się "później" i w wielu miejscach naraz,
- jak mierzyć backlog, lagi i zdrowie konsumentów.

## Jak ten dział łączy się z resztą repo

Ten folder bardzo mocno łączy się z wcześniejszymi działami o:

- webie i API,
- bazach danych,
- testowaniu,
- debugowaniu,
- asynchroniczności,
- architekturze,
- obserwowalności,
- bezpieczeństwie.

To tutaj wiele tematów z wcześniejszych folderów zaczyna pracować jednocześnie.

## Po czym poznasz, że temat rozumiesz

Po przerobieniu folderu powinieneś umieć odpowiedzieć:

- kiedy warto użyć kolejki,
- czym różni się broker od workera,
- czemu retry bez idempotencji jest niebezpieczne,
- skąd biorą się duble wiadomości,
- czym jest eventual consistency i czemu nie jest "bugiem samym w sobie",
- kiedy RabbitMQ ma sens, a kiedy Kafka,
- po co istnieje outbox pattern,
- jak myśleć o niezawodności w systemie opartym o wiadomości,
- jak zdebugować lag kolejki albo znikający event,
- jak testować system messagingowy warstwowo.

## Docelowy efekt

Po opanowaniu tego folderu nie będziesz jeszcze ekspertem od systemów rozproszonych, ale będziesz mieć bardzo mocny praktyczny fundament do pracy z kolejkami, workerami, zdarzeniami i asynchroniczną integracją w projektach Pythonowych.
