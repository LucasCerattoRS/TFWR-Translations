[<- 植える](docs/unlocks/plant.md) <right>[水やり ->](docs/unlocks/watering.md)
<right>[木 ->](docs/unlocks/trees.md)
---
# ニンジン
`plant(Entities.Carrot)` でニンジンを植える前に、土を耕す必要があります。これにより、地面が `Grounds.Soil` に変わります。土を耕すには、単に `till()` を呼び出します。再度 `till()` を呼び出すと、`Grounds.Grassland` に戻ります。

ニンジンの植え付けには木材と干し草が必要です。これらのアイテムは `plant(Entities.Carrot)` を呼び出すと自動的に削除されます。
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

各植物のコストは、その[専用ページ](objects/carrot)で確認できます。

---

[統計](docs/stats.md)      [植える](docs/unlocks/plant.md)      [水やり](docs/unlocks/watering.md)      [if文](docs/scripting/if.md)      [感覚](docs/unlocks/senses.md)      [混作](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)
