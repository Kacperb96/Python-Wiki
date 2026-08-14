# Zestaw ćwiczeń praktycznych — 12. Asynchroniczność i wielowątkowość

## Poziom 1 — async basics

1. Napisz prostą coroutine zwracającą tekst po `asyncio.sleep()`.
2. Uruchom jedną coroutine przez `asyncio.run()`.
3. Uruchom dwie coroutine współbieżnie przez `gather()`.
4. Pokaż różnicę czasu między wykonaniem sekwencyjnym i współbieżnym.
5. Dodaj timeout przez `asyncio.wait_for()`.

## Poziom 2 — taski i event loop

6. Utwórz task przez `create_task()`.
7. Uruchom task w tle i odbierz jego wynik później.
8. Anuluj zadanie i obsłuż `CancelledError`.
9. Napisz prosty worker async przetwarzający listę zadań.

## Poziom 3 — async HTTP

10. Pobierz jeden endpoint przez `httpx.AsyncClient`.
11. Pobierz kilka endpointów współbieżnie.
12. Dodaj limit współbieżności przez semafor.
13. Obsłuż timeout i błąd HTTP.

## Poziom 4 — wątki

14. Uruchom dwie funkcje w osobnych wątkach.
15. Zaimplementuj współdzielony licznik z `Lock`.
16. Użyj `Event`, by zsynchronizować dwa wątki.
17. Użyj `ThreadPoolExecutor` do przetworzenia listy zadań.

## Poziom 5 — procesy

18. Uruchom jedną funkcję w osobnym procesie.
19. Przekaż wynik przez `Queue`.
20. Użyj `Pool` do przetworzenia listy liczb.
21. Porównaj mentalnie, kiedy wybrać wątki, a kiedy procesy.

## Poziom 6 — kolejki i systemy rozproszone

22. Rozpisz mentalny przepływ zadania w RabbitMQ.
23. Zrób prosty przykład tasku Celery w kodzie.
24. Opisz przepływ zdarzenia w Kafce między producentem i konsumentami.
25. Zaprojektuj scenariusz, w którym backend HTTP wrzuca zadanie do kolejki zamiast wykonywać je natychmiast.

## Zadanie końcowe

26. Zbuduj mini system „przetwarzania zgłoszeń”:
   - wejście HTTP lub symulowane,
   - zadania async do pobierania danych,
   - wątek lub proces do osobnej pracy,
   - koncepcja kolejki background jobs,
   - timeouty,
   - obsługa błędów i anulowania.
