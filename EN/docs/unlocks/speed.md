[<- While Loop](docs/scripting/while.md) <right>[Expand 1 ->](docs/unlocks/expand_1.md)
<right>[Plant ->](docs/unlocks/plant.md)
---
# Speed Upgrade
The execution speed has doubled. The problem is that the drone now harvests faster than the grass can grow, resulting in no yield at all. To deal with this, [if](docs/scripting/if.md) branches and the [can_harvest()](functions/can_harvest) function are now unlocked.

## Checking Before Harvesting
An `if` statement runs its code block once if the given condition is `True`.

The new function `can_harvest()` provides a useful condition. `can_harvest()` returns `True` if the plant under the drone can be harvested and `False` otherwise.

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
    "items": [],
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
do_a_flip()
#CODE
if can_harvest():
	do_a_flip()
}}

You can think of a return value like this as if the function call expression `can_harvest()` gets replaced by the returned value `True` during the evaluation of the `if`.

What happens when the above code runs:
- The `if` statement runs.
- `can_harvest()` is called.
- `can_harvest()` returns `True` because the grass is fully grown.
- The statement is now `if True:`.
- The branch executes because the value is `True`.

If the grass wasn't fully grown it would not do a flip.

Now we can use `if` to prevent the drone from harvesting too early.

---

[If](docs/scripting/if.md)      [While Loop](docs/scripting/while.md)

[harvest()](functions/harvest)      [can_harvest()](functions/can_harvest)
