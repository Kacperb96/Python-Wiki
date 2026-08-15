# Readiness liveness python

## O czym jest ten rozdział

Healthcheck to dobry start, ale w praktyce bardzo ważne jest jeszcze mocniejsze rozróżnienie dwóch pytań:

- czy proces żyje,
- czy usługa jest gotowa przyjmować ruch.

Właśnie dlatego pojawiają się pojęcia:

- `liveness`,
- `readiness`.

To są dwa różne sygnały i mieszanie ich prowadzi do wielu problemów operacyjnych.

## Najprostsza intuicja liveness

Liveness odpowiada na pytanie:

- czy ten proces nadal żyje i nie utknął w stanie, z którego sam nie wyjdzie?

Najprościej:

- jeśli liveness nie przechodzi, proces wygląda na martwy albo zawieszony,
- system może uznać, że trzeba go zrestartować.

## Najprostsza intuicja readiness

Readiness odpowiada na pytanie:

- czy ta instancja jest gotowa przyjmować normalny ruch?

Najprościej:

- proces może już żyć,
- ale jeszcze nie być gotowy,
- np. bo trwa inicjalizacja albo ważna zależność nie działa.

## To nie jest to samo

To bardzo ważny punkt.

Możliwa jest sytuacja:

- `liveness = ok`,
- `readiness = fail`.

Przykład:

- aplikacja uruchomiła się jako proces,
- ale jeszcze nie połączyła się z bazą,
- więc nie powinna dostawać ruchu.

To jest całkowicie normalne.

## Przykład intuicyjny

Masz backend API.

### Liveness

Sprawdza:

- czy proces działa,
- czy główna pętla aplikacji odpowiada.

### Readiness

Sprawdza:

- czy aplikacja skończyła inicjalizację,
- czy ma wymagane zależności,
- czy sensownie może obsługiwać requesty.

## Before/after

### Bez rozróżnienia

- wszystko wrzucasz do jednego endpointu zdrowia,
- system nie wie, czy restartować usługę, czy tylko chwilowo odciąć ją od ruchu,
- reakcje operacyjne są mniej precyzyjne.

### Z rozróżnieniem

- liveness mówi o życiu procesu,
- readiness mówi o gotowości do ruchu,
- system może reagować mądrzej.

## Minimalny przykład myślowy

```python
from fastapi import FastAPI

app = FastAPI()
ready = False


@app.get("/liveness")
def liveness():
    return {"status": "alive"}


@app.get("/readiness")
def readiness():
    if not ready:
        return {"status": "not_ready"}
    return {"status": "ready"}
```

To tylko intuicja, ale bardzo dobrze pokazuje różnicę między:

- "proces żyje",
- a "usługa jest gotowa do ruchu".

## Kiedy readiness może być false

Typowe sytuacje:

- aplikacja jeszcze się inicjalizuje,
- migracja albo warmup jeszcze trwa,
- baza jest niedostępna,
- broker jest wymagany do działania danej roli,
- krytyczna zależność nie działa.

## Kiedy liveness może być false

Typowe sytuacje:

- proces się zawiesił,
- wpadł w stan, z którego nie wróci,
- pętla eventów przestała działać,
- usługa nie odpowiada nawet na minimalny check.

## Mini case study: web po deploymencie

Po wdrożeniu nowej wersji web startuje jako proces.

### Co może się dziać

- liveness jest już zielone,
- readiness jeszcze nie, bo baza nie jest gotowa albo inicjalizacja trwa.

To bardzo dobra rzecz, bo:

- system nie musi od razu restartować procesu,
- ale może jeszcze nie puszczać do niego normalnego ruchu.

## Mini case study: worker

Worker może żyć jako proces, ale nie być gotowy do sensownej pracy, jeśli:

- nie połączył się z brokerem,
- nie załadował konfiguracji,
- jest w stanie przejściowym po starcie.

To pokazuje, że readiness/liveness to nie tylko temat weba.

## Jakie checki powinny być lekkie

To bardzo ważne.

Zarówno liveness, jak i readiness nie powinny zamieniać się w ciężkie, kosztowne procesy.

Najprościej:

- liveness powinien być bardzo lekki,
- readiness może być trochę bogatszy, ale nadal rozsądny.

## Częste pułapki

### 1. Jeden endpoint robi wszystko naraz

Potem trudno odróżnić, czy system trzeba restartować, czy tylko odciąć od ruchu.

### 2. Liveness zbyt zależny od zewnętrznych systemów

Jeśli liveness pada przez chwilowy problem zależności, możesz prowokować niepotrzebne restarty.

### 3. Readiness zbyt płytki

Może zwracać "ready", mimo że aplikacja realnie nie jest gotowa.

### 4. Readiness zbyt ciężki

Sam staje się źródłem opóźnień i niestabilności.

### 5. Brak spójnego myślenia dla różnych ról

Web ma checki, worker nie, scheduler nie, i obraz systemu jest niepełny.

## Co Pythonowiec powinien rozumieć

Dobrze, żebyś umiał:

- odróżnić liveness od readiness,
- wiedzieć, że nie każda awaria zależności oznacza martwy proces,
- projektować checki pod konkretne pytania operacyjne,
- nie przeciążać checków zbyt ciężką logiką,
- stosować te pojęcia także poza samym webem, jeśli rola systemu tego wymaga.

## Output myślowy

### Bez rozróżnienia

- reakcje na problem są bardziej chaotyczne,
- trudniej poprawnie restartować albo odcinać ruch.

### Z rozróżnieniem

- system lepiej rozumie, czy instancję trzeba ubić, czy tylko chwilowo wyłączyć z obsługi ruchu,
- operacje są bardziej precyzyjne.

## Najważniejsze do zapamiętania

- Liveness mówi: "czy proces żyje?"
- Readiness mówi: "czy usługa jest gotowa do normalnej pracy?"
- To dwa różne pytania i dwa różne sygnały.
- Liveness powinien być bardzo lekki.
- Readiness może uwzględniać gotowość zależności, ale nadal musi być sensowny operacyjnie.

## Ćwiczenia

1. Wyjaśnij własnymi słowami różnicę między liveness i readiness.
2. Podaj przykład sytuacji, w której liveness jest zielony, a readiness czerwony.
3. Opisz, czemu liveness nie powinien zbyt mocno zależeć od zewnętrznych usług.
4. Wymyśl readiness check dla backendu API z bazą danych.
5. Rozpisz, jak readiness i liveness pomogłyby przy wdrożeniu nowej wersji usługi.
