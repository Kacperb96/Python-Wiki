# Optymalizacja pamięci w Pythonie

## O co chodzi

Performance to nie tylko czas wykonania.

Bardzo często problemem jest też pamięć:

- program trzyma za dużo danych,
- tworzy zbyt wiele pośrednich obiektów,
- wykonuje niepotrzebne kopie,
- ładuje wszystko naraz,
- utrzymuje obiekty dłużej niż trzeba.

To wszystko może realnie spowalniać program i utrudniać jego skalowanie.

## Najprostsza intuicja

Kod może być wolny nie tylko dlatego, że dużo liczy.

Może być wolny także dlatego, że:

- za dużo pamięta,
- za dużo kopiuje,
- za dużo alokuje.

## Najczęstsze źródła problemów pamięciowych

- pełne wczytywanie dużych danych,
- niepotrzebne listy pośrednie,
- kopiowanie struktur bez potrzeby,
- cache bez kontroli,
- trzymanie referencji do obiektów zbyt długo,
- bardzo ciężkie modele danych.

## Prosty przykład: lista vs generator

```python
numbers = [x * 2 for x in range(1000000)]
```

To od razu buduje dużą listę w pamięci.

Alternatywa:

```python
numbers = (x * 2 for x in range(1000000))
```

To generator, który produkuje dane stopniowo.

To nie zawsze rozwiązuje wszystko, ale bardzo często zmniejsza koszt pamięci.

## Eksperyment: czas vs pamięć

Pomyśl o takim porównaniu:

```python
sum([x * 2 for x in range(1000000)])
```

vs

```python
sum(x * 2 for x in range(1000000))
```

Możliwa interpretacja:

- lista bywa szybsza czasowo w części środowisk,
- generator bywa lżejszy pamięciowo,
- decyzja nie jest więc tylko pytaniem o czas.

To świetny przykład, że profil czasu i profil pamięci mogą prowadzić do innych decyzji.

## Niepotrzebne kopie

To bardzo częsty problem.

Jeśli w pipeline'ie kilka razy tworzysz nowe listy tylko po to, żeby zaraz je przetworzyć dalej, możesz niepotrzebnie pompować pamięć.

Warto pytać:

- czy ta kopia jest naprawdę potrzebna,
- czy ten krok może działać na iteratorze,
- czy potrzebuję pełnej materializacji danych na tym etapie.

## Ciężkie modele danych

Nie każdy problem pamięciowy wynika z jednego wielkiego pliku.

Czasem problemem jest to, że:

- masz milion małych obiektów,
- każdy ma sporo overheadu,
- struktura danych jest cięższa niż potrzebujesz.

To szczególnie ważne przy dużej liczbie rekordów.

## Kiedy pamięć boli najbardziej

Szczególnie gdy:

- dane są duże,
- program działa długo,
- worker lub serwer musi obsługiwać wiele zadań,
- masz wiele równoległych procesów,
- struktury danych są przerośnięte.

## Pamięć a architektura

Czasem problem pamięci nie wynika z jednej linijki, tylko z modelu całego przetwarzania.

Przykłady:

- wszystko trzymane w RAM zamiast strumieniowo,
- pełne snapshoty danych zamiast batchy,
- wielokrotne kopiowanie rekordów między warstwami.

To oznacza, że optymalizacja pamięci bywa często decyzją architektoniczną, a nie tylko lokalnym trikiem.

## Case study: profil czasu mówi jedno, profil pamięci drugie

Masz moduł analizujący duży plik.

### Wersja A

- wczytuje wszystko do listy,
- potem robi kilka przebiegów,
- działa dość szybko,
- ale zużywa bardzo dużo RAM.

### Wersja B

- działa bardziej streamingowo,
- ma mniej danych pośrednich,
- może być minimalnie wolniejsza na małych danych,
- ale skaluje się lepiej pamięciowo.

Wniosek:

- jeśli patrzysz tylko na czas mikrobenchmarku, możesz wybrać złą wersję dla dużej skali,
- jeśli patrzysz tylko na pamięć, możesz przeoczyć realny koszt CPU.

Trzeba widzieć oba profile.

## Mini case study

Masz pipeline:

- wczytaj cały plik,
- zrób listę przefiltrowanych linii,
- zrób listę sparsowanych rekordów,
- zrób listę zmapowanych wyników.

Każdy etap tworzy kolejną dużą listę.

To może być czytelne, ale pamięciowo ciężkie.

Lepszy model może polegać na:

- iteracji etapami,
- generatorach,
- batchach,
- mniejszej liczbie materializacji.

## Typowe błędy początkujących

- budowanie ogromnych list z przyzwyczajenia,
- kopiowanie danych "na wszelki wypadek",
- ignorowanie kosztu pamięci, bo kod działa lokalnie na małym przykładzie,
- brak refleksji nad długością życia obiektów,
- patrzenie tylko na czas, bez pamięci.

## Szybka ściąga

- pamięć jest równie ważna jak czas,
- generatory i streaming pomagają ograniczyć zużycie RAM,
- niepotrzebne kopie to częsty ukryty koszt,
- ciężki model danych może być realnym problemem,
- optymalizacja pamięci bywa decyzją architektoniczną.

## Ćwiczenia

1. Porównaj listę i generator dla dużego zakresu danych.
2. Wskaż przykład niepotrzebnej kopii danych.
3. Opisz pipeline, który tworzy za dużo list pośrednich.
4. Zaproponuj wersję bardziej streamingową.
5. Podaj 3 sposoby ograniczania kosztu pamięci w projekcie.

## Najważniejsze do zapamiętania

- Wydajność to także pamięć, nie tylko czas.
- Duże struktury i kopie danych łatwo zabijają skalowalność.
- Generatory i streaming są bardzo ważnymi narzędziami pamięciowymi.
- Problem pamięci często siedzi w modelu przetwarzania.
- Dobra optymalizacja pamięci zaczyna się od pytania: czy naprawdę muszę trzymać to wszystko naraz?
