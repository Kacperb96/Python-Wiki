# Zestaw ćwiczeń praktycznych — 19. Runtime, pamięć i wnętrze Pythona

W tym folderze bardzo ważne jest rozumienie intuicji. Dlatego przy wielu zadaniach warto nie tylko napisać kod, ale też własnymi słowami opisać, dlaczego wynik jest taki, a nie inny.

## Poziom 1 — model myślenia

1. Wyjaśnij różnicę między nazwą zmiennej a obiektem.
2. Opisz, co to znaczy, że dwie nazwy wskazują na ten sam obiekt.
3. Wyjaśnij własnymi słowami, czym jest runtime.
4. Opisz, po co programiście w ogóle wiedza o wnętrzu interpretera.
5. Wskaż 3 sytuacje, w których taka wiedza pomaga praktycznie.

## Poziom 2 — GIL i wykonanie

6. Wyjaśnij własnymi słowami, czym jest GIL.
7. Opisz, czemu GIL najbardziej interesuje przy pracy CPU-bound.
8. Porównaj, kiedy lepsze są wątki, a kiedy procesy.
9. Podaj przykład zadania I/O-bound.
10. Podaj przykład zadania CPU-bound.

## Poziom 3 — obiekty, referencje, pamięć

11. Napisz przykład, w którym dwie zmienne wskazują na tę samą listę.
12. Pokaż, jak mutacja przez jedną nazwę wpływa na drugą.
13. Wyjaśnij, czym jest referencja.
14. Opisz, kiedy garbage collection ma znaczenie.
15. Podaj przykład problemu z cyklem referencji albo przynajmniej opisz intuicję takiego problemu.

## Poziom 4 — stos wywołań i import

16. Wyjaśnij, czym jest stos wywołań.
17. Napisz prosty przykład rekurencji i opisz, co dzieje się na stosie.
18. Wyjaśnij, czemu import może mieć skutki uboczne.
19. Podaj przykład modułu, który coś wykonuje podczas importu.
20. Opisz, czemu zbyt ciężki kod na poziomie modułu jest złą praktyką.

## Poziom 5 — interpreter i bytecode

21. Wyjaśnij różnicę między CPython i PyPy.
22. Opisz, czym jest bytecode.
23. Wyjaśnij, po co w ogóle istnieje etap pośredni między kodem źródłowym a wykonaniem.
24. Podaj przykład, kiedy wiedza o interpreterze może wpłynąć na decyzję optymalizacyjną.
25. Wytłumacz, czemu dwa interpretery Pythona mogą różnić się wydajnością.

## Poziom 6 — zadania przekrojowe

26. Weź prosty program i wskaż w nim: obiekty, nazwy, mutacje i miejsca potencjalnego aliasowania.
27. Opisz, czy jego problem byłby bardziej CPU-bound czy I/O-bound.
28. Wskaż, czy importy w tym programie mogą mieć skutki uboczne.
29. Zastanów się, czy wiedza o bytecode cokolwiek by tu realnie zmieniła.
30. Zrób własną checklistę: kiedy warto zejść na poziom "wnętrza Pythona", a kiedy nie ma to sensu.

## Zadanie końcowe

31. Napisz krótką analizę małego programu Python, w której opiszesz:

- jak działają w nim nazwy i obiekty,
- gdzie może pojawić się problem z mutowalnością,
- czy dominuje CPU czy I/O,
- czy import ma skutki uboczne,
- czy któryś aspekt runtime tłumaczy jego zachowanie,
- jakie 3 rzeczy z tego folderu byłyby najważniejsze do zrozumienia tego programu.
