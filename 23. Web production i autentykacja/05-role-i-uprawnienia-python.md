# Role i uprawnienia python

## O czym jest ten rozdział

Samo ustalenie, kim jest użytkownik, to dopiero połowa problemu.

Druga połowa brzmi:

- co ten użytkownik może zrobić?

Tu wchodzą role, uprawnienia, scope'y i polityki dostępu.

To jest rdzeń autoryzacji.

## Uwierzytelnianie a autoryzacja

To rozróżnienie musisz mieć bardzo mocne.

Uwierzytelnianie odpowiada na pytanie:

- kim jesteś?

Autoryzacja odpowiada na pytanie:

- co wolno ci zrobić?

Przykład:

- użytkownik jest poprawnie zalogowany,
- ale nadal nie musi mieć prawa usunąć zamówienia albo wejść do panelu admina.

## Rola: najprostsza intuicja

Rola to wysoki poziom klasyfikacji użytkownika.

Przykłady:

- `admin`,
- `editor`,
- `viewer`,
- `customer`.

Rola upraszcza myślenie o dostępie.

## Uprawnienie: bardziej szczegółowy poziom

Uprawnienie opisuje konkretną możliwość działania.

Przykłady:

- `orders.read`,
- `orders.write`,
- `orders.delete`,
- `users.manage`.

To często daje większą kontrolę niż same role.

## Role a uprawnienia

Najczęstszy praktyczny model:

- użytkownik ma jedną lub kilka ról,
- role mapują się na zestaw uprawnień,
- system sprawdza konkretne uprawnienie przy akcji.

Przykład:

- `admin` ma `users.manage`, `orders.read`, `orders.write`, `orders.delete`,
- `support` ma `orders.read`, `orders.write`,
- `viewer` ma tylko `orders.read`.

## Prosta symulacja w Pythonie

```python
ROLE_PERMISSIONS = {
    "admin": {"orders.read", "orders.write", "orders.delete", "users.manage"},
    "support": {"orders.read", "orders.write"},
    "viewer": {"orders.read"},
}


def has_permission(role: str, permission: str) -> bool:
    permissions = ROLE_PERMISSIONS.get(role, set())
    return permission in permissions


print(has_permission("admin", "orders.delete"))
print(has_permission("viewer", "orders.write"))
print(has_permission("support", "orders.read"))
```

Output:

```text
True
False
True
```

## Before/after: zbyt prosto vs sensowniej

### Zbyt prosty model

```python
if user.role == "admin":
    allow()
else:
    deny()
```

Problem:

- wszystko zależy od jednej roli,
- trudno modelować przypadki pośrednie,
- szybko robi się bałagan.

### Lepszy model

```python
if user_has_permission(user, "orders.delete"):
    allow()
else:
    deny()
```

To jest zwykle bardziej elastyczne.

## Scope a uprawnienia

W systemach tokenowych i OAuth2 często pojawia się pojęcie `scope`.

To jest bardzo podobne do uprawnienia, ale zwykle myślane bardziej w kontekście tokena lub delegowanego dostępu.

Przykład:

- `orders:read`
- `orders:write`

W praktyce ważniejsze od nazwy jest to, żeby model był spójny.

## Gdzie sprawdzać autoryzację

Autoryzacja może być sprawdzana w różnych miejscach:

- w endpointzie,
- w middleware,
- w warstwie serwisowej,
- w osobnej polityce lub guardzie.

Najważniejsze, żeby decyzja nie była rozlana chaotycznie po całym kodzie.

## Przykład intuicyjny

```python
def delete_order(user_role: str, order_id: int) -> str:
    if not has_permission(user_role, "orders.delete"):
        return "403 FORBIDDEN"
    return f"order {order_id} deleted"


print(delete_order("admin", 10))
print(delete_order("viewer", 10))
```

Output:

```text
order 10 deleted
403 FORBIDDEN
```

## Najczęstsze pułapki

### 1. Mylenie roli z uprawnieniem

Rola to etykieta wyższego poziomu.

Uprawnienie to konkretna akcja.

### 2. Zbyt grube role

Jeśli masz tylko:

- `admin`,
- `user`,

bardzo szybko możesz dojść do miejsca, gdzie połowa systemu nie mieści się w takim podziale.

### 3. Sprawdzanie roli wszędzie ręcznie

Jeśli w 30 miejscach masz:

```python
if user.role == "admin":
```

to za jakiś czas będzie to trudne do utrzymania.

Lepiej centralizować decyzję.

### 4. Brak zasady najmniejszych uprawnień

Użytkownik albo aplikacja powinni mieć tylko tyle uprawnień, ile naprawdę potrzeba.

Nie więcej.

### 5. Twarde kodowanie wyjątków biznesowych w losowych miejscach

Np. jeden endpoint pozwala na coś `supportowi`, drugi już nie, trzeci ma jeszcze inne zasady i nikt nie wie czemu.

## Case study

Masz aplikację zamówień.

### Złe podejście

- `admin` może wszystko,
- wszyscy inni prawie nic,
- część wyjątków dopisywana ręcznie po if-ach.

### Lepsze podejście

- definiujesz listę operacji,
- mapujesz role do uprawnień,
- w kodzie sprawdzasz konkretne permission,
- wyjątkowe reguły biznesowe trzymasz świadomie w jednej warstwie.

## Co z właścicielem zasobu

Czasem sama rola nie wystarczy.

Przykład:

- użytkownik może edytować tylko swoje zamówienie,
- ale nie cudze.

Wtedy decyzja zależy nie tylko od roli, ale też od kontekstu zasobu.

To ważny krok w dojrzalszej autoryzacji.

## Najważniejsze do zapamiętania

- Uwierzytelnianie i autoryzacja to nie to samo.
- Rola to uproszczona kategoria, uprawnienie to konkretna możliwość działania.
- W praktyce często lepiej sprawdzać uprawnienia niż same role.
- Autoryzacja powinna być spójna i możliwie scentralizowana.
- Dobra autoryzacja opiera się na zasadzie najmniejszych uprawnień.

## Ćwiczenia

1. Wyjaśnij różnicę między rolą i uprawnieniem.
2. Zaprojektuj trzy role dla systemu zamówień i przypisz im uprawnienia.
3. Opisz przypadek, w którym sama rola nie wystarcza do podjęcia decyzji.
4. Napisz prostą funkcję `has_permission(user, permission)`.
5. Podaj dwa przykłady zbyt szerokich uprawnień i ryzyka z nimi związanego.
