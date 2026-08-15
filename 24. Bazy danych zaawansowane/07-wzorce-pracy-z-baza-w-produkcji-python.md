# Wzorce pracy z baza w produkcji python

## O czym jest ten rozdział

Na wcześniejszych etapach pracy z bazą łatwo skupić się na samym SQL-u albo ORM-ie.

W produkcji to za mało.

Zaczynają się pytania:

- gdzie otwierać transakcję,
- ile logiki trzymać w jednej operacji,
- jak unikać N+1 query,
- jak obsługiwać retry i błędy,
- jak nie robić ciężkich rzeczy w złym miejscu,
- jak nie zabić bazy mimo poprawnego kodu Python.

Ten plik zbiera praktyczne wzorce myślenia o pracy z bazą w aplikacji produkcyjnej.

## Najprostsza zasada

Nie myśl tylko:

- "czy query działa?"

Myśl także:

- ile kosztuje,
- jak często jest wykonywane,
- czy działa dobrze pod współbieżnością,
- czy jest odporne na błędy,
- czy nie robi za dużo w jednej transakcji.

## Wzorzec 1: krótkie transakcje

To jedna z najważniejszych zasad.

Transakcja powinna być możliwie krótka.

Dlaczego?

Bo dłuższa transakcja zwykle oznacza:

- dłuższe trzymanie locków,
- większe ryzyko konfliktów,
- większe ryzyko deadlocków,
- większe opóźnienia dla innych operacji.

### Słabszy wariant

- pobierasz dane,
- liczysz dużo logiki,
- robisz request do zewnętrznego API,
- dopiero potem commit.

To bardzo ryzykowny model.

### Lepszy wariant

- przygotuj, co się da, poza transakcją,
- w transakcji wykonaj tylko to, co naprawdę musi być atomowe,
- commit jak najszybciej.

## Wzorzec 2: świadome ładowanie danych

Jednym z klasycznych problemów aplikacyjnych jest N+1 query.

Najprostsza intuicja:

- pobierasz listę rekordów,
- dla każdego rekordu osobno dobierasz kolejne dane,
- liczba query rośnie lawinowo.

Przykład myślowy:

- 1 query po 100 zamówień,
- potem 100 osobnych query po dane klientów.

To często działa lokalnie i boli dopiero na większych danych.

## Wzorzec 3: czytaj tylko to, czego potrzebujesz

Jeśli do listy potrzebujesz:

- `id`,
- `status`,
- `created_at`,

nie zawsze trzeba pobierać pełen, ciężki rekord z wszystkimi relacjami i dużymi polami tekstowymi.

To prosty, ale bardzo ważny nawyk.

## Wzorzec 4: oddziel hot path od pracy ciężkiej

Nie każda operacja musi wykonać wszystko synchronicznie w request-response.

Przykład:

- zapisujesz zamówienie teraz,
- ciężki raport, przeliczenie albo wysyłka dużych powiadomień może pójść później.

Jeśli wszystko wrzucisz do jednej ścieżki z bazą, endpoint szybko stanie się ciężki i kruchy.

## Wzorzec 5: bądź ostrożny z retry

Retry bywa bardzo przydatne przy:

- chwilowych błędach,
- deadlockach,
- konfliktach przejściowych.

Ale retry bezmyślne jest niebezpieczne.

Musisz zapytać:

- czy operacja jest idempotentna,
- czy powtórzenie nie utworzy dubli,
- czy nie uruchomisz drugi raz logiki biznesowej z kosztownym skutkiem.

## Wzorzec 6: logika biznesowa nie powinna przypadkiem ukrywać kosztu bazy

Czasem kod wygląda niewinnie, ale robi bardzo dużo zapytań.

Przykład myślowy w Pythonie:

```python
for order in orders:
    print(order.customer.name)
```

Na poziomie kodu to wygląda banalnie.

Na poziomie bazy może oznaczać lawinę dodatkowych odczytów.

Dlatego trzeba umieć myśleć nie tylko o kodzie Python, ale o tym, jakie query naprawdę z niego wynikają.

## Wzorzec 7: obsługuj błędy bazodanowe świadomie

Nie każdy błąd bazy oznacza to samo.

Możesz spotkać:

