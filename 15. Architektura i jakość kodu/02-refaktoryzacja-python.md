# Refaktoryzacja w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest refaktoryzacja](#czym-jest-refaktoryzacja)
3. [Po co refaktoryzować kod](#po-co-refaktoryzować-kod)
4. [Refaktoryzacja a zmiana zachowania](#refaktoryzacja-a-zmiana-zachowania)
5. [Małe kroki](#małe-kroki)
6. [Rola testów](#rola-testów)
7. [Typowe cele refaktoryzacji](#typowe-cele-refaktoryzacji)
8. [Przykład mentalny](#przykład-mentalny)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczna ściąga](#praktyczna-ściąga)
11. [Ćwiczenia](#ćwiczenia)
12. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

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

Refaktoryzacja nie jest luksusem.

To normalne narzędzie utrzymania jakości.

---

## Refaktoryzacja a zmiana zachowania

To kluczowe rozróżnienie.

Refaktoryzacja:

- zmienia strukturę,
- nie powinna zmieniać efektu biznesowego.

Jeśli zmieniasz strukturę i zachowanie naraz, ryzyko rośnie dużo bardziej.

Dlatego warto mentalnie oddzielać:

- "sprzątanie",
- od "wprowadzania nowej funkcjonalności".

---

## Małe kroki

Najbezpieczniejsza refaktoryzacja jest zwykle:

- mała,
- iteracyjna,
- łatwa do cofnięcia albo sprawdzenia.

Duże "wielkie sprzątanie" często kończy się problemami.

---

## Rola testów

Testy są siatką bezpieczeństwa dla refaktoryzacji.

Bez nich dużo trudniej mieć pewność, że uporządkowanie kodu niczego nie zepsuło.

To właśnie dlatego dobra refaktoryzacja bardzo często idzie w parze z dobrymi testami.

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

## Przykład mentalny

Masz funkcję, która:

- odbiera dane,
- waliduje je,
- liczy wynik,
- zapisuje coś do bazy,
- buduje odpowiedź.

Lepszy kierunek po refaktoryzacji:

- funkcja walidująca,
- funkcja licząca,
- warstwa zapisu osobno,
- budowa odpowiedzi osobno.

Efekt biznesowy zostaje ten sam, ale struktura robi się dużo zdrowsza.

---

## Typowe błędy początkujących

- przepisywanie wszystkiego naraz,
- brak testów przed zmianą,
- mieszanie refaktoryzacji z nowym featurem w jednym ruchu,
- poprawianie stylu bez rozwiązania realnego problemu strukturalnego,
- "refaktoryzacja dla sportu" bez realnej potrzeby.

---

## Praktyczna ściąga

### Dobre pytania przed refaktoryzacją

- Co dokładnie jest problemem?
- Czy mam testy albo inny sposób weryfikacji?
- Czy mogę rozbić zmianę na małe kroki?
- Czy zmieniam strukturę, czy także zachowanie?

### Dobra zasada

Najpierw zrozum kod, potem go poprawiaj.

---

## Ćwiczenia

1. Rozbij długą funkcję na mniejsze części.
2. Usuń prostą duplikację.
3. Zmień złe nazwy na bardziej opisowe.
4. Rozdziel walidację, liczenie i zapis do osobnych elementów.
5. Wyjaśnij własnymi słowami, czemu małe refaktoryzacje są bezpieczniejsze.

---

## Najważniejsze do zapamiętania

- Refaktoryzacja poprawia strukturę kodu bez zmiany zachowania.
- Najlepiej robić ją małymi krokami.
- Testy bardzo zwiększają bezpieczeństwo zmian.
- Celem refaktoryzacji jest uproszczenie i obniżenie kosztu przyszłych zmian.
