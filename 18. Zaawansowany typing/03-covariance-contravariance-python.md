# Covariance i contravariance w Pythonie

## Dlaczego ten temat wydaje się trudny

Bo brzmi bardzo teoretycznie.

Na szczęście do praktycznego użycia nie musisz znać całej teorii formalnej. Wystarczy dobra intuicja.

Ten temat pojawia się wtedy, gdy system typów próbuje odpowiedzieć:

- czy typ bardziej szczegółowy można bezpiecznie podstawić tam, gdzie oczekiwany jest typ bardziej ogólny,
- i odwrotnie.

## Intuicja na przykładzie `Animal` i `Dog`

Załóżmy:

- `Dog` jest rodzajem `Animal`.

Czyli pojedynczy `Dog` może być użyty tam, gdzie oczekiwany jest `Animal`.

To jest intuicyjnie proste.

Problem robi się wtedy, gdy w grę wchodzą:

- kolekcje,
- callbacki,
- generyczne interfejsy.

## Covariance

Najprostsza intuicja:

- jeśli `Dog` jest `Animal`,
- to `Container[Dog]` może być traktowany jak `Container[Animal]`.

Ale tylko wtedy, gdy to jest bezpieczne.

Covariance zwykle dobrze pasuje do typów, które **dają** Ci wartości, a nie pozwalają ich dowolnie wkładać.

## Contravariance

Najprostsza intuicja:

- jeśli coś przyjmuje `Animal`,
- to może też obsłużyć `Dog`, bo `Dog` jest szczególnym przypadkiem `Animal`.

To dlatego contravariance często pojawia się przy callbackach i funkcjach przyjmujących argumenty.

## Dlaczego to ma znaczenie praktyczne

Bo bez tej intuicji czasem trudno zrozumieć, dlaczego checker typów akceptuje lub odrzuca pewne podstawienia.

To nie jest złośliwość narzędzia. To próba zachowania bezpieczeństwa typów.

## Intuicja dla kolekcji

Wyobraź sobie listę psów i listę zwierząt.

Gdyby każdą `list[Dog]` można było bezpiecznie traktować jako `list[Animal]`, to ktoś mógłby do tej listy dołożyć kota. A wtedy lista psów przestaje być listą psów.

To pokazuje, dlaczego temat variance jest związany z mutowalnością.

## Intuicja dla callbacków

Jeśli masz funkcję, która umie obsłużyć każde `Animal`, to poradzi sobie też z `Dog`.

Dlatego w przypadku funkcji przyjmujących argumenty pojawia się odwrócona intuicja niż przy typach zwracanych.

## Kiedy ten temat realnie się pojawia

Najczęściej przy:

- generycznych interfejsach,
- callbackach,
- `Protocol`,
- typach z biblioteki standardowej,
- bardziej precyzyjnym modelowaniu kontenerów.

## Czy trzeba umieć to formalnie

Na start nie.

Wystarczy zapamiętać dwa praktyczne pytania:

1. Czy ten typ głównie **zwraca** dane?
2. Czy ten typ głównie **przyjmuje** dane?

To bardzo pomaga zbudować intuicję.

## Najczęstszy błąd

Początkujący często próbują rozumieć variance wyłącznie jako abstrakcyjne nazwy.

Lepiej rozumieć to przez bezpieczeństwo podstawień typów.

## Przykład myślowy

### Covariance

Czy czytnik zwierząt, który tylko zwraca `Dog`, może być traktowany jako czytnik `Animal`?

Często tak, bo `Dog` jest `Animal`.

### Contravariance

Czy handler, który umie przyjąć dowolne `Animal`, może zostać użyty tam, gdzie ktoś poda mu `Dog`?

Też często tak.

## Typowe błędy początkujących

- próba uczenia się samych nazw bez intuicji,
- ignorowanie roli mutowalności,
- frustracja, że checker typów "czepia się" podstawień,
- oczekiwanie, że wszystkie generyki będą działały intuicyjnie bez dodatkowych zasad.

## Kiedy to ma sens praktycznie

W codziennym kodzie nie zawsze będziesz jawnie pisał o covariance i contravariance.

Ale bardzo warto rozumieć ten temat, gdy:

- typujesz bardziej zaawansowane API,
- pracujesz z callbackami,
- tworzysz własne generyczne abstrakcje,
- chcesz rozumieć komunikaty `mypy` lub `pyright`.

## Szybka ściąga

- covariance często dotyczy typów, które zwracają dane,
- contravariance często dotyczy typów, które przyjmują dane,
- mutowalność bardzo wpływa na to, co jest bezpieczne,
- najważniejsza jest intuicja bezpieczeństwa podstawień typów.

## Ćwiczenia

1. Wytłumacz covariance na przykładzie `Animal` i `Dog`.
2. Wytłumacz contravariance na przykładzie callbacka.
3. Opisz, dlaczego mutowalna lista komplikuje podstawienia typów.
4. Wskaż, gdzie ten temat może się pojawić przy `Protocol`.
5. Zrób własną notatkę: co jest dla Ciebie najważniejsze praktycznie w variance.

## Najważniejsze do zapamiętania

- Covariance i contravariance opisują bezpieczeństwo podstawień typów.
- Nie trzeba zaczynać od teorii formalnej, wystarczy dobra intuicja.
- Temat bardzo wiąże się z mutowalnością i callbackami.
- W praktyce jest ważny głównie przy bardziej zaawansowanych abstrakcjach.
- Jeśli rozumiesz, kto przyjmuje dane, a kto je zwraca, masz już dużą część potrzebnej intuicji.
