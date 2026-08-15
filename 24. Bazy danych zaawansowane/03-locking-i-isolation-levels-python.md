# Locking i isolation levels python

## O czym jest ten rozdział

To temat, który długo wydaje się teoretyczny, dopóki system nie zacznie pracować współbieżnie.

W aplikacji webowej bardzo szybko pojawia się sytuacja:

- dwa requesty dotykają tych samych danych,
- jedna transakcja czyta, druga aktualizuje,
- wynik zaczyna zależeć od kolejności i czasu,
- pojawiają się dziwne błędy albo niespójności.

Żeby to rozumieć, trzeba znać dwie rzeczy:

- locki,
- poziomy izolacji transakcji.

## Najprostsza intuicja locka

Lock to mechanizm, który ogranicza jednoczesny dostęp do danych w taki sposób, żeby baza mogła utrzymać spójność.

Najprostsza intuicja:

- ktoś "trzyma" fragment danych na czas operacji,
- inni muszą poczekać albo działają według określonych zasad.

## Po co locki istnieją

Bez nich dwa równoległe działania mogłyby sobie wejść w drogę.

Przykład:

- dwa requesty próbują pobrać ten sam limitowany zasób,
- oba czytają stan "została 1 sztuka",
- oba próbują odjąć 1,
- kończysz z wynikiem niezgodnym z rzeczywistością.

## Przykład intuicyjny bez bazy

```python
balance = 100


def withdraw(amount: int):
    global balance
    if balance >= amount:
        balance = balance - amount


withdraw(80)
withdraw(30)
print(balance)
```

Tu przykład jest sekwencyjny, ale przy współbieżności bardzo podobny kod może prowadzić do problemów typu lost update albo niespójny stan.

## Lost update: jedna z najważniejszych intuicji

Wyobraź sobie dwie transakcje:

- T1 czyta `stock = 10`,
- T2 czyta `stock = 10`,
- T1 zapisuje `stock = 9`,
- T2 też zapisuje `stock = 9`.

Realnie sprzedano 2 sztuki, ale stan spadł tylko o 1.

To klasyczny problem współbieżności.

## Transakcja: przypomnienie praktyczne

Transakcja grupuje operacje, które powinny być traktowane jako jedna logiczna całość.

Najczęściej myślisz o niej tak:

- albo wszystko się uda,
- albo nic się nie zapisze.

Ale w praktyce ważne jest też to, jak transakcja widzi dane innych transakcji.

## Poziomy izolacji: po co są

Poziom izolacji określa, jak bardzo jedna transakcja jest odseparowana od innych.

Czyli między innymi:

- co może zobaczyć,
- kiedy widzi zmiany innych,
- jakie anomalie są dopuszczalne.

To nie jest temat "akademicki". To temat o tym, jakie dziwne rzeczy mogą się zdarzyć w produkcji.

## Najważniejsze anomalie, które warto znać intuicyjnie

### Dirty read

Transakcja czyta dane, które inna transakcja jeszcze nie zatwierdziła.

Jeśli tamta transakcja zrobi rollback, pierwsza przeczytała coś, co w gruncie rzeczy nigdy nie powinno istnieć jako trwały stan.

### Non-repeatable read

W tej samej transakcji czytasz ten sam rekord dwa razy i dostajesz różne wyniki, bo inna transakcja zmieniła dane między odczytami.

### Phantom read

W tej samej transakcji wykonujesz podobne query dwa razy, a za drugim razem pojawiają się dodatkowe rekordy spełniające warunek.

## Read committed: intuicja

To bardzo częsty poziom izolacji.

Najprościej:

- czytasz tylko dane już zatwierdzone,
- ale między dwoma odczytami inna transakcja może coś zmienić.

Czyli dirty read zwykle odpada, ale część innych anomalii nadal może się pojawić.

## Repeatable read: intuicja

Tu transakcja stara się zapewnić większą stabilność odczytu.

Najprościej myśląc:

