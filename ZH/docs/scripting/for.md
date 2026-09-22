[<- 扩张 2](docs/unlocks/expand_2.md)
---
# For 循环
`for` 循环语句的运行方式与 Python 中类似。（在某些语言中称为 foreach 循环，但不要与 C 语言风格的 for 循环混淆，那是不同的概念）。

`for i in sequence:
	#用 i 做点什么`

与 `while` 循环类似，`for` 循环会重复调用某个代码块。但它不是根据条件循环的，而是存储序列中每有 1 个元素就执行 1 次循环体。

## 语法
for 循环语句的格式如下：

`for variable_name in sequence:
	#代码块`

`variable_name` 可以是你选定的任意名称。这个变量保存序列中的当前元素。`sequence` 必须是可迭代的值，例如一段数字范围。序列中的每个元素都会让循环体执行一次，同时该元素会赋给循环变量。

## 序列
[范围](functions/range)      <unlock=lists>[列表](docs/scripting/lists.md)      </unlock><unlock=functions>[元组](docs/scripting/tuples.md)      </unlock><unlock=dicts>[字典](docs/scripting/dicts.md)      </unlock><unlock=sets>[集合](docs/scripting/sets.md)</unlock>

## 示例
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
for i in range(5):
    harvest()
}}

这个循环会固定次数地执行循环体，基本上等同于如下代码：

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
i = 0
harvest()
i = 1
harvest()
i = 2
harvest()
i = 3
harvest()
i = 4
harvest()
}}

---

[While 循环](docs/scripting/while.md)      [Break 语句](docs/scripting/break.md)      [Continue 语句](docs/scripting/continue.md)

[range()](functions/range)
