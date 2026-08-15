# 20. Performance i optymalizacja

To jest folder o tym, jak przyspieszać kod z głową.

Nie chodzi tu o popisywanie się mikrooptymalizacjami ani o obsesję na punkcie każdej milisekundy. Chodzi o znacznie ważniejszą rzecz:

- umieć rozpoznać prawdziwy problem wydajnościowy,
- umieć go zmierzyć,
- umieć znaleźć wąskie gardło,
- umieć wybrać poprawkę, która daje realny efekt,
- i nie psuć czytelności kodu bez dobrego powodu.

To bardzo ważny dział, bo performance bez pomiaru bardzo łatwo zamienia się w zgadywanie.

## Po co ten folder

W pewnym momencie pracy z Pythonem zaczynasz trafiać na pytania takie jak:

- czemu ten fragment działa wolno,
- czy problem jest w algorytmie czy w I/O,
- czy warto użyć wątków, procesów albo async,
- czy problemem jest CPU czy pamięć,
- jak nie trzymać wszystkiego naraz w RAM,
- jak porównać dwa rozwiązania uczciwie,
- kiedy optymalizacja ma sens, a kiedy tylko komplikuje kod.

Ten folder ma nauczyć Cię właśnie takiego dojrzałego myślenia o wydajności.

## Czego nauczysz się w tym dziale

Po przerobieniu tego modułu powinieneś rozumieć:

- jak benchmarkować kod bez oszukiwania się,
- czym różni się CPU-bound od I/O-bound,
- jak profilować kod i szukać wąskich gardeł,
- dlaczego algorytm i struktura danych często dają większy zysk niż mikrosztuczki,
- jak działa streaming danych i czemu bywa ważny,
- jak myśleć o pamięci,
- kiedy optymalizować, a kiedy lepiej odpuścić.

## Najważniejsza zasada tego folderu

Najpierw mierz. Potem optymalizuj.

To jest absolutnie kluczowe.

Bardzo wiele błędów performance bierze się z tego, że ktoś:

- zakłada, gdzie jest problem,
- poprawia zły fragment,
- komplikuje kod,
- a prawdziwe wąskie gardło zostaje nietknięte.

## Jak czytać ten folder

Najlepiej iść po kolei:

1. `01-benchmarking-python.md`
2. `02-cpu-bound-vs-io-bound-python.md`
3. `03-profilowanie-zaawansowane-python.md`
4. `04-algorytmy-i-struktury-danych-w-praktyce-python.md`
5. `05-streaming-danych-python.md`
6. `06-optymalizacja-pamieci-python.md`
7. `07-kiedy-optymalizowac-python.md`

Ta kolejność ma sens, bo najpierw uczysz się mierzyć i klasyfikować problem, potem szukać źródła kosztu, a dopiero później wybierać sensowne techniki poprawy.

## Na co szczególnie uważać

W performance bardzo łatwo wpaść w trzy pułapki.

### 1. Przedwczesna optymalizacja

Kod jest jeszcze mały, problemu nie zmierzono, a ktoś już komplikuje architekturę.

### 2. Mikrooptymalizacje bez znaczenia

Zmiana jednego drobiazgu nic nie da, jeśli główny problem siedzi w złym algorytmie albo ciężkim I/O.

### 3. Mylne benchmarki

Jeśli źle mierzysz, możesz dojść do fałszywych wniosków.

## Po czym poznasz, że temat siedzi

Dobry znak, jeśli potrafisz:

- porównać dwa rozwiązania uczciwym benchmarkiem,
- rozpoznać, czy problem jest CPU-bound czy I/O-bound,
- znaleźć hot spot przez profilowanie,
- wskazać, kiedy problemem jest algorytm, a kiedy pamięć,
- wyjaśnić, czemu generator albo streaming może pomóc,
- powiedzieć, kiedy lepiej nie optymalizować.

## Jak najlepiej ćwiczyć

Najlepiej brać małe, konkretne przypadki:

- dwa sposoby filtrowania danych,
- dwa sposoby liczenia,
- listę vs generator,
- pełne wczytanie pliku vs iteracja po liniach,
- złą i lepszą strukturę danych.

Potem:

1. mierz,
2. porównuj,
3. zapisuj wnioski,
4. sprawdzaj, czy zysk jest realny i czytelność kodu nadal jest dobra.

## Podsumowanie

To jest folder o świadomym performance. Nie o magii, nie o sprytnych trikach, tylko o porządnym inżynierskim podejściu: zmierzyć, zrozumieć, poprawić to, co naprawdę boli.
