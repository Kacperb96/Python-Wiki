# CORS i middleware python

## O czym jest ten rozdział

W pracy z backendem webowym dwa pojęcia wracają bardzo często:

- `CORS`,
- `middleware`.

Początkujący często traktują je jak magię frameworka, ale warto rozumieć je prosto i praktycznie.

CORS dotyczy tego, jak przeglądarka kontroluje cross-origin requesty.
Middleware to warstwa kodu, przez którą przechodzą requesty i odpowiedzi.

## Co to jest origin

Origin to zestaw:

- protokół,
- host,
- port.

Przykłady:

- `https://app.example.com`
- `http://localhost:3000`
- `http://localhost:8000`

To są różne originy.

Nawet jeśli host jest podobny, zmiana portu albo protokołu tworzy nowy origin.

## Czym jest CORS

CORS to mechanizm przeglądarki określający, kiedy frontend z jednego originu może wykonać request do backendu z innego originu.

Najważniejsza intuicja:

- to przeglądarka pilnuje zasad CORS,
- backend odpowiada odpowiednimi nagłówkami,
- to nie jest ogólny mechanizm zabezpieczający każde źródło ruchu w internecie.

## Typowy problem

Frontend działa na:

```text
http://localhost:3000
```

Backend działa na:

```text
http://localhost:8000
```

Frontend robi request do backendu.

Jeśli backend nie zwraca odpowiednich nagłówków CORS, przeglądarka może zablokować odpowiedź.

## Przykładowy nagłówek

```http
Access-Control-Allow-Origin: http://localhost:3000
```

To mówi przeglądarce, że ten origin jest dozwolony.

## Before/after

### Brak konfiguracji CORS

Efekt:

- request może dojść do backendu,
- ale przeglądarka zablokuje frontendowi dostęp do odpowiedzi.

### Poprawniejsza konfiguracja

Backend zwraca np.:

```http
Access-Control-Allow-Origin: http://localhost:3000
Access-Control-Allow-Credentials: true
```

To pozwala przeglądarce zaakceptować odpowiedź w danym scenariuszu.

## CORS nie jest główną ochroną backendu

To bardzo ważne.

CORS nie zastępuje:

- autoryzacji,
- uwierzytelniania,
- walidacji,
- kontroli uprawnień.

Jeśli ktoś wysyła request np. poza przeglądarką, CORS sam w sobie nie rozwiązuje problemu dostępu.

Dlatego nie wolno myśleć:

- "mam CORS, więc backend jest bezpieczny".

## Preflight request: intuicja

Przy niektórych requestach przeglądarka najpierw wysyła zapytanie `OPTIONS`, żeby sprawdzić, czy dana operacja jest dozwolona.

To nazywa się preflight.

Przykład:

```http
OPTIONS /orders
Origin: http://localhost:3000
Access-Control-Request-Method: POST
Access-Control-Request-Headers: Authorization, Content-Type
```

Backend odpowiada np.:

```http
HTTP/1.1 204 No Content
Access-Control-Allow-Origin: http://localhost:3000
Access-Control-Allow-Methods: GET, POST, OPTIONS
Access-Control-Allow-Headers: Authorization, Content-Type
```

Dopiero potem przeglądarka wykona właściwy request.

## Najczęstsze pułapki CORS

### 1. Ustawienie `*` wszędzie bez myślenia

`Access-Control-Allow-Origin: *` bywa wygodne w demie, ale nie zawsze pasuje do produkcji.

Szczególnie gdy używasz ciasteczek lub credentiali.

### 2. Mylenie błędu CORS z błędem backendu

Czasem backend odpowiada poprawnie, ale frontend i tak widzi błąd z powodu przeglądarki.

### 3. Brak obsługi `OPTIONS`

Jeśli backend nie radzi sobie z preflightem, frontend może nie działać mimo poprawnej logiki endpointu.

### 4. Zbyt szerokie dopuszczenie originów

To zwiększa powierzchnię ryzyka i robi chaos konfiguracyjny.

## Co to jest middleware

Middleware to kod wykonywany pomiędzy przyjęciem requestu a wygenerowaniem odpowiedzi.

Może działać:

- przed wejściem do endpointu,
- po wyjściu z endpointu,
- wokół całego cyklu request-response.

## Do czego używa się middleware

Najczęściej do:

- logowania requestów,
- mierzenia czasu odpowiedzi,
- autoryzacji,
- dodawania nagłówków,
- obsługi CORS,
- śledzenia identyfikatora requestu,
- obsługi wyjątków.

## Prosty przykład intuicyjny

```python
def logging_middleware(handler):
    def wrapped(request):
        print(f"before: {request}")
        response = handler(request)
        print(f"after: {response}")
        return response
    return wrapped


def endpoint(request):
    return {"status": 200, "path": request["path"]}


wrapped_endpoint = logging_middleware(endpoint)
result = wrapped_endpoint({"path": "/orders"})
print(result)
```

Output:

```text
before: {'path': '/orders'}
after: {'status': 200, 'path': '/orders'}
{'status': 200, 'path': '/orders'}
```

To nie jest frameworkowy middleware, ale intuicja jest bardzo podobna.

## Przykład praktyczny: middleware mierzący czas

```python
import time


def timing_middleware(handler):
    def wrapped(request):
        start = time.time()
        response = handler(request)
        duration = time.time() - start
        print(f"request took {duration:.6f}s")
        return response
    return wrapped
```

To pokazuje, że middleware często realizuje przekrojowe zachowania wspólne dla wielu endpointów.

## Kiedy middleware ma sens

Middleware ma sens wtedy, gdy logika:

- dotyczy wielu endpointów,
- nie jest częścią właściwej logiki biznesowej jednego endpointu,
- powinna być wykonywana spójnie w całej aplikacji.

## Kiedy middleware jest złym miejscem

Jeśli próbujesz wrzucić do middleware bardzo specyficzną logikę domenową jednego przypadku biznesowego, to zwykle znak, że warstwa jest źle dobrana.

## CORS i middleware razem

W wielu frameworkach konfiguracja CORS jest realizowana właśnie jako middleware.

To wygodne, bo:

- każdy request przechodzi przez wspólną warstwę,
- można spójnie dodawać nagłówki,
- łatwiej obsłużyć preflight.

## Najważniejsze do zapamiętania

- CORS dotyczy zachowania przeglądarki przy cross-origin requestach.
- CORS nie zastępuje uwierzytelniania ani autoryzacji.
- Preflight `OPTIONS` jest normalną częścią wielu flow CORS.
- Middleware to warstwa na zachowania przekrojowe, nie miejsce na każdy rodzaj logiki.
- Dobrze zaprojektowany middleware upraszcza aplikację i centralizuje wspólne mechanizmy.

## Ćwiczenia

1. Wyjaśnij własnymi słowami, czym jest origin.
2. Opisz, czemu frontend na `localhost:3000` może mieć problem z backendem na `localhost:8000`.
3. Wytłumacz, czemu CORS nie zastępuje autoryzacji.
4. Podaj trzy dobre zastosowania middleware.
5. Opisz, kiedy middleware byłby złym miejscem na logikę biznesową.
