# 30. Projekty premium

Ten folder nie jest o składni.

To jest folder o projektach, po których ktoś patrzy na repo i myśli:

`okej, autor naprawdę umie Pythona`

Nie chodzi tylko o to, żeby projekt działał.

Chodzi o to, żeby:

- pokazywał dobrą architekturę,
- miał sensowne testy,
- był czytelny,
- używał narzędzi świadomie,
- rozwiązywał realny problem,
- i robił wrażenie skalą albo pomysłem.

Poniżej masz listę projektów od łatwiejszych do bardzo wymagających.

Przy każdym projekcie masz:

- **poziom trudności**,
- **efekt wow**,
- **co budujesz**,
- **co powinno się tam znaleźć**,
- **co sprawi, że projekt będzie wyglądał jak robiony przez kozaka**.

## 1. CLI do inteligentnego porządkowania plików

**Poziom:** łatwy / średni

**Efekt wow:** mały, ale bardzo solidny początek

### Co budujesz

Narzędzie CLI, które skanuje folder i przenosi pliki do kategorii:

- obrazy,
- PDF-y,
- archiwa,
- audio,
- wideo,
- kod,
- inne.

### Co powinno się tam znaleźć

- `pathlib`
- `argparse` albo `typer`
- logowanie
- tryb `--dry-run`
- filtrowanie po rozszerzeniach
- testy jednostkowe

### Co robi różnicę

- raport przed i po porządkowaniu,
- wykrywanie konfliktów nazw,
- cofanie operacji przez zapis planu zmian do JSON-a.

## 2. Menedżer snippetów programistycznych

**Poziom:** łatwy / średni

**Efekt wow:** praktyczny i bardzo używalny

### Co budujesz

Lokalną aplikację CLI albo TUI do przechowywania snippetów kodu z tagami, wyszukiwaniem i eksportem.

### Co powinno się tam znaleźć

- SQLite
- `dataclass`
- pełnotekstowe wyszukiwanie
- import / export
- walidacja danych
- testy

### Co robi różnicę

- kolorowy interfejs TUI,
- ranking snippetów po użyciu,
- podpowiedzi podobnych snippetów.

## 3. Analizator logów produkcyjnych

**Poziom:** średni

**Efekt wow:** wygląda bardzo profesjonalnie

### Co budujesz

Narzędzie, które czyta duże logi aplikacyjne i generuje raport:

- top błędy,
- najczęstsze endpointy,
- czasy odpowiedzi,
- podejrzane IP,
- rozkład statusów HTTP.

### Co powinno się tam znaleźć

- streaming plików zamiast ładowania wszystkiego do pamięci
- `re`
- `collections`
- eksport do CSV / JSON
- benchmark prostych podejść

### Co robi różnicę

- wykrywanie anomalii,
- grupowanie podobnych tracebacków,
- ranking najdroższych błędów.

## 4. Lokalna wyszukiwarka dokumentów

**Poziom:** średni

**Efekt wow:** bardzo fajny projekt portfolio

### Co budujesz

Silnik indeksujący lokalne pliki tekstowe, Markdown i notatki, a potem wyszukujący po słowach kluczowych.

### Co powinno się tam znaleźć

- indeksowanie dokumentów
- tokenizacja
- ranking wyników
- CLI albo proste API
- cache

### Co robi różnicę

- podświetlanie dopasowanych fragmentów,
- ranking po trafności,
- przyrostowa aktualizacja indeksu.

## 5. System backupów z deduplikacją

**Poziom:** średni

**Efekt wow:** wygląda na dojrzałe narzędzie

### Co budujesz

Program wykonujący backup folderów z wersjonowaniem, hashami i wykrywaniem duplikatów.

### Co powinno się tam znaleźć

- `hashlib`
- metadane backupu
- przywracanie wersji
- porównywanie snapshotów
- testy integracyjne

### Co robi różnicę

- backup przyrostowy,
- wykrywanie uszkodzonych plików,
- czytelny raport zmian między snapshotami.

## 6. Mini silnik reguł biznesowych

**Poziom:** średni

**Efekt wow:** pokazuje myślenie architektoniczne

### Co budujesz

Silnik, do którego wczytujesz reguły typu:

- jeśli klient premium i koszyk > 500 zł, daj rabat,
- jeśli kraj spoza UE, dołóż inną politykę podatkową,
- jeśli użytkownik ma ryzyko fraudu, zablokuj operację.

### Co powinno się tam znaleźć

