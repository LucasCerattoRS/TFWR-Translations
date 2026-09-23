[<- 种植](docs/unlocks/plant.md) <right>[调试 2 ->](docs/unlocks/debug2.md)
<right>[计时 ->](docs/unlocks/timing.md)
---
# 调试
有时候代码会无法正常运行，而你需要找出原因。有几个工具可以在这方面派上用场。

第一个是逐步执行程序。
你可以使用运行按钮旁边的按钮或设置断点来进入逐步模式。

点击代码左侧区域可以添加断点。
![|x227](Breakpoints)
当代码执行到断点所在的行时，会自动切换到逐步模式。

将鼠标移到某个变量上时，会显示它当前的值。

`print()` 函数也非常有用。它会将传递给它的所有值直接打印到空中，形成文字状的云朵效果。

示例：

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
print(0.24)
}}

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
print(can_harvest())
}}

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
print(get_pos_x(), get_pos_y())
}}

`print()` 函数会将值直接打印到空中和[输出](docs/output.md)页面。

如果你想打印大量的值，在空中书写有时可能会有点慢。
在这种情况下，可以调用 `quick_print()` 函数，只打印到输出窗口。

输出窗口还会记录警告和错误，所以如果运行结果有哪里与预期不符，不妨检查一下输出窗口。

当程序停止运行时，输出也会被写入游戏文件夹中的 [output.txt](persistent_data_path/output.txt) 文件。

---

[输出](docs/output.md)      [注释](docs/scripting/comments.md)      [调试 2](docs/unlocks/debug2.md)      [彩色地块](docs/unlocks/debug_place.md)      [模拟](docs/unlocks/simulation.md)

[print()](functions/print)      [quick_print()](functions/quick_print)
