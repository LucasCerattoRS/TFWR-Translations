[<- ニンジン](docs/unlocks/carrots.md) <right>[カボチャ ->](docs/unlocks/pumpkins.md)
---
# 木
[木](objects/tree)は茂みより効率よく木材を得られます。1本につき木材を5個得られます。茂みと同様に、草原にも土にも植えられます。

木はスペースを好むので、隣同士に植えると成長が遅くなります。すぐ北、東、西、または南のタイルに木がある場合、その木1本につき成長時間が2倍になります。したがって、すべてのタイルに木を植えると、成長に `2*2*2*2 = 16` 倍の時間がかかります。
{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 10,
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
for i in range(get_world_size()):
	for j in range(get_world_size()):
		plant(Entities.Tree)
		move(North)
	move(East)
}}

<spoiler=表示> 
ここでは `%` 演算子が役立ちます。`%` 演算子は割り算の余りを返すことを思い出してください。偶数を `2` で割ると余りは `0`、奇数を `2` で割ると余りは `1` になります。
なので、数値が偶数かどうかは次のようにチェックできます：

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
def is_even(n):
	return n % 2 == 0

print("is_even(0): ", is_even(0))
print("is_even(1): ", is_even(1))
print("is_even(2): ", is_even(2))
print("is_even(5): ", is_even(5))
print("is_even(-1): ", is_even(-1))
print("is_even(x): ", is_even(get_pos_x()))
}}
</spoiler>

---

[統計](docs/stats.md)      [演算子](docs/scripting/operators.md)      [if文](docs/scripting/if.md)      [forループ](docs/scripting/for.md)      [混作](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)
