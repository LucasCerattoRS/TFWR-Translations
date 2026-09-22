[<- Operators](docs/scripting/operators.md)
---
# Senses
The drone can see now! 

The functions `get_pos_x()` and `get_pos_y()` return the drone's current x- and y-coordinates. At the starting position, both are `0`. The x-coordinate increases by `1` for each tile toward `East`, and the y-coordinate increases by `1` for each tile toward `North`.

`num_items(item)` returns how many of an item you have.
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 10}],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
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
print(num_items(Items.Hay))
}}

`get_entity_type()` and `get_ground_type()` return the type of entity or ground that is under the drone.
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
plant(Entities.Bush)
#CODE
print(get_entity_type())
if get_entity_type() == Entities.Bush:
	do_a_flip()

print(get_ground_type())
if get_entity_type() != Grounds.Soil:
	do_a_flip()
}}

The `None` keyword is also unlocked now! `None` is a value that represents that there is no value.
For example, a function that has no `return` statement will actually return `None`.

`get_entity_type()` returns `None` if there is no entity under the drone.


If you want to find out how many of a particular unlock you have, use the `num_unlocked(unlock)` function.

For example, `num_unlocked(Unlocks.Speed)` will return the number of speed upgrades you have.

`num_unlocked(Unlocks.Senses)` will return `1` if senses are unlocked and `0` if they are not.

You can also use `num_unlocked()` on items or entities. It returns `1` if the item or entity is unlocked and `0` otherwise.

Be careful: `num_unlocked(Unlocks.Carrots)` returns the number of times the unlock was unlocked or upgraded.
`num_unlocked(Items.Carrot)` returns only `0` or `1`. The same applies to other plants.

---

[If](docs/scripting/if.md)      [Operators](docs/scripting/operators.md)      [Variables](docs/scripting/variables.md)      [Tuples](docs/scripting/tuples.md)      [Dictionaries](docs/scripting/dicts.md)      [Underground Senses](docs/unlocks/underground_senses.md)

[get_pos_x()](functions/get_pos_x)      [get_pos_y()](functions/get_pos_y)      [get_entity_type()](functions/get_entity_type)      [get_ground_type()](functions/get_ground_type)      [num_items()](functions/num_items)      [num_unlocked()](functions/num_unlocked)
