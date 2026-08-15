# Flaky tests w Pythonie

## O co chodzi

Flaky test to test, który raz przechodzi, a raz nie, mimo że kod nie został istotnie zmieniony.

To jeden z najbardziej irytujących i niebezpiecznych problemów w testach.

Bo taki test:

- nie daje zaufania,
- myli programistów,
- spowalnia pracę,
- psuje pipeline,
- uczy ludzi ignorować czerwone wyniki.

## Dlaczego flaky tests są tak groźne

Zwykły czerwony test jest przynajmniej uczciwy.

Mówi:

- coś jest nie tak.

Flaky test mówi:

- może jest źle,
- może nie,
- spróbuj jeszcze raz.

To dużo gorsze, bo niszczy zaufanie do całego zestawu testów.

## Najczęstsze przyczyny flaky tests

- zależność od czasu,
- zależność od kolejności wykonania,
- współdzielony stan między testami,
- niestabilne środowisko,
- zależność od sieci lub zewnętrznych usług,
- brak izolacji danych,
- równoległe uruchamianie testów bez przygotowania,
- losowość bez kontroli.

## Przykład intuicyjny

Test zależy od aktualnej godziny albo bieżącej daty.

Raz działa, raz nie, w zależności od momentu uruchomienia.

To bardzo klasyczny flaky case.

## Inny przykład

Jeden test zostawia dane po sobie, a drugi zakłada czyste środowisko.

Jeśli kolejność wykonania się zmieni, wynik testów też może się zmienić.

To bardzo groźna sytuacja.

## Jak rozpoznawać flaky testy

Sygnały ostrzegawcze:

- test przechodzi lokalnie, ale czasem pada w CI,
- ponowne uruchomienie bez zmian daje inny wynik,
- błąd występuje tylko czasami,
- problem znika po odpaleniu pojedynczego testu,
- test jest bardzo wrażliwy na środowisko lub timing.

## Co robić, gdy test jest flaky

Nie ignorować.

Bardzo ważne.

Dobre pytania:

- od czego zależy test,
- czy ma ukryty stan,
- czy używa czasu systemowego,
- czy dotyka zasobów współdzielonych,
- czy zależy od kolejności,
- czy integruje się z czymś niestabilnym.

## Typowe źródła niestabilności

### Czas

- `datetime.now()`,
- timeouty,
- opóźnienia,
- zegar systemowy.

### Stan współdzielony

- globalne zmienne,
- wspólne pliki,
- współdzielona baza,
- singletony i cache.

### Środowisko

- sieć,
- zewnętrzne API,
- różnice między lokalnym środowiskiem a CI.

## Realistyczny flaky case 1: test zależny od czasu

Kod:

```python
from datetime import datetime


def is_night() -> bool:
    return datetime.now().hour >= 22


def test_discount_rule():
    assert is_night() is False
```

Dlaczego to jest flaky:

- wynik zależy od chwili uruchomienia testu,
- ten sam test może być zielony o 14:00 i czerwony o 23:00.

Lepszy kierunek:

- wstrzykiwać czas,
- zamockować źródło czasu,
- testować logikę na kontrolowanym wejściu.

## Realistyczny flaky case 2: kolejność testów

Kod testowy:

```python
cache = []


def add_user(name: str) -> None:
    cache.append(name)


def test_first_user():
    add_user("Anna")
    assert cache == ["Anna"]


def test_second_user():
    add_user("Jan")
    assert cache == ["Jan"]
```

Dlaczego to jest flaky:

- testy współdzielą stan,
- kolejność wykonania wpływa na wynik,
- pojedynczo mogą przechodzić, razem już niekoniecznie.

Lepszy kierunek:

- izolować stan,
- czyścić dane przed testem,
- unikać globalnych efektów ubocznych.

## Realistyczny flaky case 3: niestabilne API zewnętrzne

Scenariusz:

- test odpytuje prawdziwe zewnętrzne API,
- raz API odpowiada szybko i poprawnie,
- innym razem jest timeout albo inny limit.

Dlaczego to jest flaky:

- wynik testu zależy od czegoś poza Twoją kontrolą,
- problem może wcale nie dotyczyć Twojego kodu.

Lepszy kierunek:

- używać contract testów, stubów albo stabilnego środowiska testowego,
- nie opierać zwykłego pipeline'u o kapryśną zewnętrzną usługę.

## Mini case study

Masz test, który tworzy rekord w bazie i oczekuje konkretnej liczby rekordów.

Jeśli inny test nie posprzątał po sobie, wynik zaczyna zależeć od kolejności wykonania.

To nie jest tylko drobny problem techniczny. To test, który niszczy zaufanie do całego zestawu.

## Dlaczego retry nie jest rozwiązaniem

Czasem ludzie próbują "naprawić" flaky tests przez ponowne odpalenie testu.

To bywa tylko maskowanie problemu.

Jeśli test jest niestabilny, trzeba zrozumieć przyczynę, a nie tylko zwiększać liczbę prób.

## Jak zapobiegać flaky tests

- izolować stan,
- unikać zależności od realnego czasu bez kontroli,
- ograniczać niepotrzebne zależności zewnętrzne,
- czyścić środowisko testowe,
- pilnować deterministycznych danych,
- jasno odróżniać test stabilny od środowiskowo ryzykownego.

## Szybka ściąga

- flaky test raz przechodzi, raz nie,
- jest groźny, bo niszczy zaufanie,
- najczęściej chodzi o czas, stan, środowisko albo kolejność,
- nie należy go ignorować ani tylko "retryować",
- trzeba znaleźć źródło niestabilności.

## Ćwiczenia

1. Podaj 5 możliwych przyczyn flaky testów.
2. Wymyśl przykład testu zależnego od czasu.
3. Opisz przypadek problemu z kolejnością testów.
4. Wyjaśnij, czemu flaky test bywa groźniejszy niż zwykły czerwony test.
5. Zrób checklistę diagnozy niestabilnego testu.

## Najważniejsze do zapamiętania

- Flaky tests niszczą zaufanie do testów bardziej niż zwykłe błędy.
- Najczęstsze źródła to czas, środowisko, stan współdzielony i kolejność.
- Retry bez diagnozy zwykle tylko maskuje problem.
- Stabilność testów jest częścią jakości systemowej.
- Jeśli test jest flaky, trzeba traktować to poważnie.
