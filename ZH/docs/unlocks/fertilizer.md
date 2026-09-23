[<- 浇水](docs/unlocks/watering.md) <right>[迷宫 ->](docs/unlocks/mazes.md)
---
# 肥料
有些时候，等待植物生长非常影响效率。
与水类似，你每 10 秒会自动获得 1 份肥料，每次升级数量翻倍。

肥料可以使植物加速生长。`use_item(Items.Fertilizer)` 会将无人机下方植物的剩余生长时间缩短 2 秒。

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "fertilizer", "n": 10}],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Tree)
use_item(Items.Fertilizer)
use_item(Items.Fertilizer)
use_item(Items.Fertilizer)
harvest()
}}

但肥料存在副作用。
施肥生长的植物会被感染。

植物被感染后，收获时一半的产量会变成奇异物质 `Items.Weird_Substance`。
奇异物质也可以用在植物上，其效果是切换该植物及所有相邻植物的感染状态。

所以如果在受感染的植物上调用 `use_item(Items.Weird_Substance)` 会治愈植物，但在健康的植物上调用它，则会感染植物。

如果在有健康邻居的受感染植物上使用它，在治愈该植物的同时会感染邻居，反之亦然。

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
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
for _ in range(3):
    for _ in range(3):
        plant(Entities.Tree)
        move(East)
    move(North)

move(North)
move(East)

for _ in range(60):
    do_a_flip()
#CODE
for _ in range(6):
    use_item(Items.Weird_Substance)
    move(East)
}}

---

[统计数据](docs/stats.md)      [浇水](docs/unlocks/watering.md)      [迷宫](docs/unlocks/mazes.md)

[use_item()](functions/use_item)
