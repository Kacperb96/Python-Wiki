# Kolejki i brokery python

## O czym jest ten rozdział

To jest punkt wejścia do całego świata messagingu.

Na początku aplikacja zwykle robi wszystko od razu:

- użytkownik wysyła request,
- backend zapisuje dane,
- wysyła maila,
- generuje raport,
- liczy PDF,
- odpala integrację,
- zwraca odpowiedź.

Dopóki system jest mały, to bywa akceptowalne.

Potem pojawiają się problemy:

- request trwa zbyt długo,
- jedna awaria zewnętrznej usługi psuje cały flow,
- ciężkie zadania blokują użytkownika,
- aplikacja potrzebuje rozdzielić producenta pracy od wykonawcy.

Wtedy wchodzą kolejki i brokery.

## Najprostsza intuicja kolejki

Kolejka to miejsce, do którego wrzucasz zadanie albo wiadomość, żeby ktoś inny mógł je odebrać i przetworzyć później.

Najprostsza intuicja:

- producer mówi: "mam pracę do wykonania",
- worker albo consumer mówi: "odbiorę to i zrobię".

To od razu rozdziela moment zgłoszenia pracy od momentu jej wykonania.

## Najprostsza intuicja brokera

Broker to pośrednik, który przechowuje i przekazuje wiadomości między nadawcami i odbiorcami.

Czyli bardzo uproszczając:

- producer nie musi znać bezpośrednio workera,
- worker nie musi być uruchomiony w tej samej chwili co producer,
- broker trzyma i dystrybuuje wiadomości według określonych zasad.

## Producer, consumer, worker

To trzy pojęcia, które trzeba rozumieć od razu.

### Producer

Producer wysyła wiadomość lub zadanie.

Przykład:

- backend po złożeniu zamówienia publikuje zadanie wysłania maila.

### Consumer

Consumer odbiera wiadomość i ją obsługuje.

### Worker

Worker to proces wykonujący zadania w tle.

W wielu systemach worker jest praktycznym rodzajem consumera.

## Przykład intuicyjny

Masz endpoint:

```text
POST /orders
```

Po udanym złożeniu zamówienia trzeba:

- zapisać zamówienie,
- wysłać maila,
- zaktualizować CRM,
- wygenerować PDF,
- wysłać event do innej usługi.

### Wersja synchroniczna

Użytkownik czeka, aż wszystko wykona się od razu.

Problemy:

- request trwa długo,
- awaria maila może wywalić całe zamówienie,
- system jest bardziej kruchy.

### Wersja z kolejką

Backend:

1. zapisuje zamówienie,
2. wrzuca zadanie `send_order_email`,
3. zwraca odpowiedź.

Worker:

- odbiera zadanie,
- wysyła maila później.

To bardzo klasyczny wzorzec.

## Minimalna symulacja w Pythonie

```python
queue = []


def publish(task_name: str, payload: dict):
    queue.append({"task": task_name, "payload": payload})


def consume_one():
    if not queue:
        return None
    return queue.pop(0)


publish("send_email", {"order_id": 123})
publish("generate_pdf", {"order_id": 123})

print(queue)
print(consume_one())
print(consume_one())
print(consume_one())
```

Output:

```text
[{'task': 'send_email', 'payload': {'order_id': 123}}, {'task': 'generate_pdf', 'payload': {'order_id': 123}}]
{'task': 'send_email', 'payload': {'order_id': 123}}
{'task': 'generate_pdf', 'payload': {'order_id': 123}}
None
```

To tylko intuicja, ale bardzo dobrze pokazuje ideę oddzielenia publikacji od wykonania.

## Co daje kolejka w praktyce

Kolejka pomaga, gdy chcesz:

- skrócić czas odpowiedzi API,
- przenieść ciężką pracę do tła,
- rozdzielić komponenty systemu,
- przetwarzać zadania niezależnie od requestu użytkownika,
- buforować chwilowy wzrost ruchu.

