# Case study: jak dobrać poziomy testów do jednego modułu w Pythonie

## Po co ten plik

Ten plik spina cały folder 22 w jedną praktyczną całość.

Nie chodzi tu o nowe definicje, tylko o odpowiedź na pytanie:

- jak dobrać poziomy testów do jednego realnego modułu?

To bardzo ważne, bo samo znanie nazw typu:

- unit,
- integracja,
- E2E,
- contract,

jeszcze nie oznacza, że umiesz dobrze rozłożyć odpowiedzialność testów.

## Mini system

Załóżmy prosty moduł zamówień.

Mamy przepływ:

1. klient wysyła request `POST /orders`,
2. payload jest walidowany,
3. `OrderService` liczy cenę,
4. zamówienie jest zapisywane w repo,
5. wysyłane jest powiadomienie,
6. API zwraca odpowiedź z `order_id` i statusem.

To bardzo dobry przykład, bo łączy kilka warstw.

## Pytanie kluczowe

Czy wszystko testować E2E?

Nie.

To byłoby:

- za ciężkie,
- za wolne,
- zbyt trudne w utrzymaniu,
- mało precyzyjne diagnostycznie.

Trzeba rozdzielić odpowiedzialność testów.

## Co testować unitowo

Unit testy są najlepsze tam, gdzie chcesz sprawdzić jedną regułę biznesową albo jedną małą decyzję w kodzie.

Unitowo testujemy:

- liczenie ceny,
- naliczanie rabatów,
- walidację pojedynczych reguł,
- edge case'y logiki domenowej,
- małe transformacje danych,
- lokalną obsługę błędów.

### Przykład

Mamy funkcję:

```python
def calculate_total(items, discount):
    if discount < 0:
        raise ValueError("discount must be >= 0")

    total = sum(item["price"] * item["qty"] for item in items)
    return total - discount
```

Tu unit testami sprawdzasz:

- pusty koszyk,
- zniżkę `0`,
- poprawne liczenie sumy,
- wyjątek dla błędnej zniżki,
- duże liczby,
- nietypowe kombinacje wejścia.

```python
def test_calculate_total_with_discount():
    items = [{"price": 10, "qty": 2}, {"price": 5, "qty": 1}]
    assert calculate_total(items, 5) == 20


def test_calculate_total_raises_for_negative_discount():
    items = [{"price": 10, "qty": 1}]

    with pytest.raises(ValueError):
        calculate_total(items, -1)
```

To jest dobry unit test, bo:

- działa szybko,
- nie potrzebuje bazy,
- nie potrzebuje HTTP,
- jasno pokazuje jedną regułę.

## Co testować integracyjnie

Integracja ma sens tam, gdzie kilka warstw musi naprawdę współpracować.

Integracyjnie testujemy:

- `OrderService` + `OrderRepository`,
- endpoint + walidacja + serwis,
- zapis i odczyt z bazy,
- mapowanie danych między warstwami,
- transakcje,
- współpracę z testową wersją zależności.

### Przykład 1

`OrderService` + `OrderRepository`

Sprawdzasz, czy:

- serwis buduje poprawny obiekt,
- repozytorium poprawnie go zapisuje,
- wynik można później odczytać.

```python
def test_order_service_saves_order_in_repository(db_session):
    service = OrderService(db_session)

    created = service.create_order(
        user_id=1,
        items=[{"sku": "A1", "qty": 2, "price": 10}],
    )

    saved = db_session.get(Order, created.id)
    assert saved is not None
    assert saved.user_id == 1
```

### Przykład 2

endpoint + walidacja + serwis

Sprawdzasz, czy:

- payload przechodzi przez warstwę wejścia,
- błędne dane są odrzucane,
- poprawne dane kończą się utworzeniem zamówienia.

To nadal nie musi być pełne E2E. To może być rozsądny test integracyjny aplikacji.

## Gdzie pasuje contract test

Jeśli moduł zamówień gada z zewnętrznym systemem płatności albo innym serwisem, contract test chroni granicę danych między systemami.

Contract test ma sens dla:

- formatu żądania płatności,
- formatu odpowiedzi statusu,
- obecności i znaczenia pól `payment_status`, `transaction_id`, `amount`,
- payloadów eventów,
- odpowiedzi partnera zewnętrznego.

### Przykład

Nasz kod zakłada, że provider zwraca:

```json
{
  "payment_id": "pay_123",
  "status": "confirmed",
  "amount": 199.99
}
```

