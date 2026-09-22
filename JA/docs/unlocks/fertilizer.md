[<- 水やり](docs/unlocks/watering.md) <right>[迷路 ->](docs/unlocks/mazes.md)
---
# 肥料
ある時点で、植物が育つのを待つだけでは効率が悪くなります。
水と同様に、10秒ごとに自動的に肥料を1つ受け取ります。アップグレードするたびに、受け取る量は倍になります。

肥料は植物を即座に成長させることができます。`use_item(Items.Fertilizer)` は、ドローンの下の植物の残りの成長時間を2秒短縮します。

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

これにはいくつかの副作用があります。
肥料で育てられた植物は感染します。

植物が感染すると、収穫時にその収穫量の半分が `Items.Weird_Substance` に変わります。
奇妙な物質は植物にも使用でき、その植物と隣接するすべての植物の感染状態を切り替える効果があります。

なので、感染した植物に `use_item(Items.Weird_Substance)` を呼び出すと治癒しますが、健康な植物に使用すると感染します。

健康な隣りがいる感染した植物に使用すると、その植物は治癒しますが、隣りは感染し、その逆も同様です。

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

[統計](docs/stats.md)      [水やり](docs/unlocks/watering.md)      [迷路](docs/unlocks/mazes.md)

[use_item()](functions/use_item)