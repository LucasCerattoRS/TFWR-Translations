[<- 철](docs/unlocks/iron.md) <right>[버섯 ->](docs/unlocks/mushroom.md)
---
# 수정

수정은 암석층 바닥 부근과 그 아래의 단단한 흙에서 바늘 모양의 광맥으로 자라요. 광맥은 수직 기둥을 이루므로 마구 파서 찾기가 꽤 어려워요.

다행히 철을 구부러뜨려 수정 광맥을 더 쉽게 찾게 해주는 탐지봉과 비슷한 걸 만들 수 있어요. 이 명령은 `prospect_quartz()`예요.

`prospect_quartz()`는 `prospect_iron()`과 다르게 작동해요. 가장 가까운 수정 광석의 방향 대신 가장 가까운 수정까지의 유클리드 거리(3차원 거리)를 반환해요. `prospect_quartz()`를 실행하면 철 1개를 소모하므로 명령을 아껴 쓰는 것이 좋을 수 있어요.

`prospect_quartz()`가 근처에서 수정을 찾지 못하거나 탐사할 철이 부족하면 `None`을 반환해요.

다음 코드를 사용하면 드론이 흙을 파고 암석층 깊숙한 곳까지 내려가요. 운이 좋다면 근처에 수정 광맥이 있을 거고, 드론이 그곳까지의 거리를 출력할 거예요.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 100}, {"item": "iron", "n": 100}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 8,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "dynamite"]
}

#CODE
move(East)
move(North)
while get_ground_type() != Grounds.Rock:
    dig()
for i in range(30):
    dig()
do_a_flip()
do_a_flip()
print(prospect_quartz())
}}

---

[통계](docs/stats.md)      [채광](docs/unlocks/mining.md)      [지하 감각](docs/unlocks/underground_senses.md)      [변수](docs/scripting/variables.md)      [연산자](docs/scripting/operators.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)      [prospect_quartz()](functions/prospect_quartz)
