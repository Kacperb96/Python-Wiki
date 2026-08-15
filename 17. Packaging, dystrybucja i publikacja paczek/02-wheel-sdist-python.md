# `wheel` i `sdist` w Pythonie

## O co chodzi

Kiedy budujesz paczkę Pythona, najczęściej pojawiają się dwa rodzaje artefaktów:

- `sdist`,
- `wheel`.

To bardzo ważne pojęcia, bo mówią o tym, **w jakiej postaci dystrybuujesz projekt**.

## `sdist` — source distribution

`sdist` to dystrybucja źródłowa.

Zawiera kod źródłowy projektu i pliki potrzebne do zbudowania paczki.

Najczęściej ma postać archiwum `.tar.gz`.

Przykładowa nazwa:

```text
moj_projekt-0.1.0.tar.gz
```

## `wheel`

`wheel` to gotowa zbudowana paczka binarna/instalowalna.

Najczęściej ma rozszerzenie `.whl`.

Przykładowa nazwa:

```text
moj_projekt-0.1.0-py3-none-any.whl
```

## Najprostsza intuicja

- `sdist` to bardziej "materiał źródłowy do zbudowania",
- `wheel` to bardziej "gotowy pakiet do instalacji".

W codziennej praktyce użytkownik zwykle woli wheel, bo instalacja jest prostsza i szybsza.

## Jak zbudować paczkę

Typowy build:

```bash
python -m build
```

Po nim zwykle pojawia się katalog `dist/`.

Przykładowa zawartość:

```text
dist/
  moj_projekt-0.1.0.tar.gz
  moj_projekt-0.1.0-py3-none-any.whl
```

## Co zwykle trafia do `dist/`

- jeden `sdist`,
- jeden lub więcej wheel-i.

Dla prostych czysto pythonowych projektów często zobaczysz wheel typu:

```text
py3-none-any
```

Co oznacza w praktyce, że paczka:

- działa na Pythonie 3,
- nie jest specyficzna dla jednej platformy,
- nie zawiera kodu natywnego zależnego od systemu.

## Kiedy `wheel` jest szczególnie ważny

Wheel daje dużą przewagę, gdy:

- użytkownik ma po prostu zainstalować paczkę,
- chcesz szybszej instalacji,
- chcesz uniknąć budowania ze źródeł po stronie użytkownika,
- projekt ma zależności lub kroki buildowe, które lepiej wykonać wcześniej.

## Kiedy `sdist` nadal ma znaczenie

`sdist` nadal jest ważny, bo:

- daje pełniejszy obraz projektu źródłowego,
- pozwala budować paczkę w różnych środowiskach,
- bywa potrzebny tam, gdzie wheel nie wystarcza albo trzeba budować od źródeł.

Dobrą praktyką jest rozumieć oba formaty, a nie traktować któregoś jako zbędnego.

## Przykład przepływu

Masz projekt `text-tools`.

1. konfigurujesz `pyproject.toml`,
2. uruchamiasz build,
3. dostajesz `sdist` i `wheel`,
4. instalujesz i testujesz build,
5. dopiero potem publikujesz.

To bardzo zdrowy workflow.

## Jak sprawdzić, co zbudowałeś

Po buildzie warto zajrzeć do `dist/` i upewnić się, że:

- wersja jest poprawna,
- nazwa projektu jest poprawna,
- artefakty rzeczywiście się pojawiły,
- nie budujesz czegoś z błędnymi metadanymi.

## Co użytkownik końcowy widzi w praktyce

Najczęściej po prostu wpisuje:

```bash
pip install nazwa-paczki
```

A pod spodem `pip` próbuje pobrać najlepszy dostępny artefakt.

Jeśli ma wheel pasujący do środowiska, zwykle wybierze właśnie jego.

## Typowe błędy początkujących

- brak sprawdzenia zawartości `dist/`,
- publikacja bez lokalnego testu instalacji,
- brak zrozumienia, że `wheel` i `sdist` to nie to samo,
- traktowanie builda jak czarnej skrzynki,
- mylenie builda z uruchamianiem projektu lokalnie.

## Kiedy to ma sens

Temat `wheel` i `sdist` ma sens zawsze, gdy:

- budujesz paczkę dla innych,
- chcesz publikować projekt,
- chcesz mieć przewidywalny proces dystrybucji,
- uczysz się bardziej profesjonalnego workflow.

## Mini checklista builda

- Czy build przechodzi bez błędów?
- Czy w `dist/` są oba artefakty?
- Czy nazwa i wersja są poprawne?
- Czy paczka daje się zainstalować lokalnie?
- Czy wheel odpowiada temu, czego oczekujesz od projektu?

## Szybka ściąga

- `sdist` — source distribution,
- `wheel` — gotowa paczka instalowalna,
- `dist/` — katalog z artefaktami builda,
- `python -m build` — typowy sposób budowania projektu.

## Ćwiczenia

1. Zbuduj mały projekt i sprawdź zawartość `dist/`.
2. Wyjaśnij różnicę między `sdist` i `wheel` własnymi słowami.
3. Rozpoznaj po nazwie pliku, który artefakt jest wheel-em.
4. Opisz, czemu wheel bywa wygodniejszy dla użytkownika końcowego.
5. Zrób checklistę, co sprawdzasz po buildzie.

## Najważniejsze do zapamiętania

- `sdist` i `wheel` to dwa różne formaty dystrybucji paczki.
- `wheel` zwykle daje szybszą i wygodniejszą instalację.
- `sdist` nadal ma znaczenie jako dystrybucja źródłowa.
- Build projektu to osobny etap od samego pisania kodu.
- Warto zawsze sprawdzać artefakty przed publikacją.
