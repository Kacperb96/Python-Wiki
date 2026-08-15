# 28. Observability i produkcyjne monitorowanie

Ten folder jest o tym, jak przestać zgadywać, co dzieje się z aplikacją po wdrożeniu, i zacząć to naprawdę widzieć.

Na początku wiele projektów działa tak:

- aplikacja czasem rzuca błąd,
- użytkownik mówi, że "coś nie działa",
- w logach jest chaos albo nie ma nic sensownego,
- nie wiadomo, czy problem dotyczy wydajności, błędów, bazy, kolejki czy środowiska.

To właśnie miejsce, gdzie wchodzi observability.

## Cel folderu

Po przerobieniu tego działu powinieneś:

- rozumieć różnicę między logami, metrykami i tracingiem,
- wiedzieć, po co structured logging daje większą wartość niż przypadkowe `print()` i luźne stringi,
- rozumieć, jakie metryki pomagają naprawdę widzieć zdrowie systemu,
- wiedzieć, po co istnieją trace'y i jak pomagają w systemach rozproszonych,
- rozumieć rolę healthchecków, readiness i liveness,
- znać sens używania narzędzi typu Sentry,
- umieć podejść do diagnozy błędu produkcyjnego bardziej systemowo, a nie tylko intuicyjnie,
- myśleć o observability jako o części architektury, nie dodatku po fakcie.

## Jak czytać ten dział

Najlepiej iść po kolei:

1. `01-structured-logging-python.md`
2. `02-metryki-python.md`
3. `03-tracing-python.md`
4. `04-healthchecki-python.md`
5. `05-readiness-liveness-python.md`
6. `06-sentry-python.md`
7. `07-diagnoza-bledow-w-produkcji-python.md`
8. `ZESTAW-CWICZEN.md`

Kolejność jest celowa: najpierw budujesz intuicję o trzech głównych filarach observability, potem o zdrowiu usług i narzędziach, a na końcu o praktycznej diagnozie problemów.

## Jak myśleć o tym folderze

Najważniejsze pytania podczas nauki:

- jak dowiem się, że system ma problem,
- jak odróżnię problem błędu od problemu wydajności,
- jak połączę pojedynczy request z jego skutkami w innych usługach,
- czy mój healthcheck naprawdę mówi coś sensownego,
- co zobaczę, gdy użytkownik zgłosi błąd w sobotę o 2:00 w nocy,
- czy moje logi i metryki pomagają, czy tylko produkują szum.

## Najczęstsze pomyłki początkujących

- mylenie observability z samym logowaniem,
- wrzucanie przypadkowych logów bez struktury i kontekstu,
- mierzenie wszystkiego bez rozumienia, co jest naprawdę ważne,
- traktowanie healthchecka jako pełnego dowodu zdrowia systemu,
- brak rozróżnienia między readiness i liveness,
- liczenie, że Sentry albo inny tool sam rozwiąże problem architektury obserwowalności,
- brak powiązania błędów z kontekstem requestu, użytkownika i wersji systemu.

## Co tutaj jest najważniejsze praktycznie

W realnym projekcie liczą się decyzje takie jak:

- jakie pola mają być w logach,
- jakie metryki naprawdę opisują zdrowie systemu,
- kiedy trace daje więcej niż sam log,
- jakie checki powinny decydować o gotowości usługi,
- co ma trafiać do systemu błędów typu Sentry,
- jak skrócić drogę od objawu do przyczyny.

## Jak ten dział łączy się z resztą repo

Ten folder bardzo mocno łączy się z wcześniejszymi działami o:

- webie i API,
- messagingu i workerach,
- Dockerze i środowisku produkcyjnym,
- CI/CD,
- bazach danych,
- debugowaniu,
- bezpieczeństwie.

To właśnie tutaj wszystkie wcześniejsze decyzje zaczynają być widoczne albo przynajmniej diagnozowalne w działającym systemie.

## Po czym poznasz, że temat rozumiesz

Po przerobieniu folderu powinieneś umieć odpowiedzieć:

- jakie informacje powinny znaleźć się w sensownym logu,
- które metryki są naprawdę użyteczne dla weba, workera i kolejki,
- kiedy tracing daje przewagę nad samymi logami,
- czym różni się readiness od liveness,
- po co wdraża się narzędzia typu Sentry,
- jak podejść do incydentu produkcyjnego krok po kroku,
- jak sprawić, żeby observability było wsparciem dla zespołu, a nie tylko źródłem szumu.

## Docelowy efekt

Po opanowaniu tego folderu nie będziesz jeszcze specjalistą od SRE czy platform observability, ale będziesz mieć bardzo mocny praktyczny fundament do budowania i wykorzystywania obserwowalności w projektach Pythonowych.
