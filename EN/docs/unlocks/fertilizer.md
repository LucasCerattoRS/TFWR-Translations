[<- Watering](docs/unlocks/watering.md) <right>[Mazes ->](docs/unlocks/mazes.md)
---
# Fertilizer
At some point, waiting for plants to grow is no longer efficient enough.
As with water, you will automatically receive 1 fertilizer every 10 seconds. The amount doubles with each upgrade.

Fertilizer can make plants grow instantly. `use_item(Items.Fertilizer)` reduces the remaining growing time of the plant under the drone by 2 seconds.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "fertilizer", "n": 10}],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Tree)
use_item(Items.Fertilizer)
use_item(Items.Fertilizer)
use_item(Items.Fertilizer)
harvest()
}}

This has some side effects.
Plants grown with fertilizer will be infected.

When a plant is infected, half of its yield is turned into `Items.Weird_Substance` when it is harvested.
Weird Substance can also be used on plants, which has the effect of toggling the infected status of the plant and all adjacent plants.

If you call `use_item(Items.Weird_Substance)` on an infected plant, it will cure it; if you use it on a healthy plant, it will infect it.

If you use it on an infected plant that has healthy neighbors, it will cure the plant but infect the neighbors and vice versa.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
for _ in range(3):
    for _ in range(3):
        plant(Entities.Tree)
        move(East)
    move(North)

move(North)
move(East)

for _ in range(60):
    do_a_flip()
#CODE
for _ in range(6):
    use_item(Items.Weird_Substance)
    move(East)
}}

---

[Stats](docs/stats.md)      [Watering](docs/unlocks/watering.md)      [Mazes](docs/unlocks/mazes.md)

[use_item()](functions/use_item)
