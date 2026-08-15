# Fixtures i test data builders w Pythonie

## O co chodzi

W pewnym momencie testy zaczynają mieć coraz więcej danych wejściowych.

Pojawia się wtedy problem:

- te same obiekty testowe są budowane w wielu miejscach,
- dane są kopiowane ręcznie,
- zmiana jednego pola wymaga edycji 10 testów,
- testy robią się ciężkie i nieczytelne.

Właśnie tu pomagają:

- fixtures,
- test data builders.

## Fixtures

Fixture to przygotowany fragment stanu albo danych, który można wygodnie wielokrotnie używać w testach.

Intuicyjnie:

- zamiast w każdym teście ręcznie tworzyć użytkownika, zamówienie albo repo,
- przygotowujesz wspólne źródło danych testowych.

## Po co fixtures

Pomagają:

- zmniejszyć duplikację,
- uprościć setup testów,
- poprawić czytelność,
- centralizować typowe dane i zależności testowe.

## Intuicyjny przykład

Zamiast w 8 testach pisać podobny kod tworzący użytkownika, możesz mieć jeden przygotowany obiekt albo funkcję pomocniczą zwracającą sensowny obiekt startowy.

## Test data builder

Builder to bardziej elastyczne podejście.

Zamiast mieć jeden sztywny obiekt testowy, tworzysz wygodny sposób budowania danych z rozsądnymi domyślnymi wartościami i możliwością nadpisania tylko tego, co ważne w danym teście.

To bardzo praktyczne, gdy obiekty są większe.

## Prosty przykład buildera

```python
def build_user(**overrides):
    user = {
        "id": 1,
        "name": "Anna",
        "email": "anna@example.com",
        "active": True,
    }
    user.update(overrides)
    return user

print(build_user())
print(build_user(name="Jan", active=False))
```

Przykładowy output:

```python
{'id': 1, 'name': 'Anna', 'email': 'anna@example.com', 'active': True}
{'id': 1, 'name': 'Jan', 'email': 'anna@example.com', 'active': False}
```

To bardzo wygodne, bo w teście zmieniasz tylko to, co istotne.

## Fixtures vs builder

### Fixture

Dobra, gdy:

- potrzebujesz wspólnego setupu,
- stan jest dość standardowy,
- testy korzystają z podobnego środowiska.

### Builder

Dobry, gdy:

- obiekty mają dużo pól,
- testy potrzebują różnych wariantów,
- chcesz elastycznie zmieniać wybrane elementy bez kopiowania całej struktury.

Bardzo często oba podejścia dobrze się uzupełniają.

## Dlaczego ręczne kopiowanie danych boli

Przy kilku testach jeszcze to przechodzi.

Przy większym module zaczynają się problemy:

- dane są niespójne,
- w jednym teście pole nazywa się inaczej,
- po zmianie modelu trzeba poprawiać dużo miejsc,
- testy bardziej opisują konstrukcję danych niż zachowanie systemu.

To bardzo pogarsza utrzymanie.

## Kiedy builder daje dużą wartość

Szczególnie gdy testujesz:

- większe modele danych,
- payloady API,
- zamówienia, użytkowników, faktury,
- obiekty z wieloma zależnościami i polami.

## Uwaga na przeinżynierowanie

Nie każdy prosty test potrzebuje wielkiego buildera.

Jeśli obiekt ma dwa pola, prosta fixture albo nawet jawne dane w teście mogą być lepsze.

Jak zwykle: chodzi o proporcję.

## Mini case study

Masz 20 testów zamówienia i w każdym ręcznie budujesz `Order` z 12 polami.

To sygnał, że:

- dane testowe są zbyt powielane,
- testy robią się kruche,
- warto wydzielić builder albo sensowną fixture.

## Typowe błędy początkujących

- kopiowanie tych samych danych testowych wszędzie,
- zbyt ciężkie fixtures robiące pół systemu,
- buildery tak skomplikowane, że trudniej je zrozumieć niż same testy,
- ukrywanie zbyt ważnych szczegółów testu w automatycznym setupie.

## Szybka ściąga

- fixtures pomagają współdzielić setup,
- buildery pomagają elastycznie budować dane,
- oba narzędzia zmniejszają duplikację,
- nie warto jednak przesadzać z abstrakcją prostych danych.

## Ćwiczenia

1. Zbuduj prosty builder użytkownika.
2. Przygotuj fixture zwracającą domyślne zamówienie.
3. Porównaj test z ręcznym budowaniem danych i z builderem.
4. Wskaż przypadek, gdzie fixture wystarczy, a builder byłby przesadą.
5. Opisz, jak zmiana modelu danych wpływa na testy z builderem vs kopiowanymi słownikami.

## Najważniejsze do zapamiętania

- Fixtures i buildery pomagają pisać czytelniejsze, mniej kruche testy.
- Fixture lepiej nadaje się do współdzielonego setupu.
- Builder lepiej nadaje się do elastycznych wariantów danych.
- Dobre dane testowe zmniejszają koszt utrzymania testów.
- Abstrakcja ma pomagać testom, a nie je zaciemniać.
