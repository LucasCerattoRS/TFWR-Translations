[<- 리스트](docs/scripting/lists.md) <right>[비용 ->](docs/unlocks/costs.md)
---
# 딕셔너리
딕셔너리는 실제 사전이 단어를 정의에 연결하듯 키를 값에 매핑하는 자료 구조예요. 이러한 값을 매우 빠르게 찾을 수 있어요.

딕셔너리는 다음과 같이 만들 수 있어요.

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
right_of = {North:East, East:South, South:West, West:North}
}}

콜론 앞의 표현식은 키이고, 콜론 뒤의 표현식은 키가 매핑되는 값이에요.
위 딕셔너리는 각 방향을 그 오른쪽 방향에 매핑해요.

다음은 드론의 위치를 그 아래에 있는 개체에 매핑하는 또 다른 딕셔너리예요.
{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}
}}

키에 매핑된 값에 접근하는 것은 리스트의 요소에 접근하는 것과 비슷해요.
`value = dict[key]`

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
right_of = {North:East, East:South, South:West, West:North}
print(right_of[South])
}}

딕셔너리에 새 키-값 쌍을 추가하려면 다음과 같이 하세요.
`dict[key] = value`

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 1},
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
move(East)
plant(Entities.Bush)
move(East)
plant(Entities.Tree)
move(East)
#CODE
entity_dict = {}
for _ in range(3):
	entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()
	move(East)
print(entity_dict)
}}

키는 고유하므로 딕셔너리에 이미 존재하는 키를 추가하면 이전 값을 덮어써요.

`dict`에서 키-값 쌍을 제거하려면 `dict.pop(key)`를 사용하세요.

`key in dict`는 `key`가 `dict`의 키이면 `True`로, 그렇지 않으면 `False`로 평가돼요.
따라서 `if key in dict:`를 사용하여 `dict`에 키가 포함되어 있는지 확인할 수 있어요.

딕셔너리를 `for` 루프에 넣으면 모든 키를 순회할 수 있어요.
{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
right_of = {North:East, East:South, South:West, West:North}
print(North in right_of)
for key in right_of:
	value = right_of[key]
	print(key, ":", value)
}}

키를 순회하는 순서는 보장되지 않아요.

[세트](docs/scripting/sets.md)도 참고하세요.

---

[리스트](docs/scripting/lists.md)      [세트](docs/scripting/sets.md)      [튜플](docs/scripting/tuples.md)      [비용](docs/unlocks/costs.md)

[len()](functions/len)
