# Pipeline lint test typecheck build python

## O czym jest ten rozdział

To jest punkt wejścia do całego działu CI/CD.

Na początku wielu osobom pipeline kojarzy się po prostu z tym, że "na GitHubie coś się odpala po pushu".

To za mało.

Pipeline to tak naprawdę zautomatyzowana ścieżka sprawdzania jakości zmiany i przygotowania artefaktu do dalszych etapów.

Bardzo często rdzeń takiej ścieżki wygląda mniej więcej tak:

- lint,
- test,
- typecheck,
- build.

## Najprostsza intuicja pipeline'u

Pipeline odpowiada na pytanie:

- czy ta zmiana w ogóle powinna pójść dalej?

Najprościej:

- kod trafia do systemu CI,
- kolejne kroki sprawdzają jego jakość,
- jeśli coś nie przejdzie, zmiana się zatrzymuje,
- jeśli wszystko przejdzie, można myśleć o merge, release albo wdrożeniu.

## Dlaczego pipeline jest ważny

Bez pipeline'u zespół łatwo wpada w model:

- każdy sprawdza coś po swojemu,
- część rzeczy odpala lokalnie, część nie,
- standard jakości jest nierówny,
- regresje wchodzą za łatwo.

Pipeline pomaga ujednolicić minimalny poziom zaufania do zmiany.

## Lint: po co jest

Lint sprawdza styl, jakość i część prostych problemów statycznych.

Najprostsza intuicja:

- pomaga wychwycić oczywiste rzeczy wcześnie,
- odciąża review od części mechanicznych uwag,
- pilnuje spójności kodu.

To nie zastępuje testów ani myślenia architektonicznego, ale jest bardzo dobrym pierwszym filtrem.

## Test: po co jest

Testy sprawdzają zachowanie kodu.

Najprościej:

- czy obecna zmiana nie psuje istniejących funkcji,
- czy nowa logika robi to, co obiecuje.

To zwykle najważniejszy element zaufania do zmiany, ale nadal nie jedyny.

## Typecheck: po co jest

Typecheck sprawdza spójność typów statycznych.

Najprościej:

- łapie część błędów, zanim kod się uruchomi,
- poprawia przewidywalność większego kodu,
- wzmacnia bezpieczeństwo refaktoryzacji.

W projektach z typingiem to bardzo praktyczny element pipeline'u.

## Build: po co jest

Build odpowiada na pytanie:

- czy z tego kodu da się zbudować artefakt, który naprawdę nadaje się do uruchomienia albo publikacji?

To może być:

- paczka Pythonowa,
- obraz Dockera,
- inny artefakt wdrożeniowy.

To bardzo ważne, bo testy mogą przejść, a build artefaktu i tak może się wysypać.

## Kolejność ma sens

Klasyczny pipeline często układa się właśnie tak:

1. lint,
2. test,
3. typecheck,
4. build.

Powód jest prosty:

- tańsze i szybsze sprawdzenia często warto robić wcześniej,
- cięższe etapy zostawiasz dalej, jeśli kod już przeszedł podstawowy filtr.

To oczywiście zależy od projektu, ale intuicja jest dobra.

## Minimalny przykład myślowy

Masz zmianę w API.

Pipeline robi:

- lint sprawdza jakość kodu,
- testy sprawdzają zachowanie endpointów,
- typecheck sprawdza zgodność typów,
- build buduje obraz aplikacji.

Jeśli typecheck albo build padnie, zmiana nie powinna iść dalej tak, jakby nic się nie stało.

## Output myślowy

### Zielony pipeline

```text
lint: ok
tests: ok
typecheck: ok
build: ok
```

### Czerwony pipeline

```text
lint: ok
tests: ok
typecheck: failed
build: skipped
```

Najważniejsza intuicja:

- pipeline nie jest po to, żeby "coś sobie odpalić",
- tylko po to, żeby blokować przejście zmian, które nie spełniają ustalonych warunków.

## Before/after

### Bez sensownego pipeline'u

- jakość zależy bardziej od osoby niż od procesu,
- łatwo przepuścić regresję,
- build może się zepsuć dopiero bardzo późno.

### Z sensownym pipeline'em

- zespół ma wspólny próg jakości,
- część problemów wychodzi natychmiast,
- zmiany są bardziej przewidywalne.

## Częste pułapki

### 1. Pipeline robi za mało

Np. odpala tylko testy, a w projekcie ważny jest też typing i build obrazu.

### 2. Pipeline robi za dużo bez myślenia

Jeśli pipeline jest bardzo ciężki i wolny bez uzasadnienia, zespół zaczyna go traktować jak przeszkodę.

### 3. Brak spójności między lokalnym a CI

Lokalnie coś przechodzi, w CI nie.

To szybko frustruje i psuje zaufanie do procesu.

### 4. Zielony pipeline traktowany jak gwarancja idealności

To też błąd.

Zielony pipeline oznacza, że przeszły konkretne kontrole, a nie że kod jest z definicji świetny architektonicznie.

## Mini case study: projekt z typingiem i Dockerem

Masz projekt FastAPI.

Pipeline powinien sensownie sprawdzić:

- styl i linter,
- testy,
- mypy lub pyright,
- build obrazu Dockera.

Jeśli build obrazu nie jest weryfikowany, możesz mieć kod, który wygląda dobrze w CI, ale nie daje się wdrożyć.

To bardzo częsty praktyczny problem.

## Co Pythonowiec powinien rozumieć

Dobrze, żebyś umiał:

- odróżnić rolę lintu, testów, typechecku i buildu,
- rozumieć, że pipeline to nie tylko odpalanie testów,
- myśleć o pipeline'ie jako o filtrze jakości i gotowości do dalszych etapów,
- rozpoznawać, kiedy pipeline jest zbyt słaby albo zbyt ciężki,
- traktować CI jako część procesu inżynierskiego, a nie tylko automatyczny gadżet.

## Output myślowy

### Słaby pipeline

- daje mało zaufania,
- przepuszcza zbyt wiele problemów,
- albo przeciwnie: jest ciężki i chaotyczny bez sensu.

### Dojrzalszy pipeline

- ma jasny cel,
- sprawdza rzeczy naprawdę istotne,
- zatrzymuje zmianę wtedy, gdy trzeba,
- buduje zaufanie do dalszych etapów procesu.

## Najważniejsze do zapamiętania

- Pipeline odpowiada na pytanie, czy zmiana może iść dalej.
- `lint -> test -> typecheck -> build` to bardzo sensowny rdzeń wielu projektów Pythonowych.
- Każdy z tych etapów sprawdza inny rodzaj ryzyka.
- Zielony pipeline nie zastępuje myślenia, ale bardzo wzmacnia jakość procesu.
- Dobrze zaprojektowany pipeline jest wsparciem dla zespołu, nie przypadkową przeszkodą.

## Ćwiczenia

1. Wyjaśnij własnymi słowami rolę lintu, testów, typechecku i buildu.
2. Opisz, czemu build artefaktu warto sprawdzać jeszcze przed releasem.
3. Wypisz dwa ryzyka pipeline'u zbyt słabego i dwa ryzyka pipeline'u zbyt ciężkiego.
4. Rozpisz pipeline dla projektu FastAPI + Docker + mypy.
5. Wytłumacz, czemu zielony pipeline nie oznacza automatycznie idealnego kodu.
