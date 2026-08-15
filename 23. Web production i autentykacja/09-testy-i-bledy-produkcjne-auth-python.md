# Testy i błędy produkcyjne w auth flow python

## Po co ten plik

Teoria o tokenach i autoryzacji jest potrzebna, ale dopiero testy i realne awarie pokazują, czy system jest naprawdę sensowny.

Ten plik pokazuje:

- co testować w module auth,
- jakie błędy pojawiają się w produkcji,
- jak czytać objawy i szukać przyczyny.

## Co warto testować unitowo

Unit testy powinny łapać małe, ważne reguły.

Przykłady:

- czy funkcja odrzuca wygasły token,
- czy `has_permission()` działa poprawnie,
- czy parser cookie wyciąga właściwą wartość,
- czy payload tokena ma wymagane pola,
- czy walidacja loginu odrzuca puste dane.

### Przykład

```python
def is_token_expired(now: int, exp: int) -> bool:
    return now >= exp


def test_token_not_expired():
    assert is_token_expired(now=100, exp=120) is False


def test_token_expired():
    assert is_token_expired(now=120, exp=120) is True
```

## Co warto testować integracyjnie

Integracja jest ważna tam, gdzie spotykają się warstwy.

Przykłady:

- login + magazyn użytkowników,
- refresh + magazyn sesji lub tokenów,
- endpoint chroniony + weryfikacja access tokena,
- autoryzacja endpointu z prawdziwym kontekstem użytkownika.

### Przykład scenariusza integracyjnego

1. zapisujesz użytkownika testowego,
2. wywołujesz `POST /login`,
3. dostajesz access token,
4. wywołujesz `GET /me`,
5. oczekujesz `200` i danych użytkownika.

## Co warto testować E2E

E2E zostaw dla kilku krytycznych flow.

Najlepsze przykłady:

- użytkownik loguje się i widzi chroniony widok,
- użytkownik z niewłaściwą rolą dostaje `403`,
- access token wygasa i klient poprawnie robi refresh,
- wylogowanie kończy sesję i kolejny refresh już nie działa.

## Mini system testowy

Załóżmy prosty kontrakt:

- `POST /login` zwraca access token,
- refresh token jest w `HttpOnly cookie`,
- `GET /me` wymaga `Authorization: Bearer ...`,
- `DELETE /orders/{id}` wymaga prawa `orders.delete`.

## Przykładowe testy dla jednego flow

### Test 1: poprawne logowanie

```python
def test_login_returns_access_token(client):
    response = client.post("/login", json={
        "email": "jan@example.com",
        "password": "tajne_haslo",
    })

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
```

### Test 2: wejście na profil po zalogowaniu

```python
def test_me_requires_valid_token(client, access_token):
    response = client.get(
        "/me",
        headers={"Authorization": f"Bearer {access_token}"},
    )

    assert response.status_code == 200
```

### Test 3: brak uprawnienia do usuwania zamówienia

```python
def test_customer_cannot_delete_order(client, customer_token):
    response = client.delete(
        "/orders/1",
        headers={"Authorization": f"Bearer {customer_token}"},
    )

    assert response.status_code == 403
```

### Test 4: admin może usunąć zamówienie

```python
def test_admin_can_delete_order(client, admin_token):
    response = client.delete(
        "/orders/1",
        headers={"Authorization": f"Bearer {admin_token}"},
    )

    assert response.status_code in {200, 204}
```

## Większy case study: wygasły access token

Załóżmy objaw:

- użytkownik twierdzi, że "aplikacja losowo mnie wylogowuje".

### Krok 1: objaw

Frontend przy wejściu na profil dostaje czasem `401 Unauthorized`.

### Krok 2: pierwsze hipotezy

- access token wygasa,
- refresh nie działa,
- klient nie wysyła cookie,
- CORS blokuje request z credentialami,
- backend źle liczy czas ważności.

### Krok 3: co sprawdzić

- logi endpointu `/refresh`,
- czy cookie rzeczywiście jest wysyłane,
- czy `exp` jest prawidłowe,
- czy klient nie używa starego tokena po odświeżeniu,
- czy zegary środowisk nie są rozjechane.

### Krok 4: możliwa prawdziwa przyczyna

Refresh token siedzi w cookie, ale frontend nie wysyła requestu z credentialami.

Skutek:

- `/refresh` nie dostaje cookie,
- backend zwraca `401`,
- użytkownik wygląda jak wylogowany.

### Lekcja

Auth flow to nie tylko token. To też:

- cookies,
- CORS,
- konfiguracja klienta,
- wygasanie,
- spójność czasu.

## Realistyczne błędy produkcyjne

### Błąd 1: `403` zamiast `401`

Objaw:

- część endpointów zwraca `403`, mimo że użytkownik w ogóle nie jest zalogowany.

