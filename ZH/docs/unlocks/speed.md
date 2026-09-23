[<- While 循环](docs/scripting/while.md) <right>[扩张 1 ->](docs/unlocks/expand_1.md)
<right>[种植 ->](docs/unlocks/plant.md)
---
# 速度升级
现在，无人机的执行速度翻倍了！但是无人机收获的速度比草生长的速度还快，这会导致根本没有收成。为了解决这个问题，现在解锁了 [If 语句](docs/scripting/if.md) 分支和 [can_harvest()](functions/can_harvest) 函数。

## 在收获前检查
当给定条件为 `True` 时，`if` 语句会执行一次其代码块。

新的 `can_harvest()` 函数提供了一个实用的条件：如果无人机下方的植物可以收获，它会返回 `True`，否则返回 `False`。

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
do_a_flip()
#CODE
if can_harvest():
	do_a_flip()
}}

你可以这样理解返回值：在判断 `if` 条件时，函数调用表达式 `can_harvest()` 就像被返回的 `True` 替换了一样。

上面的代码运行时会发生以下过程：
- 执行 `if` 语句。
- 调用 `can_harvest()`。
- 草已经完全成熟，因此 `can_harvest()` 返回 `True`。
- 语句现在变成 `if True:`。
- 值为 `True`，所以执行分支。

如果草尚未完全成熟，无人机就不会翻转。

现在我们可以结合 `if` 语句和 `can_harvest()`，防止无人机在下方植物未成熟时提前收获。

---

[If 语句](docs/scripting/if.md)      [While 循环](docs/scripting/while.md)

[harvest()](functions/harvest)      [can_harvest()](functions/can_harvest)
