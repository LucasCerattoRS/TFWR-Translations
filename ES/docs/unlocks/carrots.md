[<- Plantar](docs/unlocks/plant.md) <right>[Riego ->](docs/unlocks/watering.md)
<right>[Árboles ->](docs/unlocks/trees.md)
---
# Zanahorias
Antes de poder plantar zanahorias con `plant(Entities.Carrot)`, tienes que arar la tierra. Esto cambiará el terreno a `Grounds.Soil`. Para arar la tierra, simplemente llama a `till()`. Llamar a `till()` de nuevo lo cambiará de vuelta a `Grounds.Grassland`.

Plantar zanahorias cuesta madera y heno. Estos ítems se eliminarán automáticamente al llamar a `plant(Entities.Carrot)`.
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

Puedes ver el coste de cualquier planta en su [propia página](objects/carrot).

---

[Estadísticas](docs/stats.md)      [Plantar](docs/unlocks/plant.md)      [Riego](docs/unlocks/watering.md)      [If](docs/scripting/if.md)      [Sentidos](docs/unlocks/senses.md)      [Policultivo](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)
