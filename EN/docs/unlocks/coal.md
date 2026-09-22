[<- Mining](docs/unlocks/mining.md) <right>[Iron ->](docs/unlocks/iron.md)
<right>[Jumping ->](docs/unlocks/jump.md)
---
# Coal

It turns out that the ground right underneath the surface is a good place to find coal deposits.

Coal spawns randomly in horizontal sheets that are 1 block thick. The sheet size will grow in proportion to your world size, so you may want to increase it to find more coal!

The following program is a good starting point for finding coal. It digs down in search of a coal sheet, then digs to its east and west in hopes of finding more coal.

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
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 4,
    "digging_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 2
}
#SETUP
move(North)
move(East)
move(East)
#CODE
while get_ground_type() != Grounds.Coal:
    dig()
dig()
move(East)
dig()
move(West)
move(West)
dig()
}}

---

[Stats](docs/stats.md)      [Mining](docs/unlocks/mining.md)      [Underground Senses](docs/unlocks/underground_senses.md)

[move()](functions/move)      [get_ground_type()](functions/get_ground_type)      [dig()](functions/dig)
