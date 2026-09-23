[<- Calabazas](docs/unlocks/pumpkins.md)
---
# Policultivo
Puede que ya hayas notado que a veces las plantas rinden más cuando se plantan juntas.
La hierba, los arbustos, los árboles y las zanahorias producen más cuando tienen la planta compañera adecuada. La preferencia es distinta para cada planta y no se puede predecir. Por suerte, puedes medir la preferencia de la planta que hay debajo del dron con `get_companion()`. Devuelve una tupla cuyo primer elemento es el tipo de planta que quiere como compañera y el segundo es la posición donde la quiere. La planta compañera no tiene que haber crecido por completo para obtener la bonificación de rendimiento.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 20,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Bush)
plant_type, (x, y) = get_companion()
print(plant_type, (x, y))
move(East)
move(South)
plant(plant_type)
move(West)
move(North)
do_a_flip()
harvest()
}}

La preferencia de una planta puede ser `Entities.Grass`, `Entities.Bush`, `Entities.Tree` o `Entities.Carrot`. Cada planta elige al azar, pero siempre escogerá un tipo distinto del suyo. La posición puede estar en cualquier lugar a un máximo de 3 movimientos de la planta, salvo en su propia posición.

Si debajo del dron no hay ninguna planta con una preferencia de compañera, `get_companion()` devuelve `None`.

Antes de desbloquear el policultivo por primera vez, el multiplicador de rendimiento es `5`. Se duplica con cada mejora.

---

[Estadísticas](docs/stats.md)      [Tuplas](docs/scripting/tuples.md)      [Diccionarios](docs/scripting/dicts.md)      [Sentidos](docs/unlocks/senses.md)      [Plantar](docs/unlocks/plant.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [get_companion()](functions/get_companion)
