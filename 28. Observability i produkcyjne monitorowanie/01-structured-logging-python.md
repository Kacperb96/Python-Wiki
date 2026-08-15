# Structured logging python

## O czym jest ten rozdział

Bardzo wiele zespołów zaczyna od logowania w stylu:

```python
print("cos poszlo nie tak")
```

albo:

```python
logger.info("user logged in")
```

To lepsze niż nic, ale w produkcji szybko okazuje się niewystarczające.

Pojawiają się pytania:

- który użytkownik,
- który request,
- która wersja aplikacji,
- z którego workera,
- jaki był status odpowiedzi,
- co było inputem albo przynajmniej jaki był kontekst.

Właśnie dlatego structured logging jest tak ważny.

## Najprostsza intuicja

Structured logging oznacza, że log nie jest tylko luźnym tekstem, ale uporządkowanym zbiorem pól.

Najprościej:

- zamiast jednej nieczytelnej wiadomości,
- masz komunikat plus konkretne klucze i wartości.

To bardzo zwiększa wartość operacyjną logów.

## Log tekstowy vs log strukturalny

### Luźny log tekstowy

```text
user login failed for jan@example.com from 10.0.0.5
```

To da się przeczytać, ale trudniej to:

- filtrować,
- agregować,
- korelować z innymi zdarzeniami,
- przeszukiwać po konkretnych polach.

### Log strukturalny

```json
{
  "event": "user_login_failed",
  "email": "jan@example.com",
  "ip": "10.0.0.5",
  "service": "auth-api"
}
```

Taki log dużo łatwiej analizować automatycznie.

## Po co structured logging ma sens

Structured logging pomaga, gdy chcesz:

- filtrować logi po polach,
- łączyć logi między usługami,
- szukać tylko błędów jednego typu,
- analizować ruch użytkownika albo requestów,
- budować dashboardy i alerty na bazie zdarzeń.

To jest bardzo duża różnica praktyczna.

## Jakie pola często warto mieć

To zależy od systemu, ale bardzo często przydają się pola takie jak:

- `timestamp`,
- `level`,
- `service`,
- `environment`,
- `request_id`,
- `user_id` albo inny identyfikator podmiotu,
- `event`,
- `status_code`,
- `duration_ms`,
- `error_type`.

Najważniejsza intuicja:

- log powinien nie tylko mówić "coś się stało",
- ale też dawać kontekst potrzebny do diagnozy.

## Minimalny przykład w Pythonie

```python
import json

log = {
    "event": "order_created",
    "order_id": 123,
    "user_id": 42,
    "service": "orders-api",
}

print(json.dumps(log))
```

Output:

```text
{"event": "order_created", "order_id": 123, "user_id": 42, "service": "orders-api"}
```

To bardzo uproszczony przykład, ale dobrze buduje intuicję, że log może być obiektem danych, a nie tylko zdaniem.

## Dlaczego `request_id` jest tak ważne

W systemie webowym lub rozproszonym wiele logów dotyczy jednego przepływu requestu.

Jeśli masz `request_id`, dużo łatwiej:

- zebrać wszystkie logi jednego requestu,
- zobaczyć, gdzie poleciał dalej,
- znaleźć miejsce błędu.

Bez tego często masz tylko ocean luźnych komunikatów.

## Before/after

### Słabsze logowanie

```python
logger.error("database problem")
```

To daje mało kontekstu.

### Lepsze logowanie

```python
logger.error(
    "database problem",
    extra={
        "event": "db_query_failed",
        "request_id": "req-123",
        "query_name": "get_user_orders",
    },
)
```

Tu dużo łatwiej diagnozować, czego dotyczył problem.

## Structured logging a bezpieczeństwo

To bardzo ważny temat.

Nie wszystko wolno logować.

Zły pomysł:

- hasła,
- pełne tokeny,
- sekrety,
- bardzo wrażliwe dane osobowe bez potrzeby.

Czyli structured logging nie oznacza "loguj wszystko".

Oznacza raczej:

- loguj mądrze, w polach, z kontekstem.

## Częste pułapki

### 1. Logi pełne tekstu bez pól

Trudniej je potem przeszukiwać i analizować.

### 2. Za dużo pól bez sensu

Structured logging też może zamienić się w śmietnik, jeśli wrzucasz wszystko bez refleksji.

### 3. Brak spójności między usługami

Jeśli jedna usługa używa `request_id`, druga `correlationId`, a trzecia nic, korelacja staje się trudniejsza.

### 4. Logowanie danych wrażliwych

To duże ryzyko bezpieczeństwa i prywatności.

### 5. Brak wspólnego słownika eventów

Jeśli ten sam typ zdarzenia nazywany jest w pięciu miejscach inaczej, logi tracą wartość operacyjną.

## Mini case study: błąd zamówienia

Użytkownik zgłasza, że nie udało mu się złożyć zamówienia.

### Słabe logi

```text
order error
```

To praktycznie nic nie daje.

### Lepsze logi

```json
{
  "event": "order_creation_failed",
  "request_id": "req-123",
  "user_id": 42,
  "error_type": "inventory_conflict",
  "service": "orders-api"
}
```

Teraz od razu wiesz dużo więcej:

- jaki to typ błędu,
- kogo dotyczył,
- jakiego requestu szukać dalej.

## Structured logging a observability

Structured logging to tylko jeden filar observability, ale bardzo ważny.

Logi odpowiadają zwykle na pytanie:

- co się wydarzyło i z jakim kontekstem?

Metryki i tracing odpowiadają na inne pytania.

Dlatego nie warto próbować wszystkiego załatwić samym logowaniem.

## Co Pythonowiec powinien rozumieć

Dobrze, żebyś umiał:

- odróżnić luźny tekst od logu strukturalnego,
- dobrać sensowne pola kontekstowe,
- rozumieć, po co `request_id` i spójne nazwy eventów,
- nie logować danych, których nie powinno tam być,
- traktować logi jako narzędzie analizy, a nie pamiętnik kodu.

## Output myślowy

### Słabe logowanie

- dużo tekstu,
- mało kontekstu,
- trudna analiza.

### Dobre logowanie strukturalne

- łatwiejsze filtrowanie,
- łatwiejsza korelacja,
- szybsza diagnoza,
- większa wartość operacyjna.

## Najważniejsze do zapamiętania

- Structured logging oznacza logowanie w postaci danych z polami, nie tylko luźnych tekstów.
- Dobrze dobrany kontekst bardzo zwiększa wartość logu.
- `request_id`, `event`, `service` i podobne pola są bardzo praktyczne.
- Nie wszystko należy logować, szczególnie dane wrażliwe.
- Structured logging to ważny fundament observability, ale nie jedyny.

## Ćwiczenia

1. Wyjaśnij własnymi słowami różnicę między logiem tekstowym i strukturalnym.
2. Wypisz pięć pól, które dodałbyś do logów backendu API.
3. Opisz, czemu `request_id` jest tak ważny.
4. Podaj trzy przykłady danych, których nie powinno się logować.
5. Rozpisz lepszą, strukturalną wersję logu dla błędu tworzenia zamówienia.
