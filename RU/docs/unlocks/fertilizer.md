[<- Полив](docs/unlocks/watering.md) <right>[Лабиринты ->](docs/unlocks/mazes.md)
---
# Удобрение
В какой-то момент ожидание созревания растений становится нецелесообразным. 
Как и в случае с водой, ты будешь автоматически получать 1 удобрение каждые 10 секунд, и это количество будет удваиваться с каждым улучшением.

Удобрение позволяет растениям созреть мгновенно. `use_item(Items.Fertilizer)` уменьшает оставшееся время роста растения под дроном на 2 секунды.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "fertilizer", "n": 10}],
    "world_size": {"x": 1, "y": 1},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Tree)
use_item(Items.Fertilizer)
use_item(Items.Fertilizer)
use_item(Items.Fertilizer)
harvest()
}}

Однако у него есть побочные эффекты.
Растения, выращенные с помощью удобрения, будут заражены.

Если растение заражено, половина собранного урожая превращается в `Items.Weird_Substance`.
Странное вещество можно применять к растениям, что приводит к изменению статуса заражения у этого растения и всех соседних.

Если вызвать `use_item(Items.Weird_Substance)` на зараженном растении, вещество его вылечит, а если применить к здоровому растению — оно будет заражено.

Если ты применишь вещество к зараженному растению со здоровыми соседями, оно вылечит растение, но заразит соседей, и наоборот.

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
    "items": [{"item": "weird_substance", "n": 10}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
for _ in range(3):
    for _ in range(3):
        plant(Entities.Tree)
        move(East)
    move(North)

move(North)
move(East)

for _ in range(60):
    do_a_flip()
#CODE
for _ in range(6):
    use_item(Items.Weird_Substance)
    move(East)
}}

---

[Статистика](docs/stats.md)      [Полив](docs/unlocks/watering.md)      [Лабиринты](docs/unlocks/mazes.md)

[use_item()](functions/use_item)
