# Dev vs prod python

## O czym jest ten rozdział

Jedna z najczęstszych pomyłek w młodszych projektach brzmi mniej więcej tak:

- "skoro działa lokalnie w kontenerze, to produkcja powinna być prawie tym samym".

To bardzo niebezpieczne uproszczenie.

Development i produkcja mają część wspólną, ale ich cele nie są identyczne.

## Najprostsza intuicja

### Dev

Ma być wygodny, szybki do iteracji i przyjazny do debugowania.

### Prod

Ma być przewidywalny, bezpieczny, stabilny i operacyjnie sensowny.

To powoduje realne różnice w konfiguracji.

## Co zwykle jest ważne w dev

W developmentcie często chcesz:

- hot reload,
- głośniejsze logi,
- łatwy podgląd błędów,
- lokalne mounty kodu,
- szybsze eksperymenty,
- niższy koszt zmiany i restartu.

Czyli dev optymalizuje wygodę pracy.

## Co zwykle jest ważne w prod

W produkcji zwykle chcesz:

- debug wyłączony,
- przewidywalny start procesu,
- bezpieczniejsze ustawienia,
- sensowne logowanie i metryki,
- kontrolę zasobów,
- mniejszy obraz,
- stabilne dependency runtime,
- brak developerskich skrótów.

Czyli prod optymalizuje stabilność i bezpieczeństwo.

## Hot reload: dobry w dev, zły jako nawyk prodowy

W dev hot reload jest bardzo wygodny.

Pozwala:

- szybko zmieniać kod,
- nie budować wszystkiego od nowa,
- iterować bez ciągłego restartowania ręcznego.

Ale w produkcji takie zachowanie zwykle nie jest pożądane.

Tam chcesz bardziej kontrolowany model:

- zbudowany artefakt,
- przewidywalny start,
- brak zależności od lokalnych mountów kodu.

## Mounty kodu

W developmentcie często montujesz lokalny katalog do kontenera.

To świetne do pracy codziennej.

W produkcji zwykle chcesz uruchamiać gotowy obraz, a nie kontener zależny od zewnętrznego katalogu z hosta.

To bardzo ważna różnica mentalna.

## Logowanie i debug

### Dev

- więcej logów,
- stack trace na ekranie,
- łatwiejsze lokalne debugowanie.

### Prod

- logi muszą być użyteczne operacyjnie,
- nie powinny wyciekać wrażliwe informacje,
- debug mode nie powinien być włączony bez potrzeby.

## Sekrety i konfiguracja

W dev można mieć uproszczone lokalne sekrety testowe.

W prod:

- sekrety muszą pochodzić z bardziej bezpiecznego źródła,
- konfiguracja powinna być jawnie zarządzana,
- przypadkowy fallback do "dev default" może być bardzo groźny.

## Before/after

### Myślenie niedojrzałe

- ten sam układ ma działać wszędzie tak samo,
- debug i wygoda lokalna są ważniejsze niż bezpieczeństwo,
- produkcja jest traktowana jak większy laptop.

### Myślenie dojrzalsze

- dev i prod mają wspólny rdzeń, ale różne priorytety,
- development optymalizuje szybkość pracy,
- produkcja optymalizuje niezawodność i bezpieczeństwo.

## Typowe różnice konfiguracji

### Dev

- `DEBUG=true`,
- mount kodu,
- lokalna baza,
- luźniejsze logi,
- łatwe restartowanie.

### Prod

- `DEBUG=false`,
- gotowy obraz,
- twardsza kontrola env,
- bezpieczniejsze sekrety,
- osobna obserwowalność,
- bardziej świadome limity i restart policy.

## Mini case study: FastAPI w dev i prod

### Dev

- uruchamiasz aplikację z reloadem,
- kod jest montowany z hosta,
- łatwo oglądasz traceback.

### Prod

- uruchamiasz gotowy obraz,
- bez reload,
- z sensownym proces managerem lub serwerem aplikacyjnym,
- z bardziej przewidywalnymi logami i env.

To nie są kosmetyczne różnice. To inne cele środowiska.

## Mini case study: worker lokalny vs worker produkcyjny

### Dev worker

- może mieć prostszy lokalny broker,
- częściej restartujesz go ręcznie,
- łatwiej oglądasz pełne błędy.

### Prod worker

- musi być bardziej odporny,
- wymaga lepszych logów i metryk,
- retry i lag kolejki mają realne znaczenie biznesowe.

To pokazuje, że nawet przy tym samym kodzie operacyjna rzeczywistość jest inna.

## Częste pułapki

### 1. Przeniesienie debug ustawień do produkcji

To klasyczny błąd.

### 2. Zakładanie mountów kodu w środowisku, które powinno działać z gotowego obrazu

To osłabia przewidywalność.

### 3. Uproszczone sekrety i fallbacki z dev w prod

To bardzo groźne bezpieczeństwowo.

### 4. Brak myślenia o restartach, healthcheckach i obserwowalności w prod

Dev może sobie z tym poradzić. Produkcja niekoniecznie.

### 5. Traktowanie compose z local dev jako pełnej definicji produkcji

To częsta pułapka koncepcyjna.

## Co Pythonowiec powinien rozumieć

Dobrze, żebyś umiał:

- rozumieć, że dev i prod mają inne priorytety,
- wiedzieć, które wygody dev są złym pomysłem w prod,
- projektować konfigurację tak, żeby wspólny rdzeń był ten sam, ale szczegóły środowiska inne,
- nie mieszać debug, sekretów i modeli uruchomienia między środowiskami,
- myśleć o produkcji jako o środowisku o dużo wyższych wymaganiach operacyjnych.

## Output myślowy

### Dev traktowany jak prod 1:1

- lokalnie jest niewygodnie,
- albo produkcja staje się zbyt luźna i ryzykowna.

### Dev i prod świadomie rozdzielone

- lokalna praca jest wygodniejsza,
- produkcja jest bardziej przewidywalna,
- zespół lepiej rozumie, które różnice są celowe.

## Najważniejsze do zapamiętania

- Dev i prod nie mają identycznych celów.
- Dev optymalizuje szybkość iteracji, prod optymalizuje bezpieczeństwo i stabilność.
- Hot reload, mounty kodu i głośny debug to zwykle narzędzia devowe, nie produkcyjne.
- Produkcja powinna działać z gotowego artefaktu i lepszej kontroli środowiska.
- Świadome różnice między środowiskami to oznaka dojrzałości projektu, nie chaosu.

## Ćwiczenia

1. Wyjaśnij własnymi słowami, czemu dev i prod nie powinny być traktowane identycznie.
2. Wypisz trzy rzeczy dobre w dev, ale złe jako domyślny nawyk produkcyjny.
3. Opisz różnicę między kontenerem z mountem kodu a gotowym obrazem runtime.
4. Podaj dwa przykłady błędów wynikających z przeniesienia ustawień dev do prod.
5. Rozpisz własną checklistę różnic między środowiskiem developerskim i produkcyjnym.
