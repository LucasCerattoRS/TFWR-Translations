[<- Lists](docs/scripting/lists.md) <right>[Costs ->](docs/unlocks/costs.md)
---
# Dictionaries
Dictionaries are a data structure that maps keys to values, much like a real dictionary maps words to their definitions. It allows you to look up these values very quickly.

A dictionary can be created like this:

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
right_of = {North:East, East:South, South:West, West:North}
}}

The expression before the colon is the key and the expression after the colon is the value to which the key maps.
The above dictionary maps each direction to the direction to its right.

Here's another dictionary that maps the drone's position to the entity beneath it.
{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}
}}

Accessing the value mapped to a key is similar to accessing an element in a list:
`value = dict[key]`

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
right_of = {North:East, East:South, South:West, West:North}
print(right_of[South])
}}

You can add a new key-value pair to a dictionary like this:
`dict[key] = value`

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
    "world_size": {"x": 3, "y": 1},
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
move(East)
plant(Entities.Bush)
move(East)
plant(Entities.Tree)
move(East)
#CODE
entity_dict = {}
for _ in range(3):
	entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()
	move(East)
print(entity_dict)
}}

Keys are unique, so adding a key that already exists in the dictionary will overwrite the previous value.

Use `dict.pop(key)` to remove a key-value pair from `dict`.

`key in dict` evaluates to `True` if `key` is a key in the `dict` and `False` otherwise.
So you can use `if key in dict:` to check if `dict` contains the key.

Putting a dictionary in a `for` loop allows you to iterate over all its keys:
{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
right_of = {North:East, East:South, South:West, West:North}
print(North in right_of)
for key in right_of:
	value = right_of[key]
	print(key, ":", value)
}}

There are no guarantees about the order in which the keys are iterated.

See also [Sets](docs/scripting/sets.md)

---

[Lists](docs/scripting/lists.md)      [Sets](docs/scripting/sets.md)      [Tuples](docs/scripting/tuples.md)      [Costs](docs/unlocks/costs.md)

[len()](functions/len)
