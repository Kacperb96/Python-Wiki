# Zestaw ćwiczeń praktycznych — 21. Debugowanie i utrzymanie dużego kodu

W tym folderze szczególnie ważne jest myślenie procesem, a nie tylko znajomość pojęć.

## Poziom 1 — wejście w problem

1. Wyjaśnij własnymi słowami różnicę między objawem a przyczyną błędu.
2. Opisz, czemu czytanie całego repo od początku zwykle nie jest dobrym planem.
3. Wyjaśnij, po co tworzyć minimal reproducible example.
4. Podaj przykład regresji.
5. Wyjaśnij, czemu traceback to cenna informacja, a nie tylko strasząca ściana tekstu.

## Poziom 2 — czytanie i debugowanie

6. Weź mały moduł i wskaż, od którego miejsca zacząłbyś jego analizę.
7. Rozpisz strategię debugowania prostego błędu krok po kroku.
8. Opisz, jak zawęziłbyś problem zamiast zgadywać.
9. Napisz mały traceback i opisz, jak byś go czytał.
10. Wskaż 3 rzeczy, których nie warto robić od razu podczas debugowania.

## Poziom 3 — MRE i traceback

11. Weź zbyt duży przykład błędu i opisz, jak go zminimalizować.
12. Zbuduj własny mini błąd i uprość go do minimalnego reprodukowalnego przypadku.
13. Pokaż przykład tracebacka z 3 funkcjami i wskaż sensowny punkt startu.
14. Opisz, kiedy błąd jest lokalny, a kiedy systemowy.
15. Wyjaśnij, dlaczego dobra reprodukcja błędu często jest połową rozwiązania.

## Poziom 4 — regresje i diagnoza

16. Opisz, czym jest regresja w kodzie.
17. Zaproponuj plan zawężenia momentu, kiedy bug się pojawił.
18. Wyjaśnij, do czego służy `git bisect`.
19. Opisz, jak logi pomagają w diagnozie.
20. Wyjaśnij, czym metryki różnią się od logów.

## Poziom 5 — stary kod i refaktoryzacja

21. Weź chaotyczną funkcję i rozpisz bezpieczny plan jej poprawy.
22. Wskaż, kiedy nie warto robić dużej refaktoryzacji przy małym bugfixie.
23. Opisz, czemu małe kroki są ważne w starym repo.
24. Podaj przykład zmiany, która wygląda niewinnie, ale może być ryzykowna.
25. Zrób checklistę: co sprawdzasz przed refaktoryzacją starego modułu.

## Poziom 6 — zadania przekrojowe

26. Weź mały bug i rozpisz cały proces: objaw -> reprodukcja -> zawężenie -> poprawka -> weryfikacja.
27. Przeanalizuj mały traceback i zaproponuj hipotezy przyczyny.
28. Zastanów się, jakie logi dodałbyś do diagnozy problemu produkcyjnego.
29. Zaproponuj, jak podejść do obcego repo z 20 modułami bez czytania wszystkiego naraz.
30. Wypisz 5 zasad bezpiecznej pracy w starym kodzie.

## Zadanie końcowe

31. Weź mały fragment starego albo celowo nieczytelnego kodu i przygotuj analizę:

- co jest objawem problemu,
- jak odtworzyć błąd,
- co byłoby minimalnym przykładem,
- jak czytać traceback,
- jakich logów byś potrzebował,
- jaką najmniejszą sensowną poprawkę byś zrobił,
- jak sprawdziłbyś, że poprawka nie wprowadziła regresji.
