# Indeksy i query planning python

## O czym jest ten rozdział

To jeden z najważniejszych tematów przy pracy z bazą danych w prawdziwej aplikacji.

Na początku wszystko zwykle działa szybko, bo danych jest mało. Problem zaczyna się później:

- tabela rośnie,
- query robi się wolne,
- endpoint zaczyna odpowiadać coraz dłużej,
- CPU bazy rośnie,
- wszyscy mówią "trzeba zoptymalizować SQL".

Żeby to robić sensownie, trzeba rozumieć dwie rzeczy:

- jak działają indeksy,
- jak baza wybiera plan wykonania zapytania.

## Najprostsza intuicja o indeksie

Indeks to dodatkowa struktura danych, która pomaga szybciej znaleźć rekordy.

Najprostsza intuicja:

- bez indeksu baza często musi przejść przez bardzo dużo rekordów,
- z indeksem może zawęzić obszar szukania dużo szybciej.

To trochę jak różnica między:

- czytaniem całej książki, żeby znaleźć jedno nazwisko,
- a zajrzeniem do indeksu na końcu książki.

## Bez indeksu a z indeksem

Załóżmy tabelę `users` z kolumną `email`.

Query:

```sql
SELECT * FROM users WHERE email = 'jan@example.com';
```

### Bez indeksu

Baza może robić coś zbliżonego do:

- czytaj rekord po rekordzie,
- sprawdzaj `email`,
- zatrzymaj się po znalezieniu wyniku.

To zwykle nazywa się pełnym skanem tabeli.

### Z indeksem na `email`

Baza może szybciej dojść do pasującego rekordu, bo ma pomocniczą strukturę do wyszukiwania po tej kolumnie.

## Dlaczego indeks nie jest darmowy

To bardzo ważne.

Indeks pomaga przy odczycie, ale kosztuje przy:

- `INSERT`,
- `UPDATE`,
- `DELETE`,
- zajętości miejsca na dysku,
- utrzymaniu dodatkowych struktur.

Czyli indeks to nie jest magiczne "włącz szybciej".

To trade-off.

## Kiedy indeks często ma sens

Indeks często ma sens na kolumnach:

- po których filtrujesz,
- po których robisz `JOIN`,
- po których sortujesz,
- które są często używane w warunkach `WHERE`,
- które identyfikują rekordy w częstych query.

Przykłady:

- `email`,
- `user_id`,
- `created_at`,
- `status`,
- klucze obce.

## Kiedy indeks może nie dać wiele

Indeks może nie pomagać tak bardzo, gdy:

- tabela jest bardzo mała,
- kolumna ma bardzo małą selektywność,
- query i tak musi zwrócić bardzo dużą część tabeli,
- baza ocenia, że pełny skan będzie tańszy.

## Seletywność: intuicja

Seletywność mówi w uproszczeniu, jak dobrze dana kolumna odróżnia rekordy.

Przykład:

- `email` zwykle ma wysoką selektywność,
- `is_active` z wartościami `True/False` zwykle ma dużo niższą.

Jeśli prawie połowa tabeli ma `is_active = true`, to sam indeks na tej kolumnie nie zawsze daje wielką korzyść.

## Prosty przykład myślowy

Tabela ma 10 milionów rekordów.

Query 1:

```sql
SELECT * FROM users WHERE email = 'jan@example.com';
```

Tu indeks na `email` zwykle ma bardzo duży sens.

Query 2:

```sql
SELECT * FROM users WHERE is_active = true;
```

Jeśli 95% rekordów ma `is_active = true`, indeks może nie być tak pomocny, jak intuicyjnie się wydaje.

## Query planning: co to jest

Query planner to mechanizm bazy, który wybiera sposób wykonania zapytania.

Czyli baza nie tylko "odpala SQL", ale najpierw mniej więcej decyduje:

- jak czytać dane,
- którego indeksu użyć,
- w jakiej kolejności robić operacje,
- czy skanować tabelę, czy iść przez indeks.

To właśnie jest plan wykonania.

## Intuicja planu wykonania

Dla jednego query baza może mieć kilka możliwych strategii.

Planner wybiera tę, którą ocenia jako najtańszą.

Nie zawsze oznacza to idealny wybór, ale zwykle oznacza próbę minimalizacji kosztu.

## Przykład planu w wersji uproszczonej

Wyobraź sobie dwa możliwe plany dla query po `email`:

### Plan A

- full table scan,
- sprawdź każdy rekord.

### Plan B

