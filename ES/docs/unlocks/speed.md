[<- Bucle while](docs/scripting/while.md) <right>[Expansión 1 ->](docs/unlocks/expand_1.md)
<right>[Plantar ->](docs/unlocks/plant.md)
---
# Mejora de Velocidad
La velocidad de ejecución se ha duplicado. El problema es que ahora el dron cosecha más rápido de lo que crece la hierba, por lo que no obtiene ningún rendimiento. Para solucionarlo, se han desbloqueado las ramificaciones [if](docs/scripting/if.md) y la función [can_harvest()](functions/can_harvest).

## Comprobando Antes de Cosechar
Una instrucción `if` ejecuta su bloque de código una vez si la condición indicada es `True`.

La nueva función `can_harvest()` proporciona una condición útil. `can_harvest()` devuelve `True` si se puede cosechar la planta que hay debajo del dron y `False` en caso contrario.

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
do_a_flip()
#CODE
if can_harvest():
	do_a_flip()
}}

Puedes imaginar un valor de retorno de este tipo como si, al evaluar el `if`, la expresión de llamada `can_harvest()` se sustituyera por el valor devuelto `True`.

Lo que sucede cuando el código anterior se ejecuta:
- Se ejecuta la instrucción `if`.
- Se llama a `can_harvest()`.
- `can_harvest()` devuelve `True` porque la hierba ha crecido por completo.
- La instrucción pasa a ser `if True:`.
- La ramificación se ejecuta porque el valor es `True`.

Si la hierba no hubiera crecido por completo, no haría una voltereta.

Ahora podemos usar `if` para evitar que el dron coseche demasiado pronto.

---

[If](docs/scripting/if.md)      [Bucle while](docs/scripting/while.md)

[harvest()](functions/harvest)      [can_harvest()](functions/can_harvest)
