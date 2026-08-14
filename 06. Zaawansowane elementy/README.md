# 06. Zaawansowane elementy

To jest dział, w którym Python zaczyna być bardziej techniczny i bardziej „pod maską”.

Tutaj wchodzą tematy, które:

- nie zawsze są potrzebne pierwszego dnia,
- ale bardzo mocno pogłębiają rozumienie języka,
- sprawiają, że czytasz bardziej dojrzały kod dużo swobodniej.

Po przerobieniu tego folderu powinieneś rozumieć:

- iteratory i generatory,
- context managery,
- podstawy programowania funkcyjnego w Pythonie,
- deskryptory,
- `__slots__`,
- podstawy modelu pamięci CPythona.

## Po co w ogóle ten dział

Ten dział nie jest o „pisaniu większej liczby linijek”.

On jest o tym, żeby zacząć lepiej rozumieć:

- jak Python przetwarza dane,
- kiedy coś jest leniwe, a kiedy od razu liczone,
- jak zarządzać zasobami,
- jak działa bardziej zaawansowany model obiektów,
- czemu pewne konstrukcje są szybkie, eleganckie albo oszczędne pamięciowo.

To właśnie tutaj Python zaczyna wyglądać nie tylko jak prosty język do skryptów, ale jak bardzo przemyślany system.

## Jak czytać ten dział

Najlepiej iść w tej kolejności:

1. `01-iteratory-i-generatory-python.md`
2. `02-context-managers-python.md`
3. `03-programowanie-funkcyjne-python.md`
4. `04-deskriptory-python.md`
5. `05-slots-python.md`
6. `06-cpython-i-model-pamieci-python.md`

To dobra kolejność, bo:

- iteratory i generatory uczą pracy „po elemencie”,
- context managery uczą kontrolowania zasobów,
- programowanie funkcyjne pokazuje inny styl pracy na danych,
- deskryptory i `__slots__` zaglądają głębiej w model obiektów,
- model pamięci spina wiele wcześniejszych intuicji.

## Na co szczególnie uważać

Najczęstsze pułapki w tym dziale:

- mylenie iteratora z iterowalnym obiektem,
- mylenie generatora z listą,
- brak zrozumienia, że generator zużywa się podczas iteracji,
- używanie `map()` i `filter()` bez rozumienia, co faktycznie zwracają,
- traktowanie deskryptorów jak „magii OOP”,
- używanie `__slots__` bez świadomości ograniczeń,
- niepewność przy mutowalności, referencjach i współdzieleniu obiektów.

Jeśli któryś temat zaczyna wyglądać zbyt abstrakcyjnie, wróć do małego przykładu i sprawdź:

- co jest wejściem,
- co jest obiektem,
- co jest zwracane,
- co faktycznie zostaje wypisane.

## Po czym poznać, że temat zaczyna siedzieć

Dobry znak, jeśli potrafisz:

- wyjaśnić różnicę między listą a generatorem,
- napisać własny prosty iterator,
- użyć `yield` bez zgadywania,
- napisać własny `with` przez context manager,
- rozpoznać, kiedy `map()` albo `filter()` ma sens, a kiedy zwykła pętla jest czytelniejsza,
- wytłumaczyć, po co istnieją deskryptory,
- opisać, co robi `__slots__` i czego nie wolno przy nim zakładać,
- zrozumieć, czemu zmiana listy przez jedną referencję widać przez drugą.

## Jak najlepiej ćwiczyć

W tym dziale bardzo pomaga metoda:

1. napisz mały przykład,
2. przewidź wynik,
3. uruchom go,
4. porównaj przewidywanie z rzeczywistością,
5. dopiero potem czytaj głębsze wyjaśnienie.

To szczególnie ważne przy:

- generatorach,
- `yield`,
- `with`,
- deskryptorach,
- współdzielonych referencjach.

## Uczciwa ocena startowa tego folderu

Na ten moment ten dział ma dobry zakres tematów i sensowną kolejność, ale jeszcze nie ma poziomu dopracowania folderów `04` i `05`.

Najbardziej brakuje tu:

- mocniejszego `README`,
- większego zestawu ćwiczeń,
- większej liczby przykładów z outputem,
- bardziej „odczarowanego” tłumaczenia tematów trudniejszych, zwłaszcza deskryptorów i modelu pamięci.

To jest dobry fundament, ale jeszcze nie poziom końcowy.

Co dalej:

- po dopracowaniu tego działu można spokojnie przejść do `07. Pliki i dane`,
- albo wracać tu później jako do działu pogłębiającego zrozumienie samego Pythona.