- parser konfiguracji
- strategia / wzorce projektowe
- walidacja reguł
- testy przypadków brzegowych

### Co robi różnicę

- DSL w YAML / JSON,
- czytelny engine decyzji,
- ślad wykonania: która reguła zadziałała i dlaczego.

## 7. Asynchroniczny crawler stron

**Poziom:** średni / wyższy

**Efekt wow:** mocno pachnie realnym backendem

### Co budujesz

Crawler, który pobiera setki stron, parsuje linki i buduje mapę witryny.

### Co powinno się tam znaleźć

- `asyncio`
- `httpx`
- limity współbieżności
- retry
- timeouty
- parser HTML

### Co robi różnicę

- rate limiting per domena,
- zapis grafu linków,
- wykrywanie broken links i redirect loops.

## 8. API do zarządzania zadaniami z auth i rolami

**Poziom:** średni / wyższy

**Efekt wow:** klasyk, ale w dobrej jakości nadal robi robotę

### Co budujesz

Backend z:

- użytkownikami,
- projektami,
- zadaniami,
- komentarzami,
- rolami,
- logiem zmian.

### Co powinno się tam znaleźć

- FastAPI albo Django
- JWT albo sesje
- baza danych
- migracje
- testy API
- walidacja wejścia

### Co robi różnicę

- soft delete,
- audit log,
- paginacja,
- filtrowanie,
- sensowna struktura folderów i warstw.

## 9. Silnik rekomendacji filmów / książek

**Poziom:** średni / wyższy

**Efekt wow:** pokazuje, że umiesz zrobić coś „sprytnego”

### Co budujesz

System rekomendujący na podstawie:

- tagów,
- ocen,
- historii użytkownika,
- podobieństwa treści.

### Co powinno się tam znaleźć

- model danych
- ranking
- scoring
- testowanie logiki
- eksport wyników

### Co robi różnicę

- porównanie kilku strategii rekomendacji,
- explainability: czemu system coś polecił,
- tryb offline do ewaluacji skuteczności.

## 10. Interpreter mini języka

**Poziom:** wyższy

**Efekt wow:** bardzo mocny sygnał „ten ktoś umie myśleć”

### Co budujesz

Mały język z własną składnią, np.:

- zmienne,
- warunki,
- pętle,
- funkcje,
- proste wyrażenia.

### Co powinno się tam znaleźć

- tokenizer
- parser
- AST
- wykonanie programu
- sensowne błędy składni

### Co robi różnicę

- raportowanie błędów z numerem linii,
- debug mode,
- mini REPL.

## 11. System kolejkowania zadań w stylu mini Celery

**Poziom:** wyższy

**Efekt wow:** bardzo mocny backendowy klimat

### Co budujesz

Mini system background jobs:

- producent wrzuca zadanie,
- worker odbiera zadanie,
- status zadania jest śledzony,
- można robić retry i harmonogram.

### Co powinno się tam znaleźć

- kolejka
- worker
- statusy
- retry
- idempotencja
- timeouty

### Co robi różnicę

- dead-letter queue,
- exponential backoff,
- monitoring zadań,
- dashboard tekstowy albo webowy.

## 12. Platforma do analizy giełdowej / kryptowalutowej

**Poziom:** wyższy

**Efekt wow:** bardzo widowiskowe demo

### Co budujesz

System, który:

- pobiera dane rynkowe,
- liczy wskaźniki,
- generuje alerty,
- zapisuje historię sygnałów.

### Co powinno się tam znaleźć

- async pobieranie danych
- harmonogram
- przechowywanie historyczne
- wykresy albo dashboard
- testy logiki sygnałów

### Co robi różnicę

- symulacja strategii,
- porównanie wyników różnych wskaźników,
- alerty mailowe / webhooki.

## 13. Zaawansowany agregator ofert pracy

**Poziom:** wyższy

**Efekt wow:** bardzo praktyczny i „produkcyjny”

### Co budujesz

System, który:

- pobiera oferty z wielu źródeł,
- normalizuje dane,
- usuwa duplikaty,
- klasyfikuje stack technologiczny,
- umożliwia filtrowanie.

### Co powinno się tam znaleźć

- crawling
- parsowanie
- normalizacja
- deduplikacja
- API albo panel webowy

### Co robi różnicę

- scoring jakości oferty,
- wykrywanie widełek płacowych,
- analiza trendów rynku.

## 14. Silnik workflow / approval flow

**Poziom:** wyższy

**Efekt wow:** wygląda na projekt z poważnej firmy

### Co budujesz

