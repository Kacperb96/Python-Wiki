# XML w Pythonie — `xml.etree.ElementTree`

## Spis treści

1. [Wprowadzenie](#wprowadzenie)
2. [Czym jest XML](#czym-jest-xml)
3. [Po co znać `ElementTree`](#po-co-znać-elementtree)
4. [Parsowanie XML](#parsowanie-xml)
5. [Elementy, atrybuty i tekst](#elementy-atrybuty-i-tekst)
6. [Wyszukiwanie elementów](#wyszukiwanie-elementów)
7. [Tworzenie XML](#tworzenie-xml)
8. [Zapis do pliku](#zapis-do-pliku)
9. [Typowe błędy początkujących](#typowe-błędy-początkujących)
10. [Praktyczne przykłady](#praktyczne-przykłady)
11. [Dobre praktyki](#dobre-praktyki)
12. [Podsumowanie](#podsumowanie)
13. [Mini ściąga](#mini-ściąga)
14. [Ćwiczenia](#ćwiczenia)
15. [Przykładowe rozwiązania](#przykładowe-rozwiązania)

---

## Wprowadzenie

Choć dziś często częściej spotyka się JSON, XML nadal pojawia się w wielu integracjach i starszych systemach.

W Pythonie podstawowym narzędziem do pracy z XML jest `xml.etree.ElementTree`.

---

## Czym jest XML

XML to format danych oparty o znaczniki.

Przykład:

```xml
<user id="1">
    <name>Anna</name>
</user>
```

---

## Po co znać `ElementTree`

Bo pozwala:

- parsować XML,
- czytać elementy i atrybuty,
- budować XML programowo,
- zapisywać XML do plików.

---

## Parsowanie XML

```python
import xml.etree.ElementTree as ET

tree = ET.parse("users.xml")
root = tree.getroot()
print(root.tag)
```

---

## Elementy, atrybuty i tekst

Przykład odczytu:

```python
for user in root.findall("user"):
    print(user.get("id"))
    print(user.find("name").text)
```

---

## Wyszukiwanie elementów

Najczęściej:

- `find()`
- `findall()`

To podstawowe narzędzia pracy z drzewem XML.

---

## Tworzenie XML

```python
import xml.etree.ElementTree as ET

root = ET.Element("users")
user = ET.SubElement(root, "user", id="1")
name = ET.SubElement(user, "name")
name.text = "Anna"
```

---

## Zapis do pliku

```python
tree = ET.ElementTree(root)
tree.write("users.xml", encoding="utf-8", xml_declaration=True)
```

---

## Typowe błędy początkujących

- mylenie atrybutów i tekstu elementu,
- brak sprawdzania, czy `find()` coś zwrócił,
- traktowanie XML jak JSON,
- ignorowanie kodowania przy zapisie.

---

## Praktyczne przykłady

### Odczyt użytkowników

```python
import xml.etree.ElementTree as ET

tree = ET.parse("users.xml")
root = tree.getroot()

for user in root.findall("user"):
    print(user.get("id"), user.find("name").text)
```

### Budowa prostego XML

```python
import xml.etree.ElementTree as ET

root = ET.Element("items")
item = ET.SubElement(root, "item")
item.text = "kawa"
```

---

## Dobre praktyki

- sprawdzaj strukturę XML, z którym pracujesz,
- ostrożnie obsługuj brakujące elementy,
- zapisuj z jawnym `encoding`,
- traktuj XML jako strukturę drzewa, a nie zwykły tekst.

---

## Podsumowanie

`xml.etree.ElementTree` to praktyczne narzędzie do podstawowej pracy z XML w Pythonie.

Warto je znać, bo XML nadal żyje w wielu realnych integracjach.

---

## Mini ściąga

```python
import xml.etree.ElementTree as ET

tree = ET.parse("plik.xml")
root = tree.getroot()
```

Najważniejsze:

- `parse()` wczytuje XML,
- `getroot()` zwraca korzeń,
- `find()` i `findall()` wyszukują elementy,
- `write()` zapisuje XML.

---

## Ćwiczenia

1. Wczytaj prosty plik XML.
2. Odczytaj tekst z elementu `name`.
3. Odczytaj atrybut `id`.
4. Utwórz prosty XML z jednym elementem.
5. Zapisz wynik do pliku.

---

## Przykładowe rozwiązania

### 1. Wczytanie

```python
import xml.etree.ElementTree as ET

tree = ET.parse("users.xml")
root = tree.getroot()
```

### 2. Tekst

```python
print(root.find("user/name").text)
```

### 3. Atrybut

```python
print(root.find("user").get("id"))
```

### 4. Utworzenie

```python
root = ET.Element("users")
ET.SubElement(root, "user", id="1")
```

### 5. Zapis

```python
ET.ElementTree(root).write("out.xml", encoding="utf-8", xml_declaration=True)
```
