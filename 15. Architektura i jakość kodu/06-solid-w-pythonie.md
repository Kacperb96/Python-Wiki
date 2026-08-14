# SOLID w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co znać SOLID](#po-co-znać-solid)
3. [Single Responsibility Principle](#single-responsibility-principle)
4. [Open Closed Principle](#open-closed-principle)
5. [Liskov Substitution Principle](#liskov-substitution-principle)
6. [Interface Segregation Principle](#interface-segregation-principle)
7. [Dependency Inversion Principle](#dependency-inversion-principle)
8. [SOLID a Python](#solid-a-python)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczne przykłady](#praktyczne-przykłady)
11. [Dobre praktyki](#dobre-praktyki)
12. [Podsumowanie](#podsumowanie)
13. [Mini ściąga](#mini-ściąga)
14. [Ćwiczenia](#ćwiczenia)
15. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

SOLID to zestaw zasad projektowania, które pomagają pisać kod łatwiejszy do utrzymania, testowania i rozwijania.

To nie są magiczne reguły, ale bardzo przydatne heurystyki.

---

## Po co znać SOLID

Bo wraz ze wzrostem projektu zaczynają boleć:

- zbyt duże klasy,
- zbyt mocne powiązania,
- trudne testowanie,
- lęk przed zmianą kodu.

SOLID pomaga to ograniczać.

---

## Single Responsibility Principle

Jedna klasa lub moduł powinny mieć jedną główną odpowiedzialność.

Jeśli jeden obiekt:

- liczy,
- zapisuje do bazy,
- wysyła maile,
- formatuje raport,

to zwykle robi za dużo.

---

## Open Closed Principle

Kod powinien być otwarty na rozszerzanie, ale zamknięty na częste przerabianie istniejącego rdzenia.

W praktyce często chodzi o to, by nowe zachowania dodawać przez:

- nowe klasy,
- strategie,
- kompozycję,

a nie przez dokładanie kolejnych `ifów` w jednym miejscu.

---

## Liskov Substitution Principle

Jeśli coś dziedziczy po czymś innym, powinno dać się używać zamiennie bez psucia oczekiwań.

Jeśli podklasa łamie kontrakt klasy bazowej, projekt zaczyna się chwiać.

---

## Interface Segregation Principle

Lepiej mieć mniejsze, sensowne interfejsy niż jeden wielki interfejs robiący wszystko.

W Pythonie często przekłada się to na:

- małe protokoły,
- małe klasy,
- czytelne API metod.

---

## Dependency Inversion Principle

Wyższe warstwy nie powinny być twardo przyklejone do szczegółów niższych warstw.

Na przykład logika biznesowa nie powinna znać bezpośrednio wszystkich szczegółów konkretnej bazy czy frameworka.

---

## SOLID a Python

Python jest elastyczny i dynamiczny, więc SOLID nie wygląda tu zawsze tak samo jak w językach bardziej sztywnych.

W Pythonie ważniejsze od "ceremonii" są:

- sensowny podział odpowiedzialności,
- luźne powiązania,
- czytelność,
- testowalność.

---

## Typowe błędy początkujących

- traktowanie SOLID jak religii,
- przesadne mnożenie abstrakcji,
- brak zrozumienia problemu, który zasada rozwiązuje,
- kopiowanie wzorców z innych języków bez dopasowania do Pythona.

---

## Praktyczne przykłady

### Zła odpowiedzialność

Klasa `UserManager`, która:

- pobiera użytkownika,
- waliduje hasło,
- zapisuje do bazy,
- wysyła mail,
- loguje zdarzenia.

To zwykle znak, że odpowiedzialności są zmieszane.

### Lepszy podział

- serwis użytkowników,
- repozytorium,
- osobna usługa mailowa.

---

## Dobre praktyki

- używaj SOLID jako narzędzia myślenia, nie checklisty,
- upraszczaj powiązania między modułami,
- pilnuj odpowiedzialności klas i funkcji,
- nie buduj abstrakcji wcześniej, niż naprawdę są potrzebne.

---

## Podsumowanie

SOLID jest przydatny, jeśli pomaga pisać prostszy, czytelniejszy i bardziej utrzymywalny kod.

Największa wartość nie leży w skrócie, tylko w jakości decyzji projektowych.

---

## Mini ściąga

Najważniejsze:

- `S` jedna główna odpowiedzialność,
- `O` rozszerzaj bez ciągłego przerabiania rdzenia,
- `L` podtyp nie powinien psuć kontraktu,
- `I` preferuj mniejsze interfejsy,
- `D` wyższe warstwy niech nie zależą twardo od detali.

---

## Ćwiczenia

1. Podaj przykład klasy łamiącej SRP.
2. Wyjaśnij OCP własnymi słowami.
3. Wskaż przykład złego dziedziczenia łamiącego LSP.
4. Wyjaśnij, czemu DIP pomaga testować kod.
5. Wyjaśnij, czemu SOLID w Pythonie nie powinien oznaczać nadmiaru ceremonii.

---

## Przykładowe rozwiązania

### 1. SRP

Klasa, która jednocześnie generuje raport, zapisuje go do pliku i wysyła mail.

### 2. OCP

Nowe zachowanie lepiej dodać przez rozszerzenie niż przez przerabianie wielu starych miejsc.

### 3. LSP

Podklasa, która dziedziczy po bazie, ale przestaje spełniać oczekiwane zachowanie metod bazowych.

### 4. DIP

Bo logikę można testować z podmienionymi zależnościami zamiast z prawdziwą bazą czy API.

### 5. Ceremonia

Bo nadmiar abstrakcji może bardziej zaciemnić kod niż go poprawić.
