# Tracing python

## O czym jest ten rozdział

Logi pomagają zrozumieć pojedyncze zdarzenia.
Metryki pomagają zobaczyć stan i trend systemu.

Ale gdy system ma wiele kroków i zależności, bardzo szybko pojawia się pytanie:

- jak prześledzić jeden konkretny request albo jedną operację przez cały łańcuch usług?

To właśnie miejsce, gdzie wchodzi tracing.

## Najprostsza intuicja

Tracing pozwala śledzić jeden przepływ pracy przez wiele etapów systemu.

Najprościej:

- request wchodzi do API,
- API woła bazę,
- publikuje task,
- worker robi dalsze kroki,
- zewnętrzne API odpowiada,
- a Ty chcesz zobaczyć tę całość jako jeden powiązany przebieg.

To jest intuicja trace'a.

## Trace i span: najprostsza intuicja

Dwa pojęcia są tu kluczowe.

### Trace

Trace to cały przebieg jednej operacji lub requestu przez system.

### Span

Span to pojedynczy etap tego przebiegu.

Przykład:

- trace = "obsługa utworzenia zamówienia",
- spany =
  - walidacja requestu,
  - zapis do bazy,
  - publikacja eventu,
  - wywołanie workera,
  - wywołanie zewnętrznego CRM.

## Po co tracing ma sens

Tracing pomaga, gdy chcesz:

- znaleźć, który etap requestu jest wolny,
- zobaczyć zależności między usługami,
- powiązać błędy z konkretną ścieżką wykonania,
- zrozumieć, gdzie ginie czas albo gdzie pęka przepływ,
- diagnozować systemy rozproszone, gdzie jeden request uruchamia kilka komponentów.

## Dlaczego logi nie zawsze wystarczą

Nawet przy dobrym `request_id` logi w systemie rozproszonym mogą być trudne do ręcznego składania.

Masz wtedy:

- logi z weba,
- logi z workera,
- logi z bazy lub brokera,
- logi z integracji.

Tracing daje bardziej uporządkowany obraz ścieżki wykonania.

## Minimalna intuicja czasowa

Wyobraź sobie taki request:

- 20 ms walidacja,
- 80 ms zapis do bazy,
- 15 ms publikacja eventu,
- 900 ms odpowiedź z zewnętrznego API.

Bez tracingu możesz widzieć tylko:

- "request był wolny".

Z tracingiem widzisz:

- który dokładnie etap zjadł czas.

To ogromna różnica praktyczna.

## Przykład myślowy

Masz endpoint:

```text
POST /orders
```

Trace może wyglądać tak:

```text
trace: create_order
  span: validate_request (12 ms)
  span: save_order_to_db (45 ms)
  span: publish_order_event (8 ms)
  span: send_to_crm (740 ms)
```

Najważniejsza intuicja:

- od razu widać, gdzie system zwolnił.

## Tracing a systemy rozproszone

Tracing jest szczególnie cenny wtedy, gdy jedna akcja użytkownika przechodzi przez:

- API,
- worker,
- kolejkę,
- zewnętrzny serwis,
- bazę.

To właśnie tam ręczne składanie historii staje się trudne i kosztowne.

## Before/after

### Bez tracingu

- wiesz, że coś było wolne,
- ale trudniej zobaczyć pełną ścieżkę,
- logi trzeba składać ręcznie.

### Z tracingiem

- widzisz cały przebieg jednej operacji,
- łatwiej znaleźć wąskie gardło,
- łatwiej zrozumieć zależności i błędy w rozproszeniu.

## Tracing a request_id

To bardzo ważna relacja.

`request_id` w logach i trace mogą się wzajemnie wzmacniać.

Najprościej:

- logi dają szczegół kontekstowy,
- trace daje strukturę przepływu.

Nie chodzi o wybór jednego zamiast drugiego.

## Mini case study: wolne tworzenie zamówienia

Objaw:

- użytkownik mówi, że tworzenie zamówienia jest wolne.

Metryki pokazują:

- wzrost czasu odpowiedzi.

Logi pokazują:

- request doszedł i się zakończył.

Tracing pokazuje:

- problem nie jest w bazie,
- problem leży w wywołaniu zewnętrznego CRM, które zajmuje 900 ms.

To jest bardzo konkretna wartość tracingu.

## Mini case study: request przechodzi przez workera

Masz flow:

- API przyjmuje zgłoszenie,
- worker generuje dokument,
- potem inna usługa wysyła mail.

Trudno to zrozumieć tylko po pojedynczych logach.

Tracing pomaga zbudować historię:

- co wywołało co,
- ile trwał każdy krok,
- gdzie pojawiło się opóźnienie lub błąd.

## Częste pułapki

### 1. Próba zastąpienia tracingiem wszystkiego

Tracing nie zastępuje logów i metryk.

To osobny filar observability.

### 2. Brak sensownego kontekstu między usługami

Jeśli kontekst trace nie przechodzi dalej, ścieżka się urywa.

### 3. Tracing zbyt drobiazgowy

Jeśli każdy mikrokrok jest spanem bez sensu, narzędzie i analiza stają się ciężkie.

### 4. Tracing tylko w jednej usłudze

W systemie rozproszonym największa wartość pojawia się przy przechodzeniu przez granice komponentów.

### 5. Brak połączenia tracingu z logami i błędami

Wtedy trace istnieje, ale nie daje pełnego obrazu incydentu.

## Co Pythonowiec powinien rozumieć

Dobrze, żebyś umiał:

- rozumieć różnicę między trace i spanem,
- wiedzieć, że tracing służy do śledzenia przepływu, a nie tylko pojedynczego logu,
- rozpoznawać, kiedy trace daje większą wartość niż same logi,
- myśleć o powiązaniu trace'ów z requestami, workerami i integracjami,
- nie traktować tracingu jako zamiennika całej observability.

## Output myślowy

### Bez tracingu

- system rozproszony jest trudniejszy do zrozumienia,
- czas i błędy trzeba składać z wielu miejsc ręcznie.

### Z tracingiem

- widać ścieżkę jednej operacji,
- łatwiej znaleźć wąskie gardła,
- łatwiej zrozumieć opóźnienia między usługami.

## Najważniejsze do zapamiętania

- Trace opisuje cały przebieg jednej operacji, span opisuje jego pojedynczy etap.
- Tracing jest szczególnie cenny w systemach rozproszonych.
- Pomaga znaleźć, gdzie naprawdę znika czas albo gdzie psuje się przepływ.
- Nie zastępuje logów ani metryk.
- Największą wartość daje wtedy, gdy łączy kilka komponentów jednego flow.

## Ćwiczenia

1. Wyjaśnij własnymi słowami różnicę między trace i spanem.
2. Opisz, kiedy tracing daje przewagę nad samymi logami.
3. Rozpisz przykładowy trace dla flow tworzenia zamówienia z workerem.
4. Wskaż trzy pułapki źle wdrożonego tracingu.
5. Opisz, jak połączyłbyś `request_id`, logi i trace w jednym systemie.
