[<- Морковь](docs/unlocks/carrots.md) <right>[Тыквы ->](docs/unlocks/pumpkins.md)
---
# Деревья
[Деревья](objects/tree) дают больше древесины, чем кусты. С каждого можно получить 5 древесины. Деревья, как и кусты, можно сажать на траве и грядках.

Деревья любят простор, и если они посажены вплотную друг к другу, то растут медленнее. Время роста удваивается за каждое дерево на соседней клетке в направлении севера, востока, запада или юга. Если ты посадишь деревья на каждой клетке, они будут расти в `2*2*2*2 = 16` раз дольше.
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

<spoiler=показать> 
Здесь может пригодиться оператор `%`. Оператор `%` возвращает остаток от деления. При делении четного числа на `2` остаток равен `0`, а при делении нечетного числа на `2` — `1`.
Поэтому проверить четность числа можно так:

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

[Статистика](docs/stats.md)      [Операторы](docs/scripting/operators.md)      [If](docs/scripting/if.md)      [Цикл for](docs/scripting/for.md)      [Поликультура](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)
