# Bezpieczne użycie `subprocess` w Pythonie

## Dlaczego `subprocess` jest wrażliwy

Moduł `subprocess` pozwala uruchamiać zewnętrzne procesy systemowe.

To bardzo przydatne, ale jednocześnie niebezpieczne, bo przekraczasz granicę między aplikacją a systemem operacyjnym.

Jeśli zrobisz to źle, możesz doprowadzić do:

- command injection,
- wykonania niechcianych poleceń,
- usunięcia lub ujawnienia danych,
- zawieszenia procesu,
- trudnych do kontroli efektów ubocznych.

## Najważniejsza zasada

Jeśli do komendy trafiają dane od użytkownika, musisz być bardzo ostrożny.

W praktyce najbezpieczniejszy nawyk to:

- przekazywać polecenie jako listę argumentów,
- unikać `shell=True`, jeśli nie jest konieczne.

## Lista argumentów vs string polecenia

### Bezpieczniejszy wzorzec

```python
import subprocess

result = subprocess.run(["echo", "hello"], capture_output=True, text=True, check=True)
print(result.stdout)
```

Output:

```python
hello
```

### Mniej bezpieczny wzorzec

```python
subprocess.run("echo hello", shell=True)
```

To może działać, ale shell interpretuje cały string. Przy danych zewnętrznych robi się groźnie.

## Gdzie zaczyna się problem

### Zły przykład

```python
import subprocess

filename = input("Podaj nazwe pliku: ")
subprocess.run(f"cat {filename}", shell=True)
```

Jeśli użytkownik wpisze zwykłą nazwę, polecenie może wyglądać niewinnie.

Ale jeśli wpisze coś złośliwego, np. dodatkową komendę, shell może potraktować to jako więcej niż jedną operację.

To jest klasyczna droga do command injection.

## Bezpieczniejsza wersja

```python
import subprocess

filename = input("Podaj nazwe pliku: ")
subprocess.run(["cat", filename], check=True)
```

To nadal nie rozwiązuje wszystkich problemów, bo `filename` może być np. ścieżką do niepożądanego pliku, ale przynajmniej nie dajesz shellowi gotowego stringa do interpretacji.

## `shell=True` — kiedy ryzyko rośnie

`shell=True` nie jest automatycznie „złe” w każdym możliwym przypadku, ale bardzo zwiększa powierzchnię ryzyka.

Szczególnie gdy:

- komenda jest budowana dynamicznie,
- trafia do niej input użytkownika,
- nie masz pełnej kontroli nad argumentami,
- uruchamiasz coś z szerokimi uprawnieniami.

W praktyce, jeśli nie masz mocnego powodu, lepiej go unikać.

## `check=True`, `capture_output`, `text`

Te argumenty nie są stricte „bezpieczeństwem”, ale pomagają pisać bardziej przewidywalny kod.

### `check=True`

Jeśli proces zwróci błąd, dostaniesz wyjątek zamiast cichego niepowodzenia.

### `capture_output=True`

Pozwala przechwycić wynik procesu.

### `text=True`

Zwraca output jako string zamiast bajtów.

Przykład:

```python
import subprocess

result = subprocess.run(
    ["python3", "--version"],
    capture_output=True,
    text=True,
    check=True,
)
print(result.stdout.strip())
```

Przykładowy output:

```python
Python 3.x.x
```

## Timeout

Proces zewnętrzny może:

- zawiesić się,
- czekać zbyt długo,
- zablokować aplikację.

Dlatego często warto ustawiać timeout.

```python
import subprocess

subprocess.run(["sleep", "1"], timeout=2, check=True)
```

Jeśli proces potrwa za długo, dostaniesz wyjątek `TimeoutExpired`.

To nie jest tylko wygoda. To element odporności aplikacji.

## Walidacja argumentów

Nawet bez `shell=True` nadal trzeba kontrolować, co trafia do procesu.

Przykład:

- użytkownik wybiera jedną z dozwolonych komend,
- zamiast podawać dowolny tekst.

### Lepsze podejście: whitelist

```python
import subprocess

allowed_commands = {
    "list": ["ls", "-l"],
    "date": ["date"],
}

command_name = input("Podaj komendę: ")
if command_name not in allowed_commands:
    raise ValueError("Niedozwolona komenda")

subprocess.run(allowed_commands[command_name], check=True)
```

To dużo lepsze niż uruchamianie dowolnego stringa od użytkownika.

## Najczęstsze błędy początkujących

- używanie `shell=True` bez potrzeby,
- sklejanie komend przez f-string,
- brak walidacji argumentów,
- brak `check=True`,
- brak timeoutu,
- uruchamianie zbyt szerokich poleceń systemowych,
- brak świadomości, że proces zewnętrzny to duża odpowiedzialność.

## Zła i lepsza wersja

### Zła wersja

```python
user_input = input("Co wypisać? ")
subprocess.run(f"echo {user_input}", shell=True)
```

### Lepsza wersja

```python
user_input = input("Co wypisać? ")
subprocess.run(["echo", user_input], check=True)
```

### Jeszcze lepszy kierunek w niektórych przypadkach

Jeśli naprawdę nie potrzebujesz procesu systemowego, nie uruchamiaj go wcale.

```python
user_input = input("Co wypisać? ")
print(user_input)
```

To bardzo ważna lekcja: czasem najbezpieczniejsze użycie `subprocess` to jego brak.

## Checklista bezpiecznego `subprocess`

- Czy naprawdę potrzebuję `subprocess`?
- Czy mogę użyć listy argumentów?
- Czy mogę uniknąć `shell=True`?
- Czy argumenty są pod kontrolą?
- Czy ustawiłem `check=True`?
- Czy ustawiłem timeout?
- Czy rozumiem, co dokładnie uruchamiam?

## Szybka ściąga

Przy `subprocess` pamiętaj:

- preferuj listę argumentów,
- unikaj `shell=True`,
- nie sklejaj poleceń z inputem użytkownika,
- waliduj dozwolone opcje,
- kontroluj błędy i czas wykonania.

## Ćwiczenia

1. Napisz przykład bezpieczniejszego `subprocess.run()` z listą argumentów.
2. Pokaż ryzykowną wersję z `shell=True` i wyjaśnij zagrożenie.
3. Dodaj timeout do przykładowego procesu.
4. Zbuduj prostą whitelistę dwóch dozwolonych komend.
5. Znajdź przypadek, gdzie `subprocess` można zastąpić zwykłym Pythonem.

## Najważniejsze do zapamiętania

- `subprocess` to kontakt z systemem operacyjnym, więc wymaga ostrożności.
- Najbezpieczniej przekazywać polecenie jako listę argumentów.
- `shell=True` znacząco zwiększa ryzyko przy dynamicznych danych.
- Walidacja argumentów i whitelisty są bardzo pomocne.
- Czasem najlepszym rozwiązaniem jest w ogóle nie używać `subprocess`.
