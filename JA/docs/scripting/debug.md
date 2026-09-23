[<- 植える](docs/unlocks/plant.md) <right>[デバッグ 2 ->](docs/unlocks/debug2.md)
<right>[タイミング ->](docs/unlocks/timing.md)
---
# デバッグ
コードがうまく動かない時、その原因を突き止める必要があります。そのために役立つツールがいくつかあります。

1つ目は、プログラムをステップごとに実行することです。
実行ボタンの隣のボタンを使うか、ブレークポイントを設定することで、ステップ実行モードに入れます。

ブレークポイントは、コードの左側にあるブレークポイントパネルをクリックすることで追加できます。
![|x227](Breakpoints)
実行がブレークポイントのある行に到達すると、自動的にステップ実行モードに切り替わります。

変数にマウスカーソルを合わせると、その現在の値が表示されます。

`print()` 関数も非常に便利です。渡された値を何でも空中に直接書き出します。

例：

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
print(0.24)
}}

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
print(can_harvest())
}}

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
print(get_pos_x(), get_pos_y())
}}

`print()` 関数は、値を空中に直接、そして[出力](docs/output.md)ページに表示します。

たくさんの値を表示したい場合、空中に書き出すのは少し遅いことがあります。
その場合は、出力ウィンドウにのみ表示する `quick_print()` 関数を使用できます。

出力ウィンドウには警告やエラーも記録されるので、何かが期待通りに動かない場合は、そこをチェックすると役立つことがあります。

実行が停止すると、出力はゲームフォルダー内の [output.txt](persistent_data_path/output.txt) ファイルにも書き込まれます。

---

[出力](docs/output.md)      [コメント](docs/scripting/comments.md)      [デバッグ 2](docs/unlocks/debug2.md)      [カラフルなブロック](docs/unlocks/debug_place.md)      [シミュレーション](docs/unlocks/simulation.md)

[print()](functions/print)      [quick_print()](functions/quick_print)
