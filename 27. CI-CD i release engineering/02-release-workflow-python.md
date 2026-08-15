# Release workflow python

## O czym jest ten rozdział

Wiele osób na początku miesza trzy różne rzeczy:

- merge zmiany,
- release,
- deployment.

To bardzo częste i później robi duży bałagan.

Release workflow to nie jest po prostu "wrzucenie kodu na serwer".

To uporządkowany proces, który odpowiada na pytania:

- kiedy zmiana jest gotowa do wydania,
- jak ją oznaczyć,
- jak przygotować artefakt,
- jak zakomunikować zawartość releasu,
- kiedy i jak wdrożyć go dalej.

## Najprostsza intuicja

Release workflow to ścieżka od zaakceptowanej zmiany do świadomie przygotowanej wersji systemu.

Najprościej:

- zmiany trafiają do gałęzi głównej albo release branch,
- pipeline sprawdza jakość,
- tworzysz wersję,
- budujesz artefakt,
- publikujesz release,
- potem możesz go wdrażać.

## Merge to nie release

To jeden z najważniejszych punktów.

Merge oznacza zwykle:

- kod został połączony z głównym nurtem pracy.

Release oznacza:

- świadomie przygotowaliśmy konkretną wersję do wydania.

To nie musi być ten sam moment.

## Release to nie deployment

To drugi bardzo ważny punkt.

Release oznacza:

- wersja została przygotowana i oznaczona.

Deployment oznacza:

- ta wersja została uruchomiona w konkretnym środowisku.

Czyli można mieć sytuację:

- release już istnieje,
- ale jeszcze nie został wdrożony na produkcję.

## Typowy prosty workflow

Bardzo uproszczony, ale zdrowy workflow może wyglądać tak:

1. zmiana trafia do repo,
2. pipeline przechodzi,
3. zmiana zostaje zmergowana,
4. przygotowywana jest wersja `x.y.z`,
5. budowany jest artefakt,
6. tworzony jest tag i changelog releasu,
7. artefakt jest publikowany,
8. deployment następuje później albo od razu, zależnie od procesu.

## Po co workflow releasowy w ogóle istnieje

Bez sensownego workflow bardzo szybko pojawia się chaos:

- nie wiadomo, co weszło w daną wersję,
- trudno odtworzyć, co było wdrożone,
- artefakty powstają ręcznie i niespójnie,
- release zależy od pamięci konkretnej osoby.

Workflow releasowy daje przewidywalność.

## Najprostszy przykład myślowy

Masz projekt API.

Zmiana została zmergowana do `main`.

To jeszcze nie znaczy automatycznie, że trzeba natychmiast zrobić publiczny release.

Najpierw możesz chcieć:

- zebrać kilka zmian,
- potwierdzić gotowość,
- zaktualizować changelog,
- oznaczyć wersję,
- zbudować artefakt,
- dopiero wtedy wypuścić release.

## Release branch vs release from main

To dwa popularne style myślenia.

### Release from main

- główna gałąź jest stale releasowalna,
- release wychodzi bezpośrednio z `main`.

### Release branch

- tworzysz osobną gałąź release'ową,
- stabilizujesz konkretną wersję,
- ograniczasz, co może do niej wejść.

Nie ma jednego zawsze najlepszego modelu. To zależy od skali, zespołu i rodzaju systemu.

## Kiedy release workflow powinien być prosty

Jeśli projekt jest mały, zespół niewielki, a tempo zmian umiarkowane, workflow może być dość prosty.

Przykład:

- merge do `main`,
- zielony pipeline,
- ręczne utworzenie releasu,
- publikacja artefaktu,
- późniejszy deployment.

To bywa wystarczające.

## Kiedy release workflow robi się bardziej rozbudowany

Większa złożoność ma sens, gdy:

- system jest krytyczny,
- zmian jest dużo,
- releasy są częste,
- wiele osób pracuje równolegle,
- rollback i śledzenie wersji muszą być bardzo precyzyjne.

Wtedy dochodzą rzeczy takie jak:

- release branch,
- mocniejsze quality gates,
- staging przed produkcją,
- zatwierdzenia releasu,
- bardziej formalny changelog.

## Before/after

### Słabszy model

- ktoś ręcznie pakuje release "jak leci",
- nie wiadomo dokładnie, co weszło,
- artefakt nie jest jednoznacznie powiązany z wersją.

### Lepszy model

- release ma jasny moment powstania,
- ma wersję,
- ma tag,
- ma changelog,
- ma artefakt,
- można go jednoznacznie śledzić.

## Mini case study: paczka Pythonowa

Masz bibliotekę wewnętrzną albo publiczną paczkę Pythonową.

Zdrowy release workflow może wyglądać tak:

1. merge zmian,
2. pipeline przechodzi,
3. wersja zostaje podbita,
4. changelog jest gotowy,
5. tag wskazuje dokładny commit releasu,
6. budowana jest paczka,
7. paczka trafia do rejestru.

To bardzo przewidywalny model.

## Mini case study: aplikacja webowa

Masz backend wdrażany jako obraz Dockera.

Release workflow może wyglądać tak:

1. merge do `main`,
2. pipeline przechodzi,
3. tworzony jest release `v1.8.0`,
4. budowany jest obraz z konkretnym tagiem,
5. obraz trafia do registry,
6. deployment do staging lub prod następuje według osobnej decyzji.

To dobrze pokazuje, że release i deployment to nie to samo.

## Co Pythonowiec powinien rozumieć

Dobrze, żebyś umiał:

- odróżnić merge, release i deployment,
- rozumieć, po co wersja musi być jednoznaczna,
- wiedzieć, że release powinien dać się powiązać z artefaktem i zmianami,
- nie robić procesu zależnego od pamięci i ręcznych skrótów,
- myśleć o releasie jako o kroku inżynierskim, a nie "chwili publikacji".

## Output myślowy

### Chaotyczny release

- trudno powiedzieć, co dokładnie zostało wydane,
- trudno odtworzyć wersję,
- rollback i analiza błędów są cięższe.

### Dojrzalszy release workflow

- każda wersja jest śledzalna,
- wiadomo, co weszło,
- artefakt jest jednoznacznie powiązany z kodem,
- zespół pracuje bardziej przewidywalnie.

## Najważniejsze do zapamiętania

- Merge, release i deployment to trzy różne rzeczy.
- Release workflow porządkuje drogę od zmiany do wydanej wersji.
- Wersja, tag, changelog i artefakt powinny być ze sobą spójne.
- Im bardziej krytyczny system, tym większy sens ma dojrzalszy workflow releasowy.
- Dobrze zaprojektowany release workflow zmniejsza chaos i ryzyko operacyjne.

## Ćwiczenia

1. Wyjaśnij własnymi słowami różnicę między merge, release i deploymentem.
2. Rozpisz prosty release workflow dla biblioteki Pythonowej.
3. Opisz sytuację, w której release branch ma sens.
4. Wskaż trzy elementy, które powinny jednoznacznie identyfikować release.
5. Opisz ryzyko chaotycznego, ręcznego releasu bez spójnego procesu.