Silnik procesów typu:

- wniosek urlopowy,
- akceptacja wydatku,
- akceptacja publikacji,
- wieloetapowy onboarding.

### Co powinno się tam znaleźć

- model stanu
- przejścia
- walidacja
- historia decyzji
- role i uprawnienia

### Co robi różnicę

- konfiguracja procesu z pliku,
- diagram stanu,
- zasady dynamiczne zależne od danych.

## 15. Distributed rate limiter i abuse detector

**Poziom:** wyższy

**Efekt wow:** bardzo techniczny i bardzo mocny

### Co budujesz

Moduł chroniący API przed nadużyciami:

- limity per user,
- limity per IP,
- burst control,
- prosta detekcja podejrzanych wzorców.

### Co powinno się tam znaleźć

- Redis
- okna czasowe
- algorytmy limitowania
- metryki
- testy obciążeniowe

### Co robi różnicę

- porównanie token bucket vs sliding window,
- osobne polityki dla endpointów,
- analiza false positives.

## 16. Własny ORM-light

**Poziom:** wyższy / trudny

**Efekt wow:** bardzo mocny strzał na zrozumienie wnętrza frameworków

### Co budujesz

Lekki ORM z:

- modelami,
- polami,
- walidacją,
- zapisem do SQLite,
- prostymi zapytaniami.

### Co powinno się tam znaleźć

- deskryptory
- metaklasy albo `__init_subclass__`
- mapowanie model -> tabela
- serializacja
- testy

### Co robi różnicę

- query builder,
- lazy loading relacji,
- migracje w uproszczonej formie.

## 17. Własny system pluginów

**Poziom:** trudny

**Efekt wow:** bardzo inżynierski projekt

### Co budujesz

Aplikację, która ładuje pluginy z osobnych modułów i pozwala im rozszerzać zachowanie systemu.

### Co powinno się tam znaleźć

- dynamiczny import
- rejestr pluginów
- kontrakty interfejsów
- izolacja błędów
- wersjonowanie pluginów

### Co robi różnicę

- sandbox polityk pluginów,
- hot reload pluginów,
- capability model.

## 18. Silnik event-driven dla e-commerce

**Poziom:** trudny

**Efekt wow:** brzmi i wygląda jak prawdziwy system produkcyjny

### Co budujesz

Moduł, gdzie zdarzenia typu:

- `order_created`,
- `payment_confirmed`,
- `shipment_sent`

uruchamiają kolejne reakcje systemu.

### Co powinno się tam znaleźć

- event bus
- handler-y
- idempotencja
- retry
- log zdarzeń

### Co robi różnicę

- outbox pattern,
- obsługa duplicate events,
- symulacja awarii konsumentów.

## 19. Własny mini framework webowy

**Poziom:** trudny

**Efekt wow:** bardzo mocne portfolio

### Co budujesz

Mały framework obsługujący:

- routing,
- request / response,
- middleware,
- dependency injection,
- walidację danych.

### Co powinno się tam znaleźć

- WSGI albo ASGI
- router
- middleware chain
- obsługa wyjątków
- testy

### Co robi różnicę

- auto docs dla endpointów,
- system zależności,
- plugin middleware.

## 20. Silnik wykrywania fraudów w transakcjach

**Poziom:** trudny

**Efekt wow:** bardzo „seniorowy” temat

### Co budujesz

System punktujący ryzyko transakcji na podstawie:

- kwoty,
- geolokalizacji,
- historii użytkownika,
- liczby prób,
- nietypowych wzorców.

### Co powinno się tam znaleźć

- rule engine
- scoring
- explainability
- alerty
- audyt decyzji

### Co robi różnicę

- osobne profile ryzyka,
- symulacja danych wejściowych,
- analiza precision / recall dla progów.

## 21. Platforma do uruchamiania kodu użytkownika

**Poziom:** bardzo trudny

**Efekt wow:** ogromny

### Co budujesz

System podobny do judge albo sandbox runner:

- użytkownik wrzuca kod,
- system uruchamia go w izolacji,
- zbiera output,
- ogranicza czas i zasoby,
- raportuje wynik.

### Co powinno się tam znaleźć

- izolacja procesu
- limity czasu
- limity pamięci
- logowanie
- bezpieczne uruchamianie

### Co robi różnicę

- kolejka zadań,
- porównywanie outputu do expected output,
- profile wykonania,
- wersje środowiska uruchomieniowego.

## 22. Replikowany system cache / key-value store

**Poziom:** bardzo trudny

