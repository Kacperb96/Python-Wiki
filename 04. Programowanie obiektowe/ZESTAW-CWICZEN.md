# Zestaw ćwiczeń praktycznych — 04. Programowanie obiektowe

## Poziom 1 — klasy i obiekty

1. Utwórz klasę `Dog` z atrybutami `name` i `age`.
2. Dodaj metodę `bark()` zwracającą prosty komunikat.
3. Utwórz kilka obiektów tej klasy i wypisz ich dane.
4. Utwórz klasę `User` z `__init__`.
5. Dodaj metodę `full_info()` zwracającą string z danymi użytkownika.
6. Utwórz klasę `Car`, która ma markę i model oraz metodę `describe()`.
7. Utwórz dwie instancje tej samej klasy i pokaż, że mogą mieć różne dane.

## Poziom 2 — atrybuty, klasy, enkapsulacja

8. Dodaj atrybut klasowy `species` do klasy `Dog`.
9. Zrób licznik wszystkich utworzonych obiektów klasy `User`.
10. Utwórz klasę `BankAccount` z metodami `deposit()` i `withdraw()`.
11. Zabezpiecz wypłatę przed zejściem poniżej zera.
12. Zasymuluj atrybut „wewnętrzny”, którego nie chcesz dotykać bezpośrednio.
13. Pokaż różnicę między atrybutem klasy i instancji na własnym przykładzie.
14. Dodaj do klasy `Temperature` property, które nie pozwala ustawić wartości poniżej zera bez uzasadnienia w modelu.

## Poziom 3 — dziedziczenie i polimorfizm

15. Utwórz klasę bazową `Animal` i klasy dziedziczące `Dog`, `Cat`.
16. Nadpisz metodę `sound()` w klasach potomnych.
17. Napisz funkcję, która iteruje po liście zwierząt i wywołuje `sound()`.
18. Dodaj użycie `super()` w konstruktorze klasy potomnej.
19. Pokaż przykład polimorfizmu na klasach `Rectangle` i `Circle` z metodą `area()`.
20. Napisz klasę `Employee` i klasy potomne `Developer`, `Manager`, które różnie liczą pensję.

## Poziom 4 — kompozycja i magic methods

21. Zamiast dziedziczenia zbuduj klasę `Car`, która ma silnik jako osobny obiekt.
22. Dodaj do klasy `Product` metodę `__repr__`.
23. Dodaj do klasy `Book` metodę `__str__`.
24. Dodaj do klasy `Point` metodę `__eq__`.
25. Dodaj do klasy `Cart` metodę `__len__`.
26. Dodaj do własnej klasy `__contains__`.
27. Zbuduj klasę, która wspiera indeksowanie przez `__getitem__`.

## Poziom 5 — bardziej zaawansowane OOP

28. Zaimplementuj prostą hierarchię pracowników z metodą `calculate_salary()`.
29. Napisz klasę `Temperature`, która używa property do walidacji ustawiania wartości.
30. Zbuduj prosty registry pattern przez atrybut klasowy i metody klasowe.
31. Zaimplementuj obiekt konfiguracyjny, który jest niemutowalny „umownie”.
32. Napisz przykład, w którym kompozycja jest lepsza niż dziedziczenie, i zaimplementuj oba podejścia.
33. Zbuduj klasę `LibraryUser`, która przechowuje historię wypożyczeń jako osobny obiekt, a nie przez dziedziczenie.
34. Napisz klasę bazową i dwie klasy potomne, a potem wskaż, co jest współdzielone, a co nadpisane.
35. Zbuduj abstrakcyjną klasę `Shape` z metodą `area()`.
36. Utwórz klasy `Rectangle` i `Circle`, które implementują `area()`.
37. Pokaż, co się stanie, gdy spróbujesz utworzyć obiekt klasy abstrakcyjnej.
38. Zbuduj abstrakcyjną klasę `Notifier` z metodą `send(message)`.
39. Opisz, kiedy `ABC` ma sens, a kiedy byłoby przesadą.

## Poziom 6 — zadania przekrojowe

40. Zbuduj model sklepu:
   - `Product`,
   - `Cart`,
   - `User`,
   - metody dodawania produktów,
   - liczenie długości koszyka,
   - czytelny `__repr__`.
41. Zbuduj model biblioteki:
   - `Book`,
   - `Author`,
   - `Library`,
   - wypożyczenia,
   - zwroty,
   - sprawdzanie dostępności.
42. Zbuduj prosty system kont bankowych:
   - klasa bazowa konta,
   - konto oszczędnościowe,
   - konto firmowe,
   - polimorficzne liczenie opłat lub salda.
43. Zrób dwa rozwiązania tego samego problemu:
   - przez dziedziczenie,
   - przez kompozycję,
   i napisz, które jest lepsze i dlaczego.
44. Zbuduj mini system powiadomień:
   - abstrakcyjna klasa `Notifier`,
   - implementacje `EmailNotifier` i `SmsNotifier`,
   - wspólny kod w bazie,
   - metoda abstrakcyjna wymuszana przez `@abstractmethod`.

## Zadanie końcowe

45. Zbuduj mini system biblioteki:
   - `Book`,
   - `User`,
   - `Library`,
   - wypożyczanie,
   - zwracanie,
   - liczenie dostępnych książek,
   - czytelne metody,
   - sensowny podział klas,
   - trochę polimorfizmu albo kompozycji,
   - przynajmniej jedną metodę specjalną,
   - i jedną abstrakcyjną bazę, jeśli ma to realny sens.
