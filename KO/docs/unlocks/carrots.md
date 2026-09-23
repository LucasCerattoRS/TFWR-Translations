[<- 심기](docs/unlocks/plant.md) <right>[물주기 ->](docs/unlocks/watering.md)
<right>[나무 ->](docs/unlocks/trees.md)
---
# 당근
`plant(Entities.Carrot)`으로 당근을 심기 전에, 땅을 갈아야 해요. 그러면 땅이 `Grounds.Soil`로 바뀔 거예요. 땅을 갈려면 `till()`을 호출하면 돼요. `till()`을 다시 호출하면 `Grounds.Grassland`로 다시 바뀌어요.

당근을 심는 데는 나무와 건초가 들어요. 이 아이템들은 `plant(Entities.Carrot)`을 호출할 때 자동으로 제거돼요.

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

어떤 식물이든 그 비용은 [자체 페이지](objects/carrot)에서 볼 수 있어요.

---

[통계](docs/stats.md)      [심기](docs/unlocks/plant.md)      [물주기](docs/unlocks/watering.md)      [If문](docs/scripting/if.md)      [감각](docs/unlocks/senses.md)      [혼합 재배](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)
