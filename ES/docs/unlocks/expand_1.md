[<- Mejora de velocidad](docs/unlocks/speed.md) <right>[Expansión 2 ->](docs/unlocks/expand_2.md)
<right>[Minería ->](docs/unlocks/mining.md)
---
# Expansión 1
¡Tu granja ha crecido! Este espacio no sirve de mucho si no puedes mover el dron, así que hay una nueva función, `move()`, que mueve el dron. `move()` requiere que especifiques la dirección en la que quieres moverlo. Para ello hay cuatro constantes nuevas: `North, East, South, West`

Por ejemplo, `move(North)` moverá el dron una casilla hacia el norte.

Si te mueves más allá del borde de la granja, el dron reaparecerá en el lado opuesto.

{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 1, "y": 3},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
while True:
	move(North)
}}

---

[Bucle while](docs/scripting/while.md)      [Operadores](docs/scripting/operators.md)      [Expansión 2](docs/unlocks/expand_2.md)

[move()](functions/move)
