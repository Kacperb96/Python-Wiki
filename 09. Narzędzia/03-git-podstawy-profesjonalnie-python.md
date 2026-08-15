# Git w praktyce dla programisty Pythona

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest Git](#czym-jest-git)
3. [Po co Python developerowi Git](#po-co-python-developerowi-git)
4. [Najważniejsze pojęcia](#najważniejsze-pojęcia)
5. [Trzy obszary pracy w Git](#trzy-obszary-pracy-w-git)
6. [Pierwsza konfiguracja](#pierwsza-konfiguracja)
7. [`git init`](#git-init)
8. [`git status`](#git-status)
9. [`git add`](#git-add)
10. [`git commit`](#git-commit)
11. [`git log`](#git-log)
12. [`git diff`](#git-diff)
13. [Usuwanie i zmiana nazw plików](#usuwanie-i-zmiana-nazw-plików)
14. [Branch](#branch)
15. [`git switch` i `git checkout`](#git-switch-i-git-checkout)
16. [Merge](#merge)
17. [Konflikty merge](#konflikty-merge)
18. [`git restore`](#git-restore)
19. [`git reset` na poziomie podstaw](#git-reset-na-poziomie-podstaw)
20. [`.gitignore`](#gitignore)
21. [Repozytorium lokalne i zdalne](#repozytorium-lokalne-i-zdalne)
22. [`git remote`](#git-remote)
23. [`git push`, `git pull`, `git fetch`](#git-push-git-pull-git-fetch)
24. [Dobry workflow pracy](#dobry-workflow-pracy)
25. [Jak pisać dobre commity](#jak-pisać-dobre-commity)
26. [Typowe błędy początkujących](#typowe-błędy-początkujących)
27. [Praktyczna ściąga](#praktyczna-ściąga)
28. [Ćwiczenia](#ćwiczenia)
29. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

Git to jedno z absolutnie najważniejszych narzędzi programisty.

Jeśli piszesz kod w Pythonie, to Git daje Ci:

- historię zmian,
- możliwość cofnięcia błędów,
- bezpieczne eksperymentowanie,
- łatwiejszą pracę na kilku wersjach projektu,
- współpracę z innymi.

Nawet jeśli uczysz się sam i pracujesz solo, Git nadal jest ogromnie przydatny.

---

## Czym jest Git

Git to system kontroli wersji.

Najprościej:

Git zapamiętuje kolejne stany Twojego projektu i pozwala do nich wracać.

Możesz więc:

- zobaczyć, co zmieniłeś,
- odtworzyć starszą wersję pliku,
- pracować nad nową funkcją bez psucia głównej wersji projektu.

---

## Po co Python developerowi Git

W praktyce Git przydaje się codziennie.

Przykłady:

- tworzysz nowy moduł i chcesz zapisać bezpieczny punkt powrotu,
- refaktorujesz funkcję i chcesz porównać starą oraz nową wersję,
- eksperymentujesz z dekoratorami, klasami albo testami,
- pracujesz nad projektem z GitHubem.

Git nie poprawia kodu sam z siebie, ale daje Ci bezpieczeństwo pracy.

---

## Najważniejsze pojęcia

### Repozytorium

Projekt śledzony przez Gita.

### Commit

Zapis konkretnego stanu zmian.

### Branch

Osobna gałąź pracy, np. pod nową funkcję.

### Stage

Miejsce pośrednie pomiędzy zmianami w plikach a commitem.

### Remote

Zdalne repozytorium, np. na GitHubie.

---

## Trzy obszary pracy w Git

To bardzo ważne, bo wiele nieporozumień bierze się właśnie stąd.

Git operuje na trzech poziomach:

1. `working tree` — aktualne pliki w katalogu,
2. `staging area` — zmiany przygotowane do commita,
3. `repository` — historia commitów.

Przepływ wygląda zwykle tak:

```text
plik zmieniony -> git add -> staging area -> git commit -> historia repozytorium
```

---

## Pierwsza konfiguracja

Najczęściej wykonujesz to raz:

```bash
git config --global user.name "Jan Kowalski"
git config --global user.email "jan@example.com"
```

Możesz sprawdzić ustawienia:

```bash
git config --global --list
```

Przykładowy output:

```text
user.name=Jan Kowalski
user.email=jan@example.com
init.defaultbranch=main
```

---

## `git init`

Tworzy repozytorium Git w bieżącym katalogu.

```bash
git init
```

Przykładowy output:

```text
Initialized empty Git repository in /home/user/projekt/.git/
```

Od tego momentu katalog jest repozytorium.

---

## `git status`

To jedna z najważniejszych komend.

```bash
git status
```

Pokazuje:

- na jakiej jesteś gałęzi,
- które pliki się zmieniły,
- które są staged,
- które nie są śledzone.

Przykładowy output:

```text
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        app.py

nothing added to commit but untracked files present
```

Interpretacja:

- jesteś na branchu `main`,
- plik `app.py` istnieje, ale Git jeszcze go nie śledzi,
- trzeba użyć `git add`.

---

## `git add`

Dodaje zmiany do staging area.

```bash
git add app.py
```

Albo wszystkie zmiany:

```bash
git add .
```

Po `git add` warto od razu sprawdzić status.

Przykładowy output po `git status`:

```text
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   app.py
```

To znaczy, że plik jest już przygotowany do commita.

---

## `git commit`

Commit zapisuje staged zmiany do historii.

```bash
git commit -m "Dodaj pierwszy skrypt aplikacji"
```

Przykładowy output:

```text
[main (root-commit) a1b2c3d] Dodaj pierwszy skrypt aplikacji
 1 file changed, 5 insertions(+)
 create mode 100644 app.py
```

Co tu widzisz:

- branch: `main`,
- skrót commita: `a1b2c3d`,
- opis commita,
- liczbę zmian.

---

## `git log`

Pokazuje historię commitów.

```bash
git log
```

Przykładowy output:

```text
commit a1b2c3d4e5f6g7h8i9
Author: Jan Kowalski <jan@example.com>
Date:   Thu Aug 15 12:00:00 2026 +0000

    Dodaj pierwszy skrypt aplikacji
```

Bardziej praktyczny skrót:

```bash
git log --oneline
```

Przykładowy output:

```text
a1b2c3d Dodaj pierwszy skrypt aplikacji
9f8e7d6 Dodaj README projektu
```

---

## `git diff`

Pokazuje różnice między wersjami plików.

### Zmiany jeszcze nie dodane do stage

```bash
git diff
```

### Zmiany dodane do stage

```bash
git diff --cached
```

Przykładowy output:

```text
-print("Hello")
+print("Hello, world")
```

Interpretacja:

- linia z `-` została usunięta,
- linia z `+` została dodana.

To świetna komenda do kontroli przed commitem.

---

## Usuwanie i zmiana nazw plików

### Usunięcie pliku

```bash
git rm dane.txt
```

### Zmiana nazwy pliku

```bash
git mv stare.py nowe.py
```

Po takich operacjach Git również śledzi zmiany i możesz je commitować.

---

## Branch

Branch to osobna gałąź pracy.

Przykład zastosowania:

- na `main` masz stabilną wersję,
- tworzysz branch `dodaj-logowanie`,
- rozwijasz nową funkcję bez mieszania jej z głównym kodem.

Lista branchy:

```bash
git branch
```

Przykładowy output:

```text
* main
  dodaj-logowanie
```

Gwiazdka pokazuje aktywną gałąź.

---

## `git switch` i `git checkout`

Nowocześniejszy zapis tworzenia i przełączania branchy:

```bash
git switch -c dodaj-logowanie
```

Przykładowy output:

```text
Switched to a new branch 'dodaj-logowanie'
```

Przełączenie na istniejący branch:

```bash
git switch main
```

Starsza forma:

```bash
git checkout -b dodaj-logowanie
```

Dzisiaj warto znać obie, ale częściej używa się `switch`.

---

## Merge

Merge łączy historię jednej gałęzi z drugą.

Przykład:

1. pracujesz na branchu `dodaj-logowanie`,
2. kończysz pracę,
3. wracasz na `main`,
4. łączysz branch z `main`.

```bash
git switch main
git merge dodaj-logowanie
```

Przykładowy output:

```text
Updating a1b2c3d..d4e5f6g
Fast-forward
 app.py | 8 ++++++++
 1 file changed, 8 insertions(+)
```

`Fast-forward` oznacza prosty merge bez konfliktu historii.

---

## Konflikty merge

Konflikt pojawia się wtedy, gdy Git nie wie automatycznie, którą wersję zmian zostawić.

Przykład w pliku:

```text
<<<<<<< HEAD
print("wersja z main")
=======
print("wersja z brancha")
>>>>>>> dodaj-logowanie
```

To znaczy, że musisz ręcznie wybrać poprawną wersję.

Po poprawce:

1. zapisujesz plik,
2. robisz `git add plik.py`,
3. kończysz merge commitem.

---

## `git restore`

Ta komenda pomaga przywracać pliki.

### Cofnięcie lokalnych zmian w pliku

```bash
git restore app.py
```

To przywróci plik do stanu z ostatniego commita.

Uwaga:

jeśli miałeś tam ważne, niezapisane zmiany, zostaną utracone.

### Usunięcie pliku ze stage

```bash
git restore --staged app.py
```

To nie usuwa zmian z pliku, tylko wycofuje `git add`.

---

## `git reset` na poziomie podstaw

Na start wystarczy znać jedną bezpieczniejszą wersję:

```bash
git reset HEAD app.py
```

Efekt:

- plik wypada ze stage,
- jego zmiany nadal pozostają w katalogu roboczym.

To podobne do `git restore --staged`.

Zaawansowane użycia `git reset` potrafią być destrukcyjne, więc początkujący powinien używać tej komendy ostrożnie.

---

## `.gitignore`

Plik `.gitignore` mówi Gitowi, czego nie śledzić.

W projektach Pythona typowe wpisy to:

```gitignore
.venv/
__pycache__/
*.pyc
.env
.idea/
.vscode/
.pytest_cache/
```

Dlaczego to ważne:

- nie wrzucasz śmieci do repo,
- nie commitujesz środowiska wirtualnego,
- nie wrzucasz sekretów z `.env`.

---

## Repozytorium lokalne i zdalne

### Lokalnie

Masz pliki i historię na swoim komputerze.

### Zdalnie

Masz kopię repo na GitHubie albo innym serwerze.

To pozwala:

- robić backup,
- współpracować,
- publikować projekt.

---

## `git remote`

Pokazuje lub ustawia zdalne repozytoria.

```bash
git remote -v
```

Przykładowy output:

```text
origin  git@github.com:Kacperb96/Python-Wiki.git (fetch)
origin  git@github.com:Kacperb96/Python-Wiki.git (push)
```

Najczęściej główne zdalne repo ma nazwę `origin`.

---

## `git push`, `git pull`, `git fetch`

### `git push`

Wysyła lokalne commity do zdalnego repo:

```bash
git push origin main
```

### `git pull`

Pobiera zmiany i od razu próbuje je scalić:

```bash
git pull origin main
```

### `git fetch`

Pobiera informacje ze zdalnego repo, ale jeszcze niczego nie scala:

```bash
git fetch origin
```

To bezpieczna komenda do sprawdzenia, czy zdalnie coś się zmieniło.

---

## Dobry workflow pracy

Bardzo praktyczny prosty schemat:

1. `git status`
2. edycja plików
3. `git diff`
4. `git add ...`
5. `git diff --cached`
6. `git commit -m "..."`
7. `git push`

Taki rytm daje porządek i kontrolę.

---

## Jak pisać dobre commity

Dobry commit powinien być:

- mały,
- logiczny,
- czytelnie opisany.

Dobre przykłady:

- `Dodaj walidację adresu e-mail`
- `Popraw błąd dzielenia przez zero`
- `Rozbij moduł utils na mniejsze funkcje`

Słabe przykłady:

- `fix`
- `zmiany`
- `update`

Opis ma odpowiadać na pytanie: co dokładnie zmieniłem?

---

## Typowe błędy początkujących

- robienie commitów bez sprawdzenia `git diff`,
- commitowanie zbyt wielu niepowiązanych zmian naraz,
- wrzucanie `.venv/` do repo,
- praca cały czas tylko na `main`,
- używanie destrukcyjnych komend bez rozumienia skutków,
- ignorowanie `git status`.

---

## Praktyczna ściąga

```bash
git init
git status
git add .
git commit -m "Opis zmian"
git log --oneline
git diff
git switch -c nowa-galaz
git switch main
git merge nowa-galaz
git remote -v
git push origin main
```

---

## Ćwiczenia

1. Utwórz nowy katalog i zainicjalizuj w nim repozytorium Git.
2. Dodaj plik `app.py`, sprawdź `git status`, a potem zrób pierwszy commit.
3. Zmień zawartość `app.py` i zobacz różnicę przez `git diff`.
4. Dodaj zmianę do stage i sprawdź `git diff --cached`.
5. Utwórz branch `nowa-funkcja` i przełącz się na niego.
6. Dodaj nowy plik na branchu i zrób commit.
7. Wróć na `main` i wykonaj merge.
8. Dodaj `.gitignore` z wpisem `.venv/` i `__pycache__/`.
9. Skonfiguruj zdalne repo `origin` i sprawdź `git remote -v`.
10. Wypisz własnymi słowami różnicę między `pull`, `fetch` i `push`.

---

## Najważniejsze do zapamiętania

- `git status` to komenda, do której wracasz najczęściej.
- `git add` nie robi commita, tylko przygotowuje zmiany do commita.
- `git diff` pokazuje dokładnie, co zmieniłeś.
- Branch pozwala pracować bez ryzyka rozwalenia głównej wersji projektu.
- `.gitignore` jest obowiązkowy w projektach Pythona.
- Zanim użyjesz mocniejszych komend typu `reset`, najpierw upewnij się, że rozumiesz ich skutek.
