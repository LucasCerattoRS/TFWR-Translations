[<- 铁矿](docs/unlocks/iron.md)
---
# 藏宝图

传说有位早已离世的健忘海盗藏了一份难寻的宝藏——大概是这么回事吧。如果他把通往宝藏的路线画在地图上，后来又弄丢了呢？也许他被熔岩河逼到绝境时掉了地图，地图便保存在一层玄武岩下。测量玄武岩或许能发现线索。

<spoiler=告诉我更多>
留意一层 `Grounds.Basalt`。试着测量玄武岩，看看它会告诉你什么。线索或许会引你找到藏宝图；测量藏宝图一定能得到通往宝藏的路线——但你能解读地图给出的指示吗？
</spoiler>

<spoiler=直接告诉我怎么做>
好吧，方法是这样的：找到 `Grounds.Basalt` 地层，以及正下方的 `Grounds.Treasure_Map` 地块。你可以对玄武岩使用 `measure()`，得到下方地图地块的 `(x, y)` 坐标。

在地图地块上调用 `measure()`，就能得到一串表示藏宝路线的方向字母。N、E、S、W 分别代表 `North`、`East`、`South`、`West`；D 代表“向下”或“挖掘”。这些字母描述了由 `Grounds.Treasure_Path` 地块组成、通向宝藏的路线。

```
path = measure()
for letter in path:
    do_something(letter)
```

挖到藏宝图地块的那架无人机，必须亲自去寻找宝藏。它必须一直待在 `Grounds.Treasure_Path` 地块上方。如果移动到其他地块，路线就会断开，宝藏也会丢失。

路线尽头是一个 `Grounds.Treasure_Goal` 地块。如果无人机没有偏离路线，其上方就会出现 `Entities.Underground_Treasure`。无人机可以使用 `harvest()` 收获宝箱，获得金币。

金币数量与藏宝路线的长度成正比。升级藏宝图会增加路线的深度，升级扩张则能让路线有更多横向延伸的空间。两种升级都会延长藏宝路线，让你找到更多金币。
</spoiler>

---

[统计数据](docs/stats.md)      [For 循环](docs/scripting/for.md)      [元组](docs/scripting/tuples.md)      [地下感官](docs/unlocks/underground_senses.md)

[harvest()](functions/harvest)      [move()](functions/move)      [dig()](functions/dig)      [measure()](functions/measure)
