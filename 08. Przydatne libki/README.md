# 08. Przydatne libki

To jest bardzo praktyczny folder.

Nie chodzi tutaj o to, żeby poznać kilka "fajnych modułów" i potem o nich zapomnieć. Chodzi o coś znacznie ważniejszego:

- rozpoznawanie typowych problemów,
- wiedzę, że Python już ma gotowe narzędzie,
- umiejętność wyboru rozwiązania, które jest prostsze i czytelniejsze,
- odróżnianie sensownego użycia biblioteki od przerostu formy nad treścią.

Ten dział zbiera moduły standardowej biblioteki, które bardzo często pojawiają się w realnym kodzie:

- `re`,
- `itertools`,
- `functools`,
- `collections`,
- `typing`,
- `dataclasses`.

## Jaki problem rozwiązuje ten folder

Na początku nauki bardzo wiele rzeczy pisze się "ręcznie":

- ręczne liczenie elementów,
- ręczne grupowanie danych,
- ręczne parsowanie tekstu,
- ręczne budowanie prostych modeli danych,
- ręczne pisanie powtarzalnego kodu klas,
- ręczne ogarnianie iteratorów.

To jest normalne.

Ale potem przychodzi etap, w którym warto wiedzieć:

- kiedy zwykła pętla jest najlepsza,
- kiedy biblioteka upraszcza kod,
- kiedy narzędzie jest zbyt sprytne jak na prosty problem,
- kiedy standardowa biblioteka daje rozwiązanie bardziej idiomatyczne.

Ten folder właśnie tego uczy.

## Jak czytać ten dział

Najlepiej iść po kolei:

1. `01-re-python.md`
2. `02-itertools-python.md`
3. `03-functools-python.md`
4. `04-collections-python.md`
5. `05-typing-python.md`
6. `06-dataclasses-python.md`

Ta kolejność ma sens, bo przechodzisz od pracy na tekście i danych, przez iteratory i funkcje, do typowania i modelowania danych.

## Najważniejsze pytanie w tym folderze

Przy każdym module warto pytać nie tylko:

- jak tego użyć?

ale też:

- kiedy to ma sens?
- kiedy to upraszcza kod?
- kiedy zwykły `for`, `dict`, `split()` albo zwykła klasa są lepsze?

To jest klucz do dojrzałego korzystania z tych bibliotek.

## Szybka mapa decyzji

### `re`

Używaj, gdy:

- trzeba rozpoznać wzorzec,
- wyciągasz dane z tekstu,
- walidujesz format,
- zwykłe `split()` i `replace()` przestają wystarczać.

Nie używaj, gdy:

- wystarczy `in`, `startswith()`, `endswith()`, `split()`, `replace()`.

### `itertools`

Używaj, gdy:

- chcesz leniwie przetwarzać dane,
- łączysz wiele iterowalnych źródeł,
- generujesz kombinacje, permutacje lub pary,
- chcesz budować pipeline iteratorów.

Nie używaj, gdy:

- prosty `for` jest czytelniejszy,
- i tak natychmiast zamieniasz wszystko na listę bez potrzeby.

### `functools`

Używaj, gdy:

- chcesz dodać cache,
- poprawnie piszesz dekorator,
- wiążesz część argumentów funkcji,
- chcesz uporządkować pracę z funkcjami wyższego rzędu.

Nie używaj, gdy:

- rozwiązanie przez `partial()` albo `reduce()` robi się mniej czytelne niż zwykła funkcja.

### `collections`

Używaj, gdy:

- liczysz elementy,
- grupujesz rekordy,
- potrzebujesz kolejki,
- łączysz kilka warstw konfiguracji,
- chcesz lekkiej struktury danych.

Nie używaj, gdy:

- zwykły `dict` albo `list` są prostsze i całkowicie wystarczające.

### `typing`

Używaj, gdy:

- chcesz lepiej opisać kontrakt funkcji,
- pracujesz z większym kodem,
- chcesz szybciej wykrywać błędy narzędziami,
- budujesz kod dla siebie z przyszłości albo dla innych ludzi.

Nie używaj, gdy:

- typy stają się gęstsze od samej logiki,
- dodajesz złożone adnotacje bez żadnej realnej korzyści.

### `dataclasses`

Używaj, gdy:

- klasa głównie przechowuje dane,
- chcesz automatyczne `__init__`, `__repr__`, `__eq__`,
- modelujesz rekordy, DTO, config, value object.

Nie używaj, gdy:

- klasa ma rozbudowane zachowanie i mało danych,
- potrzebujesz bardziej niestandardowej logiki niż prostego modelu danych.

## Jak ćwiczyć najlepiej

Najlepszy styl nauki dla tego folderu wygląda tak:

1. napisz rozwiązanie ręcznie,
2. napisz drugie rozwiązanie z biblioteką,
3. porównaj długość, czytelność i elastyczność,
4. odpowiedz, które wybrałbyś do prawdziwego projektu.

To ważne, bo te moduły nie służą do popisywania się składnią. One mają upraszczać życie.

## Mini projekty, które ten folder powinien Ci umożliwić

Po przerobieniu tego działu powinieneś umieć zrobić małe rzeczy typu:

- parser logów z `re`, `dataclass`, `typing` i `Counter`,
- prostą analizę danych tekstowych z `defaultdict` i `itertools`,
- mini warstwę konfiguracji z `ChainMap` i `TypedDict`,
- model danych z `dataclass` i walidacją w `__post_init__`,
- dekorator z `wraps` i cache przez `lru_cache`.

## Po czym poznasz, że temat naprawdę siedzi

Dobry znak, jeśli potrafisz:

- wskazać, kiedy regex ma sens, a kiedy jest przesadą,
- wyjaśnić, kiedy `itertools` daje realny zysk nad zwykłą pętlą,
- użyć `Counter`, `defaultdict` i `deque` bez zastanawiania się nad prowizorką,
- dodać sensowne typowanie bez zamieniania kodu w ścianę adnotacji,
- odróżnić `dataclass` od zwykłej klasy i wiedzieć, kiedy która jest lepsza,
- połączyć kilka tych bibliotek w jednym małym projekcie.

## Główne ryzyko tego folderu

Największym błędem nie jest brak znajomości składni.

Największym błędem jest używanie tych narzędzi bez wyczucia.

Czyli na przykład:

- regex do najprostszego `split()`,
- `reduce()` zamiast czytelnego `sum()`,
- `itertools` tam, gdzie prosta lista wystarczy,
- `typing` robione tylko dla ozdoby,
- `dataclass` wciskane tam, gdzie klasa ma głównie zachowanie, nie dane.

## Podsumowanie

To jest folder o świadomym wyborze narzędzi.

Jeśli go dobrze opanujesz, zaczniesz nie tylko pisać kod, który działa, ale też częściej rozpoznawać:

- że Python już ma gotowe rozwiązanie,
- że nie trzeba wszystkiego pisać ręcznie,
- i że dobra biblioteka standardowa potrafi mocno uprościć projekt.
