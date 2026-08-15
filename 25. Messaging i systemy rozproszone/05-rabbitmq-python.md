# RabbitMQ python

## O czym jest ten rozdział

RabbitMQ to bardzo popularny broker wiadomości używany w systemach, które potrzebują niezawodnego przekazywania zadań albo komunikatów między komponentami.

Na poziomie intuicji dobrze myśleć o nim tak:

- producent publikuje wiadomość,
- broker ją przyjmuje,
- odpowiedni consumer lub worker ją odbiera.

To narzędzie jest szczególnie ważne tam, gdzie chcesz dobrze kontrolować:

- kolejki,
- routing wiadomości,
- potwierdzenia odbioru,
- retry,
- wzorce dystrybucji pracy.

## Najprostsza intuicja RabbitMQ

RabbitMQ to broker oparty o model kolejek i routingu wiadomości.

Najprościej:

- producer wysyła wiadomość,
- broker decyduje, gdzie ją skierować,
- consumer odbiera ją z odpowiedniej kolejki.

To ważne, bo producer nie musi wiedzieć dokładnie, który worker przetworzy zadanie.

## Exchange, queue, routing key: intuicja

To trzy podstawowe pojęcia, które warto znać.

### Exchange

Exchange przyjmuje wiadomość od producenta i decyduje, do której kolejki lub kolejek ma ją skierować.

### Queue

Queue przechowuje wiadomości do odebrania.

### Routing key

Routing key pomaga zdecydować, jak wiadomość ma zostać skierowana.

Najprościej możesz myśleć tak:

- producer publikuje do exchange,
- exchange patrzy na reguły,
- wiadomość trafia do jednej lub wielu kolejek.

## Prosty przykład myślowy

Masz system zamówień.

Producer publikuje wiadomości:

- `order.created`
- `order.paid`
- `email.send`

RabbitMQ może kierować je do różnych kolejek:

- kolejka maili,
- kolejka faktur,
- kolejka integracji z CRM.

To daje dużo większą kontrolę niż model "wrzuć wszystko do jednej skrzynki".

## Kiedy RabbitMQ ma sens

RabbitMQ ma sens szczególnie wtedy, gdy:

- potrzebujesz klasycznego brokera wiadomości,
- zależy Ci na kolejkach i workerach,
- chcesz dobrze sterować routingiem,
- masz zadania backgroundowe albo integracje asynchroniczne,
- chcesz rozdzielać różne typy wiadomości do różnych ścieżek.

## Kiedy RabbitMQ bywa mniej naturalny

Bywa mniej naturalny, gdy głównym celem jest raczej długoterminowy strumień zdarzeń i odczyt historii eventów przez wiele niezależnych konsumentów.

To zwykle kieruje myślenie bardziej w stronę Kafki.

## Kolejka pracy a broadcast: ważna intuicja

RabbitMQ dobrze pasuje do myślenia:

- "ktoś ma wykonać tę pracę".

Czyli bardzo często:

- jedno zadanie,
- jeden consumer lub worker,
- wykonanie i potwierdzenie.

To trochę inna intuicja niż system stricte event-streamingowy.

## Potwierdzenia odbioru: bardzo ważny temat

Jeśli consumer odbierze wiadomość, ale padnie przed zakończeniem pracy, broker musi wiedzieć, czy wiadomość uznać za przetworzoną czy zwrócić do kolejki.

Tu pojawia się bardzo ważna idea:

- `ack`.

Najprostsza intuicja:

- jeśli worker potwierdzi sukces, broker może uznać wiadomość za obsłużoną,
- jeśli nie ma potwierdzenia, wiadomość może wrócić do ponownego dostarczenia.

To od razu prowadzi do potrzeby idempotencji.

## Minimalna symulacja myślowa

```text
producer -> exchange -> queue -> consumer
```

Przepływ:

```text
order.created published
message routed to invoice queue
worker receives message
worker processes invoice
worker sends ack
message removed from queue
```

## Co się dzieje przy błędzie

Jeśli worker padnie przed `ack`, wiadomość może być dostarczona ponownie.

To znaczy:

- RabbitMQ pomaga w niezawodności,
- ale nie daje gwarancji, że Twój kod może ignorować duble.

## Before/after

### Słabszy model

- aplikacja wywołuje integracje bezpośrednio,
- awaria jednego komponentu psuje request,
- routing zadań jest twardo zakodowany w aplikacji.

### Lepszy model

- producer publikuje wiadomość,
- broker kieruje ją do odpowiednich kolejek,
- consumer przetwarza niezależnie,
- system jest bardziej rozdzielony.

## Mini case study: zamówienie i kilka skutków ubocznych

Po utworzeniu zamówienia chcesz:

- wysłać mail,
- wygenerować PDF,
- zsynchronizować CRM.

### Naiwny model

Backend robi wszystko po kolei w requestcie.

### Lepszy model z RabbitMQ

Backend publikuje odpowiednie wiadomości.

Różne kolejki i workery obsługują:

- mail,
- PDF,
- CRM.

To daje większą odporność i elastyczność.

## RabbitMQ a Celery

To ważne rozróżnienie praktyczne.

Celery:

- jest frameworkiem do tasków w Pythonie.

RabbitMQ:

- jest brokerem wiadomości.

Często one współpracują:

- Celery używa RabbitMQ jako brokera.

Czyli to nie są konkurencyjne pojęcia jeden do jednego.

## Co Pythonowiec powinien rozumieć

Dobrze, żebyś umiał:

- rozumieć rolę brokera jako pośrednika,
- kojarzyć exchange, queue i routing key na poziomie intuicyjnym,
- pamiętać, że `ack` i ponowne dostarczenie zmuszają do idempotencji,
- rozpoznać, kiedy system potrzebuje klasycznych kolejek zadań,
- nie mylić RabbitMQ z samym frameworkiem taskowym.

## Output myślowy

### Bez brokera

- komponenty są bardziej pospinane bezpośrednio,
- awarie przenoszą się łatwiej,
- routing jest sztywny.

### Z RabbitMQ

- komunikacja jest bardziej elastyczna,
- broker przejmuje odpowiedzialność za pośrednictwo,
- ale system wymaga lepszego myślenia o potwierdzeniach i dubelkach.

## Najważniejsze do zapamiętania

- RabbitMQ to broker wiadomości, a nie sam framework taskowy.
- Exchange kieruje wiadomość, queue ją przechowuje, consumer ją odbiera.
- `Ack` jest kluczowy dla niezawodnego przetwarzania.
- Ponowne dostarczenie wiadomości jest normalnym scenariuszem.
- RabbitMQ dobrze pasuje do klasycznych kolejek pracy i routingu komunikatów.

## Ćwiczenia

1. Wyjaśnij własnymi słowami rolę exchange, queue i routing key.
2. Opisz, co może się stać, jeśli worker padnie przed `ack`.
3. Podaj przykład systemu, w którym RabbitMQ ma sens jako broker.
4. Wytłumacz różnicę między RabbitMQ i Celery.
5. Rozpisz flow wiadomości `order.created` do dwóch różnych kolejek.
