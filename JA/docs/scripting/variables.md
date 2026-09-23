[<- 演算子](docs/scripting/operators.md) <right>[リスト ->](docs/scripting/lists.md)
<right>[関数 ->](docs/scripting/functions.md)
---
# 変数
変数は、値を保持できる名前付きのコンテナと考えることができます。
`=` 演算子は、変数を宣言して値を格納するために使用されます。

`variable_name = value`

演算子の左辺は変数名です。好きな名前を付けることができます。
右辺は式であり、その結果の値が変数に格納されます。

`a` という名前の変数を宣言し、値 `5` を格納します:
`a = 5`
`b` という名前の変数を宣言し、`can_harvest()` の戻り値を格納します:
`b = can_harvest()`

`=` 演算子と `==` 演算子を混同しないでください。
`==` 演算子は、2つの値が等しいかどうかをチェックし、`True` または `False` を返します。
`=` 演算子は、右側の値を左側の名前に割り当てます。

変数が割り当てられた後、コード内でそれを使用して含まれている値を取得できます

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
a = 5
for i in range(a):
	do_a_flip()
}}

上記のループは `a` が `5` に設定されているため、5回実行されます。
`for` ループの `i` も変数であり、ループの各反復でシーケンスの現在の値が自動的に割り当てられます。（`i` と呼ぶ必要はなく、任意の有効な変数名を付けることができます。）

変数は while ループでも同じことができます:

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
a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1
}}

これは上記の `for` ループと同じことをします。ただ `i` を手動でインクリメントする必要があります。
`i` をインクリメントするには、それ自身の値に `1` を足した値に設定することに注意してください。変数の値を以前の値に基づいて変更することは非常によくあることです。
これは次の演算子を使用して短縮できます: `+=, -=, *=, /=, %=`

`i = i + 1` は `i += 1` と同じです。
`a = a / 3` は `a /= 3` と同じです。

---

[演算子](docs/scripting/operators.md)      [whileループ](docs/scripting/while.md)      [forループ](docs/scripting/for.md)      [関数](docs/scripting/functions.md)      [名前スコープ](docs/scripting/scopes.md)
