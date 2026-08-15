# 09. Narzędzia

Ten dział rozwija codzienny warsztat pracy programisty Python.

To nie jest już tylko nauka składni języka.

To jest nauka pracy tak, żeby kod dało się:

- uruchamiać powtarzalnie,
- wersjonować,
- debugować,
- logować,
- profilować,
- dokumentować,
- utrzymywać jak prawdziwy projekt.

Po tym dziale powinieneś rozumieć:

- środowiska wirtualne,
- zależności i instalację bibliotek,
- git basics,
- dokumentowanie kodu,
- logging,
- debugowanie,
- profilowanie,
- praktyczne użycie `subprocess`,
- budowanie prostych CLI przez `argparse`.

## Po co w ogóle ten dział

W pewnym momencie samo „umiem pisać funkcje i klasy” przestaje wystarczać.

Zaczynają się pytania:

- jak uruchomić projekt na czysto,
- jak ogarnąć zależności,
- jak nie zaśmiecić systemowego Pythona,
- jak znaleźć błąd,
- jak sprawdzić, co spowalnia program,
- jak uruchomić zewnętrzną komendę,
- jak zostawić po sobie czytelny projekt.

To właśnie odpowiada na te pytania.

Ten dział jest bardziej warsztatowy niż językowy, ale bardzo ważny, jeśli chcesz programować dojrzalej.

## Jak czytać ten dział

Najlepiej iść po kolei:

1. `01-wirtualne-srodowiska-python.md`
2. `02-pip-i-dependency-management-python.md`
3. `03-git-podstawy-profesjonalnie-python.md`
4. `04-dokumentowanie-kodu-python.md`
5. `05-logging-python.md`
6. `06-debugowanie-python-pdb-breakpoint.md`
7. `07-profilowanie-python-timeit-cprofile-line-profiler.md`
8. `08-subprocess-python.md`
9. `09-argparse-python.md`

Ta kolejność ma sens, bo:

- najpierw tworzysz zdrowe środowisko pracy,
- potem ogarniasz zależności,
- potem uczysz się porządku w repo,
- potem dokumentacji,
- potem narzędzi do obserwacji, naprawy i mierzenia kodu.
- potem budowania prostych, używalnych narzędzi CLI.

## Na co szczególnie uważać

Najczęstsze pułapki w tym dziale:

- instalowanie bibliotek globalnie zamiast do `venv`,
- brak rozumienia, po co jest `requirements.txt` albo inna forma listy zależności,
- commitowanie śmieci do repo,
- mylenie `print()` z prawdziwym logowaniem,
- debugowanie „na ślepo” bez użycia breakpointów,
- optymalizowanie kodu bez wcześniejszego pomiaru,
- uruchamianie komend z `subprocess` bez sprawdzenia błędów i wyniku.

To jest dział, w którym bardzo łatwo robić rzeczy „na szybko”, ale właśnie tutaj zaczyna się profesjonalny nawyk pracy.

## Po czym poznać, że temat zaczyna siedzieć

Dobry znak, jeśli potrafisz:

- utworzyć i aktywować środowisko wirtualne bez zgadywania,
- zainstalować zależności i opisać je w projekcie,
- zrobić sensowny commit i `.gitignore`,
- napisać czytelny docstring,
- rozróżniać `logging.info()` od `logging.error()` i `logging.exception()`,
- użyć `breakpoint()` albo `pdb`,
- sprawdzić czas działania prostego fragmentu przez `timeit`,
- uruchomić komendę przez `subprocess.run()` i przechwycić wynik.

## Jak najlepiej ćwiczyć

W tym dziale bardzo pomaga praktyka na małym projekcie.

Najlepszy rytm nauki:

1. utwórz mały katalog projektu,
2. załóż `venv`,
3. dodaj bibliotekę,
4. opisz projekt w `README`,
5. dodaj logowanie,
6. zepsuj coś celowo i zdebuguj,
7. zmierz czas działania fragmentu,
8. uruchom prostą komendę z systemu przez `subprocess`.

To daje dużo więcej niż samo czytanie suchych opisów narzędzi.

## Uczciwa ocena startowa tego folderu

Na ten moment ten dział ma bardzo dobry zakres tematów, ale jeszcze nie ma poziomu dopracowania folderów `06-08`.

Najbardziej brakuje tu:

- mocniejszego `README`,
- większego zestawu ćwiczeń,
- większej liczby przykładów z outputem,
- większej liczby scenariuszy praktycznych z codziennej pracy programisty.

To jest dobry fundament, ale jeszcze nie końcowy poziom.

Co dalej:

- po dopracowaniu tego działu można przejść do `10. Testowanie`,
- potem do `11. Narzędzie profesjonalisty`, jeśli chcesz iść dalej w stronę realnego workflow developera.
