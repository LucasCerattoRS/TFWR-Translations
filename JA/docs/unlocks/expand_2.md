[<- 拡張 1](docs/unlocks/expand_1.md)
---
# 拡張 2
あなたの農場が再び拡張されました！今やタイルはきれいな一列ではなくなったので、正方形のグリッドを横断する方法を見つける必要があります。

`while` ループでは、感覚と演算子をアンロックするまでこれは不可能です。
`for` ループを導入する時です。

`for` ループに関するすべては[forループ](docs/scripting/for.md)ページで読むことができますが、今のところはコードを固定回数繰り返すためにのみ必要です。

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
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
#CODE
for i in range(5):
	do_a_flip()
}}

`range(n)` は `0` から `n - 1` までの数値の範囲を作成し、それには `n` 個の要素が含まれています。`for` ループは、シーケンスの各要素に対してループ本体を一度実行します。この例では `do_a_flip()` が `5` 回呼び出されます。

関数 `get_world_size()` も利用可能になりました。これは農場の辺の長さを返します。これにより、次の拡張アップグレードで壊れないコードを書くことができます。

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
    "items": [],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
for i in range(get_world_size()):
	harvest()
	move(North)
}}

この例は、任意の農場サイズで農場の1列を収穫します。

ドローンを農場の周りで動かす方法に詰まった場合は、以下のヒントを参照してください。
<spoiler=ヒントを表示>もちろん、農場を移動する方法はいくつもあります。
私たちが探しているのは、農場が再び大きくなっても壊れない体系的な方法で横断する方法です。
農場のすべての場所に体系的に到達する方法は、次の2つのステップを永遠に繰り返すことです:

1.ラップバックするまで `North` に移動する。
2. `East` に移動する。

`for i in range(get_world_size()):` は、このアイデアをコードにするのに役立つかもしれません。
</spoiler>
<spoiler=解答例を表示>
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
    "items": [],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
for i in range(get_world_size()):
	for j in range(get_world_size()):
		#すべてのタイルで宙返りする
		do_a_flip()
		move(North)
	move(East)
}}
</spoiler>

---

[forループ](docs/scripting/for.md)      [whileループ](docs/scripting/while.md)      [変数](docs/scripting/variables.md)

[move()](functions/move)      [get_world_size()](functions/get_world_size)
