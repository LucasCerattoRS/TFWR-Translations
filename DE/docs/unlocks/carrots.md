[<- Pflanzen](docs/unlocks/plant.md) <right>[Bewässerung ->](docs/unlocks/watering.md)
<right>[Bäume ->](docs/unlocks/trees.md)
---
# Karotten
Bevor du mit `plant(Entities.Carrot)` Karotten pflanzen kannst, musst du den Boden pflügen. Dadurch wird der Boden zu `Grounds.Soil`. Um den Boden zu pflügen, rufe einfach `till()` auf. Ein erneuter Aufruf von `till()` ändert ihn wieder in `Grounds.Grassland`.

Das Pflanzen von Karotten kostet Holz und Heu. Diese Gegenstände werden automatisch entfernt, wenn du `plant(Entities.Carrot)` aufrufst.
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
    "items": [{"item": "hay", "n": 1}, {"item": "wood", "n": 1}],
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
#CODE
till()
plant(Entities.Carrot)
for _ in range(8):
    do_a_flip()
harvest()
till()
}}

Die Kosten jeder Pflanze findest du auf ihrer [eigenen Seite](objects/carrot).

---

[Statistiken](docs/stats.md)      [Pflanzen](docs/unlocks/plant.md)      [Bewässerung](docs/unlocks/watering.md)      [If](docs/scripting/if.md)      [Sinne](docs/unlocks/senses.md)      [Polykultur](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)
