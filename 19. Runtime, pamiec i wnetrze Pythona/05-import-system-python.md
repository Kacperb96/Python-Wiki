# System importów w Pythonie

## O co chodzi

Import w Pythonie to nie jest tylko "wklejenie kodu z innego pliku".

To bardziej złożony mechanizm, który:

- znajduje moduł,
- ładuje go,
- wykonuje jego kod,
- zapisuje wynik w cache modułów,
- udostępnia go dalej programowi.

To bardzo ważne, bo od razu tłumaczy wiele praktycznych zjawisk.

## Najważniejsza rzecz do zapamiętania

Import wykonuje kod modułu.

To znaczy, że jeśli na najwyższym poziomie pliku masz jakiś kod, to może on uruchomić się przy imporcie.

## Prosty przykład

Plik `modul.py`:

```python
print("Importuje modul")

value = 42
```

Plik `main.py`:

```python
import modul
print(modul.value)
```

Output:

```python
Importuje modul
42
```

Widzisz, że sam import uruchomił kod modułu.

## Eksperyment 1: efekt uboczny przy imporcie

Plik `config.py`:

```python
print("Laduje konfiguracje...")
CONFIG = {"debug": True}
```

Plik `app.py`:

```python
import config
print("Start aplikacji")
```

Output:

```python
Laduje konfiguracje...
Start aplikacji
```

To tłumaczy, czemu czasem aplikacja "coś robi" jeszcze zanim dojdzie do właściwej logiki programu.

## Dlaczego to jest ważne

Bo jeśli w module na poziomie globalnym robisz ciężkie albo niebezpieczne rzeczy, to one też wykonają się przy imporcie.

Przykłady ryzyka:

- połączenie z bazą przy imporcie,
- odpalanie requestów HTTP,
- kosztowne obliczenia,
- konfiguracja z efektami ubocznymi,
- logika, która powinna siedzieć w funkcji, a nie na poziomie modułu.

## Cache modułów

Python nie importuje modułu od zera za każdym razem.

Po załadowaniu moduł trafia do cache modułów i kolejne importy zwykle korzystają z już załadowanej wersji.

To ważne, bo:

- kod modułu nie wykonuje się w nieskończoność przy każdym imporcie,
- ale pierwszy import może mieć istotne skutki uboczne.

## Eksperyment 2: moduł nie wykonuje się w kółko

Plik `tools.py`:

```python
print("Pierwsze ladowanie tools")
```

Plik `main.py`:

```python
import tools
import tools
print("Koniec")
```

Typowy output:

```python
Pierwsze ladowanie tools
Koniec
```

To pokazuje praktycznie ideę cache modułów.

## `if __name__ == "__main__"`

To klasyczny sposób na oddzielenie:

- kodu wykonywanego przy bezpośrednim uruchomieniu pliku,
- od kodu wykonywanego tylko przy imporcie.

Przykład:

```python
def main() -> None:
    print("Uruchomiono jako program")


if __name__ == "__main__":
    main()
```

To bardzo dobra praktyka przy modułach, które mogą być i importowane, i uruchamiane bezpośrednio.

## Jak Python znajduje moduł

W uproszczeniu Python przeszukuje określone miejsca, żeby znaleźć moduł o danej nazwie.

To obejmuje m.in.:

- bieżący projekt,
- katalogi na ścieżce importów,
- zainstalowane paczki.

Dlatego struktura projektu i nazwy plików mają realne znaczenie.

## Najczęstsze problemy z importami

- cykliczne importy,
- ciężki kod wykonywany przy imporcie,
- konflikt nazw modułów,
- nieintuicyjne zachowanie wynikające z tego, że kod modułu wykonał się wcześniej,
- trudności z lokalną strukturą pakietów.

## Cykliczne importy

To klasyczny problem.

Jeśli moduł A importuje B, a B importuje A i oba oczekują od razu gotowych definicji, może zrobić się bałagan.

To często sygnał, że:

- struktura modułów jest zbyt mocno sprzężona,
- trzeba coś wydzielić,
- import powinien zostać przeniesiony,
- architektura wymaga uporządkowania.

## Mini case study: "skąd ten print przy starcie programu?"

Ktoś uruchamia aplikację i jeszcze przed logiem `Start` widzi:

```text
Laduje konfiguracje...
```

Podejrzenie:

- "czy to framework coś robi?"

Wyjaśnienie runtime może być dużo prostsze:

- jakiś moduł ma kod globalny,
- importuje się przy starcie,
- import wykonuje kod modułu,
- więc print pojawia się jeszcze przed logiką aplikacji.

## Mini case study: "czemu drugi import nic nie wypisał?"

Ktoś oczekuje, że:

```python
import tools
import tools
```

dwa razy wykona kod modułu.

A output pojawia się tylko raz.

Wyjaśnienie:

- pierwszy import ładuje i cache'uje moduł,
- drugi korzysta już z załadowanej wersji.

## Kiedy ta wiedza ma sens praktycznie

Szczególnie gdy:

- projekt rośnie,
- masz wiele modułów i pakietów,
- pojawiają się dziwne efekty uboczne przy starcie aplikacji,
- walczysz z import errors albo circular imports,
- chcesz lepiej projektować strukturę kodu.

## Typowe błędy początkujących

- traktowanie importu jak czysto deklaratywnego mechanizmu bez efektów ubocznych,
- zostawianie ciężkiej logiki na poziomie modułu,
- brak `if __name__ == "__main__"` tam, gdzie ma sens,
- chaotyczna struktura pakietów,
- panika przy circular imports bez szukania przyczyny architektonicznej.

## Szybka ściąga

- import ładuje i wykonuje kod modułu,
- pierwszy import ma znaczenie szczególnie przy efektach ubocznych,
- moduły trafiają do cache,
- `if __name__ == "__main__"` pomaga oddzielić tryb uruchomienia od trybu importu,
- problemy z importami często są też problemami struktury projektu.

## Ćwiczenia

1. Zrób moduł, który coś wypisuje przy imporcie.
2. Pokaż, jak działa `if __name__ == "__main__"`.
3. Opisz, czemu ciężki kod globalny w module jest złą praktyką.
4. Wyjaśnij intuicyjnie, czym jest circular import.
5. Przejrzyj mały projekt i wskaż, gdzie import może mieć skutki uboczne.

## Najważniejsze do zapamiętania

- Import w Pythonie wykonuje kod modułu.
- To tłumaczy skutki uboczne przy starcie programu.
- `if __name__ == "__main__"` to bardzo praktyczny wzorzec.
- Problemy z importami często ujawniają problemy architektoniczne.
- Dobra struktura modułów bardzo ułatwia pracę z import systemem.
