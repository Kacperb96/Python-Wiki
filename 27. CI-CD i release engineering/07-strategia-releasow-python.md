# Strategia releasow python

## O czym jest ten rozdział

Release workflow odpowiada na pytanie, jak przygotować wersję.

Strategia releasów odpowiada na pytanie:

- jak często wydajemy,
- jak duże są releasy,
- jak ograniczamy ryzyko,
- jak planujemy tempo zmian,
- jak zachowujemy kontrolę nad tym, co trafia do użytkowników.

To bardzo praktyczny temat, bo dwa zespoły mogą mieć zupełnie różne dobre strategie releasowe zależnie od typu produktu.

## Najprostsza intuicja

Strategia releasów to zbiór zasad mówiących:

- kiedy robimy release,
- co może do niego wejść,
- jak go stabilizujemy,
- jak reagujemy na ryzyko i poprawki.

To nie jest tylko kalendarz. To sposób zarządzania zmianą.

## Małe i częste releasy vs duże i rzadkie releasy

To jedna z najważniejszych osi myślenia.

### Małe i częste releasy

Zalety:

- mniejszy zakres zmiany naraz,
- łatwiejsza diagnoza regresji,
- szybszy feedback,
- mniejsze ryzyko ogromnego releasu.

Wady:

- proces musi być dojrzały i przewidywalny,
- wymaga większej dyscypliny operacyjnej.

### Duże i rzadsze releasy

Zalety:

- mniej momentów wdrożeniowych,
- czasem wygodne przy ciężkich procesach organizacyjnych.

Wady:

- większa porcja ryzyka na raz,
- trudniejszy rollback i analiza problemów,
- większy stres releasowy.

Najczęściej dojrzalsze zespoły dążą raczej do mniejszych, bardziej przewidywalnych releasów.

## Release train: intuicja

Jedna z możliwych strategii to release train.

Najprościej:

- release wychodzi w ustalonym rytmie,
- np. co tydzień albo co dwa tygodnie,
- zmiany, które zdążą i spełnią warunki, jadą tym pociągiem,
- reszta czeka na kolejny.

To pomaga porządkować oczekiwania i ograniczać chaos typu "wrzućmy to jeszcze dziś na szybko".

## Continuous delivery a bardziej ręczny model

### Continuous delivery

System jest stale w stanie releasowalnym, a wydanie może nastąpić bardzo szybko po decyzji.

### Bardziej ręczny model

Release jest bardziej świadomie zbierany i stabilizowany przed publikacją.

Nie każdy projekt musi od razu iść w pełne continuous delivery, ale warto rozumieć kierunek.

## Hotfix: osobna ścieżka

Dobra strategia releasów powinna przewidywać sytuację awaryjną.

Czyli:

- co robimy, gdy trzeba szybko naprawić błąd na produkcji,
- czy hotfix idzie tą samą ścieżką,
- jak później scalamy go z głównym nurtem zmian.

To bardzo ważne, bo bez planu hotfix często robi organizacyjny chaos.

## Stabilizacja releasu

Przy większych zmianach czasem potrzebny jest moment stabilizacji.

Czyli:

- ograniczasz, co jeszcze może wejść,
- skupiasz się na poprawkach i walidacji,
- nie dorzucasz nowych ryzykownych elementów w ostatniej chwili.

To szczególnie ma sens przy releasach większych albo bardziej krytycznych.

## Before/after

### Słabsza strategia

- release dzieje się przypadkowo,
- zakres zmian jest nieprzewidywalny,
- priorytetem jest "wrzućmy to jeszcze szybko".

### Lepsza strategia

- zespół wie, jak wygląda rytm releasów,
- wiadomo, co może wejść do wersji,
- istnieje plan dla hotfixów i rollbacków,
- ryzyko jest rozkładane bardziej świadomie.

## Feature flags: ważne wsparcie strategii

Bardzo często dobra strategia releasów korzysta z feature flag.

Dzięki temu możesz:

- wdrożyć kod wcześniej,
- nie aktywować go od razu dla wszystkich,
- ograniczyć ryzyko uruchamiania funkcji.

To nie zastępuje releasu, ale bardzo go wspiera.

## Mini case study: mały zespół produktowy

Masz mały backend i niewielki zespół.

Sensowna strategia może być taka:

- releasy częste i małe,
- tag po każdej gotowej porcji zmian,
- staging przed produkcją,
- prosty hotfix flow,
- brak wielkiej biurokracji.

To często najlepsze rozwiązanie na tym poziomie skali.

## Mini case study: krytyczny system wewnętrzny

Masz system, którego błąd jest kosztowny dla firmy.

Tu sensowniejsza może być strategia bardziej ostrożna:

- mocniejsze quality gates,
- bardziej formalna walidacja releasu,
- release branch albo stabilizacja,
- wyraźny plan rollbacku,
- kontrolowany rollout.

Czyli strategia zależy od kosztu błędu, a nie tylko od upodobań zespołu.

## Częste pułapki

### 1. Zbyt duże releasy

Im więcej zmian w jednym rzucie, tym trudniej nad nimi zapanować.

### 2. Brak rytmu albo brak zasad

Wtedy wszystko staje się pilne i przypadkowe.

### 3. Brak ścieżki hotfix

Pierwsza awaria od razu rozwala proces.

### 4. Strategie zbyt ciężkie względem skali projektu

Jeśli mały zespół kopiuje bardzo złożony proces wielkiej organizacji, może tylko spowolnić pracę bez realnej korzyści.

### 5. Brak świadomości kosztu wdrożenia

Strategia releasów powinna być dopasowana do ryzyka biznesowego i kosztu błędu.

## Co Pythonowiec powinien rozumieć

Dobrze, żebyś umiał:

- odróżnić częsty mały release od dużego rzadkiego releasu jako świadome strategie,
- rozumieć, że strategia zależy od typu systemu i ryzyka,
- wiedzieć, po co istnieją hotfix flow, stabilizacja i feature flags,
- nie projektować procesu ani zbyt lekkiego, ani zbyt ciężkiego względem potrzeb,
- myśleć o release engineeringu jako o zarządzaniu zmianą, nie tylko automatyzacji.

## Output myślowy

### Chaotyczna strategia releasów

- zakres wersji jest nieprzewidywalny,
- zespół działa reaktywnie,
- awarie bardziej bolą.

### Dojrzalsza strategia releasów

- zmiana ma przewidywalny rytm,
- hotfix ma swoje miejsce,
- releasy są bardziej kontrolowane,
- ryzyko łatwiej ograniczać.

## Najważniejsze do zapamiętania

- Strategia releasów mówi, jak zarządzasz tempem i ryzykiem zmian.
- Małe, częste releasy często są łatwiejsze do opanowania niż duże, rzadkie releasy.
- Hotfix flow i plan stabilizacji to ważne elementy dojrzałego procesu.
- Feature flags mogą mocno wspierać bezpieczniejsze wydawanie zmian.
- Dobra strategia releasów musi być dopasowana do skali projektu i kosztu błędu.

## Ćwiczenia

1. Wyjaśnij własnymi słowami różnicę między małymi częstymi a dużymi rzadkimi release'ami.
2. Opisz, kiedy release train ma sens.
3. Wskaż, po co zespołowi potrzebna jest ścieżka hotfix.
4. Opisz, jak feature flags pomagają w strategii releasów.
5. Zaprojektuj prostą strategię releasów dla małego backendu Pythonowego.
