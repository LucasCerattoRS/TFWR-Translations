[<- Riego](docs/unlocks/watering.md)
---
# Girasoles
Los [girasoles](objects/sunflower) recogen la energía del sol. Puedes cosechar esa energía. 

Plantarlos funciona exactamente igual que plantar zanahorias o calabazas.

Cosechar un girasol crecido produce energía.
Si hay al menos 10 girasoles en la granja y cosechas uno de los que tienen más pétalos, ¡obtendrás `8` veces más energía!
Si cosechas un girasol mientras hay otro girasol con más pétalos, el siguiente girasol que coseches también te dará solo la cantidad normal de energía (no el bonus de 8x).

`measure()` devuelve el número de pétalos del girasol debajo del dron.
Los girasoles tienen al menos `7` y como máximo `15` pétalos.
Los girasoles se pueden medir incluso antes de que hayan crecido por completo y cuentan para el límite de 10 girasoles.

Varios girasoles pueden tener el mismo número de pétalos, así que puede haber varios con la cantidad máxima. En ese caso, no importa cuál coseches.

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

Mientras tengas energía, el dron la usará para funcionar al doble de velocidad.
Consume 1 de energía cada 30 acciones, como movimientos, cosechas o siembras.
Ejecutar otras instrucciones de código también puede consumir energía, pero mucha menos que las acciones del dron.

En general, todo lo que se acelera con las mejoras de velocidad también se acelera con la energía.
Cualquier cosa acelerada por la energía también usa energía proporcional al tiempo que tarda en ejecutarse, ignorando las mejoras de velocidad.
---

[Estadísticas](docs/stats.md)      [Listas](docs/scripting/lists.md)      [Diccionarios](docs/scripting/dicts.md)      [Variables](docs/scripting/variables.md)      [Bucle for](docs/scripting/for.md)      [If](docs/scripting/if.md)      [Operadores](docs/scripting/operators.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [measure()](functions/measure)
