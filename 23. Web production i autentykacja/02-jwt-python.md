# JWT python

## O czym jest ten rozdział

JWT, czyli `JSON Web Token`, to bardzo popularny format tokena używany w systemach webowych i API.

To jeden z tematów, o których mówi się dużo, ale często zbyt powierzchownie. W praktyce ważne jest nie tylko to, czym JWT jest, ale też:

- kiedy ma sens,
- kiedy jest nadużywany,
- jakie ma ograniczenia,
- jak łatwo zrobić go źle.

## Najprostsza intuicja

JWT to podpisany token, który przenosi pewne dane w postaci JSON-a.

Bardzo często backend wystawia token po zalogowaniu, a klient dołącza go do kolejnych requestów.

Typowy nagłówek:

```http
Authorization: Bearer <token>
```

Serwer po otrzymaniu tokena sprawdza:

- czy podpis jest poprawny,
- czy token nie wygasł,
- czy zawiera oczekiwane dane,
- czy użytkownik może wykonać daną akcję.

## Z czego składa się JWT

JWT ma zwykle trzy części oddzielone kropkami:

```text
header.payload.signature
```

Przykład wyglądu:

```text
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo0Miwicm9sZSI6ImFkbWluIn0.signature123
```

To nie jest szyfrowanie. To bardzo ważne.

Typowe części:

- `header` mówi np. jaki algorytm użyto,
- `payload` trzyma dane zwane claims,
- `signature` pozwala wykryć manipulację tokenem.

## JWT nie oznacza szyfrowania

To jeden z najważniejszych punktów.

Wiele osób myśli:

- "mam JWT, więc dane są ukryte".

To błędne.

W standardowym JWT payload jest zakodowany, ale niezaszyfrowany. To znaczy, że często można go odczytać.

Dlatego do tokena nie wkłada się sekretów typu:

- hasło,
- pełne dane osobowe,
- dane kart,
- inne wrażliwe informacje.

## Prosta symulacja w Pythonie

To tylko intuicja. Nie implementujemy tu prawdziwego podpisu kryptograficznego.

```python
import base64
import json

header = {"alg": "HS256", "typ": "JWT"}
payload = {"user_id": 42, "role": "admin"}

header_part = base64.urlsafe_b64encode(json.dumps(header).encode()).decode()
payload_part = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode()
signature_part = "fake-signature"

token = f"{header_part}.{payload_part}.{signature_part}"
print(token)
print(json.loads(base64.urlsafe_b64decode(payload_part.encode())))
```

Przykładowy output:

```text
eyJhbGciOiAiSFMyNTYiLCAidHlwIjogIkpXVCJ9.eyJ1c2VyX2lkIjogNDIsICJyb2xlIjogImFkbWluIn0=.fake-signature
{'user_id': 42, 'role': 'admin'}
```

Najważniejszy wniosek:

- payload da się odczytać,
- podpis chroni integralność, a nie poufność.

## Typowy flow z JWT

1. użytkownik wysyła login i hasło,
2. backend sprawdza dane,
3. backend wystawia access token,
4. klient zapisuje token,
5. klient wysyła token przy kolejnych requestach,
6. backend weryfikuje token i odczytuje claims.

### Request logowania

```http
POST /login
Content-Type: application/json

{
  "email": "jan@example.com",
  "password": "tajne_haslo"
}
```

