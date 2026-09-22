[<- Carbón](docs/unlocks/coal.md)
---
# Saltar

Tu dron ha desbloqueado el comando `jump()`.

Este comando te permite seleccionar ciertos desbloqueos y saltar hasta ellos. Resulta especialmente útil para depurar o saltar hasta una veta de mineral que acabas de pasar por alto. Para usarlo, debes pasarle un desbloqueo como argumento, por ejemplo, `Unlocks.Iron`.

`jump()` solo funciona con desbloqueos que aparecen bajo tierra, como `jump(Unlocks.Rice)` o `jump(Unlocks.Iron)`.

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
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 3,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms"],
    "starting_chunk": 0
}
#CODE
dig()
dig()
dig()
jump(Unlocks.Iron)
do_a_flip()
}}

No está garantizado que el salto te lleve directamente hasta el desbloqueo objetivo, así que puede que aún tengas que buscar un poco por la zona, pero sí está garantizado que el objetivo se encuentre cerca.

`jump()` solo se puede usar una vez por ejecución del programa.

---

[jump()](functions/jump)
