[<- はじめに](docs/getting_started.md) <right>[whileループ ->](docs/scripting/while.md)
---
# 最初のプログラム
## テキストエディタ
すべてのプログラミングはコードウィンドウで行われます。各コードウィンドウは、コードを含むテキストファイルに対応しています。
ウィンドウの上部にあるファイル名をクリックして、ファイルの名前を変更できます。

コードが実行中でない限り、任意のテキストエディタのようにコードを編集できます。
コードウィンドウの緑色の再生ボタンを押すと、プログラムを直接実行できます。
![|x50](PlayButton)

画面の右上隅にある「+」ボタンを使用して、さらにコードファイルを作成できます。
ウィンドウを別のウィンドウにドラッグしてドッキングできます。

入力を開始すると、単純なコード補完ウィンドウがポップアップ表示されることに気付くでしょう。
Tabキーを押すと、選択中の補完候補が挿入されます。
矢印キーを使用して、補完オプションをナビゲートします。

プログラミングが初めてでも心配しないでください。言語は段階的にアンロックされるため、できることすべてに圧倒されることはありません。
構文も、世界で最も広く使われているプログラミング言語の1つであるPythonに似ているため、ここで学んだことは他でも役立ちます。

すでにPythonを知っている場合も大丈夫です。序盤をすばやく進めて、もっと面白いところへ進めます。

現在、2つのドローンコマンドが利用可能です。

`harvest()`

と

`do_a_flip()`

これらは関数呼び出しです。関数は実行できるコマンドと考えることができます。`()`括弧を使用して実行します。

これらのステートメントをコードウィンドウに入力し、実行ボタンを押してみてください。

コードはステートメントのシーケンスと考えることができます。複数のステートメントを別々の行に書けば、順番に実行できます。
以下の埋め込みコードウィンドウの再生ボタンを押して、コードがどう実行されるか見てみましょう：

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
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
do_a_flip()
harvest()
harvest()
}}

## アンロック
草を集めると干し草が手に入ります。干し草はアンロックツリーでループをアンロックするために使用できます。画面右上のボタンでアンロックツリーを開きます。

---

[外部エディタ](docs/external_editor.md)      [コメント](docs/scripting/comments.md)      [whileループ](docs/scripting/while.md)

[harvest()](functions/harvest)      [do_a_flip()](functions/do_a_flip)
