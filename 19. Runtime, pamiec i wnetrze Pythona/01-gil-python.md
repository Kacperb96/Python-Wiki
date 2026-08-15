# GIL w Pythonie

## O co chodzi

GIL to skrót od Global Interpreter Lock.

To jeden z najbardziej znanych tematów wokół Pythona, ale też jeden z najbardziej źle rozumianych.

Wokół GIL narosło mnóstwo uproszczeń typu:

- "Python nie ma prawdziwych wątków",
- "Python nie nadaje się do współbieżności",
- "GIL zawsze zabija wydajność".

To wszystko jest zbyt uproszczone.

## Najprostsza intuicja

W klasycznym CPythonie GIL oznacza, że w danym momencie tylko jeden wątek wykonuje kod Pythona wewnątrz interpretera.

To ważne głównie dla zadań:

- CPU-bound,
- wielowątkowych,
- wykonywanych w CPythonie.

## Dlaczego GIL w ogóle istnieje

W uproszczeniu: pomaga uprościć zarządzanie pamięcią i współdzielonym stanem interpretera.

Nie został wymyślony po to, żeby utrudniać życie programistom, tylko jako element modelu działania interpretera.

To historyczna i praktyczna decyzja projektowa, która daje pewne korzyści, ale ma też koszty.

## Gdzie GIL najbardziej boli

Najbardziej przy zadaniach CPU-bound wykonywanych w wielu wątkach.

CPU-bound to zadania, gdzie głównym kosztem jest liczenie, np.:

- ciężkie obliczenia,
- analiza dużej ilości danych w czystym Pythonie,
- przetwarzanie dużych pętli,
- algorytmy numeryczne bez zejścia do natywnego kodu.

Jeśli dwa wątki chcą naraz intensywnie liczyć w Pythonie, GIL sprawia, że nie liczą naprawdę równolegle tak, jak można by intuicyjnie oczekiwać.

## Gdzie GIL nie jest największym problemem

Przy zadaniach I/O-bound.

I/O-bound to np.:

- czekanie na sieć,
- czekanie na bazę danych,
- czekanie na plik,
- czekanie na API.

W takich zadaniach wątki nadal mogą być bardzo sensowne, bo dużo czasu program i tak spędza na oczekiwaniu, a nie na liczeniu CPU.

## Przykład intuicyjny

### CPU-bound

Wyobraź sobie dwa wątki, które liczą miliony operacji matematycznych.

Tu GIL zaczyna mieć duże znaczenie.

### I/O-bound

Wyobraź sobie dwa wątki, które pobierają dane z internetu i większość czasu czekają na odpowiedź.

Tu wątki nadal mogą dawać bardzo sensowną współbieżność.

## GIL nie oznacza "braku wielowątkowości"

To bardzo ważne.

W Pythonie możesz mieć:

- wiele wątków,
- współbieżność,
- sensowną obsługę I/O,
- równoległość przez procesy,
- asynchroniczność.

GIL nie kasuje tych możliwości. On po prostu wpływa na konkretny model wykonywania kodu Pythona wewnątrz jednego procesu CPythona.

## Wątki vs procesy

To jedno z najpraktyczniejszych pytań związanych z GIL.

### Wątki

Dobre często dla:

- I/O-bound,
- współdzielenia pamięci w obrębie procesu,
- prostszej współbieżności dla operacji oczekujących.

### Procesy

Dobre często dla:

- CPU-bound,
- wykorzystania wielu rdzeni,
- izolacji obliczeń.

To dlatego przy obliczeniach CPU-heavy często sensowniej rozważyć `multiprocessing` niż `threading`.

## GIL a biblioteki natywne

Jeszcze jedna ważna rzecz.

Niektóre biblioteki schodzą do kodu natywnego i tam mogą działać inaczej względem GIL.

Dlatego temat nie jest tak prosty jak:

- "wątki w Pythonie są zawsze bez sensu".

W praktyce dużo zależy od tego, co dokładnie robi kod i gdzie realnie spędza czas.

## Kiedy wiedza o GIL ma sens praktycznie

Szczególnie wtedy, gdy:

- rozważasz `threading` vs `multiprocessing`,
- optymalizujesz wydajność,
- próbujesz zrozumieć brak skalowania CPU w wielu wątkach,
- projektujesz system współbieżny.

## Kiedy nie przesadzać z GIL

Nie każda aplikacja wymaga obsesji na punkcie GIL.

Jeśli piszesz zwykłe API, parser danych albo narzędzie CLI, to ważniejsze mogą być:

- algorytmy,
- I/O,
- architektura,
- cache,
- sensowne modelowanie danych.

GIL jest ważny, ale nie wszystko w Pythonie kręci się wokół niego.

## Typowe błędy początkujących

- mylenie GIL z "brakiem współbieżności",
- przekonanie, że wątki są bezużyteczne,
- używanie wątków do ciężkiego CPU licząc na świetne skalowanie,
- ignorowanie różnicy między CPU-bound i I/O-bound,
- traktowanie GIL jako jedynej przyczyny słabej wydajności.

## Szybka ściąga

- GIL dotyczy CPythona,
- najmocniej wpływa na CPU-bound w wielu wątkach,
- nie przekreśla sensu wątków przy I/O,
- dla CPU-heavy często lepsze są procesy,
- GIL to ważny element modelu interpretera, ale nie jedyny czynnik wydajności.

## Ćwiczenia

1. Wyjaśnij różnicę między CPU-bound i I/O-bound.
2. Podaj po 3 przykłady zadań każdego typu.
3. Opisz, kiedy wybrałbyś wątki, a kiedy procesy.
4. Wskaż błędne uproszczenie o GIL i popraw je własnymi słowami.
5. Zastanów się, czy Twój ostatni większy projekt był bardziej CPU-bound czy I/O-bound.

## Najważniejsze do zapamiętania

- GIL nie oznacza, że Python nie umie we współbieżność.
- Największe znaczenie ma przy CPU-bound w wielu wątkach CPythona.
- Wątki nadal są bardzo przydatne przy I/O-bound.
- Procesy często lepiej pasują do równoległych obliczeń CPU.
- Zrozumienie GIL pomaga podejmować lepsze decyzje architektoniczne i wydajnościowe.
