[<- Полив](docs/unlocks/watering.md)
---
# Подсолнухи
[Подсолнухи](objects/sunflower) накапливают энергию солнца, а ты можешь ее собирать.

Эти растения нужно сажать так же, как морковь и тыкву.

При сборе урожая с выросшего подсолнуха ты получаешь энергию.
Если на ферме не менее 10 подсолнухов и ты соберешь тот, у которого больше всего лепестков, то получишь в `8` раз больше энергии!
Если ты соберешь подсолнух, когда на ферме есть другой с бо́льшим количеством лепестков, то следующий сбор тоже принесет только обычное количество энергии (без бонуса x8).

`measure()` возвращает количество лепестков у подсолнуха под дроном.
У подсолнухов может быть не менее `7` и не более `15` лепестков.
Количество лепестков можно измерять еще до того, как подсолнух вырастет до конца; такие подсолнухи уже учитываются в лимите из 10 растений.

У нескольких подсолнухов может быть одинаковое количество лепестков, а значит, может быть несколько цветков с наибольшим количеством лепестков. В этом случае неважно, какой из них ты соберешь.

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "inventory_scale": 5,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "carrot", "n": 10}],
    "world_size": {"x": 5, "y": 2},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 4,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(North)
for _ in range(5):
    till()
    plant(Entities.Sunflower)
    move(East)
move(North)
do_a_flip()
do_a_flip()
do_a_flip()
do_a_flip()
do_a_flip()
#CODE
for _ in range(5):
    till()
    plant(Entities.Sunflower)
    print(measure())
    move(East)
for _ in range(5):
    while not can_harvest():
        pass
    harvest()
    move(East)
}}

Пока у тебя есть энергия, дрон будет использовать ее, чтобы работать в два раза быстрее.
Он расходует 1 энергии каждые 30 действий, таких как перемещения, сбор урожая, посадка и др.
Выполнение других инструкций также может расходовать энергию, но гораздо меньше, чем действия дрона.

В целом, за счет энергии можно ускорить все, что ускоряется с помощью повышения скорости.
Все, что ускоряется за счет энергии, также расходует энергию пропорционально времени, которое требуется для выполнения кода, без учета повышения скорости.

---

[Статистика](docs/stats.md)      [Списки](docs/scripting/lists.md)      [Словари](docs/scripting/dicts.md)      [Переменные](docs/scripting/variables.md)      [Цикл for](docs/scripting/for.md)      [If](docs/scripting/if.md)      [Операторы](docs/scripting/operators.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [measure()](functions/measure)
