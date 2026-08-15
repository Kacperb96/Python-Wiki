# Eventual consistency python

## O czym jest ten rozdział

Gdy system przestaje być jedną aplikacją z jedną bazą i zaczyna działać przez kolejki, workery albo wiele usług, bardzo często przestajesz mieć natychmiastową spójność wszędzie naraz.

Pojawia się wtedy temat:

- eventual consistency.

To pojęcie na początku często budzi niepokój, bo brzmi jak elegancka nazwa na "system czasem jest niespójny".

I częściowo to prawda, ale ważne jest zrozumienie, że w systemach rozproszonych bywa to świadomy kompromis projektowy, a nie automatycznie błąd.

## Najprostsza intuicja

Eventual consistency oznacza, że różne części systemu nie muszą widzieć tego samego stanu natychmiast, ale po pewnym czasie powinny dojść do zgodności.

Najprościej:

- zmiana wydarza się tu,
- informacja propaguje się dalej,
- przez chwilę system może być "w trakcie dochodzenia do nowego stanu",
- po czasie wszystko powinno się wyrównać.

## Przykład intuicyjny

Masz sklep internetowy.

Klient składa zamówienie.

Backend:

1. zapisuje zamówienie w bazie,
2. publikuje event `order_created`,
3. osobny worker aktualizuje CRM,
4. inny worker wysyła mail,
5. jeszcze inny system aktualizuje dashboard raportowy.

Tu nie wszystko musi wydarzyć się w tej samej milisekundzie.

Przez krótką chwilę może być tak, że:

- zamówienie już istnieje,
- mail jeszcze nie wyszedł,
- CRM jeszcze go nie widzi,
- dashboard jeszcze go nie policzył.

To właśnie intuicja eventual consistency.

## Eventual consistency nie oznacza chaosu

To bardzo ważne.

To nie znaczy:

- "może kiedyś się zepnie, a może nie".

To znaczy raczej:

- system akceptuje opóźnienie propagacji,
- ale projektuje mechanizmy, które mają doprowadzić do poprawnego stanu końcowego.

## Skąd bierze się opóźnienie

Najczęstsze źródła:

- kolejka przetwarza zadania trochę później,
- worker robi retry,
- inna usługa chwilowo nie odpowiada,
- dane są kopiowane do read modelu albo cache,
- system rozkłada pracę na etapy.

## Najprostszy przykład bez sieci

```python
state = {"order_status": "created", "email_sent": False}


def create_order():
    state["order_status"] = "created"


def send_email_later():
    state["email_sent"] = True


create_order()
print(state)
send_email_later()
print(state)
```

Output:

```text
{'order_status': 'created', 'email_sent': False}
{'order_status': 'created', 'email_sent': True}
```

Pomiędzy tymi dwoma momentami system jest poprawny z perspektywy procesu, ale jeszcze nie wszystko jest wyrównane.

## Kiedy eventual consistency ma sens

Eventual consistency ma sens szczególnie wtedy, gdy:

- nie wszystko musi być natychmiast widoczne wszędzie,
- chcesz rozdzielić system na komponenty,
- część pracy może wykonać się później,
- zależy Ci na skalowaniu i odporności bardziej niż na pełnej synchroniczności,
- system ma wiele read modeli albo integracji pobocznych.

## Kiedy eventual consistency boli

Boli wtedy, gdy:

- użytkownik oczekuje natychmiastowego efektu,
- system nie komunikuje dobrze stanu przejściowego,
- opóźnienie jest zbyt duże,
- brak mechanizmów naprawczych,
- zespół nie rozumie, które widoki są ostateczne, a które opóźnione.

## Before/after

### Myślenie synchroniczne

- wszystko ma być gotowe od razu,
- jedna awaria może blokować cały flow,
- system jest prostszy logicznie, ale bardziej kruchy i cięższy.

### Myślenie z eventual consistency

- część skutków następuje później,
- system jest bardziej rozdzielony,
- trzeba akceptować i kontrolować stany przejściowe.

