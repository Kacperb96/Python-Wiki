# Obrazy lekkie i bezpieczne python

## O czym jest ten rozdział

W projektach produkcyjnych nie wystarczy, że obraz "po prostu działa".

Bardzo ważne stają się pytania:

- jak duży jest obraz,
- ile rzeczy naprawdę zawiera,
- czy nie niesie zbędnego ryzyka bezpieczeństwa,
- czy nie ma w nim śmieci, narzędzi i plików, które nie są potrzebne w runtime.

To właśnie temat lekkich i bezpieczniejszych obrazów.

## Najprostsza intuicja

Im obraz jest większy i bardziej przeładowany, tym zwykle:

- dłużej się buduje,
- dłużej się pobiera,
- dłużej się wdraża,
- ma większą powierzchnię ataku,
- trudniej go utrzymywać.

To nie znaczy, że zawsze trzeba obsesyjnie ścinać każdy megabajt, ale warto świadomie ograniczać to, co trafia do runtime.

## Co zwykle niepotrzebnie trafia do obrazu

Częste problemy:

- cache narzędzi,
- pliki testowe niewymagane do runtime,
- `.git`,
- lokalne artefakty,
- pakiety buildowe potrzebne tylko chwilowo,
- pliki tymczasowe,
- sekrety lub pliki konfiguracyjne z developmentu.

## `python:slim` i podobne bazy

Na start często lepiej myśleć o lżejszej bazie niż o pełnym, ciężkim obrazie systemowym.

Przykład intuicyjny:

```dockerfile
FROM python:3.12-slim
```

To nie znaczy, że zawsze jest to jedyny dobry wybór, ale bardzo często to sensowniejsza baza niż pełny obraz z mnóstwem niepotrzebnych elementów.

## Multi-stage build: po co to istnieje

Multi-stage build pozwala oddzielić etap budowania od etapu uruchamiania.

Najprostsza intuicja:

- w pierwszym etapie masz cięższe narzędzia,
- w drugim zostawiasz tylko to, co potrzebne do runtime.

Dzięki temu finalny obraz może być:

- lżejszy,
- czystszy,
- bezpieczniejszy.

## Przykład intuicyjny

### Etap build

- instalujesz narzędzia potrzebne do kompilacji,
- budujesz zależności,
- przygotowujesz artefakty.

### Etap runtime

- kopiujesz tylko to, co potrzebne do uruchomienia aplikacji.

To bardzo dojrzały wzorzec.

## Run as non-root

Uruchamianie aplikacji jako `root` zwiększa ryzyko.

Lepsza praktyka to uruchamianie jako użytkownik z mniejszymi uprawnieniami tam, gdzie to możliwe.

Najprostsza intuicja:

- jeśli coś pójdzie źle wewnątrz kontenera,
- mniejsze uprawnienia ograniczają skalę szkody.

To nie daje pełnego bezpieczeństwa, ale jest ważnym elementem ograniczania ryzyka.

## Aktualność bazowego obrazu

To także ważne.

Jeśli bazowy obraz jest stary, możesz nieświadomie brać ze sobą:

- stare pakiety systemowe,
- znane podatności,
- nieaktualne biblioteki runtime.

To znów pokazuje, że obraz to nie tylko "opakowanie na kod", ale element bezpieczeństwa systemu.

## Before/after

### Słabszy obraz

- ciężka baza,
- dużo niepotrzebnych plików,
- narzędzia buildowe w runtime,
- proces jako `root`,
- brak kontroli nad zawartością.

### Lepszy obraz

- lżejsza baza,
- tylko potrzebne pliki,
- rozdzielenie build/runtime,
- brak sekretów,
- mniej uprzywilejowany użytkownik,
- bardziej świadoma zawartość obrazu.

## Sekrety i dane wrażliwe

To trzeba powtórzyć mocno.

Nie chcesz mieć w obrazie:

- kluczy API,
- haseł,
- prywatnych certyfikatów,
- lokalnych `.env` z produkcyjnymi sekretami.

Jeśli coś trafi do obrazu, może później zostać:

- wyciągnięte z rejestru,
- podejrzane w warstwach,
- przypadkowo ujawnione.

## Minimalizacja powierzchni ataku

Najprościej myśl o tym tak:

- im mniej rzeczy w obrazie,
- tym mniej rzeczy może zostać wykorzystanych, jeśli coś pójdzie źle.

Nie chodzi tylko o rozmiar, ale też o liczbę pakietów, narzędzi i zbędnych komponentów.

## Mini case study: obraz do weba

Masz aplikację FastAPI.

### Słabszy wariant

- pełny obraz systemowy,
- narzędzia developerskie,
- testy i cache w środku,
- uruchomienie jako `root`.

### Lepszy wariant

- lżejsza baza,
- tylko runtime dependencies,
- brak testowych śmieci,
- mniejsza liczba pakietów systemowych,
- sensowniejszy użytkownik uruchomieniowy.

To nie tylko kwestia elegancji. To realny wpływ na bezpieczeństwo i operacje.

## Mini case study: worker z biblioteką systemową

Czasem worker potrzebuje dodatkowych bibliotek systemowych do konkretnego zadania, np. generowania PDF czy przetwarzania obrazów.

Tu ważna jest świadoma decyzja:

- co naprawdę musi być w obrazie workera,
- czy web musi mieć to samo,
- czy nie warto rozdzielić obrazów lub etapów budowy.

To pokazuje, że "jeden obraz do wszystkiego" nie zawsze jest najlepszym pomysłem.

## Co Pythonowiec powinien rozumieć

Dobrze, żebyś umiał:

- widzieć obraz jako artefakt bezpieczeństwa i runtime, nie tylko wygodne opakowanie,
- ograniczać śmieci i zbędne zależności,
- rozumieć sens multi-stage build,
- nie uruchamiać wszystkiego jako `root` bez potrzeby,
- pytać, co naprawdę jest potrzebne w finalnym kontenerze.

## Output myślowy

### Naiwny obraz

- działa,
- ale jest cięższy, bardziej ryzykowny i mniej elegancki operacyjnie.

### Dojrzalszy obraz

- jest bardziej przewidywalny,
- lżejszy,
- mniejszy i zwykle bezpieczniejszy,
- lepiej nadaje się do realnych wdrożeń.

## Najważniejsze do zapamiętania

- Lekki obraz to nie tylko kwestia wygody, ale też bezpieczeństwa i operacji.
- W runtime powinno trafiać tylko to, co naprawdę potrzebne.
- Multi-stage build bardzo często pomaga.
- Nie uruchamiaj bezrefleksyjnie kontenera jako `root`.
- Obraz powinien być świadomie utrzymywanym artefaktem, nie workiem na wszystko.

## Ćwiczenia

1. Wyjaśnij własnymi słowami, czemu ciężki obraz jest problemem.
2. Wypisz pięć rzeczy, które często niepotrzebnie trafiają do obrazu.
3. Opisz intuicję multi-stage build bez używania definicji podręcznikowej.
4. Wyjaśnij, czemu uruchamianie jako `root` jest ryzykowne.
5. Rozpisz różnicę między naiwnym a dojrzalszym obrazem dla aplikacji webowej.
