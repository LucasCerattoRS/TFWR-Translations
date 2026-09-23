[<- 胡萝卜](docs/unlocks/carrots.md) <right>[南瓜 ->](docs/unlocks/pumpkins.md)
---
# 树
[树](objects/tree)是比灌木获取的木材效率更高。每棵树能提供 5 份木材。它们和灌木一样，可以种植在草地或耕过的土地上。

树喜欢保持一定的空间，相邻的两棵树生长速度会减慢。每在其正北、正东、正西或正南方向地块上种植一棵树，都会使其生长时间翻倍。所以如果在每个地块上都种上树，它们的生长时间将是原来的 `2*2*2*2 = 16` 倍。

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

<spoiler=显示>此时 `%` 运算符或许可以派上用场。记住，`%` 运算符会返回除法的余数。偶数除以 `2` 的余数是 `0`，奇数除以 `2` 的余数是 `1`。
所以你可以像这样检查一个数是否是偶数：

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

[统计数据](docs/stats.md)      [运算符](docs/scripting/operators.md)      [If 语句](docs/scripting/if.md)      [For 循环](docs/scripting/for.md)      [混合种植](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)
