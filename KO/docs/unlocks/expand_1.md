[<- 속도 업그레이드](docs/unlocks/speed.md) <right>[확장 2 ->](docs/unlocks/expand_2.md)
<right>[채광 ->](docs/unlocks/mining.md)
---
# 확장 1
농장이 넓어졌어요! 드론을 움직일 수 없다면 이 공간은 별로 쓸모가 없으니, 드론을 움직이는 새로운 함수 `move()`가 있어요. `move()`는 드론을 움직이고 싶은 방향을 지정해야 해요. 이를 위한 네 가지 새로운 상수가 있어요: `North, East, South, West`

예를 들어, `move(North)`는 드론을 북쪽으로 한 칸 움직여요.

농장 가장자리 밖으로 이동하면 드론은 농장의 반대편으로 이동돼요.
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 3},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	move(North)
}}

---

[while 루프](docs/scripting/while.md)      [연산자](docs/scripting/operators.md)      [확장 2](docs/unlocks/expand_2.md)

[move()](functions/move)
