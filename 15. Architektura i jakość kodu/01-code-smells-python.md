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
10. [Przykład mentalny](#przykład-mentalny)
11. [Typowe błędy początkujących](#typowe-błędy-początkujących)
12. [Praktyczna ściąga](#praktyczna-ściąga)
13. [Ćwiczenia](#ćwiczenia)
14. [Najważniejsze do zapamiętania](#najważniejsze-do-zapamiętania)

---

## Wprowadzenie

Code smell to sygnał ostrzegawczy, że w kodzie może być problem projektowy albo utrzymaniowy.

To nie zawsze jest błąd wykonania.

Ale bardzo często jest zapowiedzią przyszłych kłopotów.

---

## Czym są code smells

To wzorce, które sugerują:

- nadmierną złożoność,
- zły podział odpowiedzialności,
- niską czytelność,
- trudność w rozwijaniu kodu,
- rosnący koszt zmian.

Bardzo ważne:

code smell to heurystyka, a nie automatyczny wyrok.

---

## Po co je rozpoznawać

Bo szybkie zauważenie takich sygnałów pomaga:

- refaktoryzować wcześniej,
- obniżać koszt utrzymania,
- nie dopuszczać do narastania chaosu,
- łatwiej planować zmiany.

To trochę jak wczesne wykrywanie długu technicznego.

---

## Długa funkcja

Jeśli jedna funkcja ma:

- wiele kroków,
- kilka poziomów odpowiedzialności,
- długie warunki,
- dużo side effectów,

to zwykle jest kandydatem do rozbicia.

Długa funkcja nie zawsze jest zła sama w sobie, ale bardzo często ukrywa wiele problemów naraz.

---

## Duplikacja

Jeśli ten sam kod albo bardzo podobna logika pojawiają się w wielu miejscach, to sygnał ostrzegawczy.

Duplikacja zwiększa:

- koszt zmian,
- ryzyko niespójności,
- ryzyko że poprawisz jedno miejsce, a zapomnisz o drugim.

---

## Zbyt duża klasa

Klasa, która wie i robi za dużo, często jest trudna do utrzymania.

To klasyczny zapach projektu.

Często objawia się klasami typu:

- `AppManager`,
- `UserServiceManager`,
- `SystemController`.

Nazwy już same często sugerują zbyt szeroką odpowiedzialność.

---

## Ukryte efekty uboczne

Funkcja o nazwie sugerującej „obliczenie”, która:

- zapisuje do pliku,
- modyfikuje globalny stan,
- wysyła request,
- robi zapis do bazy,

jest niebezpieczna dla czytelności i przewidywalności.

Takie rzeczy bardzo utrudniają testy i debugowanie.

---

## Chaotyczne nazwy

Nazwy typu:

- `data2`,
- `handle`,
- `process`,
- `tmp`,
- `manager`,

często sygnalizują, że autor sam nie nazwał jasno odpowiedzialności.

Zła nazwa to często sygnał głębszego problemu projektowego.

---

## Feature envy i mieszanie odpowiedzialności

Jeśli funkcja albo klasa zbyt mocno interesuje się danymi innego obiektu albo logika jest rozlana po złych miejscach, to często znak słabej architektury.

To zwykle oznacza, że odpowiedzialności są źle podzielone.

---

## Przykład mentalny

Masz endpoint, który:

- waliduje wejście,
- sprawdza uprawnienia,
- pobiera dane z bazy,
- liczy rabat,
- wysyła mail,
- buduje odpowiedź HTTP.

To bardzo prawdopodobny code smell.

Kod działa, ale odpowiedzialności są sklejone w jedno miejsce.

---

## Typowe błędy początkujących

- ignorowanie takich sygnałów, bo "przecież działa",
- próba naprawy wszystkiego naraz,
- kosmetyczna zmiana nazw bez poprawy struktury,
- traktowanie code smells jak listy zakazanych konstrukcji zamiast heurystyk.

---

## Praktyczna ściąga

### Najczęstsze sygnały

- długa funkcja,
- duplikacja,
- zbyt duża klasa,
- ukryte efekty uboczne,
- mieszanie odpowiedzialności.

### Dobra reakcja

Nie panikuj.

Zacznij od małej refaktoryzacji i popraw najważniejszy problem.

---

## Ćwiczenia

1. Wskaż przykład długiej funkcji.
2. Znajdź przykład duplikacji.
3. Wskaż klasę, która może robić za dużo.
4. Znajdź przykład ukrytego efektu ubocznego.
5. Wyjaśnij własnymi słowami, czemu code smell nie zawsze oznacza natychmiastowy błąd.

---

## Najważniejsze do zapamiętania

- Code smell to sygnał ostrzegawczy, nie automatyczny wyrok.
- Najczęściej mówi o trudności utrzymania, testowania albo rozwijania kodu.
- Warto je rozpoznawać wcześnie.
- Najlepsza reakcja to małe, sensowne refaktoryzacje.
