[<- 调试](docs/scripting/debug.md) <right>[模拟 ->](docs/unlocks/simulation.md)
---
# 计时
如果想要进一步优化你的方案，你需要了解这款游戏中时间的计量方式，也就是这个科技树的内容。

## 新函数
如果要考虑事情花费的时间，有两个函数可用：

调用 `get_time()` 函数会返回丛游戏开始以来的时间，单位是秒。

调用 `get_tick_count()` 函数会返回该程序从开始到结束时所占用的 tick 数。

这两个函数以及 `quick_print()` 函数不占用 tick，甚至连调用它们的操作也不占用 tick。

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
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
start_time, start_ticks = get_time(), get_tick_count()
harvest()
time, ticks = get_time(), get_tick_count()
quick_print(time - start_time, ticks - start_ticks)
}}

## 运行时详情

### 注意
这是我们为这款游戏制定的一个易于理解且一致的计时模型，这与现实世界中的执行方式是不一样的。
你可能只有在想要极致优化代码时才会关心这个。


代码执行的基本时间单位称为“tick”。在没有速度升级和能量的情况下，每秒执行 `400` 个 tick。

通常，组合两个值的操作（例如 `+, -, *, /, //, %, and, or, ...`）占用 1 tick 来运行。
单值 `-` 和 `not` 是不占用 tick 的。
单个 `if` 分支占用 1 tick 来运行（不包括计算条件表达式所需的时间）。
函数调用以及变量的读取和写入不占用 tick ，但函数的定义将占用 1 tick。
`import` 不占用 tick。
使用 `.` 运算符访问导入的模块不占用 tick。
如果一个函数或模块是通过参数或变量赋值传递的，则使用时将占用 1 tick 而非不占用 tick。
`for` 和 `while` 循环开始时占用 1 tick，但迭代自身不占用 tick（不包含条件或者序列表达式所占用的 tick ）。
`return`、`break` 和 `continue` 都不占用 tick。
`pass` 占用 1 tick，所以它可以用来创造精确的延迟。
使用索引运算符对数据结构进行索引占用 1 tick，而在涉及字典或集合的情况下，还需要根据键的大小占用额外的 tick。

执行内置函数所占用的 tick 在每个函数的文档中都有单独说明。

---

[调试](docs/scripting/debug.md)      [模拟](docs/unlocks/simulation.md)      [排行榜](docs/unlocks/leaderboard.md)

[get_time()](functions/get_time)      [get_tick_count()](functions/get_tick_count)      [quick_print()](functions/quick_print)
