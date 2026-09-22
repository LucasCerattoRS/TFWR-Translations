[<- カボチャ](docs/unlocks/pumpkins.md) <right>[恐竜 ->](docs/unlocks/dinosaurs.md)
---
# サボテン
他の植物と同様に、[サボテン](objects/cactus)は土壌で育て、通常通り収穫できます。

しかし、サボテンにはさまざまなサイズがあり、奇妙な順序感覚を持っています。

完全に成長したサボテンを収穫し、隣接するすべてのサボテンがソートされた順序である場合、隣接するすべてのサボテンも再帰的に収穫します。

サボテンがソートされた順序と見なされるのは、`North` と `East` に隣接するすべてのサボテンが完全に成長し、サイズが同じかそれ以上であり、`South` と `West` に隣接するすべてのサボテンが完全に成長し、サイズが同じかそれ以下である場合です。

収穫が広がるのは、隣接するすべてのサボテンが完全に成長し、ソートされた順序である場合のみです。
つまり、成長したサボテンの正方形がサイズ順にソートされており、1つのサボテンを収穫すると、正方形全体が収穫されます。

完全に成長したサボテンは、ソートされていない場合は茶色に見えます。ソートされると、再び緑色になります。

収穫されたサボテンの数の2乗に等しいサボテンを受け取ります。つまり、`n`個のサボテンを同時に収穫すると、`n**2`個の`Items.Cactus`を受け取ります。

サボテンのサイズは `measure()` で測定できます。
それは常にこれらの数値のいずれかです: `0,1,2,3,4,5,6,7,8,9`。

`measure(direction)` に方向を渡して、ドローンのその方向の隣接タイルを測定することもできます。

`swap()` コマンドを使用して、サボテンを任意の方向の隣と交換できます。
`swap(direction)` は、ドローンの下のオブジェクトを、ドローンの `direction` に1タイル先のオブジェクトと交換します。

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
    "items": [{"item": "pumpkin", "n": 32}],
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
for _ in range(4):
    for _ in range(4):
        till()
        plant(Entities.Cactus)
        move(East)
    move(North)
for _ in range(4):
    for _ in range(4):
        for _ in range(4):
            x,y = get_pos_x(), get_pos_y()
            if x > 0 and measure(West) > measure():
                swap(West)
            if y > 0 and measure(South) > measure():
                swap(South)
            if x < 3 and measure(East) < measure():
                swap(East)
            if y < 3 and measure(North) < measure():
                swap(North)
            move(East)
        move(North)
move(East)
move(North)
move(North)
swap(West)
swap(South)
swap(East)
swap(North)
#CODE
swap(North)
swap(East)
swap(South)
swap(West)
harvest()
}}

## 数値の例
これらの各グリッドでは、すべてのサボテンがソートされた順序であり、収穫はフィールド全体に広がります:
`3 4 5    3 3 3    1 2 3    1 5 9
2 3 4    2 2 2    1 2 3    1 3 8
1 2 3    1 1 1    1 2 3    1 3 4`

このグリッドでは、左下のサボテンのみがソートされた順序であり、広がるには不十分です:
`1 5 3
4 9 7
3 3 2`

<spoiler=ヒント1を表示>
行がすでにソートされている場合、列をソートしても行のソートは崩れません。
</spoiler>
<spoiler=ヒント2を表示>
よく知られた巧妙なソートアルゴリズムはたくさんあります。詳しくなければ調べて、この問題に応用できるものを考えてみてください。ただし、隣接するサボテンしか交換できないため、すべてが使えるわけではありません。
</spoiler>
<spoiler=ヒント3を表示>
「バブルソート」は、おそらく最も単純なソートアルゴリズムです。要素を繰り返し調べ、順番が逆になっている隣同士を交換します。交換するものがなくなるまで続けます。

サボテンで行うと、次のようになります：
{{codeexample 
{
    "camera_position": {"x": -4, "y": 1, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "pumpkin", "n": 18}],
    "world_size": {"x": 9, "y": 1},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
for _ in range(9):
    till()
    plant(Entities.Cactus)
    move(East)
sorted = False
while not sorted:
    sorted = True
    for _ in range(9):
        move(East)
        if get_pos_x() > 0 and measure(West) > measure():
            swap(West)
            sorted = False
harvest()
}}
もちろん、この方法を改善する方法はたくさんあります！
1行をソートできたら、ヒント1を使って農場全体をソートできます。
</spoiler>

---

[統計](docs/stats.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [swap()](functions/swap)      [measure()](functions/measure)