- użyj indeksu po `email`,
- znajdź pasujące rekordy,
- pobierz pełny rekord.

Planner wybiera plan B, jeśli ocenia go jako tańszy.

## Co wpływa na plan

Baza może brać pod uwagę między innymi:

- dostępne indeksy,
- rozmiar tabeli,
- statystyki danych,
- przewidywaną liczbę pasujących rekordów,
- koszt sortowania,
- koszt joinów.

## Pseudo-EXPLAIN: jak czytać plan intuicyjnie

Nie chodzi o nauczenie się każdego szczegółu składni konkretnej bazy, tylko o prostą intuicję.

### Słaby plan

Query:

```sql
SELECT * FROM users WHERE email = 'jan@example.com';
```

Pseudo-EXPLAIN:

```text
Seq Scan on users
  Filter: email = 'jan@example.com'
  Rows scanned: 10_000_000
  Rows returned: 1
```

Interpretacja:

- baza czyta bardzo dużo rekordów,
- wynik jest mały,
- koszt jest nieproporcjonalny do celu.

### Lepszy plan

```text
Index Scan using idx_users_email on users
  Index condition: email = 'jan@example.com'
  Rows scanned: 1
  Rows returned: 1
```

Interpretacja:

- baza trafia dużo bliżej celu,
- praca jest bardziej proporcjonalna do zapytania,
- to zwykle sygnał dobrze dobranego indeksu.

## Before/after: punktowe wyszukiwanie

### Before

```sql
SELECT * FROM users WHERE email = 'jan@example.com';
```

bez indeksu.

### After

To samo query, ale z indeksem wspierającym wyszukiwanie po `email`.

Wniosek:

- samo SQL może wyglądać identycznie,
- a koszt wykonania może być radykalnie inny.

## Before/after: filtr i sortowanie

Masz query:

```sql
SELECT id, status, created_at
FROM orders
WHERE user_id = 42
ORDER BY created_at DESC
LIMIT 20;
```

### Słabszy wariant

Pseudo-EXPLAIN:

```text
Seq Scan on orders
  Filter: user_id = 42
  Sort: created_at DESC
  Rows scanned: 4_000_000
  Rows sorted: 18_000
  Rows returned: 20
```

Interpretacja:

- baza najpierw czyta bardzo dużo danych,
- potem jeszcze sortuje pasujące rekordy,
- mały wynik końcowy nie oznacza małego kosztu.

### Lepszy wariant

Pseudo-EXPLAIN:

```text
Index Scan using idx_orders_user_created_at on orders
  Index condition: user_id = 42
  Order satisfied by index
  Rows scanned: 20
  Rows returned: 20
```

Interpretacja:

- filtr i porządek odczytu wspierają się nawzajem,
- baza nie musi robić dużego dodatkowego sortowania,
- plan bardziej przypomina "weź dokładnie to, czego potrzebuję".

## Before/after: niski sens indeksu

Masz query:

```sql
SELECT * FROM users WHERE is_active = true;
```

Przy bardzo niskiej selektywności planner może nadal wybrać coś w tym stylu:

```text
Seq Scan on users
  Filter: is_active = true
  Rows scanned: 10_000_000
  Rows returned: 9_500_000
```

Interpretacja:

- nawet jeśli indeks istnieje,
- koszt dotarcia do ogromnej części tabeli może być podobny albo wyższy niż pełny skan.

To właśnie pokazuje, że indeks nie zawsze oznacza użycie indeksu.

## Before/after: duży OFFSET

Query:

```sql
SELECT id, created_at
FROM orders
ORDER BY created_at DESC
LIMIT 20 OFFSET 100000;
```

Pseudo-EXPLAIN intuicyjnie:

```text
Index Scan using idx_orders_created_at on orders
  Order satisfied by index
  Rows visited before return: 100020
  Rows returned: 20
```

Interpretacja:

- nawet jeśli indeks pomaga w porządku,
- duży `OFFSET` nadal zmusza bazę do przejścia przez dużą liczbę rekordów.

To jest pomost między planowaniem zapytań i tematem paginacji.

## Before/after: intuicja wydajności

### Wersja słabsza

```sql
SELECT * FROM orders WHERE user_id = 42;
```

bez indeksu na `user_id` w bardzo dużej tabeli.

### Lepsza wersja

to samo query, ale z dobrze dobranym indeksem na `user_id`.

Efekt praktyczny może być ogromny, szczególnie gdy endpoint odpala to query bardzo często.

## Indeksy złożone: intuicja

Czasem filtrujesz po więcej niż jednej kolumnie.

