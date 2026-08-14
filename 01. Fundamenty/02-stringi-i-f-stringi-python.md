# Stringi i f-stringi w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest string](#czym-jest-string)
3. [Jak Python przechowuje tekst](#jak-python-przechowuje-tekst)
4. [Tworzenie stringów](#tworzenie-stringów)
5. [Cudzysłowy, znaki specjalne i escapowanie](#cudzysłowy-znaki-specjalne-i-escapowanie)
6. [Stringi wielolinijkowe](#stringi-wielolinijkowe)
7. [String jako sekwencja znaków](#string-jako-sekwencja-znaków)
8. [Indeksowanie i slicing](#indeksowanie-i-slicing)
9. [Niemutowalność stringów](#niemutowalność-stringów)
10. [Najważniejsze operacje na stringach](#najważniejsze-operacje-na-stringach)
11. [Najczęściej używane metody stringów](#najczęściej-używane-metody-stringów)
12. [`split()` i `join()`](#split-i-join)
13. [Wyszukiwanie i zamiana tekstu](#wyszukiwanie-i-zamiana-tekstu)
14. [Sprawdzanie zawartości tekstu](#sprawdzanie-zawartości-tekstu)
15. [Formatowanie tekstu](#formatowanie-tekstu)
16. [Czym są f-stringi](#czym-są-f-stringi)
17. [Wyrażenia wewnątrz f-stringów](#wyrażenia-wewnątrz-f-stringów)
18. [Format specifiers we f-stringach](#format-specifiers-we-f-stringach)
19. [Kiedy f-string nie jest najlepszym wyborem](#kiedy-f-string-nie-jest-najlepszym-wyborem)
20. [Częste pułapki początkujących](#częste-pułapki-początkujących)
21. [Praktyczne przykłady](#praktyczne-przykłady)
22. [Dobre praktyki](#dobre-praktyki)
23. [Podsumowanie](#podsumowanie)
24. [Mini ściąga](#mini-ściąga)
25. [Ćwiczenia](#ćwiczenia)
26. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Stringi są wszędzie:

- w `input()`,
- w nazwach plików,
- w adresach URL,
- w logach,
- w komunikatach dla użytkownika,
- w danych z API,
- w konfiguracji.

To jeden z najczęściej używanych typów w Pythonie. Warto znać go naprawdę dobrze, bo bardzo dużo codziennego kodu to właśnie praca na tekście.

---

## Czym jest string

String, czyli `str`, reprezentuje tekst.

Przykład:

```python
imie = "Anna"
miasto = "Krakow"
```

Każdy string jest obiektem typu `str`.

```python
print(type("Python"))
```

---

## Jak Python przechowuje tekst

W Pythonie 3 stringi są tekstem w Unicode.

To ważne, bo oznacza, że możesz pracować nie tylko na znakach ASCII, ale też na polskich znakach i znakach z innych języków.

```python
tekst = "Zażółć gęślą jaźń"
```

To nadal zwykły `str`.

W praktyce oznacza to:

- możesz bez problemu mieć polskie litery w stringach,
- długość napisu to liczba znaków, a nie bajtów,
- temat kodowania wróci mocniej przy plikach i sieci.

---

## Tworzenie stringów

Najczęstsze sposoby:

```python
a = "hello"
b = 'world'
c = ""
```

Pojedyncze i podwójne cudzysłowy działają tak samo. Najważniejsza jest spójność i czytelność.

---

## Cudzysłowy, znaki specjalne i escapowanie

Jeśli w stringu chcesz użyć tego samego rodzaju cudzysłowu, musisz go uciec znakiem `\` albo użyć drugiego rodzaju cudzysłowu.

```python
tekst1 = "Ona powiedziala: \"czesc\""
tekst2 = 'Ona powiedziala: "czesc"'
```

Przydatne znaki specjalne:

- `\n` nowa linia
- `\t` tabulator
- `\\` backslash

Przykład:

```python
print("Linia 1\nLinia 2")
```

---

## Stringi wielolinijkowe

Do dłuższego tekstu możesz użyć potrójnych cudzysłowów:

```python
opis = """To jest
dluzszy
tekst"""
```

Przydaje się to np. do:

- wiadomości,
- wielolinijkowych komunikatów,
- prostych szablonów,
- docstringów.

---

## String jako sekwencja znaków

String działa jak sekwencja.

To znaczy, że:

- ma długość,
- możesz pobierać pojedyncze znaki,
- możesz ciąć fragmenty,
- możesz po nim iterować.

```python
tekst = "Python"
print(len(tekst))
print(tekst[0])
for znak in tekst:
    print(znak)
```

Output:

```python
6
P
P
y
t
h
o
n
```

---

## Indeksowanie i slicing

Indeksy zaczynają się od `0`.

```python
tekst = "Python"
print(tekst[0])   # P
print(tekst[1])   # y
print(tekst[-1])  # n
```

Output:

```python
P
y
n
```

Slicing:

```python
print(tekst[:3])   # Pyt
print(tekst[3:])   # hon
print(tekst[1:5])  # ytho
print(tekst[::2])  # Pto
print(tekst[::-1]) # nohtyP
```

Output:

```python
Pyt
hon
ytho
Pto
nohtyP
```

Ważne:

- prawy koniec slice'a nie jest wliczany,
- ujemne indeksy liczą od końca,
- slicing nie zmienia oryginału, tylko zwraca nowy string.

---

## Niemutowalność stringów

Stringi są niemutowalne.

To znaczy, że nie możesz zmienić pojedynczego znaku w miejscu:

```python
tekst = "kot"
# tekst[0] = "p"  # TypeError
```

Zamiast tego tworzysz nowy string:

```python
tekst = "p" + tekst[1:]
print(tekst)
```

Output:

```python
pot
```

To bardzo ważna cecha, bo tłumaczy, dlaczego wiele metod stringów zwraca nowy wynik zamiast zmieniać istniejący tekst.

---

## Najważniejsze operacje na stringach

Łączenie:

```python
imie = "Anna"
nazwisko = "Kowalska"
pelne = imie + " " + nazwisko
```

Powielanie:

```python
print("ha" * 3)
```

Output:

```python
hahaha
```

Sprawdzanie:

```python
print("Py" in "Python")
print("Java" not in "Python")
```

Output:

```python
True
True
```

Porównywanie:

```python
print("abc" == "abc")
print("abc" < "abd")
```

Output:

```python
True
True
```

Porównania działają leksykograficznie, czyli podobnie do kolejności słownikowej.

---

## Najczęściej używane metody stringów

### `lower()` i `upper()`

```python
tekst = "Python"
print(tekst.lower())
print(tekst.upper())
```

Output:

```python
python
PYTHON
```

### `strip()`, `lstrip()`, `rstrip()`

```python
tekst = "  Ala  "
print(tekst.strip())
print(tekst.lstrip())
print(tekst.rstrip())
```

Output:

```python
Ala
Ala  
  Ala
```

`strip()` bardzo często przydaje się przy danych od użytkownika.

### `replace()`

```python
tekst = "Ala ma kota"
print(tekst.replace("kota", "psa"))
```

Output:

```python
Ala ma psa
```

### `capitalize()` i `title()`

```python
print("python".capitalize())
print("jan kowalski".title())
```

Output:

```python
Python
Jan Kowalski
```

### `count()`

```python
print("banan".count("a"))
```

Output:

```python
2
```

---

## `split()` i `join()`

`split()` dzieli tekst na listę fragmentów.

```python
tekst = "Ala ma kota"
slowa = tekst.split()
print(slowa)
```

Output:

```python
['Ala', 'ma', 'kota']
```

Co się stało:

- przed metodą miałeś jeden string: `"Ala ma kota"`
- po metodzie masz listę stringów: `['Ala', 'ma', 'kota']`

Czyli:

- wejście: jeden tekst
- wyjście: lista kawałków tekstu

Możesz też podać separator:

```python
csv = "a,b,c"
print(csv.split(","))
```

Output:

```python
['a', 'b', 'c']
```

Tutaj Python nie dzieli po spacjach, tylko po przecinku.

Przed:

```python
"a,b,c"
```

Po:

```python
['a', 'b', 'c']
```

`join()` robi odwrotność: skleja elementy iterowalne w jeden string.

```python
slowa = ["Python", "jest", "fajny"]
wynik = " ".join(slowa)
print(wynik)
```

Output:

```python
Python jest fajny
```

Co się stało:

- przed metodą miałeś listę: `["Python", "jest", "fajny"]`
- separatorem był string `" "`, czyli pojedyncza spacja
- po metodzie dostałeś jeden string: `"Python jest fajny"`

Czyli:

- wejście: lista stringów
- separator: `" "`
- wyjście: jeden połączony string

Drugi przykład:

```python
elementy = ["a", "b", "c"]
print(",".join(elementy))
```

Output:

```python
a,b,c
```

Przed:

```python
["a", "b", "c"]
```

Po:

```python
"a,b,c"
```

To bardzo ważne:

- `split()` działa na stringu i zwraca listę,
- `join()` działa na separatorze-stringu i przyjmuje iterowalne wartości tekstowe.

Najkrótsza intuicja:

- `split()` rozbija jeden tekst na wiele kawałków
- `join()` skleja wiele kawałków w jeden tekst

Typowa pułapka:

```python
liczby = [1, 2, 3]
# print(",".join(liczby))
```

To da błąd, bo `join()` oczekuje stringów, a nie liczb.

Poprawnie:

```python
liczby = ["1", "2", "3"]
print(",".join(liczby))
```

Output:

```python
1,2,3
```

---

## Wyszukiwanie i zamiana tekstu

### `find()`

```python
tekst = "programowanie"
print(tekst.find("ram"))
print(tekst.find("xyz"))
```

Output:

```python
2
-1
```

Gdy nie znajdzie fragmentu, zwraca `-1`.

### `index()`

```python
tekst = "programowanie"
print(tekst.index("ram"))
```

Output:

```python
2
```

Jeśli nie znajdzie fragmentu, rzuci wyjątek.

### `startswith()` i `endswith()`

```python
email = "user@example.com"
print(email.startswith("user"))
print(email.endswith(".com"))
```

Output:

```python
True
True
```

To bardzo czytelne i częste w praktyce.

---

## Sprawdzanie zawartości tekstu

Python ma kilka przydatnych metod:

- `isalpha()`
- `isdigit()`
- `isalnum()`
- `isspace()`

Przykłady:

```python
print("Python".isalpha())
print("123".isdigit())
print("abc123".isalnum())
print("   ".isspace())
```

Output:

```python
True
True
True
True
```

Uwaga:

- `"123".isdigit()` jest `True`, ale to nadal string, nie `int`,
- pusty string zwykle daje `False` dla takich metod.

---

## Formatowanie tekstu

Starsze style:

```python
imie = "Anna"
tekst1 = "Czesc, %s" % imie
tekst2 = "Czesc, {}".format(imie)
```

Dziś najczęściej używa się f-stringów, bo są najczytelniejsze.

---

## Czym są f-stringi

F-string to string poprzedzony literą `f`.

```python
imie = "Anna"
tekst = f"Czesc, {imie}"
```

W nawiasach klamrowych możesz wstawiać:

- zmienne,
- wyrażenia,
- wynik funkcji.

---

## Wyrażenia wewnątrz f-stringów

```python
imie = "Anna"
wiek = 30

print(f"{imie} ma {wiek} lat")
print(f"Za rok bedzie miec {wiek + 1} lat")
print(f"Dlugosc imienia: {len(imie)}")
```

Output:

```python
Anna ma 30 lat
Za rok bedzie miec 31 lat
Dlugosc imienia: 4
```

To ogromna zaleta f-stringów: możesz czytelnie budować komunikat bez ręcznego sklejania.

---

## Format specifiers we f-stringach

F-stringi potrafią więcej niż tylko wstawianie zmiennych.

### Liczby zmiennoprzecinkowe

```python
cena = 12.34567
print(f"{cena:.2f}")
```

Output:

```python
12.35
```

### Wyrównanie

```python
print(f"{'kot':>10}")
print(f"{'kot':<10}")
print(f"{'kot':^10}")
```

Output:

```python
       kot
kot       
   kot    
```

### Dodawanie zer

```python
numer = 7
print(f"{numer:03}")
```

Output:

```python
007
```

### Separator tysięcy

```python
kwota = 1234567
print(f"{kwota:,}")
```

Output:

```python
1,234,567
```

Na początku nie musisz znać wszystkich format specifiers, ale warto wiedzieć, że istnieją.

---

## Kiedy f-string nie jest najlepszym wyborem

F-stringi są świetne, ale nie zawsze są jedyną opcją.

Przykłady:

- gdy budujesz string dynamicznie w pętli z wielu elementów, często lepsze będzie `join()`,
- gdy potrzebujesz bardzo starej kompatybilności, możesz spotkać `.format()`,
- gdy tekst jest szablonem przechowywanym poza kodem, temat robi się szerszy niż zwykły f-string.

Najczęściej jednak w zwykłym kodzie aplikacyjnym f-stringi są najlepszym wyborem.

---

## Częste pułapki początkujących

- mylenie `print()` z tworzeniem stringa,
- zapominanie, że `input()` zawsze zwraca string,
- używanie `+` do składania bardzo wielu fragmentów tekstu,
- oczekiwanie, że metody stringów zmienią oryginał w miejscu,
- brak `strip()` przy danych od użytkownika,
- używanie `find()` bez sprawdzania `-1`,
- mylenie `split()` i `join()`.

---

## Praktyczne przykłady

### Normalizacja imienia

```python
imie = "  aNNa  "
wynik = imie.strip().capitalize()
print(wynik)
```

Output:

```python
Anna
```

### Liczenie słów

```python
tekst = "Python jest bardzo przyjemny"
liczba_slow = len(tekst.split())
print(liczba_slow)
```

Output:

```python
4
```

### Budowanie komunikatu

```python
produkt = "Laptop"
cena = 3499.99
print(f"Produkt: {produkt}, cena: {cena:.2f} PLN")
```

Output:

```python
Produkt: Laptop, cena: 3499.99 PLN
```

### Bezpieczne porównanie po normalizacji

```python
odpowiedz = input("Tak/Nie: ").strip().lower()
if odpowiedz == "tak":
    print("Wybrano tak")
```

---

## Dobre praktyki

- używaj `strip()` przy tekstach od użytkownika,
- używaj f-stringów do czytelnego formatowania,
- pamiętaj, że stringi są niemutowalne,
- wybieraj `join()` do łączenia wielu fragmentów,
- normalizuj dane przed porównaniem, np. `strip().lower()`,
- nie komplikuj prostego kodu tekstowego.

---

## Podsumowanie

Stringi to jeden z fundamentów codziennej pracy w Pythonie.

Warto dobrze rozumieć:

- że string jest sekwencją znaków,
- że jest niemutowalny,
- jak działają podstawowe metody,
- kiedy używać `split()` i `join()`,
- dlaczego f-stringi są standardem nowoczesnego Pythona.

---

## Mini ściąga

```python
tekst = "  Python  "
print(tekst.strip())
print(tekst.lower())
print(tekst.upper())
print(tekst.replace("Py", "My"))
print(tekst.split())
print(", ".join(["a", "b", "c"]))

imie = "Ola"
print(f"Witaj, {imie}")
```

Najważniejsze:

- `str` to tekst,
- string jest niemutowalny,
- działa indeksowanie i slicing,
- `strip`, `split`, `join`, `replace`, `lower` są bardzo ważne,
- f-stringi to najczytelniejsze formatowanie.

---

## Ćwiczenia

1. Utwórz string z imieniem i wypisz jego długość.
2. Pobierz tekst od użytkownika i wypisz go po `strip()`, `lower()` i `upper()`.
3. Sprawdź, czy e-mail kończy się na `.com`.
4. Policz, ile razy litera `"a"` występuje w napisie.
5. Rozdziel zdanie na słowa przez `split()`.
6. Sklej listę słów w jedno zdanie przez `" ".join(...)`.
7. Zbuduj komunikat o produkcie przez f-string.
8. Wypisz liczbę zmiennoprzecinkową z dwoma miejscami po przecinku.
9. Odwróć string przez slicing.
10. Sprawdź, czy napis zawiera tylko cyfry.

---

## Przykładowe rozwiązania

### 1. Długość napisu

```python
imie = "Jan"
print(len(imie))
```

### 2. Normalizacja tekstu

```python
tekst = input("Podaj tekst: ")
print(tekst.strip())
print(tekst.lower())
print(tekst.upper())
```

### 3. Końcówka e-maila

```python
email = "user@example.com"
print(email.endswith(".com"))
```

### 4. Liczenie znaków

```python
print("banan".count("a"))
```

### 5. `split()`

```python
zdanie = "Python jest fajny"
print(zdanie.split())
```

### 6. `join()`

```python
slowa = ["Python", "jest", "fajny"]
print(" ".join(slowa))
```

### 7. F-string

```python
produkt = "Myszka"
cena = 99.9
print(f"{produkt} kosztuje {cena:.2f} PLN")
```

### 8. Dwa miejsca po przecinku

```python
liczba = 12.3456
print(f"{liczba:.2f}")
```

### 9. Odwracanie stringa

```python
tekst = "Python"
print(tekst[::-1])
```

### 10. Cyfry

```python
tekst = "12345"
print(tekst.isdigit())
```
