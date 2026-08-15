# Dependency security python

Bezpieczeństwo twojej aplikacji to nie tylko to, co sam napisałeś.

To także:

- biblioteki, które instalujesz,
- ich zależności pośrednie,
- aktualizacje,
- porzucone pakiety,
- podatności w narzędziach budowania i uruchamiania.

## 1. Problem myślenia "to tylko mała biblioteka"

Każdy pakiet:

- wnosi własny kod,
- może mieć własne błędy,
- może dodać kolejne zależności,
- może przestać być utrzymywany,
- może stać się źródłem podatności.

Im więcej paczek, tym większa powierzchnia ryzyka.

## 2. Najczęstsze błędy

- instalowanie pakietów bez zastanowienia,
- kopiowanie zależności z tutoriala,
- brak aktualizacji przez wiele miesięcy,
- brak świadomości, co w ogóle siedzi w projekcie,
- używanie ciężkiej biblioteki do czegoś, co umie standard library.

## 3. Dobre pytania przed dołożeniem biblioteki

- czy naprawdę jej potrzebuję?
- czy projekt jest utrzymywany?
- czy ta biblioteka ma dobrą reputację?
- czy nie ciągnie bardzo wielu kolejnych pakietów?
- czy problem da się rozwiązać prościej?

## 4. Wersje i aktualizacje

Brak aktualizacji bywa groźny, bo:

- zostajesz na znanych podatnościach,
- zależności stają się przestarzałe,
- coraz trudniej bezpiecznie zrobić upgrade później.

Z drugiej strony:

- bezmyślny upgrade wszystkiego naraz też może psuć system.

Potrzebne jest rozsądne utrzymanie.

## 5. Mniej zależności = mniej ryzyk

Nie zawsze, ale bardzo często tak.

Jeśli coś da się zrobić:

- prosto,
- czytelnie,
- biblioteką standardową,

to czasem warto nie dokładać kolejnego pakietu.

## 6. Przykład myślowy

Masz potrzebę prostego parsowania ścieżek i kopiowania plików.

Zanim dołożysz zewnętrzną bibliotekę, sprawdź:

- `pathlib`
- `shutil`

Może nie potrzebujesz nic więcej.

## 7. Częsty błąd początkujących

`skoro biblioteka jest popularna, to na pewno jest bezpieczna`

Popularność pomaga, ale nie daje gwarancji.

## Zadania

1. Podaj trzy ryzyka związane z dokładaniem wielu zależności.
2. Wyjaśnij, czemu czasem standard library bywa lepszym wyborem.
3. Opisz, jakie pytania warto sobie zadać przed instalacją nowego pakietu.
