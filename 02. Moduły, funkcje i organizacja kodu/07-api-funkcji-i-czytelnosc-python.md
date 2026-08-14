# Projektowanie API funkcji i czytelność w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co projektować API funkcji](#po-co-projektować-api-funkcji)
3. [Dobra nazwa funkcji](#dobra-nazwa-funkcji)
4. [Czytelne argumenty](#czytelne-argumenty)
5. [Czytelna wartość zwracana](#czytelna-wartość-zwracana)
6. [Mało niespodzianek](#mało-niespodzianek)
7. [Funkcje czyste vs efekty uboczne](#funkcje-czyste-vs-efekty-uboczne)
8. [Czytelność ponad spryt](#czytelność-ponad-spryt)
9. [Złe API i jak je poprawiać](#złe-api-i-jak-je-poprawiać)
10. [Kiedy nie używać `**kwargs`](#kiedy-nie-używać-kwargs)
11. [Typowe pułapki początkujących](#typowe-pułapki-początkujących)
12. [Praktyczne przykłady](#praktyczne-przykłady)
13. [Dobre praktyki](#dobre-praktyki)
14. [Podsumowanie](#podsumowanie)
15. [Mini ściąga](#mini-ściąga)
16. [Ćwiczenia](#ćwiczenia)
17. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Dobra funkcja to nie tylko taka, która działa.

To także taka, którą:

- łatwo wywołać,
- łatwo zrozumieć,
- trudno użyć źle,
- łatwo rozwijać dalej.

To właśnie jest jakość API funkcji.

API funkcji to po prostu to, jak inni ludzie i inne fragmenty kodu wchodzą z nią w interakcję.

---

## Po co projektować API funkcji

Bo funkcja jest interfejsem dla:

- Ciebie z przyszłości,
- innych plików,
- innych ludzi,
- testów.

Jeśli API jest mętne, to nawet poprawna logika wewnątrz będzie męczyć użytkownika funkcji.

---

## Dobra nazwa funkcji

Nazwa powinna sugerować działanie.

Dobre przykłady:

- `save_report`
- `normalize_email`
- `calculate_total`
- `is_adult`

Słabe:

- `do_it`
- `fun1`
- `handle`

Nazwa powinna odpowiadać na pytanie:

"co ta funkcja robi?"

Nie:

"jak bardzo autor nie chciał jej nazwać."

---

## Czytelne argumenty

Lepiej:

```python
def create_user(name, email, active=True):
    ...
```

niż:

```python
def create_user(a, b, c=True):
    ...
```

Argumenty są częścią API i mocno wpływają na wygodę użycia.

Dobre nazwy parametrów zmniejszają potrzebę zaglądania do wnętrza funkcji.

---

## Czytelna wartość zwracana

To bardzo ważny element API.

Nie wystarczy, że funkcja "coś zwraca". Powinno być jasne:

- co zwraca,
- kiedy zwraca `None`,
- czy zwraca pojedynczą wartość, krotkę, słownik, listę,
- czy może rzucić wyjątek zamiast czegoś zwrócić.

Przykład czytelny:

```python
def parse_int(text):
    try:
        return int(text)
    except ValueError:
        return None
```

```python
print(parse_int("12"))
print(parse_int("abc"))
```

Output:

```python
12
None
```

Przykład mniej czytelny:

```python
def parse(text):
    ...
```

gdy nie wiadomo, co ma wyjść i w jakiej formie.

---

## Mało niespodzianek

Funkcja nie powinna robić ukrytych rzeczy bez wyraźnej potrzeby.

Jeśli funkcja:

- zapisuje plik,
- wysyła request,
- modyfikuje globalny stan,

to powinno to być widoczne z nazwy albo kontekstu.

Zła niespodzianka:

```python
def policz_wynik(dane):
    wynik = sum(dane)
    print("zapisuje dane")
    return wynik
```

Jeśli nazwa sugeruje tylko obliczanie, dodatkowe działanie jest ukrytym efektem ubocznym.

---

## Funkcje czyste vs efekty uboczne

Funkcja czysta:

- dla tych samych danych wejściowych daje ten sam wynik,
- nie zmienia zewnętrznego świata.

Przykład:

```python
def dodaj(a, b):
    return a + b
```

```python
print(dodaj(2, 3))
```

Output:

```python
5
```

Funkcja z efektem ubocznym:

```python
def zapisz_log(tekst):
    print(tekst)
```

```python
zapisz_log("start")
```

Output:

```python
start
```

Oba typy są potrzebne, ale warto wiedzieć, z którym masz do czynienia.

W dobrze zaprojektowanym kodzie efekt uboczny nie powinien być ukryty przypadkiem.

---

## Czytelność ponad spryt

Kod nie ma imponować sprytnością. Ma być czytelny.

Lepiej napisać prostą, jawną funkcję niż bardzo elastyczny, ale mało zrozumiały potwór na `*args`, `**kwargs` i wielu ukrytych ścieżkach.

Jeśli funkcja wymaga tłumaczenia, jak ją wywołać, to często znak, że jej API jest za mało oczywiste.

---

## Złe API i jak je poprawiać

Słabe API:

```python
def process(a, b, c, d=None, x=False, **kwargs):
    ...
```

Tu od razu nie wiadomo:

- co robi funkcja,
- czym są argumenty,
- które są naprawdę ważne,
- kiedy używać `kwargs`.

Lepsze API:

```python
def create_user(name, email, active=True):
    ...
```

Poprawa API często polega na:

- zmianie nazwy,
- zmianie nazw argumentów,
- zmniejszeniu liczby odpowiedzialności,
- zastąpieniu zbyt szerokiego `**kwargs` jawnymi parametrami,
- rozbiciu jednej funkcji na kilka mniejszych.

---

## Kiedy nie używać `**kwargs`

`**kwargs` jest wygodne, ale bywa nadużywane.

Jeśli wiesz, że funkcja potrzebuje dokładnie:

- `name`,
- `email`,
- `active`,

to zwykle lepiej napisać:

```python
def create_user(name, email, active=True):
    ...
```

niż:

```python
def create_user(**kwargs):
    ...
```

Jawne API jest:

- czytelniejsze,
- łatwiejsze do użycia,
- łatwiejsze do testowania,
- mniej zaskakujące.

---

## Jak myśleć o kontrakcie funkcji

Każda dobra funkcja ma kontrakt, nawet jeśli nie zapisujesz go formalnie.

Kontrakt odpowiada na pytania:

- co funkcja przyjmuje,
- co funkcja zwraca,
- jakie są przypadki brzegowe,
- czy może rzucić wyjątek,
- czy ma efekt uboczny.

Przykład:

```python
def bezpieczne_dzielenie(a, b):
    if b == 0:
        return None
    return a / b

print(bezpieczne_dzielenie(10, 2))
print(bezpieczne_dzielenie(10, 0))
```

Output:

```python
5.0
None
```

Tutaj kontrakt jest dość jasny:

- przy zwykłych danych dostajesz liczbę,
- przy dzieleniu przez zero dostajesz `None`.

---

## Typowe pułapki początkujących

- zbyt ogólne nazwy,
- ukrywanie wszystkiego za `**kwargs`,
- funkcje robiące pięć rzeczy naraz,
- mieszanie zwracania danych z wypisywaniem i zapisywaniem stanu,
- nazwy argumentów typu `a`, `b`, `x`, `data2`,
- zwracanie różnych typów wyników bez jasnego kontraktu.

---

## Praktyczne przykłady

### Lepsza nazwa

```python
def normalize_email(email):
    return email.strip().lower()
```

```python
print(normalize_email("  JAN@EXAMPLE.COM "))
```

Output:

```python
jan@example.com
```

### Jawne argumenty

```python
def create_user(name, email, active=True):
    return {"name": name, "email": email, "active": active}
```

```python
print(create_user("Jan", "jan@example.com"))
```

Output:

```python
{'name': 'Jan', 'email': 'jan@example.com', 'active': True}
```

### Funkcja czysta

```python
def policz_brutto(netto, vat):
    return netto * (1 + vat)
```

```python
print(policz_brutto(100, 0.23))
```

Output:

```python
123.0
```

### Funkcja z ukrytym problemem

```python
def handle(data):
    ...
```

Taka nazwa prawie nic nie mówi.

---

## Dobre praktyki

- nazywaj funkcje czasownikami lub pytaniami,
- trzymaj funkcje możliwie małe,
- projektuj argumenty tak, by były jasne,
- projektuj zwracaną wartość tak, by była przewidywalna,
- nie ukrywaj efektów ubocznych,
- preferuj czytelność nad nadmierną elastyczność.

---

## Podsumowanie

Dobre API funkcji sprawia, że funkcja jest nie tylko poprawna, ale też wygodna w użyciu.

Najważniejsze rzeczy do zapamiętania:

- dobra nazwa dużo tłumaczy,
- argumenty są częścią interfejsu,
- zwracana wartość powinna być przewidywalna,
- funkcja nie powinna zaskakiwać ukrytymi efektami ubocznymi.

---

## Podsumowanie

Dobre API funkcji to ogromna część jakości kodu.

Im wcześniej wyrobisz ten nawyk, tym łatwiej będzie Ci pisać kod, który nie tylko działa, ale też dobrze się rozwija.

Najważniejsze pytania przy projektowaniu funkcji:

- jak się nazywa,
- jak się ją wywołuje,
- co zwraca,
- czy robi coś ukrytego,
- czy da się użyć jej źle zbyt łatwo.

---

## Mini ściąga

```python
def normalize_email(email):
    return email.strip().lower()

def is_even(n):
    return n % 2 == 0

def create_user(name, email, active=True):
    ...
```

---

## Ćwiczenia

1. Popraw trzy źle nazwane funkcje.
2. Zastąp `**kwargs` jawnymi argumentami tam, gdzie to poprawia czytelność.
3. Rozbij długą funkcję na trzy mniejsze.
4. Weź funkcję z niejasnym zwracanym wynikiem i zaprojektuj jej lepszy kontrakt.
5. Weź funkcję z ukrytym efektem ubocznym i popraw jej API albo nazwę.

---

## Przykładowe rozwiązania

### 1. Lepsza nazwa

```python
def policz_sume(a, b):
    return a + b
```

zamiast:

```python
def fun1(a, b):
    return a + b
```

### 2. Jawne argumenty

```python
def create_user(name, email, active=True):
    return {"name": name, "email": email, "active": active}
```

### 3. Lepszy kontrakt

```python
def parse_int(text):
    try:
        return int(text)
    except ValueError:
        return None
```

---

## Antywzorce i pułapki z życia

### Antywzorzec 1: funkcja robi wszystko

```python
def handle_user(data):
    ...
```

Jeśli z nazwy nie wiadomo, czy funkcja:

- waliduje,
- zapisuje,
- liczy,
- wypisuje,

to API jest zbyt mgliste.

### Antywzorzec 2: różne typy wyników bez jasnej zasady

```python
def parse(value):
    if value == "":
        return []
    if value.isdigit():
        return int(value)
    return False
```

Taka funkcja zwraca bardzo różne rzeczy i trudno ją poprawnie używać.

### Antywzorzec 3: nazwa nie zdradza efektu ubocznego

```python
def policz_raport(dane):
    ...
    zapis_do_pliku(...)
```

Jeśli nazwa sugeruje tylko obliczanie, zapis do pliku jest niespodzianką.

---

## Mini case study

Załóżmy, że chcesz stworzyć funkcję tworzącą użytkownika.

Słaba wersja:

```python
def do_it(a, b, c=False, **kwargs):
    ...
```

Lepsza wersja:

```python
def create_user(name, email, active=False):
    return {"name": name, "email": email, "active": active}
```

Co się poprawiło:

- nazwa mówi, co się dzieje,
- argumenty są czytelne,
- wynik ma przewidywalny kształt,
- łatwiej to testować i wywoływać.

To właśnie jest realna poprawa API, a nie tylko ładniejszy zapis.

---

## Mini projekt po rozdziale

Weź 5 własnych funkcji z ćwiczeń i zrób dla każdej krótki przegląd:

- czy nazwa mówi, co robi,
- czy argumenty są czytelne,
- czy wynik jest przewidywalny,
- czy funkcja ma ukryte efekty uboczne,
- czy da się ją rozbić na mniejsze części.

Potem popraw przynajmniej 2 z nich.
