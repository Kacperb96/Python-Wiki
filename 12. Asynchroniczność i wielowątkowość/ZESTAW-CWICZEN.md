# Zestaw ćwiczeń praktycznych — 12. Asynchroniczność i wielowątkowość

Ćwiczenia w tym folderze najlepiej robić nie tylko "żeby działało", ale też z odpowiedzią na pytanie:

`dlaczego akurat ten model współbieżności ma tutaj sens?`

To bardzo ważne, bo w tym obszarze łatwo nauczyć się składni, a dużo trudniej nauczyć się doboru narzędzia do problemu.

## Jak pracować z tym zestawem

Najlepszy rytm:

1. najpierw zrób małe zadania mechaniczne,
2. potem przewiduj output i kolejność wykonania,
3. potem przejdź do porównań modeli,
4. na końcu rób większe scenariusze architektoniczne.

Nie traktuj:

- `asyncio`,
- wątków,
- procesów,
- executorów,
- kolejek

jako narzędzi zamiennych 1:1.

## Poziom 1 — `async` i `await`

1. Napisz prostą coroutine zwracającą tekst po `asyncio.sleep()`.
2. Uruchom jedną coroutine przez `asyncio.run()`.
3. Napisz dwie coroutine i uruchom je sekwencyjnie.
4. Uruchom te same dwie coroutine współbieżnie przez `asyncio.gather()`.
5. Porównaj czas wykonania sekwencyjnego i współbieżnego.
6. Dodaj `await asyncio.sleep(...)` w kilku miejscach i przewiduj kolejność outputu.
7. Napisz własnymi słowami, czym różni się "mam async funkcję" od "mam realną współbieżność I/O".

## Poziom 2 — `asyncio`, taski i timeouty

8. Utwórz task przez `asyncio.create_task()`.
9. Uruchom task w tle i odbierz jego wynik później.
10. Anuluj zadanie i obsłuż `CancelledError`.
11. Dodaj timeout przez `asyncio.wait_for()`.
12. Napisz prosty async worker przetwarzający listę zadań.
13. Pokaż różnicę między zwykłym `await` a wcześniejszym utworzeniem taska.
14. Zbuduj mały przykład, w którym jedno zadanie kończy się szybko, a drugie długo trwa, i pokaż, jak zmienia się flow programu.

## Poziom 3 — async HTTP

15. Pobierz jeden endpoint przez `httpx.AsyncClient`.
16. Pobierz kilka endpointów współbieżnie.
17. Dodaj limit współbieżności przez semafor.
18. Obsłuż timeout zapytania.
19. Obsłuż błąd HTTP i wypisz czytelny komunikat.
20. Zapisz własnymi słowami, czemu jednego klienta HTTP warto współdzielić zamiast tworzyć go dla każdego requestu.
21. Porównaj mentalnie: kiedy async HTTP da dużą wartość, a kiedy będzie tylko dodatkową złożonością.

## Poziom 4 — wątki

22. Uruchom dwie funkcje w osobnych wątkach.
23. Użyj `join()`, żeby poczekać na ich zakończenie.
24. Zaimplementuj współdzielony licznik i pokaż ryzyko błędu przy równoczesnym zapisie.
25. Zabezpiecz licznik przez `Lock`.
26. Użyj `Event`, by zsynchronizować dwa wątki.
27. Użyj `ThreadPoolExecutor` do przetworzenia listy zadań I/O-bound.
28. Napisz własnymi słowami, czemu wątki są częściej dobrym wyborem dla blokującego I/O niż dla ciężkich obliczeń CPU.

## Poziom 5 — procesy

29. Uruchom jedną funkcję w osobnym procesie.
30. Przekaż dane do procesu przez argumenty.
31. Przekaż wynik z procesu przez `Queue`.
32. Użyj `Pool` do przetworzenia listy liczb.
33. Wyjaśnij, czemu przy `multiprocessing` często potrzebujesz `if __name__ == "__main__"`.
34. Porównaj mentalnie: kiedy wybrać wątki, a kiedy procesy.
35. Opisz przypadek, w którym `ProcessPoolExecutor` byłby sensowniejszy niż ręczne zarządzanie procesami.

## Poziom 6 — `concurrent.futures`

36. Użyj `ThreadPoolExecutor` do uruchomienia kilku zadań z `sleep`.
37. Użyj `executor.map()` do policzenia kwadratów liczb.
38. Użyj `as_completed()` i pokaż kolejność zakończenia zadań.
39. Zrób prosty przykład przez `ProcessPoolExecutor`.
40. Porównaj `executor.map()` i `submit() + future.result()`.
41. Opisz, kiedy `concurrent.futures` jest wygodniejsze niż ręczne `threading` lub `multiprocessing`.

## Poziom 7 — porównanie modeli współbieżności

42. Opisz scenariusz typowo I/O-bound i dobierz do niego właściwe narzędzie.
43. Opisz scenariusz typowo CPU-bound i dobierz do niego właściwe narzędzie.
44. Wskaż przypadek, gdzie `async` ma sens, ale wątki też mogłyby zadziałać.
45. Wskaż przypadek, gdzie `threading` będzie słabym wyborem.
46. Wskaż przypadek, gdzie `multiprocessing` będzie nadmiarem.
47. Napisz krótką notatkę: `problem -> najlepszy model współbieżności -> dlaczego`.
48. Porównaj na jednym przykładzie trzy podejścia: sync, `ThreadPoolExecutor`, `asyncio`.

