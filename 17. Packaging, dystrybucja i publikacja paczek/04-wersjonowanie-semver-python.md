# Wersjonowanie i SemVer w Pythonie

## Po co w ogóle wersjonowanie

Wersja projektu to nie ozdoba.

To informacja dla:

- użytkownika,
- innych programistów,
- narzędzi dependency management,
- systemów CI/CD,
- przyszłego Ciebie.

Wersja mówi, czy projekt:

- ma poprawki błędów,
- dostał nowe funkcje,
- wprowadza breaking changes,
- nadaje się do aktualizacji bez ryzyka.

## Czym jest SemVer

SemVer to skrót od Semantic Versioning.

Najczęstszy zapis:

```text
MAJOR.MINOR.PATCH
```

Przykład:

```text
1.4.2
```

## Jak czytać numer wersji

### `PATCH`

Podbijasz, gdy:

- poprawiasz bugi,
- nie zmieniasz API w sposób łamiący,
- nie wprowadzasz dużych nowych funkcji.

Przykład:

```text
1.4.2 -> 1.4.3
```

### `MINOR`

Podbijasz, gdy:

- dodajesz nowe funkcje,
- zachowujesz kompatybilność wsteczną.

Przykład:

```text
1.4.2 -> 1.5.0
```

### `MAJOR`

Podbijasz, gdy:

- wprowadzasz breaking changes,
- stare użycie przestaje działać,
- użytkownik musi coś zmienić po aktualizacji.

Przykład:

```text
1.4.2 -> 2.0.0
```

## Co to są breaking changes

To zmiany, które psują dotychczasowe użycie projektu.

Przykłady:

- usunięcie funkcji,
- zmiana sygnatury funkcji,
- zmiana formatu danych zwracanych przez API,
- zmiana zachowania, na którym użytkownicy mogli polegać.

## Wersja `0.x.y`

Bardzo ważny etap dla młodych projektów.

Wersje `0.x.y` zwykle oznaczają, że projekt jeszcze nie obiecuje pełnej stabilności API.

Przykład:

```text
0.1.0
0.2.0
0.5.3
```

To częsty i zdrowy stan na początku projektu.

## Kiedy wejść w `1.0.0`

Nie ma jednej magicznej reguły, ale zwykle wtedy, gdy:

- projekt ma sensowny zakres funkcji,
- API jest bardziej ustabilizowane,
- wiesz, czego paczka ma dotyczyć,
- chcesz jasno komunikować większą dojrzałość.

## Wersjonowanie a zaufanie użytkownika

Dobre wersjonowanie buduje przewidywalność.

Użytkownik powinien mniej więcej rozumieć:

- czy aktualizacja jest bezpieczna,
- czy może pojawić się breaking change,
- czy to tylko poprawka błędu,
- czy doszły nowe funkcje.

Jeśli numer wersji nic nie znaczy, projekt staje się trudniejszy do utrzymania i używania.

## Wersja projektu a wersje zależności

To dwa różne porządki.

- wersja projektu mówi o Twojej paczce,
- wersje zależności mówią, z jakimi bibliotekami projekt działa.

Trzeba pilnować obu rzeczy osobno.

## Przykładowy scenariusz

Masz paczkę `text-tools`.

### Start

```text
0.1.0
```

Projekt dopiero rusza.

### Dodajesz nowe komendy CLI bez psucia starego API

```text
0.2.0
```

### Poprawiasz błąd parsowania wejścia

```text
0.2.1
```

### Zmieniasz sposób działania głównej funkcji w sposób niekompatybilny

```text
1.0.0 -> 2.0.0
```

## Typowe błędy początkujących

- wersje zmieniane chaotycznie,
- brak logiki w podbijaniu numerów,
- breaking changes wypuszczane jako patch,
- brak rozróżnienia między etapem `0.x` i `1.x`,
- publikacja kilku różnych buildów pod tą samą wersją.

## Czy trzeba być ortodoksyjnym

Nie.

SemVer ma pomagać, a nie być religią.

Najważniejsze jest to, żeby wersjonowanie było:

- spójne,
- przewidywalne,
- uczciwe wobec użytkownika.

## Wersjonowanie a changelog

Dobre wersjonowanie bardzo dobrze współpracuje z changelogiem.

Czyli użytkownik widzi:

- jaka jest nowa wersja,
- co się zmieniło,
- czy zmiana jest bezpieczna,
- czy są breaking changes.

To bardzo poprawia profesjonalizm projektu.

## Mini checklista wersjonowania

- Czy zmiana jest breaking change?
- Czy tylko naprawiasz błąd?
- Czy dodajesz funkcję bez psucia starego API?
- Czy numer wersji to uczciwie komunikuje?
- Czy stary build nie został już opublikowany pod tą wersją?

## Szybka ściąga

- `PATCH` — poprawki błędów,
- `MINOR` — nowe funkcje bez łamania kompatybilności,
- `MAJOR` — breaking changes,
- `0.x` — etap młodszego, mniej stabilnego API,
- `1.0.0` — zwykle sygnał dojrzalszego projektu.

## Ćwiczenia

1. Rozpisz 5 przykładowych zmian i dobierz do nich właściwy bump wersji.
2. Podaj przykład breaking change.
3. Wyjaśnij różnicę między `0.2.1` a `1.2.1` z punktu widzenia dojrzałości projektu.
4. Zaproponuj plan wersji dla swojej paczki od `0.1.0` do `1.0.0`.
5. Zrób checklistę: kiedy patch, kiedy minor, kiedy major.

## Najważniejsze do zapamiętania

- Wersjonowanie komunikuje zmiany użytkownikowi i narzędziom.
- SemVer opiera się na `MAJOR.MINOR.PATCH`.
- Breaking changes powinny być komunikowane wyraźnie.
- Wersja `0.x` to normalny etap rozwoju projektu.
- Dobre wersjonowanie zwiększa zaufanie do paczki i ułatwia jej utrzymanie.