**Efekt wow:** bardzo techniczny, bardzo imponujący

### Co budujesz

Własny magazyn klucz-wartość z:

- TTL,
- persystencją,
- prostą replikacją,
- snapshotami,
- polityką usuwania danych.

### Co powinno się tam znaleźć

- sockety albo API
- serializacja
- log zmian
- TTL cleanup
- testy wydajnościowe

### Co robi różnicę

- leader / follower,
- recovery po restarcie,
- porównanie polityk eviction.

## 23. Silnik orkiestracji zadań typu mini Airflow

**Poziom:** bardzo trudny

**Efekt wow:** ekstremalnie mocny

### Co budujesz

System, w którym definiujesz DAG zadań:

- pobierz dane,
- przetwórz,
- waliduj,
- zapisz,
- wyślij raport.

### Co powinno się tam znaleźć

- graf zależności
- scheduler
- retry
- statusy zadań
- logi wykonania

### Co robi różnicę

- widok drzewa zależności,
- cache wyników kroków,
- wykrywanie cykli,
- backfill historycznych uruchomień.

## 24. System multi-tenant SaaS

**Poziom:** bardzo trudny

**Efekt wow:** „to już wygląda jak prawdziwy produkt”

### Co budujesz

Aplikację webową, gdzie wielu klientów korzysta z jednego systemu, ale ich dane są izolowane.

### Co powinno się tam znaleźć

- auth
- role
- tenant isolation
- billing hooks
- audit log
- observability

### Co robi różnicę

- osobne polityki limitów per tenant,
- onboarding klienta,
- feature flags,
- bezpieczne granice danych.

## 25. Platforma do analizy i monitorowania mikroserwisów

**Poziom:** ekstremalny

**Efekt wow:** bardzo duży szok

### Co budujesz

System zbierający:

- logi,
- metryki,
- trace-y,
- health status,
- alerty

z kilku usług.

### Co powinno się tam znaleźć

- collector
- parser zdarzeń
- agregacja
- dashboard
- reguły alarmowe

### Co robi różnicę

- korelacja błędów między usługami,
- analiza wpływu awarii,
- wykrywanie anomalii w czasie rzeczywistym.

## 26. Pythonowy „operating core” dla automatyzacji firmy

**Poziom:** ekstremalny

**Efekt wow:** absolutny potwór

### Co budujesz

Jedno centrum automatyzacji, które:

- odbiera zdarzenia z API,
- uruchamia workflow,
- zleca background jobs,
- zapisuje stan,
- monitoruje wykonanie,
- wysyła powiadomienia,
- audytuje każdą decyzję.

### Co powinno się tam znaleźć

- web API
- worker queue
- scheduler
- event bus
- baza danych
- cache
- auth
- observability
- testy wielowarstwowe

### Co robi różnicę

- bardzo czyste granice domen,
- retry i idempotencja wszędzie gdzie trzeba,
- dobre logi i metryki,
- deployment lokalny przez Dockera,
- projekt gotowy do pokazania jako „mój największy system”.

## Jak wybierać projekty

Jeśli chcesz budować potężne portfolio, najlepsza strategia jest taka:

1. zrób 2 mniejsze projekty bardzo porządnie,
2. zrób 2 średnie projekty z testami i dobrą strukturą,
3. zrób 1 bardzo duży projekt, który będzie Twoim pokazowym potworem.

Najlepsze projekty na efekt portfolio z tej listy:

- **7. Asynchroniczny crawler stron**
- **8. API do zarządzania zadaniami z auth i rolami**
- **11. System kolejkowania zadań w stylu mini Celery**
- **16. Własny ORM-light**
- **19. Własny mini framework webowy**
- **23. Silnik orkiestracji zadań typu mini Airflow**
- **26. Pythonowy „operating core” dla automatyzacji firmy**

## Najmocniejsze zestawy projektowe

### Zestaw „backend kozak”

- 8
- 11
- 18
- 24

### Zestaw „Python internals kozak”

- 10
- 16
- 17
- 19

### Zestaw „system design kozak”

- 15
- 18
- 23
- 26

## Ostatnia ważna rzecz

Projekt robi wrażenie nie tylko tematem.

Projekt robi wrażenie wtedy, gdy ma:

- dobrą strukturę,
- README z architekturą,
- testy,
- sensowne logowanie,
- przykładowe dane,
- screenshoty albo diagramy,
- i kilka decyzji technicznych dobrze uzasadnionych.

Jeśli dwa projekty robią to samo, ale jeden ma:

