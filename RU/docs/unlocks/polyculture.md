[<- Тыквы](docs/unlocks/pumpkins.md)
---
# Поликультура
Возможно, ты уже знаешь, что растения иногда приносят больше урожая, если их сажают вместе с другими видами.
Трава, кусты, деревья и морковь приносят больше урожая, когда у них есть правильный компаньон. Желаемый компаньон у каждого растения свой, и его предпочтения невозможно предсказать. К счастью, предпочтения растения под дроном можно измерить с помощью функции `get_companion()`. Она возвращает кортеж, где первый элемент — тип желаемого растения-компаньона, а второй — позиция, где его нужно посадить. Для получения бонуса к урожаю компаньону не обязательно полностью вырасти.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Bush)
plant_type, (x, y) = get_companion()
print(plant_type, (x, y))
move(East)
move(South)
plant(plant_type)
move(West)
move(North)
do_a_flip()
harvest()
}}

Растение может хотеть в качестве компаньона `Entities.Grass`, `Entities.Bush`, `Entities.Tree` либо `Entities.Carrot`. Значение выбирается случайным образом, но компаньон всегда отличается от растения по типу. Позиция также может быть любой в пределах трех ходов от растения, не включая позицию самого растения.

Если под дроном нет растения, у которого есть желаемый компаньон, `get_companion()` вернет `None`.

До первой разблокировки поликультуры множитель урожая равен `5`. С каждым улучшением он удваивается.
---

[Статистика](docs/stats.md)      [Кортежи](docs/scripting/tuples.md)      [Словари](docs/scripting/dicts.md)      [Датчики](docs/unlocks/senses.md)      [Посадка](docs/unlocks/plant.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [get_companion()](functions/get_companion)
