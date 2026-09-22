[<- Planter](docs/unlocks/plant.md) <right>[Arrosage ->](docs/unlocks/watering.md)
<right>[Arbres ->](docs/unlocks/trees.md)
---
# Carottes
Avant de pouvoir planter des carottes avec `plant(Entities.Carrot)`, tu dois labourer le sol. Cela changera le sol en `Grounds.Soil`. Pour labourer le sol, appelle simplement `till()`. Appeler `till()` à nouveau le retransformera en `Grounds.Grassland`.

Planter des carottes coûte du bois et du foin. Ces objets seront automatiquement retirés lors de l'appel de `plant(Entities.Carrot)`.
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

Tu peux voir le coût de n'importe quelle plante sur sa [propre page](objects/carrot).
---

[Statistiques](docs/stats.md)      [Planter](docs/unlocks/plant.md)      [Arrosage](docs/unlocks/watering.md)      [If](docs/scripting/if.md)      [Sens](docs/unlocks/senses.md)      [Polyculture](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)
