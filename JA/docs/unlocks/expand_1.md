[<- スピードアップグレード](docs/unlocks/speed.md) <right>[拡張 2 ->](docs/unlocks/expand_2.md)
<right>[採掘 ->](docs/unlocks/mining.md)
---
# 拡張 1
あなたの農場が大きくなりました！ドローンを動かせなければこのスペースはあまり役に立たないので、ドローンを動かす新しい関数 `move()` があります。`move()` は、ドローンを動かしたい方向を指定する必要があります。これには4つの新しい定数があります: `North, East, South, West`

例えば、`move(North)` はドローンを北に1マス移動させます。

農場の端を越えて移動すると、ドローンは農場の反対側に移動します。

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 3},
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
#CODE
while True:
	move(North)
}}

---

[whileループ](docs/scripting/while.md)      [演算子](docs/scripting/operators.md)      [拡張 2](docs/unlocks/expand_2.md)

[move()](functions/move)