- chaos,
- zero testów,
- brak opisu,
- brak uzasadnienia architektury,

a drugi ma:

- porządek,
- dobrą warstwowość,
- przykłady użycia,
- testy,
- edge case’y,

to właśnie ten drugi wygląda jak projekt napisany przez kozaka.

## Ścieżki kariery i projekty pod konkretny kierunek

Ta sekcja jest po to, żebyś nie wybierał projektów losowo.

Jeśli celujesz w konkretny kierunek, to nie każdy projekt daje taki sam zwrot.

Poniżej masz gotowe ścieżki.

## 1. Web Developer / Backend Developer

Jeśli chcesz iść w backend, API, aplikacje webowe i systemy serwerowe, to najmocniej działają projekty pokazujące:

- projektowanie API,
- bazę danych,
- auth,
- kolejki,
- skalowanie,
- logikę biznesową,
- architekturę warstwową.

### Najlepsze projekty

- **8. API do zarządzania zadaniami z auth i rolami**
- **11. System kolejkowania zadań w stylu mini Celery**
- **14. Silnik workflow / approval flow**
- **18. Silnik event-driven dla e-commerce**
- **24. System multi-tenant SaaS**
- **26. Pythonowy „operating core” dla automatyzacji firmy**

### Najlepsza kolejność

1. 8
2. 11
3. 14
4. 18
5. 24
6. 26

### Co robi największe wrażenie

- czysta architektura,
- porządny model danych,
- role i uprawnienia,
- kolejki i retry,
- audit log,
- sensowny deployment lokalny.

## 2. Data Scientist / Data Analyst

Jeśli chcesz iść w dane, analitykę i przetwarzanie większych zbiorów informacji, to projekty powinny pokazywać:

- czyszczenie danych,
- agregacje,
- scoring,
- raportowanie,
- automatyzację pipeline’u,
- sensowne przedstawianie wyników.

### Najlepsze projekty

- **3. Analizator logów produkcyjnych**
- **4. Lokalna wyszukiwarka dokumentów**
- **9. Silnik rekomendacji filmów / książek**
- **12. Platforma do analizy giełdowej / kryptowalutowej**
- **13. Zaawansowany agregator ofert pracy**
- **23. Silnik orkiestracji zadań typu mini Airflow**

### Najlepsza kolejność

1. 3
2. 4
3. 9
4. 13
5. 12
6. 23

### Co robi największe wrażenie

- dobre pipeline’y danych,
- mierzenie jakości wyników,
- raporty i dashboardy,
- czytelne wnioski,
- analiza trendów zamiast tylko zbierania danych.

## 3. Machine Learning Engineer / Applied ML

Jeśli celujesz bardziej w praktyczne ML niż czystą analizę danych, to projekt musi pokazać coś więcej niż notebook.

Powinien pokazywać:

- przygotowanie danych,
- feature thinking,
- scoring,
- ewaluację,
- wersjonowanie podejścia,
- sensowny interfejs wokół modelu albo logiki decyzyjnej.

### Najlepsze projekty

- **9. Silnik rekomendacji filmów / książek**
- **12. Platforma do analizy giełdowej / kryptowalutowej**
- **20. Silnik wykrywania fraudów w transakcjach**
- **25. Platforma do analizy i monitorowania mikroserwisów**
- **26. Pythonowy „operating core” dla automatyzacji firmy**

### Najlepsza kolejność

1. 9
2. 12
3. 20
4. 25
5. 26

### Co robi największe wrażenie

- explainability,
- sensowne metryki,
- porównanie kilku podejść,
- myślenie o false positives i false negatives,
- osadzenie logiki modelowej w prawdziwym systemie.

## 4. Cybersecurity / Security Engineer

Jeśli chcesz iść w bezpieczeństwo, to projekty powinny pokazywać:

- myślenie o nadużyciach,
- kontrolę uprawnień,
- bezpieczne wykonanie,
- analizę logów i zdarzeń,
- wykrywanie anomalii,
- świadomość architektury obronnej.

### Najlepsze projekty

- **3. Analizator logów produkcyjnych**
- **15. Distributed rate limiter i abuse detector**
- **20. Silnik wykrywania fraudów w transakcjach**
- **21. Platforma do uruchamiania kodu użytkownika**
- **25. Platforma do analizy i monitorowania mikroserwisów**
- **26. Pythonowy „operating core” dla automatyzacji firmy**

### Najlepsza kolejność

1. 3
2. 15
3. 20
4. 21
5. 25
6. 26

