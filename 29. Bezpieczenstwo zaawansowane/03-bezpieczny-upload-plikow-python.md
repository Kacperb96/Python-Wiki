# Bezpieczny upload plikow python

Upload plików wygląda niegroźnie, ale to jeden z tych obszarów, gdzie bardzo łatwo zrobić sobie problem.

Dlaczego?

Bo użytkownik nie dostarcza tylko "danych". Dostarcza obiekt, który:

- ma nazwę,
- ma rozmiar,
- ma typ,
- ma zawartość,
- może być złośliwy,
- może próbować wykorzystać parsery, pliki tymczasowe albo ścieżki systemowe.

## 1. Co może pójść źle

Przy uploadzie ryzyka obejmują:

- zbyt duży plik,
- zły format,
- fałszywe rozszerzenie,
- ścieżkę prowadzącą w niechciane miejsce,
- próbę nadpisania istniejących plików,
- przechowywanie pliku w publicznie dostępnym miejscu bez kontroli.

## 2. Zły sposób myślenia

Niebezpieczny wzorzec:

```python
filename = uploaded_file.filename
path = f"uploads/{filename}"
save(uploaded_file, path)
```

Problem:

- użytkownik kontroluje nazwę,
- użytkownik może próbować wymusić dziwną ścieżkę,
- nazwa może kolidować z istniejącymi plikami,
- sama nazwa i rozszerzenie niczego nie gwarantują.

## 3. Lepsze podejście

Zdrowszy schemat:

1. nadaj plikowi własny identyfikator po stronie serwera
2. zapisuj go w kontrolowanym katalogu
3. waliduj rozmiar
4. waliduj dopuszczalne typy
5. nie ufaj samemu rozszerzeniu
6. ograniczaj, kto może plik później pobrać

## 4. Przykład myślowy

Zamiast:

```text
uploads/zdjecie.png
```

lepiej:

```text
uploads/2026/08/file_8f2b31a.dat
```

A metadane trzymaj osobno:

- oryginalna nazwa,
- właściciel,
- typ zaakceptowany przez system,
- rozmiar,
- data dodania.

## 5. Typ pliku a zaufanie

To, że plik ma nazwę:

```text
raport.pdf
```

nie oznacza, że naprawdę jest poprawnym PDF-em.

To, że plik ma rozszerzenie:

```text
.jpg
```

nie oznacza, że zawartość jest bezpieczna.

Dlatego nie wystarczy sprawdzać:

- tylko nazwy,
- tylko rozszerzenia,
- tylko jednego nagłówka od klienta.

## 6. Dodatkowe dobre praktyki

- ustaw limity rozmiaru,
- ogranicz liczbę plików,
- nie trzymaj wszystkiego w katalogu publicznym,
- rozważ skanowanie lub dodatkową obróbkę w zależności od typu pliku,
- zapisuj informacje audytowe: kto wrzucił, kiedy, jaki rozmiar.

## 7. Częsty błąd początkujących

`skoro frontend pozwala tylko na .png i .jpg, to backend jest bezpieczny`

Nie. Frontend nie jest granicą zaufania.

## 8. Pseudo-output myślowy

Bezpieczniejszy system może działać tak:

Wejście:

```text
oryginalna nazwa: selfie.png
rozmiar: 1.8 MB
użytkownik: user_14
```

Po stronie systemu:

```text
zapisano jako: file_8f2b31a.dat
katalog: uploads/private/2026/08/
status: accepted
owner: user_14
```

## Zadania

1. Wyjaśnij, czemu sama nazwa pliku od użytkownika nie powinna być używana jako finalna ścieżka zapisu.
2. Podaj co najmniej 5 rzeczy, które warto sprawdzać przy uploadzie.
3. Opisz, czemu kontrola tylko po stronie frontendu nie wystarcza.
