[<- Geschwindigkeits-Upgrade](docs/unlocks/speed.md) <right>[Erweitern 2 ->](docs/unlocks/expand_2.md)
<right>[Bergbau ->](docs/unlocks/mining.md)
---
# Erweitern 1
Deine Farm ist gewachsen! Der zusätzliche Platz nützt wenig, wenn du die Drohne nicht bewegen kannst. Deshalb gibt es die neue Funktion `move()`, welche die Drohne bewegt. Bei `move()` musst du die gewünschte Bewegungsrichtung angeben. Dafür gibt es vier neue Konstanten: `North, East, South, West`

Zum Beispiel wird `move(North)` die Drohne ein Feld nach Norden bewegen.

Wenn du dich über den Rand der Farm hinausbewegst, erscheint die Drohne auf der gegenüberliegenden Seite.

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

[While-Schleife](docs/scripting/while.md)      [Operatoren](docs/scripting/operators.md)      [Erweitern 2](docs/unlocks/expand_2.md)

[move()](functions/move)
