[<- Ekspansja 2](docs/unlocks/expand_2.md)
---
# Pętla For
Pętla `for` działa tak samo jak w Pythonie. W niektórych językach nazywa się ją pętlą foreach; nie należy jej mylić z pętlą for w stylu C, która działa inaczej.

`for i in sequence:
	#zrób coś z i`

Podobnie jak pętla `while`, pętla `for` również wielokrotnie wywołuje blok kodu. Zamiast pętli opartej na warunku, wykonuje ciało pętli raz dla każdego elementu w sekwencji.

## Składnia
Pętla for wygląda tak:

`for nazwa_zmiennej in sekwencja:
	#blok kodu`

`nazwa_zmiennej` może być dowolną wybraną przez ciebie nazwą. Jest to zmienna przechowująca bieżący element sekwencji. `sekwencja` musi być wartością iterowalną, na przykład zakresem liczb. Blok kodu jest wykonywany raz dla każdego elementu, a zmienna pętli otrzymuje wartość tego elementu.

## Sekwencje
[Zakresy](functions/range)      <unlock=lists>[Listy](docs/scripting/lists.md)      </unlock><unlock=functions>[Krotki](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Słowniki](docs/scripting/dicts.md)      </unlock><unlock=sets>[Zbiory](docs/scripting/sets.md)</unlock>

## Przykład
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
for i in range(5):
    harvest()
}}

Ta pętla wykonuje ciało określoną liczbę razy. Jest to w zasadzie to samo, co napisanie

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
i = 0
harvest()
i = 1
harvest()
i = 2
harvest()
i = 3
harvest()
i = 4
harvest()
}}


---

[Pętla While](docs/scripting/while.md)      [Break](docs/scripting/break.md)      [Continue](docs/scripting/continue.md)

[range()](functions/range)
