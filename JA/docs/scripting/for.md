[<- 拡張 2](docs/unlocks/expand_2.md)
---
# Forループ
`for` ループはPythonのように動作します。（一部の言語ではforeachループと呼ばれますが、C言語スタイルのforループとは異なるものです）。

`for i in sequence:
	#iを使って何かをする`

`while` ループと同様に、`for` ループもコードブロックを繰り返し呼び出します。条件に基づいてループする代わりに、シーケンスの各要素に対してループ本体を一度実行します。

## 構文
forループは次のようになります：

`for variable_name in sequence:
	#コードブロック`

`variable_name` は自由に選べる名前です。これはシーケンス内の現在の要素を格納する変数です。`sequence` は、数値の範囲のような反復可能な値である必要があります。コードブロックは、ループ変数がその要素に割り当てられた状態で、すべての要素に対して実行されます。

## シーケンス
[範囲](functions/range)      <unlock=lists>[リスト](docs/scripting/lists.md)      </unlock><unlock=functions>[タプル](docs/scripting/tuples.md)      </unlock><unlock=dicts>[辞書](docs/scripting/dicts.md)      </unlock><unlock=sets>[セット](docs/scripting/sets.md)</unlock>

## 例
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
do_a_flip()
#CODE
for i in range(5):
    harvest()
}}

このループは本体を固定回数実行します。これは本質的に次のように書くのと同じです。

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
do_a_flip()
#CODE
i = 0
harvest()
i = 1
harvest()
i = 2
harvest()
i = 3
harvest()
i = 4
harvest()
}}


---

[whileループ](docs/scripting/while.md)      [break](docs/scripting/break.md)      [continue](docs/scripting/continue.md)

[range()](functions/range)
