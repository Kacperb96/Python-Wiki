# OAuth2 podstawy praktyczne python

## O czym jest ten rozdział

OAuth2 to temat, który bardzo często jest źle rozumiany na starcie.

Wiele osób mówi:

- "logowanie przez OAuth2",
- "JWT i OAuth2 to prawie to samo",
- "OAuth2 to po prostu token".

To są uproszczenia, które później robią bałagan.

Ten plik ma dać praktyczną intuicję: po co istnieje OAuth2 i gdzie naprawdę ma zastosowanie.

## Najważniejsza intuicja

OAuth2 to przede wszystkim framework autoryzacji.

Czyli nie tyle odpowiada na pytanie:

- kim jesteś?

ale raczej:

- czy ta aplikacja może dostać określony dostęp do zasobu w imieniu użytkownika albo jako klient?

To ważne, bo OAuth2 nie jest prostą definicją logowania użytkownika.

## Prosty przykład z życia

Wyobraź sobie aplikację, która chce uzyskać dostęp do Twojego kalendarza albo dysku w chmurze.

Nie chcesz dawać tej aplikacji swojego hasła do głównego konta.

Lepszy model jest taki:

1. aplikacja prosi o dostęp,
2. użytkownik widzi ekran zgody,
3. użytkownik zgadza się albo nie,
4. provider wystawia token z ograniczonym zakresem dostępu,
5. aplikacja działa tylko w granicach tej zgody.

To właśnie jest intuicja OAuth2.

## Główne role w OAuth2

Najczęściej spotkasz takie role:

- `resource owner` — zwykle użytkownik,
- `client` — aplikacja prosząca o dostęp,
- `authorization server` — serwer wydający tokeny,
- `resource server` — serwer z chronionymi zasobami.

### Mini mapa

- użytkownik posiada dane,
- aplikacja chce do nich dostęp,
- serwer autoryzacji wydaje token,
- serwer zasobów przyjmuje token i udostępnia dane.

## Co to jest scope

Scope to zakres dostępu.

To bardzo ważne pojęcie.

Przykład:

- `calendar.read`
- `calendar.write`
- `profile.read`
- `orders:read`

Dzięki scope'om aplikacja nie musi dostawać pełnych uprawnień do wszystkiego.

## Typowy flow w dużym skrócie

Najbardziej praktycznie na start warto rozumieć flow z autoryzacją użytkownika.

W uproszczeniu:

1. użytkownik klika "zaloguj przez dostawcę" albo "połącz konto",
2. aplikacja przekierowuje go do serwera autoryzacji,
3. użytkownik loguje się tam i zatwierdza zgodę,
4. aplikacja dostaje kod autoryzacyjny,
5. aplikacja wymienia kod na token,
6. aplikacja używa tokena do pobrania zasobu.

## Przykład krok po kroku

### Krok 1: przekierowanie użytkownika

Przeglądarka trafia na URL podobny do:

```text
https://auth.example.com/authorize?response_type=code&client_id=myapp123&redirect_uri=https://myapp.com/callback&scope=profile.read orders:read&state=abc987
```

### Co oznaczają pola

- `response_type=code` — chcemy kod autoryzacyjny,
- `client_id` — identyfikuje aplikację,
- `redirect_uri` — gdzie wróci użytkownik,
- `scope` — o jaki dostęp prosimy,
- `state` — pomaga chronić flow i zachować kontekst.

### Krok 2: provider odsyła użytkownika

Po zgodzie użytkownik wraca np. na:

```text
https://myapp.com/callback?code=AUTH_CODE_123&state=abc987
```

### Krok 3: backend wymienia kod na token

Backend wysyła request do serwera autoryzacji.

### Przykładowy request

```http
POST /token
Content-Type: application/x-www-form-urlencoded

grant_type=authorization_code&code=AUTH_CODE_123&client_id=myapp123&client_secret=sekret&redirect_uri=https://myapp.com/callback
```

### Przykładowa odpowiedź

```json
{
  "access_token": "token_abc",
  "token_type": "Bearer",
  "expires_in": 3600,
  "refresh_token": "refresh_xyz",
  "scope": "profile.read orders:read"
}
```

## Co tu jest najważniejsze praktycznie

Najważniejsze są trzy rzeczy:

