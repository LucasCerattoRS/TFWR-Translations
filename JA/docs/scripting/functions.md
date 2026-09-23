[<- 変数](docs/scripting/variables.md) <right>[インポート ->](docs/scripting/import.md)
---
# 関数
`def` キーワードを使って新しい関数を定義します:
`def f(arg1, arg2 = False):
	#関数のコード`

呼び出し演算子 `()` を使って関数を呼び出すことができます:
`f(42)`

関数のローカル変数とグローバル変数については、[スコープ](docs/scripting/scopes.md) も参照してください。

## はじめに
`harvest()` のような組み込み関数はすでに見てきましたね。
独自の関数を定義することもでき、これによりコードをモジュール式に構成できます。基本的には、コードブロックに名前を付けて、好きな場所から呼び出せるようにするものです。

## 関数の定義
例えば、ドローンを数回移動させる関数を定義できます。

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
def move_n_dir(n, dir):
	for i in range(n):
		move(dir)
}}

`def` キーワードは、これが関数定義であることを示します。
`move_n_dir` は関数が割り当てられる名前です。これは任意の有効な変数名にすることができ、関数を呼び出すために使用されます。
`n` と `dir` はパラメータです。これらは関数に渡される値を保持する変数です（これらの値は引数とも呼ばれます）。関数定義には好きなだけパラメータを追加できます。
`:` の後には、関数が呼び出されたときに実行されるコードブロックが続きます。

次のコードでは、ドローンを `North` に `2` タイル、`East` に `2` タイル移動させます。

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
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def move_n_dir(n, dir):
	for i in range(n):
		move(dir)

move_n_dir(2, North)
move_n_dir(2, East)
}}

`def function():` を見たら、実際には次のような変数代入だと考えてください:
`function = create_new_function_object()`
すべての代入と同様に、代入される前に変数を使用することはできません！
`def` 文は、関数呼び出しの前に実行される必要があります。
このコードはエラーを発生させます:

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
func()
def func():
	pass
}}

## 戻り値
`return` キーワードを使って、関数に値を返させます。
例えば、次の関数は排他的論理和（XOR）の操作を定義します。排他的論理和は、一方の値が `True` で他方が `False` の場合に `True` を返します:

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
#CODE
def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()
}}

[タプル](docs/scripting/tuples.md)を使うと、複数の値を返せます。

## デフォルト引数
引数が渡されなかった場合に使用されるデフォルト値を割り当てることもできます。

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
#CODE
def f(a = False):
	if a:
		do_a_flip()

f()

f(True)
}}

デフォルト値を持つ引数の後に、デフォルト値を持たない引数を続けることはできません。

## 高度な関数の使い方
関数は他の値と同じように値であり、`def` 文は代入文のように機能し、関数を与えた名前に割り当てます。
これにより、次のようなことができます:

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
#CODE
def f():
	def d():
		do_a_flip()
	return d

f()()
}}

ここで `f()` は関数 `f` を呼び出し、`f` は新しい関数 `d` を定義して返します。2番目の `()` は返された関数を実行し、フリップを実行します。
（何が起こっているのか分かりにくいため、このようなことをするのは通常良い考えではありません）

他の関数を引数として取る関数を使うと、非常に創造的になれます:

{{codeexample 
{
    "camera_position": {"x": -2, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "fertilizer", "n": 4}],
    "world_size": {"x": 5, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def f(g, arg):
	for _ in range(4):
		g(arg)

f(move, East)
plant(Entities.Tree)
f(use_item, Items.Fertilizer)
}}

---

[変数](docs/scripting/variables.md)      [名前スコープ](docs/scripting/scopes.md)      [タプル](docs/scripting/tuples.md)      [インポート](docs/scripting/import.md)
