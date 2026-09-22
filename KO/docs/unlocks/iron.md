[<- 석탄](docs/unlocks/coal.md) <right>[수정 ->](docs/unlocks/quartz.md)
<right>[철 탐사 ->](docs/unlocks/prospecting.md)
<right>[보물지도 ->](docs/unlocks/treasure_map.md)
---
# 철

점토 아래의 암석층에서 철 광맥을 발견했어요.

철 광맥은 처음엔 작고, 찾으려면 운이 조금 필요해요. 이 해금의 레벨이 올라가면 광맥의 최대 크기가 커져요. 철을 더 안정적으로 찾고 싶다면 철 탐사 해금도 확인해 보세요.

철 광맥은 대각선으로 뛰지 않고 항상 연속되어 있어요. 철 조각을 찾았다면 아래쪽이나 옆쪽에 더 있는지 살펴 광맥 전체를 모두 캐내세요.

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

[통계](docs/stats.md)      [채광](docs/unlocks/mining.md)      [철 탐사](docs/unlocks/prospecting.md)      [지하 감각](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)
