[<- 蘑菇](docs/unlocks/mushroom.md)
---
# 炸药

这种革命性的爆炸物是以前的采矿队留下的。（不）幸的是，你的钻头正好能引爆炸药，把周围的地块炸开。

想安全地开采炸药，你得找到由 `Grounds.Dynamite` 和 `Grounds.Soot` 组成的双层地层。上层的炸药已经有些老化，其中一些地块可以安全挖掘。不过，还有一些炸药仍会在挖掘时爆炸。

{{codeexample 
{
    "camera_position": {"x": -3, "y": -3, "z": 12},
    "show_image": true,
    "image_size": {"x": 900, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "hay", "n": 100}],
    "world_size": {"x": 5, "y": 5},
    "execution_speed": 8,
    "digging_speed": 8,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 4,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal", "quartz", "petrified_pumpkins"]
}
#SETUP
jump(Unlocks.Dynamite)
#CODE
while get_ground_type() != Grounds.Soot:
    dig()
dig()
dig()
}}

你能找出并挖掉所有哑弹，只留下仍会爆炸的地块吗？炸药层消失时，每个周围只剩活炸药或煤烟地块的活炸药地块，都会给你带来额外的炸药。

好在下方的煤烟地块可以帮忙：它们能检测相邻的炸药地块中有多少仍会爆炸。不过，它们只告诉你总数，不会指出具体是哪些地块，因此你需要结合多个煤烟地块的读数自行推断。

在煤烟地块上调用 `measure()`，会返回上方炸药层周围八个地块中活炸药的数量。结果介于 `0`（没有活炸药）和 `8`（每个相邻地块都有活炸药）之间。

炸药层中第一次挖到的一定是哑弹。每挖掉一个炸药地块都会获得少量炸药。炸药层被摧毁时，无论是成功挖光哑弹，还是不慎挖中活炸药，你还会获得额外的炸药，其数量等于完全暴露的活炸药地块数的平方。

如果挖到活炸药，两个地层都会爆炸。在挖入 `Grounds.Dynamite` 后，可以使用 `get_ground_type()` 检查是否发生了爆炸。如果地面不是 `Grounds.Soot`，说明解谜失败。反之，如果挖掉最后一个非活炸药地块，所有炸药地块都会消失，并获得该谜题的最大产量。煤烟地层会保留下来，但 `measure()` 会返回 `None`，表示谜题已成功解开。

`# 挖掘炸药地块并检查谜题状态
def dig_dynamite():
    dig()
    if get_ground_type() != Grounds.Soot:
        # 挖到活炸药，谜题失败
        return False
    elif measure() == None:
        # 挖掉最后一个哑弹地块，谜题成功
        return True
    else:
        # 测量得到一个数字，谜题仍在进行中
        return None
`

炸药层中的活炸药数量会随着深度增加，找出它们也会越来越难。

收集到的炸药可以通过 `use_item(Items.Dynamite)` 使用，并立即在无人机下方爆炸。

升级炸药可以提高挖掘炸药地块和完全暴露活炸药地块的产量，还会使炸药爆炸的能量提高 30%。

---

[统计数据](docs/stats.md)      [地下感官](docs/unlocks/underground_senses.md)      [字典](docs/scripting/dicts.md)      [集合](docs/scripting/sets.md)

[move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)      [use_item()](functions/use_item)
