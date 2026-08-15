# 15. Architektura i jakość kodu

To jest dział o tym, jak zbudować kod, który nie tylko działa dziś, ale daje się rozwijać, testować i utrzymywać przez długi czas.

Na wcześniejszych etapach najważniejsze było to, żeby kod był poprawny.

Tutaj wchodzimy poziom wyżej.

Zaczynają się pytania:

- czy ten kod da się bezpiecznie zmienić za miesiąc,
- czy wiadomo, gdzie jest logika biznesowa,
- czy zależności są jawne,
- czy projekt nie rozlewa odpowiedzialności po przypadkowych miejscach,
- czy struktura pomaga zespołowi, czy przeszkadza.

To właśnie jest dział o dojrzalszym myśleniu programistycznym.

---

## Co powinieneś rozumieć po tym dziale

Po przerobieniu całego folderu powinieneś rozumieć:

- czym są code smells,
- czym jest refaktoryzacja i jak robić ją bezpiecznie,
- czym jest architektura warstwowa,
- po co separować logikę biznesową,
- czym jest dependency injection poza frameworkami,
- jak praktycznie rozumieć SOLID w Pythonie,
- kiedy wzorce projektowe pomagają, a kiedy tylko komplikują kod.

---

## Dlaczego ten dział jest ważny

Im większy projekt, tym mniej liczy się samo „działa”, a bardziej:

- czy można coś zmienić bez rozwalenia reszty,
- czy nowa osoba rozumie strukturę projektu,
- czy testy da się pisać bez walki z infrastrukturą,
- czy odpowiedzialności są rozdzielone sensownie,
- czy architektura pomaga, a nie tylko dobrze brzmi.

To właśnie w tym dziale zaczynasz przechodzić od pisania kodu do świadomego projektowania kodu.

---

## Jak czytać ten dział

Najlepiej iść po kolei:

1. [01-code-smells-python.md](/home/kacper/Desktop/Python_naprawiony/15.%20Architektura%20i%20jako%C5%9B%C4%87%20kodu/01-code-smells-python.md)
2. [02-refaktoryzacja-python.md](/home/kacper/Desktop/Python_naprawiony/15.%20Architektura%20i%20jako%C5%9B%C4%87%20kodu/02-refaktoryzacja-python.md)
3. [03-architektura-warstwowa-python.md](/home/kacper/Desktop/Python_naprawiony/15.%20Architektura%20i%20jako%C5%9B%C4%87%20kodu/03-architektura-warstwowa-python.md)
4. [04-separacja-logiki-biznesowej-python.md](/home/kacper/Desktop/Python_naprawiony/15.%20Architektura%20i%20jako%C5%9B%C4%87%20kodu/04-separacja-logiki-biznesowej-python.md)
5. [05-dependency-injection-python.md](/home/kacper/Desktop/Python_naprawiony/15.%20Architektura%20i%20jako%C5%9B%C4%87%20kodu/05-dependency-injection-python.md)
6. [06-solid-w-pythonie.md](/home/kacper/Desktop/Python_naprawiony/15.%20Architektura%20i%20jako%C5%9B%C4%87%20kodu/06-solid-w-pythonie.md)
7. [07-wzorce-projektowe-python.md](/home/kacper/Desktop/Python_naprawiony/15.%20Architektura%20i%20jako%C5%9B%C4%87%20kodu/07-wzorce-projektowe-python.md)

Ta kolejność ma sens, bo:

- najpierw uczysz się widzieć problemy,
- potem uczysz się bezpiecznie je poprawiać,
- potem przechodzisz do większej struktury systemu,
- a na końcu do bardziej formalnych zasad i wzorców.

---

## Jak pracować z tym działem

Najlepszy sposób nauki:

1. czytaj jeden plik,
2. od razu myśl o własnym kodzie albo wcześniej napisanych folderach,
3. szukaj przykładów problemów i lepszych rozwiązań,
4. rób małe refaktoryzacje zamiast wielkich przepisań,
5. dopiero potem przechodź do ćwiczeń.

To dział, który bardzo zyskuje, kiedy patrzysz na realny kod, a nie tylko na teorię.

---

## Na co szczególnie uważać

Najczęstsze pułapki:

- traktowanie architektury jak zbioru modnych słów,
- przesadne mnożenie warstw i abstrakcji,
- kopiowanie wzorców z innych języków bez dopasowania do Pythona,
- próba „naprawy wszystkiego naraz”,
- mylenie porządnej struktury z ceremonialnością.

---

## Po czym poznać, że temat zaczyna siedzieć

Dobry znak, jeśli potrafisz:

- wskazać code smell i wyjaśnić, czemu jest groźny,
- zaplanować małą refaktoryzację bez zmiany zachowania,
- rozdzielić warstwę HTTP, biznesową i danych,
- powiedzieć, gdzie naprawdę znajduje się logika biznesowa,
- pokazać różnicę między jawną a ukrytą zależnością,
- potraktować SOLID jako narzędzie myślenia, a nie checklistę,
- dobrać prosty wzorzec wtedy, gdy rozwiązuje realny problem.

---

## Co ten dział daje w praktyce

Po opanowaniu tego folderu dużo lepiej poradzisz sobie z:

- porządkowaniem starszego kodu,
- rozwojem większych projektów,
- pisaniem kodu łatwiejszego do testowania,
- czytaniem bardziej dojrzałych repozytoriów,
- unikaniem chaosu architektonicznego.

To jest dział, który mocno odróżnia „pisanie kodu” od „budowania systemu”.

---

## Ćwiczenia

Do tego działu masz też [ZESTAW-CWICZEN.md](/home/kacper/Desktop/Python_naprawiony/15.%20Architektura%20i%20jako%C5%9B%C4%87%20kodu/ZESTAW-CWICZEN.md).

Najlepiej:

- najpierw robić code smells i refaktoryzację,
- potem warstwy, logikę biznesową i DI,
- a dopiero na końcu SOLID i wzorce.

---

## Co dalej

Po tym dziale naturalny następny krok to:

- [16. Bezpieczeństwo](/home/kacper/Desktop/Python_naprawiony/16.%20Bezpiecze%C5%84stwo)

A potem warto wrócić do wcześniejszych działów i spojrzeć na nie już z perspektywy architektury i jakości kodu.
