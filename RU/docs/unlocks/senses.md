[<- Операторы](docs/scripting/operators.md)
---
# Датчики
Дрон обрел зрение!

Функции `get_pos_x()` и `get_pos_y()` возвращают текущие координаты x и y дрона. В стартовой позиции обе равны `0`. Позиция x увеличивается на `1` за каждую клетку в направлении `East`, а позиция y — на `1` за каждую клетку в направлении `North`.
{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 2},
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
move(East)
#CODE
print("x =", get_pos_x(), "y =", get_pos_y())
if get_pos_x() == 1 and get_pos_y() == 0:
    do_a_flip()
}}

`num_items(item)` возвращает имеющееся количество предмета.
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 10}],
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
print(num_items(Items.Hay))
}}

`get_entity_type()` и `get_ground_type()` возвращают тип объекта-сущности или земли, которая находится под дроном.
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
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
plant(Entities.Bush)
#CODE
print(get_entity_type())
if get_entity_type() == Entities.Bush:
	do_a_flip()

print(get_ground_type())
if get_ground_type() != Grounds.Soil:
	do_a_flip()
}}

Теперь разблокировано ключевое слово `None`! `None` — это значение, показывающее отсутствие значения.
Например, функция, у которой нет инструкции `return`, вернет `None`.

`get_entity_type()` возвращает `None`, если под дроном нет объекта-сущности.


Если ты хочешь узнать количество имеющихся у тебя технологий, используй функцию `num_unlocked(unlock)`.

Например, `num_unlocked(Unlocks.Speed)` вернет количество имеющихся повышений скорости.

`num_unlocked(Unlocks.Senses)` вернет `1`, если датчики разблокированы, в противном случае — `0`.

Также можно использовать `num_unlocked()` для предметов и объектов-сущностей. Функция вернет `1`, если предмет или объект-сущность разблокирован, в противном случае — `0`.

Обрати внимание: `num_unlocked(Unlocks.Carrots)` вернет количество раз, когда технология была разблокирована/улучшена.
`num_unlocked(Items.Carrot)` вернет только `0` или `1`. (Это распространяется на все растения.)
---

[If](docs/scripting/if.md)      [Операторы](docs/scripting/operators.md)      [Переменные](docs/scripting/variables.md)      [Кортежи](docs/scripting/tuples.md)      [Словари](docs/scripting/dicts.md)      [Подземные датчики](docs/unlocks/underground_senses.md)

[get_pos_x()](functions/get_pos_x)      [get_pos_y()](functions/get_pos_y)      [get_entity_type()](functions/get_entity_type)      [get_ground_type()](functions/get_ground_type)      [num_items()](functions/num_items)      [num_unlocked()](functions/num_unlocked)
