# Paginacja python

## O czym jest ten rozdział

Paginacja wydaje się prostym tematem, dopóki lista danych jest mała.

Na początku myślisz zwykle:

- pobiorę 20 rekordów,
- dam `LIMIT` i `OFFSET`,
- gotowe.

I przez jakiś czas to naprawdę działa.

Problem zaczyna się później:

- tabela rośnie,
- użytkownik wchodzi na dalsze strony,
- query robią się coraz droższe,
- dane między stronami zaczynają "przeskakiwać",
- API zachowuje się mniej stabilnie.

Dlatego paginacja to nie tylko temat UI. To temat wydajności, spójności odczytu i projektowania API.

## Najprostsza intuicja paginacji

Paginacja to sposób zwracania danych kawałkami zamiast wszystkiego naraz.

To potrzebne, bo:

- listy bywają duże,
- pełny odczyt jest zbyt ciężki,
- klient zwykle nie potrzebuje wszystkiego naraz,
- API i baza powinny ograniczać koszt odpowiedzi.

## LIMIT i OFFSET: najpopularniejszy start

Najprostszy wariant wygląda tak:

```sql
SELECT * FROM orders
ORDER BY created_at DESC
LIMIT 20 OFFSET 0;
```

Druga strona:

```sql
SELECT * FROM orders
ORDER BY created_at DESC
LIMIT 20 OFFSET 20;
```

Trzecia:

```sql
SELECT * FROM orders
ORDER BY created_at DESC
LIMIT 20 OFFSET 40;
```

To jest łatwe do zrozumienia i łatwe do wdrożenia.

## Zalety offset pagination

- prosta do wdrożenia,
- łatwa do zrozumienia,
- wygodna dla klasycznych numerowanych stron,
- dobra na start dla małych i średnich zbiorów.

## Wady offset pagination

To bardzo ważne.

Im większy `OFFSET`, tym często więcej pracy ma baza.

Dlaczego?

Bo baza zwykle musi przejść przez wcześniejsze rekordy, zanim odda te docelowe.

Przykład:

```sql
LIMIT 20 OFFSET 100000
```

To może być już naprawdę kosztowne.

## Drugi problem: niestabilność stron

Jeśli między pobraniem strony 1 i strony 2 pojawią się nowe rekordy albo część rekordów zniknie, użytkownik może zobaczyć:

- duplikaty,
- pominięte rekordy,
- "przesunięte" wyniki.

To naturalna konsekwencja paginacji po zmieniającym się zbiorze danych.

## Keyset pagination: intuicja

Keyset pagination, czasem nazywana cursor-based, działa inaczej.

Zamiast mówić:

- "daj stronę numer 5",

mówisz raczej:

- "daj kolejne 20 rekordów po tym ostatnim, który już mam".

Przykład:

```sql
SELECT * FROM orders
WHERE created_at < '2026-08-15T12:00:00'
ORDER BY created_at DESC
LIMIT 20;
```

Albo bardziej stabilnie po unikalnym kluczu pomocniczym.

## Najprostsza intuicja różnicy

### Offset pagination

- skaczesz po numerach stron.

### Keyset pagination

- przesuwasz się po konkretnym punkcie w danych.

## Kiedy keyset pagination jest lepsza

Keyset pagination często jest lepsza, gdy:

- lista jest bardzo duża,
- zależy Ci na płynnej paginacji kolejnych wyników,
- dane często się zmieniają,
- potrzebujesz stabilniejszego i tańszego przechodzenia dalej.

## Kiedy offset pagination nadal ma sens

Offset nadal ma sens, gdy:

- zbiór nie jest bardzo duży,
- użytkownik naprawdę potrzebuje numerowanych stron,
- prostota wdrożenia jest ważniejsza,
- nie masz ekstremalnych wymagań wydajnościowych.

## Problem z sortowaniem

Paginacja bez stabilnego `ORDER BY` to proszenie się o kłopoty.

Zły pomysł:

```sql
SELECT * FROM orders LIMIT 20 OFFSET 20;
```

Tu baza nie ma jasnej instrukcji, w jakiej kolejności ustawiać rekordy.

Lepszy pomysł:

```sql
SELECT * FROM orders
ORDER BY created_at DESC, id DESC
LIMIT 20 OFFSET 20;
```

Dodanie dodatkowego stabilizatora, np. `id`, bywa bardzo ważne.

## Before/after

### Słabsza paginacja

- brak stabilnego sortowania,
- wysoki `OFFSET`,
- zmieniający się zbiór,
- dziwne zachowanie dalszych stron.

### Lepsza paginacja

- jawne `ORDER BY`,
- dopasowanie typu paginacji do skali systemu,
- stabilniejszy klucz porządkujący,
- świadoma decyzja: offset czy keyset.

## Mini case study: lista zamówień

Masz endpoint:

```text
GET /orders?page=200
```

W implementacji siedzi:

```sql
SELECT * FROM orders
ORDER BY created_at DESC
LIMIT 50 OFFSET 9950;
```

Przy małych danych to działa.

Przy dużych danych zaczynają się problemy:

- query robi się coraz droższe,
- dalsze strony są wolniejsze,
- przy napływie nowych rekordów wyniki są mniej stabilne.

W takim systemie często warto rozważyć keyset pagination.

## Intuicja API z cursorem

Zamiast numeru strony możesz zwracać klientowi coś w stylu:

```json
{
  "items": [...],
  "next_cursor": "2026-08-15T12:00:00|98123"
}
```

Klient potem wysyła:

```text
GET /orders?cursor=2026-08-15T12:00:00|98123
```

To mniej wygodne do ręcznego "skoku na stronę 57", ale często dużo lepsze dla dużych, żywych list.

## Co Pythonowiec powinien rozumieć

Dobrze, żebyś umiał:

- nie zakładać, że `LIMIT/OFFSET` zawsze wystarczy,
- wiedzieć, że `OFFSET` rośnie kosztowo,
- pamiętać o stabilnym sortowaniu,
- rozumieć, kiedy lista jest bardziej feedem niż numerowaną tabelą,
- dobrać strategię paginacji do realnego użycia produktu.

## Output myślowy

### Mały system

- offset działa dobrze,
- prostota wygrywa.

### Rosnący system

- dalsze strony robią się cięższe,
- brak stabilnego porządku zaczyna boleć.

### Dojrzały system z dużymi listami

- keyset bywa dużo sensowniejszy,
- API projektuje się z myślą o wydajności i stabilności, nie tylko wygodzie implementacji.

## Najważniejsze do zapamiętania

- Paginacja to temat wydajności i stabilności, nie tylko wygody UI.
- `LIMIT/OFFSET` jest proste, ale ma koszt przy dużych danych.
- Bez stabilnego `ORDER BY` paginacja jest niebezpieczna.
- Keyset pagination często lepiej skaluje się dla dużych, żywych list.
- Typ paginacji trzeba dobrać do sposobu użycia systemu.

## Ćwiczenia

1. Wyjaśnij własnymi słowami, czemu duży `OFFSET` może boleć wydajnościowo.
2. Podaj przykład, kiedy offset pagination jest całkowicie sensowna.
3. Opisz sytuację, w której keyset pagination będzie lepsza.
4. Wyjaśnij, po co w paginacji potrzebne jest stabilne `ORDER BY`.
5. Zaprojektuj odpowiedź API dla listy zamówień z użyciem kursora.
