# Zestaw ćwiczeń praktycznych — 05. Dekoratory

## Poziom 1 — funkcje i closures

1. Napisz funkcję, która przyjmuje inną funkcję i ją wywołuje.
2. Napisz funkcję zwracającą inną funkcję.
3. Zbuduj closure, która „pamięta” przekazany prefiks i dokleja go do tekstu.
4. Zbuduj closure liczące kolejne wywołania.

## Poziom 2 — pierwszy dekorator

5. Napisz prosty dekorator wypisujący komunikat przed wywołaniem funkcji.
6. Rozszerz go o komunikat po wywołaniu funkcji.
7. Napisz dekorator mierzący czas wykonania funkcji.
8. Napisz dekorator logujący nazwę funkcji i argumenty.

## Poziom 3 — argumenty i `wraps`

9. Napisz dekorator działający na funkcjach z dowolnymi argumentami.
10. Dodaj `*args` i `**kwargs` do dekoratora logującego.
11. Użyj `functools.wraps` i pokaż różnicę względem dekoratora bez `wraps`.
12. Napisz dekorator, który blokuje wykonanie funkcji przy spełnionym warunku.

## Poziom 4 — dekoratory z argumentami

13. Napisz dekorator `repeat(n)`, który wywołuje funkcję `n` razy.
14. Napisz dekorator `prefix(text)`, który dodaje prefiks do wypisywanego komunikatu.
15. Napisz dekorator `retry(times=3)` symulujący ponowne wykonanie przy wyjątku.

## Poziom 5 — praktyczne zastosowania

16. Napisz dekorator cache'ujący wyniki funkcji w prostym słowniku.
17. Napisz dekorator sprawdzający, czy użytkownik jest zalogowany, zanim wykona funkcję.
18. Napisz dekorator walidujący, że argument liczbowy jest dodatni.
19. Zbuduj dekorator klasowy do logowania tworzenia instancji.
20. Napisz dekorator do prostego rate limitingu w obrębie jednego procesu.

## Zadanie końcowe

21. Zbuduj mini zestaw dekoratorów dla małej aplikacji:
   - `@log_calls`
   - `@measure_time`
   - `@require_positive`
   - `@cache_result`
   - `@retry`

Użyj ich na kilku funkcjach i pokaż, że rozumiesz kolejność, `wraps`, argumenty i skutki uboczne.
