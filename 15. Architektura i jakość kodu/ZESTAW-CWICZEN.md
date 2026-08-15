# Zestaw ćwiczeń praktycznych — 15. Architektura i jakość kodu

Ćwiczenia są ułożone od rozpoznawania problemów do bardziej świadomego projektowania struktury kodu.

Najlepiej robić je etapami.

---

## Poziom 1 — rozpoznawanie problemów

1. Weź długą funkcję i wypisz, ile różnych odpowiedzialności zawiera.
2. Znajdź przykład duplikacji w małym kodzie i wskaż, jak go uprościć.
3. Podaj przykład złej nazwy klasy i popraw ją.
4. Wskaż przykład ukrytego efektu ubocznego.
5. Wskaż przykład funkcji, która robi za dużo.
6. Wskaż przykład klasy, która wie za dużo o innych częściach systemu.

---

## Poziom 2 — refaktoryzacja

7. Rozbij jedną długą funkcję na 3 mniejsze.
8. Zastąp duplikację wspólną funkcją pomocniczą.
9. Wydziel walidację z dużej funkcji do osobnej funkcji.
10. Rozdziel warstwę budowania odpowiedzi od warstwy liczenia wyniku.
11. Usuń martwy kod albo nieużywaną gałąź warunkową.
12. Zmień chaotyczne nazwy tak, by lepiej opisywały odpowiedzialność.

---

## Poziom 3 — architektura warstwowa

13. Weź prosty endpoint i rozdziel go na:

- HTTP,
- serwis,
- repozytorium.

14. Narysuj albo opisz przepływ danych przez te warstwy.
15. Pokaż przykład, gdzie endpoint robi za dużo.
16. Wskaż, które rzeczy powinny zostać w warstwie HTTP, a które nie.
17. Wskaż, które rzeczy powinny być w warstwie danych, a które nie.

---

## Poziom 4 — separacja logiki i DI

18. Wyjmij logikę biznesową z endpointu do osobnej funkcji albo serwisu.
19. Wstrzyknij repozytorium do serwisu zamiast tworzyć je w środku.
20. Podmień zależność w teście na fake.
21. Zrób przykład jawnej zależności i ukrytej zależności.
22. Wyjaśnij, czemu jawne zależności są łatwiejsze do testowania.
23. Wskaż przykład kodu zbyt mocno związanego z frameworkiem.

---

## Poziom 5 — SOLID

24. Znajdź w swoim kodzie przykład naruszenia SRP i popraw go.
25. Wskaż miejsce, gdzie kod rośnie przez dokładanie kolejnych `ifów`, i zaproponuj lepszą strukturę.
26. Podaj przykład podklasy, która mogłaby łamać LSP.
27. Wskaż interfejs albo klasę, która ma zbyt szerokie API.
28. Opisz przypadek, w którym logika biznesowa jest zbyt mocno przyklejona do szczegółu infrastruktury.

---

## Poziom 6 — wzorce projektowe

29. Zamień duży `if` wyboru algorytmu na prosty wzorzec Strategy.
30. Zastosuj Factory do tworzenia klienta zależnie od konfiguracji.
31. Zastosuj Adapter do ujednolicenia interfejsu dwóch różnych źródeł danych.
32. Zbuduj prosty przypadek Repository niezależnie od ORM.
33. Wyjaśnij własnymi słowami, czemu wzorzec ma być narzędziem, a nie celem samym w sobie.

---

## Poziom 7 — myślenie projektowe

34. Weź mały fragment projektu i wskaż 3 największe code smells.
35. Zastanów się, które z nich warto poprawić od razu, a które mogą poczekać.
36. Opisz, jakie ryzyko niesie duża refaktoryzacja bez testów.
37. Podaj przykład, gdzie architektura warstwowa realnie pomaga, a nie tylko dobrze wygląda.
38. Podaj przykład, gdzie zbyt wiele warstw byłoby przerostem formy nad treścią.

---

## Zadanie końcowe

39. Weź mały projekt z API albo CLI i zrefaktoryzuj go tak, żeby:

- miał czytelne warstwy,
- miał mniej code smells,
- logika biznesowa była oddzielona,
- zależności były jawne,
- przynajmniej jeden wzorzec projektowy był użyty sensownie.

40. Opisz krótko:

- co było największym problemem przed zmianą,
- jak wygląda przepływ po zmianie,
- które decyzje architektoniczne dały największą wartość,
- czego świadomie nie komplikowałeś.

---

## Jak pracować z tym zestawem

Najlepiej:

1. najpierw zrobić poziomy 1-2,
2. potem pokazać rozwiązania,
3. później wejść w warstwy i DI,
4. SOLID i wzorce traktować jako narzędzia do porządkowania, a nie ozdoby projektu.
