[<- While 循环](docs/scripting/while.md)
---
# 帽子

解锁帽子，现在你获得了几种不同颜色的新帽子，你的无人机现在可以换上新帽子了。

更换帽子的代码如下：
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
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
change_hat(Hats.Gray_Hat)
do_a_flip()
change_hat(Hats.Purple_Hat)
do_a_flip()
change_hat(Hats.Green_Hat)
do_a_flip()
change_hat(Hats.Brown_Hat)
do_a_flip()
}}

---

[恐龙](docs/unlocks/dinosaurs.md)      [第一个程序](docs/first_program.md)

[change_hat()](functions/change_hat)
