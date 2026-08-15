# Walidacja danych w Pythonie

## Po co walidować dane

Walidacja danych to jeden z najważniejszych fundamentów bezpiecznego i stabilnego programu.

Jeśli aplikacja przyjmuje dane bez kontroli, problemy pojawiają się bardzo szybko:

- wyjątki w nieoczekiwanych miejscach,
- błędne rekordy w bazie,
- niepoprawne decyzje biznesowe,
- luki bezpieczeństwa,
- trudne do diagnozowania błędy.

Walidacja nie jest dodatkiem. To pierwsza linia obrony.

## Jakie dane wymagają walidacji

W praktyce prawie wszystkie dane zewnętrzne:

- requesty HTTP,
- formularze,
- input z `input()`,
- argumenty CLI,
- pliki CSV i JSON,
- dane z webhooków,
- dane z zewnętrznych API,
- rekordy importowane z innych systemów.

## Najważniejsza zasada

Nie pytaj tylko:

- czy użytkownik podał to, czego oczekiwałem?

Pytaj też:

- co jeśli poda pustą wartość,
- co jeśli poda zły typ,
- co jeśli poda za długi tekst,
- co jeśli poda wartość skrajną,
- co jeśli poda coś złośliwego,
- co jeśli pominie pole,
- co jeśli poda poprawny technicznie format, ale bez sensu biznesowo.

## Walidacja techniczna a biznesowa

To rozróżnienie jest bardzo ważne.

### Walidacja techniczna

Sprawdza, czy dane w ogóle mają poprawny kształt.

Przykłady:

- czy pole istnieje,
- czy `age` jest liczbą całkowitą,
- czy `email` jest stringiem,
- czy tekst nie jest pusty po `strip()`,
- czy liczba mieści się w zakresie.

### Walidacja biznesowa

Sprawdza, czy dane mają sens w regułach domeny.

Przykłady:

- czy użytkownik może kupić produkt,
- czy kupon rabatowy nie wygasł,
- czy limit przelewów nie został przekroczony,
- czy liczba miejsc nie została już wyczerpana.

Technicznie poprawne dane nadal mogą być biznesowo niedozwolone.

## Gdzie walidować

Najlepiej jak najbliżej wejścia do systemu.

Czyli:

- przy odbiorze requestu,
- przy wczytywaniu pliku,
- przy przyjmowaniu argumentów CLI,
- przy odbiorze danych z zewnętrznej usługi.

To ogranicza rozlewanie się błędnych danych po całej aplikacji.

## Prosty przykład walidacji

```python
def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("age musi byc int")

    if age < 0:
        raise ValueError("age nie moze byc ujemny")

    if age > 130:
        raise ValueError("age ma nielogiczna wartosc")

    return age
```

### Przykładowe użycie

```python
print(validate_age(30))
```

Output:

```python
30
```

### Przykład błędu

```python
validate_age(-5)
```

Efekt:

```python
ValueError: age nie moze byc ujemny
```

## Walidacja pustego tekstu

```python
def validate_name(name):
    if not isinstance(name, str):
        raise TypeError("name musi byc stringiem")

    if not name.strip():
        raise ValueError("name nie moze byc pusty")

    return name.strip()
```

### Przykład

```python
print(validate_name("  Anna  "))
```

Output:

```python
Anna
```

## Walidacja prostego payloadu

```python
def validate_user_payload(payload):
    required_fields = ["name", "email", "age"]

    for field in required_fields:
        if field not in payload:
            raise ValueError(f"Brak pola: {field}")

    name = validate_name(payload["name"])
    age = validate_age(payload["age"])
    email = payload["email"]

    if not isinstance(email, str) or "@" not in email:
        raise ValueError("Niepoprawny email")

    return {
        "name": name,
        "email": email.strip(),
        "age": age,
    }
```

### Przykład

```python
payload = {"name": " Jan ", "email": "jan@example.com", "age": 25}
print(validate_user_payload(payload))
```

Output:

```python
{'name': 'Jan', 'email': 'jan@example.com', 'age': 25}
```

## Walidacja a bezpieczeństwo

Walidacja nie rozwiązuje całego bezpieczeństwa, ale bardzo pomaga.

Dzięki niej możesz wcześnie odrzucić:

- niepoprawne typy,
- absurdalne wartości,
- puste pola,
- zbyt długie dane,
- część prób nadużycia.

Uwaga: walidacja nie zastępuje innych zabezpieczeń.

Przykład:

- walidacja nie zastępuje parametryzacji SQL,
- walidacja nie zastępuje autoryzacji,
- walidacja nie zastępuje kontroli dostępu do plików.

## Frontend nie wystarcza

To klasyczny błąd początkujących.

„Przecież frontend już sprawdza formularz” nie jest argumentem bezpieczeństwa.

Dlaczego?

- request można wysłać ręcznie,
- frontend można obejść,
- aplikacja mobilna może wysłać inne dane,
- inny system może wywoływać twoje API bez UI.

Backend też musi walidować dane.

## Pydantic i nowoczesny Python

W nowoczesnych projektach bardzo często używa się `Pydantic`.

Pozwala on definiować modele danych i walidować je automatycznie.

Przykład idei:

```python
from pydantic import BaseModel, Field


class UserInput(BaseModel):
    name: str = Field(min_length=1)
    email: str
    age: int = Field(ge=0, le=130)
```

To bardzo wygodne, ale nadal trzeba rozumieć zasady walidacji. Biblioteka pomaga, ale nie myśli za ciebie.

## Typowe błędy początkujących

- brak walidacji w ogóle,
- walidowanie za późno,
- mylenie walidacji technicznej z biznesową,
- walidacja tylko na froncie,
- zbyt ogólne komunikaty błędów,
- dopuszczanie pustych stringów po `strip()`,
- brak limitów długości tekstu.

## Checklista walidacji

Przy każdym wejściu danych sprawdź:

- Czy pole istnieje?
- Czy ma dobry typ?
- Czy ma dozwolony zakres?
- Czy tekst nie jest pusty?
- Czy długość jest sensowna?
- Czy format jest poprawny?
- Czy wartość ma sens biznesowo?

## Szybka ściąga

Dobra walidacja:

- dzieje się wcześnie,
- jest jawna,
- rozdziela technikę od biznesu,
- czyści dane przed dalszym użyciem,
- nie ufa frontendowi.

## Ćwiczenia

1. Napisz walidację pola `price`, które musi być liczbą większą od zera.
2. Napisz walidację pola `username`, które nie może być puste i ma maksymalnie 20 znaków.
3. Rozdziel techniczną i biznesową walidację dla zamówienia.
4. Napisz funkcję walidującą listę identyfikatorów użytkowników.
5. Pokaż przykład, gdzie poprawny JSON nadal zawiera niepoprawne dane biznesowo.

## Najważniejsze do zapamiętania

- Walidacja danych jest podstawą bezpieczeństwa i stabilności.
- Waliduj jak najbliżej wejścia do systemu.
- Odróżniaj walidację techniczną od biznesowej.
- Frontend nie jest jedynym miejscem walidacji.
- Biblioteki pomagają, ale nie zastępują myślenia projektowego.
