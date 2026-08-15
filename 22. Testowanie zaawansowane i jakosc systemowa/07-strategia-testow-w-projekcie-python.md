# Strategia testów w projekcie Python

## O co chodzi

Strategia testów to odpowiedź na pytanie:

- jakie testy chcemy mieć,
- na jakich poziomach,
- po co,
- i co dokładnie mają chronić.

To ważne, bo bez strategii testy łatwo stają się zbiorem przypadkowych plików, które istnieją, ale nie dają prawdziwego zaufania.

## Najważniejsza zasada

Nie chodzi o maksymalną liczbę testów.

Chodzi o sensowny układ testów, który daje zaufanie przy rozsądnym koszcie utrzymania.

## Jak myśleć o strategii

Bardzo praktyczne pytania:

- które części systemu są najbardziej krytyczne,
- gdzie najłatwiej o regresję,
- które integracje są ryzykowne,
- co powinno być szybko sprawdzane lokalnie,
- co powinno być sprawdzane przed deployem,
- które testy są drogie i jak ograniczyć ich liczbę.

## Typowe poziomy strategii

### Unit tests

Dobre dla:

- małej logiki,
- czystych funkcji,
- szybkiego feedbacku,
- wielu wariantów edge case.

### Integration tests

Dobre dla:

- granic między warstwami,
- współpracy serwisu z repo,
- adapterów,
- integracji z bazą i systemem wewnętrznym.

### E2E tests

Dobre dla:

- kilku kluczowych scenariuszy biznesowych,
- ochrony najważniejszych przepływów użytkownika.

### Contract tests

Dobre dla:

- granic między usługami,
- stabilności API,
- kształtu komunikacji między systemami.

## Dobry balans

W zdrowym projekcie zwykle chcesz:

- dużo szybkich testów niższego poziomu,
- mniejszą liczbę sensownych integracji,
- jeszcze mniejszą liczbę krytycznych E2E,
- contract tests tam, gdzie system dotyka zewnętrznych albo osobno rozwijanych granic.

To dużo lepsze niż próba rozwiązania wszystkiego jednym poziomem testów.

## Co powinno mieć największe pokrycie zaufania

Nie wszystko w systemie jest równie ważne.

Najwięcej ochrony zwykle powinny dostać:

- kluczowe przepływy biznesowe,
- krytyczne obliczenia,
- miejsca z dużym ryzykiem regresji,
- integracje z zewnętrznymi systemami,
- logika, której awaria mocno boli użytkownika albo firmę.

## Mini case study

Masz aplikację zamówień.

Strategia może wyglądać tak:

- unit testy dla liczenia ceny i walidacji,
- integracyjne dla serwisu + repo,
- contract tests dla klienta płatności,
- 2-3 E2E dla stworzenia zamówienia, płatności i anulowania.

To dużo sensowniejsze niż np. 100 ciężkich E2E albo tylko same unity.

## Jak strategia pomaga w utrzymaniu

Dobra strategia pozwala odpowiedzieć:

- czemu ten test istnieje,
- co ma chronić,
- na jakim poziomie warto go trzymać,
- czy jego koszt jest uzasadniony.

Bez tego łatwo rośnie las testów bez sensownego planu.

## Typowe błędy początkujących

- brak myślenia poziomami testów,
- zbyt dużo ciężkich testów, zbyt mało szybkich,
- za duże zaufanie do samych mocków,
- zbyt dużo E2E do prostych rzeczy,
- brak odpowiedzi, co naprawdę ma chronić dany test.

## Szybka ściąga

- strategia testów to plan zaufania do systemu,
- różne poziomy testów służą różnym celom,
- nie wszystko trzeba testować na najwyższym poziomie,
- najlepsza strategia jest proporcjonalna do ryzyka i kosztu.

## Ćwiczenia

1. Rozpisz strategię testów dla małej aplikacji API.
2. Wskaż, które części systemu testowałbyś unitami, a które integracyjnie.
3. Zaproponuj 2 krytyczne E2E.
4. Wskaż miejsce na contract tests.
5. Opisz, jak rozpoznać, że test istnieje bez sensownego celu.

## Najważniejsze do zapamiętania

- Testy powinny być ułożone w sensowną strategię, nie tylko istnieć.
- Różne poziomy testów chronią różne ryzyka.
- Najlepsza strategia daje dużo zaufania przy rozsądnym koszcie.
- Nie wszystko wymaga E2E, nie wszystko da się pokryć unit testem.
- Dobre testowanie to decyzja projektowa, nie tylko techniczna.
