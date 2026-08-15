# Strategie debugowania w Pythonie

## O co chodzi

Debugowanie to nie jest seria losowych ruchów.

To proces zawężania problemu.

Najgorszy możliwy styl wygląda tak:

- może to to,
- może tamto,
- dorzucę print,
- zmienię coś jeszcze,
- zobaczmy co się stanie.

To męczące i często nieskuteczne.

Lepsze debugowanie jest bardziej metodyczne.

## Najważniejsza zasada

Najpierw zrozum objaw. Potem zawężaj przyczynę.

To bardzo ważne, bo objaw i przyczyna to nie to samo.

### Objaw

- wyjątek,
- zły wynik,
- brak odpowiedzi,
- wolne działanie,
- niepoprawny stan danych.

### Przyczyna

- rzeczywisty fragment logiki albo przepływu, który ten objaw powoduje.

## Podstawowy proces debugowania

Bardzo praktyczny schemat:

1. odtwórz problem,
2. ustal warunki wystąpienia,
3. zawęź obszar,
4. postaw hipotezę,
5. sprawdź hipotezę,
6. popraw minimalnie,
7. zweryfikuj poprawkę.

To wygląda prosto, ale bardzo porządkuje pracę.

## Odtworzenie problemu

Jeśli nie umiesz odtworzyć błędu, debugowanie robi się dużo trudniejsze.

Dlatego jedno z pierwszych pytań brzmi:

- co dokładnie trzeba zrobić, żeby problem wystąpił?

Im bardziej precyzyjna reprodukcja, tym lepiej.

## Zawężanie problemu

Bardzo ważne pytania:

- czy problem występuje zawsze czy tylko czasami,
- czy dotyczy konkretnego wejścia,
- czy dotyczy jednego środowiska,
- czy pojawił się po ostatniej zmianie,
- czy siedzi przy wejściu danych, w logice, czy na wyjściu.

Im szybciej zawęzisz, tym mniej błądzisz.

## Hipotezy zamiast zgadywania

Dobre debugowanie to nie losowanie. To tworzenie hipotez.

Przykład:

- hipoteza: błąd jest w parsowaniu daty,
- sprawdzenie: loguję wejście i wynik parsera,
- wynik: parser działa dobrze,
- wniosek: szukam dalej.

To dużo lepsze niż przypadkowe edytowanie kodu.

## Print debugging vs debugger

Printy bywają użyteczne, ale tylko wtedy, gdy używasz ich świadomie.

Dobre printy/logi pomagają odpowiedzieć na konkretne pytanie, np.:

- jaka wartość wchodzi,
- jaka wartość wychodzi,
- który warunek został spełniony,
- ile razy coś się wykonało.

Zły styl to zasypanie kodu przypadkowymi printami bez planu.

## Zawężanie przez podział

To bardzo silna technika.

Zamiast patrzeć na cały system naraz, pytaj:

- czy problem jest przed tym miejscem czy po nim,
- czy dane są poprawne tutaj czy psują się później,
- czy wyjątek rodzi się w tej warstwie, czy jest tylko objawem głębszego problemu.

To prawie jak binarne zawężanie obszaru błędu.

## Debugowanie przez uproszczenie

Jeśli system jest duży, często bardzo pomaga:

- odciąć niepotrzebne zależności,
- uprościć wejście,
- zbudować mniejszy przypadek,
- wywalić wszystko, co nie wpływa na problem.

To prowadzi naturalnie do minimal reproducible example.

## Mini case study

Bug: endpoint zwraca złą sumę zamówienia.

Chaotyczny styl:

- poprawiam wzór,
- zmieniam rounding,
- może to podatki,
- może baza.

Lepszy styl:

1. odtwórz konkretny request,
2. sprawdź wejściowe dane,
3. sprawdź wynik każdej części obliczeń,
4. zawęź, od którego kroku suma robi się zła,
5. dopiero popraw.

## Typowe błędy początkujących

- debugowanie bez reprodukcji,
- zmienianie kilku rzeczy naraz,
- brak rozdzielenia objawu od przyczyny,
- zbyt szybkie założenie, gdzie siedzi problem,
- brak weryfikacji hipotezy.

## Szybka ściąga

- debugowanie to zawężanie problemu,
- najpierw reprodukcja, potem hipoteza,
- poprawiaj jedną rzecz naraz,
- myśl w kategoriach przepływu danych i punktów decyzji,
- po poprawce zawsze sprawdź, czy naprawdę usunąłeś przyczynę.

## Ćwiczenia

1. Rozpisz proces debugowania prostego błędu krok po kroku.
2. Podaj przykład objawu i możliwej przyczyny.
3. Zbuduj plan zawężania problemu w większym module.
4. Wskaż różnicę między hipotezą a zgadywaniem.
5. Opisz, jakie printy lub logi dodałbyś do konkretnego problemu.

## Najważniejsze do zapamiętania

- Dobre debugowanie jest metodyczne.
- Najpierw trzeba odtworzyć problem.
- Objaw i przyczyna to nie to samo.
- Hipotezy trzeba sprawdzać, nie tylko wymyślać.
- Najskuteczniejsze debugowanie bardzo często polega na zawężaniu obszaru błędu.