## Ale kolejka nie jest darmowa

To bardzo ważne.

Dodanie kolejki daje korzyści, ale zwiększa też złożoność:

- pojawia się opóźnienie,
- pojawiają się retry i błędy przetwarzania,
- trzeba myśleć o idempotencji,
- trudniej śledzić cały flow,
- system staje się bardziej rozproszony.

Czyli znowu mamy trade-off.

## Kolejka a synchroniczność

Nie wszystko warto wrzucać do kolejki.

Jeśli użytkownik musi dostać wynik natychmiast i bezpośrednio zależy od niego dalsza interakcja, zadanie może nadal wymagać synchronicznego wykonania.

Kolejki są dobre zwłaszcza tam, gdzie:

- wynik może przyjść później,
- praca nie musi blokować użytkownika,
- awaria niekrytycznej części nie powinna psuć głównej operacji.

## At-least-once: bardzo ważna intuicja

W systemach messagingowych trzeba często myśleć tak:

- wiadomość może zostać dostarczona co najmniej raz,
- czyli czasem może dojść więcej niż raz.

To jedna z najważniejszych rzeczy do zrozumienia.

Jeśli consumer nie jest przygotowany na dubel, system zaczyna robić podwójne akcje.

## Before/after

### Słabszy model

- ciężka logika dzieje się w request-response,
- awaria integracji zewnętrznej blokuje użytkownika,
- backend robi za dużo na raz.

### Lepszy model

- część pracy przenosisz do tła,
- producer i worker są rozdzieleni,
- użytkownik szybciej dostaje odpowiedź,
- system lepiej znosi chwilowe skoki pracy.

## Mini case study: wysyłka maila po zamówieniu

Masz flow:

- klient składa zamówienie,
- system powinien wysłać potwierdzenie mailowe.

### Słabszy wariant

Backend od razu synchronnie łączy się z usługą mailową.

Ryzyko:

- wolny provider maili spowalnia endpoint,
- timeout psuje doświadczenie użytkownika,
- chwilowa awaria maila wpływa na zamówienie.

### Lepszy wariant

Backend zapisuje zamówienie i publikuje zadanie `send_confirmation_email`.

Zaleta:

- zamówienie może zakończyć się szybciej,
- mail jest przetwarzany osobno,
- system lepiej izoluje awarie.

## Co Pythonowiec powinien rozumieć

Dobrze, żebyś umiał:

- rozpoznać, które zadania nadają się do tła,
- rozumieć różnicę między producerem i consumerem,
- wiedzieć, że broker to pośrednik, a nie magiczna skrzynka rozwiązująca wszystko,
- przewidzieć, że wiadomość może nie wykonać się natychmiast,
- myśleć o błędach i dubelkach już na etapie projektu.

## Output myślowy

### Bez kolejki

- system jest prostszy,
- ale bardziej blokujący i mniej odporny na ciężkie zadania.

### Z kolejką

- system jest bardziej elastyczny,
- ale bardziej złożony,
- trzeba myśleć o niezawodności, opóźnieniu i powtórzeniach.

## Najważniejsze do zapamiętania

- Kolejka rozdziela moment zgłoszenia pracy od momentu jej wykonania.
- Broker pośredniczy między nadawcą i odbiorcą wiadomości.
- Producer wysyła, consumer odbiera, worker wykonuje.
- Kolejki pomagają skracać request-response i przenosić ciężką pracę do tła.
- Messaging zwiększa elastyczność, ale też złożoność systemu.

## Ćwiczenia

1. Wyjaśnij własnymi słowami różnicę między producerem, consumerem i brokerem.
2. Podaj trzy przykłady zadań, które sensownie wrzuciłbyś do kolejki.
3. Opisz sytuację, w której zadanie nie powinno być przeniesione do tła.
4. Wytłumacz, czemu kolejka nie jest darmowym przyspieszeniem wszystkiego.
5. Rozpisz flow zamówienia z wykorzystaniem brokera i workera.
