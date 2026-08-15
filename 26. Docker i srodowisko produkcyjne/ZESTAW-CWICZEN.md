# Zestaw ćwiczeń praktycznych — 26. Docker i srodowisko produkcyjne

Te ćwiczenia mają pomóc Ci przejść od podstawowej znajomości Dockera do bardziej świadomego myślenia o obrazach, środowiskach i rolach uruchomieniowych aplikacji.

## Poziom 1

1. Wyjaśnij własnymi słowami różnicę między obrazem i kontenerem.
2. Podaj trzy problemy, które Docker pomaga ograniczyć w projekcie Pythonowym.
3. Wytłumacz, czemu Dockerfile może działać, a jednocześnie być słabym Dockerfile.
4. Opisz, po co używa się `docker compose`.
5. Wyjaśnij, czemu dev i prod nie powinny być traktowane identycznie.

## Poziom 2

1. Rozpisz przykładowy Dockerfile dla prostej aplikacji Pythonowej i opisz rolę każdej instrukcji.
2. Wypisz rzeczy, które umieściłbyś w `.dockerignore` i uzasadnij dlaczego.
3. Opisz, jakie env vars mogłyby być wymagane dla weba, workera i schedulera.
4. Wyjaśnij, czemu uruchamianie kontenera jako `root` bywa ryzykowne.
5. Rozpisz prosty skład usług dla `web + db + redis + worker`.

## Poziom 3

1. Porównaj środowisko `dev`, `staging` i `prod` dla tego samego projektu Pythonowego.
2. Opisz, kiedy jeden wspólny obraz dla weba i workera ma sens, a kiedy warto rozdzielić obrazy.
3. Zaprojektuj strategię dla projektu, w którym web ma być lekki, a worker potrzebuje dodatkowych bibliotek systemowych.
4. Wytłumacz, jakie ryzyka niesie trzymanie sekretów w obrazie lub repo.
5. Opisz, jakie różnice w logowaniu, debugowaniu i uruchamianiu powinny istnieć między dev i prod.

## Zadania praktyczne z kodem i konfiguracją

1. Napisz prosty Dockerfile dla aplikacji `app.py`.
2. Napisz plik `.dockerignore` dla typowego projektu Pythonowego.
3. Przygotuj prosty plik compose dla:
   - `web`,
   - `db`,
   - `worker`.
4. Napisz prostą funkcję w Pythonie, która waliduje obecność wymaganych env vars.
5. Rozpisz trzy różne komendy startowe dla ról: `web`, `worker`, `scheduler`.

## Większe zadania projektowe

1. Zaprojektuj środowisko kontenerowe dla projektu FastAPI + Postgres + Redis + Celery.
2. Opisz, które elementy powinny być wspólne dla weba i workera, a które różne.
3. Zaprojektuj podział konfiguracji między dev i prod.
4. Opisz, jak ograniczałbyś rozmiar i ryzyko bezpieczeństwa obrazu.
5. Wskaż, które błędy środowiskowe najłatwiej popełnić przy pierwszym wdrożeniu i jak byś im zapobiegł.

## Zadanie końcowe

Wyobraź sobie, że masz backend sklepu internetowego z:

- webem,
- workerem,
- schedulerm,
- bazą,
- brokerem.

Odpowiedz pisemnie:

1. Jakie kontenery uruchamiasz osobno?
2. Czy używasz jednego obrazu czy kilku?
3. Jak rozdzielasz konfigurację dev i prod?
4. Gdzie trzymasz sekrety?
5. Jakie trzy dobre praktyki Dockerfile uznajesz za obowiązkowe?
6. Jak zadbasz o to, żeby obraz był lżejszy i bezpieczniejszy?
7. Jakie różnice między lokalnym compose a produkcyjnym uruchomieniem są najważniejsze?

## Zadanie debuggingowe

Masz objaw:

- lokalnie web działa,
- worker nie łączy się z brokerem,
- obraz buduje się bardzo długo,
- kontener jest ogromny,
- na produkcji aplikacja zachowuje się inaczej niż w dev.

Odpowiedz krok po kroku:

1. Jakie są pierwsze hipotezy?
2. Czy problem bardziej pachnie konfiguracją env, układem usług, Dockerfile czy różnicą dev/prod?
3. Co sprawdziłbyś najpierw?
4. Jakie poprawki wdrażałbyś w pierwszej kolejności?
5. Jakich praktyk brakowało najpewniej w projekcie od początku?

## Zadanie przekrojowe

Na podstawie pliku `08-case-study-fastapi-postgres-redis-celery-python.md` zaprojektuj własną wersję środowiska i odpowiedz:

1. Jakie usługi uruchamiasz osobno?
2. Które env vars muszą być wspólne między webem i workerem?
3. Jak rozwiążesz problem gotowości bazy i brokera przy starcie systemu?
4. Gdzie dodałbyś healthchecki?
5. Jak odróżniłbyś konfigurację dev od bardziej produkcyjnego runtime?
6. Jakie dwa problemy środowiskowe przewidujesz jako najbardziej prawdopodobne?
7. Jak wyglądałaby Twoja checklista debugowania "kontener żyje, ale usługa nie działa"?

## Najważniejszy cel tych ćwiczeń

Po zrobieniu tego zestawu powinieneś nie tylko znać słowa typu `obraz`, `kontener`, `Dockerfile`, `compose`, `env`, `worker` czy `prod`, ale rozumieć:

- po co istnieją,
- jakie problemy rozwiązują,
- jakie mają ograniczenia,
- kiedy naprawdę warto ich użyć,
- jak składają się w bardziej profesjonalne środowisko uruchomieniowe aplikacji Pythonowej,
- jak diagnozować je wtedy, gdy build, start albo zależności nie zachowują się tak, jak oczekujesz.
