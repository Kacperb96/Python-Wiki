# 13. Web i API

To jest dział przejścia z ogólnego Pythona do praktycznego backendu.

Tutaj zaczynasz pracować z rzeczami, które w realnych projektach pojawiają się bardzo często:

- HTTP,
- REST,
- JSON,
- walidacja danych wejściowych,
- budowanie endpointów,
- autoryzacja,
- obsługa błędów,
- testowanie kontraktu API.

To bardzo ważny moment w nauce, bo przestajesz pisać tylko kod lokalny, a zaczynasz budować interfejs, z którego korzystają inne systemy, frontend albo zewnętrzni użytkownicy.

---

## Co powinieneś rozumieć po tym dziale

Po przerobieniu całego folderu powinieneś rozumieć:

- czym jest HTTP i jak wygląda komunikacja klient-serwer,
- czym są request, response, metody HTTP i status codes,
- co znaczy REST w praktyce,
- do czego służy `Pydantic`,
- jak działa FastAPI,
- jak organizować routing,
- po co FastAPI ma dependency injection,
- jak modelować autoryzację i uprawnienia,
- jak projektować sensowną obsługę błędów,
- jak testować API.

---

## Dlaczego ten dział jest ważny

W praktyce bardzo dużo pracy backendowej polega na tym, że:

- odbierasz żądanie,
- walidujesz dane,
- uruchamiasz logikę biznesową,
- zwracasz poprawną odpowiedź HTTP,
- obsługujesz błędy i bezpieczeństwo.

Jeśli ten dział jest słaby, to później framework wygląda jak magia.

Jeśli ten dział jest mocny, to framework staje się po prostu narzędziem do wyrażenia znanych zasad.

---

## Jak czytać ten dział

Najlepiej iść dokładnie po kolei:

1. [01-http-rest-podstawy-python.md](/home/kacper/Desktop/Python_naprawiony/13.%20Web%20i%20API/01-http-rest-podstawy-python.md)
2. [02-pydantic-python.md](/home/kacper/Desktop/Python_naprawiony/13.%20Web%20i%20API/02-pydantic-python.md)
3. [03-fastapi-podstawy-python.md](/home/kacper/Desktop/Python_naprawiony/13.%20Web%20i%20API/03-fastapi-podstawy-python.md)
4. [04-fastapi-routing-python.md](/home/kacper/Desktop/Python_naprawiony/13.%20Web%20i%20API/04-fastapi-routing-python.md)
5. [05-fastapi-dependency-injection-python.md](/home/kacper/Desktop/Python_naprawiony/13.%20Web%20i%20API/05-fastapi-dependency-injection-python.md)
6. [06-autoryzacja-api-python.md](/home/kacper/Desktop/Python_naprawiony/13.%20Web%20i%20API/06-autoryzacja-api-python.md)
7. [07-obsluga-bledow-api-python.md](/home/kacper/Desktop/Python_naprawiony/13.%20Web%20i%20API/07-obsluga-bledow-api-python.md)
8. [08-testowanie-api-python.md](/home/kacper/Desktop/Python_naprawiony/13.%20Web%20i%20API/08-testowanie-api-python.md)

Ta kolejność ma sens, bo:

- najpierw rozumiesz sam protokół,
- potem walidację danych,
- potem podstawy frameworka,
- potem organizację większego API,
- a dopiero później bezpieczeństwo, błędy i testy.

---

## Jak pracować z tym działem

Najlepszy sposób nauki:

1. przeczytaj jeden plik,
2. uruchom pokazane przykłady,
3. przewiduj status code i JSON przed uruchomieniem,
4. napisz własny wariant endpointu,
5. dopiero potem przejdź do ćwiczeń.

Sam backend bardzo łatwo wygląda na zrozumiały "na sucho", ale prawdziwe zrozumienie pojawia się wtedy, gdy sam zbudujesz kilka endpointów i zobaczysz realne requesty oraz odpowiedzi.

---

## Na co szczególnie uważać

Najczęstsze pułapki:

- traktowanie HTTP jako zbioru przypadkowych statusów,
- mylenie `401` i `403`,
- projektowanie endpointów bez sensownej semantyki REST,
- wrzucanie całej logiki do endpointów,
- brak walidacji danych wejściowych,
- niespójny format błędów,
- brak testów scenariuszy negatywnych.

---

## Po czym poznać, że temat zaczyna siedzieć

Dobry znak, jeśli potrafisz:

- rozpisać sensowne endpointy dla zasobu,
- dobrać właściwą metodę HTTP i status code,
- zaprojektować model wejściowy i wyjściowy,
- napisać prosty endpoint w FastAPI,
- wydzielić router,
- użyć zależności `Depends`,
- wyjaśnić podstawowy model autoryzacji,
- zaprojektować spójny format błędów,
- napisać test dla endpointu z przypadkiem poprawnym i błędnym.

---

## Co ten dział daje w praktyce

Po opanowaniu tego folderu będziesz dużo lepiej przygotowany do:

- pisania backendów,
- czytania projektów FastAPI,
- pracy z frontendem,
- integracji z zewnętrznymi API,
- rozwijania bardziej realnych aplikacji.

To jest dział, który bardzo wyraźnie zbliża naukę Pythona do pracy projektowej.

---

## Ćwiczenia

Do tego działu masz też [ZESTAW-CWICZEN.md](/home/kacper/Desktop/Python_naprawiony/13.%20Web%20i%20API/ZESTAW-CWICZEN.md).

Najlepiej:

- najpierw zrobić HTTP i `Pydantic`,
- potem podstawy FastAPI,
- potem routing i DI,
- na końcu autoryzację, błędy i testy API.

---

## Co dalej

Po tym dziale naturalny następny krok to:

- [14. Bazy danych](/home/kacper/Desktop/Python_naprawiony/14.%20Bazy%20danych)
- a potem [15. Architektura i jakość kodu](/home/kacper/Desktop/Python_naprawiony/15.%20Architektura%20i%20jako%C5%9B%C4%87%20kodu)

Bo właśnie tam backend zaczyna łączyć HTTP z trwałością danych i lepszą strukturą aplikacji.
