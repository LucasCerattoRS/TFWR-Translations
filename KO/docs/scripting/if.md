[<- 속도 업그레이드](docs/unlocks/speed.md)
---
# If문
`if`, `elif`, `else`를 사용해 코드를 조건부로 실행할 수 있어요.

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
condition1 = False
condition2 = False
condition3 = True

if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()
}}

## 문법
`if` 문을 사용하면 조건이 `True`일 때만 코드를 실행할 수 있어요. 반복하지 않는 `while` 루프와 같아요.
`if` 문은 `while` 루프처럼 조건을 받고, 조건이 `True`로 평가되면 코드 블록을 실행해요.

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
condition = True

if condition:
	do_a_flip()
}}

`if` 블록 뒤에 `else` 블록을 추가할 수도 있어요. `else` 블록은 조건이 `False`로 평가될 때 실행돼요.

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
condition = False

if condition:
	do_a_flip()
else:
	harvest()
}}

`elif`는 "else if"의 줄임말이에요.

`if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c`

이 코드는 다음과 같이 줄일 수 있어요.

`if condition1:
	#a
elif condition2:
	#b
else:
	#c`

---

[while 루프](docs/scripting/while.md)      [연산자](docs/scripting/operators.md)      [감각](docs/unlocks/senses.md)
