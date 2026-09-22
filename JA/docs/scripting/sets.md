[<- 辞書](docs/scripting/dicts.md)
---
# セット
セットは[辞書](docs/scripting/dicts.md)に似ていますが、値がありません。順序のないキーの集合です。

辞書のように作成しますが、値はありません。
`set = {North, East, West}`

空のセットを作成するには `set()` を使用します。`{}` は空の辞書を作成することに注意してください。

セットに新しい要素を追加するには `set.add(elem)` を使用します。

セットから要素を削除するには `set.remove(elem)` を使用します。

セットに要素が含まれているかを確認するには `if elem in set:` を使用します。

セット内のすべての要素を反復処理するには `for elem in set:` を使用します。
大きなセットの場合、`in` 演算子はリストよりもはるかに高速に動作します。

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
my_set = set()
print(my_set)
my_set.add(1)
my_set.add(North)
print(my_set)
my_set.remove(North)
print(my_set)
if North in my_set:
    print("North はセットに含まれています")
else:
    print("North はセットに含まれていません")
for element in my_set:
    print(element)
}}

辞書と同様に、セットは順序がないため、要素が反復される順序についての保証はありません。

また、セット内の要素は一意であるため、すでにセットに含まれている要素を追加してもセットは変更されません。

---

[辞書](docs/scripting/dicts.md)      [リスト](docs/scripting/lists.md)      [forループ](docs/scripting/for.md)

[len()](functions/len)
