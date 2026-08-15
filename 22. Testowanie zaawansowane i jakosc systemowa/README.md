# 22. Testowanie zaawansowane i jakość systemowa

To jest folder o tym, jak testowanie przestaje być tylko pisaniem kilku unit testów, a zaczyna być elementem budowania zaufania do całego systemu.

Na wcześniejszych etapach repo był już dział o testowaniu podstawowym. Tutaj idziemy poziom wyżej.

Pojawiają się pytania takie jak:

- jak testować współpracę kilku warstw naraz,
- jak nie utopić się w zbyt ciężkich testach,
- kiedy użyć fake, a kiedy mock,
- jak przygotowywać dane testowe bez chaosu,
- czym są flaky tests i czemu są tak groźne,
- jak zbudować sensowną strategię testów dla projektu.

To nie jest już tylko temat składni `pytesta`. To temat jakości systemu.

## Po co ten folder

W prawdziwej pracy problem bardzo rzadko wygląda tak:

- "czy ta jedna funkcja zwraca 4 zamiast 5?"

Dużo częściej problem brzmi:

- czy endpoint działa razem z walidacją, serwisem i bazą,
- czy integracja z innym systemem nadal dotrzymuje kontraktu,
- czy testy nie są kruche,
- czy mamy zaufanie do zmian przed deployem,
- czy testy wykrywają realne regresje, a nie tylko zajmują czas.

Właśnie tym zajmuje się ten moduł.

## Czego nauczysz się w tym dziale

Po przerobieniu tego folderu powinieneś rozumieć:

- czym są testy integracyjne i kiedy mają sens,
- czym różnią się testy E2E od integracyjnych,
- czym są contract tests,
- jak używać fixtures i test data builders,
- czym różnią się fake, mock i stub,
- skąd biorą się flaky tests,
- jak zbudować strategię testów dla projektu zamiast zbioru przypadkowych testów.

Dodatkowo masz teraz też przekrojowy plik:

- `08-case-study-poziomy-testow-python.md`

który pokazuje na jednym mini systemie, jak rozkładać odpowiedzialność między poziomy testów.

## Najważniejsza zasada tego folderu

Celem testów nie jest mieć dużo testów.

Celem testów jest mieć **zaufanie do systemu**.

To bardzo ważne rozróżnienie.

Można mieć:

- dużo testów i mało zaufania,
- mało testów i duże ryzyko,
- albo sensowny zestaw testów, który naprawdę chroni ważne zachowania.

Ten folder ma prowadzić do trzeciej opcji.

## Jak czytać ten folder

Najlepiej iść po kolei:

1. `01-testy-integracyjne-python.md`
2. `02-testy-e2e-python.md`
3. `03-contract-tests-python.md`
4. `04-fixtures-i-test-data-builders-python.md`
5. `05-fake-mock-stub-python.md`
6. `06-flaky-tests-python.md`
7. `07-strategia-testow-w-projekcie-python.md`
8. `08-case-study-poziomy-testow-python.md`

Ta kolejność ma sens, bo najpierw budujesz intuicję poziomów testów, potem poznajesz techniki wspierające ich pisanie, a na końcu składasz to w sensowną strategię na jednym konkretnym case study.

## Na co szczególnie uważać

Najczęstsze pułapki w zaawansowanym testowaniu to:

- zbyt ciężkie testy do prostych rzeczy,
- zbyt dużo mocków i zbyt mało realnego przepływu,
- duplikacja danych testowych w 20 miejscach,
- niestabilne flaky tests,
- brak rozróżnienia między rodzajami testów,
- brak myślenia, co naprawdę ma chronić dany test.

## Jak najlepiej ćwiczyć

Najlepiej na małym, ale realistycznym module.

Na przykład:

- endpoint tworzenia zamówienia,
- integracja z repozytorium,
- walidacja i serwis,
- wysyłka powiadomienia,
- kontrakt odpowiedzi API.

To pozwala zobaczyć, jak różne typy testów obejmują różne warstwy systemu.

## Po czym poznasz, że temat siedzi

Dobry znak, jeśli potrafisz:

- wskazać, kiedy napisać test integracyjny, a kiedy E2E,
- wyjaśnić, po co istnieją contract tests,
- dobrać fake zamiast przesadnego mockowania,
- zbudować czytelne dane testowe bez bałaganu,
- rozpoznać flaky test i wyjaśnić, czemu jest niebezpieczny,
- zaproponować sensowną strategię testów dla projektu,
- rozpisać poziomy testów dla jednego konkretnego modułu.

## Podsumowanie

To jest folder o dojrzalszym testowaniu. Nie chodzi tu już tylko o to, jak uruchomić test, ale o to, jak używać testów jako narzędzia do kontroli jakości, bezpieczeństwa zmian i budowania stabilnego systemu.
