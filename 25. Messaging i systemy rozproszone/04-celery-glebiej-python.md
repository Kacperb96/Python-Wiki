# Celery glebiej python

## O czym jest ten rozdział

Celery to jedno z najczęściej spotykanych narzędzi w pythonowych backendach do wykonywania zadań w tle.

Na poziomie podstawowym myśli się o nim zwykle tak:

- mam task,
- wrzucam go do kolejki,
- worker go wykona.

To poprawna intuicja, ale w prawdziwej pracy szybko pojawiają się ważniejsze pytania:

- kiedy task powinien być użyty,
- co zrobić z retry,
- jak pilnować idempotencji,
- jak obsługiwać błędy,
- jak nie zrobić z Celery ukrytego chaosu w architekturze.

## Najprostsza intuicja Celery

Celery pozwala oddzielić zlecenie zadania od jego wykonania.

Najczęściej wygląda to tak:

- aplikacja publikuje task,
- broker przenosi wiadomość,
- worker Celery odbiera task,
- task wykonuje logikę poza request-response.

## Typowy flow

1. request trafia do backendu,
2. backend zapisuje ważny stan,
3. backend wywołuje task Celery,
4. worker odbiera zadanie,
5. task wykonuje pracę w tle,
6. wynik albo efekt uboczny pojawia się później.

## Typowe zastosowania Celery

Celery dobrze pasuje do zadań takich jak:

- wysyłka maili,
- generowanie PDF,
- przeliczanie raportów,
- import lub eksport danych,
- integracje z zewnętrznymi usługami,
- zadania cykliczne.

## Kiedy Celery ma sens

Celery ma sens, gdy:

- zadanie nie musi zakończyć się w tym samym requestcie,
- operacja trwa długo,
- awaria zewnętrznej usługi nie powinna blokować użytkownika,
- chcesz skalować liczbę workerów niezależnie od weba,
- potrzebujesz retry i przetwarzania w tle.

## Kiedy Celery może być przerostem formy

Celery może być zbyt ciężkie, gdy:

- zadanie jest bardzo proste i rzadkie,
- system nie potrzebuje jeszcze osobnej infrastruktury workerów,
- da się bezpieczniej i prościej zrobić to synchronicznie,
- zespół nie ma jeszcze potrzeby wprowadzania większej złożoności operacyjnej.

## Minimalna intuicja kodowa

To nie jest pełna konfiguracja, tylko model myślenia.

```python
from celery import Celery

app = Celery("tasks")


@app.task
def send_order_email(order_id: int):
    print(f"Sending email for order {order_id}")
```

Wywołanie:

```python
send_order_email.delay(123)
```

Najważniejsza intuicja:

- `delay()` nie wykonuje zadania od razu w tym samym procesie webowym,
- tylko publikuje je do dalszego przetwarzania.

## Output myślowy

### Request webowy

```text
order saved
celery task published
response returned to user
```

### Worker później

```text
task received
sending email for order 123
success
```

To właśnie jest podstawowa wartość Celery.

## Retry w Celery

To jeden z najważniejszych tematów.

Jeśli task rozmawia z czymś zawodnym, np. zewnętrznym API, retry bywa bardzo potrzebne.

Ale wracamy do kluczowej zasady:

- retry bez idempotencji jest groźne.

Przykład:

- wysyłka maila zwykle znosi retry lepiej,
- obciążenie konta albo naliczenie punktów już dużo gorzej.

## Task nie jest magicznie bezpieczny

To częsty błąd początkujących.

Samo wrzucenie czegoś do Celery nie rozwiązuje automatycznie:

- dubli,
- utraty wiadomości,
- problemów idempotencji,
- problemów spójności z bazą,
- złej architektury zadania.

Celery daje narzędzie. Odpowiedzialność projektowa nadal zostaje po stronie zespołu.

## Co powinien robić dobry task

Dobry task zwykle jest:

- dość wąski odpowiedzialnościowo,
- możliwie idempotentny,
- odporny na retry,
- dobrze logowany,
- łatwy do ponownego uruchomienia,
- oderwany od nadmiernej logiki webowej.

## Czego unikać

### 1. Zbyt grubych tasków

Jeśli jeden task robi:

- aktualizację bazy,
- trzy integracje,
- raport,
- mail,
- i jeszcze logikę biznesową,

to trudniej to diagnozować i retry staje się bardziej ryzykowne.

### 2. Ukrywania krytycznej logiki tylko w taskach bez kontroli stanu

Jeśli task jest krytyczny dla biznesu, musisz wiedzieć:

- kiedy został opublikowany,
- czy się wykonał,
- czy da się go odtworzyć,
- co się stanie po błędzie.

### 3. Publikowania taska zanim stan w bazie jest bezpiecznie zapisany

To bardzo ważne i prowadzi nas do outbox pattern.

### 4. Zakładania, że worker wykona wszystko dokładnie raz

To niebezpieczne założenie.

## Mini case study: PDF faktury

Masz flow:

- zamówienie zostało opłacone,
- trzeba wygenerować PDF faktury.

### Słabszy wariant

Generujesz PDF w requestcie użytkownika.

Efekt:

- request może długo trwać,
- timeout psuje UX,
- chwilowy problem z generowaniem psuje flow płatności.

### Lepszy wariant

- zapisujesz status zamówienia,
- publikujesz task `generate_invoice_pdf`,
- worker generuje plik osobno.

To dużo częstszy i dojrzalszy wzorzec.

## Taski okresowe

Celery często używa się też do zadań cyklicznych.

Przykłady:

- czyszczenie wygasłych danych,
- nocne raporty,
- synchronizacja stanów,
- przypomnienia mailowe.

Tu również ważne są:

- idempotencja,
- logowanie,
- kontrola czasu wykonania,
- świadomość, co się stanie, jeśli zadanie odpali się drugi raz.

## Co Pythonowiec powinien rozumieć

Dobrze, żebyś umiał:

- rozpoznać, które operacje sensownie nadają się do Celery,
- nie wrzucać tam wszystkiego automatycznie,
- projektować taski jako małe i przewidywalne,
- łączyć retry z idempotencją,
- pamiętać, że worker to część architektury, a nie tylko narzędzie pomocnicze.

## Output myślowy

### Naiwne użycie Celery

- "wrzućmy to do taska, będzie szybciej",
- brak myślenia o stanie, retry i dubelkach,
- system z czasem robi się trudny do debugowania.

### Dojrzalsze użycie Celery

- task ma jasny cel,
- stan główny jest zapisany sensownie,
- retry jest kontrolowane,
- skutki uboczne są projektowane świadomie.

## Najważniejsze do zapamiętania

- Celery służy do wykonywania pracy w tle, nie do magicznego naprawiania architektury.
- Task powinien być mały, przewidywalny i odporny na retry.
- Retry w Celery bez idempotencji jest ryzykowne.
- Nie każda operacja nadaje się do asynchronicznego taska.
- Worker jest częścią architektury systemu i trzeba go projektować tak samo świadomie jak API.

## Ćwiczenia

1. Podaj trzy zadania, które dobrze pasują do Celery, i dwa, które mogą nie pasować.
2. Wyjaśnij własnymi słowami, czemu `delay()` nie oznacza natychmiastowego wykonania zadania.
3. Opisz ryzyko retry taska bez idempotencji.
4. Zaprojektuj prosty task generowania PDF z bezpieczniejszym flow publikacji.
5. Wymyśl przykład zbyt grubego taska i rozbij go na mniejsze odpowiedzialności.
