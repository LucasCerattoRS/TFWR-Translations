[<- While 루프](docs/scripting/while.md) <right>[확장 1 ->](docs/unlocks/expand_1.md)
<right>[심기 ->](docs/unlocks/plant.md)
---
# 속도 업그레이드
실행 속도가 두 배가 되었어요. 문제는 이제 드론이 풀이 자라는 속도보다 더 빨리 수확해서 아무것도 얻지 못하게 된다는 점이에요. 이 문제를 해결하기 위해 [If문](docs/scripting/if.md) 분기와 [can_harvest()](functions/can_harvest) 함수가 이제 해금되었어요.

## 수확하기 전에 확인하기
`if` 문은 주어진 조건이 `True`일 때 코드 블록을 한 번 실행해요.

새로운 함수 `can_harvest()`는 유용한 조건을 제공해요. `can_harvest()`는 드론 아래의 식물을 수확할 수 있으면 `True`를, 그렇지 않으면 `False`를 반환해요.

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
    "items": [],
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
do_a_flip()
#CODE
if can_harvest():
	do_a_flip()
}}

이런 반환 값은 `if`를 평가하는 동안 함수 호출 표현식 `can_harvest()`가 반환된 값 `True`로 바뀐다고 생각하면 돼요.

위 코드가 실행될 때 일어나는 일:
- `if` 문이 실행돼요.
- `can_harvest()`가 호출돼요.
- 풀이 다 자랐기 때문에 `can_harvest()`가 `True`를 반환해요.
- 이제 문장은 `if True:`가 돼요.
- 값이 `True`이므로 분기가 실행돼요.

풀이 다 자라지 않았다면 재주를 넘지 않을 거예요.

이제 `if`를 사용해서 드론이 너무 일찍 수확하는 것을 막을 수 있어요.

---

[If문](docs/scripting/if.md)      [While 루프](docs/scripting/while.md)

[harvest()](functions/harvest)      [can_harvest()](functions/can_harvest)
