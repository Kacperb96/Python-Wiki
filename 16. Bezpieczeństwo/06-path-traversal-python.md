# Path traversal w Pythonie

## Czym jest path traversal

Path traversal to błąd bezpieczeństwa, w którym użytkownik wpływa na ścieżkę pliku i może wyjść poza dozwolony katalog.

Najczęściej kojarzy się z fragmentami takimi jak:

- `../`
- `..\\`

ale problem jest szerszy niż same te ciągi.

Chodzi o to, że aplikacja:

- przyjmuje nazwę lub ścieżkę od użytkownika,
- buduje na jej podstawie finalną ścieżkę,
- a potem bez kontroli odczytuje lub zapisuje plik.

## Typowy scenariusz problemu

Aplikacja ma udostępniać pliki tylko z katalogu `uploads/`.

Programista pisze coś takiego:

```python
def read_user_file(filename):
    path = f"uploads/{filename}"
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
```

Jeśli użytkownik poda:

```python
raport.txt
```

wszystko wygląda dobrze.

Ale jeśli poda:

```python
../../sekrety.txt
```

aplikacja może spróbować sięgnąć poza `uploads/`.

## Dlaczego to jest groźne

Taki błąd może prowadzić do:

- odczytu wrażliwych plików,
- nadpisania plików systemowych lub aplikacyjnych,
- ujawnienia konfiguracji,
- ujawnienia sekretów,
- wycieku danych innych użytkowników.

## Problem nie kończy się na `../`

Początkujący często myślą, że wystarczy sprawdzić, czy input nie zawiera `../`.

To za mało.

Dlaczego?

- istnieją różne reprezentacje ścieżek,
- systemy operacyjne różnią się separatorami,
- można próbować obejść proste filtry,
- sama nazwa pliku może być problematyczna.

Potrzebujesz bezpieczniejszego modelu, a nie tylko prostego `replace()`.

## Zły przykład

```python
def get_path(filename):
    return "uploads/" + filename
```

To jest zły wzorzec, bo:

- ścieżka jest składana jako zwykły string,
- brak normalizacji,
- brak sprawdzenia katalogu bazowego,
- brak ograniczenia do bezpiecznego zakresu.

## Lepszy kierunek z `pathlib`

```python
from pathlib import Path

BASE_DIR = Path("uploads").resolve()


def get_safe_path(filename: str) -> Path:
    candidate = (BASE_DIR / filename).resolve()

    if BASE_DIR not in candidate.parents and candidate != BASE_DIR:
        raise ValueError("Niedozwolona sciezka")

    return candidate
```

Ta wersja:

- pracuje na obiektach ścieżek,
- normalizuje finalną ścieżkę przez `resolve()`,
- sprawdza, czy wynik nadal znajduje się w dozwolonym katalogu bazowym.

## Przykład działania

```python
print(get_safe_path("raport.txt"))
```

Przykładowy efekt:

```python
/home/user/project/uploads/raport.txt
```

A dla niedozwolonej ścieżki:

```python
get_safe_path("../../sekrety.txt")
```

Efekt:

```python
ValueError: Niedozwolona sciezka
```

## Jeszcze lepszy model: nie ufaj nazwie ścieżki wcale

W wielu systemach najbezpieczniejsze jest to, żeby użytkownik nie podawał ścieżki pliku bezpośrednio.

Lepszy model:

- użytkownik podaje identyfikator pliku,
- aplikacja sama mapuje ID na znaną ścieżkę.

Przykład:

- zamiast `../../sekrety.txt`, użytkownik podaje `file_id=42`,
- a aplikacja sama znajduje plik przypisany do tego rekordu.

To zwykle bezpieczniejsze niż przyjmowanie dowolnej nazwy ścieżki.

## Walidacja nazw plików

Dodatkowa warstwa ochrony może obejmować:

- dozwolone rozszerzenia,
- ograniczenie znaków w nazwie,
- zakaz ścieżek absolutnych,
- długość nazwy,
- whitelistę formatów.

Przykład prostego ograniczenia:

```python
def validate_filename(filename: str) -> str:
    if "/" in filename or "\\" in filename:
        raise ValueError("Nazwa pliku nie moze zawierac separatorow")

    if not filename.endswith(".txt"):
        raise ValueError("Dozwolone sa tylko pliki .txt")

    return filename
```

To nie zastępuje kontroli katalogu bazowego, ale może być dodatkową warstwą ochrony.

## Odczyt i zapis

Path traversal dotyczy nie tylko odczytu.

Może też dotyczyć zapisu.

To znaczy, że użytkownik może próbować:

- nadpisać ważny plik,
- zapisać plik w nieautoryzowane miejsce,
- przygotować grunt pod dalszy atak.

Dlatego te same zasady stosują się także do operacji zapisu.

## Typowe błędy początkujących

- sklejanie ścieżek jako stringów,
- zaufanie nazwie pliku od użytkownika,
- sprawdzanie tylko `../` i nic więcej,
- brak jawnego katalogu bazowego,
- brak walidacji rozszerzeń lub formatu nazwy,
- nieodróżnianie nazwy pliku od pełnej ścieżki.

## Checklista ochrony przed path traversal

- Czy użytkownik podaje nazwę pliku lub ścieżkę?
- Czy mam katalog bazowy?
- Czy normalizuję finalną ścieżkę?
- Czy sprawdzam, że wynik nadal mieści się w dozwolonym katalogu?
- Czy mogę użyć ID zamiast ścieżki?
- Czy ograniczam format nazw i rozszerzenia?

## Szybka ściąga

Przy plikach pamiętaj:

- nie ufaj ścieżce od użytkownika,
- nie sklejaj jej bezpośrednio jako stringa,
- używaj katalogu bazowego,
- normalizuj ścieżkę,
- sprawdzaj, czy wynik nie wychodzi poza dozwolony obszar,
- jeśli można, pracuj na ID zamiast ścieżkach od użytkownika.

## Ćwiczenia

1. Napisz podatną funkcję odczytującą plik po nazwie.
2. Popraw ją przez `pathlib` i kontrolę katalogu bazowego.
3. Dodaj walidację rozszerzenia `.txt`.
4. Zaprojektuj model, w którym użytkownik podaje ID pliku zamiast ścieżki.
5. Opisz ryzyko związane z zapisem pliku w niekontrolowane miejsce.

## Najważniejsze do zapamiętania

- Path traversal to możliwość wyjścia poza dozwolony katalog przy pracy z plikami.
- Samo filtrowanie `../` nie wystarcza.
- Bezpieczniejszy model opiera się na katalogu bazowym i normalizacji ścieżek.
- `pathlib` poprawia czytelność, ale bezpieczeństwo nadal wymaga jawnych kontroli.
- W wielu przypadkach najlepiej nie przyjmować ścieżki od użytkownika wprost.
