[<- 석탄](docs/unlocks/coal.md)
---
# 점프

드론이 `jump()` 명령을 해금했어요.

이 명령으로 특정 해금 항목을 목표로 삼아 그 항목이 있는 지점 근처까지 건너뛸 수 있어요. 디버그하거나 최근에 놓친 광맥으로 이동할 때 특히 유용해요. `Unlocks.Iron`처럼 해금 항목을 인수로 전달해 사용해요.

`jump()`는 `jump(Unlocks.Rice)`나 `jump(Unlocks.Iron)`처럼 지하에 나타나는 해금 항목에서만 작동해요.

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
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 3,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms"],
    "starting_chunk": 0
}
#CODE
dig()
dig()
dig()
jump(Unlocks.Iron)
do_a_flip()
}}

점프한다고 반드시 목표 해금 항목 바로 앞에 도착하는 것은 아니라서 주변을 조금 더 찾아야 할 수도 있어요. 그래도 목표가 근처에 있다는 것은 보장돼요.

`jump()`는 프로그램 실행당 한 번만 사용할 수 있어요.

---

[jump()](functions/jump)
