[<- 扩张 1](docs/unlocks/expand_1.md)
---
# 扩张 2
你的农场又扩张了！现在地块不再是整齐的一行，所以你需要想办法遍历整个方形网格。

在使用 `while` 循环的情况下，若尚未解锁感官和运算符，则无法实现这一点。
那么是时候介绍 `for` 循环了。

在 [For 循环](docs/scripting/for.md)页面上可以阅读所有有关 `for` 循环的内容，但目前你只需要用它在固定的次数来重复执行代码。

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
for i in range(5):
	do_a_flip()
}}

`range(n)` 表示一个从 `0` 到 `n - 1` 的数字范围，其中包含 `n` 个元素。`for` 循环对序列中的每个元素执行一次循环体。在这个例子中，`do_a_flip()` 将被调用 `5` 次。

现在也可以使用 `get_world_size()` 函数了。它会返回你的农场的边长，即使下次继续扩张你的土地，你所编写的代码也不会失效。

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
for i in range(get_world_size()):
	harvest()
	move(North)
}}

在此示例中，无论农场多大，无人机都会收获农场第一列的每一个格子。

如果想不出来该如何让你的无人机飞遍整个农场，请看下面的提示。
<spoiler=显示提示>当然，有多种方法都可以遍历农场。
我们要找的是一种普遍性的遍历方法，确保代码在农场再次扩大时不会失效。
如果想让你的无人机飞遍整个农场，其中一种普遍性的方法就是永远重复以下两个步骤：

1.向 `North` 移动，直到绕回原点。
2.向 `East` 移动。

`for i in range(get_world_size()):` 可能有助于将这个想法转化为代码。
</spoiler>
<spoiler=显示可能的解决方案>
{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
for i in range(get_world_size()):
	for j in range(get_world_size()):
		#在每个地块上翻转一次
		do_a_flip()
		move(North)
	move(East)
}}
</spoiler>

---

[For 循环](docs/scripting/for.md)      [While 循环](docs/scripting/while.md)      [变量](docs/scripting/variables.md)

[move()](functions/move)      [get_world_size()](functions/get_world_size)
