# Case study: mini backend auth krok po kroku w Pythonie

## Po co ten plik

Ten plik spina cały folder 23 w jedną większą całość.

Chodzi o to, żeby nie patrzeć na sesje, JWT, refresh tokeny, role, rate limiting i CORS jako osobne hasła, tylko jako elementy jednego systemu.

## Mini system

Załóżmy prosty backend dla aplikacji `orders`.

Mamy endpointy:

- `POST /login`
- `POST /refresh`
- `POST /logout`
- `GET /me`
- `GET /orders`
- `DELETE /orders/{id}`

Założenia:

- frontend działa na `https://app.example.com`,
- backend działa na `https://api.example.com`,
- użytkownicy mają role `customer`, `support`, `admin`,
- backend używa krótkiego access tokena i refresh tokena.

## Cel architektoniczny

Chcemy osiągnąć jednocześnie:

- sensowne bezpieczeństwo,
- prosty model myślenia,
- wygodne utrzymanie sesji użytkownika,
- kontrolę nad wylogowaniem i odświeżaniem.

## Krok 1: logowanie

Użytkownik wysyła:

```http
POST /login
Content-Type: application/json

{
  "email": "jan@example.com",
  "password": "tajne_haslo"
}
```

Backend robi:

1. sprawdza dane logowania,
2. pobiera użytkownika i jego role,
3. tworzy access token ważny np. 15 minut,
4. tworzy refresh token ważny np. 14 dni,
5. zapisuje refresh token w bazie lub magazynie sesji,
6. zwraca access token i ustawia refresh token w bezpiecznym cookie.

## Przykładowa odpowiedź

```http
HTTP/1.1 200 OK
Set-Cookie: refresh_token=refresh_xyz; HttpOnly; Secure; SameSite=Lax
Content-Type: application/json

{
  "access_token": "access_abc",
  "token_type": "bearer",
  "expires_in": 900
}
```

## Dlaczego taki układ ma sens

- access token żyje krótko,
- refresh token nie musi być dostępny z JavaScriptu,
- backend może kontrolować sesję przez refresh token,
- użytkownik nie loguje się co chwilę.

## Krok 2: wejście na endpoint chroniony

Frontend wywołuje:

```http
GET /me
Authorization: Bearer access_abc
```

Backend robi:

1. sprawdza podpis i datę ważności access tokena,
2. odczytuje `sub`, role i scope albo permission set,
3. wpuszcza użytkownika do endpointu.

### Odpowiedź

```json
{
  "user_id": 42,
  "email": "jan@example.com",
  "role": "customer"
}
```

## Krok 3: access token wygasa

Po 15 minutach access token przestaje działać.

Przykładowa odpowiedź backendu:

```http
HTTP/1.1 401 Unauthorized
Content-Type: application/json

{
  "detail": "token expired"
}
```

To nie znaczy jeszcze, że użytkownik jest wylogowany całkowicie.

## Krok 4: odświeżenie sesji

Frontend lub klient wywołuje:

```http
POST /refresh
Cookie: refresh_token=refresh_xyz
```

Backend robi:

1. odczytuje refresh token,
2. sprawdza, czy istnieje,
3. sprawdza, czy nie wygasł,
4. sprawdza, czy nie został unieważniony,
5. generuje nowy access token,
6. opcjonalnie rotuje refresh token.

## Przykładowa odpowiedź

```json
{
  "access_token": "access_new_123",
  "expires_in": 900
}
```

## Krok 5: wylogowanie

Wylogowanie nie powinno oznaczać tylko "usuń token po stronie frontu".

Lepszy model:

1. frontend wywołuje `POST /logout`,
2. backend unieważnia refresh token,
3. backend czyści cookie,
4. access token i tak zaraz wygaśnie.

Przykładowa odpowiedź:

```http
HTTP/1.1 200 OK
Set-Cookie: refresh_token=; Max-Age=0; HttpOnly; Secure; SameSite=Lax
Content-Type: application/json

{
  "message": "logged out"
}
```

## Autoryzacja na endpointach

Samo zalogowanie nie wystarczy.

### `GET /orders`

Może mieć dostęp:

- `customer` do swoich zamówień,
- `support` do większej liczby zamówień,
- `admin` do wszystkiego.

### `DELETE /orders/{id}`

Może mieć dostęp:

- tylko `admin`,
- albo `support` w określonych warunkach biznesowych.

## Prosta mapa uprawnień

```python
ROLE_PERMISSIONS = {
    "customer": {"orders.read.own"},
    "support": {"orders.read", "orders.update"},
    "admin": {"orders.read", "orders.update", "orders.delete", "users.manage"},
}
```

