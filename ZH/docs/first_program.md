[<- 入门指南](docs/getting_started.md) <right>[While 循环 ->](docs/scripting/while.md)
---
# 第一个程序
## 文本编辑器

只需要在代码编辑窗口中编写代码就可以完成 1 个程序的编写。每个窗口都对应 1 个代码文件，里面的内容就是你正在编写的代码。
你可以通过单击窗口顶部的文件名来重命名文件。

程序停止运行时，就可以在窗口中编写代码，像使用其他的文本编辑器一样。
单击窗口中的绿色运行按钮可以直接执行程序。
![|x50](PlayButton)

单击屏幕右上角的“+”按钮可以创建新的代码文件。
将一个窗口拖到另一个窗口上，两个窗口可以有序地堆放在一起。

在窗口中编写代码时，会弹出一个简单的代码补全窗口。
按 Tab 键可以插入选中的补全内容。
使用方向键可以在补全选项之间切换。

如果你是第一次编程，新手也可以快速上手。这些功能是逐步解锁的，相关知识不会一股脑地砸下来，让你手忙脚乱。
这款游戏中编程的语法也与 Python 相似，而 Python 是世界上使用最广泛的编程语言之一，所以学习它并不是在浪费时间。

如果已经了解 Python，恭喜！你可以快速跳过游戏的早期阶段，进入更有趣的部分。

目前，有两个函数可以用来操控无人机。

`harvest()`

和

`do_a_flip()`

这种写法就是调用这个函数。函数可以看作是一个可执行的命令，使用 `()` 圆括号来执行。

在窗口中输入这 2 个语句，然后单击运行按钮，就可以让无人机动起来，你自己试试看吧！

你可以把代码看成一系列语句。把多个语句写在不同行上，就能依次运行。
试着点击下方嵌入式代码窗口中的运行按钮，看看代码如何执行：

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
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
do_a_flip()
harvest()
harvest()
}}

## 科技树
收集草可获得干草。干草可以用来在科技树中解锁循环功能。点击右上角的按钮可打开科技树。

---

[外部编辑器](docs/external_editor.md)      [注释](docs/scripting/comments.md)      [While 循环](docs/scripting/while.md)

[harvest()](functions/harvest)      [do_a_flip()](functions/do_a_flip)
