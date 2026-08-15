# Sesje i cookies python

## O czym jest ten rozdział

Ten plik tłumaczy, jak backend "pamięta" użytkownika między kolejnymi requestami.

To bardzo ważny temat, bo HTTP samo w sobie jest bezstanowe. Każdy request jest osobny, więc aplikacja musi mieć jakiś sposób, żeby wiedzieć:

- kim jest użytkownik,
- czy jest zalogowany,
- czy ma aktywną sesję,
- jakie ma uprawnienia albo stan koszyka.

Najczęściej w tym miejscu pojawiają się:

- cookies,
- sesje,
- identyfikatory sesji,
- ustawienia bezpieczeństwa cookie.

## Intuicja: co to jest cookie

Cookie to mały kawałek danych, który serwer może wysłać do przeglądarki.

Przeglądarka zapisuje go i dołącza do kolejnych requestów do tej samej domeny.

Najprostsza intuicja:

- serwer mówi: "zapamiętaj to",
- przeglądarka odpowiada: "okej, będę to dosyłać przy kolejnych żądaniach".

## Intuicja: co to jest sesja

Sesja to informacja po stronie serwera o zalogowanym lub aktywnym użytkowniku.

Bardzo często działa to tak:

1. użytkownik loguje się,
2. serwer tworzy sesję w pamięci lub bazie,
3. sesja dostaje `session_id`,
4. `session_id` trafia do cookie,
5. przeglądarka wysyła to cookie przy kolejnych requestach,
6. serwer po `session_id` odnajduje dane sesji.

W praktyce:

- dane sesji są na serwerze,
- klient trzyma tylko identyfikator.

To jest ważna różnica względem wielu systemów tokenowych.

## Cookie a sesja: to nie to samo

To pojęcia bardzo powiązane, ale nie identyczne.

Cookie:

- jest mechanizmem przechowywania i dosyłania małego kawałka danych przez przeglądarkę.

Sesja:

- jest mechanizmem przechowywania stanu użytkownika po stronie serwera.

Typowy układ:

- cookie przenosi `session_id`,
- serwer na podstawie `session_id` odczytuje sesję.

## Przykład flow krok po kroku

### Krok 1: logowanie

Użytkownik wysyła dane:

```http
POST /login
Content-Type: application/json

{
  "email": "jan@example.com",
  "password": "tajne_haslo"
}
```

Serwer sprawdza dane i odpowiada:

```http
HTTP/1.1 200 OK
Set-Cookie: session_id=abc123; HttpOnly; Secure; SameSite=Lax
Content-Type: application/json

{
  "message": "zalogowano"
}
```

### Co się stało

- serwer stworzył sesję,
- sesja dostała identyfikator `abc123`,
- przeglądarka zapisała cookie `session_id=abc123`.

### Krok 2: kolejny request

Przeglądarka sama dośle cookie:

```http
GET /me
Cookie: session_id=abc123
```

Serwer patrzy na `session_id`, znajduje sesję i wie, kim jest użytkownik.

### Odpowiedź

```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "email": "jan@example.com",
  "name": "Jan"
}
```

## Minimalna symulacja w Pythonie

To nie jest pełny frameworkowy przykład, tylko prosta intuicja.

```python
sessions = {}


def login(user_id: int) -> str:
    session_id = f"session-{user_id}"
    sessions[session_id] = {"user_id": user_id, "logged_in": True}
    return session_id


def get_current_user(session_id: str):
    session = sessions.get(session_id)
    if not session:
        return None
    return session["user_id"]


sid = login(42)
print(sid)
print(get_current_user(sid))
print(get_current_user("wrong-id"))
```

Output:

```text
session-42
42
None
```

W realnym systemie:

- `session_id` byłby losowy i trudny do odgadnięcia,
- sesje byłyby w bazie, Redisie albo storage sesji,
- cookie ustawia backend przez nagłówek `Set-Cookie`.

## Najważniejsze atrybuty cookie

### `HttpOnly`

Jeśli cookie ma `HttpOnly`, to JavaScript w przeglądarce nie może go odczytać przez `document.cookie`.

To pomaga ograniczyć skutki części ataków XSS.

### `Secure`

Cookie z flagą `Secure` powinno być wysyłane tylko przez HTTPS.

To bardzo ważne w produkcji.

### `SameSite`

Steruje tym, kiedy cookie ma być wysyłane przy requestach między stronami.

Najczęstsze wartości:

- `Strict`
- `Lax`
- `None`

Bardzo skrótowo:

