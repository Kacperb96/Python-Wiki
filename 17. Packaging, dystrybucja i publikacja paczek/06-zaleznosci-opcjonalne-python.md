# Zależności opcjonalne w Pythonie

## O co chodzi

Nie każda zależność projektu musi być obowiązkowa dla każdego użytkownika.

Czasem paczka ma:

- podstawowy rdzeń,
- opcjonalne funkcje,
- osobne narzędzia developerskie,
- dodatkowe integracje.

Właśnie wtedy sens mają zależności opcjonalne, często nazywane extras.

## Po co extras

Extras pozwalają powiedzieć:

- podstawowa instalacja jest lekka,
- dodatkowe funkcje można doinstalować tylko wtedy, gdy są potrzebne.

To bardzo praktyczne w projektach, które:

- mają kilka trybów użycia,
- mają opcjonalne integracje,
- nie chcą narzucać wszystkich zależności każdemu.

## Przykład w `pyproject.toml`

```toml
[project.optional-dependencies]
dev = [
  "pytest>=8.0",
  "ruff>=0.6",
]
cli = [
  "click>=8.1",
]
```

To oznacza, że projekt ma dwie grupy extras:

- `dev`,
- `cli`.

## Jak użytkownik to instaluje

Przykład:

```bash
pip install moj-projekt[dev]
```

albo:

```bash
pip install moj-projekt[cli]
```

Można też łączyć extras, jeśli projekt to wspiera.

## Kiedy to ma sens

### `dev`

Bardzo częsty przypadek.

Zależności developerskie to np.:

- pytest,
- ruff,
- mypy,
- coverage,
- build tools.

One nie są potrzebne użytkownikowi końcowemu do działania paczki.

### Integracje opcjonalne

Przykład:

- paczka działa bez `pandas`,
- ale jeśli chcesz eksport do DataFrame, instalujesz extra `pandas`.

### CLI albo web

Projekt może mieć podstawowy rdzeń biblioteczny i osobny extra dla:

- CLI,
- API,
- szyfrowania,
- integracji z bazą.

## Czego nie wrzucać do extras bez sensu

Nie używaj extras tylko dlatego, że brzmią profesjonalnie.

Jeśli zależność jest naprawdę potrzebna do podstawowego działania projektu, to powinna być zwykłą zależnością runtime.

Extras są dla funkcji opcjonalnych.

## Runtime vs dev vs extras

To ważne rozróżnienie.

### Runtime dependencies

Potrzebne zawsze do działania projektu.

### Dev dependencies

Potrzebne do pracy nad projektem.

### Extras

Potrzebne do opcjonalnych funkcji albo konkretnych wariantów użycia.

## Typowe błędy początkujących

- wrzucanie wszystkiego do głównych dependencies,
- mylenie extras z dev-only toolingiem,
- tworzenie zbyt wielu sztucznych extras,
- brak dokumentacji, co daje dany extra,
- opcjonalna funkcja, która w praktyce i tak jest wymagana prawie zawsze.

## Jak myśleć o extras dojrzale

Zadaj sobie pytania:

- czy każdy użytkownik potrzebuje tej zależności,
- czy ta funkcja naprawdę jest opcjonalna,
- czy bez tej zależności rdzeń projektu dalej ma sens,
- czy nazwa extra jasno komunikuje jego rolę.

## Przykładowy scenariusz

Masz paczkę `text-tools`.

Rdzeń działa bez dodatkowych bibliotek.

Ale:

- dla CLI chcesz `click`,
- dla developmentu chcesz `pytest` i `ruff`,
- dla eksportu CSV chcesz dodatkową integrację.

To jest bardzo sensowny moment na extras.

## Mini checklista extras

- Czy funkcja jest naprawdę opcjonalna?
- Czy nazwa extra jest czytelna?
- Czy użytkownik wie, po co go instaluje?
- Czy extra nie duplikuje głównej zależności runtime?
- Czy projekt działa sensownie bez tego extra?

## Szybka ściąga

- extras definiujesz zwykle w `[project.optional-dependencies]`,
- instalacja wygląda jak `pip install paczka[extra]`,
- extras są dla funkcji opcjonalnych,
- nie wszystko powinno trafiać do głównego `dependencies`.

## Ćwiczenia

1. Zdefiniuj `dev` extra dla małej paczki.
2. Dodaj drugi extra, np. `cli` albo `pandas`.
3. Wyjaśnij, które zależności powinny być runtime, a które opcjonalne.
4. Zaprojektuj extras dla projektu biblioteczno-CLI.
5. Opisz przypadek, gdzie extra byłby złym pomysłem.

## Najważniejsze do zapamiętania

- Zależności opcjonalne pomagają utrzymać paczkę lżejszą i bardziej elastyczną.
- Extras mają sens wtedy, gdy jakaś funkcja naprawdę nie jest potrzebna wszystkim użytkownikom.
- Trzeba odróżniać runtime, dev i extras.
- Dobrze nazwane i opisane extras poprawiają używalność projektu.
- Nadużywanie extras robi konfigurację trudniejszą zamiast lepszej.
