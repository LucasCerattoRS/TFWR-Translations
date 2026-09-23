[<- 速度升级](docs/unlocks/speed.md) <right>[胡萝卜 ->](docs/unlocks/carrots.md)
<right>[调试 ->](docs/scripting/debug.md)
<right>[运算符 ->](docs/scripting/operators.md)
---
# 种植
草会自动生长，这很好。所有其他植物都需要调用 `plant()` 函数进行种植。你现在唯一能种的植物是灌木。
你可以像这样把你想种的植物类型传递给函数：

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
plant(Entities.Bush)
}}

这会在无人机下方的地块上种植 1 丛灌木。

调用 `clear()` 函数可以将农场重置为整片草地，并重置无人机回到 (0,0) 的位置。

当农场上同时生长着多种植物时，可能会提高产量。你需要研究混合种植以了解更多信息。

---

[统计数据](docs/stats.md)      [If 语句](docs/scripting/if.md)      [感官](docs/unlocks/senses.md)      [混合种植](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)
