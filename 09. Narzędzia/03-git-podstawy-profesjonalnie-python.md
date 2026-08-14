# Git — obowiązkowe narzędzie programisty

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest Git](#czym-jest-git)
3. [Po co używa się Gita](#po-co-używa-się-gita)
4. [Repozytorium](#repozytorium)
5. [Commit](#commit)
6. [Branch](#branch)
7. [Podstawowy workflow](#podstawowy-workflow)
8. [`git init`](#git-init)
9. [`git status`](#git-status)
10. [`git add`](#git-add)
11. [`git commit`](#git-commit)
12. [`git log`](#git-log)
13. [`git diff`](#git-diff)
14. [Branchowanie](#branchowanie)
15. [Merge](#merge)
16. [Rebase — krótki wstęp](#rebase--krótki-wstęp)
17. [`gitignore`](#gitignore)
18. [Repozytorium lokalne i zdalne](#repozytorium-lokalne-i-zdalne)
19. [`git push`, `git pull`, `git fetch`](#git-push-git-pull-git-fetch)
20. [Jak pisać dobre commity](#jak-pisać-dobre-commity)
21. [Typowe błędy początkujących](#typowe-błędy-początkujących)
22. [Praktyczne przykłady](#praktyczne-przykłady)
23. [Dobre praktyki](#dobre-praktyki)
24. [Podsumowanie](#podsumowanie)
25. [Mini ściąga](#mini-ściąga)
26. [Ćwiczenia](#ćwiczenia)
27. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Git to obowiązkowe narzędzie każdego programisty.

Nawet jeśli pracujesz sam, Git daje Ci ogromne korzyści:

- historię zmian,
- możliwość cofnięcia się,
- bezpieczne eksperymentowanie,
- lepszą organizację pracy.

W pracy zespołowej Git jest absolutnie podstawowy.

---

## Czym jest Git

Git to system kontroli wersji.

Najprościej:

pozwala śledzić zmiany w plikach i zarządzać historią projektu.

---

## Po co używa się Gita

Żeby:

- zapisywać kolejne wersje projektu,
- wiedzieć, co się zmieniło,
- wracać do wcześniejszych wersji,
- pracować w gałęziach,
- współpracować z innymi.

---

## Repozytorium

Repozytorium to projekt śledzony przez Gita.

To miejsce, w którym Git przechowuje historię zmian.

---

## Commit

Commit to zapis konkretnego stanu zmian.

Najprościej:

to punkt w historii projektu.

Dobry commit powinien mieć sensowny opis i logiczny zakres.

---

## Branch

Branch to gałąź pracy.

Pozwala rozwijać nową funkcję albo poprawkę niezależnie od głównej linii rozwoju.

---

## Podstawowy workflow

Typowy prosty cykl:

1. zmieniasz pliki,
2. sprawdzasz status,
3. dodajesz pliki do stage,
4. robisz commit.

---

## `git init`

Tworzy nowe repozytorium:

```bash
git init
```

---

## `git status`

Jedna z najważniejszych komend:

```bash
git status
```

Pokazuje:

- co się zmieniło,
- co jest staged,
- co nie jest staged.

---

## `git add`

Dodaje zmiany do stage:

```bash
git add plik.py
```

albo:

```bash
git add .
```

---

## `git commit`

Tworzy commit:

```bash
git commit -m "Dodaj funkcje logowania"
```

---

## `git log`

Pokazuje historię commitów:

```bash
git log
```

---

## `git diff`

Pokazuje różnice:

```bash
git diff
```

To bardzo ważne przed commitem.

---

## Branchowanie

Tworzenie nowej gałęzi:

```bash
git branch nowa-funkcja
git checkout nowa-funkcja
```

albo krócej:

```bash
git checkout -b nowa-funkcja
```

W nowszym stylu często:

```bash
git switch -c nowa-funkcja
```

---

## Merge

Łączy gałąź z inną gałęzią.

Na przykład łączenie feature branch do main.

---

## Rebase — krótki wstęp

`rebase` to bardziej zaawansowany sposób przenoszenia zmian na inną bazę historii.

Na początku najważniejsze jest zrozumienie brancha i merge.

Do `rebase` warto wrócić, gdy podstawy są już pewne.

---

## `gitignore`

Plik `.gitignore` mówi Gitowi, czego nie śledzić.

Bardzo ważne przykłady:

- `.venv/`
- `__pycache__/`
- pliki tymczasowe,
- wygenerowane pliki buildów.

---

## Repozytorium lokalne i zdalne

### Lokalne

To Twoja kopia na komputerze.

### Zdalne

To repozytorium np. na GitHubie, GitLabie albo innym serwerze.

---

## `git push`, `git pull`, `git fetch`

### `git push`

Wysyła zmiany do zdalnego repo.

### `git pull`

Pobiera i integruje zmiany.

### `git fetch`

Pobiera informacje o zmianach bez ich automatycznego scalania.

---

## Jak pisać dobre commity

Dobry commit:

- dotyczy jednej logicznej zmiany,
- ma czytelny opis,
- nie miesza przypadkowych rzeczy.

Przykłady:

- `Dodaj walidacje emaila`
- `Napraw blad logowania`
- `Refaktoryzuj klienta API`

---

## Typowe błędy początkujących

- brak częstych commitów,
- ogromne commity z wieloma rzeczami naraz,
- commitowanie `.venv`,
- brak `git status` i `git diff` przed commitem,
- strach przed branchami.

---

## Praktyczne przykłady

```bash
git init
git status
git add .
git commit -m "Pierwsza wersja projektu"
```

```bash
git checkout -b nowa-funkcja
```

```bash
git log
git diff
```

---

## Dobre praktyki

- commituj małe logiczne zmiany,
- często sprawdzaj `git status`,
- używaj branchy do nowych funkcji,
- dbaj o `.gitignore`,
- nie commituj sekretów, środowisk i plików tymczasowych.

---

## Podsumowanie

Najważniejsze rzeczy do zapamiętania:

- Git śledzi historię zmian,
- commit zapisuje stan projektu,
- branch pozwala pracować niezależnie,
- `git status`, `git add`, `git commit`, `git diff`, `git log` to absolutne podstawy,
- Git to narzędzie obowiązkowe.

---

## Mini ściąga

```bash
git init
git status
git add .
git commit -m "Opis"
git log
git diff
git checkout -b nowa-galaz
git push
git pull
```

---

## Ćwiczenia

### Ćwiczenie 1

Zainicjuj repozytorium w katalogu testowym.

### Ćwiczenie 2

Dodaj plik i zrób pierwszy commit.

### Ćwiczenie 3

Utwórz nową gałąź.

---

## Przykładowe rozwiązania

```bash
git init
git add .
git commit -m "Start projektu"
git checkout -b eksperyment
```
