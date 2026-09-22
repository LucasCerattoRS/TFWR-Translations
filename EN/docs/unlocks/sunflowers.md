[<- Watering](docs/unlocks/watering.md)
---
# Sunflowers
[Sunflowers](objects/sunflower) collect the power of the sun. You can harvest that power. 

Planting them works exactly like planting carrots or pumpkins. 

Harvesting a grown sunflower yields power.
If there are at least 10 sunflowers on the farm and you harvest one with the largest number of petals, you get `8` times more power!
If you harvest a sunflower while there is another sunflower with more petals, the next sunflower you harvest will also only give you the normal amount of power (not the 8x bonus).

`measure()` returns the number of petals of the sunflower under the drone.
Sunflowers have at least `7` and at most `15` petals.
Even before they are fully grown, sunflowers can already be measured and count towards the 10 sunflower limit.

Several sunflowers can have the same number of petals, so there may be several with the largest number. In this case, it doesn't matter which one you harvest.

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "inventory_scale": 5,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "carrot", "n": 10}],
    "world_size": {"x": 5, "y": 2},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 4,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(North)
for _ in range(5):
    till()
    plant(Entities.Sunflower)
    move(East)
move(North)
do_a_flip()
do_a_flip()
do_a_flip()
do_a_flip()
do_a_flip()
#CODE
for _ in range(5):
    till()
    plant(Entities.Sunflower)
    print(measure())
    move(East)
for _ in range(5):
    while not can_harvest():
        pass
    harvest()
    move(East)
}}

As long as you have power, the drone will use it to run twice as fast.
It consumes 1 power every 30 actions, such as moves, harvests, or planting actions.
Executing other code statements can also use power, but much less than drone actions.

In general, everything that is sped up by speed upgrades is also sped up by power.
Anything sped up by power also uses power proportional to the time it takes to execute it, ignoring speed upgrades.

---

[Stats](docs/stats.md)      [Lists](docs/scripting/lists.md)      [Dictionaries](docs/scripting/dicts.md)      [Variables](docs/scripting/variables.md)      [For Loop](docs/scripting/for.md)      [If](docs/scripting/if.md)      [Operators](docs/scripting/operators.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [measure()](functions/measure)