A provider po zmianie zwraca:

```json
{
  "id": "pay_123",
  "state": "confirmed",
  "amount": 199.99
}
```

Wtedy:

- unit testy mogą dalej przechodzić,
- część lokalnych integracyjnych też może przejść,
- ale contract test powinien wykryć, że umowa danych już się nie zgadza.

To nie jest zwykła integracja lokalna. To granica między systemami.

## Kiedy E2E ma sens

E2E powinno chronić kilka kluczowych scenariuszy biznesowych od wejścia do końca przepływu.

Dobry kandydat na E2E:

1. użytkownik tworzy poprawne zamówienie,
2. system waliduje dane,
3. zamówienie zapisuje się poprawnie,
4. odpowiedź HTTP ma właściwy status i payload,
5. najważniejszy flow biznesowy naprawdę działa jako całość.

### Dobre pytanie E2E

- czy użytkownik naprawdę może utworzyć zamówienie od requestu do finalnej odpowiedzi?
- czy błędny payload rzeczywiście kończy się poprawnym błędem HTTP?
- czy krytyczny flow zakupu działa po spięciu wszystkich warstw?

## Kiedy E2E jest przesadą

E2E jest przesadą, gdy testujesz nim coś, co dużo taniej i stabilniej sprawdzisz niżej.

Zły kandydat na E2E:

- czy funkcja dobrze liczy rabat,
- czy walidator odrzuca pusty email,
- czy helper zamienia status na małe litery,
- czy mapper poprawnie przepisuje jedno pole,
- czy lokalna funkcja rzuca `ValueError`.

Dlaczego to przesada:

- test będzie wolny,
- będzie bardziej flaky,
- trudniej będzie znaleźć przyczynę błędu,
- koszt utrzymania będzie większy,
- mała zmiana UI albo API może rozwalić test mimo poprawnej logiki.

## Gdzie ma sens fake

Załóżmy, że chcesz testować `OrderService` bez prawdziwej bazy.

Bardzo sensowne może być:

- fake repozytorium w pamięci,
- zamiast ciężkiej realnej bazy albo zbyt kruchego mocka.

To daje dobrą równowagę między realizmem i prostotą.

## Gdzie ma sens mock

Dla powiadomień.

Jeśli po utworzeniu zamówienia serwis wywołuje `notifier.send(order_id)`, mock może być sensowny, bo tu ważna jest sama interakcja.

To dobry przykład:

- repo może mieć fake,
- notifier może mieć mock.

## Jak wygląda zły podział testów

### Zły wariant 1

Wszystko tylko unit testami.

Problem:

- nie wiesz, czy warstwy razem naprawdę działają.

### Zły wariant 2

Wszystko tylko E2E.

Problem:

- wolno,
- drogo,
- trudno diagnozować przyczynę awarii.

### Zły wariant 3

Wszystko mockowane.

Problem:

- testy przechodzą, ale realna integracja się sypie.

## Większy przekrojowy case study: jak dobrać poziomy testów do modułu `orders`

Załóżmy taki moduł:

- `validators.py` sprawdza payload,
- `pricing.py` liczy total,
- `service.py` tworzy zamówienie,
- `repository.py` zapisuje do bazy,
- `payment_client.py` komunikuje się z zewnętrznym API,
- `api.py` wystawia endpoint HTTP.

### Co testować unitowo

Unitowo testuj to, co jest czystą logiką lokalną.

Dla modułu `orders` będą to na przykład:

- `validate_items()` odrzuca pustą listę,
- `validate_email()` odrzuca błędny format,
- `calculate_total()` dobrze liczy kwoty,
- `calculate_discount()` dobrze obsługuje progi,
- `normalize_status()` poprawnie mapuje statusy.

To są testy typu:

- szybkie,
- tanie,
- bardzo precyzyjne,
- łatwe do diagnozy.

### Co testować integracyjnie

Integracyjnie testuj miejsca, gdzie naprawdę spotykają się warstwy.

Dla `orders`:

- `OrderService` zapisuje rekord przez `OrderRepository`,
- endpoint wywołuje serwis i zwraca dobry status,
- encje dobrze mapują się do tabel,
- odczyt po zapisie działa poprawnie,
- transakcja zapisuje komplet danych.

To odpowiada na pytanie:

- czy te kawałki systemu działają razem?

### Gdzie pasuje contract test

