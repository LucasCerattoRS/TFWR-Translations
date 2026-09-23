[<- 호박](docs/unlocks/pumpkins.md)
---
# 혼합 재배
때때로 식물들이 함께 심어졌을 때 더 많은 수확량을 낸다는 것을 이미 눈치챘을 수도 있어요.
풀, 덤불, 나무, 당근은 올바른 동반 식물이 있을 때 더 많은 수확량을 내요. 동반 식물 선호도는 각 개별 식물마다 다르며 예측할 수 없어요. 다행히 드론 아래 식물의 동반 식물 선호도는 `get_companion()`으로 측정할 수 있어요. 첫 번째 요소가 원하는 동반 식물의 종류이고 두 번째 요소가 그 동반 식물을 원하는 위치인 튜플을 반환해요. 수확량 보너스를 받으려면 동반 식물이 다 자라 있을 필요는 없어요.

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

식물의 동반 식물 선호도는 `Entities.Grass`, `Entities.Bush`, `Entities.Tree` 또는 `Entities.Carrot` 중 하나일 수 있어요. 각 식물은 이것을 무작위로 선택하지만, 항상 자신과 다른 식물을 선택할 거예요. 위치는 식물 자체 위치를 제외하고 식물로부터 3번 이동 이내의 어떤 위치든 될 수 있어요.

드론 아래에 동반 식물 선호도가 있는 식물이 없으면 `get_companion()`은 `None`을 반환할 거예요.

혼합 재배를 처음 해금하기 전에는 수확량 배율이 `5`예요. 업그레이드할 때마다 두 배가 돼요.

---

[통계](docs/stats.md)      [튜플](docs/scripting/tuples.md)      [딕셔너리](docs/scripting/dicts.md)      [감각](docs/unlocks/senses.md)      [심기](docs/unlocks/plant.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [get_companion()](functions/get_companion)
