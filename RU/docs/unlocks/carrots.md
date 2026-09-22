[<- Посадка](docs/unlocks/plant.md) <right>[Полив ->](docs/unlocks/watering.md)
<right>[Деревья ->](docs/unlocks/trees.md)
---
# Морковь
Чтобы сажать морковь с помощью `plant(Entities.Carrot)`, сначала нужно вскопать грядку. Это изменит тип земли на `Grounds.Soil`. Чтобы вскопать грядку, просто вызови `till()`. Повторный вызов `till()` вернет землю в состояние `Grounds.Grassland`.

Чтобы сажать морковь, нужны древесина и сено. Эти предметы будут автоматически списаны при вызове `plant(Entities.Carrot)`.
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
    "items": [{"item": "hay", "n": 1}, {"item": "wood", "n": 1}],
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
till()
plant(Entities.Carrot)
for _ in range(8):
    do_a_flip()
harvest()
till()
}}

Ты можешь увидеть стоимость любого растения на его [собственной странице](objects/carrot).

---

[Статистика](docs/stats.md)      [Посадка](docs/unlocks/plant.md)      [Полив](docs/unlocks/watering.md)      [If](docs/scripting/if.md)      [Датчики](docs/unlocks/senses.md)      [Поликультура](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)
