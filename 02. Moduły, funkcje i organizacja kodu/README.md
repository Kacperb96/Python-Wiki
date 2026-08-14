# 02. Moduły, funkcje i organizacja kodu

Ten dział uczy, jak przejść od pojedynczych instrukcji do sensownie zorganizowanego kodu.

To jest moment, w którym zaczynasz odchodzić od:

- prostych skryptów,
- kodu pisanego liniowo,
- wrzucania wszystkiego do jednego pliku,

i przechodzisz do kodu, który:

- da się ponownie używać,
- da się rozwijać,
- da się czytać po czasie,
- da się sensownie dzielić na części,
- da się importować bez chaosu,
- da się uruchamiać w przewidywalny sposób.

---

## Co powinieneś zrozumieć po tym dziale

Po tym dziale powinieneś rozumieć:

- jak projektować funkcje,
- czym różni się `print()` od `return`,
- kiedy używać zwykłych argumentów, a kiedy `*args` i `**kwargs`,
- czym jest `lambda` i kiedy nie warto jej używać,
- jak działają moduły i importy,
- czym są pakiety,
- po co istnieje `if __name__ == "__main__"`,
- jak układać kod w małym projekcie,
- jak pisać funkcje, których API jest czytelne i przewidywalne.

---

## Jak czytać ten dział

Najlepiej czytać po kolei:

1. [01-funkcje-python.md](/home/kacper/Desktop/Python/02.%20Moduły,%20funkcje%20i%20organizacja%20kodu/01-funkcje-python.md)
2. [02-args-kwargs-python.md](/home/kacper/Desktop/Python/02.%20Moduły,%20funkcje%20i%20organizacja%20kodu/02-args-kwargs-python.md)
3. [03-lambda-python.md](/home/kacper/Desktop/Python/02.%20Moduły,%20funkcje%20i%20organizacja%20kodu/03-lambda-python.md)
4. [04-moduly-i-importy-python.md](/home/kacper/Desktop/Python/02.%20Moduły,%20funkcje%20i%20organizacja%20kodu/04-moduly-i-importy-python.md)
5. [05-pakiety-python.md](/home/kacper/Desktop/Python/02.%20Moduły,%20funkcje%20i%20organizacja%20kodu/05-pakiety-python.md)
6. [06-name-main-python.md](/home/kacper/Desktop/Python/02.%20Moduły,%20funkcje%20i%20organizacja%20kodu/06-name-main-python.md)
7. [07-api-funkcji-i-czytelnosc-python.md](/home/kacper/Desktop/Python/02.%20Moduły,%20funkcje%20i%20organizacja%20kodu/07-api-funkcji-i-czytelnosc-python.md)
8. [08-organizacja-projektu-python.md](/home/kacper/Desktop/Python/02.%20Moduły,%20funkcje%20i%20organizacja%20kodu/08-organizacja-projektu-python.md)

Ta kolejność ma sens:

- najpierw uczysz się pisać funkcje,
- potem przekazywać argumenty bardziej elastycznie,
- potem przechodzisz do importów i podziału na pliki,
- a na końcu do projektowania API i organizowania projektu.

---

## Jak pracować z tym działem

Najlepiej nie tylko czytać, ale też:

1. przepisywać przykłady,
2. robić własne mikroeksperymenty,
3. rozwiązywać zadania partiami,
4. próbować dzielić własny kod na moduły i funkcje,
5. przewidywać output przed uruchomieniem,
6. porównywać dwie wersje kodu:
   - “działa”,
   - “działa i jest czytelne”.

To dział mocno praktyczny. Sama teoria nie wystarczy.

---

## Na co szczególnie uważać

W tym dziale początkujący najczęściej wpadają w te pułapki:

- mylenie `print()` i `return`,
- pisanie funkcji, które robią za dużo naraz,
- nadużywanie `*args` i `**kwargs`,
- robienie importów bez rozumienia, skąd naprawdę bierze się dana nazwa,
- wrzucanie całego programu do `main.py`,
- mieszanie logiki biznesowej z kodem startowym,
- zbyt ogólne nazwy funkcji typu `handle`, `process`, `fun1`.

Jeśli nauczysz się tych rzeczy unikać, jakość Twojego kodu skoczy bardzo mocno.

---

## Po czym poznać, że dział jest opanowany

Dobry znak to sytuacja, w której potrafisz:

- napisać czytelną funkcję z `return`,
- rozróżnić, kiedy warto użyć zwykłego parametru, a kiedy `*args` lub `**kwargs`,
- rozumieć proste importy,
- rozbić program na dwa lub trzy pliki,
- napisać prosty punkt wejścia z `main()`,
- stworzyć mały pakiet bez chaosu,
- poprawić źle zaprojektowane API funkcji,
- wyjaśnić, czemu pewna struktura projektu jest czytelna albo nieczytelna.

---

## Jak ćwiczyć najlepiej

Po tym dziale bardzo dobrze działają małe projekty typu:

- kalkulator podzielony na moduły,
- prosty menedżer zadań,
- walidator formularza,
- moduł z helperami i osobny plik startowy,
- mini CLI z `main()`.

Tu nie chodzi jeszcze o wielką aplikację.
Chodzi o nauczenie się porządku.

---

## Materiały pomocnicze

Do praktyki służy:

- [ZESTAW-CWICZEN.md](/home/kacper/Desktop/Python/02.%20Moduły,%20funkcje%20i%20organizacja%20kodu/ZESTAW-CWICZEN.md)

---

## Co dalej

Po tym dziale przejdź do:

- [03. Kolekcje](/home/kacper/Desktop/Python/03.%20Kolekcje)

A potem do:

- [04. Programowanie obiektowe](/home/kacper/Desktop/Python/04.%20Programowanie%20obiektowe)
