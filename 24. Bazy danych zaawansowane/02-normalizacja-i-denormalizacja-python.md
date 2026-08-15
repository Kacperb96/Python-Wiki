# Normalizacja i denormalizacja python

## O czym jest ten rozdział

Ten temat dotyczy projektowania modelu danych.

To jedna z tych rzeczy, które na początku wydają się proste:

- rozbij dane na tabele,
- połącz kluczami,
- gotowe.

W praktyce bardzo szybko pojawiają się pytania:

- jak mocno rozdzielać dane,
- kiedy osobna tabela ma sens,
- kiedy joinów robi się za dużo,
- kiedy wolno świadomie duplikować dane,
- jak nie wpaść w chaos.

Tu właśnie wchodzą normalizacja i denormalizacja.

## Najprostsza intuicja normalizacji

Normalizacja to porządkowanie danych tak, żeby:

- zmniejszać duplikację,
- ograniczać niespójności,
- rozdzielać różne byty do sensownych tabel,
- aktualizować informację w jednym miejscu zamiast w wielu.

Najprostsza intuicja:

- jedna informacja powinna mieć możliwie jedno źródło prawdy.

## Przykład złego modelu na start

Wyobraź sobie tabelę `orders`:

```text
order_id | customer_name | customer_email | customer_city | product_name | product_price
```

Jeśli jeden klient złoży 100 zamówień, to jego dane są powielane 100 razy.

Problemy:

- większa duplikacja,
- ryzyko niespójności,
- trudniejsze aktualizacje,
- większa szansa na błędy.

## Lepszy model z normalizacją

Dzielisz dane np. na:

- `customers`,
- `orders`,
- `products`,
- `order_items`.

Wtedy:

- klient jest zapisany raz,
- produkt jest zapisany raz,
- zamówienie łączy się relacjami,
- dane są bardziej spójne.

## Zalety normalizacji

- mniej duplikacji,
- mniejsze ryzyko niespójności,
- łatwiejsze aktualizacje,
- bardziej czytelny model domeny,
- lepsza kontrola nad relacjami między danymi.

## Koszt normalizacji

Normalizacja też nie jest darmowa.

Często oznacza:

- więcej tabel,
- więcej joinów,
- bardziej złożone query,
- czasem większy koszt odczytu.

Czyli znowu mamy trade-off.

## Denormalizacja: najprostsza intuicja

Denormalizacja to świadome dodanie pewnej duplikacji albo uproszczenia modelu po to, żeby poprawić:

- wydajność odczytu,
- prostotę najczęstszych query,
- szybkość budowania widoków albo raportów.

To ważne słowo: świadome.

Denormalizacja nie oznacza bałaganu. Oznacza celowe odejście od czystości modelu dla konkretnej korzyści.

## Przykład praktyczny denormalizacji

Masz `orders` i `customers`.

Na liście zamówień bardzo często pokazujesz:

- nazwę klienta,
- email klienta,
- miasto klienta.

Jeśli to bardzo gorąca ścieżka odczytu, czasem zespół decyduje się przechowywać część tych danych również przy zamówieniu.

Wtedy odczyt bywa prostszy i szybszy, ale pojawia się koszt utrzymania spójności.

## Before/after

### Bardziej znormalizowany model

- mniej duplikacji,
- lepsza spójność,
- częściej potrzebne joiny.

### Bardziej zdenormalizowany model

- szybszy lub prostszy odczyt w wybranych scenariuszach,
- więcej duplikowanych danych,
- większa odpowiedzialność za spójność.

## Kiedy normalizacja zwykle ma sens

Normalizacja jest zwykle dobrym punktem startowym, gdy:

- projekt dopiero powstaje,
- chcesz utrzymać porządek w modelu,
- dane często się zmieniają,
- spójność jest bardzo ważna,
- nie masz jeszcze dowodów, że odczyt jest problemem.

To dlatego wiele systemów zaczyna od dość normalnego modelu relacyjnego.

## Kiedy denormalizacja ma sens

Denormalizacja ma sens częściej wtedy, gdy:

