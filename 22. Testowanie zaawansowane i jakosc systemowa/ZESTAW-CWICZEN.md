# Zestaw ćwiczeń praktycznych — 22. Testowanie zaawansowane i jakość systemowa

W tym folderze bardzo ważne jest patrzenie na testy jako na narzędzie projektowe, a nie tylko techniczne.

## Poziom 1 — poziomy testów

1. Wyjaśnij różnicę między testem jednostkowym, integracyjnym i E2E.
2. Podaj przykład problemu, którego unit test nie wykryje, a test integracyjny tak.
3. Opisz, kiedy E2E ma sens, a kiedy byłoby przesadą.
4. Wyjaśnij własnymi słowami, czym jest contract test.
5. Podaj przykład, gdzie zaufanie do integracji z zewnętrznym systemem wymaga czegoś więcej niż mocka.

## Poziom 2 — testy integracyjne i kontraktowe

6. Zaprojektuj prosty test integracyjny dla serwisu i repozytorium.
7. Opisz, co powinien sprawdzić test integracyjny endpointu zapisującego dane do bazy.
8. Zaprojektuj przykład contract testu dla klienta API.
9. Porównaj, co daje test integracyjny, a co contract test.
10. Opisz, gdzie kończy się odpowiedzialność unit testu, a zaczyna integracja.

## Poziom 3 — dane testowe

11. Wyjaśnij, po co są fixtures.
12. Zbuduj fixture zwracającą przykładowego użytkownika.
13. Wyjaśnij, czym jest test data builder.
14. Zaprojektuj builder dla obiektu `Order`.
15. Opisz, czemu powielanie ręcznie tych samych danych testowych jest złym pomysłem.

## Poziom 4 — fake, mock, stub

16. Wyjaśnij różnicę między fake, mock i stub.
17. Podaj przykład, kiedy fake jest lepszy niż mock.
18. Podaj przykład, kiedy mock jest uzasadniony.
19. Wskaż przypadek, w którym nadmiar mocków psuje test.
20. Zaprojektuj prosty fake repozytorium do testów serwisu.

## Poziom 5 — flaky tests

21. Wyjaśnij, czym jest flaky test.
22. Podaj 5 możliwych przyczyn niestabilnych testów.
23. Opisz, czemu flaky tests są groźniejsze niż zwykłe czerwone testy.
24. Zaprojektuj checklistę diagnozy flaky testu.
25. Opisz, jakie elementy środowiska mogą powodować niestabilność testów.

## Poziom 6 — strategia testów

26. Weź mały projekt i zaproponuj, które elementy testowałbyś unit testami.
27. Wskaż, które przepływy wymagają integracji.
28. Opisz, czy potrzebne byłyby testy E2E i dlaczego.
29. Zaproponuj miejsce na contract tests.
30. Zrób mini strategię testów dla małej aplikacji webowej albo CLI.

## Zadanie końcowe

31. Weź mały moduł lub mini aplikację i przygotuj plan jakości systemowej:

- które testy powinny być jednostkowe,
- które integracyjne,
- czy potrzebne są E2E,
- czy potrzebny jest contract test,
- jak przygotować dane testowe,
- gdzie użyć fake zamiast mocka,
- jak ograniczyć ryzyko flaky tests,
- co ten zestaw testów ma naprawdę chronić.
