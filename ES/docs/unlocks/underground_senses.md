[<- Minería](docs/unlocks/mining.md)
---
# Sentidos subterráneos

Vamos a añadir algunos sensores para que tu dron pueda orientarse bajo tierra.

Ahora puedes usar `get_pos_z()` para obtener la altura del dron (empieza en 0 y se vuelve negativa a medida que el dron desciende).

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "exclude_unlocks": ["watering", "fertilizer"],
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#CODE
move(North)
move(North)
move(East)
dig()
dig()
dig()
print(get_pos_z())
}}

`get_ground_type()` devuelve el tipo de terreno que hay debajo del dron. Puedes pasarle un argumento de dirección (por ejemplo, `get_ground_type(North)`) para obtener el tipo de terreno de una casilla vecina.

Así comprobarías si el bloque que hay debajo del dron es tierra:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#CODE
dig()
if get_ground_type() == Grounds.Dirt:
    do_a_flip()
}}


`get_hardness()` devuelve la dureza de la casilla de terreno que hay debajo del dron. Puedes pasarle un argumento de dirección, como `get_hardness(North)`. Cuanto mayor sea la dureza de una casilla, más se tarda en excavarla.

`get_stability()` devuelve la estabilidad de la casilla de terreno que hay debajo del dron. Puedes pasarle un argumento de dirección, como `get_stability(North)`. Una estabilidad de 1 significa que el bloque puede soportar una diferencia de altura de 1 antes de derrumbarse.

Ten en cuenta que los cuatro bloques situados directamente junto al dron se eliminan independientemente de su estabilidad cuando el dron excava hacia abajo, a menos que tengan una función especial. La arcilla, el hierro y el cuarzo, por ejemplo, no se eliminan por esta regla. Sin embargo, siguen siendo susceptibles a derrumbes por falta de estabilidad.
---

[Minería](docs/unlocks/mining.md)      [Sentidos](docs/unlocks/senses.md)

[get_pos_z()](functions/get_pos_z)      [get_ground_type()](functions/get_ground_type)      [get_hardness()](functions/get_hardness)      [get_stability()](functions/get_stability)
