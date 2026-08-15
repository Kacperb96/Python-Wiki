# Debugowanie buildow i healthcheckow python

## Po co ten plik

W praktyce bardzo wiele problemów z Dockerem nie bierze się z samego kodu aplikacji, tylko z tego, że:

- obraz buduje się zbyt długo,
- usługa nie wstaje,
- kontener startuje, ale aplikacja nie działa,
- worker nie widzi brokera,
- web rusza szybciej niż baza,
- healthcheck pokazuje coś innego niż realne użycie systemu.

Ten plik zbiera najbardziej praktyczne problemy i sposoby myślenia o ich diagnozie.

## Najczęstsze klasy problemów

Najczęściej trafisz na problemy typu:

- build trwa za długo,
- obraz jest ogromny,
- kontener kończy się zaraz po starcie,
- usługa działa lokalnie, ale nie działa w compose,
- web nie łączy się z bazą,
- worker nie widzi Redis lub brokera,
- healthcheck nie przechodzi,
- jedna usługa czeka na drugą w nieprzewidywalny sposób.

## Problem 1: build trwa bardzo długo

### Pierwsze hipotezy

- Dockerfile źle wykorzystuje cache,
- `COPY . .` jest za wcześnie,
- brak `.dockerignore`,
- obraz ciągnie za dużo zależności,
- instalacja systemowych pakietów jest ciężka i częsta.

### Co sprawdzić

1. czy plik zależności kopiujesz przed całym kodem,
2. czy `.dockerignore` usuwa śmieci z kontekstu,
3. czy nie kopiujesz `.git`, `.venv`, cache i artefaktów,
4. czy nie unieważniasz cache przy każdej małej zmianie,
5. czy obraz bazowy nie jest niepotrzebnie ciężki.

## Problem 2: obraz jest ogromny

### Pierwsze hipotezy

- zbyt ciężka baza,
- brak multi-stage build,
- pliki developerskie w obrazie,
- cache i build tools zostały w runtime,
- kopiujesz za dużo rzeczy.

### Co poprawiać

- lżejsza baza typu `slim`,
- ograniczenie kontekstu przez `.dockerignore`,
- multi-stage build,
- tylko runtime dependencies w finalnym obrazie,
- brak sekretów i śmieci.

## Problem 3: kontener startuje i od razu kończy się

To bardzo częsty objaw.

### Możliwe przyczyny

- zła komenda startowa,
- aplikacja rzuca wyjątek na starcie,
- brak wymaganych env vars,
- proces główny kończy się natychmiast,
- worker nie może połączyć się z brokerem i pada.

### Co sprawdzić

1. komendę `CMD` lub `command`,
2. logi kontenera,
3. walidację env na starcie,
4. czy proces główny naprawdę jest długowieczny,
5. czy usługa zależna jest dostępna.

## Problem 4: web nie łączy się z bazą

### Pierwsze hipotezy

- zła `DATABASE_URL`,
- zły host w URL,
- baza jeszcze nie gotowa,
- kontenery są w innym kontekście sieciowym niż zakładano,
- env nie został poprawnie przekazany.

### Kluczowa intuicja

W compose hostem bazy często nie jest `localhost`, tylko nazwa usługi, np. `db`.

To jest bardzo częsta pułapka początkujących.

## Problem 5: worker nie widzi brokera

### Możliwe przyczyny

- zły `REDIS_URL` albo `BROKER_URL`,
- worker ma inne env niż web,
- broker jeszcze nie jest gotowy,
- kontener workera startuje poprawnie, ale aplikacja nie może zestawić połączenia.

To bardzo często nie jest problem Celery jako takiego, tylko środowiska.

## Healthcheck: najprostsza intuicja

Healthcheck to sposób na automatyczne sprawdzanie, czy usługa wygląda na zdrową.

Najprościej:

- kontener działa to za mało,
- trzeba jeszcze wiedzieć, czy usługa w środku naprawdę odpowiada sensownie.

## Przykład intuicyjny healthchecku

Dla weba można myśleć o sprawdzaniu endpointu typu:

```text
GET /health
```

Dla bazy:

- czy przyjmuje połączenie.

Dla workera:

- czy proces żyje i umie gadać z brokerem lub wykonać podstawowe sprawdzenie.

