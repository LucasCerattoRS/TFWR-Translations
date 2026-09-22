[<- Speed Upgrade](docs/unlocks/speed.md) <right>[Expand 2 ->](docs/unlocks/expand_2.md)
<right>[Mining ->](docs/unlocks/mining.md)
---
# Expand 1
Your farm has grown! This space is not much use if you can't move the drone, so there is a new function `move()` that moves the drone. `move()` requires that you specify the direction in which you want the drone to move. There are four new constants for this: `North, East, South, West`

For example, `move(North)` will move the drone one square to the north.

If you move over the edge of the farm, the drone will wrap around to the other side.

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

[While Loop](docs/scripting/while.md)      [Operators](docs/scripting/operators.md)      [Expand 2](docs/unlocks/expand_2.md)

[move()](functions/move)
