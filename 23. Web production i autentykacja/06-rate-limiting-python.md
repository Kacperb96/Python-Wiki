# Rate limiting python

## O czym jest ten rozdział

Rate limiting to mechanizm ograniczania liczby requestów w danym czasie.

Na początku łatwo myśleć o nim jak o dodatku wydajnościowym, ale w praktyce to także ważny element:

- bezpieczeństwa,
- ochrony przed brute force,
- ochrony przed spamem,
- stabilności systemu,
- sprawiedliwego podziału zasobów.

## Najprostsza intuicja

System mówi:

- "z tego źródła możesz zrobić najwyżej X requestów w czasie Y".

Przykłady:

- 5 prób logowania na minutę,
- 100 requestów na minutę na użytkownika,
- 1000 requestów na godzinę na klucz API.

## Po co to w praktyce

Rate limiting pomaga, gdy chcesz chronić:

- endpoint logowania,
- endpoint resetu hasła,
- publiczne API,
- kosztowne operacje,
- zasoby podatne na scraping albo flood.

## Typowy efekt po przekroczeniu limitu

Serwer może zwrócić np.:

```http
HTTP/1.1 429 Too Many Requests
Content-Type: application/json

{
  "detail": "rate limit exceeded"
}
```

To bardzo typowa odpowiedź.

## Prosta symulacja w Pythonie

```python
from collections import defaultdict

requests_count = defaultdict(int)
LIMIT = 3


def allow_request(client_id: str) -> bool:
    requests_count[client_id] += 1
    return requests_count[client_id] <= LIMIT


for _ in range(4):
    print(allow_request("user-42"))
```

Output:

```text
True
True
True
False
```

To bardzo uproszczony model, ale dobrze pokazuje ideę.

## Co można limitować

Najczęściej limit ustawia się względem:

- adresu IP,
- użytkownika,
- klucza API,
- sesji,
- endpointu,
- kombinacji kilku wymiarów naraz.

## Przykłady praktyczne

### Logowanie

- 5 prób na 15 minut na IP,
- dodatkowo limit na konto użytkownika.

### Publiczne API

- 100 requestów na minutę na klucz API.

### Drogi endpoint raportowy

- 10 requestów na minutę na użytkownika.

## Główne strategie limitowania

Na poziomie intuicji warto znać przynajmniej nazwy i sens:

- fixed window,
- sliding window,
- token bucket,
- leaky bucket.

Nie musisz od razu implementować ich ręcznie, ale dobrze rozumieć trade-offy.

## Fixed window: intuicja

Masz okno czasu, np. jedna minuta.

Jeśli w tej minucie przekroczysz limit, kolejne requesty są blokowane.

Zaleta:

- prostota.

Wada:

- efekt granicy okna, gdzie można zrobić burst na końcu jednego okna i początku następnego.

## Token bucket: intuicja

Wyobraź sobie wiadro z tokenami.

- każdy request zużywa token,
- tokeny powoli się odnawiają,
- jeśli nie ma tokena, request odpada.

To często daje bardziej naturalne zachowanie przy burstach.

## Before/after: zły i lepszy pomysł

### Brak limitu na logowanie

Efekt:

- łatwiej robić brute force,
- łatwiej spamować endpoint,
- system jest bardziej podatny na nadużycia.

### Limit na logowanie

Np.:

- 5 prób na minutę na IP,
- dodatkowy cooldown,
- logowanie zdarzeń.

To już znacząco poprawia sytuację.

## Najczęstsze pułapki

### 1. Limit tylko na IP

Czasem to za mało.

Wspólne sieci, NAT albo proxy mogą zaburzać obraz.

W praktyce często warto patrzeć szerzej.

### 2. Ten sam limit dla wszystkiego

Endpoint logowania, pobieranie profilu i ciężki raport nie powinny zawsze mieć tych samych limitów.

### 3. Brak informacji dla klienta

Jeśli klient dostaje samo `429`, ale nie wiadomo, co dalej, UX bywa słaby.

W praktyce można rozważyć czytelny komunikat albo nagłówki pomocnicze.

### 4. Brak logowania i monitoringu

Jeśli limity często się odpalają, to cenna informacja:

- może ktoś atakuje,
- może klient ma błąd,
- może limit jest za niski.

### 5. Traktowanie rate limiting wyłącznie jako wydajności

To błąd.

To także mechanizm bezpieczeństwa i ochrony jakości usługi.

## Mini case study

Masz endpoint `/login`.

### Bez limitu

Atakujący może wysyłać tysiące prób.

### Z limitem

Po kilku nieudanych próbach dostaje `429`.

Skutek:

- maleje skuteczność brute force,
- maleje obciążenie systemu,
- masz lepszą kontrolę nad nadużyciami.

## Intuicyjny przykład z czasem

```python
import time

attempts = {}
WINDOW = 10
LIMIT = 2


def allow_request(client_id: str) -> bool:
    now = time.time()
    timestamps = attempts.get(client_id, [])
    timestamps = [ts for ts in timestamps if now - ts < WINDOW]

    if len(timestamps) >= LIMIT:
        attempts[client_id] = timestamps
        return False

    timestamps.append(now)
    attempts[client_id] = timestamps
    return True


print(allow_request("ip-1"))
print(allow_request("ip-1"))
print(allow_request("ip-1"))
```

Przykładowy output:

```text
True
True
False
```

To już bardziej przypomina prosty sliding window.

## Kiedy rate limiting ma sens szczególnie mocno

- logowanie,
- reset hasła,
- tworzenie kont,
- endpointy publiczne,
- operacje kosztowne obliczeniowo,
- operacje płatne albo limitowane biznesowo.

## Najważniejsze do zapamiętania

- Rate limiting to nie tylko wydajność, ale też bezpieczeństwo.
- Najczęstsza odpowiedź po przekroczeniu limitu to `429 Too Many Requests`.
- Różne endpointy mogą wymagać różnych limitów.
- Dobrze dobrany limit zmniejsza skuteczność nadużyć.
- Sam limit nie wystarczy, jeśli nie masz monitoringu i sensownej strategii.

## Ćwiczenia

1. Wyjaśnij własnymi słowami, po co daje się rate limiting na endpoint logowania.
2. Podaj trzy różne rzeczy, względem których można robić limitowanie.
3. Opisz różnicę między prostym fixed window i bardziej elastycznym modelem token bucket na poziomie intuicji.
4. Zaprojektuj limit dla endpointu resetu hasła.
5. Wyjaśnij, czemu jeden limit dla wszystkich endpointów bywa złym pomysłem.
