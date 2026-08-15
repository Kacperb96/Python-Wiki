# Profilowanie w Pythonie

## O co chodzi

Profilowanie to szukanie odpowiedzi na pytanie:

- gdzie naprawdę znika czas wykonania programu?

To znacznie lepsze niż zgadywanie.

Benchmark mówi Ci zwykle:

- które rozwiązanie jest szybsze.

Profilowanie mówi:

- gdzie jest wąskie gardło.

Obie rzeczy są ważne, ale to nie to samo.

## Najprostsza intuicja

Benchmark porównuje.

Profilowanie diagnozuje.

## Dlaczego profilowanie jest ważne

Bez profilowania bardzo łatwo naprawiać zły fragment.

Na przykład:

- optymalizujesz 5% kosztu,
- a 80% czasu siedzi w innym miejscu.

To klasyczny błąd.

## Co może pokazać profilowanie

Na przykład:

- która funkcja zużywa najwięcej czasu,
- która wywoływana jest najczęściej,
- gdzie koszt się kumuluje,
- czy problem siedzi w jednej funkcji czy w całym przepływie.

## Profilowanie a intuicja

Bardzo często kod, który wygląda na najcięższy, nie jest realnym hot spotem.

A czasem niepozorna mała funkcja wywoływana setki tysięcy razy okazuje się głównym kosztem.

Dlatego profilowanie jest tak cenne.

## Prosty przykład mentalny

Masz funkcję główną, która:

- czyta dane,
- parsuje je,
- filtruje,
- sortuje,
- zapisuje wynik.

Może Ci się wydawać, że problem siedzi w parsowaniu, ale profilowanie pokaże, że np. największy koszt robi sortowanie albo niepotrzebne powtórne przeliczanie czegoś w pętli.

## Co z profilem czasu, a co z profilem pamięci

To dwa różne pytania.

### Profil czasu

Pyta:

- gdzie program spędza czas?

### Profil pamięci

Pyta:

- gdzie program zużywa pamięć,
- które struktury są za duże,
- gdzie powstają niepotrzebne kopie,
- które etapy utrzymują dane zbyt długo.

Bardzo często ludzie mieszają te dwa problemy.

Kod może być:

- czasowo w porządku, ale pamięciowo fatalny,
- albo pamięciowo lekki, ale czasowo zbyt wolny.

## Typowe źródła kosztu czasu

W Pythonie często hot spoty siedzą w:

- zbyt dużej liczbie wywołań funkcji,
- złym algorytmie,
- powtarzaniu tej samej pracy,
- niepotrzebnych konwersjach,
- kosztownych operacjach I/O,
- błędnym modelu danych.

## Typowe źródła kosztu pamięci

- pełne wczytanie dużych danych,
- tworzenie wielu list pośrednich,
- cache bez kontroli,
- ciężkie modele obiektów,
- trzymanie referencji dłużej niż trzeba,
- pipeline budujący wiele kopii tych samych danych.

## Profilowanie a benchmark

### Benchmark

Dobre pytanie:

- która z tych dwóch wersji jest szybsza?

### Profilowanie

Dobre pytanie:

- gdzie program naprawdę spędza czas lub pamięć?

To trzeba umieć rozdzielać.

## Case study: wolny moduł poprawiany krok po kroku

Załóżmy prosty moduł analizujący logi.

### Wersja 1: naiwny kod

```python
def load_lines(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        return f.readlines()


def parse_errors(lines: list[str]) -> list[str]:
    errors = []
    for line in lines:
        if "ERROR" in line:
            errors.append(line.strip())
    return errors


def count_by_message(errors: list[str]) -> dict[str, int]:
    result = {}
    for line in errors:
        if line not in result:
            result[line] = 0
        result[line] += 1
    return result
```

Na pierwszy rzut oka wygląda OK.

### Podejrzenia bez profilowania

Ktoś może powiedzieć:

- "pewnie problem jest w `if \"ERROR\" in line`",
- albo "zróbmy regex, będzie szybciej",
- albo "trzeba to przepisać na coś sprytniejszego".

To zgadywanie.

### Diagnoza czasowa

Po profilowaniu może się okazać, że:

