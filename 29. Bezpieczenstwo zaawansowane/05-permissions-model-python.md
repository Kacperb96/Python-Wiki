# Permissions model python

Jednym z najczęstszych i najbardziej kosztownych błędów aplikacyjnych jest zła kontrola dostępu.

Nie wystarczy sprawdzić:

`czy użytkownik jest zalogowany`

Trzeba jeszcze sprawdzić:

- czy wolno mu wykonać tę akcję,
- czy wolno mu zobaczyć ten zasób,
- czy działa we właściwym kontekście roli i własności.

## 1. Uwierzytelnianie a autoryzacja

### Uwierzytelnianie

Pytanie:

`kim jesteś?`

### Autoryzacja

Pytanie:

`czy wolno ci to zrobić?`

To są różne rzeczy.

## 2. Własność zasobu

Bardzo częsty błąd:

```python
if current_user:
    return invoice
```

To sprawdza tylko, czy ktoś jest zalogowany.

Brakuje jeszcze pytania:

`czy ta faktura należy do tego użytkownika?`

## 3. Przykład myślowy

Masz endpoint:

```text
GET /invoices/123
```

Jeśli aplikacja tylko sprawdzi, czy użytkownik ma aktywną sesję, a nie sprawdzi właściciela faktury, może oddać cudze dane.

## 4. Role i uprawnienia

Typowe role:

- user
- moderator
- admin

Ale sama rola to nie wszystko.

Czasem potrzebujesz sprawdzić też:

- czy obiekt należy do użytkownika,
- czy użytkownik działa w danej organizacji,
- czy ma konkretny zakres uprawnień,
- czy akcja jest dozwolona w tym stanie obiektu.

## 5. Zasada najmniejszych uprawnień

Zdrowa zasada brzmi:

`dawaj tylko tyle uprawnień, ile naprawdę potrzeba`

Skutki zbyt szerokich uprawnień:

- większy zasięg błędu,
- większe szkody po przejęciu konta,
- większe ryzyko nadużycia,
- trudniejszy audyt.

## 6. Częste antywzorce

### Antywzorzec 1

Ukrycie przycisku w UI i uznanie tego za zabezpieczenie.

Nie. Backend nadal musi sprawdzić uprawnienia.

### Antywzorzec 2

Sprawdzanie roli tylko w jednym miejscu, a w innych endpointach już nie.

### Antywzorzec 3

Rola `admin`, która daje wszystko wszędzie bez rozróżnienia kontekstu.

## 7. Pseudo-scenariusz

Wejście:

```text
user_id = 14
requested_invoice_id = 782
```

Niebezpieczne podejście:

```text
użytkownik jest zalogowany -> oddaj fakturę
```

Bezpieczniejsze podejście:

```text
użytkownik jest zalogowany
sprawdź, czy ma prawo czytać fakturę
sprawdź, czy faktura należy do niego albo do jego organizacji
```

## Zadania

1. Wyjaśnij różnicę między uwierzytelnianiem a autoryzacją.
2. Opisz, dlaczego własność zasobu jest tak ważna.
3. Podaj trzy przykłady zbyt szerokich uprawnień.
