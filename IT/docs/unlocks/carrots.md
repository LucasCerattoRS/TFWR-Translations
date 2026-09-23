[<- Pianta](docs/unlocks/plant.md) <right>[Annaffiare ->](docs/unlocks/watering.md)
<right>[Alberi ->](docs/unlocks/trees.md)
---
# Carote
Prima di poter piantare carote con `plant(Entities.Carrot)`, devi arare il terreno. Questo cambierà il terreno in `Grounds.Soil`. Per arare il terreno, chiama semplicemente `till()`. Chiamare di nuovo `till()` lo riporterà a `Grounds.Grassland`.

Piantare carote costa legno e fieno. Questi oggetti verranno rimossi automaticamente quando chiami `plant(Entities.Carrot)`.
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

Puoi vedere il costo di ogni pianta nella sua [pagina dedicata](objects/carrot).

---

[Statistiche](docs/stats.md)      [Pianta](docs/unlocks/plant.md)      [Annaffiare](docs/unlocks/watering.md)      [If](docs/scripting/if.md)      [Sensori](docs/unlocks/senses.md)      [Policoltura](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)
