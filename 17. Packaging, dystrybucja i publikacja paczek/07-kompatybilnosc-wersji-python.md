# Kompatybilność wersji w Pythonie

## O co chodzi

Kiedy publikujesz paczkę, musisz myśleć nie tylko o tym, czy działa na Twoim komputerze.

Musisz też myśleć:

- z jakimi wersjami Pythona działa,
- z jakimi wersjami zależności działa,
- czy użytkownik na innym środowisku będzie miał taki sam rezultat.

To właśnie jest praktyczny wymiar kompatybilności.

## `requires-python`

Jedno z najważniejszych pól w `pyproject.toml`:

```toml
requires-python = ">=3.11"
```

To jawnie mówi, od jakiej wersji Python projekt jest wspierany.

Bardzo ważne: nie wpisuj tego przypadkowo. Powinno odpowiadać temu, co naprawdę testujesz i wspierasz.

## Kompatybilność z interpreterem

Projekt może używać funkcji języka, które nie istnieją w starszych wersjach.

Przykłady:

- nowsza składnia typowania,
- nowe elementy standardowej biblioteki,
- zmiany zachowania interpreterów i narzędzi.

Dlatego trzeba wiedzieć, od jakiej wersji naprawdę chcesz wspierać projekt.

## Kompatybilność zależności

To drugi ważny wymiar.

Przykład:

```toml
dependencies = [
  "requests>=2.32,<3",
]
```

Takie ograniczenie komunikuje, że projekt:

- wymaga co najmniej danej wersji,
- ale nie zakłada jeszcze kompatybilności z przyszłym dużym breaking release.

## Dlaczego zakresy wersji mają znaczenie

Jeśli wpiszesz zależność zbyt szeroko, możesz dopuścić wersję, z którą projekt nie działa.

Jeśli wpiszesz zbyt wąsko, możesz niepotrzebnie blokować użytkowników.

Tu nie ma magii. To kwestia świadomego kompromisu.

## Kompatybilność a testy

Najuczciwsze podejście jest proste:

- deklaruj tylko to, co realnie testujesz.

Jeśli paczka ma działać na Pythonie `3.11` i `3.12`, warto to rzeczywiście sprawdzać w CI albo lokalnych testach.

## Typowe źródła problemów

- paczka działa tylko na jednej wersji Pythona,
- zależność podbiła major version i coś się zepsuło,
- projekt używa nowej składni bez aktualizacji `requires-python`,
- brak testów na kilku środowiskach,
- deklaracja kompatybilności nie zgadza się z rzeczywistością.

## Kiedy wspierać wiele wersji, a kiedy nie

Nie każda paczka musi wspierać bardzo szeroki zakres wersji.

Czasem lepiej świadomie powiedzieć:

- wspieramy `>=3.11`,

niż udawać zgodność od `3.8`, której nikt nie testuje.

To bardziej uczciwe i zdrowsze projektowo.

## Kompatybilność a nowoczesny Python

Im szerzej chcesz wspierać starsze wersje, tym częściej:

- rezygnujesz z wygodnej nowoczesnej składni,
- komplikujesz typowanie,
- dodajesz workaroundy,
- zwiększasz koszt utrzymania.

Dlatego kompatybilność to również decyzja projektowa, nie tylko techniczna.

## Przykładowy scenariusz

Masz nową paczkę i korzystasz z nowoczesnego typowania oraz nowej składni.

Wtedy sensowny wybór może wyglądać tak:

```toml
requires-python = ">=3.11"
```

Zamiast próbować wspierać wiele starych wersji tylko teoretycznie.

## Typowe błędy początkujących

- brak `requires-python`,
- zbyt szerokie deklaracje zgodności,
- brak testów dla deklarowanych wersji,
- zbyt luźne ograniczenia zależności,
- ignorowanie breaking changes w paczkach zewnętrznych.

## Mini checklista kompatybilności

- Czy `requires-python` odpowiada realnemu kodowi?
- Czy zależności mają sensowne zakresy wersji?
- Czy deklarowane wersje Pythona są testowane?
- Czy projekt używa składni zgodnej z deklarowanym minimum?
- Czy breaking changes w zależnościach są uwzględniane?

## Szybka ściąga

- `requires-python` określa wspieraną wersję interpretera,
- zgodność z Pythonem i zgodność z zależnościami to dwa różne problemy,
- deklaracje powinny odpowiadać realnym testom,
- szeroka kompatybilność zwiększa koszt utrzymania.

## Ćwiczenia

1. Ustaw `requires-python` dla przykładowej paczki i uzasadnij wybór.
2. Zaproponuj sensowny zakres wersji dla dwóch zależności.
3. Opisz przypadek, w którym zbyt luźna wersja zależności może złamać projekt.
4. Wskaż, jakie kompromisy daje wsparcie starszych wersji Pythona.
5. Zrób checklistę kompatybilności dla paczki publikowanej publicznie.

## Najważniejsze do zapamiętania

- Kompatybilność to nie deklaracja marketingowa, tylko realna obietnica projektu.
- `requires-python` jest jednym z najważniejszych pól konfiguracji paczki.
- Zakresy wersji zależności trzeba dobierać świadomie.
- Lepiej wspierać mniej wersji uczciwie niż wiele wersji tylko na papierze.
- Testy i kompatybilność powinny iść razem.
