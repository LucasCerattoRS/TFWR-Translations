[<- 迷路](docs/unlocks/mazes.md)
---
# メガファーム
この信じられないほど強力なアンロックにより、複数のドローンにアクセスできるようになります。
{{codeexample 
{
    "camera_position": {"x": -3, "y": 2.1, "z": 7},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": true,
    "collapsing": false,
    "autoplay": true,
    "items": [],
    "world_size": {"x": 7, "y": 7},
    "execution_speed": 21,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(North)
move(North)
move(North)
move(East)
move(East)
move(East)
change_hat(Hats.Wizard_Hat)
#CODE
def harvest_spiral(radius):
    for i in range(1, radius, 2):
        harvest()
        move(West)
        for j in range(i):
            harvest()
            move(South)
        for j in range(i+1):
            harvest()
            move(East)
        for j in range(i+1):
            harvest()
            move(North)
        for j in range(i+1):
            harvest()
            move(West)

while True:
    spawn_drone(harvest_spiral, 7)
    do_a_flip()
}}

以前と同様に、最初は1台のドローンから始まります。追加のドローンはまずスポーンさせる必要があり、プログラムが終了すると消えます。
各ドローンは独自の別のプログラムを実行します。新しいドローンは `spawn_drone(function)` 関数を使用してスポーンできます。

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def drone_function():
    move(East)
    do_a_flip()

spawn_drone(drone_function)
do_a_flip()
}}

これにより、`spawn_drone(function)` コマンドを実行したドローンと同じ位置に新しいドローンがスポーンします。新しいドローンは指定された関数の実行を開始します。それが終わると、最後に残ったドローンでない限り自動的に消えます。

ドローンは互いに衝突しません。

同時に存在できるドローンの最大数を取得するには `max_drones()` を使用します。
農場にすでにいるドローンの数を取得するには `num_drones()` を使用します。


## 例:
{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)
}}

これにより、最初のドローンが水平に移動し、より多くのドローンをスポーンします。スポーンされたドローンは垂直に移動し、その経路にあるすべてを収穫します。

利用可能なすべてのドローンがすでにスポーンされている場合、`spawn_drone()` は何もしないで `None` を返します。

各ドローンに異なる方向を渡す、もう一つの例です。
{{codeexample 
{
    "camera_position": {"x": -1, "y": 2, "z": 5},
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
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(North)
move(East)
#CODE
for dir in [North, East, South, West]:
    def task():
        move(dir)
        do_a_flip()
    spawn_drone(task)
}}

## すべてのドローンは平等
特別な「メイン」ドローンはありません。すべてのドローンが他のドローンをスポーンでき、すべてドローンの上限にカウントされます。すべてのドローンは終了すると消えます。最初のドローンがプログラムを早く終了した場合、別のドローンがコードのハイライトで実行が可視化されるものになります。すべてのドローンがブレークポイントをトリガーでき、ドローンがブレークポイントをトリガーすると、コードのハイライトはそのドローンに切り替わります。

<spoiler=ヒントを表示> 
この非常に便利な並列 `for_all` 関数をチェックしてください。これは任意の関数を受け取り、すべての農場のタイルで実行します。そのために利用可能なすべてのドローンを使用します。

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def for_all(f):
	def row():
		for _ in range(get_world_size()-1):
			f()
			move(East)
		f()
	for _ in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(North)

for_all(harvest)
}}

特に便利なパターンの一つは、利用可能なドローンがいればスポーンし、そうでなければ自分でやることです。

`if not spawn_drone(task):
	task()`
</spoiler>

## 他のドローンを待つ
別のドローンが終了するのを待つには `wait_for(drone)` 関数を使用します。ドローンをスポーンするときに `drone` ハンドルを受け取ります。
`wait_for(drone)` は、他のドローンが実行していた関数の戻り値を返します。

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
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
plant(Entities.Tree)
move(West)
#CODE
def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

drone = spawn_drone(get_entity_type_in_direction, East)
print(wait_for(drone))
}}

ドローンのスポーンには時間がかかるため、些細なことごとに新しいドローンをスポーンするのは良い考えではありません。

`has_finished(drone)` を使えば、待たなくてもドローンが終わったかどうか確認できるよ。

## 共有メモリなし
各ドローンは独自のメモリを持ち、他のドローンのグローバル変数を直接読み書きすることはできません。

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": false,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)
}}

これは `0` を表示します。なぜなら、新しいドローンは自身のグローバル `x` のコピーをインクリメントし、これは最初のドローンの `x` に影響しないからです。

## 引数の受け渡し

`spawn_drone()` は、呼び出された関数に渡される追加のオプション引数を受け入れます:

「共有メモリなし」の節が依然として適用されることに注意してください。つまり、呼び出された関数は引数のコピーに対して動作します:

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": false,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def modify(list):
	list.append('緑')
	print(list)

l = ['赤']
wait_for(spawn_drone(modify, l))
print(l)
}}

## 競合状態
複数のドローンが同時に同じ農場のタイルと対話することがあります。同じティック中に2つのドローンが同じタイルと対話すると、両方の対話が発生しますが、結果は対話の順序によって異なる場合があります。

例えば、ドローン `0` と `1` が両方ともほぼ完全に成長した同じ木の上にいると想像してください。
ドローン `0` は次を呼び出します
`use_item(Items.Fertilizer)`
ドローン `1` は次を呼び出します
`harvest()`

これらのアクションが同時に発生した場合、木はまず肥料を与えられ、次に収穫されます。その場合、木材を受け取ります。しかし、ドローン `1` がわずかに速い場合、木は肥料を与えられる前に収穫され、木材は受け取れません。
これは「競合状態」と呼ばれます。これは並列プログラミングでよくある問題で、結果は操作が実行される順序に依存します。

複数のドローンが同時に同じ位置で同じコードを実行すると、別の問題状況が発生する可能性があります。
`if get_water() < 0.5:
    use_item(Items.Water)`

複数のドローンがこれを同時に実行すると、それらはすべて最初の行を実行し、`if` ブロックに入ります。その後、それらはすべて水を使用し、多くの水を無駄にします。
ドローンが2行目に到達するまでに、他のドローンがその間にタイルに水をやったため、`get_water()` はもはや `0.5` 未満ではないかもしれません。

---

[関数](docs/scripting/functions.md)      [名前スコープ](docs/scripting/scopes.md)      [シミュレーション](docs/unlocks/simulation.md)

[spawn_drone()](functions/spawn_drone)      [num_drones()](functions/num_drones)      [max_drones()](functions/max_drones)      [wait_for()](functions/wait_for)      [has_finished()](functions/has_finished)
