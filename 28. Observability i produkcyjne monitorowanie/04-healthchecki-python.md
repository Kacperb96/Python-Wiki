# Healthchecki python

## O czym jest ten rozdział

W produkcji bardzo łatwo pomylić dwa różne stany:

- proces żyje,
- usługa naprawdę działa sensownie.

To nie jest to samo.

Właśnie dlatego healthchecki są tak ważne.

Pomagają odpowiedzieć na pytanie:

- czy ta usługa wygląda na zdrową z punktu widzenia działania operacyjnego?

## Najprostsza intuicja

Healthcheck to prosty mechanizm sprawdzania, czy usługa jest w stanie podstawowo działać.

Najprościej:

- ktoś pyta usługę: "czy jesteś zdrowa?",
- usługa odpowiada: "tak" albo "nie".

To może być:

- endpoint HTTP,
- proste sprawdzenie procesu,
- test połączenia z krytyczną zależnością,
- inny lekki sygnał zdrowia.

## Po co healthcheck ma sens

Healthcheck pomaga, gdy chcesz:

- szybko wykrywać niedziałające instancje,
- odróżnić działający proces od niedziałającej usługi,
- sterować restartami albo routingiem ruchu,
- lepiej widzieć stan komponentów w środowisku.

To bardzo praktyczne i operacyjne narzędzie.

## Najprostszy przykład

Masz endpoint:

```text
GET /health
```

Jeśli aplikacja jest podstawowo zdrowa, odpowiada np.:

```json
{
  "status": "ok"
}
```

Najważniejsza intuicja:

- healthcheck ma być lekki,
- szybki,
- prosty do interpretacji.

## Healthcheck nie jest pełnym testem biznesowym

To bardzo ważne.

Healthcheck nie powinien próbować wykonywać całego flow użytkownika typu:

- zaloguj się,
- utwórz zamówienie,
- wyślij mail,
- zaktualizuj CRM.

To byłoby za ciężkie i za kruche.

Healthcheck powinien raczej odpowiadać na pytanie:

- czy usługa w podstawowym sensie nadaje się do dalszego użycia?

## Minimalny przykład w Pythonie

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}
```

To bardzo prosty start i dobra intuicja bazowa.

## Co może sprawdzać healthcheck

To zależy od systemu, ale często może obejmować:

- czy aplikacja wstała,
- czy główna pętla eventów działa,
- czy krytyczna zależność nie jest ewidentnie martwa,
- czy konfiguracja startowa jest poprawna.

Ale trzeba uważać, by nie zrobić z niego ciężkiego mini testu integracyjnego.

## Before/after

### Brak sensownego healthchecka

- proces może żyć, ale usługa nie działa poprawnie,
- system później zauważa problem,
- trudniej automatyzować reakcję na awarię.

### Sensowny healthcheck

- szybciej widać problem,
- łatwiej odsiać martwe instancje,
- operacje i routing są bardziej świadome.

## Mini case study: API wstało, ale nie działa

Masz backend, który wystartował procesowo.

Jednak:

- konfiguracja połączenia z bazą jest zła,
- albo ważna zależność jest niedostępna,
- albo aplikacja nie skończyła poprawnie inicjalizacji.

Bez healthchecka może wyglądać, jakby wszystko było okej.

Z sensownym healthcheckiem szybciej widzisz, że instancja nie nadaje się jeszcze do pracy.

## Mini case study: worker działa jako proces, ale nie robi nic sensownego

Worker może żyć procesowo, ale:

- nie łączy się z brokerem,
- nie przetwarza zadań,
- utknął w błędnym stanie.

To pokazuje, że healthcheck bywa ważny nie tylko dla weba, ale też dla innych ról systemowych.

## Częste pułapki

### 1. Healthcheck zbyt ciężki

Jeśli robi za dużo, sam staje się źródłem problemów.

### 2. Healthcheck zbyt płytki

Jeśli zawsze zwraca `200 OK`, nawet gdy system praktycznie nie działa, ma małą wartość.

### 3. Mylenie healthchecka z pełnym monitoringiem

Healthcheck to tylko jeden element observability.

### 4. Brak spójności między rolami

Web ma check, worker nie, scheduler nie, i obraz zdrowia systemu jest niepełny.

### 5. Brak refleksji, co znaczy "zdrowy"

Dla różnych usług zdrowie może znaczyć co innego.

## Co Pythonowiec powinien rozumieć

Dobrze, żebyś umiał:

- odróżnić żyjący proces od zdrowej usługi,
- projektować healthcheck lekki, ale użyteczny,
- rozumieć, że różne role systemowe mogą potrzebować różnych checków,
- nie robić z healthchecka zbyt ciężkiego testu biznesowego,
- traktować healthcheck jako część operacyjnej widoczności systemu.

## Output myślowy

### Bez healthchecka

- system może długo udawać, że działa,
- trudniej automatyzować reakcję na problem.

### Z sensownym healthcheckiem

- szybciej widać, które instancje są podejrzane,
- łatwiej ograniczać wpływ awarii.

## Najważniejsze do zapamiętania

- Healthcheck sprawdza podstawowe zdrowie usługi.
- Nie jest pełnym testem biznesowym ani zastępstwem dla monitoringu.
- Powinien być lekki, szybki i sensownie zaprojektowany.
- Różne role systemu mogą potrzebować różnych checków.
- To ważny praktyczny element observability i operacji.

## Ćwiczenia

1. Wyjaśnij własnymi słowami, czemu żyjący proces nie zawsze oznacza zdrową usługę.
2. Podaj trzy rzeczy, które healthcheck może sprawdzać sensownie.
3. Opisz, czemu zbyt ciężki healthcheck jest złym pomysłem.
4. Wymyśl prosty endpoint `/health` dla backendu API.
5. Opisz, jak healthcheck pomógłby w diagnozie problemu "usługa niby działa, ale użytkownicy dostają błędy".
