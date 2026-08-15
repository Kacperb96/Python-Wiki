# Zestaw ćwiczeń praktycznych — 12. Asynchroniczność i wielowątkowość

Ćwiczenia są ułożone warstwowo: od prostych coroutine do bardziej architektonicznego myślenia o taskach w tle i systemach rozproszonych.

Nie przeskakuj od razu do Kafki, jeśli nie czujesz jeszcze `asyncio`.

---

## Poziom 1 — `async` i `await`

1. Napisz prostą coroutine zwracającą tekst po `asyncio.sleep()`.
2. Uruchom jedną coroutine przez `asyncio.run()`.
3. Napisz dwie coroutine i uruchom je sekwencyjnie.
4. Uruchom te same dwie coroutine współbieżnie przez `asyncio.gather()`.
5. Porównaj czas wykonania sekwencyjnego i współbieżnego.
6. Dodaj `await asyncio.sleep(...)` w kilku miejscach i przewiduj kolejność outputu.

---

## Poziom 2 — `asyncio`, taski i timeouty

7. Utwórz task przez `asyncio.create_task()`.
8. Uruchom task w tle i odbierz jego wynik później.
9. Anuluj zadanie i obsłuż `CancelledError`.
10. Dodaj timeout przez `asyncio.wait_for()`.
11. Napisz prosty async worker przetwarzający listę zadań.
12. Pokaż różnicę między zwykłym `await` a wcześniejszym utworzeniem taska.

---

## Poziom 3 — async HTTP

13. Pobierz jeden endpoint przez `httpx.AsyncClient`.
14. Pobierz kilka endpointów współbieżnie.
15. Dodaj limit współbieżności przez semafor.
16. Obsłuż timeout zapytania.
17. Obsłuż błąd HTTP i wypisz czytelny komunikat.
18. Zapisz własnymi słowami, czemu jednego klienta HTTP warto współdzielić zamiast tworzyć go dla każdego requestu.

---

## Poziom 4 — wątki

19. Uruchom dwie funkcje w osobnych wątkach.
20. Użyj `join()`, żeby poczekać na ich zakończenie.
21. Zaimplementuj współdzielony licznik i pokaż ryzyko błędu przy równoczesnym zapisie.
22. Zabezpiecz licznik przez `Lock`.
23. Użyj `Event`, by zsynchronizować dwa wątki.
24. Użyj `ThreadPoolExecutor` do przetworzenia listy zadań I/O-bound.

---

## Poziom 5 — procesy

25. Uruchom jedną funkcję w osobnym procesie.
26. Przekaż dane do procesu przez argumenty.
27. Przekaż wynik z procesu przez `Queue`.
28. Użyj `Pool` do przetworzenia listy liczb.
29. Wyjaśnij, czemu przy `multiprocessing` często potrzebujesz `if __name__ == "__main__"`.
30. Porównaj mentalnie: kiedy wybrać wątki, a kiedy procesy.

---

## Poziom 6 — porównanie modeli współbieżności

31. Opisz scenariusz typowo I/O-bound i dobierz do niego właściwe narzędzie.
32. Opisz scenariusz typowo CPU-bound i dobierz do niego właściwe narzędzie.
33. Wskaż przypadek, gdzie `async` ma sens, ale wątki też mogłyby zadziałać.
34. Wskaż przypadek, gdzie `threading` będzie słabym wyborem.
35. Wskaż przypadek, gdzie `multiprocessing` będzie nadmiarem.
36. Napisz krótką notatkę: „problem -> najlepszy model współbieżności -> dlaczego”.

---

## Poziom 7 — kolejki i systemy rozproszone

37. Rozpisz mentalny przepływ zadania w RabbitMQ.
38. Napisz prosty przykład tasku Celery w kodzie.
39. Opisz przepływ zdarzenia w Kafce między producentem i konsumentami.
40. Zaprojektuj scenariusz, w którym backend HTTP wrzuca zadanie do kolejki zamiast wykonywać je natychmiast.
41. Wyjaśnij różnicę między „task queue” a „event streaming”.
42. Opisz, czemu retry i idempotencja są ważne w pracy z kolejkami.

---

## Poziom 8 — myślenie architektoniczne

43. Masz endpoint, który generuje PDF przez 20 sekund. Opisz, czemu nie powinien robić tego wprost w żądaniu HTTP.
44. Masz crawler pobierający dane z 1000 stron. Zastanów się, co tu ma sens: sync, async, wątki czy procesy.
45. Masz ciężką analizę danych na dużych liczbach. Wybierz między wątkami a procesami i uzasadnij.
46. Masz aplikację, która wysyła maile, zapisuje logi i aktualizuje dashboard. Zastanów się, które elementy warto oddelegować do tła.
47. Własnymi słowami porównaj: `asyncio`, `threading`, `multiprocessing`, Celery.

---

## Zadanie końcowe

48. Zaprojektuj mini system „przetwarzania zgłoszeń”, który obejmuje:

- wejście HTTP albo jego symulację,
- zadania async do pobierania danych,
- osobną pracę w tle realizowaną przez wątek albo proces,
- koncepcję kolejki background jobs,
- timeouty,
- obsługę błędów i anulowania.

49. Opisz krótko:

- które elementy są I/O-bound,
- które są CPU-bound,
- gdzie używasz async,
- gdzie używasz wątków albo procesów,
- gdzie pojawia się sens kolejki.

---

## Jak pracować z tym zestawem

Najlepiej:

1. najpierw zrób zadania 1-18,
2. potem pokaż rozwiązania,
3. dopiero później przechodź do wątków i procesów,
4. część o kolejkach traktuj już bardziej architektonicznie niż jako czystą składnię.
