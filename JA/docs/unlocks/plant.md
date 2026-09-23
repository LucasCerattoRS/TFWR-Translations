[<- スピードアップグレード](docs/unlocks/speed.md) <right>[ニンジン ->](docs/unlocks/carrots.md)
<right>[デバッグ ->](docs/scripting/debug.md)
<right>[演算子 ->](docs/scripting/operators.md)
---
# 植える
草は自動的に成長するのでいいですね。他のすべての植物は `plant()` 関数で植える必要があります。今植えられる唯一の植物は茂みです。
植えたい植物の種類を次のように関数に渡すことができます:

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
plant(Entities.Bush)
}}

これにより、ドローンの下に茂みが植えられます。

`clear()` を呼び出すと、農場がすべて草に戻り、ドローンの位置がリセットされます。

農場で同時に複数の種類の植物を育てると、収穫量が増えることがあるようです。詳細については、混作を研究する必要があります。

---

[統計](docs/stats.md)      [if文](docs/scripting/if.md)      [感覚](docs/unlocks/senses.md)      [混作](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)
