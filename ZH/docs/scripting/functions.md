[<- 变量](docs/scripting/variables.md) <right>[导入 ->](docs/scripting/import.md)
---
# 函数
使用 `def` 关键字来自定义一个新的函数：
`def f(arg1, arg2 = False):
	#函数代码`

使用 `()` 来调用某个函数：
`f(42)`

另请参阅[作用域](docs/scripting/scopes.md)来了解函数中的局部变量和全局变量。

## 介绍
你已经见过像 `harvest()` 这样的内置函数。
你也可以自定义函数，从而以模块化的方式组织你的代码。简单来说，你可以给一个代码块命名，之后可以从任何地方调用该代码块。

## 函数定义
例如，你可以定义一个多次移动无人机的函数。

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
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def move_n_dir(n, dir):
	for i in range(n):
		move(dir)
}}

`def` 关键字表示这定义了一个函数。
`move_n_dir` 是函数绑定的名称。这是你自定义的变量名称，用于调用该函数。
`n` 和 `dir` 是形式参数（形参），用来接收传入函数的值的变量，这些值也称为实际参数（实参）。你可以根据需要定义多个（没有数量限制）向函数传入的形参。
`:` 后面是函数被调用时将运行的代码块。

根据上述定义，以下代码将无人机向 `North` 移动 `2` 格，向 `East` 移动 `2` 格。

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 3},
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
def move_n_dir(n, dir):
	for i in range(n):
		move(dir)

move_n_dir(2, North)
move_n_dir(2, East)
}}

看到 `def function():` 时，应该把它想象成一个这样的变量赋值：
`function = create_new_function_object()`
和其他赋值一样，在没有给变量赋初值时，无法使用该变量！
`def` 语句必须在任何函数调用之前运行。
这段代码会抛出一个错误：

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
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
func()
def func():
	pass
}}

## 返回值
使用 `return` 关键字可以让函数返回 1 个值。
例如，以下函数定义了异或运算。如果一个值为 `True` 而另一个为 `False`，异或运算返回 `True`：

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
#CODE
def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()
}}

[元组](docs/scripting/tuples.md)可以返回多个值。

## 默认参数
你还可以添加默认值，在没有传递参数的情况下，会使用默认值。

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
#CODE
def f(a = False):
	if a:
		do_a_flip()

f()

f(True)
}}

有默认值的参数后面不能跟没有默认值的参数。

## 高级函数用法
和其他的值一样，函数也是值，而 `def` 语句就像一个赋值语句，将函数赋给你自定义的名称。
因此，你可以这么做：

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
#CODE
def f():
	def d():
		do_a_flip()
	return d

f()()
}}

这里 `f()` 调用函数 `f`，它会定义并返回一个新函数 `d`。第二个 `()` 则执行返回的函数，并让无人机翻转。
(这种写法不建议，因为很难看出这个函数到底在做什么操作。)

将其他函数作为参数的函数可以让你写出很有创意的代码：

{{codeexample 
{
    "camera_position": {"x": -2, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "fertilizer", "n": 4}],
    "world_size": {"x": 5, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def f(g, arg):
	for _ in range(4):
		g(arg)

f(move, East)
plant(Entities.Tree)
f(use_item, Items.Fertilizer)
}}

---

[变量](docs/scripting/variables.md)      [名称作用域](docs/scripting/scopes.md)      [元组](docs/scripting/tuples.md)      [导入](docs/scripting/import.md)
