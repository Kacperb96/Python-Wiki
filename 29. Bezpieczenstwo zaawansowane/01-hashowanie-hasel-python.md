# Hashowanie hasel python

Hasła użytkowników nie powinny być przechowywane w bazie w postaci jawnej.

To jest jedna z najbardziej podstawowych i jednocześnie najważniejszych zasad bezpieczeństwa.

## 1. Czego absolutnie nie robić

Zły pomysł:

```python
password = "tajnehaslo123"
db.save({"password": password})
```

Jeśli baza wycieknie, atakujący od razu widzi prawdziwe hasła.

Jeszcze zły, ale nadal zły pomysł:

```python
import hashlib

hashed = hashlib.sha256(password.encode()).hexdigest()
```

To wygląda lepiej niż plain text, ale do przechowywania haseł użytkowników nadal nie jest dobrym rozwiązaniem samodzielnie.

## 2. Dlaczego zwykły hash to za mało

Hasła użytkowników są specyficzne:

- bywają krótkie,
- bywają słabe,
- bywają powtarzane między serwisami,
- da się je zgadywać słownikowo.

Dlatego mechanizm do haseł powinien:

- być wolniejszy niż zwykły hash,
- używać `salt`,
- być zaprojektowany specjalnie do przechowywania haseł.

## 3. Co to jest `salt`

`Salt` to losowa wartość dodawana do hasła przed wyliczeniem wyniku.

Po co?

- żeby dwa takie same hasła nie dawały identycznego wyniku,
- żeby utrudnić ataki oparte o gotowe tabele,
- żeby każdy rekord był traktowany indywidualnie.

Przykład intuicyjny:

Bez `salt`:

```text
"haslo123" -> ten sam wynik dla każdego użytkownika
```

Z `salt`:

```text
user A: "haslo123" + losowe_salt_A -> wynik A
user B: "haslo123" + losowe_salt_B -> wynik B
```

## 4. Czego używać w praktyce

W praktycznych aplikacjach używa się mechanizmów zaprojektowanych do haseł, na przykład:

- `bcrypt`,
- `argon2`,
- `scrypt`.

Najważniejsza myśl:

`hasła haszujemy mechanizmem do haseł, nie zwykłym hashem ogólnego przeznaczenia`

## 5. Schemat poprawnego myślenia

Przy rejestracji:

1. użytkownik podaje hasło
2. aplikacja haszuje je odpowiednim algorytmem
3. do bazy trafia tylko wynik haszowania i dane potrzebne do weryfikacji

Przy logowaniu:

1. użytkownik wpisuje hasło
2. aplikacja nie odszyfrowuje niczego
3. aplikacja porównuje wpisane hasło z zapisanym hashem przez funkcję weryfikującą

To ważne:

`haseł zwykle się nie odszyfrowuje`

## 6. Antywzorce

### Antywzorzec 1

Przechowywanie haseł jawnie.

### Antywzorzec 2

Szybki hash bez mechanizmu dedykowanego hasłom.

### Antywzorzec 3

Własny "sprytny" system typu:

```python
stored = password[::-1] + "_moja_sztuczka"
```

To nie jest bezpieczeństwo.

### Antywzorzec 4

Logowanie hasła podczas debugowania:

```python
print("password:", password)
```

To może skończyć się wyciekiem do logów.

## 7. Minimalny przykład ideowy

Pseudokod:

```python
def register_user(password):
    hashed_password = hash_password(password)
    save_user(hashed_password)


def login_user(password, stored_hash):
    return verify_password(password, stored_hash)
```

Nie chodzi tu o konkretną bibliotekę, tylko o poprawny przepływ.

## 8. Co użytkownik zobaczy, a czego nie

Przy dobrym systemie:

- użytkownik nie widzi żadnych szczegółów hashowania,
- baza nie zna jawnego hasła,
- aplikacja nie przechowuje hasła do późniejszego "odczytu".

## 9. Dodatkowe dobre praktyki

- wymagaj sensownej długości hasła,
- nie loguj hasła,
- ograniczaj liczbę prób logowania,
- rozważ MFA dla ważnych systemów,
- po incydencie resetuj lub unieważniaj zagrożone dane uwierzytelniające.

## 10. Najczęstszy błąd początkujących

Bardzo częsty błąd:

`skoro coś daje skrót, to znaczy, że nadaje się do haseł`

Nie. To za mało.

## Zadania

1. Wyjaśnij różnicę między przechowywaniem hasła jawnie a przechowywaniem hasha.
2. Opisz, po co jest `salt`.
3. Wyjaśnij, czemu zwykły szybki hash nie jest najlepszym wyborem dla haseł użytkowników.
4. Podaj trzy antywzorce związane z obsługą haseł.
