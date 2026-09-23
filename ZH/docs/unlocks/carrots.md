[<- 种植](docs/unlocks/plant.md) <right>[浇水 ->](docs/unlocks/watering.md)
<right>[树 ->](docs/unlocks/trees.md)
---
# 胡萝卜
调用 `plant(Entities.Carrot)` 函数可以种植胡萝卜。在种植胡萝卜之前你必须先耕地，只需调用 `till()` 函数即可耕地，将地块变为 `Grounds.Soil` 。再次调用 `till()` 则会将地块变回 `Grounds.Grassland`。


种植胡萝卜所需的耗材是干草和木材。请注意：调用 `plant(Entities.Carrot)` 函数种植胡萝卜时，这些耗材（干草和木材）会被消耗一定数量。

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

你可以在所有植物的[专属页面](objects/carrot)上查看所需的耗材数量。

---

[统计数据](docs/stats.md)      [种植](docs/unlocks/plant.md)      [浇水](docs/unlocks/watering.md)      [If 语句](docs/scripting/if.md)      [感官](docs/unlocks/senses.md)      [混合种植](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)
