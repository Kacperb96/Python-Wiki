# Zestaw ćwiczeń praktycznych — 25. Messaging i systemy rozproszone

Te ćwiczenia mają pomóc Ci przejść od samych pojęć do projektowania sensownego, odpornego systemu opartego o wiadomości i zadania asynchroniczne.

## Poziom 1

1. Wyjaśnij własnymi słowami różnicę między producerem, consumerem, workerem i brokerem.
2. Podaj trzy przykłady zadań, które sensownie wrzuciłbyś do kolejki.
3. Wytłumacz, czemu retry bez idempotencji jest groźne.
4. Opisz, czym jest eventual consistency bez używania podręcznikowej definicji.
5. Wyjaśnij intuicyjnie różnicę między RabbitMQ i Kafką.

## Poziom 2

1. Rozpisz flow zamówienia, w którym mail jest wysyłany asynchronicznie przez workera.
2. Zaprojektuj prosty mechanizm idempotency key dla naliczania punktów lojalnościowych.
3. Opisz sytuację, w której wiadomość może zostać dostarczona więcej niż raz.
4. Wyjaśnij, po co w RabbitMQ istnieją `exchange`, `queue` i `ack`.
5. Rozpisz przykład eventu `order.created`, który czytają trzy niezależne systemy.

## Poziom 3

1. Porównaj, kiedy wolałbyś:
   - zwykły synchroniczny request,
   - Celery z brokerem,
   - RabbitMQ jako broker kolejki pracy,
   - Kafkę jako strumień zdarzeń.
2. Opisz, które operacje biznesowe w systemie płatności są szczególnie niebezpieczne bez idempotencji.
3. Zaprojektuj prosty outbox pattern dla tworzenia zamówienia.
4. Opisz, jakie opóźnienia i stany przejściowe są akceptowalne w systemie event-driven.
5. Wypisz, jakie metryki i logi chciałbyś widzieć dla systemu workerów i kolejek.

## Zadania praktyczne z kodem

1. Zaimplementuj prostą kolejkę w Pythonie jako listę i funkcje `publish()` oraz `consume_one()`.
2. Napisz prosty przykład deduplikacji operacji na podstawie `operation_id`.
3. Zrób minimalną symulację eventual consistency na dwóch etapach procesu.
4. Napisz prosty model outboxa jako listy rekordów oczekujących na publikację.
5. Zaimplementuj prostą funkcję retry z ograniczoną liczbą prób dla operacji, która czasem rzuca wyjątek.

## Większe zadania projektowe

1. Zaprojektuj moduł `orders`, który po utworzeniu zamówienia:
   - zapisuje rekord,
   - publikuje event,
   - wysyła mail,
   - aktualizuje CRM,
   - nie blokuje użytkownika długim requestem.
2. Opisz, które elementy tego flow powinny być synchroniczne, a które asynchroniczne.
3. Zaprojektuj strategię retry i idempotencji dla:
   - wysyłki maila,
   - naliczania punktów,
   - aktualizacji CRM.
4. Rozpisz, czy bardziej pasuje tu RabbitMQ, Kafka czy Celery na brokerze i dlaczego.
5. Opisz, gdzie w tym flow zastosowałbyś outbox pattern.

## Zadanie końcowe

Wyobraź sobie, że budujesz backend sklepu internetowego z osobnymi workerami.

Odpowiedz pisemnie:

1. Które operacje zostawiłbyś synchronicznie?
2. Które operacje przeniósłbyś do kolejki?
3. Gdzie w systemie grożą duble?
4. Jak zabezpieczyłbyś najbardziej wrażliwe operacje przed skutkami retry?
5. Czy potrzebujesz RabbitMQ, Kafki, Celery czy kombinacji tych narzędzi?
6. Gdzie występuje eventual consistency i czy to jest akceptowalne?
7. Jak rozwiązałbyś problem spójności między bazą a publikacją eventu?

## Zadanie debuggingowe

Masz objaw:

- użytkownik czasem dostaje dwa maile,
- punkty lojalnościowe czasem naliczają się podwójnie,
- CRM bywa aktualizowany z opóźnieniem,
- część eventów znika po chwilowej awarii brokera.

Odpowiedz krok po kroku:

1. Jakie są pierwsze hipotezy?
2. Gdzie najbardziej podejrzewasz brak idempotencji?
3. Czy problem może dotyczyć `ack`, retry albo publishowania eventów poza bezpiecznym flow?
4. Jakie logi i metryki sprawdziłbyś najpierw?
5. Jakie poprawki wdrażałbyś w pierwszej kolejności?

## Zadanie przekrojowe

Na podstawie pliku `08-case-study-orders-event-driven-python.md` zaprojektuj własną wersję modułu `orders` i odpowiedz:

1. Które skutki uboczne zostawiłbyś poza requestem?
2. Gdzie wstawiłbyś outbox pattern?
3. Które consumerzy muszą być najbardziej idempotentni?
4. Jak zmierzyłbyś lag kolejki i opóźnienie eventów?
5. Jakie dwa testy integracyjne byłyby najważniejsze dla tego modułu?
6. Jakie dwa błędy produkcyjne przewidujesz jako najbardziej prawdopodobne?
7. Jak wyglądałaby Twoja checklista debugowania "zamówienie jest, ale dalsze skutki nie zaszły"?

## Najważniejszy cel tych ćwiczeń

Po zrobieniu tego zestawu powinieneś nie tylko znać słowa typu `broker`, `retry`, `idempotencja`, `eventual consistency`, `Kafka` czy `outbox pattern`, ale rozumieć:

- po co istnieją,
- jakie problemy rozwiązują,
- jakie mają koszty,
- kiedy naprawdę warto ich użyć,
- jak składają się w jeden odporny system rozproszony,
- jak diagnozować go wtedy, gdy rzeczy nie dzieją się od razu albo dzieją się więcej niż raz.
