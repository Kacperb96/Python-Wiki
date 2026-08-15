# Czytanie cudzego kodu w Pythonie

## O co chodzi

Czytanie cudzego kodu to osobna umiejętność.

I to bardzo ważna.

W prawdziwej pracy często nie dostajesz zadania:

- "napisz wszystko od zera".

Dużo częściej dostajesz:

- "zobacz, czemu to nie działa",
- "napraw to w istniejącym module",
- "zrozum, co robi ten fragment",
- "zrób zmianę bez rozwalenia reszty".

To wymaga zupełnie innego trybu pracy niż samo pisanie nowego kodu.

## Najczęstszy błąd początkujących

Próba czytania dużego repo od początku do końca, plik po pliku.

To bardzo często zły plan.

Duże repo trzeba czytać **celowo**, a nie linearnie.

## Najważniejsza zasada

Nie próbuj zrozumieć wszystkiego naraz.

Najpierw ustal:

- jaki masz problem,
- jaki fragment systemu jest z nim związany,
- gdzie jest punkt wejścia,
- jaki przepływ warto śledzić.

## Jak wejść w obcy kod sensownie

Bardzo praktyczna ścieżka wygląda tak:

1. zrozum objaw albo zadanie,
2. znajdź punkt wejścia,
3. znajdź główne przepływy,
4. dopiero potem schodź w szczegóły.

### Punkt wejścia może być np.:

- endpoint,
- komenda CLI,
- funkcja publiczna,
- job backgroundowy,
- test pokazujący problem,
- traceback.

To dużo lepsze niż losowe czytanie plików.

## Czytaj po przepływie, nie po katalogu

To bardzo ważne.

Zamiast myśleć:

- "przeczytam cały folder `services`",

lepiej myśleć:

- "śledzę, co dzieje się od requestu do zapisu do bazy",
- "śledzę, jak dane przepływają od wejścia do błędu",
- "śledzę, gdzie ten wyjątek może powstać".

To jest znacznie bardziej skuteczne.

## Pytania, które warto sobie zadawać

Gdy czytasz obcy kod, pytaj:

- co jest wejściem,
- co jest wyjściem,
- jaka jest odpowiedzialność tego modułu,
- jakie dane są przekazywane dalej,
- gdzie są zależności zewnętrzne,
- gdzie może siedzieć stan,
- gdzie może wystąpić efekt uboczny.

Te pytania bardzo pomagają nie zgubić się w kodzie.

## Szukaj kontraktów i granic

Duże repo łatwiej zrozumieć, gdy zauważysz:

- granice modułów,
- warstwy aplikacji,
- interfejsy publiczne,
- miejsca wejścia i wyjścia,
- logikę biznesową vs techniczną.

Nie musisz od razu znać każdej funkcji. Wystarczy najpierw rozpoznać mapę systemu.

## Nie wszystko w kodzie jest równie ważne

To bardzo ważna umiejętność.

W dużym repo część kodu jest:

- centralna,
- często używana,
- ważna dla przepływu.

Inna część jest:

- pomocnicza,
- wtórna,
- mniej istotna dla bieżącego problemu.

Jeśli próbujesz na start poświęcić tyle samo uwagi wszystkiemu, szybko się zmęczysz i zgubisz kontekst.

## Mini strategia na pierwszy kontakt z modułem

Jeśli trafiasz na nowy plik, dobrze zacząć od pytań:

- jaki jest jego główny cel,
- co eksportuje,
- kto go wywołuje,
- jakie są najważniejsze funkcje,
- czy ten plik robi za dużo.

To zwykle daje lepszy start niż czytanie każdej linijki od góry do dołu z jednakową uwagą.

## Gdy kod jest brzydki albo chaotyczny

To normalne. W prawdziwej pracy często dostajesz kod, który:

- nie jest idealnie nazwany,
- nie ma świetnej struktury,
- ma długi przepływ,
- miesza odpowiedzialności.

Wtedy tym bardziej potrzebujesz czytać go po:

- objawie,
- przepływie,
- punktach decyzji,
- danych.

A nie po nadziei, że cały kod nagle stanie się oczywisty.

## Mini case study

Masz błąd w endpointcie tworzenia zamówienia.

Zły plan:

- przeczytam całe repo od początku.

Lepszy plan:

1. znaleźć endpoint,
2. zobaczyć, jaki serwis wywołuje,
3. zobaczyć, jakie dane trafiają do serwisu,
4. sprawdzić zapis do bazy,
5. znaleźć miejsce błędu albo niezgodności.

To jest czytanie po przepływie problemu.

## Typowe błędy początkujących

- czytanie wszystkiego naraz,
- brak pytań kierunkowych,
- gubienie się w detalach bez rozumienia całości,
- ignorowanie punktu wejścia,
- próba pełnego zrozumienia całego repo przed pierwszym małym krokiem.

## Szybka ściąga

- nie czytaj dużego repo linearnie,
- zaczynaj od problemu i punktu wejścia,
- śledź przepływ danych i decyzji,
- szukaj granic modułów i odpowiedzialności,
- nie wszystko w kodzie jest równie ważne dla bieżącego zadania.

## Ćwiczenia

1. Weź mały moduł i wskaż jego punkt wejścia.
2. Rozpisz przepływ od wejścia do wyjścia dla jednej funkcji.
3. Znajdź 3 pytania, które pomogłyby Ci zrozumieć obcy plik.
4. Opisz, jak wszedłbyś w większe repo bez czytania wszystkiego.
5. Weź bug i rozpisz, które pliki czytałbyś najpierw.

## Najważniejsze do zapamiętania

- Czytanie cudzego kodu to umiejętność kierunkowa, nie liniowa.
- Najpierw rozumiesz problem i punkt wejścia, dopiero potem detale.
- Dobre pytania są ważniejsze niż chaotyczne czytanie wszystkiego.
- W dużym repo trzeba śledzić przepływ, nie katalogi.
- Nie musisz rozumieć całego systemu, żeby zrobić pierwszy sensowny krok.
