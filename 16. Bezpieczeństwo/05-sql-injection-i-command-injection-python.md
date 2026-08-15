# SQL injection i command injection w Pythonie

## Czym jest injection

Injection to sytuacja, w której nieufne dane wejściowe stają się częścią wykonywanej instrukcji.

Zamiast być tylko zwykłą wartością, zaczynają wpływać na:

- treść zapytania SQL,
- strukturę komendy systemowej,
- logikę wykonania.

To jedna z najgroźniejszych klas błędów bezpieczeństwa, bo atakujący nie tylko podaje dane, ale próbuje sterować zachowaniem systemu.

## Dwie bardzo ważne odmiany

W praktyce Pythona bardzo często spotkasz:

- SQL injection,
- command injection.

Oba błędy mają wspólny rdzeń:

- program składa instrukcję z nieufnych danych,
- a potem ją wykonuje.

## SQL injection

### Na czym polega problem

Jeśli budujesz zapytanie SQL przez sklejanie stringa z danymi użytkownika, użytkownik może wpłynąć na treść zapytania.

### Zły przykład

```python
name = input("Podaj nazwę użytkownika: ")
query = f"SELECT * FROM users WHERE name = '{name}'"
print(query)
```

Jeśli użytkownik wpisze:

```python
Anna
```

output może wyglądać tak:

```python
SELECT * FROM users WHERE name = 'Anna'
```

To wygląda niewinnie.

Ale jeśli wpisze coś złośliwego, otrzymasz zupełnie inne zapytanie logiczne.

Problem nie polega na samym f-stringu jako takim, tylko na tym, że dane użytkownika trafiają do SQL jako część instrukcji.

## Bezpieczniejszy wzorzec: parametryzacja

```python
import sqlite3

conn = sqlite3.connect("app.db")
cur = conn.cursor()

name = input("Podaj nazwę użytkownika: ")
cur.execute("SELECT * FROM users WHERE name = ?", (name,))
rows = cur.fetchall()
print(rows)
```

Tutaj `name` jest przekazywane jako parametr, a nie jako fragment samodzielnie sklejonego SQL.

To podstawowa i najważniejsza obrona przed SQL injection.

## Dlaczego parametryzacja działa

Biblioteka do bazy dostaje osobno:

- treść zapytania,
- wartości parametrów.

Dzięki temu wartość użytkownika nie jest interpretowana jako dodatkowa składnia SQL.

To ogromna różnica.

## Błędne pomysły obrony

Czasem początkujący próbują:

- ręcznie usuwać pojedyncze znaki,
- samodzielnie escapować string,
- pisać własne „filtry anty-SQL injection”.

To zły kierunek.

Najlepsza praktyka to:

- parametryzacja,
- rozsądna walidacja,
- ograniczone uprawnienia bazy.

## Command injection

### Na czym polega problem

Jeśli budujesz komendę systemową z nieufnych danych i pozwalasz shellowi ją interpretować, użytkownik może wpłynąć na to, co naprawdę zostanie wykonane.

### Zły przykład

```python
import subprocess

user_input = input("Podaj tekst: ")
subprocess.run(f"echo {user_input}", shell=True)
```

Jeśli użytkownik poda zwykły tekst, polecenie wygląda niewinnie.

Jeśli jednak poda złośliwy ciąg, shell może zinterpretować go szerzej niż zwykłą wartość argumentu.

To właśnie command injection.

## Bezpieczniejszy wariant

```python
import subprocess

user_input = input("Podaj tekst: ")
subprocess.run(["echo", user_input], check=True)
```

Tutaj dane trafiają jako osobny argument, a nie jako część jednego stringa interpretowanego przez shell.

## SQL injection vs command injection

### Wspólne elementy

- dane zewnętrzne trafiają do wykonywanej instrukcji,
- program ufa inputowi za bardzo,
- instrukcja jest składana dynamicznie,
- skutki mogą być bardzo poważne.

### Różnica

- SQL injection atakuje warstwę bazy danych,
- command injection atakuje poziom systemu operacyjnego.

