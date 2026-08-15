# 12. Asynchroniczność i wielowątkowość

To jest dział o współbieżności w Pythonie.

To jeden z tych tematów, które na początku bardzo łatwo brzmią bardziej tajemniczo, niż są w rzeczywistości.

Najważniejsze pytania tego działu to:

- kiedy używać `async` i `await`,
- czym różni się współbieżność od równoległości,
- kiedy lepsze są wątki,
- kiedy lepsze są procesy,
- kiedy potrzebujesz kolejki albo systemu z workerami,
- jak nie pomylić narzędzia z problemem, który chcesz rozwiązać.

To bardzo ważny dział, bo nowoczesny Python bardzo często styka się z:

- HTTP,
- bazami danych,
- zewnętrznymi API,
- workerami w tle,
- większą liczbą zadań wykonywanych „naraz”.

---

## Co powinieneś rozumieć po tym dziale

Po przerobieniu tego folderu powinieneś rozumieć:

- czym są `async` i `await`,
- jak działa `asyncio`,
- czym jest event loop,
- czym są coroutine, taski i futures,
- jak robić async HTTP,
- kiedy `threading` ma sens,
- co zmienia GIL,
- kiedy `multiprocessing` jest lepsze od wątków,
- jak działa `concurrent.futures`,
- po co istnieją systemy kolejkowe takie jak RabbitMQ, Celery i Kafka,
- jak dobrać model współbieżności do typu problemu.

---

## Dlaczego ten dział jest ważny

W pewnym momencie program przestaje być prostym sekwencyjnym skryptem.

Zaczyna:

- czekać na sieć,
- obsługiwać wiele żądań,
- robić kilka rzeczy obok siebie,
- delegować pracę do tła,
- wykorzystywać wiele rdzeni.

Wtedy pojawiają się pytania architektoniczne.

I właśnie ten dział ma Ci dać porządną mapę:

- async do I/O,
- wątki do części zadań blokujących i integracji,
- procesy do CPU-bound,
- kolejki do zadań tła i systemów rozproszonych.

---

## Jak czytać ten dział

Najlepiej iść po kolei:

1. [01-async-await-w-praktyce-python.md](/home/kacper/Desktop/Python_naprawiony/12.%20Asynchroniczno%C5%9B%C4%87%20i%20wielow%C4%85tkowo%C5%9B%C4%87/01-async-await-w-praktyce-python.md)
2. [02-asyncio-event-loop-tasks-futures-python.md](/home/kacper/Desktop/Python_naprawiony/12.%20Asynchroniczno%C5%9B%C4%87%20i%20wielow%C4%85tkowo%C5%9B%C4%87/02-asyncio-event-loop-tasks-futures-python.md)
3. [03-http-async-aiohttp-httpx-python.md](/home/kacper/Desktop/Python_naprawiony/12.%20Asynchroniczno%C5%9B%C4%87%20i%20wielow%C4%85tkowo%C5%9B%C4%87/03-http-async-aiohttp-httpx-python.md)
4. [04-wielowatkowosc-threading-python.md](/home/kacper/Desktop/Python_naprawiony/12.%20Asynchroniczno%C5%9B%C4%87%20i%20wielow%C4%85tkowo%C5%9B%C4%87/04-wielowatkowosc-threading-python.md)
5. [05-wieloprocesowosc-multiprocessing-python.md](/home/kacper/Desktop/Python_naprawiony/12.%20Asynchroniczno%C5%9B%C4%87%20i%20wielow%C4%85tkowo%C5%9B%C4%87/05-wieloprocesowosc-multiprocessing-python.md)
6. [06-narzedzia-kolejkujace-rabbitmq-celery-kafka-python.md](/home/kacper/Desktop/Python_naprawiony/12.%20Asynchroniczno%C5%9B%C4%87%20i%20wielow%C4%85tkowo%C5%9B%C4%87/06-narzedzia-kolejkujace-rabbitmq-celery-kafka-python.md)
7. [07-concurrent-futures-python.md](/home/kacper/Desktop/Python_naprawiony/12.%20Asynchroniczno%C5%9B%C4%87%20i%20wielow%C4%85tkowo%C5%9B%C4%87/07-concurrent-futures-python.md)

Ta kolejność ma sens:

- najpierw rozumiesz model async,
- potem mechanikę `asyncio`,
- potem praktyczne async HTTP,
- potem przechodzisz do wątków,
- potem do procesów,
- potem do prostego, wygodnego interfejsu executorów,
- a na końcu do kolejek i systemów rozproszonych.

---

## Jak pracować z tym działem

Najlepszy sposób nauki:

1. przeczytaj jeden plik,
2. uruchom wszystkie przykłady,
3. przewiduj output przed uruchomieniem,
4. porównuj wersję sekwencyjną i współbieżną,
5. zmieniaj przykłady samodzielnie,
6. dopiero potem przechodź do ćwiczeń.

To bardzo ważne, bo w tym dziale samo czytanie często daje złudzenie zrozumienia.

Współbieżność trzeba zobaczyć w działaniu.

---

## Na co szczególnie uważać

Najczęstsze pułapki:

- mylenie async z równoległością na wielu rdzeniach,
- używanie `async` tam, gdzie nie ma realnego I/O,
- próba przyspieszania CPU-bound kodu przez `threading`,
- ignorowanie GIL,
- brak rozumienia, kiedy zadanie powinno iść do procesu, a kiedy do kolejki,
- traktowanie RabbitMQ, Celery i Kafki jak rzeczy zamienne 1:1.

---

## Po czym poznać, że temat zaczyna siedzieć

Dobry znak, jeśli potrafisz:

- wyjaśnić różnicę między `async`, wątkiem i procesem,
- wskazać, kiedy `asyncio.gather()` daje sensowny zysk,
- opisać, czym jest event loop,
- powiedzieć, czemu GIL ma znaczenie dla CPU-bound,
- wyjaśnić, kiedy worker kolejki jest lepszy niż wykonanie pracy w żądaniu HTTP,
- dobrać narzędzie do konkretnego scenariusza zamiast zgadywać.

---

## Co ten dział daje w praktyce

Po opanowaniu tego folderu dużo lepiej zrozumiesz:

- nowoczesne backendy async,
- asynchroniczne integracje HTTP,
- zadania w tle,
- przetwarzanie równoległe,
- architektury rozproszone.

To jest dział, który mocno poszerza horyzont poza „piszę funkcję i ją wywołuję”.

---

## Ćwiczenia

Do tego działu masz też [ZESTAW-CWICZEN.md](/home/kacper/Desktop/Python_naprawiony/12.%20Asynchroniczno%C5%9B%C4%87%20i%20wielow%C4%85tkowo%C5%9B%C4%87/ZESTAW-CWICZEN.md).

Najlepiej:

- najpierw zrobić async basics,
- potem `asyncio` i HTTP,
- dopiero później wątki i procesy,
- a na końcu część kolejkową i bardziej architektoniczną.

---

## Co dalej

Po tym dziale naturalny następny krok to:

- [13. Web i API](/home/kacper/Desktop/Python_naprawiony/13.%20Web%20i%20API)
- albo [14. Bazy danych](/home/kacper/Desktop/Python_naprawiony/14.%20Bazy%20danych)

Bo właśnie tam bardzo często wykorzystujesz rzeczy z tego folderu w praktyce.
