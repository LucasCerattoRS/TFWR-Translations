[<- Expansión 1](docs/unlocks/expand_1.md)
---
# Expansión 2
¡Tu granja se ha expandido de nuevo! Ahora las casillas ya no están en una bonita fila, así que necesitas encontrar una manera de recorrer una cuadrícula cuadrada.

Con el bucle `while` esto no es posible hasta que desbloquees los sentidos y los operadores.
Es hora de introducir el bucle `for`.

Puedes leer todo sobre el bucle `for` en la página [Bucle For](docs/scripting/for.md), pero por ahora solo lo necesitarás para repetir código un número fijo de veces.

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
for i in range(5):
	do_a_flip()
}}

`range(n)` crea una secuencia de `n` números desde `0` hasta `n - 1`. El bucle `for` ejecuta su cuerpo una vez por cada elemento de la secuencia. En este ejemplo, se llamará `5` veces a `do_a_flip()`.

La función `get_world_size()` también está disponible ahora. Devuelve la longitud del lado de tu granja. De esta manera, puedes escribir código que no se romperá con la próxima mejora de expansión.

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
    "items": [],
    "world_size": {"x": 3, "y": 3},
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
do_a_flip()
#CODE
for i in range(get_world_size()):
	harvest()
	move(North)
}}

Este ejemplo cosecha una columna de la granja para cualquier tamaño de granja.

Si no sabes cómo mover el dron por la granja, consulta la siguiente pista.
<spoiler=mostrar pista>Hay, por supuesto, varias formas de moverse por la granja.
Lo que buscamos es una forma de recorrerla de manera sistemática que no se rompa cuando la granja vuelva a crecer.
Una forma sistemática de llegar a todos los lugares de la granja sería repetir siempre estos dos pasos:

1. Muévete hacia el `North` hasta que el dron reaparezca en el lado opuesto.
2. Muévete hacia el `East`.

`for i in range(get_world_size()):` puede ser útil para convertir esta idea en código.
</spoiler>
<spoiler=mostrar posible solución>
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
    "items": [],
    "world_size": {"x": 3, "y": 3},
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
do_a_flip()
#CODE
for i in range(get_world_size()):
	for j in range(get_world_size()):
		#hacer un giro en cada casilla
		do_a_flip()
		move(North)
	move(East)
}}
</spoiler>

---

[Bucle for](docs/scripting/for.md)      [Bucle while](docs/scripting/while.md)      [Variables](docs/scripting/variables.md)

[move()](functions/move)      [get_world_size()](functions/get_world_size)
