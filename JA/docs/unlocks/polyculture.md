[<- カボチャ](docs/unlocks/pumpkins.md)
---
# 混作
植物を一緒に植えると収穫量が増えることがあるのに、すでにお気づきかもしれません。
草、茂み、木、ニンジンは、適切なコンパニオンプラントがあると収穫量が増えます。コンパニオンの好みは個々の植物ごとに異なり、予測することはできません。収穫量のボーナスを得るには、コンパニオンが完全に成長している必要はありません。幸いなことに、ドローンの下の植物のコンパニオンの好みは `get_companion()` を使用して測定できます。これはタプルを返し、最初の要素はコンパニオンとして望む植物の種類、2番目の要素はそのコンパニオンを望む位置です。

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

植物のコンパニオンの好みは `Entities.Grass`、`Entities.Bush`、`Entities.Tree`、または `Entities.Carrot` のいずれかになります。各植物はこれをランダムに選択しますが、常に自分自身とは異なる植物を選択します。位置も、植物自身の位置を除く、植物から3手以内の任意の位置になります。

ドローンの下にコンパニオンの好みを持つ植物がない場合、`get_companion()` は `None` を返します。

混作が初めてアンロックされる前は、収穫倍率は `5` です。アップグレードするたびに2倍になります。

---

[統計](docs/stats.md)      [タプル](docs/scripting/tuples.md)      [辞書](docs/scripting/dicts.md)      [感覚](docs/unlocks/senses.md)      [植える](docs/unlocks/plant.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [get_companion()](functions/get_companion)
