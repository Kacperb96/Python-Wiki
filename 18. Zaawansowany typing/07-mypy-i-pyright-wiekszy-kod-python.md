# `mypy` i `pyright` w większym kodzie Python

## O co chodzi

Samo dodanie adnotacji typów nie daje pełnej wartości, jeśli nigdzie ich nie sprawdzasz.

Tu właśnie wchodzą narzędzia takie jak:

- `mypy`,
- `pyright`.

One analizują kod statycznie i pomagają wykrywać błędy zanim program w ogóle się uruchomi.

## Co dają w praktyce

Dzięki checkerom typów możesz wcześniej złapać np.:

- zły typ argumentu,
- błędne użycie `None`,
- niezgodny zwracany typ,
- niepoprawne użycie interfejsu,
- problemy przy refaktoryzacji.

To nie zastępuje testów, ale jest bardzo silnym wsparciem jakości kodu.

## `mypy` vs `pyright`

Na poziomie nauki najważniejsze jest to, że oba narzędzia robią podobną klasę pracy:

- sprawdzają typy statycznie,
- analizują kontrakty,
- pomagają rozwijać większy kod.

Różnią się szczegółami, stylem działania i ergonomią, ale nie trzeba na start robić z tego wojny religijnej.

Najważniejsze jest świadome używanie przynajmniej jednego z nich.

## Kiedy checker typów daje największą wartość

Szczególnie gdy:

- projekt ma wiele modułów,
- pracujesz zespołowo,
- API jest używane w wielu miejscach,
- robisz refaktoryzację,
- wracasz do starego kodu,
- logika danych jest złożona.

## Czego checker nie robi

To ważne:

- nie zastępuje runtime walidacji,
- nie zastępuje testów,
- nie gwarantuje poprawności biznesowej,
- nie sprawia automatycznie, że kod jest dobrze zaprojektowany.

On pomaga w jednej bardzo konkretnej warstwie: zgodności typów i kontraktów.

## Jak wdrażać typing do istniejącego projektu

Nie trzeba robić wszystkiego naraz.

Bardzo zdrowe podejście:

1. zacząć od najważniejszych modułów,
2. typować publiczne API,
3. ograniczać `Any`,
4. poprawiać błędy iteracyjnie,
5. stopniowo podnosić jakość.

To zwykle działa lepiej niż wielka jednorazowa rewolucja.

## Najczęstsze pułapki

### 1. Zbyt dużo `Any`

To często znak, że typing formalnie istnieje, ale nie daje pełnej wartości.

### 2. Zbyt szybkie włączenie bardzo restrykcyjnych reguł

Może zabić motywację i zamienić cały temat w walkę z narzędziem.

### 3. Typowanie wszystkiego naraz

To często kończy się chaosem.

### 4. Traktowanie checkera jak wroga

Jeśli narzędzie coś zgłasza, zwykle warto zrozumieć dlaczego, a nie tylko je uciszyć.

## Jak rozsądnie pracować z błędami typów

Dobre pytania przy błędzie:

- czy kontrakt funkcji jest źle opisany,
- czy kod runtime rzeczywiście jest niebezpieczny,
- czy tu powinien być węższy typ,
- czy przypadkiem nie użyłem `Any` albo złego `Optional`,
- czy ten błąd nie pokazuje realnego problemu architektonicznego.

## Typing a refaktoryzacja

To jedna z największych wartości.

Gdy zmieniasz API albo przenosisz logikę między modułami, checker typów potrafi szybko pokazać miejsca, które przestały być spójne.

W większym kodzie to ogromna pomoc.

## Kiedy typing może przeszkadzać

Jeśli:

- projekt jest bardzo eksperymentalny,
- kod żyje 15 minut,
- adnotacje są cięższe niż sama logika,
- narzędzie wymusza zbyt dużo formalizmu na prostym kodzie,

to trzeba zachować rozsądek.

Zaawansowany typing ma pomagać, nie dominować.

## Mini strategia dla projektu

Rozsądna ścieżka wygląda tak:

1. typuj nowe moduły,
2. typuj warstwy publiczne,
3. unikaj `Any`, jeśli da się go usunąć,
4. dodawaj `Protocol`, generyki i `TypeGuard` tam, gdzie naprawdę pomagają,
5. uruchamiaj checker regularnie.

## Typowe błędy początkujących

- mylenie typingu z runtime walidacją,
- nadmiar `Any`,
- zbyt ciężkie typowanie bez potrzeby,
- brak strategii stopniowego wdrażania,
- ignorowanie błędów zamiast rozumienia ich przyczyny.

## Szybka ściąga

- `mypy` i `pyright` wspierają statyczną analizę typów,
- największy zysk dają w większym i dłużej utrzymywanym kodzie,
- nie zastępują testów ani walidacji runtime,
- najlepiej wdrażać je iteracyjnie i świadomie.

## Ćwiczenia

1. Wybierz mały moduł i opisz, jakie błędy typów checker mógłby tam znaleźć.
2. Zaprojektuj plan wdrożenia typingu do istniejącego projektu.
3. Wskaż miejsca, gdzie `Any` osłabia jakość typów.
4. Opisz różnicę między błędem wykrytym przez test a błędem wykrytym przez checker typów.
5. Przygotuj własną checklistę rozsądnego używania `mypy` lub `pyright`.

## Najważniejsze do zapamiętania

- Typy dają pełniejszą wartość dopiero razem z checkerem statycznym.
- `mypy` i `pyright` pomagają wykrywać problemy wcześniej.
- Największy sens mają w większym i wielokrotnie używanym kodzie.
- Nie zastępują testów ani walidacji runtime.
- Najlepiej wdrażać je stopniowo i bez przesadnego formalizmu.
