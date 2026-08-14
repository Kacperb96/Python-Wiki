# Zestaw ćwiczeń praktycznych — 02. Moduły, funkcje i organizacja kodu

Ćwiczenia są ułożone od prostych do bardziej projektowych. Ich celem jest nie tylko przećwiczenie składni, ale też wyrobienie nawyku dzielenia kodu na sensowne części.

Najlepiej:

- robić je po kolei,
- uruchamiać wszystko lokalnie,
- samemu rozbijać kod na pliki,
- zwracać uwagę nie tylko na to, czy działa, ale też czy da się to wygodnie czytać.

---

## Poziom 1 — funkcje

1. Napisz funkcję `dodaj(a, b)`, która zwraca sumę dwóch liczb.
2. Napisz funkcję `powitaj(imie)`, która zwraca powitanie.
3. Napisz funkcję `pole_prostokata(a, b)`.
4. Napisz funkcję z argumentem domyślnym, np. `powitaj(imie="swiecie")`.
5. Napisz funkcję, która przyjmuje listę liczb i zwraca ich sumę.
6. Napisz funkcję `jest_parzysta(n)`, która zwraca `True` lub `False`.
7. Napisz funkcję `policz_srednia(liczby)`, która zwraca wynik zamiast go wypisywać.
8. Napisz przykład dwóch funkcji: jednej, która tylko `print()`uje, i drugiej, która `return`uje. Pokaż różnicę w użyciu.

---

## Poziom 2 — `*args`, `**kwargs`, `lambda`

9. Napisz funkcję `suma(*args)`, która sumuje dowolną liczbę argumentów.
10. Napisz funkcję `pokaz_dane(**kwargs)`, która wypisuje wszystkie przekazane pary klucz-wartość.
11. Napisz funkcję, która przyjmuje `prefix` i `*args`, a potem zwraca listę stringów z prefiksem.
12. Użyj `lambda`, aby posortować listę krotek po drugim elemencie.
13. Użyj `lambda`, aby przekształcić listę liczb w listę ich kwadratów przez `map()`.
14. Użyj `lambda`, aby odfiltrować liczby dodatnie przez `filter()`.
15. Napisz przykład, w którym zwykłe `def` będzie czytelniejsze niż `lambda`.
16. Napisz funkcję z jawnymi argumentami i drugą wersję na `**kwargs`, a potem porównaj czytelność obu.

---

## Poziom 3 — moduły i importy

17. Utwórz plik `math_utils.py` z dwiema funkcjami i zaimportuj go do `main.py`.
18. Utwórz moduł z funkcją `normalizuj_email()` i użyj go w osobnym pliku.
19. Sprawdź działanie `if __name__ == "__main__"` w prostym module.
20. Napisz plik, który po imporcie nie wykonuje kodu testowego, ale po uruchomieniu bezpośrednim już tak.
21. Podziel prosty program kalkulatora na:
   - moduł z logiką,
   - moduł startowy.
22. Napisz dwa moduły i pokaż różnicę między `import module` a `from module import nazwa`.

---

## Poziom 4 — pakiety i organizacja projektu

23. Utwórz prosty pakiet `app` z plikami `users.py` i `utils.py`.
24. Dodaj `__init__.py` i zaimportuj funkcję z jednego modułu do drugiego.
25. Zrób prostą strukturę projektu:
   - `app/`
   - `tests/`
   - `README.md`
26. Napisz mały program CLI z funkcją `main()` i poprawnym punktem wejścia.
27. Utwórz prosty moduł `validators.py` i użyj go w `main.py` do walidacji danych wejściowych.
28. Zorganizuj projekt „książki” na pakiety:
   - `books`
   - `authors`
   - `services`
29. Dodaj prosty przykład importu względnego wewnątrz pakietu.

---

## Poziom 5 — projektowanie API funkcji

30. Weź 3 źle nazwane funkcje i popraw ich nazwy oraz argumenty.
31. Rozbij długą funkcję na 3 mniejsze, każdą z jedną odpowiedzialnością.
32. Napisz funkcję, która ma jawne argumenty zamiast ukrytego `**kwargs`, jeśli to poprawia czytelność.
33. Stwórz mały moduł z 5 funkcjami pomocniczymi i upewnij się, że ich nazwy jasno opisują działanie.
34. Napisz funkcję, która niczego nie zapisuje globalnie, tylko zwraca dane dalej do przetworzenia.
35. Napisz funkcję, która ma zbyt ogólną nazwę, a potem zaprojektuj jej lepsze API.

---

## Zadanie końcowe

36. Zbuduj mini projekt `task_manager`:
   - pakiet `tasks`,
   - moduł `storage`,
   - moduł `cli`,
   - funkcję `main()`,
   - kilka funkcji do dodawania, listowania i oznaczania zadań,
   - czytelne importy i sensowny podział odpowiedzialności.

Jeśli zrobisz to samodzielnie i rozumiesz, dlaczego kod został podzielony właśnie tak, to znaczy, że dział 2 naprawdę siedzi.
