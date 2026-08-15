# Refaktoryzacja w starym repo w Pythonie

## O co chodzi

Refaktoryzacja w starym repo to zupełnie inna sytuacja niż pisanie ładnego kodu od zera.

W starym systemie masz często:

- niepełne testy,
- niejasne zależności,
- stare założenia biznesowe,
- kod z efektami ubocznymi,
- nieczytelne nazwy,
- duże ryzyko przypadkowego rozwalenia czegoś obok.

Dlatego refaktoryzacja w takim środowisku musi być ostrożniejsza i bardziej metodyczna.

## Najważniejsza zasada

Małe kroki wygrywają.

To jedna z najważniejszych zasad pracy w starym repo.

Zamiast:

- przepisać cały moduł,
- uporządkować wszystko naraz,
- zrobić wielką "czystkę",

lepiej:

- zawęzić zakres,
- zabezpieczyć zachowanie,
- zrobić małą poprawkę,
- sprawdzić efekt,
- dopiero iść dalej.

## Refaktoryzacja a bugfix

To ważne rozróżnienie.

### Bugfix

Zmienia zachowanie, bo chcesz naprawić błąd.

### Refaktoryzacja

Zmieniasz strukturę kodu bez zmiany oczekiwanego zachowania.

W praktyce często te rzeczy się mieszają, ale dobrze wiedzieć, kiedy robisz co.

## Jak podchodzić do starego modułu

Bardzo praktyczna ścieżka:

1. zrozum odpowiedzialność modułu,
2. odtwórz obecne zachowanie,
3. znajdź najbezpieczniejszy punkt wejścia do zmiany,
4. zrób mały krok,
5. sprawdź, czy nic nie pękło.

## Największe ryzyko w starym kodzie

Nie to, że kod jest brzydki.

Największe ryzyko to:

- ukryte zależności,
- nieoczywiste efekty uboczne,
- brak testów,
- niejawne sprzężenia,
- założenia, których nikt już nie pamięta.

Dlatego trzeba szanować stary kod nawet wtedy, gdy wygląda źle.

## Co poprawiać najpierw

Najbezpieczniej zwykle zaczynać od:

- poprawy nazw,
- wydzielania małych funkcji,
- usuwania duplikacji,
- izolowania efektów ubocznych,
- dokładania testów wokół zachowania,
- małych uproszczeń przepływu.

To często daje dużo czytelności przy relatywnie małym ryzyku.

## Czego nie robić od razu

Nie zaczynaj od:

- wielkiego przepisywania wszystkiego,
- zmian architektury bez zabezpieczenia zachowania,
- mieszania wielu celów w jednym kroku,
- porządków estetycznych bez zrozumienia przepływu.

To prosta droga do regresji.

## Mini case study

Masz funkcję 150-liniową, która:

- waliduje dane,
- liczy wynik,
- zapisuje do bazy,
- loguje,
- obsługuje wyjątki.

Zły plan:

- przepiszę ją całą od nowa, będzie piękniej.

Lepszy plan:

1. ustal obecne zachowanie,
2. wyodrębnij jedną małą część,
3. zachowaj wynik,
4. sprawdź, czy nic się nie zmieniło,
5. powtórz dla kolejnego małego kroku.

## Refaktoryzacja a zaufanie do systemu

W starym repo bardzo ważne jest budowanie zaufania do zmian.

To oznacza, że dobra refaktoryzacja powinna być:

- mała,
- czytelna,
- łatwa do review,
- łatwa do cofnięcia,
- mało ryzykowna.

To dużo ważniejsze niż imponujący rozmiar zmiany.

## Typowe błędy początkujących

- zbyt duży zakres jednej zmiany,
- refaktoryzacja bez zrozumienia zachowania,
- mieszanie clean-upu z naprawą błędu i zmianą funkcjonalną naraz,
- brak kontroli nad efektami ubocznymi,
- próba "uratowania całego modułu" w jednym PR-ze.

## Szybka ściąga

- stare repo wymaga ostrożniejszej refaktoryzacji,
- małe kroki są bezpieczniejsze niż wielkie przepisywanie,
- najpierw zrozum, potem zmieniaj,
- izoluj zachowanie i efekty uboczne,
- refaktoryzacja ma zwiększać bezpieczeństwo zmian, a nie tylko estetykę kodu.

## Ćwiczenia

1. Weź chaotyczną funkcję i zaproponuj plan 3 małych kroków refaktoryzacji.
2. Wskaż, co byłoby ryzykowne w dużym jednorazowym przepisaniu modułu.
3. Rozdziel działania: bugfix vs refaktoryzacja.
4. Zrób checklistę bezpiecznej zmiany w starym kodzie.
5. Opisz przypadek, gdzie poprawa nazewnictwa już daje dużą wartość bez dużego ryzyka.

## Najważniejsze do zapamiętania

- Refaktoryzacja starego repo wymaga pokory i małych kroków.
- Największe ryzyko siedzi w ukrytych zależnościach i efektach ubocznych.
- Nie trzeba ratować całego modułu naraz.
- Dobra zmiana jest mała, czytelna i bezpieczna.
- W starym kodzie bardziej liczy się kontrola ryzyka niż spektakularność refaktoryzacji.
