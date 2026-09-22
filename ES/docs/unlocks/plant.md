[<- Mejora de velocidad](docs/unlocks/speed.md) <right>[Zanahorias ->](docs/unlocks/carrots.md)
<right>[Depuración ->](docs/scripting/debug.md)
<right>[Operadores ->](docs/scripting/operators.md)
---
# Plantar
La hierba es agradable porque crece automáticamente. Todas las demás plantas deben ser plantadas con la función `plant()`. La única planta que puedes plantar ahora mismo es un arbusto.
Puedes pasar el tipo de planta que quieres plantar a la función de esta manera:

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
#CODE
plant(Entities.Bush)
}}

Esto plantará un arbusto debajo del dron.

Llama a `clear()` para restablecer la granja a todo hierba y restablecer la posición del dron.

Parece que, si cultivas más de un tipo de planta en la granja al mismo tiempo, a veces puedes obtener un mayor rendimiento. Tendrás que investigar el policultivo para saber más.

---

[Estadísticas](docs/stats.md)      [If](docs/scripting/if.md)      [Sentidos](docs/unlocks/senses.md)      [Policultivo](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)
