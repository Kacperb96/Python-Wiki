# `if __name__ == "__main__"` w Pythonie

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Po co istnieje `__name__`](#po-co-istnieje-__name__)
3. [Co oznacza warunek `if __name__ == "__main__"`](#co-oznacza-warunek-if-__name__--__main__)
4. [Skrypt a moduł importowany](#skrypt-a-moduł-importowany)
5. [Typowe zastosowania](#typowe-zastosowania)
6. [Dlaczego to ważne zawodowo](#dlaczego-to-ważne-zawodowo)
7. [Jak łączyć to z `main()`](#jak-łączyć-to-z-main)
8. [Kod testowy i demo modułu](#kod-testowy-i-demo-modułu)
9. [Typowe pułapki początkujących](#typowe-pułapki-początkujących)
10. [Praktyczne przykłady](#praktyczne-przykłady)
11. [Dobre praktyki](#dobre-praktyki)
12. [Podsumowanie](#podsumowanie)
13. [Mini ściąga](#mini-ściąga)
14. [Ćwiczenia](#ćwiczenia)
15. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

`if __name__ == "__main__"` to bardzo ważny idiom Pythona.

Pozwala odróżnić:

- uruchomienie pliku jako programu,
- import pliku jako modułu.

To podstawa czystego oddzielenia definicji funkcji od kodu startowego.

---

## Po co istnieje `__name__`

Python ustawia specjalną zmienną `__name__`.

Jej wartość zależy od tego, jak plik jest używany.

- przy bezpośrednim uruchomieniu pliku: `__name__ == "__main__"`
- przy imporcie: `__name__` zwykle równa się nazwie modułu

---

## Co oznacza warunek `if __name__ == "__main__"`

To warunek:

"wykonaj ten kod tylko wtedy, gdy plik jest uruchamiany bezpośrednio".

Przykład:

```python
def hello():
    print("czesc")

if __name__ == "__main__":
    hello()
```

Przy bezpośrednim uruchomieniu pliku output będzie:

```python
czesc
```

---

## Skrypt a moduł importowany

Jeśli uruchomisz plik bezpośrednio:

```bash
python hello.py
```

blok pod `if __name__ == "__main__"` się wykona.

Jeśli zrobisz:

```python
import hello
```

to definicje funkcji będą dostępne, ale kod z tego bloku nie uruchomi się automatycznie.

---

## Typowe zastosowania

Najczęściej:

- punkt wejścia programu,
- ręczny test modułu,
- demo działania,
- wywołanie funkcji `main()`.

Najczęstszy wzorzec:

```python
def main():
    print("start programu")

if __name__ == "__main__":
    main()
```

Przy bezpośrednim uruchomieniu pliku output będzie:

```python
start programu
```

---

## Dlaczego to ważne zawodowo

Bo kod:

- da się bezpiecznie importować,
- nie ma niechcianych efektów ubocznych,
- jest łatwiejszy do testowania,
- ma czytelny punkt wejścia.

To bardzo ważne w większych projektach i narzędziach CLI.

---

## Jak łączyć to z `main()`

Najczytelniejszy wzorzec wygląda zwykle tak:

```python
def main():
    print("program startuje")

if __name__ == "__main__":
    main()
```

To daje:

- osobną funkcję z logiką startową,
- prosty punkt wejścia,
- możliwość importowania modułu bez odpalenia programu.

---

## Kod testowy i demo modułu

Czasem chcesz mieć w module małe demo albo ręczny test.

```python
def dodaj(a, b):
    return a + b

if __name__ == "__main__":
    print(dodaj(2, 3))
```

Output:

```python
5
```

To dobre miejsce na prosty test ręczny, ale nie na rozbudowane testy automatyczne.

---

## Typowe pułapki początkujących

- trzymanie całego programu na poziomie globalnym pliku,
- wykonywanie logiki programu przy samym imporcie,
- brak rozdziału między funkcjami a kodem startowym,
- wrzucanie zbyt dużej ilości logiki bezpośrednio do bloku `if __name__ == "__main__":`.

---

## Praktyczne przykłady

### Prosty punkt wejścia

```python
def main():
    print("Program wystartowal")

if __name__ == "__main__":
    main()
```

### Kod testowy tylko przy uruchomieniu

```python
def dodaj(a, b):
    return a + b

if __name__ == "__main__":
    print(dodaj(2, 3))
```

### Import bez efektu ubocznego

```python
def hello():
    print("czesc")
```

Taki plik można importować bez niechcianego uruchamiania programu.

---

## Dobre praktyki

- trzymaj punkt wejścia w `main()`,
- używaj `if __name__ == "__main__"` do uruchamiania programu,
- nie mieszaj definicji funkcji z logiką wykonywaną przy imporcie,
- używaj tego idiomu konsekwentnie w skryptach i prostych CLI.

---

## Podsumowanie

To prosty mechanizm, ale bardzo ważny dla czystej organizacji kodu.

Jeśli dobrze go używasz, Twoje moduły są bezpieczniejsze i czytelniejsze.

---

## Mini ściąga

```python
def main():
    ...

if __name__ == "__main__":
    main()
```

---

## Ćwiczenia

1. Utwórz plik z funkcją `main()`.
2. Dodaj `if __name__ == "__main__":`.
3. Sprawdź różnicę między uruchomieniem a importem.
4. Dodaj prosty ręczny test modułu pod tym blokiem.

---

## Przykładowe rozwiązania

```python
def main():
    print("hello")

if __name__ == "__main__":
    main()
```
