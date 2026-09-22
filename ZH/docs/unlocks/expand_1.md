[<- 速度升级](docs/unlocks/speed.md) <right>[扩张 2 ->](docs/unlocks/expand_2.md)
<right>[采矿 ->](docs/unlocks/mining.md)
---
# 扩张 1
你的农场变大了！无人机现在可以移动了，调用新的函数 `move()` 来移动无人机。`move()` 可以指定无人机移动的方向，为此还引入了四个新的常量：`North, East, South, West`，分别是“向上”、“向右”、“向下”和“向左”。


例如，`move(North)` 会将无人机向上移动 1 格。

如果超过农场边缘，无人机会绕回另一边。

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 3},
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
#CODE
while True:
	move(North)
}}

---

[While 循环](docs/scripting/while.md)      [运算符](docs/scripting/operators.md)      [扩张 2](docs/unlocks/expand_2.md)

[move()](functions/move)
