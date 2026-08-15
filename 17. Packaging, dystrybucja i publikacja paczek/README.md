# 17. Packaging, dystrybucja i publikacja paczek

To jest folder, który zamienia kod "mam projekt lokalnie" w kod, który da się sensownie:

- zbudować,
- zainstalować,
- wersjonować,
- opublikować,
- używać jako paczki albo narzędzia CLI.

Bardzo wielu ludzi umie pisać kod w Pythonie, ale dużo mniej ludzi naprawdę rozumie, jak ten kod przygotować do dystrybucji. A to właśnie jest ważny krok między nauką języka a bardziej profesjonalnym użyciem Pythona.

## Po co w ogóle ten folder

Dopóki piszesz małe skrypty tylko dla siebie, packaging może wydawać się czymś odległym.

Ale bardzo szybko pojawiają się pytania:

- jak zainstalować ten projekt na innym komputerze,
- jak uruchamiać go jako komendę,
- jak zdefiniować zależności,
- jak oznaczyć wersję,
- jak zbudować paczkę,
- jak wrzucić ją na PyPI,
- jak zadbać o kompatybilność z różnymi wersjami Pythona.

Ten folder jest właśnie o tym.

## Czego nauczysz się w tym module

Po przerobieniu tego działu powinieneś rozumieć:

- po co istnieje `pyproject.toml`,
- czym różnią się `wheel` i `sdist`,
- jak działa publikacja na PyPI i TestPyPI,
- jak sensownie wersjonować projekt,
- jak robić CLI przez entry points,
- jak definiować zależności opcjonalne,
- jak myśleć o kompatybilności wersji Pythona i zależności.

## Jak czytać ten folder

Najlepiej iść po kolei:

1. `01-pyproject-toml-zaawansowanie-python.md`
2. `02-wheel-sdist-python.md`
3. `03-publikacja-pypi-testpypi-python.md`
4. `04-wersjonowanie-semver-python.md`
5. `05-entry-points-cli-python.md`
6. `06-zaleznosci-opcjonalne-python.md`
7. `07-kompatybilnosc-wersji-python.md`

Ta kolejność ma sens, bo najpierw budujesz fundament konfiguracji, potem uczysz się builda i publikacji, a dopiero później wchodzisz w bardziej dojrzałe decyzje o wersjonowaniu i kompatybilności.

## Najważniejsze pytania w tym folderze

Przy każdym temacie dobrze pytać:

- co jest obowiązkowe, a co tylko wygodne,
- co jest standardem, a co stylem konkretnego narzędzia,
- co służy programiście lokalnie, a co użytkownikowi końcowemu,
- jak uniknąć sytuacji, w której paczka działa tylko "u mnie".

## Typowe błędy początkujących

Najczęstsze problemy w tym obszarze to:

- brak sensownego `pyproject.toml`,
- przypadkowe mieszanie narzędzi i konwencji,
- publikacja bez testu na TestPyPI,
- niejasne wersjonowanie,
- brak wpisania wymagań Pythona,
- mylenie zależności runtime z dev dependencies,
- brak zrozumienia, czym różni się build od instalacji.

## Co jest szczególnie ważne praktycznie

W tym folderze bardzo ważne są nie tylko definicje, ale też przepływ pracy.

Czyli na przykład:

1. masz projekt,
2. definiujesz metadata i zależności,
3. budujesz paczkę,
4. testujesz instalację,
5. publikujesz na TestPyPI,
6. dopiero potem na prawdziwe PyPI.

To jest znacznie cenniejsze niż pamięciowe uczenie się pojedynczych pól konfiguracji.

## Po czym poznasz, że temat siedzi

Dobry znak, jeśli potrafisz:

- napisać sensowny `pyproject.toml`,
- zbudować `wheel` i `sdist`,
- wyjaśnić różnicę między nimi,
- przygotować prostą paczkę CLI,
- opublikować projekt na TestPyPI,
- dobrać wersję projektu i zależności w przewidywalny sposób,
- wskazać ryzyka kompatybilności.

## Jak najlepiej ćwiczyć

Najlepszy sposób nauki tego działu to praktyka na małej paczce.

Na przykład:

- prosty kalkulator,
- parser tekstu,
- małe CLI,
- biblioteka narzędziowa.

Dla takiego projektu możesz przejść cały cykl:

- lokalny kod,
- packaging,
- build,
- instalacja,
- entry point,
- publikacja testowa.

## Podsumowanie

To bardzo ważny krok w stronę bardziej profesjonalnego Pythona. Po tym folderze projekt przestaje być tylko "folderem z plikami", a zaczyna być czymś, co da się świadomie dystrybuować i utrzymywać.