- największy koszt jest w `readlines()` dla ogromnego pliku,
- potem w kosztownym trzymaniu wszystkiego naraz,
- a nie w samym `if`.

### Diagnoza pamięciowa

Może się też okazać, że:

- problemem nie jest głównie czas,
- tylko fakt, że `load_lines()` ładuje cały plik do pamięci,
- potem `parse_errors()` tworzy drugą dużą listę,
- a `count_by_message()` dopiero po tym robi agregację.

### Wersja 2: poprawka architektoniczna

```python
def iter_lines(path: str):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line


def count_errors(path: str) -> dict[str, int]:
    result: dict[str, int] = {}
    for line in iter_lines(path):
        if "ERROR" in line:
            normalized = line.strip()
            result[normalized] = result.get(normalized, 0) + 1
    return result
```

### Co się poprawiło

- nie ładujesz całego pliku naraz,
- nie tworzysz dodatkowej listy błędów,
- robisz agregację od razu,
- zmniejszasz koszt pamięci,
- często poprawiasz też czas przez mniejszą liczbę obiektów pośrednich.

### Najważniejsza lekcja

Największa poprawka nie wynikała z mikrooptymalizacji jednej linijki.

Wynikała z:

- lepszego modelu przetwarzania,
- streamingu,
- ograniczenia danych pośrednich.

To jest właśnie prawdziwe performance engineering.

## Kiedy profilować

Szczególnie gdy:

- program realnie działa za wolno,
- nie wiesz, gdzie jest hot spot,
- chcesz potwierdzić podejrzenia,
- po zmianie chcesz sprawdzić, czy poprawiłeś właściwy fragment.

## Kiedy nie profilować obsesyjnie

Nie każdy mały skrypt potrzebuje zaawansowanego profilowania.

Jeśli problem jest oczywisty i mały, czasem wystarczy prosta poprawka. Ale gdy pojawia się realny koszt i niepewność, profilowanie staje się bardzo rozsądne.

## Mini case study

Masz kod, który wygląda niewinnie:

- jedna funkcja filtruje,
- druga mapuje,
- trzecia liczy coś w środku pętli.

Po profilowaniu okazuje się, że problemem nie jest filtr, tylko funkcja pomocnicza uruchamiana milion razy.

To właśnie klasyczny moment, w którym profilowanie wygrywa z intuicją.

## Typowe błędy początkujących

- brak profilowania przed optymalizacją,
- poprawianie "na czuja",
- zakładanie, że najdłuższy fragment kodu wizualnie jest najdroższy,
- mylenie liczby wywołań z całkowitym kosztem,
- brak porównania przed i po poprawce,
- brak rozróżnienia między profilem czasu a profilem pamięci.

## Co robić po profilowaniu

Profilowanie samo w sobie nie jest celem.

Po nim trzeba:

1. wskazać hot spot,
2. zrozumieć jego przyczynę,
3. dobrać poprawkę,
4. zmierzyć efekt po zmianie.

To bardzo ważny workflow.

## Szybka ściąga

- profilowanie pokazuje, gdzie znika czas lub pamięć,
- nie zastępuje benchmarków,
- pomaga znaleźć hot spoty,
- chroni przed optymalizacją nie tego miejsca, co trzeba,
- powinno prowadzić do konkretnej poprawki i ponownego pomiaru.

## Ćwiczenia

1. Opisz różnicę między benchmarkiem i profilowaniem.
2. Podaj przykład sytuacji, gdzie intuicja może wskazać zły hot spot.
3. Rozpisz workflow: profilowanie -> poprawka -> pomiar po zmianie.
4. Wskaż 5 możliwych źródeł kosztu w Pythonie.
5. Opisz przypadek, gdzie funkcja wywoływana bardzo często robi większy koszt niż jedna duża operacja.

## Najważniejsze do zapamiętania

- Profilowanie służy do diagnozy, nie do zgadywania.
- Pokazuje, gdzie program naprawdę spędza czas lub pamięć.
- Bardzo często obala intuicję programisty.
- Powinno prowadzić do celowanej poprawki.
- Bez profilowania łatwo optymalizować nie to, co trzeba.
