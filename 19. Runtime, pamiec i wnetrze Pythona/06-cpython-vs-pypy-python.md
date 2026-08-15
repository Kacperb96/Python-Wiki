# CPython vs PyPy w Pythonie

## O co chodzi

Wiele osób mówi po prostu "Python", jakby istniał jeden interpreter.

W praktyce masz różne implementacje języka Python.

Dwie najbardziej znane to:

- CPython,
- PyPy.

Najczęściej, gdy ktoś mówi "Python", ma na myśli właśnie CPython.

## CPython

To referencyjna i najpopularniejsza implementacja Pythona.

To właśnie z CPythonem związane są takie tematy jak:

- GIL w typowym sensie, o którym zwykle się mówi,
- reference counting w praktycznym modelu pamięci,
- większość domyślnych oczekiwań narzędzi i bibliotek.

To najczęściej używany interpreter w praktyce.

## PyPy

PyPy to alternatywna implementacja Pythona, znana m.in. z podejścia do wydajności i własnego sposobu wykonania.

Nie chodzi o to, że jeden jest "prawdziwy", a drugi nie. To po prostu różne implementacje tego samego języka z różnymi trade-offami.

## Dlaczego to ma znaczenie

Bo czasem mówimy o zachowaniu "Pythona", a tak naprawdę mówimy o zachowaniu konkretnego interpretera.

To bardzo ważne rozróżnienie.

## Najprostsza intuicja

Język Python to specyfikacja i sposób pisania kodu.

Interpreter to konkretna implementacja, która ten kod wykonuje.

Czyli:

- piszesz Python,
- ale uruchamiasz go na konkretnym interpreterze.

## Wydajność

Różne interpretery mogą różnić się:

- szybkością wykonania,
- zachowaniem pamięci,
- optymalizacjami,
- zgodnością z niektórymi bibliotekami,
- kosztami startu i działania w różnych scenariuszach.

To oznacza, że dwa interpretery mogą wykonywać ten sam program poprawnie, ale z inną charakterystyką wydajnościową.

## Kompatybilność ekosystemu

CPython ma zwykle najszersze wsparcie ekosystemu.

To ważne szczególnie wtedy, gdy projekt zależy od:

- rozszerzeń natywnych,
- konkretnych bibliotek niskopoziomowych,
- narzędzi testowanych głównie pod CPythonem.

W praktyce często właśnie dlatego CPython jest domyślnym wyborem.

## Czy PyPy jest po prostu "szybszy Python"

To zbyt proste uproszczenie.

Bywa szybszy w niektórych scenariuszach, ale nie chodzi o uniwersalne "zawsze lepiej".

Realna odpowiedź zależy od:

- rodzaju obciążenia,
- bibliotek,
- czasu życia procesu,
- charakteru aplikacji.

## Kiedy ta wiedza ma sens

Szczególnie gdy:

- interesuje Cię performance,
- porównujesz zachowanie kodu w różnych środowiskach,
- czytasz materiały o wnętrzu Pythona,
- próbujesz zrozumieć, że część właściwości przypisanych Pythonowi dotyczy w praktyce CPythona.

## Typowe błędy początkujących

- mylenie języka Python z konkretnym interpreterem,
- zakładanie, że każda implementacja zachowuje się identycznie pod każdym względem runtime i wydajności,
- przekonanie, że wiedza o GIL zawsze automatycznie opisuje każdy interpreter tak samo,
- ocenianie wydajności języka bez uwzględnienia interpretera.

## Co zapamiętać praktycznie

Na co dzień najczęściej pracujesz na CPythonie.

Ale warto wiedzieć, że:

- pewne zachowania są właściwością implementacji,
- nie wszystkiego nie można przypisywać "Pythonowi w ogóle",
- interpreter ma znaczenie dla performance i runtime behavior.

## Szybka ściąga

- CPython to najpopularniejsza implementacja Pythona,
- PyPy to alternatywna implementacja z innymi trade-offami,
- język i interpreter to nie to samo,
- wydajność i zachowanie runtime mogą zależeć od implementacji.

## Ćwiczenia

1. Wyjaśnij różnicę między językiem Python a interpreterem Python.
2. Opisz, czemu wydajność programu nie zależy wyłącznie od samej składni języka.
3. Wyjaśnij, czemu większość rozmów o GIL dotyczy przede wszystkim CPythona.
4. Zastanów się, kiedy w praktyce wybór interpretera mógłby mieć znaczenie.
5. Wypisz 3 rzeczy, które po tym rozdziale bardziej kojarzysz z implementacją niż z samym językiem.

## Najważniejsze do zapamiętania

- Python jako język i interpreter Pythona to nie to samo.
- Najczęściej używany interpreter to CPython.
- PyPy i inne implementacje mogą różnić się zachowaniem runtime i wydajnością.
- Wiele praktycznych tematów o "Pythonie" dotyczy tak naprawdę CPythona.
- Ta wiedza pomaga myśleć precyzyjniej o performance i wnętrzu języka.
