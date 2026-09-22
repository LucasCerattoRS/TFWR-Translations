[<- Pumpkins](docs/unlocks/pumpkins.md)
---
# Polyculture
You may have already noticed that sometimes plants yield more when planted together.
Grass, bushes, trees, and carrots yield more when they have the right plant companion. Companion preference is different for each individual plant and cannot be predicted. Fortunately, the companion preference of the plant under the drone can be measured using `get_companion()`. It returns a tuple where the first element is the type of plant it wants as its companion and the second element is the position where it wants its companion. The companion doesn't need to be fully grown to get the yield bonus.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Bush)
plant_type, (x, y) = get_companion()
print(plant_type, (x, y))
move(East)
move(South)
plant(plant_type)
move(West)
move(North)
do_a_flip()
harvest()
}}

A plant's companion preference can be `Entities.Grass`, `Entities.Bush`, `Entities.Tree`, or `Entities.Carrot`. Each plant chooses randomly, but it will always choose a different type of plant from itself. The position can be anywhere within 3 moves of the plant except the plant's own position.

If there is no plant with a companion preference under the drone, `get_companion()` returns `None`.

When polyculture is first unlocked, the yield multiplier is `5`. It doubles every time you upgrade it.

---

[Stats](docs/stats.md)      [Tuples](docs/scripting/tuples.md)      [Dictionaries](docs/scripting/dicts.md)      [Senses](docs/unlocks/senses.md)      [Plant](docs/unlocks/plant.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [get_companion()](functions/get_companion)