Command injection bywa szczególnie niebezpieczne, bo może prowadzić do wykonania niepożądanych poleceń na hostcie.

## Skąd biorą się te błędy

Najczęstsze przyczyny:

- ręczne sklejanie stringów,
- brak rozdzielenia instrukcji od danych,
- brak zaufania do bezpiecznych interfejsów bibliotecznych,
- chęć „szybkiego rozwiązania”,
- niedocenienie ryzyka, bo „to tylko wewnętrzne narzędzie”.

## Jak bronić się przed SQL injection

- używaj parametryzowanych zapytań,
- nie sklejaj SQL przez f-string lub `+`,
- waliduj dane wejściowe,
- nadawaj bazie minimalne potrzebne uprawnienia,
- jeśli używasz ORM, nadal rozumiej, gdzie kończy się bezpieczeństwo ORM-a.

## Jak bronić się przed command injection

- unikaj `shell=True`, jeśli nie jest konieczne,
- używaj listy argumentów w `subprocess.run()`,
- nie przekazuj nieufnych danych do komend bez kontroli,
- stosuj whitelistę dozwolonych opcji,
- jeśli można, zastąp wywołanie systemowe zwykłym Pythonem.

## Mini porównanie

### Zły SQL

```python
query = f"SELECT * FROM users WHERE email = '{email}'"
```

### Lepszy SQL

```python
cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
```

### Zła komenda

```python
subprocess.run(f"cat {filename}", shell=True)
```

### Lepsza komenda

```python
subprocess.run(["cat", filename], check=True)
```

## Ważna uwaga

Sama walidacja nie zastępuje parametryzacji ani bezpiecznego API.

Przykład:

- nawet jeśli sprawdzisz, że `email` wygląda poprawnie,
- i tak używaj parametrów SQL.

Podobnie:

- nawet jeśli `filename` wygląda rozsądnie,
- i tak nie buduj komendy przez `shell=True` bez potrzeby.

## Typowe błędy początkujących

- SQL przez f-string,
- ręczne escapowanie zamiast parametryzacji,
- `subprocess` ze stringiem budowanym z inputu,
- myślenie, że „użytkownik przecież poda normalną wartość”,
- brak świadomości, że narzędzia wewnętrzne też mogą być nadużyte.

## Checklista anti-injection

- Czy dane użytkownika trafiają do SQL?
- Czy używam parametrów zamiast sklejania?
- Czy dane trafiają do komendy systemowej?
- Czy mogę uniknąć `shell=True`?
- Czy mogę zastąpić wywołanie systemowe zwykłym Pythonem?
- Czy waliduję i ograniczam dopuszczalne wartości?

## Szybka ściąga

Injection pojawia się wtedy, gdy dane zaczynają sterować instrukcją.

Najważniejsze obrony:

- SQL: parametryzacja,
- system: lista argumentów i brak `shell=True` tam, gdzie nie trzeba,
- zawsze: nieufność wobec inputu.

## Ćwiczenia

1. Napisz przykład podatnego zapytania SQL, a potem popraw go przez parametryzację.
2. Napisz przykład ryzykownego użycia `subprocess`, a potem popraw go.
3. Własnymi słowami wyjaśnij wspólny mechanizm SQL injection i command injection.
4. Podaj przykład walidacji, która pomaga, ale nie zastępuje parametryzacji.
5. Znajdź w projekcie miejsce, gdzie dynamiczne składanie instrukcji byłoby ryzykowne.

## Najważniejsze do zapamiętania

- Injection to sytuacja, w której dane użytkownika stają się częścią wykonywanej instrukcji.
- SQL injection i command injection mają wspólny mechanizm, choć atakują inne warstwy systemu.
- Najlepszą obroną przed SQL injection jest parametryzacja.
- Najlepszą obroną przed command injection jest unikanie `shell=True` i używanie listy argumentów.
- Walidacja pomaga, ale nie zastępuje bezpiecznych interfejsów wykonania.
