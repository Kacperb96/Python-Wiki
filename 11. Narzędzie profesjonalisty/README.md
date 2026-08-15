# 11. Narzędzie profesjonalisty

To jest dział o codziennym, dojrzałym workflow pracy nad projektem Python.

Nie chodzi tu już tylko o sam język.

Chodzi o pytania typu:

- jak skonfigurować projekt sensownie od początku,
- jak utrzymać spójny styl kodu,
- jak automatycznie łapać błędy jakościowe,
- jak uporządkować zależności i środowisko,
- jak zautomatyzować lokalny workflow,
- jak sprawić, żeby projekt sam się sprawdzał w CI.

To właśnie ten dział zaczyna pokazywać różnicę między "pisaniem kodu" a "prowadzeniem projektu jak profesjonalista".

---

## Co powinieneś rozumieć po tym dziale

Po przerobieniu tego folderu powinieneś rozumieć:

- czym jest `pyproject.toml` i dlaczego stał się centralnym plikiem projektu,
- po co używa się `ruff`, `black` i `isort`,
- czym jest `pre-commit` i co daje zespołowi,
- jak `mypy` uzupełnia testy i linting,
- czym różnią się `poetry`, `uv`, `pip` i `venv`,
- po co komu `Makefile` w projekcie Python,
- jak działa podstawowy pipeline CI w GitHub Actions,
- kiedy `tox` ma sens,
- kiedy `nox` ma sens,
- jak złożyć z tych narzędzi jeden spójny workflow.

---

## Dlaczego ten dział jest ważny

Na pewnym etapie nauki sam kod to za mało.

Pojawia się potrzeba:

- powtarzalności,
- porządku,
- automatyzacji,
- szybkiego onboardingu,
- spójnych zasad jakości.

Właśnie dlatego profesjonalne projekty mają zwykle nie tylko `src/` i `tests/`, ale też:

- `pyproject.toml`,
- konfigurację lintingu i formatowania,
- hooki `pre-commit`,
- pipeline CI,
- jasny sposób odpalania testów i checków.

---

## Jak czytać ten dział

Najlepiej iść po kolei:

1. [01-pyproject-toml-python.md](/home/kacper/Desktop/Python_naprawiony/11.%20Narz%C4%99dzie%20profesjonalisty/01-pyproject-toml-python.md)
2. [02-ruff-python.md](/home/kacper/Desktop/Python_naprawiony/11.%20Narz%C4%99dzie%20profesjonalisty/02-ruff-python.md)
3. [03-black-python.md](/home/kacper/Desktop/Python_naprawiony/11.%20Narz%C4%99dzie%20profesjonalisty/03-black-python.md)
4. [04-isort-python.md](/home/kacper/Desktop/Python_naprawiony/11.%20Narz%C4%99dzie%20profesjonalisty/04-isort-python.md)
5. [05-pre-commit-python.md](/home/kacper/Desktop/Python_naprawiony/11.%20Narz%C4%99dzie%20profesjonalisty/05-pre-commit-python.md)
6. [06-mypy-python.md](/home/kacper/Desktop/Python_naprawiony/11.%20Narz%C4%99dzie%20profesjonalisty/06-mypy-python.md)
7. [07-poetry-python.md](/home/kacper/Desktop/Python_naprawiony/11.%20Narz%C4%99dzie%20profesjonalisty/07-poetry-python.md)
8. [08-uv-python.md](/home/kacper/Desktop/Python_naprawiony/11.%20Narz%C4%99dzie%20profesjonalisty/08-uv-python.md)
9. [09-makefile-dla-python.md](/home/kacper/Desktop/Python_naprawiony/11.%20Narz%C4%99dzie%20profesjonalisty/09-makefile-dla-python.md)
10. [10-github-actions-python.md](/home/kacper/Desktop/Python_naprawiony/11.%20Narz%C4%99dzie%20profesjonalisty/10-github-actions-python.md)
11. [11-tox-python.md](/home/kacper/Desktop/Python_naprawiony/11.%20Narz%C4%99dzie%20profesjonalisty/11-tox-python.md)
12. [12-nox-python.md](/home/kacper/Desktop/Python_naprawiony/11.%20Narz%C4%99dzie%20profesjonalisty/12-nox-python.md)

Ta kolejność ma sens, bo:

- najpierw budujesz bazę projektu,
- potem ogarniasz jakość kodu,
- potem automatyzację lokalną,
- potem zarządzanie zależnościami,
- na końcu automatyzację zespołową i wielośrodowiskową.

---

## Jak pracować z tym działem

Najlepszy sposób nauki:

1. przeczytaj jeden plik,
2. odtwórz pokazany przykład u siebie,
3. przewidź, co zrobi narzędzie,
4. uruchom je naprawdę,
5. porównaj wynik z opisem,
6. zrób 1-2 własne warianty,
7. przejdź do ćwiczeń.

Ten dział bardzo zyskuje, kiedy naprawdę odpalasz narzędzia, a nie tylko czytasz o nich teoretycznie.

---

## Na co szczególnie uważać

Najczęstsze pułapki:

- dokładanie zbyt wielu narzędzi naraz bez zrozumienia,
- mieszanie kilku workflow zależności bez planu,
- kopiowanie konfiguracji z internetu bez świadomości, co ona robi,
- wybieranie narzędzia dlatego, że jest modne, a nie dlatego, że rozwiązuje problem,
- traktowanie lintingu, typów i CI jako biurokracji zamiast wsparcia jakości.

---

## Po czym poznać, że temat zaczyna siedzieć

Dobry znak, jeśli potrafisz:

- wyjaśnić rolę `pyproject.toml`,
- odróżnić formatter od lintera,
- powiedzieć, kiedy `ruff` wystarczy, a kiedy potrzebujesz jeszcze innych narzędzi,
- złożyć prosty `pre-commit`,
- wyjaśnić sens `mypy`,
- opisać różnicę `poetry` vs `uv` vs `pip` + `venv`,
- napisać prosty `Makefile`,
- rozumieć, po co projektowi CI,
- wskazać, kiedy `tox` albo `nox` są zasadne.

---

## Co ten dział daje w praktyce

Po opanowaniu tego folderu zaczniesz budować projekty, które są:

- bardziej przewidywalne,
- łatwiejsze do uruchomienia,
- łatwiejsze do rozwijania,
- przyjemniejsze we współpracy,
- bardziej zbliżone do realnych repozytoriów zawodowych.

---

## Ćwiczenia

Do tego działu masz też [ZESTAW-CWICZEN.md](/home/kacper/Desktop/Python_naprawiony/11.%20Narz%C4%99dzie%20profesjonalisty/ZESTAW-CWICZEN.md).

Najlepiej robić go partiami:

- najpierw `pyproject.toml` i narzędzia jakości,
- potem `pre-commit`, `mypy`, `Makefile`,
- dopiero później `poetry`, `uv`, CI, `tox`, `nox`.

---

## Co dalej

Po tym dziale naturalny następny krok to:

- [12. Asynchroniczność i wielowątkowość](/home/kacper/Desktop/Python_naprawiony/12.%20Asynchroniczno%C5%9B%C4%87%20i%20wielow%C4%85tkowo%C5%9B%C4%87)
- albo [13. Web i API](/home/kacper/Desktop/Python_naprawiony/13.%20Web%20i%20API)

Ale najpierw dobrze mieć uporządkowany obraz nowoczesnego workflow projektu.
