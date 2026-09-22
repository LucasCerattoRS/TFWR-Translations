[<- Coal](docs/unlocks/coal.md) <right>[Quartz ->](docs/unlocks/quartz.md)
<right>[Iron Prospecting ->](docs/unlocks/prospecting.md)
<right>[Treasure Map ->](docs/unlocks/treasure_map.md)
---
# Iron

You've discovered iron veins in the stone layer below the clay.

Iron veins start small and you'll need some luck to find them. As you gain higher levels in this unlock, the maximum size of an ore vein increases. For a more consistent way to find iron, you may also want to look at the ore prospecting unlock.

An iron vein is always continuous, with no diagonal jumps. If you find a piece of iron, look for more below or next to it to ensure you collect the whole vein.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 1,
    "digging_speed": 4,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz"]
}
#SETUP
jump(Unlocks.Iron)
#CODE
for i in range(4):
    dig()
do_a_flip()
}}

---

[Stats](docs/stats.md)      [Mining](docs/unlocks/mining.md)      [Iron Prospecting](docs/unlocks/prospecting.md)      [Underground Senses](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)
