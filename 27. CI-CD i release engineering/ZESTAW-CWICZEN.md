# Zestaw ćwiczeń praktycznych — 27. CI-CD i release engineering

Te ćwiczenia mają pomóc Ci przejść od podstawowego rozumienia CI/CD do świadomego projektowania pipeline'ów, releasów i wdrożeń.

## Poziom 1

1. Wyjaśnij własnymi słowami różnicę między lintem, testami, typecheckiem i buildem.
2. Podaj trzy przykłady jakościowych warunków, które pipeline może sprawdzać.
3. Wytłumacz, czym różni się merge, release i deployment.
4. Opisz, po co istnieją changelog i tagi.
5. Wyjaśnij, czemu automatyczna publikacja nie oznacza automatycznego deploymentu.

## Poziom 2

1. Rozpisz prosty pipeline dla projektu Pythonowego z testami, typingiem i obrazem Dockera.
2. Zaprojektuj quality gates dla merge do `main`.
3. Opisz prosty release workflow dla biblioteki Pythonowej.
4. Wypisz, jakie informacje powinny znaleźć się w changelogu wersji `v1.4.0`.
5. Rozpisz, jakie kroki wykonałbyś przed deploymentem na staging.

## Poziom 3

1. Porównaj strategię małych częstych releasów z dużymi rzadkimi releasami.
2. Opisz, kiedy warto publikować artefakt automatycznie po tagu.
3. Zaprojektuj podstawowy hotfix flow dla backendu produkcyjnego.
4. Wytłumacz, jakie quality gates powinny obowiązywać osobno dla merge, release i deploymentu.
5. Opisz, jak feature flags mogą zmniejszać ryzyko releasu.

## Zadania praktyczne z procesem i konfiguracją

1. Rozpisz przykładową kolejność etapów pipeline'u `lint -> test -> typecheck -> build` i uzasadnij ją.
2. Napisz przykładowy changelog dla wersji backendu z trzema zmianami funkcjonalnymi i dwiema poprawkami błędów.
3. Zaprojektuj regułę wersjonowania i tagowania dla projektu Pythonowego.
4. Rozpisz checklistę przed wypuszczeniem releasu produkcyjnego.
5. Przygotuj prostą mapę: `commit -> tag -> artefakt -> deployment`.

## Większe zadania projektowe

1. Zaprojektuj pełny proces CI/CD dla projektu FastAPI wdrażanego jako obraz Dockera.
2. Opisz, które elementy procesu zautomatyzowałbyś od razu, a które zostawiłbyś jako świadome decyzje manualne.
3. Zaprojektuj quality gates dla projektu z mypy, testami integracyjnymi i buildem obrazu.
4. Opisz, jak wyglądałby release workflow dla:
   - paczki Pythonowej,
   - backendu API,
   - systemu z workerami.
5. Wskaż, jakie błędy releasowe najłatwiej popełnić na początku i jak im zapobiegać.

## Zadanie końcowe

Wyobraź sobie, że masz backend sklepu internetowego, który jest rozwijany przez mały zespół i wdrażany kilka razy w tygodniu.

Odpowiedz pisemnie:

1. Jak wygląda pipeline obowiązkowy dla każdego merge requesta?
2. Jakie quality gates blokują merge?
3. Kiedy tworzysz release?
4. Jak tagujesz wersję i prowadzisz changelog?
5. Co publikujesz automatycznie?
6. Co wdrażasz najpierw na staging, a co na prod?
7. Jak wygląda ścieżka hotfixu?

## Zadanie debuggingowe

Masz objaw:

- pipeline czasem jest zielony, ale release i tak psuje się później,
- staging działa, a produkcja ma problem po wdrożeniu,
- nikt nie jest pewny, jaka wersja jest teraz wdrożona,
- changelog nie zgadza się z tym, co faktycznie weszło.

Odpowiedz krok po kroku:

1. Jakie są pierwsze hipotezy?
2. Czy problem bardziej pachnie słabym pipeline'em, złym release workflow, brakiem quality gates czy chaosem wersjonowania?
3. Co sprawdziłbyś najpierw?
4. Jakie poprawki procesu wdrożyłbyś w pierwszej kolejności?
5. Jakich praktyk brakowało najpewniej od początku?

## Zadanie przekrojowe

Na podstawie pliku `08-case-study-pr-do-deployment-python.md` zaprojektuj własny proces i odpowiedz:

1. Jak wygląda droga zmiany od PR do produkcji?
2. Które etapy są automatyczne, a które wymagają decyzji człowieka?
3. Jak zapewnisz spójność między tagiem, changelogiem i artefaktem?
4. Jakie dwa quality gates uznajesz za absolutnie obowiązkowe?
5. Jak zaprojektujesz rollback dla błędnego wdrożenia?
6. Jakie dwa problemy procesu przewidujesz jako najbardziej prawdopodobne?
7. Jak wyglądałaby Twoja checklista debugowania sytuacji "pipeline zielony, ale release zły"?

## Najważniejszy cel tych ćwiczeń

Po zrobieniu tego zestawu powinieneś nie tylko znać słowa typu `pipeline`, `release`, `tag`, `deployment`, `quality gate` czy `artifact`, ale rozumieć:

- po co istnieją,
- jakie problemy rozwiązują,
- jakie mają ograniczenia,
- kiedy naprawdę warto ich użyć,
- jak składają się w bardziej przewidywalny i dojrzały proces dostarczania zmian,
- jak diagnozować go wtedy, gdy pipeline, release albo deployment nie zachowują się tak, jak oczekujesz.
