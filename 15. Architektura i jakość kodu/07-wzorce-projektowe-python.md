# Wzorce projektowe w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co znać wzorce projektowe](#po-co-znać-wzorce-projektowe)
3. [Wzorzec to narzędzie, nie cel](#wzorzec-to-narzędzie-nie-cel)
4. [Factory](#factory)
5. [Strategy](#strategy)
6. [Adapter](#adapter)
7. [Repository](#repository)
8. [Observer i callbacki](#observer-i-callbacki)
9. [Python a klasyczne wzorce](#python-a-klasyczne-wzorce)
10. [Typowe błędy początkujących](#typowe-błędy-początkujących)
11. [Praktyczne przykłady](#praktyczne-przykłady)
12. [Dobre praktyki](#dobre-praktyki)
13. [Podsumowanie](#podsumowanie)
14. [Mini ściąga](#mini-ściąga)
15. [Ćwiczenia](#ćwiczenia)
16. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Wzorce projektowe to powtarzalne sposoby rozwiązywania typowych problemów projektowych.

Nie są gotowym kodem do skopiowania, tylko sposobem myślenia o strukturze rozwiązania.

---

## Po co znać wzorce projektowe

Bo pomagają:

- szybciej rozpoznawać typ problemu,
- porządkować architekturę,
- rozmawiać o kodzie wspólnym językiem,
- unikać przypadkowego chaosu w projekcie.

---

## Wzorzec to narzędzie, nie cel

To bardzo ważna zasada.

Nie chodzi o to, żeby "wcisnąć wzorzec" wszędzie.

Chodzi o to, żeby użyć go wtedy, gdy realnie upraszcza projekt.

---

## Factory

Factory pomaga oddzielić tworzenie obiektów od miejsca, które ich używa.

To przydatne, gdy sposób tworzenia zależy od:

- konfiguracji,
- typu wejścia,
- środowiska,
- konkretnej implementacji.

---

## Strategy

Strategy pozwala podmieniać algorytm lub zachowanie bez rozbijania wszystkiego wielkimi `if`-ami.

To bardzo praktyczne, gdy masz kilka wariantów tej samej operacji.

---

## Adapter

Adapter przydaje się, gdy chcesz dopasować jeden interfejs do drugiego.

Na przykład:

- stara biblioteka zwraca dane w innym formacie,
- twój kod oczekuje nowego, spójnego API.

---

## Repository

Repository porządkuje dostęp do danych.

To wzorzec, który już pojawił się w warstwie danych i jest bardzo praktyczny w backendzie Python.

---

## Observer i callbacki

W Pythonie część klasycznych wzorców bywa realizowana prościej przez:

- callbacki,
- eventy,
- hooki,
- subskrypcje.

Nie zawsze trzeba budować ciężką obiektową konstrukcję.

---

## Python a klasyczne wzorce

Python jest elastyczny, więc niektóre wzorce z książek OO wyglądają tu lżej.

Czasem:

- funkcja wystarczy zamiast klasy,
- prosty obiekt wystarczy zamiast rozbudowanej hierarchii,
- kompozycja jest lepsza niż dziedziczenie.

---

## Typowe błędy początkujących

- traktowanie wzorców jak trofeów,
- kopiowanie wzorców bez zrozumienia problemu,
- budowanie niepotrzebnej ceremonii,
- ignorowanie prostszych, pythonowych rozwiązań.

---

## Praktyczne przykłady

### Strategy

Masz kilka sposobów naliczania rabatu:

- rabat dla nowego klienta,
- rabat dla VIP,
- rabat sezonowy.

To naturalny kandydat na Strategy.

### Factory

W zależności od typu konfiguracji tworzysz inny klient do wysyłki powiadomień.

---

## Dobre praktyki

- używaj wzorców wtedy, gdy rozwiązują realny problem,
- preferuj prostotę nad ceremonialność,
- dopasuj wzorzec do stylu Pythona,
- traktuj wzorce jako język projektowy, nie kolekcję obowiązkowych dekoracji.

---

## Podsumowanie

Wzorce projektowe są bardzo przydatne, ale ich siła leży w dopasowaniu do kontekstu.

Najlepszy wzorzec to taki, który upraszcza system, a nie robi z niego łamigłówkę.

---

## Mini ściąga

Najważniejsze:

- `Factory` porządkuje tworzenie obiektów,
- `Strategy` podmienia zachowanie,
- `Adapter` dopasowuje interfejsy,
- `Repository` porządkuje dostęp do danych.

---

## Ćwiczenia

1. Wyjaśnij, po co znać wzorce projektowe.
2. Podaj przykład problemu dla `Strategy`.
3. Podaj przykład problemu dla `Factory`.
4. Wyjaśnij, czym jest `Adapter`.
5. Wyjaśnij, czemu wzorzec nie powinien być celem samym w sobie.

---

## Przykładowe rozwiązania

### 1. Po co wzorce

Żeby szybciej rozpoznawać typowe problemy projektowe i organizować kod sensownie.

### 2. `Strategy`

Kilka różnych algorytmów naliczania ceny końcowej.

### 3. `Factory`

Tworzenie różnych implementacji klienta zależnie od konfiguracji.

### 4. `Adapter`

To warstwa dopasowująca jedno API do drugiego.

### 5. Czemu nie cel

Bo wzorzec ma pomagać, a nie komplikować projekt dla samej formy.