Możliwa przyczyna:

- backend miesza brak uwierzytelnienia z brakiem uprawnień.

Lepsza interpretacja:

- `401` gdy nie ma poprawnego uwierzytelnienia,
- `403` gdy użytkownik jest rozpoznany, ale nie ma prawa wykonać akcji.

### Błąd 2: token działa lokalnie, nie działa na produkcji

Objaw:

- lokalnie wszystko działa,
- na produkcji użytkownicy nagle dostają błędy autoryzacji.

Możliwe przyczyny:

- inny `issuer`,
- zły `audience`,
- różnica czasu systemowego,
- inny sekret lub klucz podpisu.

### Błąd 3: logowanie działa, refresh nie działa

Objaw:

- użytkownik loguje się poprawnie,
- po kilkunastu minutach sesja umiera.

Możliwe przyczyny:

- refresh token nie jest zapisywany,
- cookie ma zły zakres lub flagi,
- endpoint `/refresh` nie czyta właściwego cookie,
- rotacja tokena usuwa sesję za wcześnie.

### Błąd 4: admin nagle traci część uprawnień

Objaw:

- panel admina działa częściowo,
- niektóre akcje kończą się `403`.

Możliwe przyczyny:

- zmiana mapowania ról do uprawnień,
- rozjazd między payloadem tokena a bazą,
- stary token z nieaktualną rolą,
- błąd w warstwie `has_permission`.

### Błąd 5: przeglądarka zgłasza problem, backend "działa"

Objaw:

- DevTools pokazuje błąd CORS,
- backend twierdzi, że endpoint zwraca `200`.

Możliwa przyczyna:

- odpowiedź backendu istnieje,
- ale przeglądarka blokuje frontendowi dostęp do niej przez złą konfigurację CORS.

## Contract drift w auth flow

To też się zdarza.

### Przykład

Frontend zakłada, że odpowiedź z `/login` ma:

```json
{
  "access_token": "...",
  "expires_in": 900
}
```

Backend po zmianie zwraca:

```json
{
  "token": "...",
  "ttl": 900
}
```

Jeśli zmiana nie została uzgodniona:

- frontend może przestać działać,
- testy kontraktowe powinny to wykryć.

## Flaky tests w auth

Ten obszar bardzo łatwo robi flaky testy.

### Przykład 1: zależność od czasu

Test raz działa, raz nie, bo access token wygasa dokładnie na granicy.

Lepiej:

- zamrażać czas,
- kontrolować `now`,
- nie opierać testu na prawdziwym upływie sekund.

### Przykład 2: współdzielony stan refresh tokenów

Jeden test unieważnia token, a drugi przypadkiem korzysta z tego samego stanu.

Lepiej:

- izolować fixtures,
- resetować magazyn tokenów,
- unikać współdzielonego globalnego stanu.

### Przykład 3: zależność od kolejności testów

Jeśli test admina tworzy użytkownika lub token, a test klienta zakłada jego brak, kolejność uruchomienia może zmieniać wynik.

## Co powinno być dobrze zalogowane w produkcji

W auth flow warto logować mądrze, ale bez wycieku sekretów.

Dobrze logować:

- nieudane logowania,
- odrzucone refresh tokeny,
- `401` i `403` z kontekstem technicznym,
- reuse starego refresh tokena,
- przekroczenia rate limitu.

Nie logować pełnych sekretów i tokenów wprost.

## Szybka checklista debugowania auth

Gdy coś nie działa, sprawdź po kolei:

1. czy użytkownik przesłał prawidłowe dane,
2. czy backend wystawił token,
3. czy klient go naprawdę wysyła,
4. czy token nie wygasł,
5. czy refresh działa,
6. czy role i uprawnienia są zgodne,
7. czy CORS albo cookies nie blokują przepływu,
8. czy limity requestów nie odcinają klienta.

## Najważniejsze do zapamiętania

- Auth trzeba testować warstwowo: unit, integracja, kilka E2E.
- Najczęstsze awarie auth nie wynikają tylko z jednego tokena, ale z całego przepływu.
- `401` i `403` to nie to samo.
- Czas, cookies, CORS i rotacja tokenów bardzo często wpływają na błędy.
- Dobre logi i sensowne testy oszczędzają mnóstwo czasu przy diagnozie.

## Ćwiczenia

1. Zapisz trzy różne sytuacje, które powinny kończyć się `401`, i trzy, które powinny kończyć się `403`.
2. Opisz test integracyjny dla endpointu `/refresh`.
3. Zaprojektuj contract test dla odpowiedzi z `/login`.
4. Opisz flaky test związany z wygasaniem tokena i pokaż, jak go naprawić.
5. Rozpisz własną checklistę debugowania problemu "użytkownicy losowo są wylogowywani".
