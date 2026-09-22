[<- Riego](docs/unlocks/watering.md) <right>[Laberintos ->](docs/unlocks/mazes.md)
---
# Fertilizante
En algún momento, esperar a que las plantas crezcan deja de ser lo bastante eficiente.
Al igual que con el agua, recibirás automáticamente 1 fertilizante cada 10 segundos. La cantidad se duplica con cada mejora.

El fertilizante puede hacer que las plantas crezcan instantáneamente. `use_item(Items.Fertilizer)` reduce el tiempo de crecimiento restante de la planta bajo el dron en 2 segundos.

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

Esto tiene algunos efectos secundarios.
Las plantas cultivadas con fertilizante se infectarán.

Cuando una planta está infectada, la mitad de su rendimiento se convierte en `Items.Weird_Substance` cuando se cosecha.
La Sustancia Extraña también se puede usar en las plantas, lo que tiene el efecto de cambiar el estado de infección de la planta y de todas las plantas adyacentes.

Si llamas a `use_item(Items.Weird_Substance)` sobre una planta infectada, la curará; si lo usas sobre una planta sana, la infectará.

Si lo usas sobre una planta infectada que tiene vecinas sanas, curará la planta pero infectará a las vecinas, y viceversa.

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

[Estadísticas](docs/stats.md)      [Riego](docs/unlocks/watering.md)      [Laberintos](docs/unlocks/mazes.md)

[use_item()](functions/use_item)
