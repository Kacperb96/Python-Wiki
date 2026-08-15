# 10. Testowanie

To jest jeden z najważniejszych działów całego kompendium.

W pewnym momencie nauki programowania samo "umiem napisać kod" przestaje wystarczać.

Zaczynają się dużo ważniejsze pytania:

- skąd mam wiedzieć, że kod naprawdę działa,
- jak bezpiecznie coś refaktorować,
- jak nie psuć starych funkcji przy dodawaniu nowych,
- jak testować przypadki błędne,
- jak oddzielić logikę od zależności zewnętrznych,
- jak mierzyć jakość testów,
- jak pisać testy, które pomagają, a nie tylko istnieją.

Właśnie na te pytania odpowiada ten folder.

---

## Co powinieneś rozumieć po tym dziale

Po przejściu całego folderu powinieneś rozumieć:

- czym jest test i po co się go pisze,
- czym różnią się testy jednostkowe od integracyjnych,
- jak pisać testy w `pytest`,
- jak używać asercji, fixture'ów i parametryzacji,
- jak organizować katalog testów,
- jak mockować zależności przez `unittest.mock`,
- czym jest `coverage` i jak czytać raport pokrycia,
- czym są testy property-based i jak działa `hypothesis`,
- jakie testy dają realną wartość, a jakie tylko sztucznie podbijają statystyki.

---

## Dlaczego ten dział jest tak ważny

Testowanie nie jest dodatkiem dla dużych firm.

To codzienne narzędzie pracy programisty.

Testy pomagają Ci:

- szybciej znajdować błędy,
- bezpieczniej rozwijać projekt,
- refaktoryzować bez strachu,
- lepiej projektować API funkcji i klas,
- unikać regresji,
- rozumieć własny kod po czasie.

Bardzo często dobrze napisany test mówi o zachowaniu funkcji równie dużo jak sama implementacja.

---

## Jak czytać ten dział

Najlepiej iść dokładnie po kolei:

1. [01-testowanie-podstawy-pytest-python.md](/home/kacper/Desktop/Python_naprawiony/10.%20Testowanie/01-testowanie-podstawy-pytest-python.md)
2. [02-pytest-zaawansowane-python.md](/home/kacper/Desktop/Python_naprawiony/10.%20Testowanie/02-pytest-zaawansowane-python.md)
3. [03-mocking-python-unittest-mock.md](/home/kacper/Desktop/Python_naprawiony/10.%20Testowanie/03-mocking-python-unittest-mock.md)
4. [04-coverage-py-python.md](/home/kacper/Desktop/Python_naprawiony/10.%20Testowanie/04-coverage-py-python.md)
5. [05-testy-oparte-na-wlasciwosciach-hypothesis-python.md](/home/kacper/Desktop/Python_naprawiony/10.%20Testowanie/05-testy-oparte-na-wlasciwosciach-hypothesis-python.md)

Ta kolejność ma sens:

- najpierw uczysz się pisać zwykłe testy,
- potem poznajesz wygodniejsze mechanizmy `pytest`,
- potem uczysz się izolować zależności przez mocki,
- potem mierzysz jakość pokrycia,
- a na końcu poznajesz bardziej zaawansowany styl testowania przez właściwości.

---

## Jak pracować z tym działem

Najlepszy sposób nauki:

1. przeczytaj jeden plik,
2. przepisz wszystkie przykłady,
3. uruchom je samodzielnie,
4. przewiduj output przed uruchomieniem,
5. napisz własne 2-3 warianty,
6. zrób ćwiczenia z tego zakresu,
7. dopiero potem przechodź dalej.

Testowania nie da się dobrze nauczyć samym czytaniem.

Tutaj bardzo ważna jest praktyka.

---

## Na co szczególnie uważać

W tym dziale początkujący najczęściej wpadają w te pułapki:

- piszą testy tylko dla "szczęśliwej ścieżki",
- nie testują wyjątków i błędnych danych,
- mylą test jednostkowy z integracyjnym,
- nadużywają mocków albo mockują nie to miejsce, co trzeba,
- skupiają się na procencie coverage zamiast na sensie testów,
- piszą testy zbyt mocno związane z implementacją,
- traktują test jako formalność zamiast narzędzia do kontroli jakości.

---

## Po czym poznać, że temat zaczyna siedzieć

Dobry znak, jeśli potrafisz:

- napisać prosty test bez zaglądania do notatek,
- uruchomić `pytest` i zrozumieć raport błędu,
- użyć fixture i parametryzacji,
- napisać test sprawdzający wyjątek,
- zamockować zewnętrzną zależność,
- wyjaśnić, czemu wysoki coverage nie musi oznaczać dobrych testów,
- wskazać choć jedną sensowną właściwość do testu `hypothesis`.

---

## Co ten dział daje w praktyce

Po dobrym opanowaniu tego folderu będziesz pisał kod dojrzalej.

Nie tylko dlatego, że "umiesz testy", ale dlatego, że:

- zaczynasz projektować funkcje łatwiejsze do sprawdzenia,
- lepiej oddzielasz logikę od efektów ubocznych,
- myślisz o edge case'ach,
- szybciej zauważasz, gdzie kod jest zbyt ciasno powiązany,
- zaczynasz budować projekty, które łatwiej utrzymać.

To jeden z tych działów, które bardzo mocno podnoszą poziom programisty.

---

## Jak korzystać z ćwiczeń

Plik [ZESTAW-CWICZEN.md](/home/kacper/Desktop/Python_naprawiony/10.%20Testowanie/ZESTAW-CWICZEN.md) jest ułożony warstwowo.

Najlepiej:

- najpierw zrób poziom 1 i 2,
- potem wróć do praktycznych przykładów z plików,
- dopiero później wchodź w mocking, coverage i `hypothesis`.

Nie próbuj robić wszystkiego naraz.

W testowaniu bardzo ważne jest, żeby rozumieć po co używasz danego narzędzia.

---

## Jeśli opanujesz ten dział solidnie

Będziesz umiał:

- budować podstawowy pakiet testów dla małego projektu,
- pisać testy jednostkowe i prostsze integracyjne,
- wykrywać regresje po zmianach,
- sensownie używać `pytest`,
- czytać błędy testów bez paniki,
- budować dużo pewniejsze projekty niż osoba, która tylko "ręcznie klika i sprawdza".

---

## Co dalej

Po tym dziale naturalnym następnym krokiem jest:

- [11. Narzędzie profesjonalisty](/home/kacper/Desktop/Python_naprawiony/11.%20Narz%C4%99dzie%20profesjonalisty)
- albo [12. Asynchroniczność i wielowątkowość](/home/kacper/Desktop/Python_naprawiony/12.%20Asynchroniczno%C5%9B%C4%87%20i%20wielow%C4%85tkowo%C5%9B%C4%87)

Ale dopiero wtedy, gdy podstawy testowania są już naprawdę pewne.
