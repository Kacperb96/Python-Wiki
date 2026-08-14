# Zestaw ćwiczeń praktycznych — 16. Bezpieczeństwo

## Poziom 1 — podstawy bezpieczeństwa

1. Wypisz 5 miejsc, w których do aplikacji wchodzą nieufne dane.
2. Wskaż, które dane w projekcie powinny być traktowane jako sekrety.
3. Znajdź przykład hardkodowanego sekretu i opisz, czemu to zły pomysł.

## Poziom 2 — walidacja danych

4. Napisz walidację wieku, który nie może być ujemny.
5. Napisz walidację wymaganych pól w prostym payloadzie słownikowym.
6. Rozdziel walidację techniczną i biznesową na małym przykładzie.
7. Napisz przykład, gdzie frontend waliduje dane, ale backend i tak musi zrobić to ponownie.

## Poziom 3 — env vars i sekrety

8. Odczytaj `API_TOKEN` z env var.
9. Zaprojektuj `.env.example` dla małego projektu.
10. Opisz, które dane powinny być w env vars, a które nie muszą.

## Poziom 4 — bezpieczne subprocess i injection

11. Pokaż przykład bezpiecznego użycia `subprocess.run()` z listą argumentów.
12. Pokaż ryzykowny przykład z `shell=True`.
13. Napisz bezpieczniejszą wersję polecenia budowanego wcześniej przez f-string.
14. Pokaż przykład SQL injection i popraw go przez parametryzację.
15. Pokaż przykład command injection i opisz ryzyko.

## Poziom 5 — pliki i serializacja

16. Opisz przykład path traversal przy pobieraniu pliku po nazwie od użytkownika.
17. Zaprojektuj sposób ograniczenia ścieżki do jednego katalogu bazowego.
18. Opisz, czemu `pickle` nie nadaje się do nieufnych danych z zewnątrz.
19. Zbuduj bezpieczniejszy przepływ: JSON -> parse -> walidacja -> zapis.

## Zadanie końcowe

20. Zrób mini audyt bezpieczeństwa małego projektu Python:
   - gdzie wchodzi input,
   - gdzie są sekrety,
   - gdzie jest baza,
   - czy są operacje systemowe,
   - czy jest ryzyko path traversal,
   - czy dane są walidowane,
   - jakie 5 najważniejszych poprawek trzeba wdrożyć najpierw.