### Odpowiedź

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "access_token": "<jwt>",
  "token_type": "bearer"
}
```

### Kolejny request

```http
GET /me
Authorization: Bearer <jwt>
```

## Claims: co zwykle siedzi w payloadzie

Typowe dane w tokenie:

- `sub` — identyfikator użytkownika,
- `exp` — data wygaśnięcia,
- `iat` — data wystawienia,
- `iss` — wystawca,
- `aud` — odbiorca,
- własne pola typu `role`, `scope`, `tenant_id`.

Przykład payloadu:

```json
{
  "sub": "42",
  "role": "admin",
  "exp": 1790000000,
  "scope": "orders:read orders:write"
}
```

## Before/after: dobry i zły payload

### Zły payload

```json
{
  "user_id": 42,
  "email": "jan@example.com",
  "password": "tajne_haslo",
  "full_profile": {
    "address": "..."
  }
}
```

Źle, bo token zawiera za dużo i nawet dane wrażliwe.

### Lepszy payload

```json
{
  "sub": "42",
  "role": "admin",
  "exp": 1790000000
}
```

Lepiej, bo token przenosi tylko minimum potrzebne do autoryzacji.

## Zalety JWT

- dobrze pasuje do API,
- backend może działać bardziej bezstanowo,
- łatwo przekazywać token między usługami,
- wygodnie używać w architekturach rozproszonych,
- dobrze nadaje się do krótkotrwałych access tokenów.

## Wady JWT

- trudniej unieważniać natychmiast pojedyncze tokeny,
- łatwo przesadzić z ilością danych w payloadzie,
- ludzie często błędnie traktują JWT jako rozwiązanie "na wszystko",
- błędy konfiguracyjne potrafią mieć poważne skutki,
- skradziony ważny token działa jak przepustka do czasu wygaśnięcia.

## Najczęstsze pułapki

### 1. Za długi czas życia access tokena

Jeśli access token żyje zbyt długo, skutki jego kradzieży są większe.

Często lepiej:

- krótszy access token,
- osobny refresh token.

### 2. Trzymanie sekretów w payloadzie

Nie wkładaj tam haseł i bardzo wrażliwych danych.

### 3. Brak walidacji `exp`, `iss`, `aud`

Sama weryfikacja podpisu nie zawsze wystarcza.

W praktyce często sprawdza się też:

- czy token nie wygasł,
- czy pochodzi od właściwego wystawcy,
- czy jest przeznaczony dla właściwego odbiorcy.

### 4. Trzymanie tokena w niebezpiecznym miejscu

To temat architektoniczny, ale bardzo ważny.

Zależy od typu aplikacji, ale trzeba myśleć o ryzykach XSS, CSRF i kradzieży tokenów.

### 5. Pakowanie całej autoryzacji w jedną rolę

Samo `role=admin` bywa zbyt toporne. Czasem lepsze są granularne uprawnienia lub scope'y.

## JWT a sesje

To nie jest pytanie: "co nowocześniejsze?"

To jest pytanie: "co lepiej pasuje do systemu?"

Sesje:

- prostsze do unieważniania,
- stan po stronie serwera,
- często bardzo dobre do klasycznych aplikacji webowych.

JWT:

- wygodne w API i systemach rozproszonych,
- bardziej bezstanowe,
- dobre dla krótkotrwałych tokenów i integracji.

## Przykład walidacji intuicyjnej

```python
import time


def is_token_active(payload: dict) -> bool:
    exp = payload.get("exp")
    if exp is None:
        return False
    return time.time() < exp


print(is_token_active({"exp": time.time() + 60}))
print(is_token_active({"exp": time.time() - 60}))
print(is_token_active({}))
```

Output:

```text
True
False
False
```

To oczywiście tylko fragment prawdziwej walidacji, ale buduje intuicję.

## Kiedy JWT ma sens

JWT często ma sens, gdy:

- budujesz API dla różnych klientów,
- masz architekturę usługową,
- potrzebujesz bezstanowego access tokena,
- chcesz prosto przenosić tożsamość między komponentami,
- planujesz access tokeny krótkiego życia i sensowną rotację.

## Kiedy JWT bywa złym wyborem

JWT bywa przerostem formy, gdy:

- masz prostą aplikację serwer-renderowaną,
- chcesz łatwe unieważnianie sesji użytkownika,
- nie potrzebujesz rozproszonej architektury,
- problem da się prościej rozwiązać klasyczną sesją.

## Najważniejsze do zapamiętania

- JWT to podpisany token, a nie automatycznie szyfrowany sejf.
- Payload zwykle da się odczytać.
- Token powinien zawierać minimum potrzebnych danych.
- Krótkie życie access tokena jest zwykle lepsze niż bardzo długie.
- JWT nie jest z definicji lepszy od sesji.

## Ćwiczenia

1. Wyjaśnij własnymi słowami różnicę między podpisaniem a szyfrowaniem JWT.
2. Podaj trzy dobre pola, które mogą być w payloadzie, i trzy złe.
3. Opisz ryzyko związane z bardzo długim czasem życia access tokena.
4. Porównaj sesje i JWT dla małej aplikacji webowej.
5. Napisz prosty pseudokod walidacji tokena po stronie backendu.
