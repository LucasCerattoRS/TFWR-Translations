[<- while 루프](docs/scripting/while.md)
---
# 모자

드론을 위한 몇 가지 새로운 색상의 모자를 해금했어요.

이렇게 장착할 수 있어요:
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

[공룡](docs/unlocks/dinosaurs.md)      [첫 번째 프로그램](docs/first_program.md)

[change_hat()](functions/change_hat)
