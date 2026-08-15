# Architektura warstwowa w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest architektura warstwowa](#czym-jest-architektura-warstwowa)
3. [Po co dzielić system na warstwy](#po-co-dzielić-system-na-warstwy)
4. [Typowe warstwy](#typowe-warstwy)
5. [Warstwa HTTP, biznesowa i danych](#warstwa-http-biznesowa-i-danych)
6. [Korzyści dla testowania](#korzyści-dla-testowania)
7. [Korzyści dla utrzymania](#korzyści-dla-utrzymania)
8. [Przykład mentalny](#przykład-mentalny)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczna ściąga](#praktyczna-ściąga)
11. [Ćwiczenia](#ćwiczenia)
12. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

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
- inna rozmawia z bazą albo infrastrukturą.

To po prostu sposób ograniczania chaosu przez czytelne granice odpowiedzialności.

---

## Po co dzielić system na warstwy

Bo pomaga:

- zapanować nad złożonością,
- ograniczyć chaos,
- łatwiej testować kod,
- łatwiej wymieniać elementy infrastruktury,
- lepiej rozumieć przepływ danych.

---

## Typowe warstwy

W backendzie Python często pojawiają się:

- warstwa HTTP albo prezentacji,
- warstwa aplikacyjna albo biznesowa,
- warstwa danych albo infrastruktury.

Nie każdy projekt musi nazywać je tak samo, ale sens zwykle jest podobny.

---

## Warstwa HTTP, biznesowa i danych

### Warstwa HTTP

- odbiera request,
- zwraca response,
- mapuje dane wejścia i wyjścia.

### Warstwa biznesowa

- realizuje reguły domenowe,
- koordynuje przepływ,
- podejmuje decyzje biznesowe.

### Warstwa danych

- pobiera i zapisuje dane,
- komunikuje się z bazą,
- ukrywa szczegóły trwałości danych.

---

## Korzyści dla testowania

To ogromna zaleta.

Jeśli logika biznesowa nie zależy twardo od frameworka i bazy, da się ją testować:

- szybciej,
- czyściej,
- z mniejszą ilością setupu.

---

## Korzyści dla utrzymania

Zmiana w jednej warstwie nie musi od razu rozwalać całego systemu.

To daje:

- lepszą modularność,
- mniejszy chaos zmian,
- łatwiejsze code review,
- lepszą przewidywalność projektu.

---

## Przykład mentalny

Dobry podział:

- endpoint `POST /orders`,
- serwis `create_order`,
- repozytorium `save_order`.

Zły podział:

endpoint, który:

- waliduje,
- liczy,
- odpytuje bazę,
- wysyła mail,
- buduje odpowiedź.

Technicznie może działać.

Architektonicznie zwykle szybko robi się trudny do utrzymania.

---

## Typowe błędy początkujących

- wrzucanie wszystkiego do endpointów,
- brak rozróżnienia między logiką biznesową a bazą,
- sztuczne mnożenie warstw w bardzo małym projekcie,
- nazwanie katalogów `services` i `utils` bez realnego podziału odpowiedzialności.

---

## Praktyczna ściąga

### Dobre pytanie

Która warstwa powinna za to odpowiadać?

### Dobry podział

- HTTP odbiera i zwraca,
- biznes decyduje,
- dane zapisują i pobierają.

### Uwaga

Warstwy mają upraszczać projekt, a nie być ozdobą architektury.

---

## Ćwiczenia

1. Rozdziel prosty endpoint na warstwę HTTP, biznesową i danych.
2. Opisz przepływ danych przez te warstwy.
3. Wskaż przykład endpointu, który robi za dużo.
4. Wyjaśnij własnymi słowami, czemu rozdział warstw poprawia testowalność.
5. Podaj przykład projektu, w którym zbyt wiele warstw byłoby przerostem formy nad treścią.

---

## Najważniejsze do zapamiętania

- Architektura warstwowa porządkuje system przez rozdział odpowiedzialności.
- Warstwa HTTP nie powinna być centrum logiki biznesowej.
- Rozdział warstw poprawia testowalność i utrzymanie.
- Dobra architektura ma upraszczać projekt, a nie go komplikować.
