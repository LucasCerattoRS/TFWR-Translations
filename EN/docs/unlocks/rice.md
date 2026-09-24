[<- Mining](docs/unlocks/mining.md) <right>[Bamboo ->](docs/unlocks/bamboo.md)
<right>[Petrified Pumpkins ->](docs/unlocks/petrified_pumpkins.md)
<right>[Perlite and Loam ->](docs/unlocks/special_soils.md)
---
# Rice

Underneath the surface you have noticed a thin sheet of clay. As it turns out, this fertile ground is perfect for planting rice seedlings.

Rice will dry out the clay it was planted on. You can only use each clay block once. Luckily, the sheet is a few blocks thick. And of course, you can always just `clear()` the world to get the clay sheet back.

You might find the following code useful to dig down until you find clay.

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

[Stats](docs/stats.md)      [Mining](docs/unlocks/mining.md)      [Underground Senses](docs/unlocks/underground_senses.md)      [If](docs/scripting/if.md)      [For Loop](docs/scripting/for.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)
