[<- 벼](docs/unlocks/rice.md)
---
# 화석화된 호박

어쩐지 지하에서 호박을 찾을 수 있다는군요. 단단하게 굳어 화석화되었지만, 우리가 쓰기에는 아직 충분해요.

화석화된 호박은 지하에 3x3x3 또는 5x5x5 크기의 블록 뭉치로 나타나요. 확실하게 찾는 방법은 없으니 드론이 운 좋게 하나를 파내기를 바라야 해요. 화석화된 호박은 돌과 철층 아래의 단단한 흙에, 수정이 나오는 것과 대략 같은 높이에 생성돼요(수정을 해금했다면요).

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 100}],
    "exclude_unlocks": ["mushrooms", "watering", "fertilizer", "pyramid", "dynamite"],
    "world_size": {"x": 6, "y": 6},
    "execution_speed": 8,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 3
}
#SETUP
jump(Unlocks.Petrified_Pumpkins)
move(East)
move(North)
move(North)
move(North)
#CODE
while get_ground_type() != Grounds.Petrified_Pumpkin:
    dig()
z = get_pos_z()
for i in range(get_world_size()):
    for j in range(get_world_size()):
        while get_pos_z() > z:
            dig()
        move(North)
    move(East)
}}

---

[통계](docs/stats.md)      [채광](docs/unlocks/mining.md)      [지하 감각](docs/unlocks/underground_senses.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)
