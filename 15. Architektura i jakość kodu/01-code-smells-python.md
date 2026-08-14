# Code smells w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym są code smells](#czym-są-code-smells)
3. [Po co je rozpoznawać](#po-co-je-rozpoznawać)
4. [Długa funkcja](#długa-funkcja)
5. [Duplikacja](#duplikacja)
6. [Zbyt duża klasa](#zbyt-duża-klasa)
7. [Ukryte efekty uboczne](#ukryte-efekty-uboczne)
8. [Chaotyczne nazwy](#chaotyczne-nazwy)
9. [Feature envy i mieszanie odpowiedzialności](#feature-envy-i-mieszanie-odpowiedzialności)
10. [Typowe błędy początkujących](#typowe-błędy-początkujących)
11. [Praktyczne przykłady](#praktyczne-przykłady)
12. [Dobre praktyki](#dobre-praktyki)
13. [Podsumowanie](#podsumowanie)
14. [Mini ściąga](#mini-ściąga)
15. [Ćwiczenia](#ćwiczenia)
16. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Code smell to sygnał ostrzegawczy, że w kodzie może być problem projektowy lub utrzymaniowy.

To nie zawsze jest błąd wykonania, ale często zapowiedź przyszłych kłopotów.

---

## Czym są code smells

To wzorce, które sugerują:

- nadmierną złożoność,
- zły podział odpowiedzialności,
- niską czytelność,
- trudność w rozwijaniu kodu.

---

## Po co je rozpoznawać

Bo szybkie zauważenie takich sygnałów pomaga:

- refaktoryzować wcześniej,
- obniżać koszt utrzymania,
- nie dopuszczać do narastania chaosu.

---

## Długa funkcja

Jeśli jedna funkcja ma:

- wiele kroków,
- kilka poziomów odpowiedzialności,
- długie warunki,
- dużo side effectów,

to zwykle jest kandydatem do rozbicia.

---

## Duplikacja

Jeśli ten sam kod lub bardzo podobna logika pojawiają się w wielu miejscach, to sygnał ostrzegawczy.

Duplikacja zwiększa koszt zmian i ryzyko niespójności.

---

## Zbyt duża klasa

Klasa, która wie i robi za dużo, często jest trudna do utrzymania.

To klasyczny zapach projektu.

---

## Ukryte efekty uboczne

Funkcja o nazwie sugerującej "obliczenie", która:

- zapisuje do pliku,
- modyfikuje globalny stan,
- wysyła request,

jest niebezpieczna dla czytelności i przewidywalności.

---

## Chaotyczne nazwy

Nazwy typu:

- `data2`,
- `handle`,
- `process`,
- `tmp`,

często sygnalizują, że autor sam nie nazwał jasno odpowiedzialności.

---

## Feature envy i mieszanie odpowiedzialności

Jeśli funkcja lub klasa zbyt mocno interesuje się danymi innego obiektu albo logika jest rozlana po złych miejscach, to często znak słabej architektury.

---

## Typowe błędy początkujących

- ignorowanie takich sygnałów, bo "przecież działa",
- próba naprawy wszystkiego naraz,
- kosmetyczna zmiana nazw bez poprawy struktury,
- traktowanie code smells jak listy zakazanych konstrukcji zamiast heurystyk.

---

## Praktyczne przykłady

### Long method

Funkcja 150-liniowa obsługująca cały proces biznesowy.

### Duplikacja

Ta sama walidacja emaila skopiowana do pięciu miejsc.

### God object

Klasa `AppManager`, która robi wszystko.

---

## Dobre praktyki

- ucz się rozpoznawać zapachy wcześnie,
- reaguj małymi refaktoryzacjami,
- nie przesadzaj z polowaniem na ideał,
- traktuj code smells jako sygnały do myślenia.

---

## Podsumowanie

Code smells pomagają widzieć problemy wcześniej, zanim staną się drogimi awariami utrzymaniowymi.

To bardzo praktyczna umiejętność profesjonalna.

---

## Mini ściąga

Najważniejsze sygnały:

- długa funkcja,
- duplikacja,
- zbyt duża klasa,
- ukryte side effecty,
- słabe nazewnictwo.

---

## Ćwiczenia

1. Podaj przykład długiej funkcji jako code smell.
2. Wyjaśnij, czemu duplikacja boli.
3. Podaj przykład ukrytego efektu ubocznego.
4. Wyjaśnij, czemu zła nazwa też jest sygnałem problemu.
5. Wyjaśnij, czemu code smell nie zawsze oznacza bug.

---

## Przykładowe rozwiązania

### 1. Długa funkcja

Na przykład funkcja obsługująca cały checkout, płatność i mail w jednym miejscu.

### 2. Duplikacja

Bo trzeba poprawiać tę samą logikę w wielu miejscach i łatwo coś pominąć.

### 3. Side effect

Funkcja `calculate_total`, która przy okazji zapisuje coś do bazy.

### 4. Zła nazwa

Bo utrudnia zrozumienie odpowiedzialności kodu.

### 5. Nie zawsze bug

Bo to raczej sygnał projektowy, że kod może być trudniejszy do dalszego utrzymania.
