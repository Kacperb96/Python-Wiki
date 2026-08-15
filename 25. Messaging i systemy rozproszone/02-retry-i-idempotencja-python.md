# Retry i idempotencja python

## O czym jest ten rozdział

Gdy system pracuje z kolejkami, workerami albo zewnętrznymi usługami, błędy nie są wyjątkiem od reguły. One są normalną częścią życia systemu.

Bardzo szybko pojawia się pytanie:

- co zrobić, gdy zadanie nie powiedzie się za pierwszym razem?

Naturalna odpowiedź brzmi:

- spróbować ponownie.

To właśnie retry.

Ale tu pojawia się drugi, jeszcze ważniejszy temat:

- co jeśli ta sama operacja wykona się drugi raz?

Tu wchodzi idempotencja.

## Retry: najprostsza intuicja

Retry to ponowienie operacji po błędzie.

Najprostszy sens retry:

- zewnętrzna usługa miała chwilowy timeout,
- połączenie chwilowo padło,
- worker został przerwany,
- baza albo broker miały chwilowy problem.

W takich sytuacjach druga próba może się udać.

## Retry nie zawsze ma sens

To bardzo ważne.

Retry ma sens głównie przy błędach przejściowych.

Przykłady:

- timeout,
- chwilowy brak połączenia,
- krótkotrwałe przeciążenie,
- deadlock albo przejściowy konflikt.

Retry zwykle nie rozwiąże problemu, gdy:

- payload jest zły,
- walidacja biznesowa jest błędna,
- nie istnieje wymagany rekord,
- logika zadania jest wadliwa.

## Najprostsza intuicja idempotencji

Operacja idempotentna to taka, którą można wykonać wiele razy, a efekt końcowy pozostaje taki sam jak po jednym poprawnym wykonaniu.

Najprościej:

- jeśli wiadomość dojdzie dwa razy, system nie powinien zrobić szkody dwa razy.

## Przykład nieidempotentny

Masz task:

```python
def add_reward_points(user_id: int, points: int):
    user.points += points
```

Jeśli task wykona się dwa razy, użytkownik dostaje punkty podwójnie.

To klasyczny problem.

## Przykład bardziej idempotentny

Masz task:

```python
def mark_invoice_as_paid(invoice_id: int):
    invoice.status = "paid"
```

Jeśli status już jest `paid`, drugie wykonanie nie musi zmienić nic istotnego.

To dużo bezpieczniejszy wzorzec.

## Minimalna symulacja w Pythonie

### Nieidempotentne zachowanie

```python
balance = 0


def add_money(amount: int):
    global balance
    balance += amount


add_money(100)
add_money(100)
print(balance)
```

Output:

```text
200
```

Jeśli drugie wykonanie było przypadkowym dublem, wynik jest zły.

### Bardziej idempotentne zachowanie

```python
invoice = {"status": "pending"}


def mark_paid(record: dict):
    record["status"] = "paid"


mark_paid(invoice)
mark_paid(invoice)
print(invoice)
```

Output:

```text
{'status': 'paid'}
```

Drugie wykonanie nie robi dodatkowej szkody.

## Czemu retry bez idempotencji jest groźne

To jedna z najważniejszych lekcji całego folderu.

Jeśli system robi retry, a zadanie nie jest idempotentne, możesz dostać:

- podwójne maile,
- podwójne naliczenie punktów,
- podwójne obciążenie konta,
- wielokrotne wysłanie webhooka,
- duplikaty rekordów.

Czyli retry poprawia niezawodność techniczną, ale może zepsuć logikę biznesową.

## Najczęstsze źródła dubli

Duble mogą pojawić się, gdy:

- producer opublikuje wiadomość drugi raz,
- worker wykona zadanie i padnie przed potwierdzeniem,
- broker ponownie dostarczy wiadomość,
- klient wyśle to samo polecenie ponownie,
- system sam zrobi retry po błędzie.

Dlatego nie wolno zakładać modelu:

