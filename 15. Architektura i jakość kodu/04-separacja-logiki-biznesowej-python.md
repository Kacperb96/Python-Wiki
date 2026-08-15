# Separacja logiki biznesowej w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest logika biznesowa](#czym-jest-logika-biznesowa)
3. [Po co ją separować](#po-co-ją-separować)
4. [Logika biznesowa a framework](#logika-biznesowa-a-framework)
5. [Logika biznesowa a baza danych](#logika-biznesowa-a-baza-danych)
6. [Logika biznesowa a warstwa HTTP](#logika-biznesowa-a-warstwa-http)
7. [Korzyści dla testów](#korzyści-dla-testów)
8. [Przykład mentalny](#przykład-mentalny)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczna ściąga](#praktyczna-ściąga)
11. [Ćwiczenia](#ćwiczenia)
12. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

Jedna z najważniejszych rzeczy w większym projekcie to umiejętność oddzielenia tego, "jak aplikacja działa biznesowo", od tego, "jak rozmawia z frameworkiem, bazą i światem zewnętrznym".

To właśnie separacja logiki biznesowej.

---

## Czym jest logika biznesowa

To reguły i decyzje domenowe.

Na przykład:

- czy zamówienie może zostać złożone,
- jak liczyć rabat,
- kiedy wysłać powiadomienie,
- jakie warunki musi spełnić użytkownik.

To nie są szczegóły HTTP ani szczegóły bazy.

To odpowiedź na pytanie: jak działa świat tego systemu.

---

## Po co ją separować

Bo gdy logika biznesowa jest rozlana po:

- endpointach,
- zapytaniach SQL,
- callbackach frameworka,
- klasach infrastrukturalnych,

projekt szybko staje się trudny do testowania i rozwijania.

---

## Logika biznesowa a framework

Framework HTTP nie powinien być centrum domeny.

Endpoint powinien raczej:

- odebrać request,
- wywołać logikę,
- zwrócić response.

To prostsze i zdrowsze niż wkładanie wszystkiego do dekorowanej funkcji endpointu.

---

## Logika biznesowa a baza danych

Logika biznesowa nie powinna znać wszystkich szczegółów SQL i ORM tam, gdzie nie musi.

Dzięki temu łatwiej:

- testować,
- podmieniać warstwę danych,
- utrzymywać granice odpowiedzialności.

---

## Logika biznesowa a warstwa HTTP

To bardzo częsty błąd.

Jeśli warunki biznesowe są rozpisane wprost w endpointach, potem trudno je wykorzystać:

- w CLI,
- w innym API,
- w testach,
- w kolejce background jobs.

To znak, że logika jest zbyt mocno przyklejona do transportu.

---

## Korzyści dla testów

To ogromny plus.

Logikę biznesową można testować bez:

- serwera HTTP,
- prawdziwej bazy,
- całej infrastruktury.

To zwykle daje testy:

- szybsze,
- prostsze,
- bardziej odporne na zmiany techniczne.

---

## Przykład mentalny

Zły kierunek:

endpoint:

- waliduje payload,
- sprawdza warunki biznesowe,
- odpytuje bazę,
- wysyła mail,
- buduje odpowiedź.

Lepszy kierunek:

- endpoint odbiera request,
- serwis domenowy podejmuje decyzję,
- repozytorium zapisuje dane,
- infrastruktura wysyła mail.

To dużo czytelniejszy podział odpowiedzialności.

---

## Typowe błędy początkujących

- cała logika w endpointach,
- logika biznesowa w modelach ORM bez planu,
- brak osobnej warstwy albo choćby modułu domenowego,
- mieszanie walidacji HTTP z regułami biznesowymi,
- przyklejanie domeny do frameworka.

---

## Praktyczna ściąga

### Logika biznesowa odpowiada na pytania

- czy wolno,
- kiedy,
- jak policzyć,
- jakie są reguły.

### Nie powinna być rozlana po

- endpointach,
- SQL,
- callbackach frameworka.

### Dobra zasada

Oddziel to, co domenowe, od tego, co infrastrukturalne.

---

## Ćwiczenia

1. Wskaż fragment logiki biznesowej w prostym API.
2. Wyjmij ją z endpointu do osobnej funkcji albo serwisu.
3. Opisz, które elementy są domenowe, a które infrastrukturalne.
4. Wyjaśnij, czemu logikę biznesową lepiej testować bez HTTP i bazy.
5. Podaj przykład miejsca, gdzie logika biznesowa została zbyt mocno przyklejona do frameworka.

---

## Najważniejsze do zapamiętania

- Logika biznesowa to reguły domeny.
- Nie powinna być rozlana po endpointach, SQL i infrastrukturze.
- Jej separacja poprawia testowalność, czytelność i możliwość ponownego użycia.
- Im czytelniejsze granice odpowiedzialności, tym zdrowszy projekt.
