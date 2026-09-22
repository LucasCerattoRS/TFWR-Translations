[<- Расширение 1](docs/unlocks/expand_1.md)
---
# Расширение 2
Ферма снова выросла! Клетки больше не расположены аккуратным рядом, поэтому тебе нужно найти способ облететь квадратное поле.

Цикл `while` тут не поможет, пока ты не разблокируешь датчики и операторы.
Пришло время познакомиться с циклом `for`.

Ты можешь прочитать все о цикле `for` на странице [Цикл `for`](docs/scripting/for.md). Пока он понадобится только для того, чтобы повторить код определенное количество раз.

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
for i in range(5):
	do_a_flip()
}}

`range(n)` создает последовательность из `n` чисел от `0` до `n - 1`. Цикл `for` выполняет свой блок по одному разу для каждого элемента последовательности. В этом примере `do_a_flip()` будет вызвана `5` раз.

Тебе также доступна функция `get_world_size()`. Она возвращает длину стороны фермы. Таким образом, ты можешь писать код, который не перестанет работать при следующем улучшении расширения.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 3},
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
do_a_flip()
#CODE
for i in range(get_world_size()):
	harvest()
	move(North)
}}

В этом примере дрон собирает урожай с одного столбца на ферме любого размера.

Если ты не понимаешь, как перемещать дрон по ферме, посмотри подсказку ниже.
<spoiler=показать подсказку>Конечно, есть несколько способов перемещения по ферме.
Однако нам нужен способ облетать ее систематически, чтобы код не перестал работать при следующем улучшении фермы.
Систематический способ добраться до любого места на ферме — это вечно повторять следующие два шага:

1. Двигайся на `North`, пока дрон не окажется с противоположной стороны.
2. Двигайся на `East`.

Для воплощения этой идеи в коде может подойти такая запись: `for i in range(get_world_size()):`.
</spoiler>
<spoiler=показать возможное решение>
{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 3},
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
do_a_flip()
#CODE
for i in range(get_world_size()):
	for j in range(get_world_size()):
		#сделать сальто на каждой клетке
		do_a_flip()
		move(North)
	move(East)
}}
</spoiler>

---

[Цикл for](docs/scripting/for.md)      [Цикл while](docs/scripting/while.md)      [Переменные](docs/scripting/variables.md)

[move()](functions/move)      [get_world_size()](functions/get_world_size)
