# Testy E2E w Pythonie

## O co chodzi

E2E to skrót od end-to-end.

Test E2E sprawdza pełny przepływ systemu z perspektywy użytkownika albo zewnętrznego klienta.

Nie patrzy już tylko na jedną warstwę lub kilka współpracujących klas. Patrzy na całą drogę:

- od wejścia,
- przez logikę,
- przez integracje,
- aż do końcowego rezultatu.

## Najprostsza intuicja

Test integracyjny pyta:

- czy kilka części współpracuje dobrze?

Test E2E pyta:

- czy cały scenariusz biznesowy działa od początku do końca?

To inny poziom zaufania i inny koszt.

## Przykład E2E

Scenariusz:

- użytkownik wysyła request tworzący zamówienie,
- system waliduje dane,
- zapisuje rekord,
- nalicza cenę,
- wysyła powiadomienie,
- zwraca poprawną odpowiedź.

To już nie jest tylko integracja dwóch klas. To przepływ całego użycia systemu.

## Dlaczego E2E są ważne

Bo czasem wszystko wygląda dobrze lokalnie w poszczególnych warstwach, ale cały system jako całość nadal zawodzi.

E2E potrafią wykryć np.:

- zły wiring systemu,
- niezgodność konfiguracji,
- brakujący krok w przepływie,
- problem w kolejności działań,
- błędy, które pojawiają się dopiero przy pełnym scenariuszu.

## Dlaczego E2E są drogie

To bardzo ważne.

E2E zwykle są:

- wolniejsze,
- trudniejsze w utrzymaniu,
- bardziej podatne na niestabilność,
- bardziej zależne od środowiska,
- trudniejsze do diagnozowania niż unit testy.

Dlatego nie powinny być jedynym typem testów w projekcie.

## Kiedy E2E mają sens

Szczególnie gdy:

- chcesz chronić kluczowe przepływy biznesowe,
- system ma wiele warstw i integracji,
- potrzebujesz najwyższego poziomu zaufania dla kilku krytycznych scenariuszy,
- deploy bez takiego testu byłby zbyt ryzykowny.

## Kiedy nie przesadzać

Nie każdy detal wymaga E2E.

Jeśli spróbujesz testować E2E wszystko, zwykle skończysz z:

- wolnym pipeline'em,
- trudnym utrzymaniem,
- flaky tests,
- mniejszą czytelnością tego, co naprawdę ma być chronione.

E2E są ważne, ale powinny być użyte selektywnie.

## Co powinien chronić dobry test E2E

Najlepiej coś naprawdę wartościowego, np.:

- rejestrację użytkownika,
- logowanie,
- tworzenie zamówienia,
- finalizację płatności,
- eksport ważnego raportu.

Czyli przepływ, którego awaria naprawdę boli system i użytkownika.

## E2E vs integracja

### Integracja

Chroni współpracę kilku elementów.

### E2E

Chroni cały scenariusz użycia systemu.

Dobrze mieć oba poziomy, ale nie mylić ich ról.

## Mini case study

Masz:

- testy serwisów,
- testy repo,
- testy endpointów.

Wszystko przechodzi.

A mimo to użytkownik nie może skutecznie złożyć zamówienia, bo jeden krok w pełnym przepływie nie zapisuje pola wymaganej konfiguracji.

To bardzo typowy przypadek, w którym E2E daje wartość ponad niższe poziomy testów.

## Typowe błędy początkujących

- zbyt dużo E2E,
- testowanie detali zamiast krytycznych scenariuszy,
- używanie E2E jako substytutu niższych warstw testów,
- brak refleksji nad kosztem utrzymania,
- niestabilność wynikająca z zbyt wielkiej złożoności środowiska.

## Szybka ściąga

- E2E testuje pełny scenariusz od wejścia do końca,
- daje bardzo wysoki poziom zaufania,
- ale jest kosztowny i ciężki,
- najlepiej chroni kilka najważniejszych przepływów systemu,
- nie powinien zastępować unitów i integracji.

## Ćwiczenia

1. Podaj 3 scenariusze, które warto testować E2E.
2. Wskaż 3 rzeczy, których nie testowałbyś E2E.
3. Opisz, czym różni się E2E od integracji na przykładzie API.
4. Zaprojektuj jeden test E2E dla tworzenia zamówienia.
5. Wytłumacz, czemu nadmiar E2E szkodzi pipeline'owi i utrzymaniu.

## Najważniejsze do zapamiętania

- E2E chroni pełny scenariusz użytkownika lub systemu.
- Daje wysoki poziom zaufania, ale kosztuje dużo więcej niż niższe poziomy testów.
- Powinien być używany do najważniejszych przepływów, a nie do wszystkiego.
- Nie zastępuje integracji ani unit testów.
- Najlepsze E2E są celowe, małe w liczbie i bardzo wartościowe biznesowo.
