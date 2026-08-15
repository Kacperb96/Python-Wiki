# Testowanie API w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co testować API](#po-co-testować-api)
3. [Co testować w API](#co-testować-w-api)
4. [Status code i body odpowiedzi](#status-code-i-body-odpowiedzi)
5. [Scenariusze pozytywne i negatywne](#scenariusze-pozytywne-i-negatywne)
6. [Walidacja danych wejściowych](#walidacja-danych-wejściowych)
7. [Autoryzacja i uprawnienia](#autoryzacja-i-uprawnienia)
8. [Warstwa HTTP vs logika biznesowa](#warstwa-http-vs-logika-biznesowa)
9. [Przykład testu endpointu](#przykład-testu-endpointu)
10. [Typowe błędy początkujących](#typowe-błędy-początkujących)
11. [Praktyczna ściąga](#praktyczna-ściąga)
12. [Ćwiczenia](#ćwiczenia)
13. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

Testy API są bardzo ważne, bo sprawdzają kontrakt między klientem a serwerem.

To nie tylko testowanie funkcji, ale też zachowania warstwy HTTP.

---

## Po co testować API

Bo API musi zachowywać się przewidywalnie dla:

- frontendu,
- innych usług,
- partnerów integracyjnych,
- testów automatycznych.

Dobre testy API chronią przed regresją nie tylko logiki, ale też samego kontraktu HTTP.

---

## Co testować w API

Najczęściej:

- status code,
- strukturę body,
- walidację wejścia,
- błędy,
- autoryzację,
- podstawowe scenariusze biznesowe.

---

## Status code i body odpowiedzi

To absolutne minimum.

Test powinien sprawdzać nie tylko, że endpoint "odpowiedział", ale że zrobił to poprawnie:

- `200`, `201`, `404`, `422` itd.,
- poprawny JSON,
- potrzebne pola,
- sensowny komunikat błędu.

---

## Scenariusze pozytywne i negatywne

### Pozytywne

- poprawne dane,
- poprawna autoryzacja,
- oczekiwany wynik.

### Negatywne

- brak danych,
- błędny format,
- brak uprawnień,
- brak zasobu,
- konflikt stanu.

To bardzo ważne, bo początkujący często testują tylko happy path.

---

## Walidacja danych wejściowych

API powinno odrzucać błędne dane na wejściu.

To bardzo ważny obszar testów.

Musisz sprawdzać nie tylko poprawne requesty, ale też:

- brak wymaganych pól,
- złe typy,
- niepoprawne formaty.

---

## Autoryzacja i uprawnienia

Nie wystarczy sprawdzić "czy działa".

Trzeba też sprawdzić:

- kto może wykonać daną operację,
- co dzieje się bez tokenu,
- co dzieje się z błędnym tokenem,
- co dzieje się bez właściwej roli.

---

## Warstwa HTTP vs logika biznesowa

Nie wszystko trzeba testować wyłącznie przez API.

Dobrze rozdzielać:

- testy endpointów,
- testy logiki biznesowej,
- testy integracyjne.

To pozwala budować testy szybsze, czytelniejsze i mniej kruche.

---

## Przykład testu endpointu

Mentalny przykład:

- `POST /users` powinien zwrócić `201`,
- odpowiedź powinna mieć `id`,
- przy błędnych danych powinien pojawić się np. `422`.

Przykład testu stylu FastAPI/TestClient:

```python
def test_create_user(client):
    response = client.post(
        "/users",
        json={"name": "Anna", "email": "anna@example.com"},
    )

    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Anna"
    assert "id" in data
```

To prosty, ale bardzo realistyczny kształt testu API.

---

## Typowe błędy początkujących

- testowanie tylko happy path,
- brak sprawdzania kodów błędów,
- ignorowanie walidacji wejścia,
- brak testów autoryzacji,
- mieszanie zbyt wielu odpowiedzialności w jednym teście,
- testowanie samego `200`, bez patrzenia na body.

---

## Praktyczna ściąga

### W testach API najczęściej sprawdzasz

- status code,
- body odpowiedzi,
- strukturę JSON,
- scenariusze negatywne,
- autoryzację.

### Dobre pytania do testu

- Czy endpoint zwraca właściwy status?
- Czy JSON ma właściwy kształt?
- Co dzieje się przy błędnych danych?
- Co dzieje się bez uprawnień?

---

## Ćwiczenia

1. Napisz test dla `GET /health`.
2. Napisz test dla poprawnego `POST /users`.
3. Napisz test dla błędnych danych wejściowych.
4. Napisz test dla braku autoryzacji.
5. Napisz test dla braku zasobu.
6. Wyjaśnij własnymi słowami, czym różni się test logiki biznesowej od testu samego endpointu.

---

## Najważniejsze do zapamiętania

- Testy API sprawdzają kontrakt HTTP, a nie tylko sam kod funkcji.
- Trzeba testować zarówno scenariusze poprawne, jak i błędne.
- Status code i body odpowiedzi są równie ważne.
- Walidacja wejścia i autoryzacja to obowiązkowe obszary testów API.
- Nie wszystko trzeba testować wyłącznie przez warstwę HTTP.