## Poziom 8 — kolejki i systemy rozproszone

49. Rozpisz mentalny przepływ zadania w RabbitMQ.
50. Napisz prosty przykład tasku Celery w kodzie.
51. Opisz przepływ zdarzenia w Kafce między producentem i konsumentami.
52. Zaprojektuj scenariusz, w którym backend HTTP wrzuca zadanie do kolejki zamiast wykonywać je natychmiast.
53. Wyjaśnij różnicę między `task queue` a `event streaming`.
54. Opisz, czemu retry i idempotencja są ważne w pracy z kolejkami.
55. Podaj przykład problemu, którego nie rozwiąże ani `asyncio`, ani wątki, ale dobrze rozwiąże kolejka z workerem.

## Poziom 9 — case studies architektoniczne

56. Masz endpoint, który generuje PDF przez 20 sekund. Opisz, czemu nie powinien robić tego wprost w żądaniu HTTP.
57. Masz crawler pobierający dane z 1000 stron. Zastanów się, co tu ma sens: sync, async, wątki czy procesy.
58. Masz ciężką analizę danych na dużych liczbach. Wybierz między wątkami a procesami i uzasadnij.
59. Masz aplikację, która wysyła maile, zapisuje logi i aktualizuje dashboard. Zastanów się, które elementy warto oddelegować do tła.
60. Własnymi słowami porównaj: `asyncio`, `threading`, `multiprocessing`, `concurrent.futures`, Celery.
61. Opisz system, w którym jeden fragment powinien używać async, a inny osobnego workera kolejki.

## Poziom 10 — większe zadania przekrojowe

62. Zaprojektuj mini system „przetwarzania zgłoszeń”, który obejmuje:

- wejście HTTP albo jego symulację,
- zadania async do pobierania danych,
- osobną pracę w tle realizowaną przez wątek albo proces,
- koncepcję kolejki background jobs,
- timeouty,
- obsługę błędów i anulowania.

63. Opisz krótko:

- które elementy są I/O-bound,
- które są CPU-bound,
- gdzie używasz async,
- gdzie używasz wątków albo procesów,
- gdzie pojawia się sens kolejki.

64. Zrób większe porównanie dla jednego problemu:

- wersja sekwencyjna,
- wersja `asyncio`,
- wersja `ThreadPoolExecutor`.

Potem odpowiedz:

- która była najprostsza,
- która była najszybsza dla tego typu problemu,
- która byłaby najłatwiejsza do utrzymania.

65. Zaprojektuj moduł `reporting`, który:

- pobiera dane z kilku API,
- wykonuje kosztowne obliczenia,
- zapisuje wynik do pliku,
- a użytkownik nie powinien czekać na wszystko w żądaniu HTTP.

Masz rozpisać:

- co zrobisz async,
- co zrobisz w tle,
- co zrobisz przez proces,
- czy potrzebujesz kolejki,
- jak będziesz obsługiwać timeouty i błędy.

## Jak oceniać większe zadania

Przy zadaniach przekrojowych nie wystarczy, że "coś działa".

Dobre rozwiązanie powinno umieć obronić:

- dlaczego użyto właśnie tego modelu współbieżności,
- które fragmenty są I/O-bound, a które CPU-bound,
- gdzie są timeouty i co się dzieje po ich przekroczeniu,
- jak wygląda obsługa błędów,
- czy rozwiązanie da się rozwijać bez chaosu,
- czy nie użyto zbyt ciężkiego narzędzia do prostego problemu.

## Checklista do capstone'ów

Jeśli robisz większe zadanie, sprawdź:

1. Czy umiesz nazwać typ problemu: I/O-bound czy CPU-bound?
2. Czy umiesz uzasadnić wybór: `asyncio`, wątki, procesy albo kolejka?
3. Czy kod obsługuje timeouty, anulowanie albo awarie workerów?
4. Czy nie blokujesz event loop ciężką pracą CPU?
5. Czy nie używasz procesów tam, gdzie wystarczyłby prosty async albo wątki?
6. Czy wyniki i błędy są zbierane w czytelny sposób?
7. Czy rozwiązanie byłoby zrozumiałe dla drugiej osoby w zespole?

## Po czym poznasz bardzo dobrą odpowiedź

Bardzo dobra odpowiedź:

- nie tylko pokazuje kod,
- ale też tłumaczy kompromisy,
- porównuje co najmniej dwa możliwe podejścia,
- wskazuje pułapki,
- i potrafi powiedzieć, czemu czegoś nie wybrano.

To szczególnie ważne w zadaniach 62-66, bo tam już bardziej ćwiczysz myślenie architektoniczne niż samą składnię.

## Zadanie końcowe

66. Przygotuj przekrojowy dokument:

`Jak dobrać model współbieżności do problemu w Pythonie`

Uwzględnij w nim:

- różnicę między I/O-bound i CPU-bound,
- kiedy używać `asyncio`,
- kiedy używać wątków,
- kiedy używać procesów,
- kiedy używać `concurrent.futures`,
- kiedy używać kolejki i workera,
- typowe pułapki,
- 3 własne case studies z uzasadnieniem wyboru.