## Healthcheck nie jest pełnym testem biznesowym

To ważne.

Healthcheck nie powinien próbować robić całego scenariusza zamówienia.

Ma odpowiadać raczej na pytanie:

- czy usługa jest w stanie podstawowo działać?

Nie:

- czy cały system biznesowy działa idealnie end-to-end.

## Problem 6: `depends_on` nie wystarcza

To bardzo klasyczna pułapka.

`depends_on` pomaga w kolejności startu kontenerów, ale nie gwarantuje gotowości usług.

Przykład:

- `db` wystartował jako kontener,
- ale Postgres jeszcze nie przyjmuje połączeń,
- web już próbuje się połączyć,
- dostajesz błąd na starcie.

To dlatego healthchecki i logika ponowień startu bywają potrzebne.

## Mini case study: lokalnie działa, w compose nie działa

Objaw:

- `python app.py` lokalnie działa,
- w kontenerze web pada od razu.

### Możliwe przyczyny

- brak pakietu systemowego w obrazie,
- zły katalog roboczy,
- brak env,
- zła komenda startowa,
- inna ścieżka importów,
- zależność od lokalnego pliku, którego nie ma w obrazie.

### Co robić

- porównać realne środowisko lokalne i obraz,
- sprawdzić, co naprawdę trafiło do obrazu,
- przejrzeć logi i komendę startową.

## Mini case study: healthcheck przechodzi, ale użytkownik nadal ma błędy

To też się zdarza.

### Co to znaczy

- healthcheck może być zbyt płytki,
- np. web odpowiada na `/health`, ale nie ma połączenia z ważną zależnością,
- albo jedna rola działa, ale worker i tak jest martwy.

Wniosek:

- healthcheck musi być sensowny, ale nie za ciężki,
- i trzeba wiedzieć, czego dokładnie dowodzi.

## Co warto logować i obserwować

Przy problemach środowiskowych bardzo przydają się:

- log startu kontenera,
- log walidacji env,
- błędy połączeń do bazy i brokera,
- czasy buildów,
- rozmiar obrazu,
- status healthchecków,
- liczba restartów kontenera.

## Szybka checklista debugowania

Gdy coś nie działa, sprawdź po kolei:

1. czy obraz zbudował się z tego, co naprawdę chciałeś spakować,
2. czy komenda startowa jest poprawna,
3. czy env vars są obecne,
4. czy hosty usług w compose są poprawne,
5. czy zależności naprawdę są gotowe, a nie tylko uruchomione,
6. czy logi pokazują błąd importu, połączenia albo konfiguracji,
7. czy healthcheck mierzy właściwą rzecz,
8. czy problem dotyczy weba, workera, schedulera czy samego obrazu.

## Flaky problemy startowe

Są też problemy, które wyglądają losowo.

Przykłady:

- raz web połączy się z bazą, raz nie,
- raz worker złapie Redis, raz padnie,
- raz scheduler wystartuje po czasie, raz nie.

To często pachnie:

- gotowością usług,
- brakiem retry przy starcie,
- zbyt naiwnym założeniem o kolejności uruchomienia.

## Co ten plik pokazuje

Najważniejsza lekcja:

- środowisko kontenerowe to nie tylko budowanie obrazu,
- to także diagnoza cache, startu procesu, połączeń, gotowości usług i sensowności healthchecków.

## Najważniejsze do zapamiętania

- Długi build zwykle oznacza problem z cache, kontekstem albo ciężarem obrazu.
- Start kontenera nie oznacza jeszcze gotowości usługi.
- `depends_on` nie rozwiązuje pełnej gotowości zależności.
- Healthcheck powinien być sensowny, ale nie zbyt ciężki.
- Logi, env i hosty usług to pierwsze miejsca, które warto sprawdzać przy awarii środowiska.

## Ćwiczenia

1. Rozpisz checklistę debugowania problemu "web nie łączy się z bazą".
2. Podaj trzy powody, dla których build obrazu może być niepotrzebnie wolny.
3. Wyjaśnij własnymi słowami, czemu uruchomiony kontener nie zawsze oznacza gotową usługę.
4. Zaprojektuj prosty healthcheck dla aplikacji webowej.
5. Opisz, jak odróżniłbyś problem obrazu od problemu konfiguracji env albo gotowości zależności.
