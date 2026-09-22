[<- Ulepszenie prędkości](docs/unlocks/speed.md) <right>[Ekspansja 2 ->](docs/unlocks/expand_2.md)
<right>[Górnictwo ->](docs/unlocks/mining.md)
---
# Ekspansja 1
Twoja farma urosła! Ta przestrzeń nie jest zbyt użyteczna, jeśli nie możesz poruszać dronem, więc dostępna jest nowa funkcja `move()`, która go przesuwa. `move()` wymaga wskazania kierunku ruchu drona. Służą do tego cztery nowe stałe: `North, East, South, West`

Na przykład, `move(North)` przesunie drona o jedno pole na północ.

Jeśli wyjdziesz poza krawędź farmy, dron pojawi się po jej drugiej stronie.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 3},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	move(North)
}}

---

[Pętla While](docs/scripting/while.md)      [Operatory](docs/scripting/operators.md)      [Ekspansja 2](docs/unlocks/expand_2.md)

[move()](functions/move)
