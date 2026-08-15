# Testy integracyjne w Pythonie

## O co chodzi

Test integracyjny sprawdza współpracę kilku elementów systemu naraz.

Nie testujesz już tylko jednej małej funkcji w izolacji. Sprawdzasz, czy razem działają poprawnie np.:

- serwis i repozytorium,
- endpoint i warstwa walidacji,
- logika aplikacji i baza,
- dwa moduły komunikujące się przez realny kontrakt.

## Najprostsza intuicja

Unit test pyta:

- czy ta jedna jednostka działa poprawnie?

Test integracyjny pyta:

- czy te części razem naprawdę się dogadują?

To bardzo ważna różnica.

## Po co testy integracyjne

Bo bardzo wiele błędów nie siedzi w pojedynczej funkcji, tylko w styku między częściami systemu.

Przykłady:

- źle mapowane dane,
- zły format zapisu do bazy,
- niespójność modelu wejścia i modelu domenowego,
- zła konfiguracja zależności,
- różnice między fake a realną implementacją.

Unit test może tego nie złapać.

## Przykład intuicyjny

Masz serwis:

- przyjmuje dane zamówienia,
- waliduje je,
- zapisuje do repozytorium.

Unit test serwisu może przejść świetnie z mockiem.

Ale dopiero test integracyjny pokaże, czy:

- realne repo przyjmuje ten format,
- zapis działa,
- dane wracają zgodnie z oczekiwaniem.

## Kiedy test integracyjny ma sens

Szczególnie gdy:

- warstwy systemu mają realną współpracę,
- problem może siedzieć na granicy modułów,
- chcesz mieć więcej zaufania niż daje sam unit test,
- integracja z bazą albo adapterem jest ważna biznesowo.

## Kiedy nie przesadzać

Nie każda rzecz wymaga testu integracyjnego.

Jeśli masz prostą czystą funkcję bez zależności, unit test zwykle wystarczy.

Testy integracyjne są cięższe, wolniejsze i droższe w utrzymaniu, więc powinny być używane tam, gdzie naprawdę dają wartość.

## Przykład mentalny: serwis + repozytorium

Masz:

- `OrderService`,
- `OrderRepository`.

Unit test serwisu z mockiem repo sprawdza, że:

- serwis wywołuje repo poprawnie.

Test integracyjny sprawdza dodatkowo, czy:

- prawdziwa implementacja repo działa z tym serwisem,
- zapis i odczyt mają sens,
- integracja naprawdę działa poza symulacją.

## Czego test integracyjny nie powinien robić bez sensu

Nie powinien:

- udawać całego świata, jeśli wystarczy mniejszy zakres,
- stawać się ciężkim E2E bez potrzeby,
- obejmować zbyt wielu warstw naraz, gdy problem można uchwycić niżej.

To nadal test z określonym zakresem, nie chaos.

## Granica między unit a integracją

To nie zawsze jest idealnie ostre.

Ale dobra intuicja jest taka:

- im więcej realnych zależności współpracuje razem,
- tym bardziej wchodzisz w test integracyjny.

## Mini case study

Bug: endpoint tworzy rekord, ale w bazie jedno pole zapisuje się pod złą nazwą.

Unit test serwisu przechodzi, bo mock repo nic o tym nie wie.

Test integracyjny z prawdziwą warstwą danych może od razu ujawnić problem.

To świetny przykład wartości integracji.

## Typowe błędy początkujących

- brak testów integracyjnych tam, gdzie granice modułów są ryzykowne,
- zbyt ciężkie testy integracyjne obejmujące pół systemu,
- testowanie wszystkiego mockami i myślenie, że to wystarczy,
- brak jasnej odpowiedzi, co konkretnie test integracyjny ma chronić.

## Szybka ściąga

- test integracyjny sprawdza współpracę kilku części systemu,
- jest cięższy niż unit test, ale daje więcej zaufania,
- szczególnie przydaje się na granicach warstw i adapterów,
- nie powinien być ani zbyt mały, ani bezmyślnie ogromny.

## Ćwiczenia

1. Podaj 3 przykłady rzeczy, które warto testować integracyjnie.
2. Opisz różnicę między testem serwisu z mockiem a testem integracyjnym serwisu z prawdziwym repo.
3. Wskaż granicę systemu, gdzie bug może ujawnić się tylko w integracji.
4. Zastanów się, które fragmenty Twojego projektu wymagają takiego poziomu zaufania.
5. Napisz własnymi słowami, co dokładnie ma chronić dobry test integracyjny.

## Najważniejsze do zapamiętania

- Test integracyjny sprawdza współpracę realnych elementów systemu.
- Jest bardzo ważny tam, gdzie błędy rodzą się na styku warstw.
- Mocki nie zastępują wszystkich integracji.
- Integracja daje więcej zaufania, ale kosztuje więcej niż unit test.
- Trzeba świadomie wybierać, które współprace naprawdę warto testować na tym poziomie.
