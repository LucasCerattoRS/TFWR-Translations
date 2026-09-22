[<- 연산자](docs/scripting/operators.md) <right>[리스트 ->](docs/scripting/lists.md)
<right>[함수 ->](docs/scripting/functions.md)
---
# 변수
변수는 값을 담을 수 있는 이름이 붙은 컨테이너라고 생각할 수 있어요.
`=` 연산자는 변수를 선언하고 값을 저장하는 데 사용돼요.

`variable_name = value`

연산자의 왼쪽 피연산자는 변수 이름이에요. 원하는 어떤 이름이든 붙일 수 있어요.
오른쪽 피연산자는 결과값이 변수에 저장될 표현식이에요.

`a`라는 이름의 변수를 선언하고 값 `5`를 저장하세요:
`a = 5`
`b`라는 이름의 변수를 선언하고 `can_harvest()`의 반환 값을 저장하세요:
`b = can_harvest()`

`=` 연산자와 `==` 연산자를 혼동하지 마세요.
`==` 연산자는 두 값이 같은지 확인하고 `True` 또는 `False`를 반환해요.
`=` 연산자는 오른쪽의 값을 왼쪽의 이름에 할당해요.

변수가 할당된 후에는 코드에서 사용하여 포함된 값을 가져올 수 있어요.

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
a = 5
for i in range(a):
	do_a_flip()
}}

위의 루프는 `a`가 `5`로 설정되었기 때문에 5번 실행돼요.
`for` 루프의 `i`도 변수이며, 루프의 각 반복에서 시퀀스의 현재 값이 자동으로 할당돼요. (`i`라고 부를 필요는 없으며, 유효한 변수 이름을 붙일 수 있어요.)

변수를 사용하면 while 루프로도 같은 일을 할 수 있어요:

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
a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1
}}

이것은 위의 `for` 루프와 같은 일을 하지만 `i`를 수동으로 증가시켜야 해요.
`i`를 증가시키려면 현재 값에 `1`을 더한 값으로 설정해요. 이전 값에 기반하여 변수 값을 변경하는 것은 매우 흔한 일이에요.
다음 연산자들을 사용하여 줄여 쓸 수 있어요: `+=, -=, *=, /=, %=`

`i = i + 1`은 `i += 1`과 같아요
`a = a / 3`은 `a /= 3`과 같아요

---

[연산자](docs/scripting/operators.md)      [while 루프](docs/scripting/while.md)      [for 루프](docs/scripting/for.md)      [함수](docs/scripting/functions.md)      [이름 스코프](docs/scripting/scopes.md)
