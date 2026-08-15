# Quality gates python

## O czym jest ten rozdział

Sam pipeline to jeszcze nie wszystko.

Możesz mieć pipeline, który coś odpala, ale nadal nie wiesz:

- co dokładnie blokuje merge,
- co blokuje release,
- kiedy zmiana jest wystarczająco dobra,
- co jest tylko ostrzeżeniem, a co twardym warunkiem przejścia dalej.

Tu właśnie wchodzą quality gates.

## Najprostsza intuicja

Quality gate to warunek, który zmiana musi spełnić, żeby przejść do kolejnego etapu procesu.

Najprościej:

- jeśli gate przejdzie, zmiana idzie dalej,
- jeśli nie przejdzie, proces się zatrzymuje.

To może dotyczyć:

- merge do głównej gałęzi,
- publikacji artefaktu,
- deploymentu na staging,
- deploymentu na produkcję.

## Po co quality gates istnieją

Bez quality gates bardzo łatwo wejść w model:

- pipeline coś pokazuje,
- ale i tak da się przepchnąć zmianę bez większej dyscypliny,
- standard jakości zależy bardziej od presji czasu niż od procesu.

Quality gates zamieniają oczekiwania jakościowe w konkretne zasady.

## Przykłady quality gates

Typowe quality gates to na przykład:

- testy muszą przejść,
- typecheck musi przejść,
- build musi się udać,
- coverage nie może spaść poniżej progu,
- wymagane review musi być zakończone,
- nie może być krytycznych podatności,
- release notes muszą istnieć,
- artefakt musi być podpisany albo oznaczony zgodnie z zasadą projektu.

## Gate a informacja diagnostyczna

To ważne rozróżnienie.

Nie wszystko, co pipeline mierzy, musi być od razu gate'em.

Przykład:

- możesz mierzyć czas builda,
- ale niekoniecznie blokować merge po jednej wolniejszej wartości.

Z kolei:

- failing tests bardzo często powinny być twardym gate'em.

Czyli nie każda metryka jest automatycznie warunkiem blokującym.

## Twarde i miękkie gate'y

To dobra intuicja praktyczna.

### Twardy gate

- bez spełnienia warunku zmiana nie idzie dalej.

Przykład:

- testy nie przeszły,
- build się nie zbudował,
- typowanie padło.

### Miękki gate albo ostrzeżenie

- system zgłasza problem,
- ale nie zawsze blokuje cały proces.

Przykład:

- niewielkie pogorszenie czasu builda,
- ostrzeżenie o stylu niskiego priorytetu,
- techniczny sygnał do poprawy później.

## Kiedy gate powinien być twardy

Twardy gate ma sens wtedy, gdy naruszenie naprawdę zwiększa ryzyko w sposób, którego zespół nie chce akceptować.

Przykłady:

- testy regresyjne nie przeszły,
- artefakt nie da się zbudować,
- nie ma wymaganej migracji lub walidacji,
- typowanie wykryło realny problem spójności.

## Kiedy zbyt wiele gate'ów szkodzi

To bardzo ważne.

Jeśli pipeline blokuje wszystko zbyt agresywnie i bez sensu, zespół zaczyna:

- traktować go jak wroga,
- szukać skrótów,
- obniżać zaufanie do procesu.

Czyli gate ma zwiększać jakość, a nie produkować biurokrację bez wartości.

## Before/after

### Słabszy model

- pipeline coś pokazuje,
- ale nie wiadomo, co naprawdę blokuje zmianę,
- część problemów jest ignorowana zależnie od sytuacji.

### Lepszy model

- zespół wie, jakie są twarde warunki przejścia,
- wartościowe ryzyka są zatrzymywane wcześnie,
- proces jest bardziej przewidywalny.

## Mini case study: projekt z mypy i Dockerem

Masz projekt backendowy, w którym ważne są:

- testy,
- mypy,
- build obrazu,
- podstawowe bezpieczeństwo dependency.

Sensowny zestaw gate'ów może wyglądać tak:

- failing tests blokują merge,
- failing mypy blokuje merge,
- failing build blokuje release,
- krytyczna podatność blokuje deployment.

To bardziej dojrzały model niż jedno wielkie "pipeline czerwony" bez jasnych zasad.

## Mini case study: coverage

Coverage to bardzo ciekawy przykład.

Może być użyteczne jako gate, ale tylko wtedy, gdy zespół rozumie jego sens.

Zły model:

- ślepy próg coverage jako cel sam w sobie.

Lepszy model:

- coverage jako jeden z sygnałów jakości,
- sensownie dopasowany do projektu,
- nie traktowany jako jedyna prawda o testach.

## Quality gates a release

Gate'y mogą działać na różnych poziomach.

### Dla merge

- testy,
- lint,
- typecheck,
- review.

### Dla release

- poprawne wersjonowanie,
- changelog,
- build artefaktu,
- finalna walidacja pipeline'u.

### Dla deploymentu

- dostępność artefaktu,
- zdrowie środowiska docelowego,
- wymagane zatwierdzenia,
- brak krytycznych blokad bezpieczeństwa.

To ważne, bo nie każdy gate dotyczy tego samego etapu.

## Co Pythonowiec powinien rozumieć

Dobrze, żebyś umiał:

- odróżnić kontrolę informacyjną od prawdziwego quality gate'u,
- rozumieć, które warunki naprawdę powinny blokować proces,
- nie projektować gate'ów zbyt luźnych ani zbyt biurokratycznych,
- myśleć o gate'ach osobno dla merge, release i deploymentu,
- traktować quality gate jako element zarządzania ryzykiem.

## Output myślowy

### Brak jasnych gate'ów

- proces jest mniej przewidywalny,
- decyzje są bardziej uznaniowe,
- ryzyko łatwiej przechodzi dalej.

### Sensowne gate'y

- wiadomo, co jest obowiązkowe,
- zespół ma jaśniejsze granice jakości,
- release i deployment są mniej przypadkowe.

## Najważniejsze do zapamiętania

- Quality gate to warunek przejścia do kolejnego etapu procesu.
- Nie każda metryka z pipeline'u musi być od razu gate'em.
- Twarde gate'y powinny chronić przed realnym ryzykiem.
- Zbyt wiele źle dobranych gate'ów może szkodzić procesowi.
- Merge, release i deployment mogą mieć różne zestawy gate'ów.

## Ćwiczenia

1. Wyjaśnij własnymi słowami, czym różni się quality gate od zwykłej informacji diagnostycznej.
2. Podaj trzy przykłady twardych gate'ów i dwa przykłady sygnałów, które nie muszą być od razu blokujące.
3. Opisz, kiedy coverage jako gate ma sens, a kiedy może prowadzić do złych zachowań.
4. Rozpisz quality gates osobno dla merge, release i deploymentu.
5. Wytłumacz, czemu zbyt agresywny zestaw gate'ów może szkodzić zespołowi.