- aplikacja nie dostaje hasła użytkownika do zewnętrznego systemu,
- dostęp może być ograniczony przez scope,
- token można wygasić i odświeżać.

## OAuth2 a logowanie

Tu łatwo o zamieszanie.

OAuth2 sam w sobie dotyczy autoryzacji dostępu.

W praktyce bywa używany w flow logowania, ale nie należy myśleć, że:

- OAuth2 = pełna definicja uwierzytelniania użytkownika.

W realnych systemach logowanie federacyjne często opiera się o dodatkowe warstwy i standardy, ale na tym etapie najważniejsze jest dobre rozumienie samego rdzenia OAuth2.

## OAuth2 a JWT

To nie są synonimy.

OAuth2:

- opisuje przepływy uzyskiwania dostępu,
- definiuje role i sposób wydawania tokenów.

JWT:

- jest formatem tokena.

Możliwe sytuacje:

- OAuth2 używa tokena w formacie JWT,
- OAuth2 używa tokena niebędącego JWT,
- aplikacja używa JWT bez pełnego OAuth2 flow wewnątrz własnego systemu.

## Mini before/after: złe i dobre myślenie

### Złe myślenie

- "OAuth2 to taki JWT z logowaniem"

### Lepsze myślenie

- "OAuth2 opisuje, jak aplikacja dostaje autoryzowany dostęp do zasobu; JWT może być jednym z formatów tokena"

## Najczęstsze pułapki

### 1. Brak rozumienia `state`

`state` pomaga chronić flow i wiązać odpowiedź z konkretną próbą autoryzacji.

To nie jest przypadkowy ozdobnik.

### 2. Zbyt szerokie scope'y

Jeśli aplikacja prosi o wszystko, rośnie ryzyko i maleje zaufanie.

Lepsza praktyka:

- proś tylko o to, co naprawdę potrzebne.

### 3. Mylenie klienta publicznego i poufnego

Nie każde środowisko może bezpiecznie trzymać sekret klienta.

To ważne projektowo.

### 4. Traktowanie access tokena jak stałego klucza

Access tokeny zwykle powinny żyć krótko.

## Pseudokod intuicyjny

```python
def exchange_code_for_token(code: str) -> dict:
    if not code:
        raise ValueError("missing code")

    return {
        "access_token": "token_abc",
        "refresh_token": "refresh_xyz",
        "scope": "profile.read",
    }


result = exchange_code_for_token("AUTH_CODE_123")
print(result["access_token"])
print(result["scope"])
```

Output:

```text
token_abc
profile.read
```

To oczywiście nie jest prawdziwa implementacja, ale buduje flow w głowie.

## Kiedy OAuth2 ma sens

OAuth2 ma sens, gdy:

- aplikacja chce uzyskać dostęp do danych lub zasobów innego systemu,
- masz ekrany zgody użytkownika,
- chcesz ograniczyć zakres dostępu przez scope,
- budujesz integracje między systemami,
- potrzebujesz standardowego modelu delegowania dostępu.

## Kiedy nie zaczynać od OAuth2

Jeśli budujesz bardzo prostą lokalną aplikację i nie masz zewnętrznych dostawców ani złożonych przepływów, pełne OAuth2 może być za ciężkie na start.

Najpierw warto dobrze rozumieć:

- zwykłe logowanie,
- sesje,
- tokeny,
- role i uprawnienia.

## Najważniejsze do zapamiętania

- OAuth2 to framework autoryzacji, a nie po prostu "login".
- Nie daje się aplikacji cudzego hasła, tylko ograniczony dostęp.
- Scope określa, do czego aplikacja ma prawo.
- OAuth2 i JWT to różne pojęcia.
- Najlepiej myśleć o OAuth2 jako o delegowaniu dostępu w kontrolowany sposób.

## Ćwiczenia

1. Wyjaśnij różnicę między OAuth2 i JWT w dwóch zdaniach.
2. Opisz flow: aplikacja prosi o dostęp do kalendarza użytkownika.
3. Wyjaśnij, po co istnieje `scope`.
4. Wytłumacz, czemu aplikacja nie powinna dostawać hasła użytkownika do zewnętrznego systemu.
5. Wypisz trzy błędy projektowe przy wdrażaniu OAuth2.
