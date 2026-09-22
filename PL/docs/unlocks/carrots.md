[<- Sadzenie](docs/unlocks/plant.md) <right>[Podlewanie ->](docs/unlocks/watering.md)
<right>[Drzewa ->](docs/unlocks/trees.md)
---
# Marchewki
Zanim będziesz mógł sadzić marchewki za pomocą `plant(Entities.Carrot)`, musisz zaorać ziemię. Zmieni to podłoże na `Grounds.Soil`. Aby zaorać ziemię, po prostu wywołaj `till()`. Ponowne wywołanie `till()` zmieni je z powrotem na `Grounds.Grassland`.

Sadzenie marchewek kosztuje drewno i siano. Te przedmioty zostaną automatycznie usunięte podczas wywoływania `plant(Entities.Carrot)`.
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

Możesz zobaczyć koszt każdej rośliny na jej [własnej stronie](objects/carrot).
---

[Statystyki](docs/stats.md)      [Sadzenie](docs/unlocks/plant.md)      [Podlewanie](docs/unlocks/watering.md)      [If](docs/scripting/if.md)      [Zmysły](docs/unlocks/senses.md)      [Uprawa współrzędna](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)