- jeśli już coś przeczytałeś, ten odczyt ma być bardziej powtarzalny w obrębie transakcji.

W zależności od silnika bazy szczegóły mogą się różnić, ale intuicja jest taka: izolacja jest silniejsza niż przy `read committed`.

## Serializable: intuicja

To bardzo silny poziom izolacji.

Najprościej:

- system zachowuje się tak, jakby transakcje były wykonywane jedna po drugiej, a nie równolegle.

Zaleta:

- najmniej anomalii.

Koszt:

- większe ryzyko blokowania, retry i spadku przepustowości.

## Locking a wydajność

To bardzo ważne napięcie projektowe.

Silniejsza kontrola współbieżności daje większą spójność, ale może kosztować:

- czekanie,
- większą liczbę konfliktów,
- wolniejsze requesty,
- mniejszą przepustowość.

Dlatego nie wybiera się poziomu izolacji tylko z myślą "najmocniejszy = najlepszy".

## Mini case study: stan magazynowy

Masz endpoint kupna produktu.

Przepływ:

1. odczytaj `stock`,
2. sprawdź czy `stock > 0`,
3. zmniejsz `stock`,
4. zapisz wynik.

Przy współbieżnych requestach to klasyczne miejsce problemów.

Bez odpowiedniego modelu współbieżności możesz:

- sprzedać za dużo,
- zgubić aktualizację,
- wejść w konflikt między transakcjami.

## Kiedy lock może być potrzebny

Lock bywa potrzebny, gdy:

- czytasz i zaraz modyfikujesz ten sam rekord,
- chcesz uniknąć równoległego przetwarzania tej samej pracy,
- jedna operacja musi mieć wyraźny wyłączny dostęp przez chwilę.

## Kiedy zbyt szerokie lockowanie szkodzi

Jeśli lockujesz za dużo albo za długo, możesz mieć:

- kolejki oczekiwania,
- timeouty,
- spadek wydajności,
- większe ryzyko deadlocków.

## Before/after: myślenie niedojrzałe i dojrzalsze

### Niedojrzałe myślenie

- "przecież to tylko update jednego rekordu"

### Dojrzalsze myślenie

- "czy dwa requesty mogą wejść tu jednocześnie i zepsuć stan?"

## Co Pythonowiec powinien umieć praktycznie

Dobrze, żebyś umiał:

- rozpoznać, że problem jest współbieżnościowy, a nie tylko "losowy",
- kojarzyć pojęcia lost update, lock, isolation,
- rozumieć, że transakcja to nie tylko commit/rollback,
- wiedzieć, że wyższa izolacja ma koszt,
- szukać miejsc, gdzie dwa requesty operują na tych samych danych.

## Output myślowy

### Bez świadomości współbieżności

- test lokalny działa,
- produkcja czasem daje dziwne wyniki,
- błąd trudno odtworzyć.

### Ze świadomością współbieżności

- patrzysz na krytyczne sekcje danych,
- przewidujesz konflikty,
- dobierasz model transakcji i blokowania bardziej świadomie.

## Najważniejsze do zapamiętania

- Locki pomagają utrzymać spójność przy współbieżnym dostępie.
- Poziomy izolacji określają, jak transakcje widzą się nawzajem.
- Wyższa izolacja zwykle daje większą spójność, ale też koszt.
- Problemy współbieżności często ujawniają się dopiero pod obciążeniem.
- Transakcja to nie tylko "wszystko albo nic", ale też zasady widoczności danych.

## Ćwiczenia

1. Wyjaśnij własnymi słowami, czemu dwa równoległe requesty mogą zepsuć stan nawet przy prostym update.
2. Opisz intuicyjnie różnicę między `read committed` i `serializable`.
3. Podaj przykład lost update w systemie zamówień albo magazynu.
4. Wypisz dwa koszty zbyt agresywnego lockowania.
5. Wskaż w przykładowym flow aplikacji miejsce, gdzie sprawdziłbyś ryzyko konfliktu współbieżności.
