# Fake, mock i stub w Pythonie

## O co chodzi

W testach bardzo często nie chcesz używać wszystkich prawdziwych zależności.

Na przykład:

- nie chcesz wysyłać prawdziwego e-maila,
- nie chcesz pisać do prawdziwej bazy,
- nie chcesz odpalać zewnętrznego API,
- nie chcesz mieć niestabilności środowiska.

Wtedy używasz podstawionych obiektów testowych. I właśnie tu pojawiają się pojęcia:

- fake,
- mock,
- stub.

## Stub

Stub zwykle po prostu zwraca przygotowaną odpowiedź.

Jego rola jest mała:

- dać testowi potrzebny wynik,
- bez prawdziwej logiki zależności.

Przykład intuicyjny:

- metoda `get_rate()` zawsze zwraca `0.23`.

## Fake

Fake to zwykle prostsza, ale działająca implementacja zależności.

Nie jest prawdziwą produkcyjną wersją, ale zachowuje się sensownie.

Przykład:

- repozytorium trzyma dane w pamięci zamiast w prawdziwej bazie.

Fake często bywa świetny, bo test zachowuje więcej realizmu niż przy samym mockowaniu.

## Mock

Mock to obiekt używany m.in. do sprawdzania interakcji.

Pomaga odpowiedzieć na pytania takie jak:

- czy metoda została wywołana,
- z jakimi argumentami,
- ile razy została wywołana.

Mock bardziej skupia się na tym, jak obiekt był użyty, niż na realnej logice zależności.

## Intuicja praktyczna

### Stub

Daje odpowiedź.

### Fake

Daje prostą działającą implementację.

### Mock

Pomaga sprawdzić interakcję.

To nie są absolutnie sztywne definicje akademickie, ale bardzo dobra praktyczna intuicja.

## Kiedy fake bywa lepszy niż mock

Bardzo często fake daje lepsze testy niż mock, bo:

- test mniej zależy od szczegółów implementacji,
- bardziej przypomina prawdziwe użycie,
- mniej skupia się na tym *jak* coś zostało zrobione, a bardziej *czy efekt jest poprawny*.

To bardzo ważna lekcja.

## Kiedy mock ma sens

Mock ma sens, gdy naprawdę chcesz sprawdzić interakcję, np.:

- czy wysłano powiadomienie,
- czy wywołano konkretne API,
- czy retry został uruchomiony,
- czy logger dostał ważny komunikat.

Czyli gdy sama interakcja jest częścią kontraktu zachowania.

## Przykład fake repozytorium

```python
class FakeUserRepository:
    def __init__(self):
        self.users = {}

    def save(self, user):
        self.users[user["id"]] = user

    def get(self, user_id):
        return self.users.get(user_id)
```

To prosty fake:

- działa sensownie,
- nie potrzebuje prawdziwej bazy,
- pozwala testować logikę wyżej.

## Dlaczego nadmiar mocków szkodzi

Jeśli wszystko mockujesz, test może zacząć testować bardziej:

- szczegóły implementacji,
- kolejność wywołań,
- mało ważne interakcje,

niż rzeczywiste zachowanie systemu.

Takie testy łatwo stają się kruche i zbyt mocno związane z bieżącym kształtem kodu.

## Mini case study

Masz `OrderService`, który zapisuje zamówienie i wysyła e-mail.

### Dobry pomysł

- fake repozytorium do przechowania danych,
- mock albo stub dla wysyłki e-maila.

Dlaczego?

- zapis możesz testować bardziej realistycznie,
- a efekt uboczny wysyłki chcesz tylko skontrolować.

To jest sensowny kompromis.

## Typowe błędy początkujących

- mockowanie wszystkiego,
- brak rozróżnienia między sprawdzaniem wyniku a sprawdzaniem interakcji,
- używanie mocka tam, gdzie fake byłby prostszy i czytelniejszy,
- zbyt rozbudowane stuby i fake bez potrzeby.

## Szybka ściąga

- stub daje przygotowaną odpowiedź,
- fake daje uproszczoną działającą implementację,
- mock pomaga sprawdzić interakcję,
- nie wszystko trzeba mockować,
- fake bardzo często daje bardziej stabilne testy niż mock.

## Ćwiczenia

1. Zbuduj prosty fake repozytorium.
2. Wymyśl przykład stuba zwracającego stałą wartość.
3. Podaj przykład interakcji, którą sensownie sprawdzić mockiem.
4. Opisz przypadek, gdzie nadmiar mocków szkodzi testowi.
5. Zaproponuj strategię fake vs mock dla małego serwisu zamówień.

## Najważniejsze do zapamiętania

- Fake, mock i stub rozwiązują różne problemy testowe.
- Fake często daje bardziej realistyczne i mniej kruche testy.
- Mock ma sens, gdy interakcja sama w sobie jest ważna.
- Nie warto mockować wszystkiego bez refleksji.
- Wybór typu podstawionej zależności powinien wynikać z celu testu.
