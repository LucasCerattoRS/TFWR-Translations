[<- 당근](docs/unlocks/carrots.md) <right>[호박 ->](docs/unlocks/pumpkins.md)
---
# 나무
[나무](objects/tree)는 덤불보다 목재를 얻기에 더 좋은 방법이에요. 각각 목재 5개를 줘요. 덤불처럼 풀이나 흙 위에 심을 수 있어요.

나무는 공간을 좀 확보하는 것을 좋아해서 바로 옆에 심으면 성장이 느려져요. 바로 북쪽, 동쪽, 서쪽, 남쪽에 있는 타일에 다른 나무가 있을 때마다 성장 시간이 두 배가 돼요. 그래서 모든 타일에 나무를 심으면 자라는 데 `2*2*2*2 = 16`배 더 오래 걸릴 거예요.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 10,
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
for i in range(get_world_size()):
	for j in range(get_world_size()):
		plant(Entities.Tree)
		move(North)
	move(East)
}}

<spoiler=보기> 
`%` 연산자가 여기서 유용할 수 있어요. `%` 연산자는 나눗셈의 나머지를 반환해요. 짝수를 `2`로 나누면 나머지가 `0`이고 홀수를 `2`로 나누면 나머지가 `1`이에요.
그래서 숫자가 짝수인지 이렇게 확인할 수 있어요:

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": false,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def is_even(n):
	return n % 2 == 0

print("is_even(0): ", is_even(0))
print("is_even(1): ", is_even(1))
print("is_even(2): ", is_even(2))
print("is_even(5): ", is_even(5))
print("is_even(-1): ", is_even(-1))
print("is_even(x): ", is_even(get_pos_x()))
}}
</spoiler>

---

[통계](docs/stats.md)      [연산자](docs/scripting/operators.md)      [If문](docs/scripting/if.md)      [For 루프](docs/scripting/for.md)      [혼합 재배](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)
