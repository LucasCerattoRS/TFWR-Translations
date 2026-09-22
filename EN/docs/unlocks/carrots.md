[<- Plant](docs/unlocks/plant.md) <right>[Watering ->](docs/unlocks/watering.md)
<right>[Trees ->](docs/unlocks/trees.md)
---
# Carrots
Before you can plant carrots with `plant(Entities.Carrot)`, you have to till the soil. This will change the ground to `Grounds.Soil`. To till the soil, simply call `till()`. Calling `till()` again will change it back to `Grounds.Grassland`.

Planting carrots costs wood and hay. These items will be automatically removed when calling `plant(Entities.Carrot)`.
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
    "items": [{"item": "hay", "n": 1}, {"item": "wood", "n": 1}],
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
#CODE
till()
plant(Entities.Carrot)
for _ in range(8):
    do_a_flip()
harvest()
till()
}}

You can see the cost of any plant on its [own page](objects/carrot).

---

[Stats](docs/stats.md)      [Plant](docs/unlocks/plant.md)      [Watering](docs/unlocks/watering.md)      [If](docs/scripting/if.md)      [Senses](docs/unlocks/senses.md)      [Polyculture](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)
