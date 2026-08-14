# Bezpieczeństwo w Pythonie — podstawy

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co Pythonowcowi bezpieczeństwo](#po-co-pythonowcowi-bezpieczeństwo)
3. [Najczęstsze obszary ryzyka](#najczęstsze-obszary-ryzyka)
4. [Dane wejściowe są nieufne](#dane-wejściowe-są-nieufne)
5. [Sekrety i konfiguracja](#sekrety-i-konfiguracja)
6. [Dostęp do plików i systemu](#dostęp-do-plików-i-systemu)
7. [Bazy danych i zapytania](#bazy-danych-i-zapytania)
8. [Autoryzacja i uprawnienia](#autoryzacja-i-uprawnienia)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczne przykłady](#praktyczne-przykłady)
11. [Dobre praktyki](#dobre-praktyki)
12. [Podsumowanie](#podsumowanie)
13. [Mini ściąga](#mini-ściąga)
14. [Ćwiczenia](#ćwiczenia)
15. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Bezpieczeństwo nie jest dodatkiem "na później".

W praktyce to część jakości oprogramowania od samego początku projektu.

---

## Po co Pythonowcowi bezpieczeństwo

Bo nawet mały błąd może prowadzić do:

- wycieku danych,
- nieautoryzowanego dostępu,
- uszkodzenia systemu,
- kosztownych incydentów.

---

## Najczęstsze obszary ryzyka

Najczęściej:

- dane wejściowe,
- sekrety,
- zapytania do bazy,
- wywołania systemowe,
- dostęp do plików,
- autoryzacja.

---

## Dane wejściowe są nieufne

Jedna z najważniejszych zasad:

nie ufaj danym z zewnątrz.

Dotyczy to:

- formularzy,
- JSON z API,
- parametrów URL,
- plików uploadowanych przez użytkownika.

---

## Sekrety i konfiguracja

Hasła, tokeny i klucze API nie powinny być wpisywane na sztywno w kodzie.

To bardzo częsty i bardzo kosztowny błąd.

---

## Dostęp do plików i systemu

Każde operacje na ścieżkach i komendach systemowych trzeba projektować ostrożnie.

Tu pojawiają się ryzyka takie jak:

- path traversal,
- command injection.

---

## Bazy danych i zapytania

Ręczne sklejanie SQL z danymi użytkownika to proszenie się o problemy.

Parametryzacja to standard bezpieczeństwa.

---

## Autoryzacja i uprawnienia

Nie wystarczy wiedzieć, kim jest użytkownik.

Trzeba jeszcze wiedzieć, czy wolno mu wykonać daną operację.

---

## Typowe błędy początkujących

- hardkodowanie sekretów,
- brak walidacji inputu,
- sklejanie SQL,
- używanie `shell=True` bez potrzeby,
- zbyt szeroki dostęp do zasobów.

---

## Praktyczne przykłady

### Zła praktyka

- token API wpisany w repo,
- SQL składany przez f-string,
- ścieżka pliku budowana bez walidacji.

### Dobra praktyka

- env vars,
- walidacja,
- parametryzacja,
- kontrola dostępu.

---

## Dobre praktyki

- traktuj input jako nieufny,
- trzymaj sekrety poza kodem,
- ograniczaj uprawnienia,
- używaj bezpiecznych interfejsów do bazy i systemu,
- testuj przypadki błędne i nieuprawnione.

---

## Podsumowanie

Podstawy bezpieczeństwa to obowiązkowa kompetencja profesjonalnego Pythonowca.

Bardzo wiele problemów da się ograniczyć prostymi, dobrymi nawykami.

---

## Mini ściąga

Najważniejsze:

- nie ufaj inputowi,
- nie trzymaj sekretów w kodzie,
- nie sklejaj SQL,
- ostrożnie uruchamiaj komendy systemowe,
- pilnuj autoryzacji.

---

## Ćwiczenia

1. Wymień 4 obszary ryzyka bezpieczeństwa w Pythonie.
2. Wyjaśnij, czemu input jest nieufny.
3. Wyjaśnij, czemu nie wolno trzymać sekretów w repo.
4. Wskaż ryzyko sklejania SQL.
5. Wyjaśnij, czemu autoryzacja to osobny temat od autentykacji.

---

## Przykładowe rozwiązania

### 1. Obszary

- input,
- sekrety,
- baza danych,
- komendy systemowe.

### 2. Czemu nieufny

Bo może być błędny, złośliwy lub niezgodny z oczekiwaniami aplikacji.

### 3. Sekrety w repo

Bo mogą wyciec i dać niepowołanym osobom dostęp do systemu.

### 4. SQL

Może prowadzić do SQL injection.

### 5. Autoryzacja vs autentykacja

Bo jedno ustala tożsamość, a drugie uprawnienia.
