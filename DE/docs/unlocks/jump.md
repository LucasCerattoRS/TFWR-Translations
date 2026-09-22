[<- Kohle](docs/unlocks/coal.md)
---
# Springen

Deine Drohne hat den Befehl `jump()` freigeschaltet.

Mit diesem Befehl kannst du bestimmte Freischaltungen anvisieren und direkt zu ihnen springen. Das ist besonders beim Debuggen praktisch oder wenn du zu einer Erzader zurückspringen möchtest, die du kurz zuvor verpasst hast. Übergib dazu eine Freischaltung als Argument, beispielsweise `Unlocks.Iron`.

`jump()` funktioniert nur mit Freischaltungen, die unterirdisch vorkommen, beispielsweise `jump(Unlocks.Rice)` oder `jump(Unlocks.Iron)`.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 3,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms"],
    "starting_chunk": 0
}
#CODE
dig()
dig()
dig()
jump(Unlocks.Iron)
do_a_flip()
}}

Ein Sprung bringt dich nicht garantiert direkt zur anvisierten Freischaltung. Möglicherweise musst du noch ein wenig in der Umgebung suchen, das Ziel befindet sich aber garantiert in der Nähe.

`jump()` kann pro Programmausführung nur einmal verwendet werden.

---

[jump()](functions/jump)
