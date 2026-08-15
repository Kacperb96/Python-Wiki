# Publikacja na PyPI i TestPyPI w Pythonie

## O co chodzi

PyPI to główny publiczny rejestr paczek Pythona.

To właśnie tam trafia bardzo wiele bibliotek, które instalujesz przez:

```bash
pip install nazwa-paczki
```

TestPyPI to środowisko testowe służące do bezpiecznego sprawdzenia procesu publikacji przed wrzuceniem paczki na prawdziwe PyPI.

## Dlaczego TestPyPI jest ważne

Publikacja na publiczny rejestr to już nie jest zabawa lokalna.

Jeśli coś zrobisz źle, możesz opublikować:

- złą wersję,
- błędne metadata,
- uszkodzony build,
- niekompletną paczkę.

Dlatego bardzo zdrowy workflow wygląda tak:

1. build lokalny,
2. test instalacji lokalnej,
3. publikacja na TestPyPI,
4. test instalacji z TestPyPI,
5. dopiero publikacja na prawdziwe PyPI.

## Typowy przepływ publikacji

### 1. Budujesz paczkę

```bash
python -m build
```

### 2. Otrzymujesz pliki w `dist/`

Na przykład:

```text
dist/
  text_tools-0.1.0.tar.gz
  text_tools-0.1.0-py3-none-any.whl
```

### 3. Wysyłasz artefakty

Do publikacji często używa się `twine`.

Przykład dla TestPyPI:

```bash
twine upload --repository testpypi dist/*
```

A dla prawdziwego PyPI:

```bash
twine upload dist/*
```

## Dlaczego nie od razu na PyPI

Bo łatwiej poprawić błąd na etapie testowym niż po publicznej publikacji.

Dobre praktyki tutaj naprawdę oszczędzają stres.

## Co warto sprawdzić przed publikacją

- czy build się udał,
- czy wersja projektu jest poprawna,
- czy README wygląda dobrze,
- czy paczka da się zainstalować,
- czy metadane projektu są sensowne,
- czy nie publikujesz przypadkiem złej wersji.

## Test instalacji z TestPyPI

Po publikacji testowej warto sprawdzić, czy paczkę da się zainstalować jako użytkownik końcowy.

Czyli nie tylko "czy ja ją zbudowałem", ale też:

- czy ktoś inny może ją pobrać,
- czy zależności są poprawne,
- czy build rzeczywiście nadaje się do użycia.

## README i metadane też mają znaczenie

Publikacja to nie tylko pliki.

Użytkownik na stronie paczki widzi także:

- nazwę,
- opis,
- README,
- wersję,
- informacje o kompatybilności,
- linki do repo.

Jeśli to jest chaotyczne, paczka wygląda nieprofesjonalnie nawet wtedy, gdy działa technicznie.

## Bezpieczeństwo publikacji

W kontekście publikacji warto uważać na:

- tokeny do rejestru,
- błędne poświadczenia,
- publikację nie tej wersji co trzeba,
- publikację builda bez wcześniejszego testu.

Tokenów nie powinno się trzymać w repo ani w kodzie.

## Kiedy to ma sens

Publikacja na PyPI ma sens, gdy:

- tworzysz bibliotekę dla innych,
- chcesz używać paczki w wielu projektach,
- budujesz narzędzie CLI do wygodnej instalacji,
- uczysz się pełnego cyklu życia projektu Python.

Nie każdy lokalny skrypt musi kończyć na PyPI. Ale warto rozumieć ten proces.

## Typowe błędy początkujących

- publikacja bez TestPyPI,
- brak lokalnego testu instalacji,
- brak podbicia wersji,
- błędne metadata,
- zły README,
- publikacja z pośpiechu bez checklisty,
- mylenie rejestru testowego z produkcyjnym.

## Mini checklista przed publikacją

- Czy wersja została podbita?
- Czy build jest aktualny?
- Czy `dist/` nie zawiera starych artefaktów?
- Czy README wygląda poprawnie?
- Czy instalacja została przetestowana?
- Czy testowa publikacja działa?

## Szybka ściąga

- PyPI — publiczny rejestr paczek,
- TestPyPI — bezpieczne środowisko testowe,
- `python -m build` — build,
- `twine upload ...` — publikacja.

## Ćwiczenia

1. Opisz pełny workflow od kodu lokalnego do publikacji testowej.
2. Wyjaśnij, po co istnieje TestPyPI.
3. Zrób checklistę publikacji paczki.
4. Wskaż 5 rzeczy, które trzeba sprawdzić przed wysłaniem paczki.
5. Opisz, jakie ryzyko niesie publikacja bez testów instalacji.

## Najważniejsze do zapamiętania

- PyPI to publiczny rejestr paczek, a TestPyPI służy do bezpiecznych testów publikacji.
- Publikacja powinna być poprzedzona buildem i testem instalacji.
- README, metadata i wersja projektu są częścią jakości publikacji.
- Nie warto publikować "na żywioł".
- TestPyPI to bardzo zdrowy etap przed prawdziwym releasem.
