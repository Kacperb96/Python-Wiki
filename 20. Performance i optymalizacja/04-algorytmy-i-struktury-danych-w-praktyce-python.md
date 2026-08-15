# Algorytmy i struktury danych w praktyce Python

## O co chodzi

Bardzo często największy zysk wydajnościowy nie bierze się z mikrooptymalizacji składni.

Największy zysk bierze się z:

- lepszego algorytmu,
- lepszej struktury danych,
- usunięcia zbędnej pracy.

To jedna z najważniejszych lekcji performance.

## Dlaczego to jest takie ważne

Jeśli algorytm jest zły, to nawet bardzo elegancko zapisany kod nadal może być wolny.

Z kolei dobra struktura danych potrafi dać ogromny skok wydajności bez żadnych sztuczek.

## Najprostsza intuicja

Nie pytaj od razu:

- jak przyspieszyć tę linijkę.

Najpierw pytaj:

- czy robię właściwą rzecz,
- czy robię ją odpowiednią liczbę razy,
- czy używam odpowiedniej struktury danych.

## Przykład: lista vs set

Wyobraź sobie, że często sprawdzasz, czy element istnieje w kolekcji.

### Wersja z listą

```python
blocked = ["anna", "jan", "ola", "marek"]
print("jan" in blocked)
```

### Wersja z setem

```python
blocked = {"anna", "jan", "ola", "marek"}
print("jan" in blocked)
```

Obie działają, ale semantycznie i wydajnościowo `set` często jest lepszy do testu przynależności.

## Przykład: wyszukiwanie rekordu

Masz listę użytkowników i ciągle szukasz po `id`.

### Słaby model

```python
users = [
    {"id": 1, "name": "Anna"},
    {"id": 2, "name": "Jan"},
]


def find_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    return None
```

Dla małej listy to wystarczy. Dla dużej i częstego wyszukiwania lepszy może być słownik.

### Lepszy model

```python
users_by_id = {
    1: {"id": 1, "name": "Anna"},
    2: {"id": 2, "name": "Jan"},
}

print(users_by_id.get(2))
```

To nie jest mikrooptymalizacja. To lepsza struktura danych do problemu.

## Przykład: zła złożoność ukryta w pętli

```python
items = [1, 2, 3, 4, 5]
result = []

for x in items:
    if x not in result:
        result.append(x)
```

Przy małych danych to wygląda niewinnie.

Przy dużych danych może być niepotrzebnie kosztowne, bo w każdej iteracji robisz kolejne przeszukiwanie.

Często lepszym narzędziem okaże się `set`, `dict` albo inny model przetwarzania.

## Algorytm > sprytny zapis

To bardzo ważne.

Zmiana z:

- złego algorytmu na dobry,

często daje dużo większy zysk niż:

- zamiana pętli na comprehension,
- mały trik ze stringami,
- przestawienie dwóch linii kodu.

## Kiedy struktura danych ma największe znaczenie

Szczególnie gdy:

- często wyszukujesz,
- często grupujesz,
- liczysz wystąpienia,
- filtrujesz duże zbiory,
- trzymasz dużo danych w pamięci,
- często usuwasz lub dodajesz z przodu kolekcji.

## Typowe pary decyzji

### `list` vs `set`

- `list` gdy ważna kolejność i prosty przebieg,
- `set` gdy ważna szybka przynależność i unikalność.

### `list` vs `dict`

- `list` gdy dane naturalnie są sekwencją,
- `dict` gdy chcesz szybki dostęp po kluczu.

### `list` vs `deque`

- `list` dla zwykłej sekwencji,
- `deque` dla kolejki i operacji z obu końców.

To nie są tylko decyzje "stylu", ale też decyzje performance.

## Mini case study

Masz endpoint, który dla każdego użytkownika szuka danych po `id` w liście 100 000 rekordów.

Jeśli robisz to wielokrotnie, problemem nie jest składnia pętli. Problemem jest model danych.

Zamiana listy na mapowanie `id -> rekord` może dać znacznie większy efekt niż jakakolwiek kosmetyka kodu.

## Typowe błędy początkujących

- szukanie mikrooptymalizacji przed sprawdzeniem algorytmu,
- używanie niewłaściwej struktury danych do wzorca dostępu,
- brak myślenia o tym, jak często dana operacja się powtarza,
- zakładanie, że każda kolekcja jest równie dobra do wszystkiego.

## Szybka ściąga

- bardzo często największy zysk daje lepszy algorytm,
- struktura danych wpływa bezpośrednio na wydajność,
- `set` jest świetny do testu przynależności,
- `dict` jest świetny do dostępu po kluczu,
- zanim optymalizujesz składnię, sprawdź model problemu.

## Ćwiczenia

1. Porównaj wyszukiwanie elementu w liście i w secie.
2. Zrób przykład dostępu po `id` przez listę i przez `dict`.
3. Znajdź fragment kodu, gdzie zła struktura danych psuje wydajność.
4. Opisz przypadek, gdzie algorytm da większy zysk niż mikrooptymalizacja.
5. Wypisz 5 pytań, które warto sobie zadać przed wyborem struktury danych.

## Najważniejsze do zapamiętania

- Największy zysk performance bardzo często daje lepszy algorytm.
- Dobra struktura danych to jeden z najmocniejszych sposobów przyspieszania kodu.
- Mikrooptymalizacje mają sens dopiero po sprawdzeniu modelu danych.
- Nie każda kolekcja nadaje się równie dobrze do każdego problemu.
- Wydajność bardzo często zaczyna się od poprawnego modelu, nie od sztuczek.
