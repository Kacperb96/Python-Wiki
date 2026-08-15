# Narzędzia kolejkowe w Pythonie — RabbitMQ, Celery, Kafka

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co używać systemów kolejkowych](#po-co-używać-systemów-kolejkowych)
3. [Kiedy kolejka ma sens](#kiedy-kolejka-ma-sens)
4. [Podstawowe pojęcia](#podstawowe-pojęcia)
5. [Producent i konsument](#producent-i-konsument)
6. [RabbitMQ](#rabbitmq)
7. [Celery](#celery)
8. [Kafka](#kafka)
9. [RabbitMQ vs Celery vs Kafka](#rabbitmq-vs-celery-vs-kafka)
10. [Przykładowy mentalny przepływ](#przykładowy-mentalny-przepływ)
11. [Retry, idempotencja i odporność](#retry-idempotencja-i-odporność)
12. [Kolejki a asynchroniczność w aplikacji](#kolejki-a-asynchroniczność-w-aplikacji)
13. [Typowe błędy początkujących](#typowe-błędy-początkujących)
14. [Praktyczna ściąga](#praktyczna-ściąga)
15. [Ćwiczenia](#ćwiczenia)
16. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

Systemy kolejkowe pozwalają rozdzielać pracę między różne części systemu.

Zamiast robić wszystko natychmiast w jednym miejscu, możesz:

- wrzucić zadanie do kolejki,
- odebrać je później,
- przetworzyć niezależnie,
- zwiększyć skalę systemu.

To bardzo ważne w większych aplikacjach i architekturach rozproszonych.

---

## Po co używać systemów kolejkowych

Kolejki rozwiązują kilka praktycznych problemów:

- odciążają główną aplikację,
- wygładzają skoki ruchu,
- pozwalają przetwarzać zadania w tle,
- zwiększają niezawodność,
- rozdzielają producenta od konsumenta.

Przykład:

użytkownik wysyła formularz, a aplikacja nie musi od razu wysyłać maila, generować PDF i robić analityki w tym samym żądaniu HTTP.

---

## Kiedy kolejka ma sens

Najczęściej gdy:

- zadanie trwa długo,
- zadanie może być wykonane później,
- potrzebujesz workerów w tle,
- obciążenie przychodzi falami,
- chcesz oddzielić usługi od siebie.

---

## Podstawowe pojęcia

Warto znać:

- message,
- queue,
- producer,
- consumer,
- broker,
- topic,
- acknowledgment,
- retry,
- idempotencję.

To słownictwo wraca w prawie każdym systemie kolejkowym.

---

## Producent i konsument

Producent:

- wysyła wiadomość.

Konsument:

- odbiera i przetwarza wiadomość.

Dzięki temu komponent wysyłający nie musi wiedzieć dokładnie, kiedy i gdzie zadanie zostanie wykonane.

---

## RabbitMQ

RabbitMQ to broker wiadomości.

Jest często używany do:

- kolejek zadań,
- routingu komunikatów,
- klasycznej komunikacji producer-consumer.

Dobrze pasuje do scenariuszy typu:

- wyślij zadanie do workera,
- odbierz i potwierdź wykonanie,
- rozdziel ruch między konsumentów.

---

## Celery

Celery to framework do zadań w tle w Pythonie.

To nie jest sam broker.

Celery zwykle korzysta z brokera, np.:

- RabbitMQ,
- Redis.

Celery daje:

- definicję tasków,
- workerów,
- retry,
- harmonogramy,
- wygodne uruchamianie zadań asynchronicznych z poziomu kodu aplikacji.

Mentalnie:

aplikacja mówi „wykonaj to później”, a Celery zajmuje się dostarczeniem zadania do workera.

---

## Kafka

Kafka to platforma do strumieniowania zdarzeń i bardzo wydajnego przesyłania danych.

Jest często używana do:

- event streamingu,
- logów zdarzeń,
- integracji między usługami,
- analityki danych w czasie zbliżonym do rzeczywistego.

Kafka mentalnie różni się od prostych kolejek zadań.

Tu częściej myślisz o strumieniu zdarzeń i historii komunikatów niż o pojedynczym „zrób task i zapomnij”.

---

## RabbitMQ vs Celery vs Kafka

### RabbitMQ

To broker wiadomości.

### Celery

To framework tasków w tle, zwykle używający brokera.

### Kafka

To platforma event streamingowa, bardziej do zdarzeń i przepływów danych niż do prostych tasków backgroundowych.

To nie są rzeczy całkiem wymienne 1:1.

---

## Przykładowy mentalny przepływ

Scenariusz:

1. użytkownik wrzuca plik do aplikacji,
2. aplikacja zapisuje zgłoszenie,
3. zamiast od razu robić ciężkie przetwarzanie, wysyła wiadomość do kolejki,
4. worker odbiera zadanie,
5. przetwarza plik,
6. zapisuje wynik,
7. opcjonalnie wysyła kolejne zdarzenie albo powiadomienie.

To jest właśnie bardzo typowy wzorzec „task w tle”.

---

## Retry, idempotencja i odporność

To bardzo ważne pojęcia.

### Retry

Jeśli zadanie chwilowo się nie uda, system może spróbować ponownie.

### Idempotencja

Jeśli to samo zadanie wykona się drugi raz, wynik nie powinien zepsuć systemu.

To ważne, bo w systemach rozproszonych duplikaty i powtórzenia naprawdę się zdarzają.

---

## Kolejki a asynchroniczność w aplikacji

Ważne rozróżnienie:

- async w aplikacji pomaga przeplatać oczekujące operacje,
- kolejka pomaga oddelegować pracę poza aktualne żądanie albo poza aktualny proces.

To są różne poziomy rozwiązania problemu.

`async` nie zastępuje RabbitMQ czy Celery.

Celery nie zastępuje `asyncio`.

---

## Typowe błędy początkujących

- traktowanie RabbitMQ, Celery i Kafki jak dokładnie tego samego,
- wrzucanie wszystkiego do kolejki bez potrzeby,
- brak myślenia o retry,
- brak myślenia o idempotencji,
- mieszanie prostych task queue z event streamingiem.

---

## Praktyczna ściąga

### Gdy chcesz taski w tle w Pythonie

Bardzo często myślisz o:

- Celery,
- brokerze typu RabbitMQ albo Redis.

### Gdy myślisz o strumieniu zdarzeń

Częściej pojawia się Kafka.

### Pytanie praktyczne

Czy chcesz:

- wykonać zadanie później,
- czy przesyłać i konsumować strumień zdarzeń?

To rozróżnienie jest kluczowe.

---

## Ćwiczenia

1. Rozpisz rolę producenta, konsumenta i brokera.
2. Opisz scenariusz, w którym RabbitMQ ma sens.
3. Opisz scenariusz, w którym Celery ma sens.
4. Opisz scenariusz, w którym Kafka ma sens.
5. Wyjaśnij różnicę między task queue i event streamingiem.
6. Wyjaśnij własnymi słowami, czemu idempotencja jest ważna.

---

## Najważniejsze do zapamiętania

- Kolejki służą do oddelegowywania i rozdzielania pracy.
- RabbitMQ to broker wiadomości.
- Celery to framework tasków w tle, zwykle używający brokera.
- Kafka jest bardziej o strumieniu zdarzeń niż o prostych taskach backgroundowych.
- Retry i idempotencja są kluczowe w systemach rozproszonych.
