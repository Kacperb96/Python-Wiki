# Moduły i importy w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest moduł](#czym-jest-moduł)
3. [Po co dzielić kod na moduły](#po-co-dzielić-kod-na-moduły)
4. [Podstawowe formy importu](#podstawowe-formy-importu)
5. [Import całego modułu vs import nazw](#import-całego-modułu-vs-import-nazw)
6. [Aliasowanie przez `as`](#aliasowanie-przez-as)
7. [Jak Python znajduje moduły](#jak-python-znajduje-moduły)
8. [Efekty uboczne przy imporcie](#efekty-uboczne-przy-imporcie)
9. [Cykliczne importy i skąd biorą się problemy](#cykliczne-importy-i-skąd-biorą-się-problemy)
10. [Importy lokalne wewnątrz funkcji](#importy-lokalne-wewnątrz-funkcji)
11. [Kiedy `import *` jest złym pomysłem](#kiedy-import--jest-złym-pomysłem)
12. [Jak myśleć o podziale modułów](#jak-myśleć-o-podziale-modułów)
13. [Typowe pułapki początkujących](#typowe-pułapki-początkujących)
14. [Praktyczne przykłady](#praktyczne-przykłady)
15. [Dobre praktyki](#dobre-praktyki)
16. [Podsumowanie](#podsumowanie)
17. [Mini ściąga](#mini-ściąga)
18. [Ćwiczenia](#ćwiczenia)
19. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Moduły i importy to fundament organizacji kodu w Pythonie.

Jeśli dobrze je rozumiesz, potrafisz:

- dzielić program na mniejsze pliki,
- używać kodu z innych plików,
- unikać bałaganu,
- budować większe projekty bez chaosu.

Na początku temat wydaje się prosty: "mam plik i go importuję". W praktyce właśnie tu zaczyna się realna organizacja projektu.

---

## Czym jest moduł

Moduł to po prostu plik `.py` z kodem Pythona.

Przykład:

plik `math_utils.py`:

```python
def dodaj(a, b):
    return a + b
```

W innym pliku:

```python
import math_utils
print(math_utils.dodaj(2, 3))
```

Output:

```python
5
```

Jeden plik to jeden moduł. Nawet jeśli nie myślisz o tym świadomie, pisząc skrypt `.py` już tworzysz moduł.

---

## Po co dzielić kod na moduły

Bo to pomaga:

- rozdzielać odpowiedzialności,
- łatwiej odnajdywać kod,
- ponownie używać funkcji,
- testować mniejsze części osobno,
- ograniczać chaos.

Lepszy jest projekt z plikami:

- `validators.py`
- `users.py`
- `main.py`

niż jeden gigantyczny `app.py` ze wszystkim.

Moduł nie ma być tylko "innym plikiem". Powinien mieć sensowną odpowiedzialność.

---

## Podstawowe formy importu

```python
import math
from math import sqrt
from math import sqrt as pierwiastek
```

Każda forma ma swoje miejsce.

### `import module`

```python
import math
print(math.sqrt(9))
```

Output:

```python
3.0
```

### `from module import name`

```python
from math import sqrt
print(sqrt(9))
```

Output:

```python
3.0
```

### Alias

```python
from math import sqrt as pierwiastek
print(pierwiastek(9))
```

Output:

```python
3.0
```

---

## Import całego modułu vs import nazw

Import całego modułu:

```python
import math
print(math.sqrt(9))
```

Import konkretnej nazwy:

```python
from math import sqrt
print(sqrt(9))
```

Import całego modułu bywa czytelniejszy, bo od razu widać, skąd pochodzi dana funkcja.

Import konkretnych nazw bywa krótszy, ale łatwiej wtedy zgubić źródło pochodzenia funkcji i łatwiej o konflikt nazw.

Na początku dobra intuicja jest taka:

- jeśli moduł jest mały i używasz jednej rzeczy, `from ... import ...` jest okej,
- jeśli chcesz zachować maksymalną czytelność pochodzenia, `import module` bywa lepsze.

---

## Aliasowanie przez `as`

```python
import math as m
from math import sqrt as pierwiastek
```

Alias ma sens, gdy:

- nazwa jest długa,
- istnieje powszechny standard,
- chcesz uniknąć konfliktu nazw.

Nie warto jednak robić aliasów tylko dla sprytu.

Dobry alias poprawia czytelność. Zły alias tylko ją psuje.

---

## Jak Python znajduje moduły

Najprościej:

- sprawdza bieżący projekt,
- sprawdza standardową bibliotekę,
- sprawdza zainstalowane pakiety.

Na początku najważniejsze jest zrozumienie, że plik musi być w miejscu, z którego Python może go zaimportować.

Jeśli struktura projektu jest chaotyczna, importy też szybko staną się chaotyczne.

---

## Efekty uboczne przy imporcie

Kod na najwyższym poziomie pliku wykonuje się przy imporcie.

Przykład:

```python
print("to wykona sie przy imporcie")
```

To oznacza, że moduł nie powinien przy imporcie:

- odpalać programu,
- pytać użytkownika o dane,
- robić ciężkiej logiki testowej,
- modyfikować globalnego stanu bez wyraźnej potrzeby.

Od tego jest `if __name__ == "__main__"`.

To jeden z najważniejszych praktycznych powodów, dla których w ogóle używa się tego idiomu.

---

## Cykliczne importy i skąd biorą się problemy

Cykliczny import pojawia się wtedy, gdy:

- moduł `a` importuje `b`,
- a moduł `b` importuje `a`.

Przykład myślowy:

```python
# a.py
from b import func_b

# b.py
from a import func_a
```

To często prowadzi do błędów albo trudnych do zrozumienia problemów inicjalizacji modułów.

Najczęściej oznacza to, że:

- odpowiedzialności są źle podzielone,
- wspólną logikę trzeba wynieść do trzeciego modułu.

To nie zawsze jest błąd składniowy. Czasem projekt "prawie działa", ale importy zaczynają się zapętlać koncepcyjnie.

---

## Importy lokalne wewnątrz funkcji

Czasem zobaczysz importy wewnątrz funkcji:

```python
def policz():
    import math
    return math.sqrt(9)
```

Na co dzień lepiej trzymać importy na górze pliku.

Import lokalny może mieć sens, gdy:

- chcesz uniknąć cyklicznego importu,
- moduł jest potrzebny tylko w rzadkiej ścieżce wykonania,
- chcesz ograniczyć koszt ładowania.

Ale nie powinno to być domyślne rozwiązanie dla zwykłego kodu.

---

## Kiedy `import *` jest złym pomysłem

Zły przykład:

```python
from math import *
```

Dlaczego to jest zwykle zły pomysł:

- nie widać, jakie nazwy trafiają do przestrzeni nazw,
- łatwiej o konflikt nazw,
- trudniej czytać kod,
- trudniej szukać źródła funkcji.

W normalnym kodzie aplikacyjnym lepiej tego unikać.

---

## Jak myśleć o podziale modułów

Dobry moduł zwykle:

- robi jedną grupę rzeczy,
- ma nazwę opisującą odpowiedzialność,
- nie miesza logiki biznesowej z uruchamianiem programu,
- nie zawiera przypadkowych funkcji tylko dlatego, że "gdzieś trzeba było je wrzucić".

Przykłady sensownych modułów:

- `validators.py`
- `storage.py`
- `text_utils.py`
- `users.py`

Przykłady słabszych nazw:

- `helpers.py`
- `utils2.py`
- `misc.py`

Takie nazwy zwykle szybko stają się workiem na wszystko.

---

## Typowe pułapki początkujących

- wrzucanie całej logiki do jednego pliku,
- chaotyczne `from ... import *`,
- brak rozdziału między logiką a kodem startowym,
- zaskoczenie, że import wykonuje kod z pliku,
- mylenie problemu struktury projektu z "błędem importu",
- dokładanie funkcji do przypadkowego modułu bez myślenia o odpowiedzialności.

---

## Praktyczne przykłady

### Moduł z funkcjami

`math_utils.py`

```python
def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b
```

`main.py`

```python
import math_utils

print(math_utils.dodaj(2, 3))
```

### Moduł z normalizacją e-maila

`text_utils.py`

```python
def normalizuj_email(email):
    return email.strip().lower()
```

`app.py`

```python
from text_utils import normalizuj_email

print(normalizuj_email("  TEST@MAIL.COM "))
```

### Zły podział

`helpers.py`

```python
def normalizuj_email(email):
    ...

def policz_vat(cena):
    ...

def odpal_program():
    ...
```

To zwykle znak, że moduł nie ma jednej odpowiedzialności.

---

## Dobre praktyki

- dziel kod na moduły według odpowiedzialności,
- unikaj `import *`,
- preferuj czytelne importy,
- trzymaj logikę programu oddzielnie od kodu startowego,
- pamiętaj, że import uruchamia kod na najwyższym poziomie pliku,
- traktuj problemy z importami jako sygnał do poprawy struktury projektu, a nie tylko do łatania składni.

---

## Podsumowanie

Moduły i importy to podstawa większego kodu.

Jeśli je dobrze rozumiesz, dużo łatwiej przejść od małych skryptów do prawdziwych projektów.

Najważniejsze nie jest samo `import`, tylko to, czy podział na pliki ma sens architektoniczny.

---

## Mini ściąga

```python
import math
from math import sqrt
from math import sqrt as pierwiastek
```

Najważniejsze:

- moduł to plik `.py`,
- import pozwala użyć kodu z innego pliku,
- kod na najwyższym poziomie modułu wykona się przy imporcie,
- `import *` zwykle jest złym pomysłem,
- cykliczne importy zwykle sygnalizują zły podział odpowiedzialności.

---

## Ćwiczenia

1. Utwórz `math_utils.py` z dwiema funkcjami.
2. Zaimportuj go w `main.py`.
3. Utwórz `text_utils.py` z funkcją `normalizuj_email`.
4. Sprawdź, co wykona się przy imporcie modułu.
5. Napisz dwa moduły, które mają zły podział odpowiedzialności, a potem rozbij je lepiej.
6. Pokaż przykład, kiedy import lokalny wewnątrz funkcji może mieć sens.

---

## Przykładowe rozwiązania

### 1. `math_utils.py`

```python
def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b
```

### 2. `main.py`

```python
import math_utils

print(math_utils.dodaj(2, 3))
```

### 3. `text_utils.py`

```python
def normalizuj_email(email):
    return email.strip().lower()
```

### 4. Import

Kod na najwyższym poziomie pliku wykona się automatycznie przy imporcie.

### 5. Lepszy podział

Wyodrębnij np.:

- `text_utils.py`
- `billing.py`
- `main.py`

zamiast jednego worka `helpers.py`.

---

## Antywzorce i pułapki z życia

### Antywzorzec 1: moduł-worek

Plik typu:

```text
helpers.py
```

do którego trafia wszystko, czego nie wiadomo gdzie dać, prawie zawsze z czasem staje się źródłem chaosu.

### Antywzorzec 2: logika programu uruchamiana przy imporcie

```python
print("Start programu")
main()
```

na najwyższym poziomie pliku oznacza, że zwykły import może uruchomić program.

### Antywzorzec 3: łatanie złej struktury lokalnymi importami wszędzie

Import lokalny czasem ma sens, ale jeśli pojawia się masowo, to często znak, że problem leży głębiej w podziale modułów.

---

## Mini case study

Masz prosty kalkulator zapisany początkowo w jednym pliku:

```text
calculator.py
```

Z czasem dodajesz:

- walidację,
- parsowanie danych,
- menu użytkownika,
- operacje matematyczne.

Dobry moment na podział:

- `operations.py` dla logiki obliczeń,
- `validators.py` dla sprawdzania danych,
- `main.py` dla uruchamiania programu.

Jeśli zamiast tego dalej doklejasz wszystko do jednego pliku, to importy nie są problemem samym w sobie. Problemem jest brak sensownego rozdziału odpowiedzialności.

---

## Mini projekt po rozdziale

Weź prosty skrypt jednoplikiowy i rozbij go na:

- `main.py`,
- `text_utils.py`,
- `validators.py`,
- `math_utils.py`.

Wymagania:

- żadna logika programu nie odpala się przy samym imporcie,
- importy są czytelne,
- każdy moduł ma jedną główną odpowiedzialność.
