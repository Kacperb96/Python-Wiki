# Zestaw ćwiczeń praktycznych — 15. Architektura i jakość kodu

## Poziom 1 — rozpoznawanie problemów

1. Weź długą funkcję i wypisz, ile różnych odpowiedzialności zawiera.
2. Znajdź przykład duplikacji w małym kodzie i wskaż, jak go uprościć.
3. Podaj przykład złej nazwy klasy i popraw ją.
4. Wskaż przykład ukrytego efektu ubocznego.

## Poziom 2 — refaktoryzacja

5. Rozbij jedną długą funkcję na 3 mniejsze.
6. Zastąp duplikację wspólną funkcją pomocniczą.
7. Wydziel walidację z dużej funkcji do osobnej funkcji.
8. Rozdziel warstwę budowania odpowiedzi od warstwy liczenia wyniku.

## Poziom 3 — architektura warstwowa

9. Weź prosty endpoint i rozdziel go na:
   - HTTP,
   - serwis,
   - repozytorium.
10. Narysuj przepływ danych przez te warstwy.
11. Pokaż przykład, gdzie endpoint robi za dużo.

## Poziom 4 — separacja logiki i DI

12. Wyjmij logikę biznesową z endpointu do osobnej funkcji lub serwisu.
13. Wstrzyknij repozytorium do serwisu zamiast tworzyć je w środku.
14. Podmień zależność w teście na fake.
15. Zrób przykład jawnej zależności i ukrytej zależności.

## Poziom 5 — SOLID i wzorce

16. Znajdź w swoim kodzie przykład naruszenia SRP i popraw go.
17. Zamień duży `if` wyboru algorytmu na prosty wzorzec Strategy.
18. Zastosuj Factory do tworzenia klienta zależnie od konfiguracji.
19. Zastosuj Adapter do ujednolicenia interfejsu dwóch różnych źródeł danych.
20. Zbuduj prosty przypadek Repository niezależnie od ORM.

## Zadanie końcowe

21. Weź mały projekt z API albo CLI i zrefaktoryzuj go tak, żeby:
   - miał czytelne warstwy,
   - miał mniej code smells,
   - logika biznesowa była oddzielona,
   - zależności były jawne,
   - przynajmniej jeden wzorzec projektowy był użyty sensownie.
