[<- 演算子](docs/scripting/operators.md)
---
# 感覚
ドローンの目が見えるようになりました！

関数 `get_pos_x()` と `get_pos_y()` は、ドローンの現在のx座標とy座標を返します。開始位置では両方とも `0` です。x座標は `East` に向かってタイルごとに `1` ずつ増加し、y座標は `North` に向かってタイルごとに `1` ずつ増加します。
{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 2},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(East)
#CODE
print("x =", get_pos_x(), "y =", get_pos_y())
if get_pos_x() == 1 and get_pos_y() == 0:
    do_a_flip()
}}

`num_items(item)` は、持っているアイテムの数を返します。
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 10}],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
print(num_items(Items.Hay))
}}

`get_entity_type()` と `get_ground_type()` は、ドローンの下にあるエンティティまたは地面の種類を返します。
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
plant(Entities.Bush)
#CODE
print(get_entity_type())
if get_entity_type() == Entities.Bush:
	do_a_flip()

print(get_ground_type())
if get_ground_type() != Grounds.Soil:
	do_a_flip()
}}

`None` キーワードもアンロックされました！ `None` は値がないことを表す値です。
例えば、`return` 文がない関数は実際には `None` を返します。

ドローンの下にエンティティがない場合、`get_entity_type()` は `None` を返します。


特定のアンロックをいくつ持っているかを知りたい場合は、`num_unlocked(unlock)` 関数を使用します。

例えば、`num_unlocked(Unlocks.Speed)` は持っているスピードアップグレードの数を返します。

`num_unlocked(Unlocks.Senses)` は、感覚がアンロックされていれば `1` を、そうでなければ `0` を返します。

`num_unlocked()` はアイテムやエンティティにも使用できます。アンロックされていれば `1` を、そうでなければ `0` を返します。

`num_unlocked(Unlocks.Carrots)` は、それがアンロック/アップグレードされた回数を返すので注意してください。
`num_unlocked(Items.Carrot)` は `0` または `1` のみを返します。（他の植物も同様です）

---

[if文](docs/scripting/if.md)      [演算子](docs/scripting/operators.md)      [変数](docs/scripting/variables.md)      [タプル](docs/scripting/tuples.md)      [辞書](docs/scripting/dicts.md)      [地下の感覚](docs/unlocks/underground_senses.md)

[get_pos_x()](functions/get_pos_x)      [get_pos_y()](functions/get_pos_y)      [get_entity_type()](functions/get_entity_type)      [get_ground_type()](functions/get_ground_type)      [num_items()](functions/num_items)      [num_unlocked()](functions/num_unlocked)
