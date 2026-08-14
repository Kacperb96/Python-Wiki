# 03. Kolekcje

To jeden z najważniejszych działów całego kompendium.

Tutaj uczysz się pracować na danych, a to w Pythonie dzieje się praktycznie wszędzie:

- w prostych skryptach,
- w analizie danych,
- w backendzie,
- w automatyzacji,
- w testach,
- w programowaniu obiektowym,
- w pracy z plikami i API.

Po opanowaniu tego folderu powinieneś swobodnie rozumieć:

- kiedy użyć `list`, `tuple`, `dict` i `set`,
- czym różni się struktura mutowalna od niemutowalnej,
- jak działa kopiowanie danych i skąd biorą się błędy z referencjami,
- jak budować kolekcje przez comprehensions,
- kiedy generator expression jest lepszy od listy,
- jak działają protokoły kolekcji (`Iterable`, `Sequence`, `Mapping`),
- do czego służą `Counter`, `defaultdict`, `deque`, `ChainMap`, `namedtuple`,
- jak pisać własne kolekcje zachowujące się jak obiekty wbudowane.

## Jak czytać ten folder

Najlepiej iść po kolei:

1. `01-listy-...`
2. `02-tuple-...`
3. `03-dict-...`
4. `04-set-...`
5. `05-mutowalnosc-...`
6. `06-kopiowanie-...`
7. `07-comprehensions-...`
8. `08-zagniezdzone-comprehensions-...`
9. `09-generator-expressions-...`
10. `10-protokoly-kolekcji-...`
11. `11-counter-...`
12. `12-defaultdict-...`
13. `13-deque-...`
14. `14-chainmap-...`
15. `15-namedtuple-...`
16. `16-wlasne-kolekcje-...`

To nie jest przypadkowa kolejność.

Najpierw poznajesz podstawowe typy kolekcji, potem ich zachowanie, potem wygodne konstrukcje do pracy z danymi, a na końcu bardziej zaawansowane narzędzia i własne abstrakcje.

## Co trzeba opanować naprawdę dobrze

Jeśli chcesz mieć solidne podstawy, po tym folderze powinieneś bez zastanowienia umieć:

- dodać, usunąć, posortować i przefiltrować elementy listy,
- rozumieć różnicę między listą a tuple,
- używać słownika do modelowania danych nazwanych,
- używać zbiorów do usuwania duplikatów i porównań,
- wyjaśnić, co znaczy mutowalność,
- przewidzieć skutki płytkiej i głębokiej kopii,
- pisać list/dict/set comprehensions,
- odróżnić comprehension od generator expression,
- rozpoznać sytuacje, w których przyda się `Counter` albo `defaultdict`,
- użyć `deque` jako kolejki,
- wyjaśnić, czym jest `ChainMap`,
- czytać i tworzyć prosty `namedtuple`.

## Na co szczególnie uważać

W tym folderze jest kilka tematów, na których początkujący najczęściej się wykładają:

- mylenie przypisania z kopiowaniem,
- nieświadomość, że lista i słownik są mutowalne,
- zbyt mechaniczne używanie comprehension tam, gdzie zwykła pętla jest czytelniejsza,
- traktowanie generatora jak listy,
- niezrozumienie, że `defaultdict` może utworzyć klucz już przy samym odczycie,
- używanie `set`, jakby miał stabilną kolejność,
- brak rozróżnienia między “widokiem na dane” a “kopią danych”.

Jeśli te rzeczy rozumiesz, to jesteś już kawał dalej niż większość osób po pobieżnym kursie.

## Jak pracować z przykładami

Nie tylko czytaj kod.

Rób trzy rzeczy:

1. przepisz przykład i uruchom go sam,
2. spróbuj przewidzieć output zanim zobaczysz wynik,
3. zmień jedną rzecz i zobacz, co się stanie.

Na przykład:

- zmień kolejność słowników w `ChainMap`,
- zamień `list` na `tuple`,
- użyj zagnieżdżonej listy zamiast płaskiej,
- drugi raz przejdź po generatorze,
- skopiuj strukturę zagnieżdżoną na dwa sposoby.

Właśnie wtedy materiał naprawdę “wchodzi”.

## Jak poznać, że umiesz materiał

Możesz uznać folder `03` za dobrze opanowany, jeśli:

- samodzielnie rozwiązujesz ćwiczenia z `ZESTAW-CWICZEN.md`,
- potrafisz własnymi słowami wyjaśnić różnice między podstawowymi kolekcjami,
- nie gubisz się przy referencjach, mutowalności i kopiowaniu,
- wiesz, kiedy używać listy, a kiedy słownika lub zbioru,
- rozumiesz output przykładów bez zgadywania.

## Co dalej

Po tym folderze bardzo naturalny następny krok to:

- [04. Programowanie obiektowe](/home/kacper/Desktop/Python/04.%20Programowanie%20obiektowe)

Jeśli chcesz równolegle pisać praktyczne skrypty, możesz też zaglądać do:

- [07. Pliki i dane](/home/kacper/Desktop/Python/07.%20Pliki%20i%20dane)

Ale uczciwie: bez dobrego ogarnięcia kolekcji dalsze działy będą dużo trudniejsze.
