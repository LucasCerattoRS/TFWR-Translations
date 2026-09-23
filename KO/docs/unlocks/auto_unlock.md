[<- 비용](docs/unlocks/costs.md)
---
# 자동 해금
게임을 완전히 자동화하려면, `unlock()` 함수를 사용하여 기능을 자동으로 해금할 수 있어요.
예를 들어, `unlock(Unlocks.Speed)`와 `unlock(Unlocks.Expand)`를 사용하여 속도 및 확장 기능을 해금할 수 있어요.

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

해금 비용을 알아보려면, 식물이나 아이템에 하던 것처럼 `get_cost()` 함수를 사용하면 돼요.
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

[비용](docs/unlocks/costs.md)      [딕셔너리](docs/scripting/dicts.md)      [If문](docs/scripting/if.md)      [리더보드](docs/unlocks/leaderboard.md)

[get_cost()](functions/get_cost)      [unlock()](functions/unlock)
