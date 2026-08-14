# Sekrety i zmienne środowiskowe w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym są sekrety](#czym-są-sekrety)
3. [Po co używać env vars](#po-co-używać-env-vars)
4. [Czego nie robić](#czego-nie-robić)
5. [Odczyt env vars w Pythonie](#odczyt-env-vars-w-pythonie)
6. [Brakujące zmienne i fallbacki](#brakujące-zmienne-i-fallbacki)
7. [Sekrety a repozytorium](#sekrety-a-repozytorium)
8. [Sekrety a środowiska](#sekrety-a-środowiska)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczne przykłady](#praktyczne-przykłady)
11. [Dobre praktyki](#dobre-praktyki)
12. [Podsumowanie](#podsumowanie)
13. [Mini ściąga](#mini-ściąga)
14. [Ćwiczenia](#ćwiczenia)
15. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Sekrety takie jak hasła, tokeny czy klucze API to jedna z najbardziej wrażliwych części projektu.

Bardzo ważne jest, by od początku obchodzić się z nimi poprawnie.

---

## Czym są sekrety

Sekrety to dane, które dają dostęp do systemów lub zasobów.

Na przykład:

- hasło do bazy,
- token API,
- klucz JWT,
- sekret integracyjny.

---

## Po co używać env vars

Zmienne środowiskowe pomagają:

- trzymać sekrety poza kodem,
- zmieniać konfigurację między środowiskami,
- ograniczać ryzyko wycieku przez repozytorium.

---

## Czego nie robić

Nie wpisuj sekretów bezpośrednio do:

- kodu,
- commitów,
- publicznych plików konfiguracyjnych,
- screenshotów i przykładów bez anonimizacji.

---

## Odczyt env vars w Pythonie

```python
import os

db_password = os.getenv("DB_PASSWORD")
```

To bardzo podstawowy i ważny wzorzec.

---

## Brakujące zmienne i fallbacki

Czasem zmienna może nie istnieć.

Dlatego trzeba świadomie zdecydować:

- czy jest obowiązkowa,
- czy ma mieć wartość domyślną,
- czy program ma się zatrzymać.

---

## Sekrety a repozytorium

Repozytorium nie powinno przechowywać prawdziwych sekretów.

Można trzymać:

- przykładowy `.env.example`,
- dokumentację wymaganych zmiennych,

ale nie prawdziwe wartości.

---

## Sekrety a środowiska

Development, staging i production mogą mieć różne wartości sekretów.

To kolejny powód, dla którego nie warto ich hardkodować.

---

## Typowe błędy początkujących

- token wpisany w kod,
- wrzucenie `.env` do repo,
- brak sprawdzenia, czy krytyczna zmienna istnieje,
- logowanie sekretów do konsoli lub plików.

---

## Praktyczne przykłady

### Odczyt tokenu

```python
import os

token = os.getenv("API_TOKEN")
```

### Zła praktyka

```python
API_TOKEN = "super-tajny-token"
```

---

## Dobre praktyki

- trzymaj sekrety poza kodem,
- dokumentuj wymagane env vars,
- nie loguj sekretów,
- jasno oddzielaj konfigurację od logiki.

---

## Podsumowanie

Sekrety i env vars to podstawowy temat bezpieczeństwa i konfiguracji aplikacji.

Dobry nawyk tu oszczędza bardzo wielu poważnych problemów w przyszłości.

---

## Mini ściąga

```python
import os

token = os.getenv("API_TOKEN")
```

Najważniejsze:

- sekrety nie powinny być w kodzie,
- env vars to częsty sposób ich dostarczania,
- `.env.example` może być OK, prawdziwe `.env` zwykle nie powinno trafić do repo.

---

## Ćwiczenia

1. Wyjaśnij, czym jest sekret.
2. Odczytaj zmienną `API_TOKEN`.
3. Wskaż przykład złej praktyki z sekretami.
4. Wyjaśnij, po co używać `.env.example`.
5. Wyjaśnij, czemu nie wolno logować sekretów.

---

## Przykładowe rozwiązania

### 1. Sekret

To wrażliwa wartość dająca dostęp do systemu lub zasobu.

### 2. Odczyt

```python
import os

print(os.getenv("API_TOKEN"))
```

### 3. Zła praktyka

Hardkodowanie hasła do bazy w pliku `.py`.

### 4. `.env.example`

Pomaga pokazać, jakie zmienne są potrzebne, bez ujawniania prawdziwych wartości.

### 5. Czemu nie logować

Bo logi też mogą wyciec albo być dostępne dla osób, które nie powinny znać tych danych.
