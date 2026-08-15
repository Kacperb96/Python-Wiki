# Debugging walkthrough w Pythonie

## Po co ten plik

Ten plik spina cały folder 21 w jedną praktyczną historię.

Nie chodzi tu o pojedyncze definicje, tylko o pokazanie pełnego procesu:

- od objawu,
- przez reprodukcję,
- zawężenie problemu,
- analizę tracebacka,
- zbudowanie minimalnego przykładu,
- aż do poprawki.

To jest dokładnie ten rodzaj pracy, który pojawia się w prawdziwym repo.

## Scenariusz

Masz zgłoszenie:

- "czasem endpoint tworzenia zamówienia wywala 500",
- "dzieje się to tylko dla części użytkowników",
- "nie wiadomo czemu".

Na start masz tylko objaw.

## Krok 1: nazwij objaw precyzyjnie

Zły opis:

- "zamówienia nie działają"

Lepszy opis:

- "endpoint POST /orders czasem kończy się 500 dla części payloadów"

To ważne, bo dobry debugging zaczyna się od precyzji.

## Krok 2: odtwórz problem

Szukasz konkretnego wejścia, które powoduje błąd.

Załóżmy, że znajdujesz taki payload:

```python
payload = {
    "user": {"name": "Anna"},
    "price": 100,
}
```

I ten przypadek wywala błąd.

To już ogromny postęp.

## Krok 3: przeczytaj traceback

Masz traceback w stylu:

```text
Traceback (most recent call last):
  File "app.py", line 30, in endpoint
    return create_order(payload)
  File "service.py", line 22, in create_order
    total = calculate_total(payload["user"], payload["price"])
  File "pricing.py", line 10, in calculate_total
    discount = user["discount"]
KeyError: 'discount'
```

### Co już wiesz

- miejsce eksplozji: `user["discount"]`,
- przepływ: `endpoint -> create_order -> calculate_total`,
- typ błędu: `KeyError`.

### Czego jeszcze nie wiesz

- czy `discount` powinno zawsze istnieć,
- czy payload jest niepoprawny,
- czy brakuje walidacji,
- czy logika biznesowa błędnie zakłada obecność tego pola.

## Krok 4: zawęź problem

Nie poprawiasz jeszcze kodu.

Najpierw pytasz:

- czy każdy użytkownik musi mieć `discount`,
- czy to pole jest opcjonalne,
- czy bug jest w wejściu, czy w logice ceny,
- czy wcześniej była walidacja.

To bardzo ważne, bo bez tego łatwo zrobić błędną poprawkę.

## Krok 5: zbuduj minimal reproducible example

Wyciągasz problem z całego API do małego przykładu:

```python
def calculate_total(user: dict, price: int) -> int:
    discount = user["discount"]
    return price - discount


print(calculate_total({"name": "Anna"}, 100))
```

Teraz masz mały, czysty przypadek odtwarzający błąd.

To już bardzo pomaga.

## Krok 6: postaw hipotezy

Możliwe hipotezy:

1. `discount` powinno być obowiązkowe, ale walidacja nie działa.
2. `discount` jest opcjonalne, ale logika nie obsługuje braku.
3. payload jest budowany źle wcześniej.

To są sensowne hipotezy. Nie zgadujesz już na ślepo.

## Krok 7: sprawdź kontrakt biznesowy

Załóżmy, że ustalasz:

- użytkownik bez zniżki jest poprawnym przypadkiem,
- brak `discount` powinien oznaczać `0`.

To zmienia wszystko.

Bug nie polega na tym, że dane są błędne. Bug polega na tym, że logika ceny źle założyła kształt danych.

## Krok 8: zrób najmniejszą sensowną poprawkę

Przed:

```python
def calculate_total(user: dict, price: int) -> int:
    discount = user["discount"]
    return price - discount
```

Po:

```python
def calculate_total(user: dict, price: int) -> int:
    discount = user.get("discount", 0)
    return price - discount
```

To jest mała poprawka, proporcjonalna do problemu.

## Krok 9: zweryfikuj, że poprawka działa

Sprawdzasz:

```python
print(calculate_total({"name": "Anna"}, 100))
print(calculate_total({"name": "Anna", "discount": 15}, 100))
```

Output:

```python
100
85
```

Teraz masz:

- poprawkę,
- dwa scenariusze,
- lepsze rozumienie zachowania.

## Krok 10: zadaj pytanie o miejsce docelowe poprawki

To bardzo ważne.

Czy poprawka powinna zostać tylko tu?

Możliwe, że warto też:

- dopisać walidację,
- doprecyzować kontrakt danych,
- dodać test,
- zalogować nietypowy przypadek.

Czyli samo usunięcie błędu to nie zawsze koniec myślenia.

## Co ten walkthrough pokazuje

Ten przykład spina prawie cały folder 21:

- objaw został nazwany precyzyjnie,
- błąd został odtworzony,
- traceback zawęził obszar,
- zbudowano MRE,
- hipotezy były sprawdzane zamiast zgadywane,
- poprawka była mała i konkretna,
- wynik został zweryfikowany.

To właśnie jest dobre debugowanie.

## Drugi mini walkthrough: regresja

Masz informację:

- "to działało tydzień temu, dziś nie działa".

Plan:

1. ustal ostatni dobry stan,
2. odtwórz problem,
3. znajdź test lub prosty check,
4. zawężaj historię zmian,
5. znajdź commit źródłowy,
6. dopiero potem popraw.

To pokazuje, że nie każdy debugging wygląda tak samo. Ale proces zawężania nadal pozostaje wspólny.

## Typowe złe ścieżki w takim przypadku

- od razu pisać dużą poprawkę,
- ignorować traceback,
- nie robić reprodukcji,
- poprawić tylko objaw bez zrozumienia kontraktu,
- mieszać bugfix z wielką refaktoryzacją.

## Szybka ściąga

Dobry walkthrough debugowania wygląda zwykle tak:

1. objaw,
2. reprodukcja,
3. traceback,
4. zawężenie,
5. MRE,
6. hipoteza,
7. poprawka,
8. weryfikacja.

## Ćwiczenia

1. Weź powyższy przykład i rozpisz go własnymi słowami bez patrzenia na tekst.
2. Zmień case tak, aby błąd dotyczył `None` zamiast `KeyError`, i przejdź przez ten sam proces.
3. Dopisz, jakie logi dodałbyś do tego scenariusza.
4. Opisz, kiedy poprawka powinna być w miejscu eksplozji, a kiedy warstwę wyżej.
5. Zbuduj własny krótki debugging walkthrough dla innego typu błędu.

## Najważniejsze do zapamiętania

- Debugowanie to proces, nie seria przypadkowych ruchów.
- Największą moc daje połączenie reprodukcji, tracebacka i zawężania problemu.
- MRE bardzo przyspiesza zrozumienie błędu.
- Dobra poprawka jest mała, uzasadniona i zweryfikowana.
- Jeśli potrafisz przejść taki walkthrough spokojnie, to naprawdę umiesz debugować.
