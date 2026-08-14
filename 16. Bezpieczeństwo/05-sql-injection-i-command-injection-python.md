# SQL injection i command injection w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest injection](#czym-jest-injection)
3. [SQL injection](#sql-injection)
4. [Command injection](#command-injection)
5. [Skąd biorą się te błędy](#skąd-biorą-się-te-błędy)
6. [Jak bronić się przed SQL injection](#jak-bronić-się-przed-sql-injection)
7. [Jak bronić się przed command injection](#jak-bronić-się-przed-command-injection)
8. [Typowe błędy początkujących](#typowe-błędy-początkujących)
9. [Praktyczne przykłady](#praktyczne-przykłady)
10. [Dobre praktyki](#dobre-praktyki)
11. [Podsumowanie](#podsumowanie)
12. [Mini ściąga](#mini-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Injection to jedna z najgroźniejszych i najbardziej klasycznych kategorii błędów bezpieczeństwa.

W Pythonie najczęściej praktycznie spotyka się:

- SQL injection,
- command injection.

---

## Czym jest injection

To sytuacja, gdy nieufne dane wejściowe zostają potraktowane jak część polecenia, zapytania albo instrukcji.

Wtedy użytkownik może wpłynąć na to, co naprawdę wykona system.

---

## SQL injection

SQL injection pojawia się, gdy dane użytkownika są wstrzykiwane do zapytania SQL bez bezpiecznej parametryzacji.

To może prowadzić do:

- odczytu cudzych danych,
- modyfikacji danych,
- usuwania rekordów,
- obejścia logiki aplikacji.

---

## Command injection

Command injection pojawia się, gdy dane użytkownika trafiają do komendy systemowej i są interpretowane jak część polecenia.

To może być bardzo niebezpieczne, bo dotyka już poziomu systemu operacyjnego.

---

## Skąd biorą się te błędy

Najczęściej z:

- ręcznego sklejania stringów,
- zaufania do inputu,
- braku walidacji,
- używania niebezpiecznych interfejsów bez ostrożności.

---

## Jak bronić się przed SQL injection

Najważniejsze:

- używaj parametryzowanych zapytań,
- nie sklejaj SQL z inputem użytkownika,
- korzystaj z bezpiecznych warstw bibliotecznych.

---

## Jak bronić się przed command injection

Najważniejsze:

- nie buduj komend z inputu użytkownika,
- przekazuj argumenty jako listę,
- unikaj `shell=True`, jeśli nie jest konieczne,
- waliduj i ograniczaj dane wejściowe.

---

## Typowe błędy początkujących

- SQL przez f-string,
- `subprocess` ze stringiem budowanym z inputu,
- brak walidacji i sanitizacji,
- błędne przekonanie, że "to tylko wewnętrzne narzędzie".

---

## Praktyczne przykłady

### Ryzykowny SQL

```python
query = f"SELECT * FROM users WHERE name = '{name}'"
```

### Bezpieczniej

```python
cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
```

### Ryzykowna komenda

```python
subprocess.run(f"echo {user_input}", shell=True)
```

### Bezpieczniej

```python
subprocess.run(["echo", user_input])
```

---

## Dobre praktyki

- nigdy nie sklejaj SQL z inputem,
- ostrożnie traktuj każdą komendę systemową,
- zakładaj, że input może być złośliwy,
- testuj scenariusze błędne i nietypowe.

---

## Podsumowanie

SQL injection i command injection to bardzo realne zagrożenia.

Dobra wiadomość jest taka, że podstawowe mechanizmy obrony są proste, jeśli używa się ich konsekwentnie.

---

## Mini ściąga

Najważniejsze:

- SQL: używaj parametrów,
- system: używaj listy argumentów,
- nie ufaj inputowi,
- unikaj sklejania poleceń i zapytań ręcznie.

---

## Ćwiczenia

1. Wyjaśnij, czym jest injection.
2. Podaj przykład SQL injection.
3. Podaj przykład command injection.
4. Wyjaśnij, jak bronić się przed SQL injection.
5. Wyjaśnij, czemu `shell=True` bywa ryzykowne.

---

## Przykładowe rozwiązania

### 1. Injection

To sytuacja, gdy dane użytkownika stają się częścią wykonywanego polecenia lub zapytania.

### 2. SQL injection

Na przykład sklejanie SQL z inputem przez f-string.

### 3. Command injection

Na przykład budowanie komendy systemowej ze stringa zawierającego input użytkownika.

### 4. Obrona przed SQL injection

Parametryzacja zapytań i unikanie ręcznego sklejania SQL.

### 5. `shell=True`

Bo zwiększa ryzyko niekontrolowanej interpretacji polecenia przez shell.
