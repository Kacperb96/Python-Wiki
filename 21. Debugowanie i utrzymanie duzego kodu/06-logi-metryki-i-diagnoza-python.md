# Logi, metryki i diagnoza problemów w Pythonie

## O co chodzi

Kiedy problem występuje w działającym systemie, bardzo często nie masz luksusu pełnego debuggera i idealnej reprodukcji lokalnie.

Wtedy ogromnie ważne stają się:

- logi,
- metryki,
- obserwowalność przepływu systemu.

To one pomagają zrozumieć, co się dzieje w prawdziwym środowisku.

## Logi

Logi mówią Ci zwykle:

- co się wydarzyło,
- w jakiej kolejności,
- z jakimi danymi kontekstowymi,
- na jakim poziomie błędu lub informacji.

Dobre logi bardzo pomagają debugować bez wchodzenia od razu w cały kod.

## Metryki

Metryki pokazują bardziej zagregowany obraz systemu.

Na przykład:

- liczba błędów,
- czasy odpowiedzi,
- liczba requestów,
- użycie pamięci,
- liczba retry,
- długość kolejki.

Logi są często bardziej narracyjne. Metryki bardziej liczbowe i trendowe.

## Różnica praktyczna

### Logi pomagają odpowiedzieć

- co dokładnie stało się w konkretnym przypadku?

### Metryki pomagają odpowiedzieć

- czy problem jest częsty,
- kiedy się nasila,
- jak wpływa na system jako całość.

Obie rzeczy są bardzo ważne, ale odpowiadają na trochę inne pytania.

## Jak logować sensownie

Dobre logi powinny być:

- czytelne,
- kontekstowe,
- spójne,
- niezbyt hałaśliwe,
- bez wycieku sekretów i danych wrażliwych.

Bardzo ważne jest też to, żeby logi pomagały odpowiedzieć na konkretne pytania, a nie tylko zalewały terminal tekstem.

## Zły log

```python
print("tu jestem")
```

Taki komunikat prawie nic nie mówi.

## Lepszy log

```python
print(f"Tworzenie zamowienia dla user_id={user_id}, items_count={len(items)}")
```

To już daje kontekst.

W prawdziwym kodzie zwykle użyjesz loggera zamiast `print`, ale sama zasada pozostaje ta sama.

## Jakie pytania pomagają dobrać logi

- jaka operacja właśnie się zaczęła,
- jaki był kluczowy input,
- jaka decyzja została podjęta,
- jaki był wynik pośredni,
- gdzie przepływ się zatrzymał,
- jaki kontekst pozwoli później zrozumieć błąd.

## Metryki a diagnoza trendów

Jeśli widzisz pojedynczy błąd w logu, to jeszcze nie znaczy, że rozumiesz skalę problemu.

Metryki pomagają zobaczyć:

- czy błędów jest 1 czy 10 000,
- czy czas odpowiedzi rośnie,
- czy problem pojawia się po deployu,
- czy tylko jedna ścieżka systemu jest dotknięta.

## Mini case study

Objaw:

- użytkownicy mówią, że system "czasem wolno działa".

Bez logów i metryk trudno ruszyć.

Z logami możesz zobaczyć:

- które requesty są wolne,
- przy jakim wejściu,
- gdzie przepływ się zatrzymuje.

Z metrykami możesz zobaczyć:

- czy wzrost opóźnienia jest ogólny,
- czy tylko dla jednego endpointu,
- czy koreluje z obciążeniem albo deployem.

To razem daje dużo lepszą diagnozę.

## Kiedy ta wiedza ma sens

Szczególnie gdy:

- problem nie występuje lokalnie,
- system działa w środowisku produkcyjnym albo testowym,
- bug jest niestabilny albo trudny do odtworzenia,
- trzeba rozumieć trend, a nie tylko pojedynczy wyjątek.

## Typowe błędy początkujących

- zbyt mało kontekstu w logach,
- zbyt dużo hałasu bez informacji wartościowej,
- logowanie sekretów albo danych wrażliwych,
- brak rozróżnienia między problemem jednostkowym a trendem systemowym,
- brak myślenia, jakie pytania logi i metryki mają pomagać rozstrzygać.

## Szybka ściąga

- logi pokazują konkretne zdarzenia i kontekst,
- metryki pokazują trendy i skalę,
- dobre logi pomagają debugować realne przepływy,
- metryki pomagają rozpoznać, czy problem jest lokalny czy systemowy,
- diagnoza w dużym systemie bardzo często potrzebuje obu tych źródeł.

## Ćwiczenia

1. Napisz 3 słabe logi i popraw je na bardziej użyteczne.
2. Podaj 5 przykładów metryk, które warto śledzić w API.
3. Opisz przypadek, gdzie logi pomogą bardziej niż metryki.
4. Opisz przypadek, gdzie metryki pomogą bardziej niż pojedynczy log.
5. Zrób checklistę: co logować, a czego nie logować.

## Najważniejsze do zapamiętania

- Logi i metryki to podstawowe narzędzia diagnozy działającego systemu.
- Logi odpowiadają na pytanie „co się wydarzyło”, a metryki na pytanie „jak często i na jaką skalę”.
- Dobre logowanie wymaga kontekstu, nie tylko obecności tekstu.
- Złe logi potrafią bardziej przeszkadzać niż pomagać.
- W większych systemach bez logów i metryk debugowanie jest znacznie trudniejsze.