Najważniejszy wniosek:

- autoryzacja to nie tylko "czy token jest poprawny",
- autoryzacja to też "czy ta osoba może zrobić właśnie to".

## Gdzie tu wchodzi rate limiting

Nie każdy endpoint potrzebuje tego samego limitu.

### Sensowne przykłady

- `POST /login` — mocny limit przeciw brute force,
- `POST /refresh` — limit przeciw nadużyciom lub błędnemu klientowi,
- `POST /reset-password` — limit przeciw spamowi,
- `GET /orders` — lżejszy limit, zależnie od systemu.

## Gdzie tu wchodzi CORS

Ponieważ frontend i backend są na różnych originach:

- `https://app.example.com`
- `https://api.example.com`

CORS ma znaczenie.

Backend musi świadomie dopuścić frontendowy origin.

Przykładowa konfiguracja myślowa:

- allow origin: `https://app.example.com`,
- allow methods: `GET, POST, DELETE, OPTIONS`,
- allow headers: `Authorization, Content-Type`,
- allow credentials: jeśli używasz cookie.

## Gdzie tu wchodzi middleware

W takim systemie sensowne middleware na start to np.:

- logging middleware,
- request id middleware,
- timing middleware,
- CORS middleware,
- middleware łapiący wyjątki i zwracający spójny JSON błędu.

## Typowe błędy projektowe w takim systemie

### Błąd 1

Trzymanie wszystkiego w jednym bardzo długim access tokenie.

Skutek:

- większe ryzyko po kradzieży tokena,
- trudniejsze wylogowanie.

### Błąd 2

Brak rozróżnienia między uwierzytelnianiem i autoryzacją.

Skutek:

- użytkownik ma poprawny token, ale backend nie kontroluje dobrze operacji.

### Błąd 3

Zbyt szerokie role typu:

- `admin`,
- `user`.

Skutek:

- szybko brakuje precyzji.

### Błąd 4

Brak rate limitingu na logowanie.

Skutek:

- system jest bardziej podatny na brute force.

### Błąd 5

Myślenie, że CORS zabezpiecza cały backend.

Skutek:

- fałszywe poczucie bezpieczeństwa.

## Jak dobrać poziomy testów do tego modułu

### Unit

Unitowo testuj:

- walidację danych logowania,
- generowanie payloadu tokena,
- sprawdzanie `exp`,
- funkcję `has_permission`,
- mapowanie ról do uprawnień.

### Integration

Integracyjnie testuj:

- `POST /login` + magazyn użytkowników,
- `POST /refresh` + magazyn refresh tokenów,
- `GET /me` + weryfikację access tokena,
- autoryzację endpointu na realnej warstwie aplikacji.

### E2E

E2E testuj tylko krytyczne flow:

- użytkownik loguje się i wchodzi na profil,
- access token wygasa i sesja jest odświeżana,
- użytkownik bez uprawnień dostaje `403`.

## Minimalny pseudokod spajający całość

```python
def login(email: str, password: str) -> dict:
    user = authenticate(email, password)
    access_token = issue_access_token(user)
    refresh_token = issue_refresh_token(user)
    save_refresh_token(user.id, refresh_token)
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
    }


def refresh(refresh_token: str) -> dict:
    session = get_refresh_session(refresh_token)
    if session is None:
        raise ValueError("invalid refresh token")
    return {"access_token": issue_access_token(session.user)}


def can_delete_order(user, order_id: int) -> bool:
    return has_permission(user.role, "orders.delete")
```

## Najważniejsze do zapamiętania

- Dobrze zaprojektowany auth flow składa się z kilku warstw, nie z jednego tokena.
- Uwierzytelnianie, odświeżanie sesji i autoryzacja to różne problemy.
- Krótki access token i kontrolowany refresh token to częsty sensowny model.
- Role i uprawnienia trzeba projektować świadomie, a nie dopisywać przypadkowo.
- Rate limiting, CORS i middleware są częścią produkcyjnej dojrzałości systemu.

## Ćwiczenia

1. Rozpisz własną wersję tego mini backendu z sesjami zamiast JWT.
2. Zaproponuj czasy życia access tokena i refresh tokena dla aplikacji webowej.
3. Zdecyduj, które endpointy wymagałyby `customer`, `support` i `admin`.
4. Opisz, które trzy middleware dodałbyś jako pierwsze i dlaczego.
5. Wskaż dwa miejsca, gdzie najłatwiej popełnić błąd bezpieczeństwa w tym flow.
