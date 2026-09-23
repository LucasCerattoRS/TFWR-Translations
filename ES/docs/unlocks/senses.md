[<- Operadores](docs/scripting/operators.md)
---
# Sentidos
¡El dron puede ver ahora! 

Las funciones `get_pos_x()` y `get_pos_y()` devuelven las coordenadas x e y actuales del dron. En la posición inicial, ambas son `0`. La coordenada x aumenta en `1` por cada casilla hacia el `East`, y la coordenada y aumenta en `1` por cada casilla hacia el `North`.
{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 2},
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
move(East)
#CODE
print("x =", get_pos_x(), "y =", get_pos_y())
if get_pos_x() == 1 and get_pos_y() == 0:
    do_a_flip()
}}

`num_items(item)` devuelve cuántos de un ítem tienes.
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 10}],
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
print(num_items(Items.Hay))
}}

`get_entity_type()` y `get_ground_type()` devuelven el tipo de entidad o terreno que hay debajo del dron.
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
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
plant(Entities.Bush)
#CODE
print(get_entity_type())
if get_entity_type() == Entities.Bush:
	do_a_flip()

print(get_ground_type())
if get_ground_type() != Grounds.Soil:
	do_a_flip()
}}

¡La palabra clave `None` también está desbloqueada ahora! `None` es un valor que representa que no hay valor.
Por ejemplo, una función que no tiene una instrucción `return` en realidad devolverá `None`.

`get_entity_type()` devuelve `None` si no hay ninguna entidad debajo del dron.


Si quieres saber cuántos de un desbloqueo en particular tienes, usa la función `num_unlocked(unlock)`.

Por ejemplo, `num_unlocked(Unlocks.Speed)` devolverá el número de mejoras de velocidad que tienes.

`num_unlocked(Unlocks.Senses)` devolverá `1` si los sentidos están desbloqueados y `0` si no lo están.

También puedes usar `num_unlocked()` con ítems o entidades. Devuelve `1` si el ítem o la entidad está desbloqueado y `0` en caso contrario.

Ten cuidado: `num_unlocked(Unlocks.Carrots)` devuelve el número de veces que se ha desbloqueado o mejorado el desbloqueo.
`num_unlocked(Items.Carrot)` solo devuelve `0` o `1`. Lo mismo se aplica a las demás plantas.

---

[If](docs/scripting/if.md)      [Operadores](docs/scripting/operators.md)      [Variables](docs/scripting/variables.md)      [Tuplas](docs/scripting/tuples.md)      [Diccionarios](docs/scripting/dicts.md)      [Sentidos subterráneos](docs/unlocks/underground_senses.md)

[get_pos_x()](functions/get_pos_x)      [get_pos_y()](functions/get_pos_y)      [get_entity_type()](functions/get_entity_type)      [get_ground_type()](functions/get_ground_type)      [num_items()](functions/num_items)      [num_unlocked()](functions/num_unlocked)
