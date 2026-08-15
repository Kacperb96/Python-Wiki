# Case study: moduł orders, indeksy, paginacja i współbieżność

## Po co ten plik

Ten plik spina cały folder 24 w jedną praktyczną całość.

Nie chodzi już o pojedyncze pojęcia, tylko o odpowiedź na pytanie:

- jak te wszystkie decyzje łączą się w jednym realnym module?

Tu zobaczysz razem:

- model danych,
- query,
- indeksy,
- paginację,
- konflikty współbieżności,
- soft delete,
- historię zmian,
- wzorce pracy z bazą w produkcji.

## Mini system

Załóżmy moduł `orders` w sklepie internetowym.

System ma obsługiwać:

- listę zamówień użytkownika,
- listę zamówień dla supportu,
- zmianę statusu zamówienia,
- anulowanie zamówienia,
- historię zmian statusów,
- ukrywanie logicznie usuniętych rekordów,
- duży ruch i równoległe operacje.

## Podstawowe tabele

Najprostszy sensowny model może wyglądać tak:

- `users`
- `orders`
- `order_items`
- `order_status_history`
- `audit_log`

### Przykładowe kolumny `orders`

- `id`
- `user_id`
- `status`
- `total_amount`
- `created_at`
- `updated_at`
- `deleted_at`

### Przykładowe kolumny `order_status_history`

- `id`
- `order_id`
- `old_status`
- `new_status`
- `changed_by`
- `changed_at`

## Najczęstsze query w systemie

Załóżmy, że system naprawdę najczęściej robi takie rzeczy:

1. pobiera ostatnie zamówienia użytkownika,
2. filtruje listę zamówień supportu po statusie,
3. pobiera szczegóły jednego zamówienia,
4. zmienia status zamówienia,
5. zapisuje historię statusów,
6. ukrywa logicznie usunięte rekordy.

To ważne, bo indeksów i modelu nie dobiera się do pięknej teorii, tylko do realnych query.

## Query 1: lista zamówień użytkownika

```sql
SELECT id, status, total_amount, created_at
FROM orders
WHERE user_id = 42 AND deleted_at IS NULL
ORDER BY created_at DESC
LIMIT 20;
```

### Co tu jest ważne

- filtr po `user_id`,
- filtr po `deleted_at IS NULL`,
- sortowanie po `created_at DESC`,
- mały `LIMIT`,
- to prawdopodobnie hot path.

### Kandydat na indeks

W praktyce można myśleć o indeksie wspierającym ten wzorzec dostępu, np. takim, który pomaga po:

- `user_id`,
- stanie aktywności rekordu,
- porządku czasu.

Najważniejsza lekcja:

- indeks powinien wspierać realny filtr i realny porządek odczytu.

## Query 2: lista supportu po statusie

```sql
SELECT id, user_id, status, total_amount, created_at
FROM orders
WHERE status = 'paid' AND deleted_at IS NULL
ORDER BY created_at DESC
LIMIT 50;
```

Tu znowu ważne są:

- filtr po `status`,
- ignorowanie rekordów usuniętych logicznie,
- sortowanie po czasie,
- częste wykonania w panelu operacyjnym.

## Query 3: szczegóły zamówienia

```sql
SELECT *
FROM orders
WHERE id = 981 AND deleted_at IS NULL;
```

To query zwykle jest prostsze i bardziej punktowe.

Tu najczęściej główną rolę gra klucz główny, ale nadal trzeba pamiętać o logice soft delete.

## Before/after: zły i lepszy model odczytu listy

### Słabsza wersja

```sql
SELECT *
FROM orders
WHERE user_id = 42
ORDER BY created_at DESC
LIMIT 20 OFFSET 5000;
```

Problemy:

- `SELECT *` może czytać za dużo,
- duży `OFFSET` robi się kosztowny,
- brak warunku `deleted_at IS NULL` może dać złe wyniki,
- przy wzroście danych dalsze strony będą coraz cięższe.

### Lepsza wersja

```sql
SELECT id, status, total_amount, created_at
FROM orders
WHERE user_id = 42
  AND deleted_at IS NULL
  AND (created_at, id) < ('2026-08-15 12:00:00', 981)
ORDER BY created_at DESC, id DESC
LIMIT 20;
```

Zalety:

- pobierasz tylko potrzebne kolumny,
- masz bardziej stabilny porządek,
- używasz keyset pagination zamiast dużego `OFFSET`,
- uwzględniasz soft delete.

## Paginacja: decyzja produktowa i techniczna

### Dla użytkownika końcowego

Lista "moje zamówienia" często dobrze pasuje do keyset pagination, bo:

- użytkownik zwykle przewija kolejne rekordy,
- nie potrzebuje skakać na stronę 184,
- stabilność i wydajność są ważniejsze niż numer strony.

### Dla panelu admina

Tu decyzja bywa bardziej złożona.

Czasem:

- numerowane strony są wygodne UX-owo,
- ale duże `OFFSET` robią się drogie,
- więc trzeba świadomie ocenić kompromis.

## Współbieżność: zmiana statusu zamówienia

Załóżmy, że dwa procesy próbują zmienić status tego samego zamówienia.

### Ryzyko

- jeden operator ustawia `paid`,
- drugi niemal równocześnie ustawia `cancelled`,
- historia zmian robi się dziwna,
- stan końcowy może zależeć od kolejności.

