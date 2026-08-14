# Dependency Injection w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest dependency injection](#czym-jest-dependency-injection)
3. [Po co stosować DI](#po-co-stosować-di)
4. [Zależności jawne vs ukryte](#zależności-jawne-vs-ukryte)
5. [DI a testowalność](#di-a-testowalność)
6. [DI a luźne powiązania](#di-a-luźne-powiązania)
7. [Jak DI wygląda w Pythonie](#jak-di-wygląda-w-pythonie)
8. [Kiedy nie przesadzać](#kiedy-nie-przesadzać)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczne przykłady](#praktyczne-przykłady)
11. [Dobre praktyki](#dobre-praktyki)
12. [Podsumowanie](#podsumowanie)
13. [Mini ściąga](#mini-ściąga)
14. [Ćwiczenia](#ćwiczenia)
15. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Dependency injection, czyli wstrzykiwanie zależności, to sposób organizacji kodu, w którym potrzebne obiekty są dostarczane z zewnątrz zamiast tworzone "na sztywno" w środku.

To bardzo ważny temat dla testowalności i architektury.

---

## Czym jest dependency injection

Jeśli obiekt potrzebuje:

- repozytorium,
- klienta HTTP,
- loggera,
- konfiguracji,

to może je dostać jako zależności zamiast samemu je tworzyć.

---

## Po co stosować DI

Bo pomaga:

- podmieniać implementacje,
- uprościć testy,
- ograniczyć twarde powiązania,
- czytelniej budować warstwy systemu.

---

## Zależności jawne vs ukryte

Jawna zależność:

- widać ją w konstruktorze lub argumencie funkcji.

Ukryta zależność:

- obiekt sam coś importuje, tworzy lub pobiera globalnie.

Jawne zależności zwykle dużo łatwiej zrozumieć i testować.

---

## DI a testowalność

To jedna z największych zalet.

Zamiast prawdziwej bazy czy klienta API możesz w testach podstawić:

- fake,
- mock,
- stub.

---

## DI a luźne powiązania

Jeśli logika biznesowa zależy od abstrakcji lub prostego kontraktu, a nie od konkretnego szczegółu, system jest mniej kruchy.

To bardzo cenna właściwość większych projektów.

---

## Jak DI wygląda w Pythonie

W Pythonie DI często jest prostsze niż w niektórych innych językach.

Często wystarczy:

- przekazanie obiektu do konstruktora,
- przekazanie funkcji jako argumentu,
- użycie zależności w FastAPI.

Nie zawsze potrzebujesz ciężkiego kontenera DI.

---

## Kiedy nie przesadzać

W małym skrypcie lub bardzo prostym projekcie nadmiar abstrakcji może bardziej przeszkadzać niż pomagać.

DI ma sens tam, gdzie rzeczywiście daje elastyczność i testowalność.

---

## Typowe błędy początkujących

- tworzenie wszystkiego globalnie,
- ukryte zależności wewnątrz metod,
- przesadna abstrakcja w małych projektach,
- mylenie DI z "robieniem wszystkiego przez interfejsy" nawet bez potrzeby.

---

## Praktyczne przykłady

### Zależność repozytorium

Serwis użytkowników nie musi wiedzieć, jak działa baza.

Wystarczy, że dostanie obiekt repozytorium.

### Zależność klienta HTTP

Klasa integracyjna może dostać klienta API z zewnątrz zamiast sama go tworzyć.

---

## Dobre praktyki

- utrzymuj zależności jawne,
- wstrzykuj to, co realnie warto podmieniać,
- nie komplikuj małych projektów nadmiarem warstw,
- używaj DI tam, gdzie poprawia testowalność i czytelność.

---

## Podsumowanie

Dependency injection to jedna z najbardziej praktycznych technik porządkowania kodu.

W Pythonie da się ją stosować lekko i skutecznie, bez niepotrzebnej ciężkości.

---

## Mini ściąga

Najważniejsze:

- zależności warto dostarczać z zewnątrz,
- jawne zależności są czytelniejsze,
- DI poprawia testowalność,
- nie zawsze potrzebujesz rozbudowanego frameworka DI.

---

## Ćwiczenia

1. Wyjaśnij, czym jest dependency injection.
2. Podaj przykład ukrytej zależności.
3. Podaj przykład jawnej zależności.
4. Wyjaśnij, czemu DI poprawia testowalność.
5. Wyjaśnij, czemu nie warto przesadzać z DI w małym skrypcie.

---

## Przykładowe rozwiązania

### 1. DI

To dostarczanie zależności z zewnątrz zamiast tworzenia ich na sztywno w środku obiektu.

### 2. Ukryta zależność

Metoda, która sama tworzy klienta bazy lub API bez pokazania tego w interfejsie.

### 3. Jawna zależność

Repozytorium przekazane do konstruktora serwisu.

### 4. Testowalność

Bo można łatwo podstawić fake lub mock zamiast prawdziwego systemu zewnętrznego.

### 5. Mały skrypt

Bo dodatkowa abstrakcja może tylko obniżyć czytelność bez realnej korzyści.
