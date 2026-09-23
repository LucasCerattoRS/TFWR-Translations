[<- 南瓜](docs/unlocks/pumpkins.md) <right>[恐龙 ->](docs/unlocks/dinosaurs.md)
---
# 仙人掌
像其他植物一样，[仙人掌](objects/cactus)可以种植在耕过的土地上并收获。

然而，仙人掌大小不一，并有一种奇怪的秩序感。

如果收获一株完全成熟的仙人掌，并且所有相邻的仙人掌都已排序，则所有相邻的仙人掌也会以递归方式收获。

如果所有 `North`(上边) 和 `East`(右边) 方向的相邻仙人掌都完全成熟且尺寸大于或等于自身，并且所有 `South`(下边) 和 `West`(左边) 方向的相邻仙人掌都完全成熟且尺寸小于或等于自身，那么这个仙人掌就被认为是处于已排序状态。

当所有相邻的仙人掌都完全成熟并处于已排序状态时，可以触发“连锁收集”。
也就是说，如果一个方形区域的成熟仙人掌已经按大小排序，那么收获其中一株仙人掌时，会收获整个方形区域。

一株完全成熟的仙人掌如果未排序，会显示为棕色。一旦排序好，则会变回绿色。

你将获得的仙人掌数量等于所收获仙人掌数量的平方。因此，如果同时收获 `n` 个仙人掌，则将获得 `n**2` 个 `Items.Cactus`。

仙人掌的大小可以调用 `measure()` 函数获取。
获取的结果始终为以下数字之一：`0,1,2,3,4,5,6,7,8,9`。

你也可以向 `measure(direction)` 函数传入 1 个方向参数来获取无人机对应方向上的相邻地块的仙人掌大小。

调用 `swap()` 函数可将 1 株仙人掌与其任何方向的邻居交换位置。
`swap(direction)` 将无人机下方的物体与无人机 `direction` 方向 1 格处的物体交换位置。

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "pumpkin", "n": 32}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
for _ in range(4):
    for _ in range(4):
        till()
        plant(Entities.Cactus)
        move(East)
    move(North)
for _ in range(4):
    for _ in range(4):
        for _ in range(4):
            x,y = get_pos_x(), get_pos_y()
            if x > 0 and measure(West) > measure():
                swap(West)
            if y > 0 and measure(South) > measure():
                swap(South)
            if x < 3 and measure(East) < measure():
                swap(East)
            if y < 3 and measure(North) < measure():
                swap(North)
            move(East)
        move(North)
move(East)
move(North)
move(North)
swap(West)
swap(South)
swap(East)
swap(North)
#CODE
swap(North)
swap(East)
swap(South)
swap(West)
harvest()
}}

## 数字示例
在这些网格中，所有的仙人掌都处于已排序状态，可以连锁收获整片田地：
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

在下面网格中，只有左下角的仙人掌处于已排序状态，这还无法触发“连锁收集”：
`1 5 3
4 9 7
3 3 2`

<spoiler=显示提示 1>
如果行已经排序，对列进行排序时，不会打乱行的顺序。
</spoiler>
<spoiler=显示提示 2>
如果不熟悉排序算法，不如“百度一下”，思考可以参照哪些算法来解决这个问题。当然，并不是所有算法都有效，因为你只能交换相邻的仙人掌。
</spoiler>
<spoiler=显示提示 3>
“冒泡排序”或许是最简单的排序算法。它的思路是反复遍历元素，将顺序不对的相邻元素交换，直到所有元素都排好序。

下面是用仙人掌演示的效果：
{{codeexample 
{
    "camera_position": {"x": -4, "y": 1, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "pumpkin", "n": 18}],
    "world_size": {"x": 9, "y": 1},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
for _ in range(9):
    till()
    plant(Entities.Cactus)
    move(East)
sorted = False
while not sorted:
    sorted = True
    for _ in range(9):
        move(East)
        if get_pos_x() > 0 and measure(West) > measure():
            swap(West)
            sorted = False
harvest()
}}
当然，这个策略还有很多改进空间！
当你成功排好一整行后，就可以利用提示 1 来对整片田地排序。
</spoiler>

---

[统计数据](docs/stats.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [swap()](functions/swap)      [measure()](functions/measure)