- masz już realne obciążenie,
- znasz najczęstsze query,
- wiesz, że joiny albo agregacje robią się drogie,
- chcesz zoptymalizować hot path,
- potrafisz świadomie utrzymać spójność.

## Najczęstsze pułapki

### 1. Denormalizacja za wcześnie

To częsty błąd.

Jeśli nie masz jeszcze danych o realnym użyciu, możesz skomplikować model bez zysku.

### 2. Zbyt idealistyczna normalizacja

Czasem model jest tak "czysty", że codzienna praca z nim staje się ciężka, a najważniejsze query są niepotrzebnie drogie.

### 3. Brak źródła prawdy po denormalizacji

Jeśli duplikujesz dane, musisz wiedzieć:

- które miejsce jest kanoniczne,
- co aktualizuje kopie,
- kiedy mogą się rozjechać.

### 4. Mieszanie danych operacyjnych i raportowych bez planu

Czasem system zaczyna dorzucać kolejne pola tylko po to, żeby raport działał szybciej.

Bez jasnej strategii robi się z tego chaos.

## Mini case study

Masz system zamówień.

Na dashboardzie support bardzo często potrzebuje listy:

- numer zamówienia,
- status,
- nazwa klienta,
- email klienta,
- ostatnia data aktualizacji.

### Wersja znormalizowana

Query wymaga joinu `orders` + `customers`.

### Wersja częściowo zdenormalizowana

W tabeli `orders` trzymasz także `customer_name_snapshot` i `customer_email_snapshot`.

Zaleta:

- odczyt listy jest prostszy.

Koszt:

- dane klienta przy zamówieniu są snapshotem, nie zawsze aktualnym profilem.

I to może być całkowicie poprawne biznesowo, jeśli właśnie taki jest cel.

## Snapshot danych: bardzo ważna intuicja

Czasem duplikacja nie jest błędem, tylko świadomym utrwaleniem stanu historycznego.

Przykład:

- chcesz wiedzieć, jaki adres dostawy był w momencie zakupu,
- a nie jaki adres klient ma dzisiaj.

Wtedy snapshot jest sensowny i wręcz pożądany.

## Co Pythonowiec powinien rozumieć

Nie musisz od razu projektować złożonych schematów jak architekt danych.

Ale dobrze, żebyś umiał:

- rozpoznać duplikację problematyczną,
- rozpoznać duplikację celową,
- zapytać, gdzie jest źródło prawdy,
- ocenić, czy dany odczyt jest hot pathem,
- odróżnić potrzeby operacyjne od raportowych.

## Output myślowy

### Zbyt znormalizowany system

- model jest bardzo czysty,
- ale odczyt kluczowych ekranów staje się ciężki,
- rośnie liczba joinów i koszt query.

### Zbyt zdenormalizowany system

- początkowo czyta się wygodnie,
- po czasie dane zaczynają się rozjeżdżać,
- trudno ustalić, która wartość jest prawdziwa.

### Dojrzały kompromis

- model jest głównie uporządkowany,
- denormalizacja pojawia się tam, gdzie są ku temu dowody i sens biznesowy.

## Najważniejsze do zapamiętania

- Normalizacja ogranicza duplikację i poprawia spójność.
- Denormalizacja może poprawić wydajność odczytu i uprościć hot path.
- Denormalizacja ma sens wtedy, gdy jest świadoma i kontrolowana.
- Nie każda duplikacja jest błędem, czasem jest snapshotem historycznym.
- Najlepszy model to zwykle kompromis, a nie skrajność.

## Ćwiczenia

1. Wyjaśnij własnymi słowami, po co istnieje normalizacja.
2. Podaj przykład sytuacji, w której denormalizacja ma sens biznesowy.
3. Opisz ryzyko wynikające z duplikowania danych bez jasnego źródła prawdy.
4. Wymyśl przykład snapshotu, który powinien być zachowany historycznie.
5. Weź prosty moduł `orders` i zaproponuj, które dane trzymałbyś osobno, a które ewentualnie zduplikował.
