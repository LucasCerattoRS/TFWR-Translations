[<- Bergbau](docs/unlocks/mining.md) <right>[Bambus ->](docs/unlocks/bamboo.md)
<right>[Versteinerte Kürbisse ->](docs/unlocks/petrified_pumpkins.md)
<right>[Perlit und Lehmboden ->](docs/unlocks/special_soils.md)
---
# Reis

Unter der Oberfläche hast du eine dünne Tonschicht entdeckt. Wie sich herausstellt, eignet sich dieser fruchtbare Boden perfekt zum Pflanzen von Reissetzlingen.

Reis trocknet den Ton aus, auf dem er gepflanzt wurde. Du kannst jeden Tonblock nur einmal verwenden. Zum Glück ist die Schicht mehrere Blöcke dick. Und natürlich kannst du jederzeit mit `clear()` die Welt zurücksetzen, um die Tonschicht wiederherzustellen.

Der folgende Code könnte dir helfen, nach unten zu graben, bis du Ton findest.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "exclude_unlocks": ["watering", "fertilizer"],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 8,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#SETUP
move(East)
#CODE
while get_ground_type() != Grounds.Clay:
    dig()
plant(Entities.Rice)
move(North)
do_a_flip()
}}

---

[Statistiken](docs/stats.md)      [Bergbau](docs/unlocks/mining.md)      [Unterirdische Sinne](docs/unlocks/underground_senses.md)      [If](docs/scripting/if.md)      [For-Schleife](docs/scripting/for.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)
