[<- 字典](docs/scripting/dicts.md) <right>[自动解锁 ->](docs/unlocks/auto_unlock.md)
---
# 成本
所有成本都可以用一个将物品映射到数量的字典表示。

`get_cost()` 函数返回的值就是这样的一个字典：某种植物或某个科技树项目的耗材。

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

向科技树中的各种项目添加第二个可选参数，就可以获取你想要的解锁等级对应的耗材数量。默认情况下为当前的解锁等级。

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

如果科技树中的某些项目已经到达最高等级，调用 `get_cost()` 函数则返回一个空字典。

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
		print("缺少", cost[item] - num_items(item), item)
}}

---

[字典](docs/scripting/dicts.md)      [自动解锁](docs/unlocks/auto_unlock.md)      [排行榜](docs/unlocks/leaderboard.md)

[get_cost()](functions/get_cost)