Przykład:

```sql
SELECT * FROM orders WHERE user_id = 42 AND status = 'paid';
```

Wtedy pojedyncze indeksy nie zawsze są najlepszą odpowiedzią.

Czasem sens ma indeks złożony, np.:

- `(user_id, status)`.

Ale tu zaczynają się ważne szczegóły projektowe:

- kolejność kolumn ma znaczenie,
- nie każdy indeks złożony pomaga wszystkim zapytaniom tak samo.

## Pseudo-EXPLAIN dla indeksu złożonego

Query:

```sql
SELECT id, total_amount
FROM orders
WHERE user_id = 42 AND status = 'paid';
```

Słabszy plan intuicyjnie:

```text
Bitmap/Filter plan
  Scan many rows for user_id
  Filter status afterward
  Rows scanned: 18_000
  Rows returned: 220
```

Lepszy plan intuicyjnie:

```text
Index Scan using idx_orders_user_status on orders
  Index condition: user_id = 42 AND status = 'paid'
  Rows scanned: 220
  Rows returned: 220
```

Najważniejsza myśl:

- im bliżej indeks odpowiada realnemu warunkowi zapytania, tym mniejszy koszt dodatkowego filtrowania.

## Najczęstsze pułapki z indeksami

### 1. Indeksowanie wszystkiego

To bardzo częsty odruch.

Problem:

- baza więcej kosztuje przy zapisach,
- rośnie rozmiar danych,
- system staje się cięższy,
- część indeksów i tak będzie mało użyteczna.

### 2. Brak indeksu na kolumnie często używanej w joinach

To bardzo częsty problem wydajnościowy.

### 3. Ignorowanie sortowania

Jeśli często robisz:

```sql
SELECT * FROM orders ORDER BY created_at DESC;
```

to sposób dostępu do danych przy sortowaniu też ma znaczenie.

### 4. Zakładanie, że indeks zawsze zostanie użyty

Nie.

Planner może uznać, że pełny skan jest tańszy.

### 5. Brak patrzenia na realne query aplikacji

Indeks dobiera się pod rzeczywiste wzorce użycia, a nie pod losowe przeczucia.

## Mini case study

Masz endpoint:

```text
GET /users/42/orders
```

A pod spodem query:

```sql
SELECT * FROM orders WHERE user_id = 42 ORDER BY created_at DESC LIMIT 20;
```

Jeśli tabela `orders` ma miliony rekordów, to warto myśleć o:

- filtrze po `user_id`,
- sortowaniu po `created_at`,
- tym, że to query jest pewnie wykonywane bardzo często.

To już nie jest temat "czy dodać jakiś indeks", tylko "jaki wzorzec dostępu obsługuje ten endpoint".

## Co Pythonowiec powinien umieć praktycznie

Nie musisz od razu być ekspertem od silnika bazy.

Ale dobrze, żebyś umiał:

- zauważyć, że query robi się wolne przy wzroście danych,
- skojarzyć problem z indeksem albo jego brakiem,
- rozumieć, że planner wybiera plan na podstawie kosztu,
- nie dodawać indeksów bezmyślnie,
- pytać: jakie query mamy naprawdę najczęściej?

## Output myślowy: jak zmienia się system

### Bez indeksu

- mała tabela: "działa okej",
- średnia tabela: "czasem wolno",
- duża tabela: "endpoint zaczyna boleć".

### Z dobrze dobranym indeksem

- mała tabela: różnica może być mało widoczna,
- średnia tabela: zaczyna być odczuwalnie lepiej,
- duża tabela: różnica może być krytyczna dla działania systemu.

## Najważniejsze do zapamiętania

- Indeks przyspiesza część odczytów, ale nie jest darmowy.
- Query planner wybiera plan wykonania na podstawie kosztu.
- Nie każde query skorzysta z indeksu tak samo.
- Trzeba patrzeć na realne wzorce użycia aplikacji.
- Dobry indeks to decyzja projektowa, a nie automatyczna reakcja.

## Ćwiczenia

1. Wyjaśnij własnymi słowami, czemu indeks nie jest darmowy.
2. Podaj trzy kolumny, które często warto indeksować, i jedną, na której indeks może nie dać dużo.
3. Opisz, czym jest query planner bez używania definicji podręcznikowej.
4. Zinterpretuj własnymi słowami różnicę między pseudo-`Seq Scan` i pseudo-`Index Scan`.
5. Weź przykładowy endpoint i opisz, jakie query może pod nim siedzieć oraz które pola są kandydatami do indeksów.
