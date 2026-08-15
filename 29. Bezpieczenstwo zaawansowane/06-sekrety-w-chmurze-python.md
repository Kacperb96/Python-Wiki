# Sekrety w chmurze python

Sekrety to nie tylko hasła w kodzie.

To także:

- tokeny API,
- connection stringi,
- klucze do usług chmurowych,
- dane do bazy,
- klucze podpisujące,
- sekrety sesji i JWT.

W większych systemach problemem staje się nie tylko samo istnienie sekretu, ale też:

- gdzie jest trzymany,
- kto ma do niego dostęp,
- czy może wyciec do logów,
- jak go rotować,
- jak ograniczać skutki wycieku.

## 1. Najgorszy wariant

```python
API_KEY = "super-secret-prod-key"
```

Dlaczego to złe:

- trafia do repo,
- trafia do historii,
- może trafić do screenshotów,
- trudno to bezpiecznie rotować,
- zwykle kończy się bałaganem między środowiskami.

## 2. Lepsze podejście

Sekrety powinny być poza kodem.

Najprostsza intuicja:

- kod zna nazwę sekretu,
- środowisko dostarcza wartość,
- dostęp powinien być ograniczony,
- system powinien unikać pokazywania sekretu w logach.

## 3. Ryzyka operacyjne

Nawet jeśli sekret nie siedzi w kodzie, nadal mogą być problemy:

- zbyt szeroki dostęp wielu usług,
- jeden sekret używany wszędzie,
- brak rotacji,
- kopiowanie sekretów między środowiskami,
- wyciek przez debug output,
- wyciek przez exception message.

## 4. Dobre praktyki

- rozdzielaj sekrety per środowisko,
- ograniczaj dostęp zgodnie z potrzebą,
- nie wypisuj pełnych wartości,
- rotuj po incydencie,
- dokumentuj, do czego sekret służy,
- nie używaj jednego globalnego klucza do wszystkiego.

## 5. Przykład myślowy

Źle:

```text
dev, stage i prod używają tego samego klucza
```

Lepiej:

```text
każde środowisko ma własny sekret
każda usługa ma tylko potrzebny zakres
```

## 6. Logowanie a sekrety

Bardzo częsty problem:

```python
print(config)
```

albo:

```python
logger.info("payload=%s", payload)
```

Jeśli w tym payloadzie albo konfiguracji siedzą sekrety, właśnie zrobiłeś potencjalny wyciek.

## 7. Co zrobić po wycieku

Jeśli sekret wyciekł:

1. nie zakładaj, że "pewnie nikt nie widział"
2. potraktuj go jak zagrożony
3. zrotuj go
4. ustal zasięg wycieku
5. dodaj zabezpieczenia, żeby to się nie powtórzyło

## Zadania

1. Podaj co najmniej 5 przykładów sekretów w typowej aplikacji.
2. Wyjaśnij, czemu samo trzymanie sekretu poza kodem jeszcze nie kończy tematu bezpieczeństwa.
3. Opisz, co zrobić po przypadkowym wycieku tokena.
