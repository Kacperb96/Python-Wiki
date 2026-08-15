# Bezpieczna serializacja w Pythonie

## Czym jest serializacja

Serializacja to zamiana danych lub obiektów na format, który można:

- zapisać do pliku,
- przesłać przez sieć,
- umieścić w cache,
- przekazać do innego systemu.

Deserializacja to proces odwrotny, czyli odtworzenie danych z tego formatu.

Sama serializacja jest czymś normalnym i potrzebnym. Problem zaczyna się wtedy, gdy bezrefleksyjnie deserializujesz nieufne dane.

## Dlaczego to ma związek z bezpieczeństwem

Dane z zewnątrz nie są zaufane.

Jeśli aplikacja:

- pobiera payload,
- deserializuje go,
- a potem traktuje jak bezpieczny,

to może narobić sobie problemów.

Ryzyko zależy od formatu i biblioteki, ale podstawowa zasada jest prosta:

- nie każda deserializacja jest równie bezpieczna,
- nawet poprawnie sparsowane dane nadal wymagają walidacji.

## JSON jako bezpieczniejszy wybór

Dla zwykłej wymiany danych JSON jest zazwyczaj rozsądnym wyborem.

Dlaczego?

- opisuje proste struktury danych,
- jest przewidywalny,
- nie służy do odtwarzania arbitralnych obiektów aplikacji,
- dobrze współpracuje z walidacją modeli wejściowych.

Przykład:

```python
import json

raw_data = '{"name": "Anna", "age": 25}'
data = json.loads(raw_data)
print(data)
```

Output:

```python
{'name': 'Anna', 'age': 25}
```

To jeszcze nie znaczy, że dane są poprawne biznesowo. To znaczy tylko, że JSON został poprawnie sparsowany.

## Poprawny JSON nadal może być zły

Spójrz na taki przykład:

```python
import json

raw_data = '{"name": "", "age": -1000}'
data = json.loads(raw_data)
print(data)
```

Output:

```python
{'name': '', 'age': -1000}
```

Format JSON jest poprawny.

Ale dane są bez sensu.

To pokazuje bardzo ważną rzecz:

- parsowanie formatu to nie to samo co walidacja danych.

## `pickle` i dlaczego trzeba uważać

`pickle` jest wygodnym mechanizmem Pythona do serializacji obiektów.

Problem polega na tym, że nie powinien być używany do nieufnych danych z zewnątrz.

To jedna z najważniejszych praktycznych zasad bezpieczeństwa w Pythonie.

### Co zapamiętać praktycznie

Jeśli dane pochodzą od:

- użytkownika,
- internetu,
- zewnętrznego systemu,
- pliku, któremu nie ufasz,

nie używaj `pickle.loads()` bez pełnej kontroli kontekstu.

## Bezpieczniejszy przepływ danych

Dobry, praktyczny wzorzec wygląda tak:

1. odbierz dane,
2. sparsuj prosty format, np. JSON,
3. zwaliduj strukturę i wartości,
4. dopiero potem użyj danych w logice aplikacji.

Przykład:

```python
import json


def validate_user(data):
    if not isinstance(data.get("name"), str) or not data["name"].strip():
        raise ValueError("Niepoprawne name")

    if not isinstance(data.get("age"), int) or data["age"] < 0:
        raise ValueError("Niepoprawne age")

    return {"name": data["name"].strip(), "age": data["age"]}


raw_data = '{"name": " Anna ", "age": 25}'
parsed = json.loads(raw_data)
validated = validate_user(parsed)
print(validated)
```

Output:

```python
{'name': 'Anna', 'age': 25}
```

## Format a bezpieczeństwo to nie to samo

Początkujący czasem myślą:

- skoro coś jest JSON-em, to jest bezpieczne.

To nieprawda.

JSON jest zwykle bezpieczniejszy jako format niż mechanizmy odtwarzające złożone obiekty, ale nadal możesz dostać dane:

- puste,
- absurdalne,
- zbyt duże,
- niezgodne z kontraktem,
- złośliwe biznesowo.

## Kiedy `pickle` może mieć sens

W bardzo kontrolowanych, wewnętrznych scenariuszach, gdzie:

- obie strony są zaufane,
- dokładnie rozumiesz ryzyko,
- nie przyjmujesz danych z niepewnego źródła.

Ale jako ogólna zasada nauki Python security:

- nie używaj `pickle` do nieufnych danych.

## Typowe błędy początkujących

- deserializacja danych z zewnątrz bez walidacji,
- przekonanie, że poprawny JSON oznacza poprawne dane,
- użycie `pickle` tam, gdzie wystarczyłby JSON,
- brak limitów na wielkość lub strukturę danych,
- mieszanie parsowania z logiką biznesową bez etapu walidacji.

## Checklista bezpiecznej deserializacji

- Skąd pochodzą dane?
- Czy to źródło jest zaufane?
- Czy używam prostego, przewidywalnego formatu?
- Czy waliduję dane po parsowaniu?
- Czy unikam `pickle` dla nieufnych danych?
- Czy wiem, jaki kontrakt danych naprawdę akceptuję?

## Szybka ściąga

Przy serializacji i deserializacji pamiętaj:

- dla danych zewnętrznych preferuj prostsze formaty jak JSON,
- parsowanie nie zastępuje walidacji,
- poprawny format nie gwarantuje sensownych danych,
- `pickle` wymaga dużej ostrożności,
- nieufne dane trzeba traktować z ograniczonym zaufaniem na każdym kroku.

## Ćwiczenia

1. Napisz przykład poprawnego JSON-a, który zawiera błędne dane biznesowo.
2. Zbuduj prosty przepływ `JSON -> parse -> walidacja -> użycie`.
3. Wyjaśnij własnymi słowami, dlaczego `pickle` nie nadaje się do nieufnych danych z internetu.
4. Porównaj `json.loads()` i ryzykowną deserializację arbitralnych obiektów.
5. Zastanów się, jakie pola w twoim projekcie szczególnie wymagają walidacji po parsowaniu.

## Najważniejsze do zapamiętania

- Serializacja sama w sobie nie jest problemem, problemem jest nieostrożna deserializacja.
- JSON jest zwykle bezpieczniejszym wyborem dla nieufnych danych niż mechanizmy odtwarzające złożone obiekty.
- Poprawny format danych nie oznacza, że dane są sensowne lub bezpieczne.
- `pickle` nie powinien być używany do nieufnych danych zewnętrznych.
- Bezpieczny przepływ to: parse, walidacja, dopiero potem użycie.
