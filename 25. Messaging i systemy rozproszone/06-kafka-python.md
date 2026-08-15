# Kafka python

## O czym jest ten rozdział

Kafka to narzędzie, które bardzo często pojawia się wtedy, gdy system przestaje myśleć tylko kategorią "zrób zadanie w tle", a zaczyna myśleć kategorią:

- publikujemy zdarzenia,
- wiele systemów może je konsumować,
- dane płyną jako strumień,
- liczy się kolejność, skala i możliwość niezależnego odczytu.

To ważne, bo Kafka nie jest po prostu "kolejnym RabbitMQ" w przebraniu. Intuicja użycia jest inna.

## Najprostsza intuicja Kafki

Kafka bardzo dobrze pasuje do myślenia o zdarzeniach jako strumieniu danych.

Najprościej:

- producer publikuje event,
- event trafia do topicu,
- consumer czyta ten event,
- inni consumerzy też mogą go czytać niezależnie.

Czyli to nie musi być model:

- jedno zadanie dla jednego workera.

Bardziej chodzi o:

- zdarzenie staje się częścią strumienia, który różne systemy mogą przetwarzać po swojemu.

## Topic, partition, offset: intuicja

To trzy kluczowe pojęcia.

### Topic

Topic to logiczny kanał zdarzeń.

Przykłady:

- `orders.created`
- `payments.completed`
- `users.updated`

### Partition

Partition to część topicu, która pomaga skalować zapis i odczyt.

Dobrze myśleć o niej jako o fragmencie strumienia.

### Offset

Offset to pozycja wiadomości w partition.

Consumer wie dzięki temu, do którego miejsca już doszedł.

## Najważniejsza różnica intuicyjna względem klasycznej kolejki

W klasycznej kolejce często myślisz:

- wiadomość ma zostać odebrana i zniknąć z codziennej ścieżki pracy.

W Kafce częściej myślisz:

- zdarzenie zostało zapisane do strumienia,
- różni konsumenci mogą je czytać niezależnie,
- ważne jest śledzenie pozycji czytania.

To bardzo inny model.

## Prosty przykład myślowy

Masz event:

```text
order.created
```

Może go czytać:

- system mailingowy,
- system raportowy,
- system CRM,
- system analityczny,
- system antifraud.

I każdy z nich może przetwarzać ten sam event osobno, swoim tempem.

To jedna z największych zalet tego modelu.

## Kiedy Kafka ma sens

Kafka ma sens szczególnie wtedy, gdy:

- masz dużo zdarzeń,
- kilka systemów chce konsumować te same eventy,
- myślisz strumieniowo,
- potrzebujesz dobrze skalować publikację i odczyt,
- architektura jest bardziej event-driven niż task-driven.

## Kiedy Kafka może być za ciężka

Kafka bywa przerostem formy, gdy:

- potrzebujesz po prostu kilku tasków w tle,
- system jest mały,
- jeden worker ma wykonać jedno zadanie,
- nie potrzebujesz osobnego modelu strumienia zdarzeń.

Wtedy klasyczny broker i worker mogą być prostsze i lepsze.

## Consumer groups: intuicja

Kafka pozwala łączyć konsumentów w grupy.

Najprościej:

- jedna grupa konsumuje topic jako jeden logiczny odbiorca,
- kilka instancji w grupie może dzielić pracę między siebie,
- inna grupa może niezależnie czytać ten sam topic od swojej pozycji.

To jest bardzo ważne praktycznie.

Przykład:

- grupa `billing-service`,
- grupa `analytics-service`,
- grupa `email-service`.

Każda grupa ma swój własny postęp czytania.

## Offsety: czemu są ważne

Offset mówi, gdzie consumer jest w strumieniu.

To oznacza, że system może odpowiadać na pytania:

- co już przeczytano,
- gdzie zatrzymał się consumer,
- czy consumer nadąża,
- czy można odtworzyć przetwarzanie od wcześniejszego miejsca.

To daje ogromną moc, ale też dodatkową złożoność.

## Before/after

### Myślenie kolejką pracy

- jedno zadanie,
- ktoś ma je wykonać,
- ważne jest przekazanie pracy.

### Myślenie strumieniem zdarzeń

- zdarzenie staje się częścią ciągu danych,
- różne systemy mogą czytać je niezależnie,
- ważna jest skala, kolejność i pozycja odczytu.

## Mini case study: zdarzenia zamówień

Masz topic `orders.events`.

Publikowane eventy:

- `order.created`
- `order.paid`
- `order.cancelled`

### Kto może to czytać

- billing,
- CRM,
- analityka,
- dashboard operacyjny,
- system notyfikacji.

Każdy z nich działa niezależnie.

To bardzo naturalny model dla Kafki.

## Kafka a RabbitMQ

To częste źródło zamieszania.

RabbitMQ częściej kojarzy się z:

- klasycznym brokerem,
- kolejkami pracy,
- routingiem wiadomości,
- taskami i workerami.

Kafka częściej kojarzy się z:

- event streamingiem,
- topicami i partycjami,
- wieloma niezależnymi konsumentami,
- czytaniem strumienia danych.

To nie znaczy, że granica jest absolutna, ale intuicja projektowa jest inna.

## Ważna pułapka: wydarzenie to nie rozkaz

W architekturze eventowej często warto odróżniać:

- command — "zrób to",
- event — "to się właśnie wydarzyło".

Kafka bardzo często pasuje bardziej do tego drugiego modelu.

To wpływa na sposób myślenia o kontraktach i odpowiedzialnościach usług.

## Co Pythonowiec powinien rozumieć

Dobrze, żebyś umiał:

- odróżnić model task-driven od event-driven,
- rozumieć topic, partition i offset na poziomie intuicyjnym,
- wiedzieć, że różne grupy konsumentów mogą czytać to samo niezależnie,
- rozpoznać, kiedy system bardziej przypomina strumień eventów niż klasyczną kolejkę,
- nie wdrażać Kafki tylko dlatego, że "duże firmy używają".

## Output myślowy

### Bez myślenia strumieniowego

- Kafka wygląda jak zbyt skomplikowana kolejka,
- zespół próbuje używać jej jak prostego work queue.

### Ze zrozumieniem modelu

- widać, że chodzi o strumień zdarzeń,
- różne systemy mogą niezależnie konsumować dane,
- architektura robi się bardziej event-driven i skalowalna.

## Najważniejsze do zapamiętania

- Kafka lepiej pasuje do strumieni zdarzeń niż do prostego modelu "jedno zadanie dla jednego workera".
- Topic, partition i offset to podstawowe pojęcia tego modelu.
- Różne grupy konsumentów mogą niezależnie czytać ten sam strumień.
- Kafka i RabbitMQ rozwiązują częściowo inne klasy problemów.
- Kafka ma sens wtedy, gdy architektura naprawdę potrzebuje modelu event streamingowego.

## Ćwiczenia

1. Wyjaśnij własnymi słowami różnicę między topicem, partition i offsetem.
2. Opisz sytuację, w której Kafka ma większy sens niż klasyczna kolejka z workerem.
3. Wytłumacz, czemu różne grupy konsumentów są tak ważne.
4. Porównaj intuicyjnie RabbitMQ i Kafkę bez wchodzenia w detale implementacyjne.
5. Rozpisz flow eventu `order.created` czytanego przez trzy niezależne systemy.
