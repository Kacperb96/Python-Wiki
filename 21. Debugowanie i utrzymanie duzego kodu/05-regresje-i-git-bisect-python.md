# Regresje i `git bisect` w Pythonie

## O co chodzi

Regresja to sytuacja, w której coś działało wcześniej, a po zmianie przestało działać albo działa gorzej.

To bardzo częsty typ problemu w prawdziwych projektach.

Nie piszesz nowej funkcji od zera, tylko próbujesz odpowiedzieć na pytanie:

- która zmiana to zepsuła?

I właśnie tu bardzo przydaje się myślenie o regresji oraz narzędzie takie jak `git bisect`.

## Czym jest regresja

To nie tylko wyjątek po deployu.

Regresją może być:

- błąd funkcjonalny,
- spadek wydajności,
- zmiana zachowania API,
- popsuty edge case,
- zniknięcie wcześniejszej poprawki,
- zepsucie testu, który wcześniej przechodził.

## Najważniejsza intuicja

Jeśli wiesz, że kiedyś było dobrze, a teraz jest źle, to problem leży gdzieś między tymi punktami historii.

To ogromnie pomaga, bo zamiast patrzeć na cały świat, możesz zawęzić zakres zmian.

## Pytania, które warto zadać przy regresji

- kiedy ostatnio działało,
- kiedy pierwszy raz przestało działać,
- czy są testy pokazujące różnicę,
- czy błąd dotyczy jednej ścieżki czy wielu,
- czy problem jest funkcjonalny, wydajnościowy czy środowiskowy.

## Jak myśleć o zawężaniu regresji

Masz historię zmian.

Jeśli umiesz wskazać:

- jeden commit dobry,
- jeden commit zły,

to możesz zawężać problem dużo szybciej niż ręcznym losowym przeglądaniem historii.

## `git bisect` — intuicja

`git bisect` działa jak binarne zawężanie.

Zamiast sprawdzać commit po commicie liniowo, narzędzie pomaga skakać po historii tak, żeby szybciej dojść do zmiany wprowadzającej problem.

To bardzo praktyczne, gdy historia jest duża.

## Kiedy `git bisect` ma sens

Szczególnie gdy:

- masz regresję,
- potrafisz określić stan dobry i zły,
- błąd da się odtworzyć albo przetestować,
- historia jest zbyt długa na ręczne zgadywanie.

## Regresja a test reprodukujący

To bardzo ważne połączenie.

Jeśli masz:

- test albo prosty sposób sprawdzania,

zawężanie regresji staje się dużo łatwiejsze i bardziej obiektywne.

Bez tego nadal się da pracować, ale koszt rośnie.

## Mini case study

Masz endpoint, który jeszcze tydzień temu zwracał poprawny format JSON, a dziś zwraca zły kształt pola.

Nie chcesz analizować 40 commitów ręcznie.

Lepszy plan:

1. znajdź ostatni dobry commit,
2. znajdź pierwszy zły stan,
3. odtwórz problem albo uruchom test,
4. zawężaj historię.

To jest dokładnie problem, do którego `git bisect` bardzo pasuje.

## Nie każda regresja jest wyłącznie kodowa

To ważne.

Czasem regresja wynika z:

- zmiany konfiguracji,
- zmiany środowiska,
- nowej wersji zależności,
- danych,
- innego systemu, z którym się integrujesz.

Ale nawet wtedy myślenie regresyjne nadal pomaga zawęzić moment, kiedy coś przestało być prawdą.

## Typowe błędy początkujących

- brak ustalenia ostatniego dobrego stanu,
- ręczne przeglądanie historii bez strategii,
- poprawianie objawu bez znalezienia zmiany źródłowej,
- brak testu lub prostego sposobu potwierdzania, czy commit jest dobry czy zły,
- zakładanie, że regresja musi wynikać tylko z jednego oczywistego pliku.

## Szybka ściąga

- regresja = coś działało, teraz nie działa,
- kluczowe są punkt dobry i punkt zły,
- `git bisect` pomaga zawężać binarnie historię,
- test albo jasna reprodukcja bardzo pomagają,
- regresje mogą dotyczyć funkcji, wydajności i zachowania systemu.

## Ćwiczenia

1. Opisz 3 przykłady regresji.
2. Rozpisz plan zawężenia regresji między dwoma stanami repo.
3. Wyjaśnij własnymi słowami, do czego służy `git bisect`.
4. Opisz, czemu test reprodukujący bardzo pomaga przy regresji.
5. Wymyśl przypadek regresji wydajnościowej, a nie funkcjonalnej.

## Najważniejsze do zapamiętania

- Regresja to bardzo częsty typ problemu w realnych projektach.
- Najważniejsze jest zawężenie: kiedy było dobrze, kiedy już było źle.
- `git bisect` bardzo pomaga przy długiej historii zmian.
- Reprodukcja problemu lub test są tu ogromnie ważne.
- Myślenie regresyjne oszczędza mnóstwo czasu w debugowaniu dużych repo.
