# Refresh tokeny python

## O czym jest ten rozdział

Jeśli access token żyje krótko, bardzo szybko pojawia się pytanie:

- skąd brać nowy token bez zmuszania użytkownika do logowania co kilka minut?

Tu właśnie wchodzą refresh tokeny.

To jeden z najważniejszych praktycznych tematów w systemach opartych o tokeny, bo łączy:

- wygodę użytkownika,
- bezpieczeństwo,
- zarządzanie sesją,
- wylogowanie i rotację.

## Najprostsza intuicja

Masz dwa tokeny:

- `access token` — krótko żyjący, używany przy zwykłych requestach,
- `refresh token` — dłużej żyjący, używany do pobrania nowego access tokena.

To oznacza:

- access token może być bardziej krótki i bezpieczny,
- użytkownik nie musi logować się co chwilę,
- backend może lepiej kontrolować odświeżanie sesji.

## Typowy flow

1. użytkownik loguje się,
2. backend zwraca access token i refresh token,
3. klient używa access tokena,
4. access token wygasa,
5. klient wysyła refresh token do endpointu odświeżania,
6. backend sprawdza refresh token,
7. backend wystawia nowy access token,
8. opcjonalnie wystawia też nowy refresh token.

## Przykład odpowiedzi po logowaniu

```json
{
  "access_token": "access_abc",
  "refresh_token": "refresh_xyz",
  "expires_in": 900
}
```

Interpretacja:

- `access_token` służy do zwykłych requestów,
- `refresh_token` służy tylko do odświeżania,
- `expires_in=900` oznacza np. 15 minut.

## Przykład requestu do odświeżenia

```http
POST /refresh
Content-Type: application/json

{
  "refresh_token": "refresh_xyz"
}
```

### Przykładowa odpowiedź

```json
{
  "access_token": "access_new_123",
  "expires_in": 900
}
```

## Minimalna symulacja w Pythonie

```python
valid_refresh_tokens = {"refresh_xyz": 42}


def refresh_access_token(refresh_token: str):
    user_id = valid_refresh_tokens.get(refresh_token)
    if user_id is None:
        return None

    return {
        "access_token": f"access-for-{user_id}",
        "expires_in": 900,
    }


print(refresh_access_token("refresh_xyz"))
print(refresh_access_token("bad-token"))
```

Output:

```text
{'access_token': 'access-for-42', 'expires_in': 900}
None
```

To tylko intuicja, ale pokazuje podstawowy model.

## Dlaczego nie robić bardzo długiego access tokena zamiast refresh tokena

Bo wtedy kradzież tokena jest groźniejsza.

Jeśli access token jest ważny np. miesiąc, to atakujący może używać go przez długi czas.

Lepszy model to często:

- krótki access token,
- bardziej kontrolowany refresh token,
- możliwość rotacji i unieważniania.

## Gdzie trzymać refresh token

To decyzja architektoniczna i bezpieczeństwa.

Najważniejsza zasada na tym etapie:

- refresh token jest bardziej wrażliwy niż access token, bo pozwala uzyskiwać kolejne tokeny.

W praktyce często myśli się o:

- `HttpOnly cookie`,
- bezpiecznym przechowywaniu po stronie klienta zależnie od typu aplikacji,
- silniejszej kontroli użycia niż dla zwykłego access tokena.

## Rotacja refresh tokena

Bardzo dobra praktyka to rotacja.

To znaczy:

1. klient wysyła refresh token,
2. backend wystawia nowy access token,
3. backend wystawia też nowy refresh token,
4. stary refresh token przestaje być ważny.

To zmniejsza ryzyko nadużycia skradzionego refresh tokena.

## Before/after

### Słaby model

- access token żyje bardzo długo,
- refresh token nie jest rotowany,
- brak możliwości unieważnienia.

### Lepszy model

- access token żyje krótko,
- refresh token jest trzymany ostrożnie,
- refresh token jest rotowany,
- backend potrafi go unieważnić.

## Najczęstsze pułapki

### 1. Traktowanie refresh tokena jak zwykłego tokena do API

Refresh token nie powinien latać po wszystkich endpointach.

Jego rola jest wąska:

- służy do odświeżania sesji.

### 2. Brak możliwości wylogowania ze wszystkich urządzeń

Jeśli system nie potrafi unieważnić refresh tokenów, wylogowanie bywa pozorne.

### 3. Brak rotacji

Jeśli ten sam refresh token żyje bardzo długo i można go używać wiele razy, ryzyko rośnie.

### 4. Za długi czas życia refresh tokena bez dodatkowych zabezpieczeń

Długi refresh token może mieć sens, ale musi iść z tym kontrola:

- revocation,
- rotacja,
- monitoring,
- wiązanie z sesją lub urządzeniem.

## Mini case study

Załóżmy taki system:

- access token żyje 10 minut,
- refresh token żyje 14 dni,
- każde odświeżenie generuje nowy refresh token,
- wylogowanie usuwa aktywny refresh token z bazy.

To jest dużo dojrzalszy model niż:

- access token na 30 dni,
- jeden refresh token bez końca,
- brak unieważniania.

## Co backend zwykle sprawdza przy refreshu

- czy token istnieje,
- czy nie wygasł,
- czy nie został unieważniony,
- czy należy do tej sesji lub użytkownika,
- czy nie wykryto reuse starego tokena po rotacji.

## Reuse detection: intuicja

Jeśli po rotacji ktoś spróbuje użyć starego refresh tokena, to może oznaczać wyciek albo próbę nadużycia.

To bardzo cenna informacja bezpieczeństwa.

## Najważniejsze do zapamiętania

- Access token i refresh token mają różne role.
- Refresh token zwykle jest bardziej wrażliwy.
- Krótszy access token + refresh token to często sensowny kompromis.
- Rotacja refresh tokenów znacząco poprawia bezpieczeństwo.
- System powinien umieć token unieważnić, a nie tylko czekać aż sam wygaśnie.

## Ćwiczenia

1. Wyjaśnij własnymi słowami różnicę między access tokenem i refresh tokenem.
2. Narysuj flow odświeżania tokena krok po kroku.
3. Opisz ryzyko wynikające z braku rotacji refresh tokena.
4. Wypisz, co backend powinien sprawdzić przy endpointzie `/refresh`.
5. Zaproponuj sensowny model wylogowania w systemie opartym o refresh tokeny.
