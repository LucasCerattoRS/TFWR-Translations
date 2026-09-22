[<- Speed Upgrade](docs/unlocks/speed.md) <right>[Carrots ->](docs/unlocks/carrots.md)
<right>[Debug ->](docs/scripting/debug.md)
<right>[Operators ->](docs/scripting/operators.md)
---
# Plant
Grass is nice because it grows automatically. All other plants have to be planted with the `plant()` function. The only plant you can plant right now is a bush.
You can pass the type of plant you want to plant to the function like this:

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
#CODE
plant(Entities.Bush)
}}

This will plant a bush under the drone.

Call `clear()` to reset the farm to all grass and reset the drone position.

It seems that if you grow more than one type of plant on the farm at the same time, you can sometimes get a higher yield. You'll need to research polyculture to learn more.

---

[Stats](docs/stats.md)      [If](docs/scripting/if.md)      [Senses](docs/unlocks/senses.md)      [Polyculture](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)
