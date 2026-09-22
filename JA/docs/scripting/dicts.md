[<- リスト](docs/scripting/lists.md) <right>[コスト ->](docs/unlocks/costs.md)
---
# 辞書
辞書は、実際の辞書が単語をその定義に対応付けるのと同じように、キーを値に対応付け、非常に迅速に検索できるデータ構造です。

辞書は次のように作成できます：

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
right_of = {North:East, East:South, South:West, West:North}
}}

コロンの前の式がキーで、コロンの後の式がキーが対応する値です。
上記の辞書は、各方向をその右の方向にマッピングします。

これは、ドローンの位置をその上にあるエンティティにマッピングする別の例です。
{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}
}}

キーにマッピングされた値へのアクセスは、リスト内の要素へのアクセスに似ています：
`value = dict[key]`

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
right_of = {North:East, East:South, South:West, West:North}
print(right_of[South])
}}

辞書に新しいキーと値のペアを追加するには、次のようにします：
`dict[key] = value`

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
    "items": [],
    "world_size": {"x": 3, "y": 1},
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
plant(Entities.Bush)
move(East)
plant(Entities.Tree)
move(East)
#CODE
entity_dict = {}
for _ in range(3):
	entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()
	move(East)
print(entity_dict)
}}

キーは一意なので、辞書にすでに存在するキーを追加すると、以前の値が上書きされます。

`dict` からキーと値のペアを削除するには、`dict.pop(key)` を使用します。

`key in dict` は、`key` が `dict` のキーである場合は `True`、そうでない場合は `False` に評価されます。
したがって、`if key in dict:` を使用して `dict` にキーが含まれているかどうかを確認できます。

`for` ループで辞書を使用すると、すべてのキーを反復処理できます：
{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
right_of = {North:East, East:South, South:West, West:North}
print(North in right_of)
for key in right_of:
	value = right_of[key]
	print(key, ":", value)
}}

キーが反復される順序についての保証はありません。

参照：[セット](docs/scripting/sets.md)

---

[リスト](docs/scripting/lists.md)      [セット](docs/scripting/sets.md)      [タプル](docs/scripting/tuples.md)      [コスト](docs/unlocks/costs.md)

[len()](functions/len)