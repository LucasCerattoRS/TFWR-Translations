[<- Quartz](docs/unlocks/quartz.md) <right>[Dynamite ->](docs/unlocks/dynamite.md)
---
# Mushroom

Many types of mushrooms grow in colonies underground. Look for a stratum of `Grounds.Mushroom` while digging. You can then `measure()` the ground to get the mushroom type as a number, starting from `0`.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 100}, {"item": "iron", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 6,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron"]
}

#SETUP
jump(Unlocks.Mushrooms)
#CODE
while get_ground_type() != Grounds.Mushroom:
    dig()
do_a_flip()
print(measure())
}}

Mushrooms of the same type like to be together, but they are a bit too shy to grow on top of each other. Push a mushroom block on top of another mushroom block of the same type and they will disappear, earning you mushrooms as a reward.

You can use `can_push(direction)` to check whether the block under the drone can be pushed and whether anything is blocking it in the given direction. `push(direction)` pushes the block and returns whether the push was successful.

Blocks cannot be pushed upward, and the push will fail if another block is in the way. When pushed into the air, blocks fall and land on the next block below them.

Remember that you can call `place(Grounds.Dirt)` to place blocks below the drone. This can be useful for filling in holes so that you can push blocks over them.

---

[Stats](docs/stats.md)      [Underground Senses](docs/unlocks/underground_senses.md)      [Dictionaries](docs/scripting/dicts.md)

[move()](functions/move)      [measure()](functions/measure)      [can_push()](functions/can_push)      [push()](functions/push)      [place()](functions/place)      [get_ground_type()](functions/get_ground_type)
