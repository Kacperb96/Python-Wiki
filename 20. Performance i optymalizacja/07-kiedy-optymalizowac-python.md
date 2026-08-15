# Kiedy optymalizować w Pythonie

## O co chodzi

To jest prawdopodobnie najważniejszy plik całego folderu.

Bo performance to nie tylko pytanie:

- jak przyspieszyć kod,

ale też:

- kiedy w ogóle warto to robić,
- co optymalizować najpierw,
- kiedy koszt komplikacji jest większy niż zysk.

## Najważniejsza zasada

Nie optymalizuj tylko dlatego, że "może kiedyś będzie wolno".

Optymalizuj wtedy, gdy:

- masz realny problem,
- masz pomiar,
- rozumiesz źródło kosztu,
- zysk jest wart ceny w złożoności.

## Przedwczesna optymalizacja

To klasyczny problem.

Programista zaczyna:

- komplikować kod,
- dodawać cache,
- przebudowywać architekturę,
- zmieniać strukturę danych,
- robić sprytne konstrukcje,

zanim jeszcze wie, czy to w ogóle jest potrzebne.

To zwykle zły kierunek.

## Kiedy jeszcze nie optymalizować

Bardzo często nie warto optymalizować, gdy:

- nie ma realnego bottlenecku,
- kod jest mały i prosty,
- problem jest tylko hipotetyczny,
- nie masz jeszcze pomiarów,
- architektura i funkcjonalność nie są ustabilizowane.

Na wczesnym etapie projektu czytelność i poprawność zwykle są ważniejsze niż sprytna szybkość.

## Kiedy optymalizacja ma sens

Optymalizuj, gdy:

- użytkownik realnie odczuwa problem,
- worker nie wyrabia,
- API ma zbyt duże opóźnienia,
- batch trwa nieakceptowalnie długo,
- pamięć rośnie za mocno,
- profilowanie pokazało wyraźny hot spot,
- wiesz, że poprawka da realny efekt.

## Kolejność myślenia

Bardzo zdrowa ścieżka wygląda tak:

1. zauważ problem,
2. zmierz go,
3. sklasyfikuj: CPU, I/O, pamięć, algorytm,
4. znajdź hot spot,
5. wybierz najmądrzejszą poprawkę,
6. zmierz efekt po zmianie.

To znacznie lepsze niż "optymalizuję wszystko po trochu".

## Koszt optymalizacji

Każda optymalizacja ma cenę.

Może nią być:

- większa złożoność kodu,
- trudniejszy onboarding,
- gorsza czytelność,
- większa liczba edge case'ów,
- trudniejsze testowanie,
- większa zależność od konkretnego środowiska.

Dlatego trzeba umieć pytać:

- czy ten zysk jest wart tej ceny?

## Dobry performance engineering

To nie jest konkurs na najbardziej sprytny kod.

To raczej umiejętność wybierania takich poprawek, które:

- dają duży efekt,
- nie psują projektu,
- są uzasadnione pomiarem,
- są proporcjonalne do skali problemu.

## Mini case study 1

Masz funkcję wykonywaną raz dziennie przez 0.4 sekundy.

Ktoś chce ją przepisać na skomplikowany pipeline z cache i async.

To prawdopodobnie zła inwestycja czasu.

## Mini case study 2

Masz endpoint używany tysiące razy dziennie, który z powodu złego algorytmu wykonuje bardzo drogie wyszukiwanie w każdej prośbie.

To bardzo dobry kandydat do optymalizacji.

## Co optymalizować najpierw

Najlepiej:

- największe hot spoty,
- najdroższe operacje,
- najbardziej odczuwalne wąskie gardła,
- błędy algorytmiczne,
- złą strukturę danych,
- niepotrzebne I/O.

Nie zaczynaj od kosmetycznych rzeczy, które nic nie zmienią dla użytkownika ani systemu.

## Typowe błędy początkujących

- optymalizowanie bez pomiaru,
- optymalizowanie zbyt wcześnie,
- poprawianie najmniej istotnego fragmentu,
- psucie czytelności dla marginalnego zysku,
- ignorowanie ceny utrzymania bardziej skomplikowanego kodu.

## Szybka ściąga

- nie każda wolna rzecz wymaga optymalizacji,
- najpierw mierz, potem działaj,
- wybieraj poprawki o dużym wpływie,
- pamiętaj o koszcie złożoności,
- czytelny kod bez realnego problemu często jest lepszy niż przekombinowany "szybszy" kod.

## Ćwiczenia

1. Podaj 3 przypadki, kiedy nie warto jeszcze optymalizować.
2. Podaj 3 przypadki, kiedy optymalizacja jest bardzo sensowna.
3. Opisz koszt utrzymania zbyt sprytnego kodu.
4. Rozpisz workflow optymalizacji od pomiaru do wyniku.
5. Zrób checklistę: czy ten problem naprawdę warto optymalizować teraz?

## Najważniejsze do zapamiętania

- Najważniejsze pytanie w performance to nie tylko „jak?”, ale też „czy już?”
- Optymalizacja ma sens wtedy, gdy problem jest realny i zmierzony.
- Najlepsze poprawki są proporcjonalne do wagi problemu.
- Złożoność kodu też jest kosztem.
- Dobra optymalizacja to decyzja inżynierska, nie odruch.
