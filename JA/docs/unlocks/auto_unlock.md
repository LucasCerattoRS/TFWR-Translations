[<- コスト](docs/unlocks/costs.md)
---
# 自動アンロック
ゲームを完全に自動化するには、`unlock()` 関数を使用して機能を自動的にアンロックできます。
例えば、`unlock(Unlocks.Speed)` や `unlock(Unlocks.Expand)` を使用して、スピードや拡張機能をアンロックできます。

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 300}, {"item": "wood", "n": 100000}],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
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
for _ in range(6):
    harvest()
    unlock(Unlocks.Grass)
}}

アンロックのコストを決定するには、植物やアイテムの場合と同様に `get_cost()` 関数を使用するだけです。
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
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "loops"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
print(get_cost(Unlocks.Loops))
}}

---

[コスト](docs/unlocks/costs.md)      [辞書](docs/scripting/dicts.md)      [if文](docs/scripting/if.md)      [リーダーボード](docs/unlocks/leaderboard.md)

[get_cost()](functions/get_cost)      [unlock()](functions/unlock)
