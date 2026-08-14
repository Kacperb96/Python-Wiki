# Architektura warstwowa w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest architektura warstwowa](#czym-jest-architektura-warstwowa)
3. [Po co dzielić system na warstwy](#po-co-dzielić-system-na-warstwy)
4. [Typowe warstwy](#typowe-warstwy)
5. [Warstwa HTTP, biznesowa i danych](#warstwa-http-biznesowa-i-danych)
6. [Korzyści dla testowania](#korzyści-dla-testowania)
7. [Korzyści dla utrzymania](#korzyści-dla-utrzymania)
8. [Typowe błędy początkujących](#typowe-błędy-początkujących)
9. [Praktyczne przykłady](#praktyczne-przykłady)
10. [Dobre praktyki](#dobre-praktyki)
11. [Podsumowanie](#podsumowanie)
12. [Mini ściąga](#mini-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Architektura warstwowa to jeden z najprostszych i najbardziej praktycznych sposobów organizacji większego backendu.

Nie jest jedyną słuszną architekturą, ale bardzo często jest dobrym punktem startowym.

---

## Czym jest architektura warstwowa

To podział systemu na warstwy o różnych odpowiedzialnościach.

Najczęściej jedna warstwa:

- odbiera wejście,
- inna wykonuje logikę,
- inna rozmawia z bazą lub infrastrukturą.

---

## Po co dzielić system na warstwy

Bo pomaga:

- zapanować nad złożonością,
- ograniczyć chaos,
- łatwiej testować kod,
- łatwiej wymieniać elementy infrastruktury.

---

## Typowe warstwy

W backendzie Python często pojawiają się:

- warstwa HTTP lub prezentacji,
- warstwa aplikacyjna lub biznesowa,
- warstwa danych lub infrastruktury.

---

## Warstwa HTTP, biznesowa i danych

Warstwa HTTP:

- odbiera request,
- zwraca response.

Warstwa biznesowa:

- realizuje reguły domenowe,
- koordynuje przepływ.

Warstwa danych:

- pobiera i zapisuje dane,
- komunikuje się z bazą.

---

## Korzyści dla testowania

To ogromna zaleta.

Jeśli logika biznesowa nie zależy twardo od frameworka i bazy, da się ją testować szybciej i czyściej.

---

## Korzyści dla utrzymania

Zmiana w jednej warstwie nie musi od razu rozwalać całego systemu.

To daje:

- lepszą modularność,
- mniejszy chaos zmian,
- łatwiejsze code review.

---

## Typowe błędy początkujących

- wrzucanie wszystkiego do endpointów,
- brak rozróżnienia między logiką biznesową a bazą,
- sztuczne mnożenie warstw w bardzo małym projekcie,
- nazwanie katalogów "services" i "utils" bez realnego podziału odpowiedzialności.

---

## Praktyczne przykłady

### Dobry podział

- endpoint `POST /orders`
- serwis `create_order`
- repozytorium `save_order`

### Zły podział

Endpoint, który:

- waliduje,
- liczy,
- odpytuje bazę,
- wysyła mail,
- buduje odpowiedź.

---

## Dobre praktyki

- buduj warstwy wokół odpowiedzialności,
- trzymaj logikę biznesową poza frameworkiem, jeśli to sensowne,
- nie komplikuj małych projektów ponad potrzebę,
- pilnuj, by warstwy miały czytelne granice.

---

## Podsumowanie

Architektura warstwowa to praktyczne narzędzie porządkowania backendu Python.

Najlepiej działa wtedy, gdy rzeczywiście upraszcza projekt, a nie gdy jest tylko modnym hasłem.

---

## Mini ściąga

Najważniejsze:

- warstwa HTTP odbiera i zwraca,
- warstwa biznesowa podejmuje decyzje,
- warstwa danych rozmawia z bazą,
- rozdział poprawia testowalność i utrzymanie.

---

## Ćwiczenia

1. Rozdziel prosty endpoint na trzy warstwy.
2. Wyjaśnij rolę warstwy biznesowej.
3. Wyjaśnij rolę warstwy danych.
4. Wskaż przykład mieszania odpowiedzialności.
5. Wyjaśnij, czemu nie każdy mały projekt potrzebuje pełnej rozbudowanej architektury.

---

## Przykładowe rozwiązania

### 1. Trzy warstwy

- endpoint przyjmuje dane,
- serwis wykonuje logikę,
- repozytorium zapisuje do bazy.

### 2. Warstwa biznesowa

Zawiera reguły i decyzje aplikacji.

### 3. Warstwa danych

Obsługuje dostęp do bazy i innych trwałych źródeł danych.

### 4. Mieszanie

Endpoint robiący jednocześnie walidację, logikę i zapytania SQL.

### 5. Czemu nie zawsze

Bo nadmiar warstw w małym projekcie może tylko zwiększyć złożoność.
