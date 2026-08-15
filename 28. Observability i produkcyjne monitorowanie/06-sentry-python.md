# Sentry python

## O czym jest ten rozdział

W pewnym momencie sam fakt, że błąd pojawił się w logach, przestaje wystarczać.

Potrzebujesz wiedzieć:

- gdzie błąd wystąpił,
- jak często się powtarza,
- od której wersji się pojawia,
- kogo dotyczy,
- jaki ma stack trace,
- czy to nowy incydent, czy znany problem wracający po raz setny.

Właśnie dlatego narzędzia typu Sentry są tak praktyczne.

## Najprostsza intuicja

Sentry to narzędzie do zbierania, grupowania i analizowania błędów z działającej aplikacji.

Najprościej:

- aplikacja rzuca wyjątek albo raportuje problem,
- Sentry zbiera zdarzenie,
- grupuje podobne incydenty,
- pokazuje kontekst i historię.

To dużo więcej niż zwykły log błędu.

## Co daje Sentry w praktyce

Sentry pomaga, gdy chcesz:

- widzieć błędy z produkcji w jednym miejscu,
- grupować powtarzające się problemy,
- otrzymywać alerty,
- analizować stack trace i kontekst,
- wiedzieć, od jakiej wersji błąd się pojawił,
- szybciej reagować na regresje po deploymencie.

To bardzo duża wartość operacyjna.

## Log błędu vs zdarzenie w Sentry

### Log błędu

Może wyglądać tak:

```text
ERROR: division by zero in billing.py:42
```

To już coś daje, ale często brakuje:

- grupowania,
- kontekstu wersji,
- informacji o skali problemu,
- łatwej widoczności trendu.

### Zdarzenie w Sentry

Może mieć:

- stack trace,
- timestamp,
- środowisko,
- release,
- tagi,
- użytkownika,
- breadcrumbs,
- liczbę wystąpień.

To zupełnie inny poziom diagnostyczny.

## Najprostszy przykład myślowy

Aplikacja rzuca wyjątek:

```python
1 / 0
```

Sentry może pokazać nie tylko sam `ZeroDivisionError`, ale też:

- że błąd pojawił się 83 razy,
- że zaczął się po releasie `v1.8.0`,
- że dotyczy endpointu rozliczeń,
- że wcześniej użytkownik przeszedł przez konkretną ścieżkę.

To właśnie robi różnicę w praktyce.

## Release w Sentry: bardzo ważna rzecz

Jeśli Sentry wie, jaka wersja aplikacji jest wdrożona, dużo łatwiej odpowiedzieć:

- czy błąd pojawił się po ostatnim deploymencie,
- czy dotyczy starej wersji,
- czy hotfix naprawdę pomógł.

To jeden z najważniejszych praktycznych aspektów integracji.

## Breadcrumbs: intuicja

Breadcrumbs to ślady prowadzące do błędu.

Najprościej:

- co działo się tuż przed wyjątkiem,
- jakie kroki użytkownik lub system wykonał wcześniej.

To bardzo cenne, bo sam wyjątek często nie mówi całej historii.

## Kontekst użytkownika i requestu

Sentry zyskuje ogromnie na wartości, gdy dostaje sensowny kontekst, np.:

- `request_id`,
- `user_id`,
- środowisko,
- release,
- typ endpointu albo operacji.

To pozwala szybciej przejść od ogólnego błędu do konkretnego incydentu.

## Before/after

### Bez Sentry

- błędy są rozsiane po logach,
- trudniej zobaczyć skalę problemu,
- trudniej grupować podobne incydenty,
- reakcja na regresję jest wolniejsza.

### Z Sentry

- błędy są zebrane i pogrupowane,
- łatwiej zobaczyć wpływ nowej wersji,
- łatwiej priorytetyzować naprawy,
- łatwiej śledzić, czy błąd wraca.

## Czego Sentry nie zastępuje

To bardzo ważne.

Sentry nie zastępuje:

- sensownych logów,
- metryk,
- tracingu,
- dobrego procesu deploymentu,
- testów.

To bardzo mocny element observability, ale nadal tylko jeden z filarów.

## Mini case study: błąd po deploymencie

Nowa wersja backendu została wdrożona.

Po kilku minutach Sentry pokazuje:

- nowy typ wyjątku,
- tylko w środowisku `prod`,
- tylko dla endpointu `/orders/export`,
- od releasu `v1.8.0`.

To bardzo szybko zawęża obszar poszukiwań.

Bez takiego narzędzia diagnoza mogłaby trwać dużo dłużej.

## Mini case study: błąd rzadki, ale kosztowny

Użytkownicy zgłaszają sporadyczny problem.

W logach trudno go znaleźć, bo dzieje się rzadko.

Sentry pokazuje:

- ten sam wyjątek wystąpił 6 razy w ciągu ostatnich 3 dni,
- dotyczy jednego typu użytkownika,
- pojawia się po konkretnym flow.

To bardzo cenna różnica między "gdzieś kiedyś był error" a realną diagnostyką produkcyjną.

## Częste pułapki

### 1. Integracja bez release i środowiska

Wtedy tracisz dużą część wartości operacyjnej.

### 2. Wysyłanie zbyt wielu mało istotnych zdarzeń

To prowadzi do szumu i słabszej priorytetyzacji.

### 3. Brak kontekstu użytkownika albo requestu

Błędy są wtedy mniej użyteczne diagnostycznie.

### 4. Traktowanie Sentry jako zamiennika logów

To nie jest dobra droga.

### 5. Brak zasad alertowania

Jeśli wszystko krzyczy, zespół przestaje reagować sensownie.

## Co Pythonowiec powinien rozumieć

Dobrze, żebyś umiał:

- rozumieć, po co narzędzia błędowe zbierają więcej niż sam stack trace,
- wiedzieć, że release i środowisko mocno zwiększają wartość diagnostyczną,
- nie zasypywać systemu błędów bezużytecznym szumem,
- łączyć Sentry z logami, metrykami i procesem releasowym,
- traktować narzędzie jako wsparcie operacyjne, nie magiczne rozwiązanie wszystkiego.

## Output myślowy

### Bez narzędzia typu Sentry

- błędy są trudniejsze do grupowania,
- wolniej widać skalę problemu,
- regresje po deploymencie są mniej czytelne.

### Z narzędziem typu Sentry

- błędy są bardziej uporządkowane,
- łatwiej widzieć wpływ releasu,
- łatwiej priorytetyzować problemy i reagować szybciej.

## Najważniejsze do zapamiętania

- Sentry pomaga zbierać, grupować i analizować błędy z działającego systemu.
- Największą wartość daje z kontekstem: release, środowisko, request, użytkownik.
- Nie zastępuje logów, metryk ani tracingu.
- Może bardzo przyspieszyć diagnozę regresji po deploymencie.
- Bez sensownej selekcji i kontekstu łatwo zamienić je w źródło szumu.

## Ćwiczenia

1. Wyjaśnij własnymi słowami, czym Sentry daje więcej niż zwykły log błędu.
2. Wypisz pięć informacji, które zwiększają wartość diagnostyczną zdarzenia błędowego.
3. Opisz, czemu release w narzędziu błędowym jest tak ważny.
4. Wymyśl przykład szumu, który niepotrzebnie zaśmiecałby system błędów.
5. Rozpisz, jak wykorzystałbyś Sentry do diagnozy regresji po nowym deploymencie.
