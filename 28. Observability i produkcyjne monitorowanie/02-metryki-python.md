# Metryki python

## O czym jest ten rozdział

Jeśli logi odpowiadają często na pytanie:

- co dokładnie się wydarzyło,

to metryki bardzo często odpowiadają na pytania:

- jak często to się dzieje,
- czy system jest zdrowy,
- czy robi się wolniej,
- czy liczba błędów rośnie,
- czy backlog kolejek nie wymyka się spod kontroli.

To właśnie czyni metryki tak ważnym filarem observability.

## Najprostsza intuicja

Metryka to liczbowy opis jakiegoś aspektu działania systemu.

Przykłady:

- liczba requestów,
- czas odpowiedzi,
- liczba błędów,
- liczba zadań w kolejce,
- zużycie pamięci,
- liczba aktywnych workerów.

Najprościej:

- log mówi o pojedynczym zdarzeniu,
- metryka pomaga zobaczyć wzorzec i trend.

## Po co metryki mają sens

Metryki pomagają, gdy chcesz:

- widzieć stan systemu w czasie,
- budować dashboardy,
- stawiać alerty,
- odróżniać incydent jednostkowy od rosnącego trendu,
- obserwować wydajność i obciążenie.

Bez metryk bardzo łatwo działać reaktywnie i punktowo.

## Najprostsze rodzaje pytań, na które odpowiadają metryki

### Pytania o ruch

- ile requestów na minutę ma system,
- jak rośnie lub spada ruch.

### Pytania o błędy

- ile jest błędów 500,
- czy odsetek błędów wzrósł po wdrożeniu.

### Pytania o czas

- czy endpoint zwolnił,
- ile trwa przetworzenie zadania.

### Pytania o backlog i zasoby

- ile wiadomości czeka w kolejce,
- czy workerzy nadążają,
- czy zużycie pamięci nie rośnie niepokojąco.

## Przykładowe metryki backendu webowego

Dla API bardzo często sensowne są metryki takie jak:

- liczba requestów,
- liczba odpowiedzi 2xx, 4xx, 5xx,
- czas odpowiedzi endpointów,
- liczba aktywnych requestów,
- liczba timeoutów,
- liczba błędów zależności zewnętrznych.

## Przykładowe metryki workera

Dla workera bardzo często sensowne są:

- liczba przetworzonych zadań,
- liczba błędnych zadań,
- liczba retry,
- czas wykonania zadania,
- liczba wiadomości oczekujących,
- wiek najstarszej wiadomości.

## Minimalny przykład myślowy

Wyobraź sobie metryki dla endpointu `/orders`.

Widzisz dashboard:

```text
requests_per_minute: 1200
error_rate: 0.2%
p95_latency_ms: 180
```

Potem po wdrożeniu:

```text
requests_per_minute: 1180
error_rate: 4.8%
p95_latency_ms: 950
```

Nawet bez czytania pojedynczych logów już widzisz, że coś poszło źle.

To właśnie potęga metryk.

## Metryki a logi

To bardzo ważne rozróżnienie.

### Logi

Dają szczegół kontekstu konkretnego zdarzenia.

### Metryki

Dają agregację i obraz trendu.

Nie chodzi o wybór jednego zamiast drugiego.

One odpowiadają na różne pytania.

## Metryki a alerty

Bardzo często alerty stoją właśnie na metrykach.

Przykłady:

- jeśli `error_rate` przekroczy próg,
- jeśli backlog kolejki rośnie zbyt długo,
- jeśli `p95 latency` rośnie powyżej akceptowalnego poziomu,
- jeśli workerzy nie przetwarzają zadań.

To dużo bardziej operacyjne niż ręczne patrzenie w logi co kilka godzin.

## Before/after

### Bez sensownych metryk

- problem zauważasz późno,
- trudno odróżnić incydent od trendu,
- alerty są słabsze albo ich nie ma.

### Z sensownymi metrykami

- szybciej widzisz zmianę stanu systemu,
- łatwiej budować alerty,
- łatwiej oceniać wpływ wdrożenia albo incydentu.

## Co mierzyć, a czego nie mierzyć obsesyjnie

To ważny temat.

Nie chodzi o to, żeby mierzyć wszystko, co się da.

Chodzi o to, żeby mierzyć to, co naprawdę pomaga ocenić:

- zdrowie systemu,
- doświadczenie użytkownika,
- wydajność krytycznych ścieżek,
- ryzyko operacyjne.

Zbyt wiele chaotycznych metryk daje tylko szum.

## Mini case study: wzrost 500 po deploymencie

Po wdrożeniu nowej wersji widzisz:

- wzrost `5xx`,
- wzrost czasu odpowiedzi,
- ten sam poziom ruchu.

To od razu daje bardzo mocny sygnał, że problem raczej nie wynika z nagłego wzrostu ruchu, tylko z jakości nowej wersji albo zależności.

Bez metryk mogłoby to wyjść dużo później.

## Mini case study: worker i kolejka

Masz system asynchroniczny.

Metryki pokazują:

- liczba zadań przychodzących: stabilna,
- czas zadania: rośnie,
- backlog kolejki: rośnie,
- wiek najstarszej wiadomości: rośnie.

To bardzo mocny sygnał, że workerzy nie nadążają albo coś spowalnia przetwarzanie.

## Częste pułapki

### 1. Metryki bez pytań biznesowo-operacyjnych

Jeśli nie wiesz, po co metryka istnieje, szybko robi się tylko szumem.

### 2. Alertowanie na wszystko

To prowadzi do alert fatigue.

### 3. Brak rozróżnienia między średnią a ogonem rozkładu

Średni czas odpowiedzi może wyglądać dobrze, a użytkownicy i tak cierpieć przez bardzo wolny ogon.

### 4. Brak metryk dla workerów i kolejek

Zespół widzi tylko web, a problem leży w asynchronicznym zapleczu.

### 5. Mierzenie bez interpretacji

Metryki są wartościowe tylko wtedy, gdy wiadomo, co ich zmiana oznacza.

## Co Pythonowiec powinien rozumieć

Dobrze, żebyś umiał:

- rozumieć, że metryki są o trendzie i stanie systemu, nie o szczególe jednego zdarzenia,
- dobrać kilka kluczowych metryk dla weba i workera,
- rozpoznawać, które metryki nadają się do alertowania,
- nie mylić średniej z pełnym obrazem wydajności,
- traktować metryki jako narzędzie decyzji operacyjnych.

## Output myślowy

### Bez metryk

- system żyje albo umiera trochę po cichu,
- problemy wychodzą później,
- trudniej ocenić wpływ zmian.

### Z sensownymi metrykami

- szybciej widzisz anomalie,
- łatwiej ustawić alerty,
- łatwiej odróżnić objaw od trendu.

## Najważniejsze do zapamiętania

- Metryki pomagają widzieć stan, trend i skalę problemu.
- Logi i metryki odpowiadają na różne pytania.
- Nie chodzi o mierzenie wszystkiego, tylko rzeczy ważnych.
- Web, worker i kolejka potrzebują często różnych metryk.
- Dobre metryki bardzo wspierają diagnostykę i alertowanie.

## Ćwiczenia

1. Wyjaśnij własnymi słowami różnicę między logiem i metryką.
2. Wypisz pięć sensownych metryk dla backendu API.
3. Wypisz pięć sensownych metryk dla workera i kolejki.
4. Opisz, czemu średni czas odpowiedzi nie zawsze wystarcza.
5. Rozpisz, jakie alerty zbudowałbyś na podstawie metryk systemu zamówień.
