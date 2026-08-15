# 18. Zaawansowany typing

To jest folder, który przesuwa typowanie w Pythonie z poziomu:

- `def add(a: int, b: int) -> int`

na poziom:

- świadomego projektowania interfejsów,
- lepszego opisywania zależności między typami,
- bardziej precyzyjnego kontraktu w większym kodzie,
- sensownego używania narzędzi takich jak `mypy` i `pyright`.

To ważny krok, bo proste adnotacje typów to dopiero początek. W większych projektach pojawiają się problemy, których zwykłe `int`, `str`, `list[str]` i `dict[str, int]` nie opisują wystarczająco dobrze.

## Po co ten folder

W praktyce typowanie zaczyna być naprawdę wartościowe wtedy, gdy kod:

- ma więcej modułów,
- pracuje na callbackach,
- ma własne kontrakty i interfejsy,
- używa dekoratorów,
- operuje na danych generycznych,
- ma być czytelny i bezpieczny dla innych programistów.

Właśnie wtedy pojawiają się takie pojęcia jak:

- `Protocol`,
- `TypeVar`,
- generyki,
- covariance,
- contravariance,
- `ParamSpec`,
- `TypeGuard`,
- `overload`.

## Czego nauczysz się w tym dziale

Po przerobieniu tego folderu powinieneś rozumieć:

- jak opisywać interfejs po zachowaniu przez `Protocol`,
- jak pisać funkcje i klasy generyczne,
- po co istnieją variance i kiedy się pojawiają,
- jak typować dekoratory bez gubienia sygnatury,
- jak zawężać typy przez `TypeGuard`,
- kiedy używać `@overload`,
- jak używać `mypy` i `pyright` w większym kodzie bez przesady i bez chaosu.

## Najważniejsza zasada

Zaawansowany typing ma pomagać projektować kod lepiej, a nie robić z kodu pokaz składni.

To bardzo ważne.

Jeśli typowanie:

- poprawia kontrakt,
- zmniejsza liczbę pomyłek,
- poprawia czytelność,
- ułatwia refaktoryzację,

to jest świetne.

Jeśli natomiast:

- przykrywa logikę ścianą adnotacji,
- jest bardziej skomplikowane niż problem,
- zostało dodane tylko po to, żeby wyglądać profesjonalnie,

to zwykle jest przesadą.

## Jak czytać ten folder

Najlepiej iść po kolei:

1. `01-protocol-python.md`
2. `02-typevar-i-generyki-python.md`
3. `03-covariance-contravariance-python.md`
4. `04-paramspec-python.md`
5. `05-typeguard-python.md`
6. `06-overload-python.md`
7. `07-mypy-i-pyright-wiekszy-kod-python.md`

Ta kolejność ma sens, bo najpierw poznajesz praktyczne kontrakty i generyki, potem trudniejsze aspekty systemu typów, a na końcu narzędzia w realnym projekcie.

## Na co szczególnie uważać

W tym folderze bardzo łatwo o dwa błędy.

### Błąd 1: typowanie zbyt słabe

Czyli np. wszędzie `Any`, byle narzędzie przestało krzyczeć.

To zabija sens typowania.

### Błąd 2: typowanie zbyt ciężkie

Czyli system adnotacji tak skomplikowany, że sam kod staje się mniej zrozumiały.

Tu też tracisz korzyści.

Celem jest środek:

- typy mają być użyteczne,
- precyzyjne tam, gdzie trzeba,
- proste tam, gdzie da się pozostać prostym.

## Po czym poznasz, że temat naprawdę siedzi

Dobry znak, jeśli potrafisz:

- opisać kontrakt klasy bez dziedziczenia przez `Protocol`,
- napisać funkcję generyczną, która zachowuje typ wejścia,
- zrozumieć, dlaczego dekorator bez `ParamSpec` traci informację o sygnaturze,
- zawęzić typ po własnym checkerze przez `TypeGuard`,
- rozpoznać, kiedy `@overload` coś realnie poprawia,
- sensownie skonfigurować `mypy` lub `pyright` bez wojny z kodem.

## Jak najlepiej ćwiczyć

Najlepiej nie traktować tego folderu jak samej teorii.

Dobra praktyka to:

1. napisz prostą wersję bez zaawansowanego typingu,
2. zobacz, gdzie kontrakt jest nieprecyzyjny,
3. dopiero wtedy dodaj `Protocol`, `TypeVar`, `ParamSpec` albo `TypeGuard`,
4. oceń, czy faktycznie poprawiło to kod.

To ważne, bo zaawansowany typing powinien rozwiązywać realne problemy, a nie być sztuką dla sztuki.

## Podsumowanie

To jest jeden z bardziej wymagających folderów, ale też jeden z tych, które mocno podnoszą poziom dojrzałości kodu. Po jego opanowaniu będziesz znacznie lepiej rozumiał nie tylko adnotacje, ale też sam projekt interfejsów i kontraktów w Pythonie.
