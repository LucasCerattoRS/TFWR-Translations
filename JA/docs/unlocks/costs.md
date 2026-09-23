[<- 辞書](docs/scripting/dicts.md) <right>[自動アンロック ->](docs/unlocks/auto_unlock.md)
---
# コスト
どんなコストも、アイテムを数値にマッピングする辞書として表現できます。

`get_cost()` 関数は、そのような辞書を返します。植物やアンロックのコストを返します。

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

アンロックの場合、コストを知りたいアンロックレベルをオプションの第2引数として渡すことができます。デフォルトでは、現在のアンロックレベルです。

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

すでに最大レベルのアンロックの場合、`get_cost()` は空の辞書を返します。

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
		print("不足", cost[item] - num_items(item), item)
}}

---

[辞書](docs/scripting/dicts.md)      [自動アンロック](docs/unlocks/auto_unlock.md)      [リーダーボード](docs/unlocks/leaderboard.md)

[get_cost()](functions/get_cost)