## Stan przejściowy: bardzo ważna intuicja

W systemie rozproszonym często istnieje okres, w którym prawidłowa odpowiedź brzmi:

- "zamówienie zostało przyjęte, dalsze kroki są w toku".

To nie musi być bug.

To może być świadomie zaprojektowany etap życia procesu.

## Mini case study: zamówienie i mail

Klient składa zamówienie.

### Oczekiwanie naiwne

- skoro zamówienie jest zapisane, to mail już musi być wysłany.

### Realistyczny system

- zamówienie jest zapisane,
- mail jest w kolejce,
- worker wyśle go za chwilę,
- chwilowy brak maila nie oznacza utraty zamówienia.

To bardzo typowy przykład eventual consistency, który biznes często musi zrozumieć.

## Mini case study: read model

Masz osobny dashboard analityczny.

- baza operacyjna przyjmuje zamówienie,
- event trafia do kolejki,
- osobny proces aktualizuje agregaty raportowe.

Przez chwilę dashboard może nie pokazywać najnowszego zamówienia.

To normalne, jeśli system jest tak zaprojektowany.

## Co trzeba zaprojektować dobrze

Jeśli akceptujesz eventual consistency, musisz dobrze zaprojektować:

- retry,
- idempotencję,
- monitorowanie opóźnień,
- komunikację stanów przejściowych,
- możliwość naprawy lub ponownego przetworzenia.

Bo bez tego opóźniona spójność zmienia się po prostu w bałagan.

## Najczęstsze pułapki

### 1. Udawanie, że wszystko jest natychmiastowe

Jeśli UI albo API obiecuje za dużo, użytkownik uzna normalne opóźnienie za błąd.

### 2. Brak monitorowania lagów i opóźnień

Jeśli worker stoi albo kolejka się zapycha, eventual consistency może trwać za długo.

### 3. Brak mechanizmów naprawczych

Jeśli event zginie albo consumer padnie bez retry, stan może nigdy się nie wyrównać.

### 4. Mieszanie systemów krytycznie spójnych z tymi, które mogą być opóźnione

Nie wszystko nadaje się do eventual consistency w takim samym stopniu.

## Co Pythonowiec powinien rozumieć

Dobrze, żebyś umiał:

- rozpoznać, które części systemu mogą być opóźnione,
- odróżnić stan przejściowy od realnego błędu,
- wiedzieć, że rozproszenie prawie zawsze wprowadza opóźnienie,
- zaprojektować komunikację między komponentami z myślą o retry i dubelkach,
- nie obiecywać natychmiastowej spójności tam, gdzie architektura jej nie daje.

## Output myślowy

### Bez akceptacji eventual consistency

- zespół walczy o pełną synchroniczność wszędzie,
- rośnie sprzężenie i kruchość systemu,
- awarie bocznych integracji blokują główny flow.

### Ze świadomą eventual consistency

- część systemu działa później,
- ale całość jest bardziej elastyczna,
- trzeba jednak dobrze kontrolować opóźnienie i naprawialność.

## Najważniejsze do zapamiętania

- Eventual consistency oznacza opóźnioną, ale docelową zgodność stanu.
- W systemach rozproszonych to często świadomy kompromis, a nie błąd sam w sobie.
- Stan przejściowy może być normalnym etapem procesu.
- Retry, idempotencja i monitoring są kluczowe, żeby ta architektura działała bez chaosu.
- Nie każda część systemu nadaje się do tego samego poziomu opóźnienia i asynchroniczności.

## Ćwiczenia

1. Wyjaśnij własnymi słowami, czym jest eventual consistency.
2. Podaj przykład systemu, w którym opóźniona spójność jest akceptowalna.
3. Opisz sytuację, w której eventual consistency byłaby trudna biznesowo.
4. Wypisz trzy mechanizmy, które pomagają utrzymać eventual consistency pod kontrolą.
5. Rozpisz flow zamówienia, w którym część skutków dzieje się asynchronicznie.