- "to na pewno wykona się dokładnie raz".

## Idempotency key: intuicja

Jedna z najważniejszych technik to klucz idempotencji.

Najprościej:

- każda operacja dostaje unikalny identyfikator,
- system zapisuje, że to żądanie już było przetworzone,
- powtórka z tym samym kluczem nie wykonuje skutków drugi raz.

## Przykład intuicyjny

```python
processed = set()


def process_payment(operation_id: str, amount: int):
    if operation_id in processed:
        return "already processed"

    processed.add(operation_id)
    return f"charged {amount}"


print(process_payment("op-1", 100))
print(process_payment("op-1", 100))
```

Output:

```text
charged 100
already processed
```

To bardzo uproszczone, ale dobrze oddaje ideę.

## Retry policy: o czym trzeba myśleć

Retry to nie tylko "spróbuj jeszcze raz".

Trzeba zdecydować:

- ile razy próbować,
- po jakim czasie,
- czy użyć backoff,
- kiedy przestać,
- co zrobić z wiadomością po wielu niepowodzeniach.

## Backoff: intuicja

Zamiast próbować od razu w pętli, często czekasz coraz dłużej między próbami.

To pomaga, gdy problem jest przejściowy i system potrzebuje chwili na odzyskanie stabilności.

## Before/after

### Słabszy model

- każde niepowodzenie kończy się utratą zadania,
- albo każde zadanie retry'ujesz bez limitu,
- albo retry robisz bez idempotencji.

### Lepszy model

- retry tylko dla sensownych błędów,
- kontrolowana liczba prób,
- idempotentny consumer albo deduplikacja,
- możliwość odłożenia zadania do osobnej ścieżki błędów.

## Mini case study: wysyłka maila

Masz task wysyłki maila potwierdzającego zamówienie.

### Problem

Provider mailowy chwilowo nie odpowiada.

### Retry ma sens?

Tak, bo to typowy błąd przejściowy.

### Ryzyko

Jeśli task nie pilnuje, czy mail już został faktycznie wysłany, możesz wysłać dwa potwierdzenia.

### Wniosek

Retry jest dobre, ale wysyłka powinna być zaprojektowana tak, żeby dubel nie robił szkody albo był wykrywany.

## Mini case study: naliczanie punktów

Masz task:

- po zakupie dodaj 100 punktów lojalnościowych.

Jeśli worker wykona task dwa razy, klient dostanie 200 punktów.

To dużo groźniejsze niż podwójny mail.

Tu idempotencja jest krytyczna.

## Co Pythonowiec powinien rozumieć

Dobrze, żebyś umiał:

- odróżnić błąd przejściowy od trwałego,
- rozpoznać, czy dana operacja jest idempotentna,
- wiedzieć, gdzie duplikat robi realną szkodę biznesową,
- zaprojektować prosty mechanizm deduplikacji,
- nie ufać założeniu "wykona się tylko raz".

## Output myślowy

### Retry bez idempotencji

- system jest bardziej odporny technicznie,
- ale biznesowo może produkować szkody.

### Retry z idempotencją

- system lepiej znosi chwilowe błędy,
- a duble nie psują logiki tak łatwo.

## Najważniejsze do zapamiętania

- Retry ma sens głównie przy błędach przejściowych.
- Retry bez idempotencji może być niebezpieczne.
- Operacja idempotentna nie robi dodatkowej szkody przy powtórzeniu.
- W systemach messagingowych trzeba zakładać możliwość dubli.
- Klucz idempotencji to bardzo ważna technika projektowa.

## Ćwiczenia

1. Wyjaśnij własnymi słowami różnicę między retry i idempotencją.
2. Podaj przykład operacji, dla której retry ma sens, i takiej, dla której samo retry nie pomoże.
3. Wskaż trzy operacje biznesowe, które są groźne bez idempotencji.
4. Opisz prosty mechanizm deduplikacji wiadomości.
5. Rozpisz flow przetwarzania płatności z idempotency key.
