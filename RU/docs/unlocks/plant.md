[<- Повышение скорости](docs/unlocks/speed.md) <right>[Морковь ->](docs/unlocks/carrots.md)
<right>[Отладка ->](docs/scripting/debug.md)
<right>[Операторы ->](docs/scripting/operators.md)
---
# Посадка
Трава хороша тем, что растет автоматически. Все остальные растения нужно сажать с помощью функции `plant()`. Пока что ты можешь посадить только куст.
Ты можешь передать тип растения, которое хочешь посадить, в функцию следующим образом:

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

Под дроном будет посажен куст.

Чтобы сбросить все участки фермы до луга и вернуть дрон на исходную позицию, вызови `clear()`.

Похоже, если выращивать на ферме одновременно более одного типа растений, иногда урожай получается больше. Чтобы узнать об этом подробнее, исследуй поликультуру.

---

[Статистика](docs/stats.md)      [If](docs/scripting/if.md)      [Датчики](docs/unlocks/senses.md)      [Поликультура](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)
