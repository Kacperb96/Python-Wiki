# Refaktoryzacja w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest refaktoryzacja](#czym-jest-refaktoryzacja)
3. [Po co refaktoryzować kod](#po-co-refaktoryzować-kod)
4. [Refaktoryzacja a zmiana zachowania](#refaktoryzacja-a-zmiana-zachowania)
5. [Małe kroki](#małe-kroki)
6. [Rola testów](#rola-testów)
7. [Typowe cele refaktoryzacji](#typowe-cele-refaktoryzacji)
8. [Typowe błędy początkujących](#typowe-błędy-początkujących)
9. [Praktyczne przykłady](#praktyczne-przykłady)
10. [Dobre praktyki](#dobre-praktyki)
11. [Podsumowanie](#podsumowanie)
12. [Mini ściąga](#mini-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Refaktoryzacja to poprawianie struktury kodu bez zmiany jego zewnętrznego zachowania.

To jedna z najważniejszych codziennych umiejętności profesjonalnego programisty.

---

## Czym jest refaktoryzacja

Nie chodzi o "pisanie wszystkiego od nowa".

Chodzi o uporządkowanie kodu tak, aby był:

- czytelniejszy,
- prostszy,
- łatwiejszy do testowania,
- łatwiejszy do rozwijania.

---

## Po co refaktoryzować kod

Bo kod z czasem naturalnie się starzeje.

Bez refaktoryzacji rośnie:

- chaos,
- duplikacja,
- lęk przed zmianą,
- koszt utrzymania.

---

## Refaktoryzacja a zmiana zachowania

To kluczowe rozróżnienie.

Refaktoryzacja:

- zmienia strukturę,
- nie powinna zmieniać efektu biznesowego.

Jeśli zmieniasz strukturę i zachowanie naraz, ryzyko rośnie dużo bardziej.

---

## Małe kroki

Najbezpieczniejsza refaktoryzacja jest zwykle:

- mała,
- iteracyjna,
- łatwa do cofnięcia lub sprawdzenia.

Duże "wielkie sprzątanie" często kończy się problemami.

---

## Rola testów

Testy są siatką bezpieczeństwa dla refaktoryzacji.

Bez nich dużo trudniej mieć pewność, że uporządkowanie kodu niczego nie zepsuło.

---

## Typowe cele refaktoryzacji

Najczęściej:

- rozbicie długiej funkcji,
- wydzielenie powtarzającej się logiki,
- poprawa nazw,
- rozdzielenie odpowiedzialności,
- uproszczenie warunków,
- usunięcie martwego kodu.

---

## Typowe błędy początkujących

- przepisywanie wszystkiego naraz,
- brak testów przed zmianą,
- mieszanie refaktoryzacji z nowym featurem w jednym ruchu,
- poprawianie stylu bez rozwiązania realnego problemu strukturalnego.

---

## Praktyczne przykłady

### Długa funkcja

Jedna funkcja:

- pobiera dane,
- waliduje,
- liczy,
- zapisuje,
- loguje.

To dobry kandydat do rozbicia.

### Lepszy kierunek

- funkcja walidująca,
- funkcja licząca,
- warstwa zapisu osobno.

---

## Dobre praktyki

- refaktoryzuj małymi krokami,
- zaczynaj od miejsc, które realnie bolą,
- trzymaj testy blisko zmian,
- nie myl refaktoryzacji z przepisywaniem dla sportu.

---

## Podsumowanie

Refaktoryzacja to nie luksus, tylko podstawowe narzędzie utrzymania jakości kodu.

Najlepsza refaktoryzacja upraszcza życie zespołu, zamiast tylko zmieniać układ plików.

---

## Mini ściąga

Najważniejsze:

- refaktoryzacja poprawia strukturę,
- nie powinna zmieniać zachowania,
- najlepiej robić ją małymi krokami,
- testy są kluczowe.

---

## Ćwiczenia

1. Wyjaśnij różnicę między refaktoryzacją a nowym featurem.
2. Podaj przykład długiej funkcji do rozbicia.
3. Wyjaśnij, czemu testy pomagają w refaktoryzacji.
4. Podaj przykład duplikacji, którą warto usunąć.
5. Wyjaśnij, czemu małe kroki są bezpieczniejsze.

---

## Przykładowe rozwiązania

### 1. Różnica

Refaktoryzacja poprawia strukturę bez zmiany zachowania, a nowy feature dodaje nowe zachowanie.

### 2. Długa funkcja

Na przykład funkcja obsługująca cały proces zamówienia od walidacji po zapis i mail.

### 3. Testy

Bo pozwalają szybko sprawdzić, czy po zmianie struktury system nadal działa tak samo.

### 4. Duplikacja

Ten sam kod walidacyjny skopiowany w trzech endpointach.

### 5. Małe kroki

Bo łatwiej znaleźć źródło problemu i mniejsze jest ryzyko dużej regresji.
