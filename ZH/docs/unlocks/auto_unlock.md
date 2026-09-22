[<- 成本](docs/unlocks/costs.md)
---
# 自动解锁
你可以调用 `unlock()` 函数使科技树中的项目进行自动解锁，这可以实现完全自动化，解放双手！
例如，你可以调用 `unlock(Unlocks.Speed)` 和 `unlock(Unlocks.Expand)` 函数来解锁速度和扩张土地。

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

对科技树中的项目使用 `get_cost()` 函数，就可以获取该项目解锁或者升级所需的耗材数量，就像对植物或物品使用函数那样。
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

[成本](docs/unlocks/costs.md)      [字典](docs/scripting/dicts.md)      [If 语句](docs/scripting/if.md)      [排行榜](docs/unlocks/leaderboard.md)

[get_cost()](functions/get_cost)      [unlock()](functions/unlock)