## Słabszy przepływ

1. odczytaj zamówienie,
2. policz logikę,
3. zapisz nowy status,
4. dopisz historię,
5. zrób jeszcze dodatkowe rzeczy w tej samej transakcji.

To zwiększa ryzyko:

- długich locków,
- konfliktów,
- deadlocków,
- trudniejszego debugowania.

## Lepszy przepływ

1. przygotuj wszystko, co możesz, przed transakcją,
2. w transakcji zablokuj tylko potrzebny rekord,
3. sprawdź aktualny status,
4. wykonaj zmianę,
5. dopisz historię,
6. zakończ transakcję,
7. cięższe akcje uboczne zrób później.

## Gdzie może pojawić się deadlock

Wyobraź sobie dwa procesy:

- jeden aktualizuje `orders`, potem `order_status_history`,
- drugi najpierw dotyka `order_status_history`, a potem `orders`.

Jeśli oba trzymają locki i wejdą na siebie w złej kolejności, ryzyko deadlocka rośnie.

Najważniejsza lekcja:

- spójna kolejność dotykania zasobów ma znaczenie nawet wtedy, gdy mówimy o "prostym" module zamówień.

## Soft delete w tym module

Załóżmy, że anulowane albo ukryte zamówienia nie powinny znikać fizycznie.

Wtedy:

- `deleted_at IS NULL` pojawia się w normalnych query,
- historia zamówienia zostaje,
- support może nadal analizować przeszłe zdarzenia,
- system nie gubi kontekstu biznesowego.

Ale koszt jest realny:

- trzeba pamiętać o filtrze prawie wszędzie,
- indeksy i query muszą brać ten model pod uwagę.

## Audit log i historia statusów

Dwa różne poziomy historii mogą współistnieć.

### `order_status_history`

Służy do historii domenowej konkretnego zamówienia.

### `audit_log`

Służy do szerszego śladu operacyjnego:

- kto zmienił coś w systemie,
- kiedy,
- jaką akcję wykonał.

To rozróżnienie pomaga utrzymać porządek.

## Większy case study: zwalniająca lista zamówień

Objaw:

- pierwsze strony listy zamówień działają dobrze,
- dalsze strony są dużo wolniejsze,
- support raportuje czasem duplikaty albo "przeskakiwanie" rekordów.

### Hipoteza 1

Za duży koszt `OFFSET`.

### Hipoteza 2

Brak stabilnego porządku przy paginacji.

### Hipoteza 3

Brak indeksu dopasowanego do realnego wzorca filtrowania i sortowania.

### Rozsądna poprawka

- przejście na keyset pagination dla gorących ścieżek,
- jawne `ORDER BY created_at DESC, id DESC`,
- pobieranie tylko potrzebnych kolumn,
- lepsze dopasowanie indeksu do filtra i sortowania.

## Większy case study: sporadyczne konflikty statusów

Objaw:

- rzadkie błędy przy równoczesnych zmianach,
- czasem dziwna kolejność w historii,
- czasem rollback transakcji.

### Możliwe przyczyny

- zbyt długa transakcja,
- różna kolejność dotykania tabel,
- brak jasnej strategii blokowania rekordu zamówienia,
- mieszanie ciężkiej logiki z częścią krytyczną transakcji.

### Rozsądna poprawka

- skrócić transakcję,
- spójnie dotykać tych samych zasobów,
- logikę uboczną wyciągnąć poza transakcję,
- dodać sensowny retry tylko tam, gdzie to bezpieczne.

## Jak dobrać poziomy testów do tego modułu

### Unit

Testuj:

- reguły zmiany statusu,
- walidację przejść statusów,
- budowanie parametrów paginacji,
- logikę filtrowania aktywnych rekordów.

### Integration

Testuj:

- query listy zamówień z paginacją,
- zapis historii statusu,
- działanie soft delete,
- transakcję zmiany statusu.

### E2E

Testuj:

- użytkownik widzi własne zamówienia w poprawnej kolejności,
- support zmienia status i historia jest widoczna,
- usunięte logicznie rekordy nie wracają w zwykłych widokach.

## Co ten case study pokazuje

Najważniejsza lekcja:

- indeksy, paginacja, współbieżność i historia danych nie są osobnymi tematami,
- one spotykają się dokładnie w tych samych endpointach i query.

To dlatego dojrzała praca z bazą wymaga patrzenia na cały moduł, a nie tylko na pojedyncze zapytanie.

## Najważniejsze do zapamiętania

- Projektuj pod realne query, nie pod ładny schemat w oderwaniu od użycia.
- Paginacja i indeksy muszą pasować do rzeczywistego wzorca odczytu.
- Soft delete wpływa na query, indeksy i widoki danych.
- Zmiany statusów to nie tylko update, ale też historia i współbieżność.
- Najlepsze decyzje bazodanowe wychodzą z patrzenia na cały flow modułu.

## Ćwiczenia

1. Zaprojektuj własną wersję tabel dla modułu `orders`.
2. Wskaż, które query w tym module byłyby hot pathem.
3. Opisz, gdzie użyłbyś offset pagination, a gdzie keyset.
4. Wymień dwa miejsca, gdzie może dojść do konfliktu współbieżności.
5. Rozpisz, jakie indeksy rozważyłbyś najpierw i dlaczego.
