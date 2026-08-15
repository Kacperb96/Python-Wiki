# Automatyczna publikacja python

## O czym jest ten rozdział

Gdy pipeline i release workflow zaczynają być uporządkowane, pojawia się następne pytanie:

- co dokładnie publikować automatycznie i kiedy?

Automatyczna publikacja to nie jest po prostu "wrzuć wszystko od razu po merge'u".

To świadoma decyzja o tym:

- jaki artefakt publikujemy,
- po jakich kontrolach,
- do jakiego miejsca,
- z jakim poziomem automatyzacji.

## Najprostsza intuicja

Automatyczna publikacja oznacza, że po spełnieniu określonych warunków pipeline sam publikuje artefakt albo release do docelowego miejsca.

To może być np.:

- paczka Pythonowa do rejestru,
- obraz Dockera do registry,
- gotowy artefakt releasowy do systemu wdrożeń.

## Po co automatyzować publikację

Automatyzacja pomaga, gdy chcesz:

- ograniczyć ręczne błędy,
- mieć powtarzalny proces,
- szybciej dostarczać artefakty,
- mieć jednoznaczny związek między kodem, pipeline'em i opublikowaną wersją,
- nie opierać releasu na pamięci jednej osoby.

## Automatyczna publikacja to nie automatyczny deployment

To bardzo ważne.

Publikacja artefaktu i deployment to nadal różne rzeczy.

Przykład:

- pipeline po tagu `v1.4.0` publikuje obraz Dockera do registry,
- ale sam deployment na produkcję może wymagać osobnej decyzji albo osobnego etapu.

To zdrowe rozróżnienie.

## Co można publikować automatycznie

Najczęściej automatycznie publikuje się:

- paczki Pythonowe,
- obrazy Dockera,
- artefakty buildowe,
- release notes,
- paczki do wewnętrznych registry.

To zwykle ma sens wtedy, gdy wejściowe quality gates są już dobrze ustawione.

## Kiedy automatyczna publikacja ma sens

Automatyczna publikacja ma sens, gdy:

- build jest powtarzalny,
- wersja jest jednoznaczna,
- quality gates są stabilne,
- zespół chce ograniczyć ręczne kroki,
- publikacja nie powinna zależeć od improwizacji.

## Kiedy trzeba uważać

Pełna automatyzacja może być zbyt agresywna, gdy:

- proces releasowy nie jest jeszcze dojrzały,
- wersjonowanie jest niespójne,
- projekt nie odróżnia dobrze artefaktu od deploymentu,
- publikacja może mieć duże skutki zewnętrzne,
- zespół nie ma jeszcze zaufania do pipeline'u.

## Trigger publikacji

To bardzo ważna decyzja.

Publikacja może odpalać się np.:

- po merge do `main`,
- po utworzeniu tagu,
- po ręcznym zatwierdzeniu releasu,
- po przejściu specjalnego workflow release'owego.

Nie ma jednego uniwersalnego modelu.

## Publish on tag: bardzo częsty wzorzec

Bardzo zdrowy model wygląda tak:

1. kod jest gotowy,
2. release dostaje wersję,
3. tworzony jest tag,
4. pipeline uruchamia publikację artefaktu dla tego tagu.

To dobre, bo:

- publikacja jest związana z konkretną wersją,
- łatwo odtworzyć, skąd wziął się artefakt,
- mniej ryzykujesz przypadkowe publikacje z losowego commita.

## Before/after

### Słabszy model

- ktoś ręcznie publikuje paczkę albo obraz,
- łatwo pomylić wersję,
- łatwo opublikować z niewłaściwego commita,
- proces jest mniej powtarzalny.

### Lepszy model

- pipeline sam publikuje po spełnieniu warunków,
- artefakt jest powiązany z wersją i tagiem,
- zespół może ufać procesowi bardziej niż ręcznej pamięci.

## Mini case study: publikacja paczki Pythonowej

Masz bibliotekę Pythonową.

Zdrowy model może wyglądać tak:

1. merge zmian,
2. pipeline przechodzi,
3. przygotowujesz wersję `1.5.0`,
4. tagujesz commit jako `v1.5.0`,
5. pipeline buduje paczkę,
6. paczka trafia do rejestru.

To daje bardzo czytelną ścieżkę od kodu do publikacji.

## Mini case study: obraz Dockera

Masz backend wdrażany jako obraz.

Zdrowy model:

1. release `v2.3.1`,
2. pipeline buduje obraz,
3. obraz dostaje sensowny tag wersji,
4. obraz trafia do registry,
5. deployment może nastąpić później w osobnym kroku.

To dużo dojrzalsze niż ręczne budowanie obrazu na czyimś laptopie.

## Sekrety w publikacji

To bardzo ważny temat.

Automatyczna publikacja często wymaga dostępu do:

- registry,
- rejestru paczek,
- kont wdrożeniowych,
- kluczy podpisujących.

Te rzeczy nie powinny być wpisywane w repo ani jawnie w pipeline config bez ochrony.

Czyli automatyzacja wymaga jednocześnie dyscypliny bezpieczeństwa.

## Częste pułapki

### 1. Automatyczna publikacja bez stabilnego wersjonowania

Potem nie wiadomo, która wersja jest czym.

### 2. Publikacja z `main` bez jasnych zasad

Może prowadzić do publikowania za często albo zbyt przypadkowo.

### 3. Brak rozróżnienia artefaktu i wdrożenia

To może dać fałszywe poczucie kontroli nad procesem.

### 4. Ręczne nadpisywanie opublikowanych artefaktów

To bardzo niebezpieczne z perspektywy śledzalności.

### 5. Brak jednoznacznego związku między tagiem, buildem i changelogiem

Wtedy automatyzacja istnieje, ale nie daje prawdziwego porządku.

## Co Pythonowiec powinien rozumieć

Dobrze, żebyś umiał:

- rozumieć, co znaczy automatyczna publikacja artefaktu,
- nie mylić publikacji z deploymentem,
- myśleć o triggerze publikacji jako decyzji procesowej,
- dbać o jednoznaczne powiązanie wersji, tagu i artefaktu,
- pamiętać, że automatyzacja bez zasad może tylko szybciej produkować chaos.

## Output myślowy

### Ręczna publikacja

- większe ryzyko pomyłki,
- większa zależność od konkretnej osoby,
- gorsza powtarzalność procesu.

### Automatyczna publikacja

- większa przewidywalność,
- łatwiejsza śledzalność,
- mniej ręcznych kroków,
- ale większa potrzeba dyscypliny procesowej i bezpieczeństwa.

## Najważniejsze do zapamiętania

- Automatyczna publikacja dotyczy artefaktów, nie musi oznaczać automatycznego deploymentu.
- Dobrze działa, gdy wersjonowanie, tagowanie i quality gates są już uporządkowane.
- Bardzo częsty sensowny model to publikacja po tagu.
- Sekrety i uprawnienia do publikacji trzeba traktować bardzo ostrożnie.
- Automatyzacja jest wartościowa wtedy, gdy wzmacnia porządek, a nie przyspiesza chaos.

## Ćwiczenia

1. Wyjaśnij własnymi słowami różnicę między automatyczną publikacją i automatycznym deploymentem.
2. Opisz, czemu publikacja po tagu jest często sensownym modelem.
3. Rozpisz prosty workflow automatycznej publikacji paczki Pythonowej.
4. Wypisz trzy ryzyka źle zaprojektowanej automatycznej publikacji.
5. Opisz, jakie powiązania powinny istnieć między tagiem, wersją i artefaktem.
