# Csrf xss ssrf python

To są trzy różne klasy problemów bezpieczeństwa, które początkujący często wrzucają do jednego worka.

Warto je rozróżniać bardzo jasno.

## 1. `CSRF`

`CSRF` oznacza sytuację, w której przeglądarka zalogowanego użytkownika wykonuje niechcianą akcję w aplikacji.

Intuicja:

- użytkownik jest zalogowany,
- jego przeglądarka ma ważną sesję,
- złośliwa strona próbuje wymusić request do właściwej aplikacji,
- serwer błędnie uznaje to za legalne działanie użytkownika.

To dotyczy głównie aplikacji opartych o sesję/cookies.

### Przykład myślowy

Użytkownik jest zalogowany do panelu.

Otwiera inną stronę, która ukrycie wysyła request:

```text
POST /change-email
```

Jeśli serwer nie ma dobrej ochrony `CSRF`, może przyjąć tę zmianę.

### Ochrona

Typowe mechanizmy:

- token `CSRF`,
- odpowiednie ustawienia cookies,
- sprawdzanie źródła i kontekstu żądania,
- rozdzielenie metod tylko do odczytu od metod zmieniających stan.

## 2. `XSS`

`XSS` oznacza, że do strony trafia niebezpieczna treść, którą przeglądarka potraktuje jak kod.

Intuicja:

- użytkownik dostarcza dane,
- aplikacja wyświetla je bezpiecznie albo niebezpiecznie,
- jeśli wyświetla je źle, może dojść do wykonania złośliwego skryptu.

### Myślowy przykład

Jeśli użytkownik zapisze komentarz zawierający skrypt, a aplikacja wyrenderuje go bez odpowiedniego escapowania, ktoś inny może otworzyć stronę i uruchomić ten skrypt w swojej przeglądarce.

### Skutki

- kradzież sesji,
- przejęcie działań użytkownika,
- podmiana treści na stronie,
- wykonywanie złośliwych akcji po stronie klienta.

### Ochrona

- escapowanie outputu,
- bezpieczne renderowanie HTML,
- nieufność wobec danych od użytkownika,
- ograniczenie wstrzykiwania surowego HTML/JS.

## 3. `SSRF`

`SSRF` oznacza, że atakujący wykorzystuje aplikację-serwer do wykonywania żądań do innych zasobów.

Intuicja:

- aplikacja potrafi pobierać zasoby po URL,
- użytkownik kontroluje ten URL,
- serwer robi request w imieniu aplikacji,
- przez to może sięgnąć tam, gdzie użytkownik normalnie by nie sięgnął.

### Przykład myślowy

Masz funkcję:

```python
download(url)
```

Jeśli użytkownik może podać dowolny URL, aplikacja może zostać zmuszona do pobrania czegoś z wewnętrznej sieci, panelu admina albo wrażliwego zasobu.

### Ochrona

- allowlisty domen lub hostów,
- brak pełnej swobody w podawaniu URL,
- ograniczanie dostępu do sieci wewnętrznej,
- walidacja schematów i kierunków requestów.

## 4. Jak to odróżniać

### `CSRF`

Problem dzieje się przez zaufanie do sesji użytkownika i requestu z przeglądarki.

### `XSS`

Problem dzieje się przez niebezpieczne wyświetlanie danych w przeglądarce.

### `SSRF`

Problem dzieje się wtedy, gdy serwer wykonuje request tam, gdzie nie powinien.

## 5. Najczęstsze błędy początkujących

- traktowanie każdego inputu HTML jako bezpiecznego,
- brak zrozumienia różnicy między atakiem na przeglądarkę a atakiem przez backend,
- pozwalanie użytkownikowi na pełną kontrolę adresów URL,
- przekonanie, że "aplikacja wewnętrzna nie potrzebuje takich zabezpieczeń".

## 6. Mini porównanie

Objaw:

```text
Po wejściu na stronę komentarza wykonuje się dziwny kod w przeglądarce.
```

Najbardziej pasuje:

`XSS`

Objaw:

```text
Zalogowany użytkownik wykonał akcję, której sam nie kliknął.
```

Najbardziej pasuje:

`CSRF`

Objaw:

```text
Aplikacja backendowa pobiera zasoby z podejrzanych lub wewnętrznych adresów.
```

Najbardziej pasuje:

`SSRF`

## Zadania

1. Wyjaśnij własnymi słowami różnicę między `CSRF`, `XSS` i `SSRF`.
2. Podaj po jednym przykładzie sytuacji pasującej do każdego z tych problemów.
3. Opisz, dlaczego możliwość podania dowolnego URL przez użytkownika bywa ryzykowna.
