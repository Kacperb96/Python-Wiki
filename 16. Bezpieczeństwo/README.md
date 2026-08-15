# 16. Bezpieczeństwo

To jest jeden z najważniejszych folderów w całym repo.

Dlaczego? Bo bezpieczeństwo nie jest osobnym „dodatkiem”, który robi się dopiero na końcu projektu. Ono przenika prawie każdy obszar programowania:

- dane wejściowe,
- pliki,
- bazę danych,
- API,
- logowanie,
- sekrety i konfigurację,
- operacje systemowe,
- uprawnienia użytkowników.

Można napisać aplikację, która działa poprawnie funkcjonalnie, a jednocześnie jest podatna na bardzo proste ataki lub błędy bezpieczeństwa. W praktyce oznacza to, że program:

- przyjmuje niebezpieczne dane,
- ujawnia sekrety,
- pozwala wykonać nieautoryzowane operacje,
- zapisuje lub odczytuje nie te pliki, które powinien,
- buduje ryzykowne zapytania do bazy,
- uruchamia niebezpieczne polecenia systemowe.

Ten folder ma dać Ci bardzo solidne podstawy bezpieczeństwa w Pythonie na poziomie programisty aplikacyjnego.

Nie chodzi tu jeszcze o pełny świat security engineering, pentestów czy zaawansowanej kryptografii. Chodzi o coś bardziej praktycznego i potrzebnego na co dzień:

- jak nie pisać podatnego kodu,
- jak myśleć o ryzyku,
- jak zauważać klasyczne błędy,
- jak wdrażać bezpieczniejsze nawyki od początku.

## Czego nauczysz się w tym folderze

Po przerobieniu tego modułu powinieneś rozumieć:

- dlaczego dane wejściowe są zawsze nieufne,
- czym różni się walidacja techniczna od biznesowej,
- jak bezpiecznie pracować z sekretami i zmiennymi środowiskowymi,
- jak używać `subprocess`, żeby nie otwierać drogi do command injection,
- czym jest SQL injection i jak broni przed nim parametryzacja,
- czym jest path traversal,
- dlaczego nie wolno bezmyślnie deserializować nieufnych danych,
- jak patrzeć na kod bardziej „napastniczo”, a nie tylko funkcjonalnie.

## Jak czytać ten folder

Najlepiej iść po kolei.

Kolejność nie jest przypadkowa:

1. najpierw dostajesz ogólne myślenie o bezpieczeństwie,
2. potem walidację danych,
3. następnie sekrety i konfigurację,
4. później ryzyka wokół procesów systemowych i baz danych,
5. na końcu ścieżki plikowe i serializację.

To daje dobrą progresję: od zasad ogólnych do coraz bardziej konkretnych kategorii podatności.

## Jak korzystać z materiału dobrze

Nie czytaj tego folderu jak samej teorii.

Lepiej przy każdym rozdziale zadawać sobie pytania:

- skąd wchodzą dane do programu,
- czy tym danym ufam bez powodu,
- gdzie tworzę ścieżki,
- czy gdzieś sklejam komendy lub SQL,
- czy przechowuję sekrety bezpiecznie,
- czy użytkownik może zrobić więcej, niż powinien,
- czy ten kod byłby bezpieczny, gdyby dane były złośliwe.

To bardzo ważny moment nauki: przestajesz patrzeć tylko z perspektywy „czy działa?”, a zaczynasz patrzeć też z perspektywy „czy to można nadużyć?”.

## Co ten folder daje praktycznie

Po solidnym przerobieniu tego działu powinieneś umieć:

- napisać bezpieczniejszy backend,
- lepiej projektować walidację,
- unikać klasycznych błędów początkujących,
- zauważać czerwone flagi w cudzym kodzie,
- robić prosty mini-audyt bezpieczeństwa małego projektu.

## Czego ten folder jeszcze nie próbuje pokryć w pełni

Ten moduł nie ma być pełnym podręcznikiem do:

- kryptografii,
- zaawansowanego uwierzytelniania,
- OAuth i OpenID Connect w pełnym zakresie,
- bezpieczeństwa infrastruktury,
- bezpieczeństwa kontenerów i chmury,
- pełnych praktyk DevSecOps.

Ale daje bardzo dobry fundament programistyczny. A to dokładnie ten poziom, od którego trzeba zacząć.

## Po czym poznasz, że materiał masz opanowany

Jeśli po tym folderze potrafisz:

- wskazać miejsca wejścia nieufnych danych,
- zaprojektować bezpieczniejszą walidację,
- odróżnić bezpieczne i niebezpieczne użycie `subprocess`,
- wyjaśnić, czemu `pickle` dla nieufnych danych to zły pomysł,
- pokazać bezpieczniejszą pracę z bazą i ścieżkami,
- znaleźć kilka podatności w prostym projekcie,

to znaczy, że masz już naprawdę sensowną bazę.

## Jak pracować z ćwiczeniami

Nie zatrzymuj się na samym przeczytaniu odpowiedzi czy teorii.

Najlepsza ścieżka to:

1. przeczytać rozdział,
2. własnymi słowami wytłumaczyć zagadnienie,
3. napisać mały przykład błędny,
4. poprawić go,
5. dopiero potem przejść dalej.

W bezpieczeństwie bardzo dużo daje porównywanie:

- wersji podatnej,
- wersji poprawionej,
- i zrozumienia, co dokładnie było ryzykiem.

## Podsumowanie

To zamykający, ale bardzo praktyczny folder. Łączy wiele wcześniejszych tematów z repo i pokazuje, że dobry Python to nie tylko kod działający, ale też kod odporniejszy na błędy, nadużycia i niebezpieczne scenariusze.

Czytaj go uważnie, testuj przykłady i staraj się patrzeć na kod nie tylko jak programista, ale też jak ktoś, kto próbuje znaleźć jego słabe miejsca.
