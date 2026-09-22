[<- Mining](docs/unlocks/mining.md)
---
# Underground Senses

Let's add a few sensors so your drone can find its way around underground.

You can now use `get_pos_z()` to get the drone's height (starting at 0 and becoming negative as the drone descends).

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
    "exclude_unlocks": ["watering", "fertilizer"],
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#CODE
move(North)
move(North)
move(East)
dig()
dig()
dig()
print(get_pos_z())
}}

`get_ground_type()` returns the type of ground under the drone. You can pass it a direction argument—for example, `get_ground_type(North)`—to get the ground type of a neighboring tile.

Here's how you would check if the block under the drone is dirt:

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
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#CODE
dig()
if get_ground_type() == Grounds.Dirt:
    do_a_flip()
}}


`get_hardness()` returns the hardness of the ground tile under the drone. You can pass it a direction argument, such as `get_hardness(North)`. The higher a tile's hardness, the longer it takes to dig.

`get_stability()` returns the stability of the ground tile under the drone. You can pass it a direction argument, such as `get_stability(North)`. A stability of 1 means that the block can withstand a height difference of 1 before it caves in.

Note that the four blocks directly next to the drone are removed regardless of their stability as the drone digs down, unless the block has a special function. Clay, iron, and quartz, for example, are not removed by this rule. They're still susceptible to cave-ins due to lack of block stability, however.
---

[Mining](docs/unlocks/mining.md)      [Senses](docs/unlocks/senses.md)

[get_pos_z()](functions/get_pos_z)      [get_ground_type()](functions/get_ground_type)      [get_hardness()](functions/get_hardness)      [get_stability()](functions/get_stability)
