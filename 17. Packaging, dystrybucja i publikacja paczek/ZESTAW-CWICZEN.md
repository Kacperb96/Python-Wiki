# Zestaw ćwiczeń praktycznych — 17. Packaging, dystrybucja i publikacja paczek

W tym folderze najlepiej ćwiczyć na jednym małym projekcie, który stopniowo rozwijasz od zwykłego katalogu z kodem do paczki gotowej do dystrybucji.

## Poziom 1 — fundament

1. Wyjaśnij, po co istnieje `pyproject.toml`.
2. Wypisz, jakie podstawowe metadata paczki warto tam umieścić.
3. Wyjaśnij różnicę między paczką instalowalną a zwykłym katalogiem z kodem.
4. Opisz, czym różni się zależność runtime od dev dependency.
5. Wskaż, jakie pole w konfiguracji mówi o wymaganej wersji Pythona.

## Poziom 2 — budowanie paczki

6. Utwórz minimalny `pyproject.toml` dla małego projektu.
7. Zbuduj paczkę i sprawdź, jakie pliki pojawiły się po buildzie.
8. Wyjaśnij różnicę między `wheel` i `sdist`.
9. Sprawdź zawartość katalogu `dist/` po buildzie.
10. Opisz, kiedy użytkownik instaluje gotowy wheel, a kiedy buduje paczkę ze źródeł.

## Poziom 3 — publikacja i wersjonowanie

11. Przygotuj wersję projektu `0.1.0`.
12. Opisz, kiedy podbić `patch`, `minor` i `major`.
13. Przygotuj projekt do publikacji na TestPyPI.
14. Wypisz kroki bezpiecznej publikacji testowej.
15. Wyjaśnij, czemu warto najpierw publikować na TestPyPI, a nie od razu na PyPI.

## Poziom 4 — CLI i entry points

16. Zbuduj małe CLI, które wypisuje tekst albo przetwarza argument.
17. Skonfiguruj entry point tak, aby narzędzie uruchamiało się jako komenda.
18. Wyjaśnij różnicę między `python -m modul` a skryptem CLI z entry point.
19. Dodaj prostą pomoc `--help` do narzędzia.
20. Opisz, kiedy projekt warto publikować jako bibliotekę, a kiedy jako CLI.

## Poziom 5 — extras i kompatybilność

21. Dodaj zależność opcjonalną, np. `dev` albo `cli`.
22. Wyjaśnij, kiedy extras mają sens.
23. Ustaw wymaganie `requires-python` dla projektu.
24. Wskaż dwa możliwe problemy kompatybilności między wersjami Pythona.
25. Opisz, jak sprawdzić, czy paczka działa na więcej niż jednej wersji interpretera.

## Poziom 6 — zadania przekrojowe

26. Weź mały projekt z repo i wyobraź sobie, że ma stać się paczką instalowalną.
27. Rozpisz, jakie metadata, zależności i entry points byłyby potrzebne.
28. Zaproponuj wersję `0.1.0`, a potem scenariusz przejścia do `0.2.0` i `1.0.0`.
29. Opisz, które pliki i katalogi użytkownik końcowy powinien zobaczyć po buildzie.
30. Przygotuj checklistę publikacji, której sam byś używał przed wypuszczeniem nowej wersji.

## Zadanie końcowe

31. Zbuduj małą paczkę Python, która:

- ma `pyproject.toml`,
- da się zbudować do `wheel` i `sdist`,
- ma prosty entry point CLI,
- ma wersję projektu,
- ma co najmniej jedną zależność opcjonalną,
- ma opis kompatybilności z wersją Pythona.

Na końcu opisz:

- jakie decyzje podjąłeś,
- co było obowiązkowe,
- co było tylko wygodne,
- jakie błędy najłatwiej tu popełnić.
