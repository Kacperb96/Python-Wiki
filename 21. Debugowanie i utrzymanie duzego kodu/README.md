# 21. Debugowanie i utrzymanie dużego kodu

To jest folder o jednej z najważniejszych umiejętności prawdziwego programisty: nie tylko pisać nowy kod, ale też rozumieć, diagnozować i poprawiać kod, który już istnieje.

Bardzo wielu ludzi czuje się pewnie, gdy piszą coś od zera. Znacznie trudniej robi się wtedy, gdy:

- repo ma tysiące linii,
- kod pisał ktoś inny,
- bug pojawia się tylko czasami,
- traceback wygląda chaotycznie,
- nie wiadomo, od czego zacząć,
- poprawka musi być bezpieczna i mała.

Właśnie tym zajmuje się ten folder.

## Po co ten dział

W prawdziwej pracy bardzo dużo czasu spędza się nie na tworzeniu zupełnie nowych modułów, tylko na:

- czytaniu cudzego kodu,
- diagnozowaniu błędów,
- szukaniu regresji,
- analizie logów,
- poprawianiu starego systemu,
- robieniu zmian bez rozwalania całości.

To nie jest dodatek do programowania. To jest rdzeń codziennej praktyki.

## Czego nauczysz się w tym module

Po przerobieniu tego folderu powinieneś umieć:

- sensownie wejść w obce repo,
- nie tonąć od razu w zbyt dużej ilości kodu,
- debugować metodycznie zamiast zgadywać,
- robić minimal reproducible example,
- czytać tracebacki jak mapę problemu,
- rozumieć regresje i zawężać moment, kiedy bug się pojawił,
- używać logów i metryk do diagnozy,
- bezpieczniej refaktoryzować stary kod.

Dodatkowo masz teraz też przekrojowy plik:

- `08-debugging-walkthrough-python.md`

który prowadzi przez pełny proces debugowania od objawu do poprawki.

## Najważniejsza zasada tego folderu

Nie zgaduj. Zawężaj problem.

To jest jedna z najważniejszych zasad debugowania.

Bardzo wiele osób debuguje tak:

- zmienię coś na ślepo,
- może pomoże,
- jeszcze jeden print,
- może to to,
- a może tamto.

To jest kosztowne i często chaotyczne.

Lepsze podejście to:

1. zrozumieć objaw,
2. odtworzyć problem,
3. zawęzić źródło,
4. potwierdzić hipotezę,
5. dopiero potem poprawiać.

## Jak czytać ten folder

Najlepiej iść po kolei:

1. `01-czytanie-cudzego-kodu-python.md`
2. `02-strategie-debugowania-python.md`
3. `03-minimal-reproducible-example-python.md`
4. `04-analiza-tracebackow-python.md`
5. `05-regresje-i-git-bisect-python.md`
6. `06-logi-metryki-i-diagnoza-python.md`
7. `07-refaktoryzacja-w-starym-repo-python.md`
8. `08-debugging-walkthrough-python.md`

Ta kolejność ma sens, bo najpierw uczysz się wejścia w duży kod i myślenia debugerskiego, potem zawężania i czytania śladów błędu, a na końcu bardziej operacyjnego utrzymania starego systemu oraz pełnego przejścia przez case debuggingowy.

## Najczęstsze błędy początkujących

- czytanie całego repo od początku do końca bez planu,
- poprawianie bez pełnego zrozumienia objawu,
- zgadywanie zamiast odtwarzania błędu,
- ignorowanie tracebacka,
- brak minimalnego przykładu,
- zbyt duże refaktoryzacje przy małej poprawce,
- brak rozdzielenia objawu od przyczyny.

## Jak najlepiej ćwiczyć

Ten folder najlepiej ćwiczyć na prawdziwych lub półprawdziwych przypadkach:

- błędny moduł,
- wyjątek z tracebackiem,
- regresja po zmianie,
- chaotyczna funkcja do poprawy,
- dziwny bug w większym przepływie.

Nie chodzi o samo „wiedzieć co to jest traceback”. Chodzi o to, żeby umieć go użyć jako narzędzie pracy.

## Po czym poznasz, że temat siedzi

Dobry znak, jeśli potrafisz:

- wejść w obcy kod i znaleźć ważne miejsca bez paniki,
- odróżnić objaw od źródła problemu,
- stworzyć mały reprodukowalny przypadek,
- przeczytać traceback i wskazać sensowny punkt startu,
- zawęzić regresję do konkretnej zmiany,
- zrobić poprawkę w starym kodzie bez rozwalania połowy systemu,
- przejść przez pełny debugging walkthrough z głowy.

## Podsumowanie

To jest folder, który bardzo mocno zbliża Cię do poziomu prawdziwej pracy programistycznej. Pisanie kodu od zera jest ważne, ale umiejętność debugowania, rozumienia cudzego kodu i bezpiecznego utrzymania dużego repo jest tym, co naprawdę robi z kogoś mocnego developera.
