# 19. Runtime, pamięć i wnętrze Pythona

To jest jeden z tych folderów, które mocno zmieniają sposób myślenia o Pythonie.

Do tej pory wiele tematów w repo było skupionych na tym:

- jak pisać kod,
- jak organizować projekt,
- jak używać bibliotek,
- jak testować i budować aplikacje.

Tutaj przechodzimy poziom głębiej i zaczynamy pytać:

- co Python naprawdę robi pod maską,
- jak działają obiekty,
- skąd biorą się referencje i problemy z pamięcią,
- dlaczego istnieje GIL,
- jak działa import,
- czym jest bytecode,
- czym różni się CPython od PyPy.

To nie jest dział tylko dla ludzi lubiących teorię. To bardzo praktyczna wiedza, jeśli chcesz rozumieć wydajność, debugować dziwne zachowania i pisać dojrzalszy kod.

## Po co ten folder

W pewnym momencie zwykła znajomość składni przestaje wystarczać.

Zaczynasz wtedy zadawać pytania takie jak:

- czemu dwie zmienne wskazują na ten sam obiekt,
- czemu mutacja w jednym miejscu wpływa na drugie,
- czemu wielowątkowość CPU-bound nie działa tak, jak się spodziewałem,
- czemu import ma skutki uboczne,
- czemu ten kod zużywa tyle pamięci,
- co właściwie interpreter wykonuje.

Ten folder pomaga zbudować właśnie taką głębszą intuicję.

## Czego nauczysz się w tym module

Po przerobieniu tego działu powinieneś rozumieć:

- czym jest GIL i kiedy ma znaczenie,
- jak Python traktuje obiekty, nazwy i tożsamość,
- jak działają referencje i garbage collection,
- czym jest stos wywołań,
- jak działa system importów,
- czym różni się CPython od PyPy,
- czym jest bytecode i po co w ogóle o nim wiedzieć.

Dodatkowo masz teraz też przekrojowy plik:

- `08-runtime-case-studies-python.md`

który łączy te zagadnienia w konkretne, dziwne zachowania kodu wyjaśnione przez runtime.

## Najważniejsze nastawienie do tego działu

Nie chodzi o to, żeby po tym folderze zostać twórcą interpretera Pythona.

Chodzi o to, żebyś:

- lepiej rozumiał zachowanie kodu,
- unikał błędnych intuicji,
- lepiej diagnozował problemy,
- miał mocniejszy fundament do performance, debugowania i architektury.

## Jak czytać ten folder

Najlepiej iść po kolei:

1. `01-gil-python.md`
2. `02-model-obiektow-python.md`
3. `03-referencje-i-garbage-collection-python.md`
4. `04-stos-wyolan-python.md`
5. `05-import-system-python.md`
6. `06-cpython-vs-pypy-python.md`
7. `07-bytecode-python.md`
8. `08-runtime-case-studies-python.md`

Ta kolejność ma sens, bo najpierw budujesz model działania, a dopiero potem patrzysz na praktyczne case studies, które go spinają.

## Dlaczego ten dział jest ważny praktycznie

Ta wiedza pomaga bardzo konkretnie w takich rzeczach jak:

- rozumienie mutowalności i aliasowania,
- debugowanie problemów z pamięcią,
- dobór wątków vs procesów,
- rozumienie kosztu importów,
- diagnozowanie recursion errors,
- czytanie bardziej zaawansowanych komunikatów i zachowań runtime.

## Typowe błędy początkujących

Najczęstsze błędne intuicje to:

- mylenie nazwy zmiennej z obiektem,
- brak zrozumienia, że wiele nazw może wskazywać na ten sam obiekt,
- przekonanie, że GIL oznacza "Python nie ma wielowątkowości",
- brak świadomości, że import wykonuje kod modułu,
- traktowanie garbage collection jak magicznej czarnej skrzynki,
- brak zrozumienia, że CPython i PyPy to nie to samo.

## Jak najlepiej uczyć się tego folderu

Ten dział najlepiej czytać z nastawieniem:

1. zrozumieć intuicję,
2. zobaczyć prosty przykład,
3. porównać własne wcześniejsze wyobrażenie z rzeczywistym modelem,
4. dopiero potem przejść dalej.

Tutaj nie wygrywa ten, kto przeczyta najszybciej. Wygrywa ten, kto naprawdę zacznie widzieć, co dzieje się pod spodem.

## Po czym poznasz, że temat siedzi

Dobry znak, jeśli potrafisz:

- wyjaśnić, czym różni się nazwa od obiektu,
- rozumiesz, czemu aliasowanie i mutowalność czasem robią bałagan,
- potrafisz powiedzieć, kiedy GIL ma znaczenie,
- wiesz, że import nie jest tylko "wklejeniem pliku",
- rozumiesz, po co istnieje bytecode,
- potrafisz wytłumaczyć, czemu PyPy i CPython mogą zachowywać się inaczej wydajnościowo,
- wyjaśnić kilka dziwnych zachowań kodu bez odwoływania się do "magii Pythona".

## Podsumowanie

To jeden z tych folderów, które najmocniej budują głębię rozumienia Pythona. Po jego opanowaniu będziesz patrzył na wiele zjawisk dużo spokojniej i precyzyjniej, bo przestaną być "dziwną magią" interpretera.
