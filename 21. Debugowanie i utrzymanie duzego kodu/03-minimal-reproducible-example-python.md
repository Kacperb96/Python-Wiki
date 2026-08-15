# Minimal reproducible example w Pythonie

## O co chodzi

Minimal reproducible example, czyli MRE, to możliwie najmniejszy przykład, który nadal odtwarza problem.

To jedna z najpotężniejszych technik debugowania.

Bo kiedy umiesz sprowadzić problem do małego przykładu, zwykle:

- lepiej rozumiesz błąd,
- szybciej widzisz przyczynę,
- łatwiej prosisz kogoś o pomoc,
- łatwiej sprawdzasz poprawkę.

## Co znaczy "minimal"

Minimal nie znaczy byle jaki skrót.

To znaczy:

- wywal wszystko, co nie jest potrzebne do wystąpienia błędu,
- zostaw tylko to, co naprawdę tworzy problem.

## Co znaczy "reproducible"

To znaczy, że przykład naprawdę odtwarza błąd.

Nie:

- "u mnie czasem się dzieje",

ale:

- "jeśli uruchomisz to tak, dostaniesz ten konkretny problem".

## Dlaczego MRE jest tak ważne

Bo duży system zaciemnia obraz.

Jeśli bug występuje w 20-modułowej aplikacji, to nie znaczy, że musisz debugować od razu wszystkie 20 modułów.

Często problem da się sprowadzić do:

- jednej funkcji,
- jednego wejścia,
- jednego warunku,
- jednego modelu danych.

## Jak tworzyć MRE

Bardzo praktyczny proces:

1. odtwórz błąd,
2. usuń nieistotne części,
3. uprość dane wejściowe,
4. usuń frameworkowy szum,
5. zostaw tylko to, co nadal powoduje problem.

## Przykład intuicyjny

Masz błąd w aplikacji webowej.

Zamiast od razu odpalać cały serwer, bazę i integracje, możesz często sprowadzić problem do:

- jednej funkcji parsera,
- jednego obiektu wejściowego,
- jednego błędnego wywołania.

To właśnie jest MRE.

## Przykład: za duży przypadek

```python
# wielki endpoint
# baza
# logowanie
# serializacja
# walidacja
# kilka serwisów
# bug gdzieś po drodze
```

Tak się bardzo źle diagnozuje problem.

## Przykład: lepszy MRE

```python
def normalize_price(value: str) -> float:
    return float(value.replace(",", "."))

print(normalize_price("12,50"))
```

Jeśli to tu siedzi problem, nie potrzebujesz całej aplikacji do jego odtworzenia.

## Dlaczego MRE często samo ujawnia błąd

To bardzo ciekawe zjawisko.

W trakcie upraszczania przykładu często nagle widzisz:

- która wartość jest zła,
- który warunek jest zbędny,
- który krok psuje dane,
- gdzie założenie było błędne.

Czyli samo tworzenie MRE bywa połową rozwiązania.

## MRE a pytanie o pomoc

Jeśli chcesz poprosić innego programistę o pomoc, MRE jest ogromnie ważne.

Porównaj:

### Zły styl

- "w moim projekcie coś nie działa, tu jest 14 plików"

### Dobry styl

- "tu jest 15-liniowy przykład, który pokazuje problem"

Druga forma jest wielokrotnie bardziej użyteczna.

## Typowe błędy początkujących

- przykład nadal za duży,
- brak dokładnego wejścia powodującego błąd,
- zostawienie zbyt wielu zależności,
- mylenie MRE z ogólnym opisem problemu,
- brak sprawdzenia, czy uproszczony przykład nadal naprawdę odtwarza błąd.

## Mini case study

Bug występuje przy imporcie CSV i tylko dla jednego rekordu.

Zamiast debugować cały import pipeline, możesz dojść do MRE w stylu:

```python
row = {"price": "12,50", "count": "x"}
parse_row(row)
```

Teraz problem jest mały, konkretny i da się z nim pracować.

## Szybka ściąga

- MRE to najmniejszy przykład, który nadal odtwarza problem,
- usuń wszystko, co nie wpływa na błąd,
- uprość dane i przepływ,
- sprawdź, że przykład nadal naprawdę działa jako reprodukcja,
- MRE bardzo pomaga zarówno w debugowaniu, jak i proszeniu o pomoc.

## Ćwiczenia

1. Weź duży przypadek i opisz, jak zmniejszyłbyś go do MRE.
2. Zrób własny mały przykład błędu i uprość go maksymalnie.
3. Porównaj zły i dobry opis problemu do innego programisty.
4. Wskaż, jakie elementy najczęściej można usunąć przy budowie MRE.
5. Opisz, czemu MRE bywa połową rozwiązania.

## Najważniejsze do zapamiętania

- Minimal reproducible example to jedno z najlepszych narzędzi debugowania.
- Dobry MRE jest mały, konkretny i naprawdę odtwarza błąd.
- Upraszczanie problemu bardzo często prowadzi do jego zrozumienia.
- MRE pomaga zarówno Tobie, jak i innym osobom analizującym problem.
- Jeśli nie potrafisz zrobić MRE, problem często nadal jest zbyt słabo zrozumiany.
