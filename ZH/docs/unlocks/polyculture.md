[<- 南瓜](docs/unlocks/pumpkins.md)
---
# 混合种植
你可能已经注意到，有时植物种在一起时的产量会更高。
草、灌木、树和胡萝卜在有合适的“伴生植物”时产量更高。每个植物的伴生偏好都不同，这是随机的，无法预测。还好，无人机下方地块上的植物的伴生属性可以通过调用 `get_companion()` 函数来获取。结果会返回一个元组，其中第一个元素是植物想要的伴生植物类型，第二个元素则是它想要伴生植物种下的位置（坐标）。伴生植物无需完全成熟，就能提供产量加成。

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
    "operation_ticks": 20,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Bush)
plant_type, (x, y) = get_companion()
print(plant_type, (x, y))
move(East)
move(South)
plant(plant_type)
move(West)
move(North)
do_a_flip()
harvest()
}}

具有伴生属性的植物种类只有 `Entities.Grass`、`Entities.Bush`、`Entities.Tree` 和 `Entities.Carrot` 这四种。每个植物都会随机选择与自身种类不同的植物作为伴生对象；伴生对象的位置可以在距植物三步以内的任何地块，但不会是植物自身的位置。

如果无人机下方没有具有伴生偏好的植物，调用 `get_companion()` 函数将返回 `None`。

首次解锁混合种植之前，产量乘数为 `5`。此后每次升级都会翻倍。

---

[统计数据](docs/stats.md)      [元组](docs/scripting/tuples.md)      [字典](docs/scripting/dicts.md)      [感官](docs/unlocks/senses.md)      [种植](docs/unlocks/plant.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [get_companion()](functions/get_companion)