- `Strict` jest najbardziej restrykcyjne,
- `Lax` jest często sensownym kompromisem,
- `None` zwykle wymaga `Secure` i jest potrzebne np. przy niektórych cross-site flow.

## Przykład before/after dla cookie

### Bez ustawień bezpieczeństwa

```http
Set-Cookie: session_id=abc123
```

### Lepsza wersja

```http
Set-Cookie: session_id=abc123; HttpOnly; Secure; SameSite=Lax
```

Druga wersja jest bezpieczniejsza, bo:

- ogranicza dostęp z JavaScriptu,
- wymusza HTTPS,
- pomaga kontrolować wysyłkę cookie w cross-site requestach.

## Kiedy sesje mają sens

Sesje bardzo często są dobrym wyborem, gdy:

- masz klasyczną aplikację webową,
- backend i frontend są blisko siebie,
- chcesz prostsze wylogowanie i unieważnianie stanu,
- chcesz trzymać wrażliwszy stan po stronie serwera,
- nie potrzebujesz rozproszonego, bezstanowego systemu tokenowego.

## Zalety sesji

- stan użytkownika jest po stronie serwera,
- łatwiej unieważnić sesję,
- łatwiej wymusić wylogowanie,
- nie trzeba upychać informacji w tokenie po stronie klienta,
- model jest prosty do zrozumienia.

## Wady sesji

- serwer musi gdzieś przechowywać stan,
- w większej skali trzeba dobrze rozwiązać storage sesji,
- przy wielu instancjach aplikacji często potrzebujesz współdzielonego magazynu sesji,
- architektura jest mniej bezstanowa niż w niektórych systemach tokenowych.

## Najczęstsze pułapki

### 1. Trzymanie zbyt wielu danych w cookie

Cookie nie jest miejscem na duże lub wrażliwe dane użytkownika.

Zły pomysł:

- email,
- rola,
- całe profile,
- dane biznesowe,
- hasła.

Lepiej:

- trzymać minimalny identyfikator,
- resztę czytać po stronie serwera.

### 2. Brak wygaszania sesji

Jeśli sesja nigdy nie wygasa, ryzyko rośnie.

W praktyce warto mieć:

- czas życia sesji,
- wygaszanie po bezczynności,
- możliwość ręcznego unieważnienia.

### 3. Brak rotacji `session_id` po logowaniu

Po udanym logowaniu często warto wygenerować świeże `session_id`, żeby ograniczyć ryzyko session fixation.

### 4. Brak `HttpOnly` i `Secure`

To bardzo częsty błąd w materiałach początkujących i małych projektach demo.

## Mini antyprzykład

```python
cookie_value = {
    "user_id": 42,
    "email": "jan@example.com",
    "role": "admin",
}
```

To zły kierunek jako zwykłe cookie po stronie klienta, bo:

- klient widzi te dane,
- klient może próbować nimi manipulować,
- łatwo przesadzić z ilością informacji.

## Kiedy cookie nie oznacza zalogowania

Samo posiadanie cookie jeszcze nie znaczy, że użytkownik jest poprawnie uwierzytelniony.

Trzeba sprawdzić:

- czy cookie istnieje,
- czy sesja istnieje po stronie serwera,
- czy nie wygasła,
- czy nie została unieważniona,
- czy użytkownik nadal ma dostęp.

## Sesje a API

W wielu nowoczesnych API ludzie automatycznie myślą o JWT, ale sesje nadal mają sens.

Szczególnie gdy:

- aplikacja jest głównie webowa,
- kontrolujesz frontend i backend,
- chcesz prostszy model bezpieczeństwa,
- nie potrzebujesz przenosić stanu między wieloma niezależnymi klientami.

## Najważniejsze do zapamiętania

- HTTP jest bezstanowe, więc stan użytkownika trzeba utrzymać dodatkowym mechanizmem.
- Cookie i sesja to nie to samo.
- Bardzo częsty model to: cookie z `session_id` + sesja po stronie serwera.
- `HttpOnly`, `Secure` i `SameSite` to praktyczne, ważne ustawienia.
- Sesje są nadal bardzo sensownym rozwiązaniem w wielu projektach.

## Ćwiczenia

1. Narysuj własnymi słowami flow logowania opartego o sesję.
2. Wyjaśnij różnicę między cookie a sesją bez używania słowa "to prawie to samo".
3. Wypisz trzy ryzyka wynikające ze złej konfiguracji cookie.
4. Opisz, co backend powinien zrobić przy wylogowaniu użytkownika.
5. Wyjaśnij, kiedy wybrałbyś sesje zamiast JWT.
