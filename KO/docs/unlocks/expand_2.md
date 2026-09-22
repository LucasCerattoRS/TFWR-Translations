[<- 확장 1](docs/unlocks/expand_1.md)
---
# 확장 2
농장이 다시 확장되었어요! 이제 타일들이 더 이상 예쁘게 한 줄로 있지 않아서, 정사각형 격자를 순회하는 방법을 찾아야 해요.

`while` 루프로는 감각과 연산자를 해금하기 전까지 불가능해요.
이제 `for` 루프를 소개할 시간이에요.

`for` 루프에 대한 모든 내용은 [For 루프](docs/scripting/for.md) 페이지에서 읽을 수 있지만, 지금은 코드를 정해진 횟수만큼 반복하는 데만 필요할 거예요.

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
#CODE
for i in range(5):
	do_a_flip()
}}

`range(n)`은 `0`부터 `n - 1`까지 `n`개의 숫자로 이루어진 시퀀스를 만들어요. `for` 루프는 시퀀스의 각 요소마다 본문을 한 번씩 실행해요. 이 예시에서는 `do_a_flip()`이 `5`번 호출돼요.

`get_world_size()` 함수도 이제 사용할 수 있어요. 농장의 한 변 길이를 반환해요. 이렇게 하면 다음 확장 업그레이드에도 망가지지 않는 코드를 작성할 수 있어요.

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
    "items": [],
    "world_size": {"x": 3, "y": 3},
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
do_a_flip()
#CODE
for i in range(get_world_size()):
	harvest()
	move(North)
}}

이 예시는 농장 크기와 관계없이 농장의 한 열을 수확해요.

드론을 농장에서 어떻게 움직일지 알아내느라 막혔다면 아래 힌트를 보세요.
<spoiler=힌트 보기>물론 농장을 돌아다니는 방법은 여러 가지가 있어요.
우리가 찾는 것은 농장이 다시 커져도 망가지지 않는 체계적인 순회 방법이에요.
농장의 모든 곳에 도달하는 체계적인 방법은 다음 두 단계를 계속 반복하는 것이에요.

1. 드론이 반대편으로 돌아올 때까지 `North`로 이동해요.
2. `East`로 이동해요.

`for i in range(get_world_size()):`가 이 아이디어를 코드로 바꾸는 데 도움이 될 수 있어요.
</spoiler>
<spoiler=가능한 해결책 보기>
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
    "items": [],
    "world_size": {"x": 3, "y": 3},
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
do_a_flip()
#CODE
for i in range(get_world_size()):
	for j in range(get_world_size()):
		# 모든 타일에서 재주넘기
		do_a_flip()
		move(North)
	move(East)
}}
</spoiler>

---

[For 루프](docs/scripting/for.md)      [While 루프](docs/scripting/while.md)      [변수](docs/scripting/variables.md)

[move()](functions/move)      [get_world_size()](functions/get_world_size)
