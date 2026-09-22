[<- 채광](docs/unlocks/mining.md)
---
# 지하 감각

드론이 지하에서 길을 찾을 수 있도록 센서를 몇 개 추가해 볼게요.

이제 `get_pos_z()`로 드론의 높이를 알 수 있어요. 0에서 시작하고 드론이 내려갈수록 음수가 돼요.

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
    "exclude_unlocks": ["watering", "fertilizer"],
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#CODE
move(North)
move(North)
move(East)
dig()
dig()
dig()
print(get_pos_z())
}}

`get_ground_type()`은 드론 아래의 땅 종류를 반환해요. `get_ground_type(North)`처럼 방향 인수를 전달하면 인접한 타일의 땅 종류를 알 수 있어요.

드론 아래의 블록이 흙인지 확인하는 방법은 다음과 같아요.

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
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#CODE
dig()
if get_ground_type() == Grounds.Dirt:
    do_a_flip()
}}


`get_hardness()`는 드론 아래 땅 타일의 경도를 반환해요. `get_hardness(North)`처럼 방향 인수를 전달할 수 있어요. 타일의 경도가 높을수록 파는 데 오래 걸려요.

`get_stability()`는 드론 아래 땅 타일의 안정성을 반환해요. `get_stability(North)`처럼 방향 인수를 전달할 수 있어요. 안정성이 1이라면 블록이 붕괴하기 전에 높이 차이 1까지 견딜 수 있다는 뜻이에요.

드론이 아래로 파내려갈 때 특수 기능이 있는 블록이 아니라면 드론 바로 옆의 네 블록은 안정성과 관계없이 제거돼요. 예를 들어 점토, 철, 수정은 이 규칙에 따라 제거되지 않아요. 하지만 블록 안정성이 부족해 일어나는 붕괴에는 여전히 영향을 받아요.
---

[채광](docs/unlocks/mining.md)      [감각](docs/unlocks/senses.md)

[get_pos_z()](functions/get_pos_z)      [get_ground_type()](functions/get_ground_type)      [get_hardness()](functions/get_hardness)      [get_stability()](functions/get_stability)
