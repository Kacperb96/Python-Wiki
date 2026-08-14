# 05. Dekoratory

Ten dział prowadzi od fundamentu:

- funkcje jako obiekty,
- closures,
- wrappery,

do pełnego zrozumienia dekoratorów w praktyce.

Po przerobieniu tego folderu powinieneś rozumieć:

- dlaczego dekoratory w ogóle działają,
- czym różni się funkcja od wywołania funkcji,
- jak zbudować prosty dekorator,
- jak pisać dekoratory dla funkcji z argumentami,
- po co używa się `functools.wraps`,
- czym są dekoratory klasowe,
- gdzie dekoratory pojawiają się w prawdziwych projektach.

## Po co w ogóle ten dział

Dekoratory to jeden z najbardziej charakterystycznych mechanizmów Pythona.

Na początku często wyglądają jak magia, ale w praktyce składają się z kilku prostych elementów:

- funkcja może być wartością,
- funkcja może zwracać inną funkcję,
- funkcja wewnętrzna może pamiętać stan z zewnątrz,
- składnia `@` to tylko wygodny skrót.

Jeśli zrozumiesz ten dział naprawdę dobrze, to później dużo łatwiej będzie Ci czytać:

- frameworki webowe,
- kod testów,
- biblioteki z cache, logowaniem i walidacją,
- bardziej zaawansowany kod Pythona.

## Jak czytać ten dział

Najlepiej iść dokładnie po kolei:

1. `01-funkcje-jako-obiekty-python.md`
2. `02-closures-python.md`
3. `03-prosty-dekorator-python.md`
4. `04-dekoratory-z-argumentami-python.md`
5. `05-functools-wraps-python.md`
6. `06-wbudowane-dekoratory-python.md`
7. `07-dekoratory-klasowe-python.md`
8. `08-dekoratory-od-prostych-po-zaawansowane-python.md`
9. `09-dekoratory-we-frameworkach-python.md`

To jest dział warstwowy.

Jeśli przeskoczysz od razu do trudniejszych dekoratorów bez opanowania funkcji jako obiektów i closures, to wszystko zacznie wyglądać nienaturalnie.

## Na co szczególnie uważać

Najczęstsze pułapki w tym temacie:

- mylenie `funkcja` z `funkcja()`,
- brak zrozumienia, że dekorator zwraca nową funkcję,
- gubienie `return` w wrapperze,
- brak `*args, **kwargs`,
- brak `@wraps`,
- zbyt szybkie przechodzenie do dekoratorów z argumentami.

Jeśli któryś dekorator wydaje się nieintuicyjny, wróć krok wcześniej:

- do funkcji jako obiektów,
- do closures,
- do ręcznego przypisania `f = dekorator(f)`.

## Po czym poznać, że temat zaczyna siedzieć

Dobry znak, jeśli potrafisz bez patrzenia:

- wyjaśnić, czemu `@dekorator` to skrót dla przypisania funkcji,
- napisać prosty dekorator z wrapperem,
- dodać do niego `*args, **kwargs`,
- zachować wynik oryginalnej funkcji,
- użyć `@wraps`,
- wytłumaczyć, czemu closure jest tu potrzebne.

Jeszcze lepszy znak:

potrafisz samodzielnie napisać dekorator do:

- logowania,
- walidacji,
- prostego cache,
- liczenia wywołań,
- kontroli dostępu.

## Jak najlepiej ćwiczyć

Najlepsza metoda w tym dziale:

1. najpierw uruchom przykład bez dekoratora,
2. potem ręcznie zrób `funkcja = dekorator(funkcja)`,
3. dopiero potem użyj składni `@`,
4. na końcu dopisz `*args, **kwargs` i `@wraps`.

To bardzo pomaga zrozumieć, co tak naprawdę dzieje się pod spodem.

## Uczciwa ocena startowa tego folderu

Na ten moment ten folder ma dobry temat i sensowny układ, ale jest jeszcze wyraźnie słabszy od dopracowanych folderów `01-04`.

Najbardziej brakuje tu:

- mocniejszego `README`,
- większego zestawu ćwiczeń,
- większej liczby przykładów z outputem w części plików,
- bardziej rozbudowanych mini-scenariuszy praktycznych.

To jest dobry fundament, ale jeszcze nie poziom `10/10`.

Co dalej:

- po dopracowaniu tego działu można przejść do `06. Zaawansowane elementy`,
- albo wrócić do praktyki i zrobić większy zestaw ćwiczeń z dekoratorów.
