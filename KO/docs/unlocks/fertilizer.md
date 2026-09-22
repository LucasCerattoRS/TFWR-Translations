[<- 물주기](docs/unlocks/watering.md) <right>[미로 ->](docs/unlocks/mazes.md)
---
# 비료
어느 시점부터는 식물이 자라기를 기다리는 것이 더 이상 효율적이지 않아요. 
물과 비슷하게, 10초마다 자동으로 비료 1개를 받으며, 업그레이드할 때마다 그 양이 두 배가 돼요.

비료는 식물이 즉시 자라게 할 수 있어요. `use_item(Items.Fertilizer)`는 드론 아래 식물의 남은 성장 시간을 2초 줄여줘요.

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

이것은 몇 가지 부작용이 있어요.
비료로 자란 식물은 감염돼요.

식물이 감염되면, 수확할 때 수확량의 절반이 `Items.Weird_Substance`로 바뀌어요.
기묘한 물질은 식물에도 사용할 수 있는데, 식물과 모든 인접한 식물의 감염 상태를 토글하는 효과가 있어요.

따라서 감염된 식물에 `use_item(Items.Weird_Substance)`를 호출하면 치료되지만, 건강한 식물에 사용하면 감염시켜요.

건강한 이웃이 있는 감염된 식물에 사용하면, 그 식물은 치료되지만 이웃은 감염되고, 그 반대도 마찬가지예요.

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

[통계](docs/stats.md)      [물주기](docs/unlocks/watering.md)      [미로](docs/unlocks/mazes.md)

[use_item()](functions/use_item)