### Co robi największe wrażenie

- threat thinking,
- logi bezpieczeństwa,
- limity i ochrona przed abuse,
- izolacja wykonania,
- audyt decyzji,
- analiza wzorców podejrzanego ruchu.

## 5. Automation Engineer / Python Developer do narzędzi

Jeśli chcesz robić automatyzacje, narzędzia wewnętrzne i systemy wspierające pracę firm, to największą wartość mają projekty pokazujące:

- CLI,
- workflow,
- przetwarzanie plików,
- orkiestrację,
- background jobs,
- integrację kilku komponentów.

### Najlepsze projekty

- **1. CLI do inteligentnego porządkowania plików**
- **5. System backupów z deduplikacją**
- **6. Mini silnik reguł biznesowych**
- **11. System kolejkowania zadań w stylu mini Celery**
- **14. Silnik workflow / approval flow**
- **26. Pythonowy „operating core” dla automatyzacji firmy**

### Najlepsza kolejność

1. 1
2. 5
3. 6
4. 11
5. 14
6. 26

### Co robi największe wrażenie

- niezawodność,
- dobra obsługa błędów,
- możliwość wznowienia pracy,
- logowanie,
- konfiguracja z plików,
- praktyczność.

## 6. Software Engineer / Python Generalist

Jeśli chcesz być po prostu bardzo mocnym Python developerem, a nie tylko „kimś od jednego kąta”, to powinieneś mieszać projekty z:

- backendu,
- internals,
- asynchroniczności,
- architektury,
- tooling,
- system designu.

### Najlepsze projekty

- **7. Asynchroniczny crawler stron**
- **8. API do zarządzania zadaniami z auth i rolami**
- **10. Interpreter mini języka**
- **16. Własny ORM-light**
- **19. Własny mini framework webowy**
- **23. Silnik orkiestracji zadań typu mini Airflow**

### Najlepsza kolejność

1. 7
2. 8
3. 10
4. 16
5. 19
6. 23

### Co robi największe wrażenie

- szerokość umiejętności,
- umiejętność projektowania abstrakcji,
- rozumienie wnętrza Pythona,
- testy,
- jakość API i interfejsów.

## 7. Python Internals / Framework Engineer

Jeśli najbardziej jarają Cię wnętrzności języka, frameworki, parsery, pluginy i mechanizmy, to ta ścieżka jest najbardziej „kozacka technicznie”.

### Najlepsze projekty

- **10. Interpreter mini języka**
- **16. Własny ORM-light**
- **17. Własny system pluginów**
- **19. Własny mini framework webowy**
- **22. Replikowany system cache / key-value store**
- **23. Silnik orkiestracji zadań typu mini Airflow**

### Najlepsza kolejność

1. 10
2. 16
3. 17
4. 19
5. 22
6. 23

### Co robi największe wrażenie

- deskryptory,
- metaklasy,
- import system,
- projektowanie runtime,
- scheduler,
- protokoły i kontrakty.

## 8. DevOps / Platform / SRE-minded Python

Jeśli chcesz używać Pythona do budowy narzędzi platformowych, systemów monitorujących i automatyzacji operacyjnej, to warto iść w projekty pokazujące:

- obserwowalność,
- logi i metryki,
- workflow,
- cache,
- retry,
- recovery,
- produkcyjne myślenie o awariach.

### Najlepsze projekty

- **3. Analizator logów produkcyjnych**
- **5. System backupów z deduplikacją**
- **11. System kolejkowania zadań w stylu mini Celery**
- **22. Replikowany system cache / key-value store**
- **25. Platforma do analizy i monitorowania mikroserwisów**
- **26. Pythonowy „operating core” dla automatyzacji firmy**

### Najlepsza kolejność

1. 3
2. 5
3. 11
4. 22
5. 25
6. 26

### Co robi największe wrażenie

- odporność na awarie,
- sensowne logowanie i alerting,
- backup i recovery,
- monitoring,
- myślenie o systemie jako całości.

## Jeśli nie wiesz jeszcze, którą ścieżkę wybrać

Najbezpieczniejszy zestaw na bardzo mocne portfolio ogólne to:

1. **7. Asynchroniczny crawler stron**
2. **8. API do zarządzania zadaniami z auth i rolami**
3. **11. System kolejkowania zadań w stylu mini Celery**
4. **16. Własny ORM-light**
5. **19. Własny mini framework webowy**

To jest zestaw, który daje:

- backend,
- async,
- architekturę,
- internals,
- design,
- efekt wow.
