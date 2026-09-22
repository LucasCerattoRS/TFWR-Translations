[<- Pierwsze kroki](docs/getting_started.md) <right>[Pętla While ->](docs/scripting/while.md)
---
# Pierwszy program
## Edytor tekstu
Wszystkie operacje programistyczne odbywają się w oknach kodu. Każde okno kodu odpowiada plikowi tekstowemu zawierającemu kod. 
Możesz zmienić nazwę pliku, klikając jego nazwę na górze okna.

Kod można edytować jak w każdym edytorze tekstu, o ile nie jest uruchomiony.
Możesz uruchomić program bezpośrednio, naciskając zielony przycisk odtwarzania w oknie kodu.
![|x50](PlayButton)

Możesz tworzyć więcej plików z kodem za pomocą przycisku "+" w prawym górnym rogu ekranu.
Możesz zadokować okno do innego okna, przeciągając je na nie.

Zauważysz, że po rozpoczęciu pisania pojawi się proste okno uzupełniania kodu.
Naciśnij Tab, aby wstawić wybrane uzupełnienie.
Użyj klawiszy strzałek, aby poruszać się po opcjach uzupełniania.

Nie martw się, jeśli programujesz po raz pierwszy. Język jest odblokowywany krok po kroku, więc nie zostaniesz przytłoczony wszystkimi rzeczami, które możesz zrobić. 
Składnia jest również podobna do Pythona, jednego z najczęściej używanych języków programowania na świecie, więc zdobyta tutaj wiedza przyda ci się także gdzie indziej.

Jeśli już znasz Pythona, to też w porządku: szybko przejdziesz przez początkową fazę gry i dotrzesz do ciekawszych rzeczy.

Obecnie dostępne są dwa polecenia drona.

`harvest()`

i 

`do_a_flip()`

Są to wywołania funkcji. Możesz myśleć o funkcji jak o poleceniu, które można wykonać. Nawiasy `()` je wykonują.

Spróbuj wpisać te instrukcje w oknie kodu i nacisnąć przycisk wykonania.

Możesz myśleć o swoim kodzie jako o sekwencji instrukcji. Aby uruchomić wiele instrukcji po kolei, umieść je w osobnych wierszach. 
Naciśnij przycisk odtwarzania w poniższym osadzonym oknie kodu, aby zobaczyć jego działanie:

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
do_a_flip()
harvest()
harvest()
}}

## Odblokowania
Zbieranie trawy da ci siano. Siana można użyć do odblokowania pętli w drzewku technologii. Otwórz drzewko technologii za pomocą przycisku w prawym górnym rogu ekranu.

---

[Zewnętrzny edytor](docs/external_editor.md)      [Komentarze](docs/scripting/comments.md)      [Pętla While](docs/scripting/while.md)

[harvest()](functions/harvest)      [do_a_flip()](functions/do_a_flip)
