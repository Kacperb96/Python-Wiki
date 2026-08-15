# CPU-bound vs I/O-bound w Pythonie

## O co chodzi

To jedno z najważniejszych rozróżnień w całym temacie performance.

Zanim zaczniesz optymalizować, musisz rozumieć, co naprawdę ogranicza program:

- procesor,
- czy oczekiwanie na zewnętrzne operacje.

## CPU-bound

CPU-bound oznacza, że program większość czasu spędza na liczeniu.

Przykłady:

- intensywne obliczenia matematyczne,
- duże pętle w czystym Pythonie,
- analiza danych w pamięci,
- przetwarzanie dużej liczby rekordów z ciężką logiką.

Wąskim gardłem jest wtedy CPU.

## I/O-bound

I/O-bound oznacza, że program większość czasu spędza na czekaniu.

Czeka np. na:

- plik,
- bazę danych,
- sieć,
- API,
- dysk,
- socket.

Wąskim gardłem nie jest liczenie, tylko zewnętrzne wejście/wyjście.

## Najprostsza intuicja

### CPU-bound

Program jest "zajęty pracą".

### I/O-bound

Program jest "zajęty czekaniem".

To rozróżnienie bardzo wpływa na to, jakie techniki poprawy wydajności mają sens.

## Dlaczego to ma takie znaczenie

Bo inny typ problemu oznacza inne rozwiązania.

### Dla CPU-bound

Często ważniejsze są:

- lepszy algorytm,
- lepsza struktura danych,
- procesy zamiast wątków,
- zejście do kodu natywnego albo wyspecjalizowanych bibliotek.

### Dla I/O-bound

Często pomagają:

- wątki,
- async,
- batchowanie operacji,
- mniej round-tripów do bazy/API,
- cache.

## Prosty przykład mentalny

### CPU-bound

Przeliczanie miliona rekordów z kosztowną logiką dla każdego elementu.

### I/O-bound

Pobieranie 1000 odpowiedzi z API, gdzie każda czeka na sieć.

W obu przypadkach program może być "wolny", ale przyczyna i lekarstwo są zupełnie inne.

## GIL a CPU-bound

To temat bardzo związany z folderem 19.

Jeśli problem jest CPU-bound i chcesz użyć wielu wątków w CPythonie, GIL zaczyna mieć znaczenie.

Dlatego przy CPU-heavy obliczeniach często sensowniejsze są procesy niż wątki.

## Wątki i I/O-bound

Przy I/O-bound wątki nadal mogą być świetnym narzędziem.

Bo jeśli jeden wątek czeka na odpowiedź z sieci, inny może robić coś w tym czasie.

To dlatego hasło "wątki w Pythonie są bez sensu" jest po prostu błędne.

## Jak rozpoznać, z czym masz do czynienia

Zadaj sobie pytania:

- czy program głównie liczy,
- czy głównie czeka,
- czy CPU rośnie mocno,
- czy problemem są requesty, pliki lub baza,
- czy kolejne optymalizacje algorytmu coś zmieniają,
- czy skrócenie liczby operacji sieciowych daje większy efekt niż poprawa pętli.

## Mini case study 1

Masz skrypt, który przetwarza plik 5 GB i wykonuje ciężkie dopasowania regexowe w każdej linii.

To może być mieszany przypadek, ale jeśli plik jest lokalny i koszt siedzi głównie w przetwarzaniu tekstu, problem może być bardziej CPU-bound niż się wydaje.

## Mini case study 2

Masz aplikację, która pobiera dane z 50 endpointów HTTP i scala wyniki.

To bardzo często będzie I/O-bound.

Największy zysk może dać współbieżność I/O, a nie mikrooptymalizacja jednej funkcji czyszczącej stringi.

## Typowe błędy początkujących

- brak rozróżnienia CPU i I/O,
- używanie wątków do ciężkich obliczeń CPU z nadzieją na idealne skalowanie,
- optymalizowanie pętli, gdy problem siedzi w bazie albo API,
- mylenie ogólnego "wolno działa" z konkretnym typem wąskiego gardła.

## Szybka ściąga

- CPU-bound = głównie liczenie,
- I/O-bound = głównie czekanie,
- CPU-bound często kieruje w stronę algorytmów, struktur danych i procesów,
- I/O-bound często kieruje w stronę wątków, async i redukcji kosztu zewnętrznych operacji.

## Ćwiczenia

1. Podaj 5 przykładów CPU-bound.
2. Podaj 5 przykładów I/O-bound.
3. Opisz problem z własnego doświadczenia i sklasyfikuj go.
4. Wyjaśnij, czemu GIL bardziej interesuje przy CPU-bound.
5. Wskaż, jakie rozwiązania rozważyłbyś dla każdego typu problemu.

## Najważniejsze do zapamiętania

- To jedno z najważniejszych rozróżnień w performance.
- Inny typ problemu oznacza inne sensowne narzędzia.
- Bez tej klasyfikacji bardzo łatwo optymalizować nie to, co trzeba.
- CPU-bound i I/O-bound mogą wyglądać podobnie z zewnątrz, ale wymagają innego myślenia.
- Poprawna diagnoza jest często ważniejsza niż sama technika optymalizacji.