- konflikt unikalności,
- timeout,
- deadlock,
- zerwane połączenie,
- błąd walidacji danych,
- konflikt współbieżności.

Dojrzała aplikacja nie traktuje wszystkiego jako jednego ogólnego `500` bez kontekstu.

## Wzorzec 8: obserwuj najbardziej kosztowne query

W produkcji warto wiedzieć:

- które query są najwolniejsze,
- które występują najczęściej,
- które endpointy generują największy koszt,
- które operacje wywołują konflikty albo timeouty.

Bez tej wiedzy optymalizacja jest zgadywaniem.

## Mini case study: lista zamówień supportu

Masz ekran supportu z listą zamówień.

### Słaby wariant

- pobierasz pełne rekordy zamówień,
- dla każdego dociągasz klienta osobno,
- dla każdego liczysz dodatkowe agregaty w pętli,
- wszystko dzieje się przy jednym requestcie.

Efekt:

- dużo query,
- długi czas odpowiedzi,
- rosnący koszt wraz z liczbą rekordów.

### Lepszy wariant

- pobierasz tylko pola potrzebne do listy,
- ograniczasz liczbę round-tripów,
- agregacje planujesz świadomie,
- cięższe rzeczy odsuwasz poza hot path, jeśli to możliwe.

## Wzorzec 9: nie mieszaj wszystkiego w jednej warstwie

Dobrze, gdy kod jasno pokazuje:

- gdzie jest logika aplikacyjna,
- gdzie są operacje repozytorium lub dostępu do danych,
- gdzie zaczyna się transakcja,
- gdzie łapane są błędy i mapowane na odpowiedzi API.

To ułatwia zarówno optymalizację, jak i debugowanie.

## Wzorzec 10: projektuj pod realne użycie, nie pod teorię

Teoretycznie model może być piękny, a query poprawne.

Ale jeśli:

- użytkownik najczęściej ogląda listę 50 ostatnich zamówień,
- support robi masowo filtrowanie po statusie,
- raport dzienny liczy milion rekordów,

to właśnie pod te ścieżki trzeba projektować sposób pracy z bazą.

## Before/after

### Niedojrzałe podejście

- ważne, że działa lokalnie,
- SQL i ORM są traktowane jak czarna skrzynka,
- transakcja obejmuje za dużo,
- obserwowanie kosztu query prawie nie istnieje.

### Dojrzalsze podejście

- patrzysz na hot path,
- liczysz round-tripy,
- skracasz transakcje,
- świadomie obchodzisz się z retry i błędami,
- obserwujesz najdroższe zapytania.

## Co Pythonowiec powinien umieć praktycznie

Dobrze, żebyś umiał:

- rozpoznać N+1 query,
- skracać transakcje,
- nie robić ciężkiej logiki w złym miejscu,
- odróżnić błąd współbieżności od walidacji biznesowej,
- pytać, ile zapytań naprawdę wykonuje dany endpoint,
- traktować bazę jako współuczestnika architektury, a nie tylko magazyn danych.

## Output myślowy

### Kod wygląda dobrze, ale produkcja boli

- query jest za dużo,
- transakcje są za długie,
- koszt ujawnia się dopiero przy ruchu.

### Kod i sposób pracy z bazą są świadome

- mniej niespodzianek pod obciążeniem,
- łatwiejsze debugowanie,
- prostsza optymalizacja,
- większa przewidywalność systemu.

## Najważniejsze do zapamiętania

- Produkcyjna praca z bazą to nie tylko poprawny SQL, ale też koszt, współbieżność i architektura użycia.
- Krótkie transakcje są jedną z najważniejszych zasad.
- N+1 query to klasyczny problem, który trzeba umieć zauważać.
- Nie wszystko powinno dziać się synchronicznie w jednym requestcie.
- Bez obserwowalności najdroższych query optymalizacja jest zgadywaniem.

## Ćwiczenia

1. Wyjaśnij własnymi słowami, czemu długa transakcja jest ryzykowna.
2. Opisz intuicyjnie problem N+1 query.
3. Podaj przykład operacji, której nie wrzucałbyś w całości do jednego requestu z bazą.
4. Wypisz trzy informacje o query, które chciałbyś widzieć w produkcji.
5. Weź prosty endpoint listy i opisz, jakie koszty bazodanowe może ukrywać.
