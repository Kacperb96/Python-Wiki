# 04. Programowanie obiektowe

Ten dział wprowadza OOP w sensownej kolejności: od klas i obiektów do bardziej zaawansowanych mechanizmów.

Po tym dziale powinieneś rozumieć:

- klasy i obiekty,
- `__init__`,
- atrybuty instancji i klasy,
- hermetyzację,
- dziedziczenie,
- polimorfizm,
- kompozycję,
- klasy abstrakcyjne i `@abstractmethod`,
- magic methods,
- podstawy metaklas.

Czytaj po kolei od `01-...` do `08-...`.

---

## Po co w ogóle ten dział

Programowanie obiektowe nie jest po to, żeby "robić klasy dla zasady".

To narzędzie, które pomaga:

- grupować dane i zachowanie w jednym miejscu,
- modelować obiekty świata programu,
- ograniczać chaos w większym kodzie,
- budować kod, który łatwiej rozwijać.

Jeśli dobrze zrozumiesz OOP, łatwiej będzie Ci później czytać:

- frameworki webowe,
- biblioteki,
- większe projekty,
- kod innych programistów.

---

## Jak czytać ten dział

Najlepiej iść dokładnie po kolei:

1. klasy, obiekty i metody,
2. `__init__`, atrybuty instancji i klasy,
3. hermetyzacja,
4. dziedziczenie i `super()`,
5. polimorfizm,
6. kompozycja vs dziedziczenie,
7. klasy abstrakcyjne i `@abstractmethod`,
8. magic methods,
9. metaklasy.

Ta kolejność ma znaczenie.

Nie warto przeskakiwać od razu do magic methods czy metaklas, jeśli nie czujesz jeszcze klas, atrybutów i dziedziczenia.

---

## Na co szczególnie uważać

W OOP początkujący najczęściej wpadają w te pułapki:

- tworzenie klas tam, gdzie zwykła funkcja i słownik byłyby prostsze,
- mylenie klasy z obiektem,
- brak zrozumienia roli `self`,
- wrzucanie całej logiki do `__init__`,
- nadużywanie dziedziczenia,
- traktowanie OOP jak “ładniejszej składni”, a nie sposobu modelowania problemu.

To bardzo ważny dział, ale też taki, w którym łatwo zacząć pisać kod “bardziej skomplikowany niż trzeba”.

---

## Po czym poznać, że OOP zaczyna siedzieć

Dobry znak to sytuacja, w której potrafisz:

- napisać prostą klasę z sensownymi atrybutami i metodami,
- odróżnić atrybut klasy od atrybutu instancji,
- wyjaśnić, po co użyć `super()`,
- pokazać przykład polimorfizmu bez sztucznego komplikowania,
- powiedzieć, kiedy kompozycja jest lepsza niż dziedziczenie,
- wyjaśnić, kiedy `ABC` ma sens, a kiedy byłoby przesadą,
- napisać `__repr__`, `__str__`, `__len__` albo `__eq__` w prostym obiekcie.

---

## Jak najlepiej ćwiczyć

W tym dziale najlepiej działają małe modele domenowe:

- `User`,
- `Book`,
- `Cart`,
- `BankAccount`,
- `Dog`,
- `Order`,
- `Library`.

Czyli nie abstrakcyjne klasy “A”, “B”, “C”, tylko coś, co naprawdę modeluje dane i zachowanie.

---

Co dalej:

- przejdź do [05. Dekoratory](/home/kacper/Desktop/Python/05.%20Dekoratory)
- potem do [06. Zaawansowane elementy](/home/kacper/Desktop/Python/06.%20Zaawansowane%20elementy)
