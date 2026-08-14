# Walidacja danych w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co walidować dane](#po-co-walidować-dane)
3. [Walidacja a bezpieczeństwo](#walidacja-a-bezpieczeństwo)
4. [Walidacja a logika biznesowa](#walidacja-a-logika-biznesowa)
5. [Typy, format i zakres wartości](#typy-format-i-zakres-wartości)
6. [Walidacja na granicy systemu](#walidacja-na-granicy-systemu)
7. [Walidacja w API i formularzach](#walidacja-w-api-i-formularzach)
8. [Walidacja a Pydantic](#walidacja-a-pydantic)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczne przykłady](#praktyczne-przykłady)
11. [Dobre praktyki](#dobre-praktyki)
12. [Podsumowanie](#podsumowanie)
13. [Mini ściąga](#mini-ściąga)
14. [Ćwiczenia](#ćwiczenia)
15. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Walidacja danych to jeden z podstawowych mechanizmów obrony jakości i bezpieczeństwa systemu.

Jeśli aplikacja przyjmuje dane bez sensownej kontroli, problemy są tylko kwestią czasu.

---

## Po co walidować dane

Bo dane wejściowe mogą być:

- błędne,
- niepełne,
- w złym typie,
- złośliwe,
- niezgodne z regułami biznesowymi.

---

## Walidacja a bezpieczeństwo

Walidacja nie rozwiązuje całego bezpieczeństwa, ale jest bardzo ważną linią obrony.

Pomaga wcześniej odrzucić niepoprawne wejście.

---

## Walidacja a logika biznesowa

To nie to samo.

Walidacja odpowiada np.:

- czy email ma poprawny format,
- czy liczba jest dodatnia,
- czy pole istnieje.

Logika biznesowa odpowiada np.:

- czy użytkownik może kupić ten produkt,
- czy limit został przekroczony.

---

## Typy, format i zakres wartości

Najczęściej sprawdzasz:

- typ,
- wymagane pola,
- zakres liczbowy,
- długość tekstu,
- format danych.

---

## Walidacja na granicy systemu

Najlepiej walidować dane jak najbliżej wejścia do systemu.

Na przykład:

- przy requestach HTTP,
- przy odczycie pliku,
- przy wejściu z CLI,
- przy danych z zewnętrznego API.

---

## Walidacja w API i formularzach

To bardzo ważny obszar praktyczny.

API i formularze są naturalnym miejscem, gdzie do systemu wpadają dane z zewnątrz.

---

## Walidacja a Pydantic

`Pydantic` bardzo dobrze wspiera walidację w nowoczesnym Pythonie.

Szczególnie przydaje się w:

- FastAPI,
- konfiguracji,
- modelach danych wejściowych.

---

## Typowe błędy początkujących

- brak walidacji,
- walidacja zbyt późno,
- mylenie walidacji technicznej z biznesową,
- ufanie, że klient frontendowy "na pewno już sprawdził dane".

---

## Praktyczne przykłady

### Proste sprawdzenie

```python
def validate_age(age):
    if age < 0:
        raise ValueError("wiek nie moze byc ujemny")
```

### Format emaila

Walidacja może sprawdzać podstawowe wymagania formatu zanim dane trafią dalej.

---

## Dobre praktyki

- waliduj na granicy systemu,
- rozdzielaj walidację techniczną od biznesowej,
- nie ufaj klientowi,
- trzymaj komunikaty błędów czytelne i przewidywalne.

---

## Podsumowanie

Walidacja danych to jedna z tych praktyk, które mają ogromny wpływ zarówno na bezpieczeństwo, jak i stabilność aplikacji.

To fundament, nie dodatek.

---

## Mini ściąga

Najważniejsze:

- waliduj input,
- rób to możliwie wcześnie,
- rozróżniaj walidację techniczną i biznesową,
- nie ufaj danym z zewnątrz.

---

## Ćwiczenia

1. Wyjaśnij, po co walidować dane.
2. Podaj przykład walidacji technicznej.
3. Podaj przykład reguły biznesowej.
4. Wyjaśnij, czemu frontend nie wystarcza jako jedyna walidacja.
5. Wyjaśnij, czemu warto walidować dane na granicy systemu.

---

## Przykładowe rozwiązania

### 1. Po co walidować

Żeby odrzucać błędne lub niebezpieczne dane, zanim trafią głębiej do systemu.

### 2. Techniczna

Sprawdzenie, czy pole `age` jest liczbą dodatnią.

### 3. Biznesowa

Sprawdzenie, czy użytkownik nie przekroczył limitu zakupów.

### 4. Czemu frontend nie wystarcza

Bo klient może być złośliwy, błędny albo całkowicie pominąć frontend.

### 5. Granica systemu

Bo wtedy problem wykrywasz najwcześniej i nie rozlewasz błędnych danych po dalszych warstwach.
