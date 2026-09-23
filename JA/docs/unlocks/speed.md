[<- whileループ](docs/scripting/while.md) <right>[拡張 1 ->](docs/unlocks/expand_1.md)
<right>[植える ->](docs/unlocks/plant.md)
---
# スピードアップグレード
実行速度が2倍になりました。問題は、ドローンが草の成長よりも速く収穫するようになり、全く収穫できなくなってしまうことです。これに対処するために、[If文](docs/scripting/if.md)分岐と[can_harvest()](functions/can_harvest)関数がアンロックされました。

## 収穫する前にチェックする
`if` ステートメントは、指定した条件が `True` の場合にコードブロックを1回実行します。

新しい関数 `can_harvest()` は、便利な条件を提供します。`can_harvest()` は、ドローンの下の植物が収穫できる場合は `True` を、そうでない場合は `False` を返します。

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
do_a_flip()
#CODE
if can_harvest():
	do_a_flip()
}}

このような戻り値は、`if` の条件を評価するときに、関数呼び出しの式 `can_harvest()` が戻り値の `True` に置き換わると考えられます。

上記のコードが実行されると、次のようになります：
- `if` ステートメントが実行されます。
	- `can_harvest()` が呼び出されます
- 草が完全に成長しているので、`can_harvest()` が `True` を返します。
	- 文は `if True:` になります
- 値が `True` なので、分岐内のコードが実行されます。

草が完全に成長していなければ、宙返りはしません。

これで `if` を使って、ドローンが早すぎる収穫をするのを防ぐことができます。

---

[if文](docs/scripting/if.md)      [whileループ](docs/scripting/while.md)

[harvest()](functions/harvest)      [can_harvest()](functions/can_harvest)
