# Zestaw ćwiczeń praktycznych — 02. Moduły, funkcje i organizacja kodu

Ćwiczenia są ułożone od prostych do bardziej projektowych.

Ich celem jest nie tylko przećwiczenie składni, ale też wyrobienie nawyku:

- dzielenia kodu na sensowne części,
- projektowania czytelnych funkcji,
- oddzielania logiki od punktu wejścia,
- budowania małego projektu bez chaosu.

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
9. Napisz funkcję `bezpieczne_dzielenie(a, b)`, która zwraca wynik albo `None`, gdy dzielisz przez zero.
10. Napisz funkcję, która przyjmuje tekst i zwraca jego znormalizowaną wersję: bez spacji z boków i małymi literami.

---

## Poziom 2 — `*args`, `**kwargs`, `lambda`

11. Napisz funkcję `suma(*args)`, która sumuje dowolną liczbę argumentów.
12. Napisz funkcję `pokaz_dane(**kwargs)`, która wypisuje wszystkie przekazane pary klucz-wartość.
13. Napisz funkcję, która przyjmuje `prefix` i `*args`, a potem zwraca listę stringów z prefiksem.
14. Użyj `lambda`, aby posortować listę krotek po drugim elemencie.
15. Użyj `lambda`, aby przekształcić listę liczb w listę ich kwadratów przez `map()`.
16. Użyj `lambda`, aby odfiltrować liczby dodatnie przez `filter()`.
17. Napisz przykład, w którym zwykłe `def` będzie czytelniejsze niż `lambda`.
18. Napisz funkcję z jawnymi argumentami i drugą wersję na `**kwargs`, a potem porównaj czytelność obu.
19. Napisz funkcję, która przyjmuje dowolną liczbę ocen i zwraca najwyższą ocenę.
20. Napisz funkcję, która przyjmuje `**kwargs` i buduje słownik profilu użytkownika.

---

## Poziom 3 — moduły i importy

21. Utwórz plik `math_utils.py` z dwiema funkcjami i zaimportuj go do `main.py`.
22. Utwórz moduł z funkcją `normalizuj_email()` i użyj go w osobnym pliku.
23. Sprawdź działanie `if __name__ == "__main__"` w prostym module.
24. Napisz plik, który po imporcie nie wykonuje kodu testowego, ale po uruchomieniu bezpośrednim już tak.
25. Podziel prosty program kalkulatora na:
   - moduł z logiką,
   - moduł startowy.
26. Napisz dwa moduły i pokaż różnicę między `import module` a `from module import nazwa`.
27. Napisz moduł `validators.py` i wykorzystaj go w `main.py`.
28. Zrób moduł `formatters.py`, który zawiera 2-3 funkcje pomocnicze, i użyj go w drugim pliku.

---

## Poziom 4 — pakiety i organizacja projektu

29. Utwórz prosty pakiet `app` z plikami `users.py` i `utils.py`.
30. Dodaj `__init__.py` i zaimportuj funkcję z jednego modułu do drugiego.
31. Zrób prostą strukturę projektu:
   - `app/`
   - `tests/`
   - `README.md`
32. Napisz mały program CLI z funkcją `main()` i poprawnym punktem wejścia.
33. Utwórz prosty moduł `validators.py` i użyj go w `main.py` do walidacji danych wejściowych.
34. Zorganizuj projekt „książki” na pakiety:
   - `books`
   - `authors`
   - `services`
35. Dodaj prosty przykład importu względnego wewnątrz pakietu.
36. Utwórz pakiet `shop`, w którym jeden moduł korzysta z drugiego przez import względny.

---

## Poziom 5 — projektowanie API funkcji

37. Weź 3 źle nazwane funkcje i popraw ich nazwy oraz argumenty.
38. Rozbij długą funkcję na 3 mniejsze, każdą z jedną odpowiedzialnością.
39. Napisz funkcję, która ma jawne argumenty zamiast ukrytego `**kwargs`, jeśli to poprawia czytelność.
40. Stwórz mały moduł z 5 funkcjami pomocniczymi i upewnij się, że ich nazwy jasno opisują działanie.
41. Napisz funkcję, która niczego nie zapisuje globalnie, tylko zwraca dane dalej do przetworzenia.
42. Napisz funkcję, która ma zbyt ogólną nazwę, a potem zaprojektuj jej lepsze API.
43. Napisz funkcję, która zwraca dane, a nie wypisuje ich od razu, a potem pokaż, jak dzięki temu łatwiej ją przetestować.
44. Zaprojektuj dwie wersje tej samej funkcji:
   - jedną z chaotycznym API,
   - drugą z czytelnym API,
   i opisz różnicę.

---

## Poziom 6 — mini projekty

45. Zbuduj mini kalkulator z podziałem na:
   - `operations.py`,
   - `main.py`.
46. Zbuduj prosty menedżer kontaktów z modułami:
   - `storage.py`,
   - `formatters.py`,
   - `main.py`.
47. Zbuduj mini walidator użytkownika:
   - `validators.py`,
   - `users.py`,
   - `main.py`.
48. Zrób prostą aplikację do liczenia średniej ocen z osobnym modułem na logikę i osobnym punktem wejścia.

---

## Zadanie końcowe

49. Zbuduj mini projekt `task_manager`:
   - pakiet `tasks`,
   - moduł `storage`,
   - moduł `cli`,
   - funkcję `main()`,
   - kilka funkcji do dodawania, listowania i oznaczania zadań,
   - czytelne importy,
   - sensowny podział odpowiedzialności,
   - brak mieszania logiki z kodem startowym.

Jeśli zrobisz to samodzielnie i rozumiesz, dlaczego kod został podzielony właśnie tak, to znaczy, że dział 2 naprawdę siedzi.
