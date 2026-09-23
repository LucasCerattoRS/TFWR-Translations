[<- 运算符](docs/scripting/operators.md)
---
# 感官
无人机现在拥有视觉能力了！

调用 `get_pos_x()` 和 `get_pos_y()` 函数会返回无人机当前的 x 和 y 坐标。在起始位置时，两者都返回 `0`。x 的坐标向 `East` （右）方向每格增加 `1`，y 的坐标向 `North` （上）方向每格增加 `1`。
{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 2},
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
#CODE
print("x =", get_pos_x(), "y =", get_pos_y())
if get_pos_x() == 1 and get_pos_y() == 0:
    do_a_flip()
}}

调用 `num_items(item)` 函数会返回你现在拥有某种物品的数量。
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
    "items": [{"item": "hay", "n": 10}],
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
print(num_items(Items.Hay))
}}

调用 `get_entity_type()` 和 `get_ground_type()` 函数会返回无人机当前下方实体或地块类型。

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
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
plant(Entities.Bush)
#CODE
print(get_entity_type())
if get_entity_type() == Entities.Bush:
	do_a_flip()

print(get_ground_type())
if get_ground_type() != Grounds.Soil:
	do_a_flip()
}}

`None` 关键字现在也解锁了！`None` 是一个表示没有值的值。
例如，调用一个没有 `return` 语句的函数实际上就会返回 `None`。

如果无人机下方没有实体，调用 `get_entity_type()` 函数会返回 `None`。


如果想知道你现在拥有的某个特定科技树项目的数量，可以调用 `num_unlocked(unlock)` 函数。

例如，调用 `num_unlocked(Unlocks.Speed)` 函数会返回你现在拥有的速度的等级。

如果感官已解锁，调用 `num_unlocked(Unlocks.Senses)` 函数会返回 `1`，否则返回 `0`。

你也可以对物品或实体调用 `num_unlocked()` 函数，已解锁会返回 `1`，否则返回 `0`。

请注意：调用 `num_unlocked(Unlocks.Carrots)` 函数会返回胡萝卜是否被解锁或者胡萝卜当前的等级。
调用 `num_unlocked(Items.Carrot)` 函数则只会返回 `0` 或 `1`。（其他植物也一样）

---

[If 语句](docs/scripting/if.md)      [运算符](docs/scripting/operators.md)      [变量](docs/scripting/variables.md)      [元组](docs/scripting/tuples.md)      [字典](docs/scripting/dicts.md)      [地下感官](docs/unlocks/underground_senses.md)

[get_pos_x()](functions/get_pos_x)      [get_pos_y()](functions/get_pos_y)      [get_entity_type()](functions/get_entity_type)      [get_ground_type()](functions/get_ground_type)      [num_items()](functions/num_items)      [num_unlocked()](functions/num_unlocked)
