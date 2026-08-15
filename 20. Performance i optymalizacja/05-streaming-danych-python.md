# Streaming danych w Pythonie

## O co chodzi

Streaming danych to przetwarzanie danych stopniowo, kawałek po kawałku, zamiast ładowania wszystkiego naraz do pamięci.

To bardzo ważne przy:

- dużych plikach,
- dużych odpowiedziach z API,
- długich pipeline'ach przetwarzania,
- danych, których nie musisz mieć wszystkich jednocześnie.

## Najprostsza intuicja

### Wersja ciężka

- wczytaj wszystko,
- trzymaj wszystko w pamięci,
- dopiero potem przetwarzaj.

### Wersja streamingowa

- pobierz element,
- przetwórz,
- przejdź dalej,
- nie trzymaj całego świata na raz.

## Dlaczego to jest ważne

Bo bardzo wiele problemów z wydajnością to nie tylko kwestia CPU, ale też pamięci i modelu przetwarzania.

Jeśli ładujesz ogromny plik albo milion rekordów naraz, możesz:

- zużywać za dużo RAM,
- spowalniać program,
- generować niepotrzebny koszt GC,
- utrudniać skalowanie rozwiązania.

## Prosty przykład: zła wersja

```python
with open("duzy_plik.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    process(line)
```

To jest wygodne, ale trzyma wszystkie linie na raz.

## Lepszy kierunek: iteracja po pliku

```python
with open("duzy_plik.txt", "r", encoding="utf-8") as f:
    for line in f:
        process(line)
```

To klasyczny i bardzo dobry przykład streamingu.

## Generator jako narzędzie streamingu

Generatory bardzo dobrze wspierają streaming.

```python
def numbers():
    for i in range(5):
        yield i

for x in numbers():
    print(x)
```

Output:

```python
0
1
2
3
4
```

Elementy powstają wtedy, gdy są potrzebne.

## Pipeline danych

Streaming świetnie działa, gdy budujesz przetwarzanie etapowe.

Przykład ideowy:

- czytasz linie,
- filtrujesz,
- parsujesz,
- agregujesz,
- zapisujesz wynik.

Nie zawsze trzeba wszystko materializować do listy po każdym kroku.

## Kiedy streaming ma sens

Szczególnie gdy:

- dane są duże,
- wejście jest strumieniem,
- nie potrzebujesz wszystkich elementów naraz,
- chcesz ograniczyć zużycie pamięci,
- budujesz pipeline przetwarzania.

## Kiedy pełne wczytanie może być OK

Nie zawsze streaming jest konieczny.

Jeśli:

- dane są małe,
- potrzebujesz wielokrotnego dostępu losowego,
- prostota kodu jest ważniejsza,
- koszt pamięci jest pomijalny,

pełne wczytanie może być całkowicie rozsądnym wyborem.

## Mini case study

Masz plik 10 GB i próbujesz zrobić:

```python
lines = f.readlines()
```

To problem nie tylko techniczny, ale projektowy.

Prawdziwe pytanie brzmi:

- czy naprawdę muszę mieć wszystkie linie jednocześnie?

Jeśli nie, to streaming jest często naturalną odpowiedzią.

## Typowe błędy początkujących

- wczytywanie wszystkiego z przyzwyczajenia,
- zamienianie generatorów na listę bez potrzeby,
- brak refleksji, czy wszystkie dane są potrzebne jednocześnie,
- mylenie prostoty implementacyjnej z dobrą architekturą przetwarzania.

## Szybka ściąga

- streaming = przetwarzanie etapowe bez trzymania wszystkiego naraz,
- generatory i iteracja po plikach świetnie to wspierają,
- daje zyski głównie w pamięci i skalowalności,
- nie zawsze jest konieczny, ale często jest bardzo sensowny.

## Ćwiczenia

1. Porównaj `readlines()` z iteracją po pliku.
2. Napisz prosty generator filtrujący dane.
3. Zbuduj mały pipeline generatorów.
4. Opisz przypadek, gdzie streaming ma przewagę nad listą.
5. Wskaż sytuację, w której pełne wczytanie danych nadal jest rozsądne.

## Najważniejsze do zapamiętania

- Streaming pomaga ograniczyć zużycie pamięci.
- Jest bardzo ważny przy dużych danych i długich pipeline'ach.
- Generatory są jednym z najpraktyczniejszych narzędzi do streamingu w Pythonie.
- Nie trzeba wszystkiego streamować, ale warto umieć rozpoznać moment, kiedy to ma sens.
- To często poprawa modelu przetwarzania, nie tylko wydajności jednej funkcji.
