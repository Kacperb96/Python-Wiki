# Separacja logiki biznesowej w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest logika biznesowa](#czym-jest-logika-biznesowa)
3. [Po co ją separować](#po-co-ją-separować)
4. [Logika biznesowa a framework](#logika-biznesowa-a-framework)
5. [Logika biznesowa a baza danych](#logika-biznesowa-a-baza-danych)
6. [Logika biznesowa a warstwa HTTP](#logika-biznesowa-a-warstwa-http)
7. [Korzyści dla testów](#korzyści-dla-testów)
8. [Typowe błędy początkujących](#typowe-błędy-początkujących)
9. [Praktyczne przykłady](#praktyczne-przykłady)
10. [Dobre praktyki](#dobre-praktyki)
11. [Podsumowanie](#podsumowanie)
12. [Mini ściąga](#mini-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

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

---

## Po co ją separować

Bo gdy logika biznesowa jest rozlana po:

- endpointach,
- zapytaniach SQL,
- callbackach frameworka,

projekt szybko staje się trudny do testowania i rozwijania.

---

## Logika biznesowa a framework

Framework HTTP nie powinien być centrum twojej domeny.

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

---

## Korzyści dla testów

To ogromny plus.

Logikę biznesową można testować bez:

- serwera HTTP,
- prawdziwej bazy,
- całej infrastruktury.

---

## Typowe błędy początkujących

- cała logika w endpointach,
- logika biznesowa w modelach ORM bez planu,
- brak osobnej warstwy lub choćby modułu domenowego,
- mieszanie walidacji HTTP z regułami biznesowymi.

---

## Praktyczne przykłady

### Zły kierunek

Endpoint:

- waliduje payload,
- sprawdza warunki biznesowe,
- odpytuje bazę,
- wysyła mail,
- buduje odpowiedź.

### Lepszy kierunek

- endpoint odbiera request,
- serwis domenowy podejmuje decyzję,
- repozytorium zapisuje dane,
- infrastruktura wysyła mail.

---

## Dobre praktyki

- utrzymuj logikę biznesową w osobnych funkcjach, serwisach lub modułach,
- nie przyklejaj domeny do frameworka,
- oddzielaj warstwę danych od decyzji biznesowych,
- testuj reguły biznesowe niezależnie od transportu i infrastruktury.

---

## Podsumowanie

Separacja logiki biznesowej to jedna z najcenniejszych praktyk architektonicznych w backendzie Python.

Im lepiej to zrobisz, tym mniej projekt będzie zależał od przypadkowej struktury frameworka.

---

## Mini ściąga

Najważniejsze:

- logika biznesowa to reguły domeny,
- nie powinna być rozlana po endpointach i SQL,
- jej separacja poprawia testowalność i utrzymanie.

---

## Ćwiczenia

1. Podaj przykład logiki biznesowej.
2. Wyjaśnij, czemu nie warto trzymać jej całej w endpointach.
3. Wyjaśnij, czemu oddzielenie od bazy pomaga.
4. Wskaż różnicę między walidacją requestu a regułą biznesową.
5. Wyjaśnij, czemu taka separacja pomaga testować.

---

## Przykładowe rozwiązania

### 1. Przykład

Reguła mówiąca, że rabat VIP działa tylko dla aktywnego klienta.

### 2. Czemu nie w endpointach

Bo wtedy kod domenowy jest przyklejony do HTTP i trudniej go rozwijać oraz testować.

### 3. Oddzielenie od bazy

Bo logikę można uruchamiać i testować bez całej infrastruktury danych.

### 4. Różnica

Walidacja requestu sprawdza format i obecność danych, a reguła biznesowa sprawdza zasady domeny.

### 5. Testowanie

Bo nie trzeba podnosić całego stosu HTTP i bazy do sprawdzenia samych reguł.
