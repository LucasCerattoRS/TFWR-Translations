[<- Expansión 2](docs/unlocks/expand_2.md)
---
# Bucle For
El bucle `for` funciona como en Python. En algunos lenguajes se llama bucle foreach y no debe confundirse con el bucle for de estilo C, que funciona de otra manera.

`for i in sequence:
	#hacer algo con i`

Similar al bucle `while`, el bucle `for` también llama repetidamente a un bloque de código. En lugar de iterar basándose en una condición, ejecuta el cuerpo del bucle una vez por cada elemento en una secuencia.

## Sintaxis
Un bucle for se ve así:

`for variable_name in sequence:
	#bloque de código`

`variable_name` puede ser cualquier nombre que elijas. Es una variable que almacena el elemento actual de la secuencia. `sequence` debe ser un valor iterable, como un rango de números. El bloque de código se ejecuta una vez por cada elemento y la variable del bucle recibe ese elemento.

## Secuencias
[Rangos](functions/range)      <unlock=lists>[Listas](docs/scripting/lists.md)      </unlock><unlock=functions>[Tuplas](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Diccionarios](docs/scripting/dicts.md)      </unlock><unlock=sets>[Conjuntos](docs/scripting/sets.md)</unlock>

## Ejemplo
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
for i in range(5):
    harvest()
}}

Este bucle ejecuta el cuerpo un número fijo de veces. Es esencialmente lo mismo que escribir

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
i = 0
harvest()
i = 1
harvest()
i = 2
harvest()
i = 3
harvest()
i = 4
harvest()
}}


---

[Bucle while](docs/scripting/while.md)      [Break](docs/scripting/break.md)      [Continue](docs/scripting/continue.md)

[range()](functions/range)
