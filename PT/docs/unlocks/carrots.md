[<- Plantar](docs/unlocks/plant.md) <right>[Irrigação ->](docs/unlocks/watering.md)

<right>[Árvores ->](docs/unlocks/trees.md)

---

# Cenouras

Antes de poder plantar cenouras com `plant(Entities.Carrot)`, você precisa arar o solo. Isso mudará o chão para `Grounds.Soil`. Para arar o solo, basta chamar `till()`. Chamar `till()` novamente o mudará de volta para `Grounds.Grassland`.

Plantar cenouras custa madeira e feno. Esses itens serão removidos automaticamente ao chamar `plant(Entities.Carrot)`.

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

Você pode ver o custo de qualquer planta em sua [própria página](objects/carrot).

---

[Estatísticas](docs/stats.md)      [Plantar](docs/unlocks/plant.md)      [Irrigação](docs/unlocks/watering.md)      [If](docs/scripting/if.md)      [Sentidos](docs/unlocks/senses.md)      [Policultura](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)
