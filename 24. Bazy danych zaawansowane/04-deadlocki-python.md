# Deadlocki python

## O czym jest ten rozdział

Deadlock to jeden z tych problemów bazodanowych, które brzmią groźnie i niestety naprawdę potrafią boleć w produkcji.

Najczęściej objawia się to tak:

- request nagle długo wisi,
- część transakcji kończy się błędem,
- problem pojawia się tylko czasami,
- lokalnie prawie nie da się go odtworzyć,
- pod większym ruchem zaczyna wracać.

Żeby rozumieć deadlocki, trzeba najpierw mieć prostą intuicję o lockach i kolejności dostępu do danych.

## Najprostsza intuicja deadlocka

Deadlock pojawia się wtedy, gdy dwie transakcje czekają na siebie nawzajem i żadna nie może ruszyć dalej.

Bardzo prosty obraz:

- transakcja A trzyma zasób 1 i czeka na zasób 2,
- transakcja B trzyma zasób 2 i czeka na zasób 1.

Obie stoją.

## Przykład myślowy

Wyobraź sobie dwa rekordy:

- konto `A`,
- konto `B`.

Dwie transakcje robią przelewy:

### Transakcja T1

1. lockuje konto `A`,
2. chce zablokować konto `B`.

### Transakcja T2

1. lockuje konto `B`,
2. chce zablokować konto `A`.

Jeśli obie wykonają się w złym momencie, masz klasyczny deadlock.

## Dlaczego baza nie może czekać w nieskończoność

Gdyby system nic z tym nie zrobił, transakcje mogłyby wisieć bez końca.

Dlatego baza zwykle wykrywa deadlock i wybiera jedną transakcję jako ofiarę.

Efekt praktyczny:

- jedna transakcja jest przerywana,
- druga może dokończyć pracę.

To dlatego w aplikacji widzisz czasem błąd deadlocka zamiast wiecznego oczekiwania.

## To nie jest po prostu "wolna baza"

To ważne rozróżnienie.

Wolne query i deadlock to nie to samo.

### Wolne query

- może długo liczyć,
- może skanować dużo danych,
- może zużywać CPU lub IO.

### Deadlock

- dotyczy wzajemnego blokowania transakcji,
- wynika z konfliktu kolejności dostępu,
- kończy się zwykle błędem i rollbackiem jednej transakcji.

## Najczęstszy wzorzec prowadzący do deadlocka

Najczęściej problem pojawia się wtedy, gdy różne ścieżki kodu lockują te same zasoby w różnej kolejności.

Przykład:

- ścieżka A: najpierw `users`, potem `orders`,
- ścieżka B: najpierw `orders`, potem `users`.

Pod współbieżnością to bardzo ryzykowny układ.

## Before/after

### Słabszy wzorzec

- różne fragmenty systemu dotykają tych samych tabel w różnej kolejności,
- transakcje są długie,
- dużo logiki dzieje się w obrębie jednej transakcji.

### Lepszy wzorzec

- kolejność dostępu do zasobów jest spójna,
- transakcje są możliwie krótkie,
- poza transakcją wynosisz to, co nie musi trzymać locków.

## Mini case study: dwa transfery

Masz funkcję przelewu między kontami.

### Zły pomysł

Dla przelewu `A -> B` lockujesz najpierw `A`, potem `B`.
Dla przelewu `B -> A` lockujesz najpierw `B`, potem `A`.

Pod współbieżnością łatwo o deadlock.

### Lepszy pomysł

Zawsze lockujesz konta w tej samej kolejności, np. po rosnącym `account_id`.

Wtedy:

- niezależnie od kierunku biznesowego operacji,
- techniczna kolejność blokowania jest stała.

To bardzo klasyczna technika ograniczania deadlocków.

## Co zwiększa ryzyko deadlocków

- różna kolejność lockowania rekordów,
- długie transakcje,
- wiele aktualizacji w jednej transakcji,
- mieszanie odczytów, update'ów i dodatkowej logiki w jednym dużym bloku,
- wysoki poziom współbieżności,
- nieprzewidywalne ścieżki biznesowe dotykające tych samych danych.

## Co zmniejsza ryzyko deadlocków

- spójna kolejność dostępu do zasobów,
- krótsze transakcje,
- mniejsza liczba lockowanych rekordów,
- odsuwanie pracy niebazodanowej poza transakcję,
- retry po błędach deadlocka tam, gdzie to bezpieczne,
- dobra obserwowalność i logi.

## Retry: ważna praktyka

Ponieważ jedna transakcja przy deadlocku zwykle jest wycofywana, aplikacja często może spróbować ponownie.

Ale retry ma sens tylko wtedy, gdy:

- operacja jest bezpieczna do powtórzenia,
- wiesz, że nie robisz przez to dubli logiki biznesowej,
- masz kontrolę nad idempotencją.

## Pseudokod intuicyjny

```python
def transfer_money(from_id: int, to_id: int, amount: int):
    first_id, second_id = sorted([from_id, to_id])

    # najpierw blokuj w stałej kolejności technicznej
    first_account = lock_account(first_id)
    second_account = lock_account(second_id)

    # potem wykonaj logikę biznesową przelewu
    apply_transfer(from_id, to_id, amount)
```

Najważniejsza intuicja:

- kolejność techniczna blokowania może być inna niż kierunek biznesowy operacji.

## Objawy produkcyjne

Deadlocki często wyglądają tak:

- sporadyczne błędy przy wysokim ruchu,
- błędy tylko dla określonych operacji,
- czasem tylko o konkretnych godzinach,
- nieudane retry pojedynczych requestów,
- wzrost liczby rollbacków transakcji.

## Jak o tym myśleć jako Pythonowiec

Nie musisz analizować wewnętrznych mechanizmów silnika bazy na poziomie eksperta.

Ale dobrze, żebyś umiał:

- rozpoznać, że to może być deadlock, a nie zwykły timeout,
- sprawdzić, które ścieżki biznesowe dotykają tych samych rekordów,
- zapytać o kolejność lockowania,
- skrócić transakcję,
- dodać retry tam, gdzie to rozsądne.

## Output myślowy

### Bez świadomości deadlocków

- błąd wydaje się losowy,
- zespół szuka winy w frameworku albo sieci,
- problem wraca pod obciążeniem.

### Ze świadomością deadlocków

- patrzysz na kolejność zasobów,
- zawężasz ścieżki konfliktu,
- projektujesz transakcje ostrożniej.

## Najważniejsze do zapamiętania

- Deadlock to wzajemne blokowanie transakcji, a nie po prostu wolne zapytanie.
- Najczęstszą przyczyną jest różna kolejność lockowania tych samych zasobów.
- Baza zwykle przerywa jedną transakcję, żeby odblokować sytuację.
- Krótsze transakcje i spójna kolejność dostępu mocno pomagają.
- Retry po deadlocku bywa sensowne, ale tylko przy bezpiecznej logice.

## Ćwiczenia

1. Wyjaśnij własnymi słowami, czym deadlock różni się od zwykiego wolnego query.
2. Opisz prosty przykład deadlocka na dwóch rekordach.
3. Wypisz trzy rzeczy, które zwiększają ryzyko deadlocków.
4. Wyjaśnij, czemu spójna kolejność lockowania jest tak ważna.
5. Opisz, kiedy retry po deadlocku ma sens, a kiedy może być niebezpieczne.
