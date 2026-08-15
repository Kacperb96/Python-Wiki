# 24. Bazy danych zaawansowane

Ten folder jest o tym, co zaczyna boleć dopiero wtedy, gdy aplikacja naprawdę pracuje na danych pod obciążeniem.

Na wcześniejszych etapach zwykle wystarcza myślenie:

- mam tabelę,
- robię query,
- dostaję wynik.

W prawdziwych projektach to za mało.

Zaczynają się pytania:

- czemu query jest wolne,
- czemu paginacja zaczyna zwalniać,
- czemu dwa requesty wchodzą sobie w drogę,
- czemu pojawiają się deadlocki,
- kiedy warto denormalizować,
- jak usuwać dane bez psucia historii,
- jak pracować z bazą bez robienia sobie problemów w produkcji.

## Cel folderu

Po przerobieniu tego działu powinieneś:

- rozumieć, po co są indeksy i jak wpływają na koszt zapytań,
- wiedzieć, czym jest query planning na poziomie praktycznym,
- rozumieć kompromis między normalizacją i denormalizacją,
- wiedzieć, czym są locki, poziomy izolacji i skąd biorą się anomalia współbieżności,
- rozumieć mechanikę deadlocków i sposoby ograniczania ich ryzyka,
- umieć dobrać sensowną strategię paginacji,
- wiedzieć, kiedy soft delete i audit log mają sens,
- znać praktyczne wzorce pracy z bazą w kodzie produkcyjnym,
- umieć spojrzeć na moduł danych jako całość: query, indeksy, historię i współbieżność razem.

## Jak czytać ten dział

Najlepiej iść po kolei:

1. `01-indeksy-i-query-planning-python.md`
2. `02-normalizacja-i-denormalizacja-python.md`
3. `03-locking-i-isolation-levels-python.md`
4. `04-deadlocki-python.md`
5. `05-paginacja-python.md`
6. `06-soft-delete-i-audit-log-python.md`
7. `07-wzorce-pracy-z-baza-w-produkcji-python.md`
8. `08-case-study-orders-baza-python.md`
9. `ZESTAW-CWICZEN.md`

Kolejność jest celowa: najpierw wydajność zapytań i model danych, potem współbieżność, potem wzorce produkcyjne, a na końcu przekrojowy case study spinający wszystko w jeden moduł.

## Jak myśleć o tym folderze

Najważniejsze pytania podczas nauki:

- jak baza znajduje dane,
- ile pracy wykonuje przy zapytaniu,
- jak zmienia się koszt wraz z rozmiarem tabeli,
- co się dzieje, gdy dwa procesy dotykają tych samych rekordów,
- gdzie prostszy model danych kończy się wolniejszym systemem,
- kiedy problemem jest SQL, a kiedy architektura użycia danych,
- jak wszystkie te decyzje spotykają się w jednym endpointzie albo jednym module.

## Najczęstsze pomyłki początkujących

- myślenie, że indeks "zawsze przyspiesza wszystko",
- brak rozumienia kosztu `OFFSET` przy dużej paginacji,
- traktowanie poziomów izolacji jak czysto teoretycznego tematu,
- brak świadomości, że aktualizacje też kosztują przy dużej liczbie indeksów,
- denormalizowanie zbyt wcześnie albo bez planu,
- używanie soft delete bez filtrowania rekordów w całym systemie,
- brak porządku w transakcjach i kolejności lockowania zasobów,
- patrzenie na pojedyncze query bez patrzenia na cały flow modułu.

## Co tutaj jest najważniejsze praktycznie

W realnym projekcie liczą się decyzje takie jak:

- które kolumny naprawdę indeksować,
- jak czytać plan zapytania bez obsesji na punkcie każdego szczegółu,
- kiedy model relacyjny zostawić w spokoju, a kiedy go świadomie rozszerzyć,
- jak ograniczyć konflikty między transakcjami,
- jak paginować bez degradacji wydajności,
- jak przechowywać historię zmian i usunięć,
- jak pisać kod aplikacyjny, który nie robi przypadkowo drogich albo niebezpiecznych operacji na bazie,
- jak patrzeć na moduł danych całościowo, a nie tylko na pojedyncze zapytanie.

## Jak ten dział łączy się z resztą repo

Ten folder bardzo mocno łączy się z wcześniejszymi działami o:

- webie i API,
- testowaniu,
- debugowaniu,
- performance,
- architekturze,
- bezpieczeństwie,
- produkcyjnej obserwowalności.

To tutaj często wychodzą problemy, które na poziomie samego Pythona były niewidoczne.

## Po czym poznasz, że temat rozumiesz

Po przerobieniu folderu powinieneś umieć odpowiedzieć:

- kiedy indeks pomaga, a kiedy nie,
- czemu jedno query robi się wolne na dużych danych,
- jak odróżnić offset pagination od keyset pagination i kiedy której użyć,
- skąd biorą się deadlocki,
- co może pójść źle przy współbieżnych aktualizacjach,
- kiedy soft delete upraszcza biznes, a kiedy komplikuje system,
- jakich zasad trzymać się przy pracy z bazą w kodzie produkcyjnym,
- jak połączyć model danych, indeksy, paginację i historię zmian w jednym sensownym module.

## Docelowy efekt

Po opanowaniu tego folderu nie będziesz jeszcze DBA, ale będziesz mieć bardzo mocną praktyczną bazę do pisania aplikacji w Pythonie, które korzystają z relacyjnej bazy w sposób świadomy, wydajny i bezpieczny.
