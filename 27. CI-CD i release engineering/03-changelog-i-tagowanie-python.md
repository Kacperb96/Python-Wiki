# Changelog i tagowanie python

## O czym jest ten rozdział

Release bez czytelnego changelogu i bez sensownego tagowania bardzo szybko staje się trudny do śledzenia.

Pojawiają się wtedy pytania:

- co weszło do tej wersji,
- który commit odpowiada za ten release,
- kiedy dana zmiana trafiła do użytkowników,
- skąd wziął się bug w konkretnej wersji.

Właśnie dlatego changelog i tagi są tak ważne.

## Najprostsza intuicja changelogu

Changelog to uporządkowany opis zmian między wersjami.

Najprościej:

- mówi ludziom, co się zmieniło,
- pomaga zespołowi i użytkownikom zrozumieć zawartość release'u,
- daje czytelny zapis historii produktu.

## Najprostsza intuicja tagu

Tag to etykieta wskazująca konkretny punkt w historii repo.

Najprościej:

- mówi: ten commit odpowiada za wersję `v1.4.0`.

To bardzo ważne, bo pozwala jednoznacznie powiązać:

- kod,
- artefakt,
- release,
- późniejszy deployment.

## Po co changelog ma sens

Changelog pomaga, gdy chcesz:

- szybko zobaczyć, co weszło do wersji,
- przygotować komunikację dla zespołu albo użytkowników,
- ułatwić debugging regresji,
- rozumieć tempo i zakres zmian w czasie.

Bez niego łatwo zostać z listą commitów, która nie zawsze mówi to, co najważniejsze.

## Po co tag ma sens

Tag pomaga, gdy chcesz:

- wskazać dokładny commit releasu,
- budować artefakty z konkretnej wersji,
- wrócić do znanego punktu w historii,
- łatwiej analizować, od której wersji pojawił się problem.

To bardzo mocna praktyczna kotwica w procesie releasowym.

## Przykład prostego changelogu

```text
## v1.4.0 - 2026-08-15
- dodano endpoint eksportu raportu
- poprawiono paginację listy zamówień
- naprawiono błąd podwójnego naliczania punktów
```

Najważniejsza intuicja:

- changelog ma być czytelny dla ludzi,
- nie tylko mechanicznie poprawny.

## Przykład tagu

Typowy tag może wyglądać tak:

```text
v1.4.0
```

Najważniejsze jest, żeby zespół miał spójną konwencję.

## Changelog to nie lista wszystkich commitów

To częsty błąd.

Commit history i changelog to nie to samo.

Commit może być techniczny, drobny albo wewnętrzny.

Changelog powinien raczej opisywać sensowne zmiany z perspektywy releasu:

- nowe funkcje,
- ważne poprawki,
- breaking changes,
- zmiany operacyjne warte odnotowania.

## Before/after

### Słabszy model

- tagi są nieregularne albo przypadkowe,
- changelog jest pusty albo nieczytelny,
- nikt nie wie, co naprawdę weszło do wersji.

### Lepszy model

- każda wersja ma tag,
- changelog opisuje ważne zmiany,
- można łatwo powiązać wersję z kodem i releasem.

## Wersjonowanie a changelog

Changelog dobrze współgra z wersjonowaniem.

Przykład:

- `v1.3.0` — nowe funkcje,
- `v1.3.1` — poprawka błędu,
- `v2.0.0` — zmiana łamiąca kompatybilność.

Wtedy changelog i wersja razem opowiadają historię zmian dużo lepiej niż same commity.

## Co warto wpisywać do changelogu

Najczęściej warto uwzględniać:

- nowe funkcje,
- ważne poprawki błędów,
- breaking changes,
- istotne zmiany bezpieczeństwa,
- zmiany wpływające na wdrożenie lub konfigurację.

## Czego zwykle nie trzeba eksponować zbyt mocno

Nie każdy drobiazg deweloperski musi lądować w changelogu użytkowym.

Przykłady:

- drobne refaktoryzacje bez wpływu na zachowanie,
- kosmetyczne poprawki testów,
- małe wewnętrzne porządki kodu.

To zależy od typu projektu, ale warto mieć filtr znaczenia.

## Mini case study: paczka publiczna

Masz bibliotekę Pythonową publikowaną zewnętrznie.

W tym przypadku changelog jest szczególnie ważny, bo odbiorcy potrzebują wiedzieć:

- czy update jest bezpieczny,
- czy są breaking changes,
- czy dana poprawka ich dotyczy.

Tag pozwala jednoznacznie odtworzyć kod odpowiadający paczce.

## Mini case study: backend wewnętrzny

Nawet jeśli projekt nie jest publiczną biblioteką, changelog nadal ma sens.

Pomaga np. odpowiedzieć:

- co weszło w ostatnim releasie backendu,
- czy zmiana obejmuje migrację bazy,
- czy wdrożenie wymaga nowej konfiguracji,
- kiedy pojawiła się konkretna poprawka.

## Częste pułapki

### 1. Brak tagów albo tagi tworzone przypadkowo

Wtedy trudniej związać release z kodem.

### 2. Changelog zbyt techniczny albo zbyt pusty

Jeśli jest tylko dla autora i nikt poza nim go nie rozumie, jego wartość spada.

### 3. Brak spójnej konwencji wersji

Tagi typu:

- `release-final-final2`,
- `nowa-wersja`,

bardzo szybko robią bałagan.

### 4. Aktualizowanie changelogu po fakcie bez dyscypliny

Wtedy łatwo pominąć ważne rzeczy albo dopisać je nieprecyzyjnie.

### 5. Mylenie changelogu z logiem commitów

To znowu osłabia czytelność.

## Co Pythonowiec powinien rozumieć

Dobrze, żebyś umiał:

- rozumieć rolę changelogu jako narzędzia komunikacji i śledzenia zmian,
- wiedzieć, po co tag ma wskazywać konkretny punkt historii,
- odróżniać sensowne zmiany releasowe od technicznej drobnicy,
- utrzymywać spójną konwencję tagowania,
- traktować changelog i tagi jako część release engineeringu, a nie dokumentację poboczną.

## Output myślowy

### Bez changelogu i tagów

- release istnieje bardziej w pamięci ludzi niż w systemie,
- trudniej analizować historię i regresje.

### Z sensownym changelogiem i tagami

- wiadomo, co wyszło,
- wiadomo z jakiego kodu,
- łatwiej rozumieć i śledzić rozwój systemu.

## Najważniejsze do zapamiętania

- Changelog opisuje sensowne zmiany releasowe.
- Tag wskazuje konkretny commit odpowiadający wersji.
- To dwa bardzo ważne elementy porządku w release workflow.
- Changelog nie jest tym samym co lista commitów.
- Spójna konwencja tagów i wersji bardzo ułatwia życie zespołu.

## Ćwiczenia

1. Wyjaśnij własnymi słowami różnicę między changelogiem i historią commitów.
2. Podaj przykład sensownego tagu wersji i złego tagu wersji.
3. Rozpisz prosty changelog dla wersji `v1.4.0` backendu zamówień.
4. Wskaż trzy rzeczy, które warto wpisywać do changelogu.
5. Opisz, jak tag pomaga przy analizie regresji w konkretnej wersji.
