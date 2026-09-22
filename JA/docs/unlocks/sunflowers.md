
[<- 水やり](docs/unlocks/watering.md)
---
# ヒマワリ
[ヒマワリ](objects/sunflower)は太陽のパワーを集めます。そのパワーを収穫できます。

植え方は、ニンジンやカボチャと全く同じです。

成長したヒマワリを収穫すると、パワーが得られます。
農場にヒマワリが10本以上あり、その中で最も花びらの数が多いものを収穫すると、`8`倍のパワーが手に入ります！
もし、より花びらの数が多いヒマワリが他にある状態で収穫してしまうと、次に収穫するヒマワリも通常のパワーしか得られなくなります（8倍ボーナスは適用されません）。

`measure()` はドローンの下のヒマワリの花びらの数を返します。
ヒマワリの花びらは最低 `7`枚、最高 `15`枚です。
ヒマワリは完全に成長する前でも測定でき、10本のヒマワリの上限に数えられます。

複数のヒマワリが同じ花びらの数を持つことがあるため、最も花びらの数が多いヒマワリも複数存在する可能性があります。この場合、どれを収穫しても構いません。

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "inventory_scale": 5,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "carrot", "n": 10}],
    "world_size": {"x": 5, "y": 2},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 4,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(North)
for _ in range(5):
    till()
    plant(Entities.Sunflower)
    move(East)
move(North)
do_a_flip()
do_a_flip()
do_a_flip()
do_a_flip()
do_a_flip()
#CODE
for _ in range(5):
    till()
    plant(Entities.Sunflower)
    print(measure())
    move(East)
for _ in range(5):
    while not can_harvest():
        pass
    harvest()
    move(East)
}}

パワーがある限り、ドローンはそれを使って2倍の速さで動きます。
30回のアクション（移動、収穫、植え付けなど）ごとに1パワーを消費します。
他のコードステートメントを実行することでもパワーを使用しますが、ドローンのアクションよりはるかに少ないです。

一般的に、スピードアップグレードで速くなるものはすべて、パワーによっても速くなります。
パワーでスピードアップするものはすべて、スピードアップグレードを無視して、実行にかかる時間に比例してパワーを消費します。

---

[統計](docs/stats.md)      [リスト](docs/scripting/lists.md)      [辞書](docs/scripting/dicts.md)      [変数](docs/scripting/variables.md)      [forループ](docs/scripting/for.md)      [if文](docs/scripting/if.md)      [演算子](docs/scripting/operators.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [measure()](functions/measure)