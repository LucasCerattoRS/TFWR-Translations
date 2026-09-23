[<- Rice](docs/unlocks/rice.md) <right>[Colorful Blocks ->](docs/unlocks/debug_place.md)
<right>[Pyramids ->](docs/unlocks/pyramid.md)
---
# Bamboo

Bamboo is a plant that can grow up to 6 blocks tall. It won't grow while there is a drone above it, so make sure to `move` the drone after using `plant(Entities.Bamboo)`. Planting bamboo costs rice.

Bamboo produces flowers when it reaches a certain height, chosen randomly. Use `measure()` to check at which height it will flower. `measure()` starts counting at 0, so if the bamboo flowers on the second block, `measure()` returns 1:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 1000, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "rice", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
print(measure())
move(East)
}}

You will get max yield from bamboo when you `harvest()` while your drone is directly above the flower. For every block of difference from that, the yield will be divided by eight.
For example, if if its flower is at height 3 but you harvest it two blocks above that, the yield will be divided by 64.

To harvest flowers that are higher up, fly into the bamboo when the drone is at the desired height. The newly unlocked `place()` command helps with this.

Use `place(Grounds.Dirt)` to stack blocks next to the bamboo to climb up. Then use `move()` to fly into the bamboo from the side. Your drone should be directly above the flower when calling `harvest()`.

`place(Grounds.Dirt)` costs you 1 block! You can also place other grounds such as `Grounds.Rock`, but not special blocks such as `Grounds.Clay`.

Bamboo grows exactly 1 block per second.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 1000, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "block", "n": 100}, {"item": "rice", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
print(measure())
move(East)
place(Grounds.Dirt)
do_a_flip() # wait a bit
do_a_flip()
move(West)
harvest()
}}

---

[Stats](docs/stats.md)      [For Loop](docs/scripting/for.md)      [Variables](docs/scripting/variables.md)      [If](docs/scripting/if.md)      [Functions](docs/scripting/functions.md)      [Rice](docs/unlocks/rice.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [place()](functions/place)      [measure()](functions/measure)
