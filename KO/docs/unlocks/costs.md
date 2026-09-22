[<- 딕셔너리](docs/scripting/dicts.md) <right>[자동 해금 ->](docs/unlocks/auto_unlock.md)
---
# 비용
모든 비용은 아이템을 숫자에 매핑하는 딕셔너리로 나타낼 수 있어요.

`get_cost()` 함수는 이런 딕셔너리를 반환해요. 식물이나 해금 항목의 비용을 반환해요.

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
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
print(get_cost(Entities.Pumpkin))
}}

해금 항목의 경우 비용을 알고 싶은 해금 레벨을 선택적인 두 번째 인수로 전달할 수 있어요. 기본값은 현재 해금 레벨이에요.

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
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
print(get_cost(Unlocks.Loops, 0))
print(get_cost(Unlocks.Loops, 1))
}}

이미 최대 레벨인 해금 항목에서 `get_cost()`는 빈 딕셔너리를 반환해요.

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
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
cost = get_cost(Entities.Carrot)
for item in cost:
	if num_items(item) < cost[item]:
		print("부족", cost[item] - num_items(item), item)
}}

---

[딕셔너리](docs/scripting/dicts.md)      [자동 해금](docs/unlocks/auto_unlock.md)      [리더보드](docs/unlocks/leaderboard.md)

[get_cost()](functions/get_cost)
