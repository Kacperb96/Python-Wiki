# Soft delete i audit log python

## O czym jest ten rozdział

Nie każdą daną w systemie można po prostu usunąć na twardo.

W realnych aplikacjach bardzo szybko pojawiają się pytania:

- czy użytkownik naprawdę znika z systemu,
- czy zamówienie da się skasować bez śladu,
- jak odtworzyć historię zmian,
- kto zmienił dany rekord i kiedy,
- jak pogodzić wygodę operacyjną z historią i wymaganiami biznesowymi.

Tu pojawiają się dwa bardzo ważne wzorce:

- soft delete,
- audit log.

## Soft delete: najprostsza intuicja

Soft delete oznacza, że rekord nie jest fizycznie usuwany z tabeli, tylko oznaczany jako usunięty.

Najczęściej przez pola typu:

- `deleted_at`,
- `is_deleted`,
- `deleted_by`.

Najprostsza intuicja:

- rekord nadal jest w bazie,
- ale normalna logika aplikacji traktuje go jako niewidoczny.

## Przykład

Zamiast:

```sql
DELETE FROM users WHERE id = 42;
```

robisz coś w stylu:

```sql
UPDATE users
SET deleted_at = NOW()
WHERE id = 42;
```

## Po co soft delete ma sens

Soft delete ma sens, gdy:

- chcesz możliwość przywrócenia danych,
- potrzebujesz historii operacyjnej,
- rekordy są powiązane z innymi danymi,
- twarde usunięcie mogłoby zniszczyć kontekst biznesowy,
- użytkownik "usuwa" coś funkcjonalnie, ale system nadal potrzebuje śladu.

## Typowe przykłady

- konto użytkownika,
- produkt wycofany z oferty,
- zamówienie ukryte z interfejsu,
- rekord biznesowy, którego historia nadal ma znaczenie.

## Największa pułapka soft delete

Największy problem brzmi:

- trzeba pamiętać o filtrowaniu usuniętych rekordów wszędzie tam, gdzie nie powinny się pokazywać.

Jeśli o tym zapomnisz, możesz mieć bardzo dziwne bugi:

- "usunięty" użytkownik nadal pojawia się na liście,
- statystyki liczą rekordy, które miały zniknąć,
- walidacja unikalności przestaje być intuicyjna.

## Before/after

### Hard delete

- rekord znika fizycznie,
- mniej danych do utrzymania,
- mniej historii,
- trudniej coś odzyskać.

### Soft delete

- rekord zostaje,
- łatwiej zachować historię i relacje,
- trzeba pilnować filtrowania,
- model aplikacji staje się trochę bardziej złożony.

## Kiedy soft delete może być złym pomysłem

Soft delete nie jest zawsze najlepszy.

Może być złym pomysłem, gdy:

- dane naprawdę powinny zostać usunięte bez śladu,
- trzymanie dużej liczby martwych rekordów szkodzi wydajności,
- model biznesowy nie potrzebuje odzyskiwania ani historii,
- system robi się nadmiernie skomplikowany tylko po to, żeby "może kiedyś" coś przywrócić.

## Audit log: najprostsza intuicja

Audit log to zapis zdarzeń i zmian, który odpowiada na pytania:

- kto coś zrobił,
- co się zmieniło,
- kiedy to się stało,
- czasem także z jakiego kontekstu lub powodu.

To jest bardziej historia działań niż sam aktualny stan danych.

## Przykład wpisu audit logu

```text
2026-08-15 12:30:11 | user_id=42 | action=order_status_changed | order_id=981 | from=pending | to=paid
```

To może być osobna tabela, osobny strumień zdarzeń albo inny mechanizm historyczny.

## Po co audit log ma sens

Audit log pomaga, gdy chcesz:

- odtwarzać historię zmian,
- diagnozować błędy,
- wyjaśniać działania użytkowników i administratorów,
- spełniać wymagania operacyjne albo compliance,
- rozumieć, skąd wziął się obecny stan systemu.

## Soft delete a audit log: to nie to samo

To bardzo ważne.

Soft delete mówi:

- rekord nie znika fizycznie.

Audit log mówi:

- zapisujemy historię zdarzeń i zmian.

Możesz mieć:

- soft delete bez pełnego audit logu,
- audit log bez soft delete,
- oba mechanizmy naraz.

## Mini case study

Masz system zamówień.

### Biznes chce:

- ukrywać zamówienia anulowane z części widoków,
- zachować historię zmian statusu,
- wiedzieć, który operator zmienił status.

Sensowny model może być taki:

- zamówienie nie jest usuwane twardo,
- statusy są zapisywane w historii,
- zmiany krytyczne trafiają do audit logu,
- główne query filtrują tylko rekordy aktywne, jeśli tak wymaga widok.

## Snapshot vs audit

To też ważne rozróżnienie.

Snapshot to często zapis stanu danych w określonym momencie.
Audit log to zwykle zapis zdarzenia lub zmiany.

Przykład:

- snapshot adresu dostawy przy zamówieniu,
- audit log: kto i kiedy zmienił status zamówienia.

To są różne potrzeby.

## Najczęstsze pułapki

### 1. Dodanie soft delete bez spójnego filtrowania

To najczęstszy problem.

### 2. Audit log pełen zbyt mało użytecznych wpisów

Jeśli zapisujesz wszystko bez sensu, trudno potem znaleźć naprawdę ważne informacje.

### 3. Trzymanie za mało kontekstu

Audit log typu:

```text
action=updated
```

często jest prawie bezużyteczny.

### 4. Mieszanie danych operacyjnych z historią bez jasnych zasad

Po czasie trudno zrozumieć, co jest aktualnym stanem, a co historią.

### 5. Założenie, że soft delete rozwiązuje każdy problem historii

Nie.

Soft delete nie daje pełnego obrazu zmian w czasie.

## Co Pythonowiec powinien umieć praktycznie

Dobrze, żebyś umiał:

- ocenić, czy dany rekord nadaje się do soft delete,
- pamiętać, że soft delete wpływa na wszystkie query,
- rozumieć, kiedy potrzebny jest audit log,
- odróżnić historię zdarzeń od samego "rekord nadal istnieje",
- zapytać, jakie pytania biznes chce móc później zadać o historię systemu.

## Output myślowy

### Bez soft delete i bez historii

- system jest prostszy,
- ale mniej odwracalny i mniej wyjaśnialny.

### Soft delete bez dyscypliny

- rekordy niby znikają,
- ale w praktyce wracają w losowych miejscach systemu.

### Dobrze zaprojektowane podejście

- wiadomo, które dane są aktywne,
- wiadomo, co jest historią,
- wiadomo, które operacje da się odtworzyć i wyjaśnić.

## Najważniejsze do zapamiętania

- Soft delete to oznaczenie rekordu jako usuniętego, a nie fizyczne usunięcie.
- Audit log zapisuje historię działań i zmian.
- To dwa różne mechanizmy i często oba są potrzebne.
- Soft delete wymaga konsekwentnego filtrowania w całym systemie.
- Historia bez kontekstu szybko staje się mało użyteczna.

## Ćwiczenia

1. Wyjaśnij własnymi słowami różnicę między hard delete i soft delete.
2. Podaj przykład rekordu, dla którego soft delete ma sens, i taki, dla którego może nie mieć.
3. Opisz, jakie pola dodałbyś do prostego audit logu.
4. Wyjaśnij, czemu soft delete nie zastępuje pełnej historii zmian.
5. Zaprojektuj prosty model historii dla systemu zamówień.
