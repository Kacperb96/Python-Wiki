# Zestaw ćwiczeń praktycznych — 04. Programowanie obiektowe

## Poziom 1 — klasy i obiekty

1. Utwórz klasę `Dog` z atrybutami `name` i `age`.
2. Dodaj metodę `bark()` zwracającą prosty komunikat.
3. Utwórz kilka obiektów tej klasy i wypisz ich dane.
4. Utwórz klasę `User` z `__init__`.
5. Dodaj metodę `full_info()` zwracającą string z danymi użytkownika.

## Poziom 2 — atrybuty, klasy, enkapsulacja

6. Dodaj atrybut klasowy `species` do klasy `Dog`.
7. Zrób licznik wszystkich utworzonych obiektów klasy `User`.
8. Utwórz klasę `BankAccount` z metodami `deposit()` i `withdraw()`.
9. Zabezpiecz wypłatę przed zejściem poniżej zera.
10. Zasymuluj atrybut „wewnętrzny”, którego nie chcesz dotykać bezpośrednio.

## Poziom 3 — dziedziczenie i polimorfizm

11. Utwórz klasę bazową `Animal` i klasy dziedziczące `Dog`, `Cat`.
12. Nadpisz metodę `sound()` w klasach potomnych.
13. Napisz funkcję, która iteruje po liście zwierząt i wywołuje `sound()`.
14. Dodaj użycie `super()` w konstruktorze klasy potomnej.
15. Pokaż przykład polimorfizmu na klasach `Rectangle` i `Circle` z metodą `area()`.

## Poziom 4 — kompozycja i magic methods

16. Zamiast dziedziczenia zbuduj klasę `Car`, która ma silnik jako osobny obiekt.
17. Dodaj do klasy `Product` metodę `__repr__`.
18. Dodaj do klasy `Book` metodę `__str__`.
19. Dodaj do klasy `Point` metodę `__eq__`.
20. Dodaj do klasy `Cart` metodę `__len__`.

## Poziom 5 — bardziej zaawansowane OOP

21. Zaimplementuj prostą hierarchię pracowników z metodą `calculate_salary()`.
22. Napisz klasę `Temperature`, która używa property do walidacji ustawiania wartości.
23. Zbuduj prosty registry pattern przez atrybut klasowy i metody klasowe.
24. Zaimplementuj obiekt konfiguracyjny, który jest niemutowalny „umownie”.
25. Napisz przykład, w którym kompozycja jest lepsza niż dziedziczenie, i zaimplementuj oba podejścia.

## Zadanie końcowe

26. Zbuduj mini system biblioteki:
   - `Book`,
   - `User`,
   - `Library`,
   - wypożyczanie,
   - zwracanie,
   - liczenie dostępnych książek,
   - czytelne metody, sensowny podział klas, trochę polimorfizmu albo kompozycji.
