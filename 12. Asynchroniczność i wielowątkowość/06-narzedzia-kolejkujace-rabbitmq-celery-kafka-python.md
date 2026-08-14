# Narzędzia kolejkujące w Pythonie — RabbitMQ, Celery, Kafka

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
10. [Typowe zastosowania](#typowe-zastosowania)
11. [Retry, idempotencja i odporność](#retry-idempotencja-i-odporność)
12. [Kolejki a asynchroniczność w aplikacji](#kolejki-a-asynchroniczność-w-aplikacji)
13. [Typowe błędy początkujących](#typowe-błędy-początkujących)
14. [Praktyczne przykłady](#praktyczne-przykłady)
15. [Dobre praktyki](#dobre-praktyki)
16. [Podsumowanie](#podsumowanie)
17. [Mini ściąga](#mini-ściąga)
18. [Ćwiczenia](#ćwiczenia)
19. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

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
- retry.

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

Zwykle dobrze pasuje do scenariuszy typu:

- wyślij zadanie do workera,
- odbierz i potwierdź wykonanie,
- rozdziel ruch między konsumentów.

RabbitMQ kojarzy się z AMQP i klasycznym messagingiem.

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

Przykład mentalny:

aplikacja mówi "wykonaj to później", a Celery zajmuje się dostarczeniem zadania do workera.

---

## Kafka

Kafka to platforma do strumieniowania zdarzeń i bardzo wydajnego przesyłania danych.

Jest często używana do:

- event streaming,
- logów zdarzeń,
- integracji między usługami,
- analityki danych w czasie zbliżonym do rzeczywistego.

Kafka różni się mentalnie od prostych kolejek zadań.

Często bardziej myślisz o strumieniu zdarzeń i historii komunikatów niż o pojedynczym "zrób task i zapomnij".

---

## RabbitMQ vs Celery vs Kafka

Najprościej:

`RabbitMQ`:

- broker wiadomości.

`Celery`:

- framework do tasków w tle w Pythonie,
- zwykle działa na brokerze, np. RabbitMQ.

`Kafka`:

- platforma event streamingowa,
- świetna do dużej skali i przepływu zdarzeń.

To nie są idealni bezpośredni konkurenci w każdym scenariuszu.

---

## Typowe zastosowania

RabbitMQ:

- task queue,
- kolejki workerów,
- routing zadań.

Celery:

- maile w tle,
- generowanie raportów,
- przetwarzanie obrazów po uploadzie,
- harmonogramowane zadania.

Kafka:

- eventy biznesowe,
- pipeline danych,
- logowanie zdarzeń,
- integracja wielu mikroserwisów.

---

## Retry, idempotencja i odporność

To bardzo ważna część pracy z kolejkami.

Jeśli zadanie się nie uda, system może spróbować ponownie.

Dlatego zadania powinny być możliwie:

- idempotentne,
- odporne na powtórne wykonanie,
- dobrze logowane.

Przykład ryzyka:

jeśli task wysyła mail bez zabezpieczenia, retry może wysłać go dwa razy.

---

## Kolejki a asynchroniczność w aplikacji

To dwa różne poziomy problemu.

`asyncio`:

- pomaga w ramach jednego procesu i jednego programu.

System kolejkowy:

- rozdziela pracę między procesy, maszyny i usługi.

Można używać obu rzeczy jednocześnie, ale nie zastępują się wprost.

---

## Typowe błędy początkujących

- mylenie Celery z brokerem,
- używanie Kafki do prostych zadań, gdzie wystarczyłaby zwykła kolejka,
- brak idempotencji,
- brak retry policy,
- brak monitoringu i obserwowalności workerów,
- wrzucanie do komunikatów zbyt ciężkich danych.

---

## Praktyczne przykłady

### Przykład mentalny z Celery

```python
from celery import Celery

app = Celery("tasks", broker="pyamqp://guest@localhost//")

@app.task
def dodaj(a, b):
    return a + b
```

Wywołanie:

```python
wynik = dodaj.delay(2, 3)
```

Tutaj zadanie trafia do brokera, a worker wykona je później.

### Przykład myślowy z RabbitMQ

- aplikacja publikuje komunikat "przetworz zamowienie",
- kolejka przechowuje wiadomość,
- worker odbiera komunikat,
- po sukcesie wysyła potwierdzenie.

### Przykład myślowy z Kafką

- serwis płatności publikuje zdarzenie `payment_completed`,
- inne usługi czytają to zdarzenie,
- analityka, powiadomienia i księgowość reagują niezależnie.

---

## Dobre praktyki

- dobieraj narzędzie do problemu, a nie do mody,
- projektuj taski jako idempotentne,
- dodawaj retry z rozsądnym backoffem,
- monitoruj kolejki, opóźnienia i błędy workerów,
- nie wkładaj do wiadomości więcej danych, niż trzeba.

---

## Podsumowanie

RabbitMQ, Celery i Kafka rozwiązują podobny obszar, ale nie ten sam problem.

W dużym uproszczeniu:

- RabbitMQ dobrze pasuje do klasycznych kolejek wiadomości,
- Celery do tasków w tle w ekosystemie Pythona,
- Kafka do event streaming i dużej skali zdarzeń.

Najważniejsze jest zrozumienie architektury, a nie tylko składni.

---

## Mini ściąga

Najkrócej:

- `RabbitMQ` = broker wiadomości,
- `Celery` = taski w tle dla Pythona,
- `Kafka` = strumienie zdarzeń i event streaming.

Pamiętaj:

- kolejka odciąża aplikację,
- retry wymaga ostrożności,
- idempotencja jest kluczowa,
- async w kodzie i system kolejkowy to różne warstwy rozwiązania.

---

## Ćwiczenia

1. Wyjaśnij własnymi słowami różnicę między producentem a konsumentem.
2. Podaj przykład zadania, które warto wrzucić do Celery.
3. Wskaż przypadek, w którym RabbitMQ pasuje lepiej niż Kafka.
4. Wskaż przypadek, w którym Kafka pasuje lepiej niż prosta kolejka zadań.
5. Wyjaśnij, dlaczego idempotencja jest ważna przy retry.

---

## Przykładowe rozwiązania

### 1. Producent i konsument

Producent wysyła wiadomość do systemu kolejkowego, a konsument ją odbiera i przetwarza.

### 2. Zadanie do Celery

Na przykład:

- wysyłka maila po rejestracji,
- generowanie PDF,
- przetworzenie zdjęcia po uploadzie.

### 3. RabbitMQ lepszy niż Kafka

Gdy potrzebujesz klasycznej kolejki tasków dla workerów i prostego routingu komunikatów.

### 4. Kafka lepsza niż prosta kolejka

Gdy wiele usług ma niezależnie reagować na strumień zdarzeń biznesowych w dużej skali.

### 5. Idempotencja

Bo przy ponowieniu to samo zadanie może zostać wykonane więcej niż raz, a system nie powinien przez to produkować błędnych skutków ubocznych.