Contract test pasuje tam, gdzie system spotyka zewnętrzną umowę danych.

W module `orders`:

- klient płatności oczekuje konkretnego JSON-a,
- webhook płatności ma określone pola,
- event `order_created` ma określony format,
- inny serwis czy frontend zakłada określony shape odpowiedzi.

To odpowiada na pytanie:

- czy nadal zgadzamy się z drugim systemem, jak wyglądają dane?

### Kiedy E2E ma sens

E2E ma sens dla kilku najważniejszych flow biznesowych.

Dla `orders`:

- użytkownik tworzy poprawne zamówienie,
- użytkownik dostaje błąd dla złego payloadu,
- krytyczny flow płatności kończy się poprawnym statusem,
- podstawowa ścieżka zakupu działa od początku do końca.

To odpowiada na pytanie:

- czy cały scenariusz naprawdę działa oczami użytkownika?

### Kiedy E2E jest przesadą

Nie wrzucaj do E2E rzeczy takich jak:

- każdy wariant rabatu,
- każdy edge case walidacji,
- każdy wariant mappera,
- każda mała gałąź warunku,
- każda pomocnicza funkcja.

To lepiej pokryć unitami albo integracją.

## Lepszy podział

Dla naszego mini systemu:

- unit testy dla logiki ceny i walidacji,
- integracyjne dla serwisu i repo,
- contract testy dla zewnętrznej płatności,
- 2-3 E2E dla krytycznych przepływów,
- fake dla repo,
- mock dla wysyłki powiadomień.

To jest rozsądna, warstwowa strategia.

## Mini przykład pełniejszego zestawu

### Unit

- `test_calculate_total_with_discount`
- `test_calculate_total_empty_cart`
- `test_validate_payload_missing_price`
- `test_validate_email_rejects_invalid_value`

### Integration

- `test_order_service_saves_order_in_repository`
- `test_create_order_endpoint_persists_valid_order`
- `test_order_repository_reads_saved_order`

### Contract

- `test_payment_client_accepts_expected_response_shape`
- `test_order_created_event_contains_required_fields`

### E2E

- `test_user_can_create_order_successfully`
- `test_invalid_order_is_rejected`
- `test_paid_order_flow_finishes_successfully`

To daje bardzo czytelną mapę zaufania.

## Szybka mapa decyzji

Jeśli pytasz:

- czy ta jedna reguła biznesowa jest poprawna -> unit,
- czy te dwie-trzy warstwy działają razem -> integration,
- czy nadal zgadzamy się co do formatu danych z innym systemem -> contract,
- czy użytkownik może przejść cały najważniejszy flow -> E2E.

## Co ten case study pokazuje

Najważniejsza lekcja:

- różne problemy wymagają różnych poziomów testów,
- nie wszystko testuje się tak samo,
- dobra strategia to rozdzielenie odpowiedzialności.

## Jak z tego korzystać w praktyce

Gdy masz moduł, zadaj sobie pytania:

1. co tu jest czystą logiką,
2. gdzie zaczyna się współpraca między warstwami,
3. gdzie jest granica zewnętrznego kontraktu,
4. które przepływy są krytyczne dla użytkownika,
5. które zależności lepiej zastąpić fake, a które mockiem.

To bardzo dobry framework myślenia.

## Szybka ściąga

- unit testy chronią logikę lokalną,
- integracja chroni współpracę warstw,
- contract tests chronią granice między systemami,
- E2E chronią kilka krytycznych przepływów,
- fake i mock mają różne role i nie są wymienne jeden do jednego.

## Ćwiczenia

1. Weź własny moduł i rozpisz go na poziomy testów według tego schematu.
2. Wskaż, które zależności zrobiłbyś fake, a które mockiem.
3. Wybierz 2 przepływy E2E i uzasadnij, czemu są krytyczne.
4. Zaprojektuj prosty contract test dla jednej z granic modułu.
5. Opisz, który z poziomów testów byłby najdroższy i dlaczego.

## Najważniejsze do zapamiętania

- Dobór poziomów testów to decyzja projektowa, nie przypadek.
- Nie wszystko powinno być testowane tym samym typem testu.
- Najlepsza strategia rozdziela odpowiedzialność między poziomy testów.
- E2E powinno chronić kilka kluczowych scenariuszy, a nie całą drobnicę.
- Fake, mock, integracja i kontrakty mają sens tylko wtedy, gdy wspólnie budują zaufanie do systemu.
