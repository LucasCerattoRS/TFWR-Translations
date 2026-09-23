[<- Variables](docs/scripting/variables.md) <right>[Import ->](docs/scripting/import.md)
---
# Funciones
Usa la palabra clave `def` para definir una nueva función:
`def f(arg1, arg2 = False):
	#código de la función`

Puedes usar el operador de llamada `()` para llamar a la función:
`f(42)`

Consulta también [Ámbitos](docs/scripting/scopes.md) para aprender sobre variables locales y globales en funciones.

## Introducción
Ya has visto funciones integradas como `harvest()`.
También puedes definir tus propias funciones, lo que te permite estructurar el código de forma modular. Una función da un nombre a un bloque de código para que puedas llamarlo donde lo necesites.

## Definiciones de Funciones
Por ejemplo, podrías definir una función que mueva el dron varias veces.

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def move_n_dir(n, dir):
	for i in range(n):
		move(dir)
}}

La palabra clave `def` indica que esto es una definición de función. 
`move_n_dir` es el nombre al que se vincula la función. Puede ser cualquier nombre de variable válido y se usará para llamar a la función.
`n` y `dir` son parámetros. Son variables que contienen los valores que se pasan a la función; estos valores también se llaman argumentos. Puedes añadir tantos parámetros como quieras a la definición de una función.
Después de los `:` viene el bloque de código que se ejecutará cuando se llame a la función.

El siguiente código mueve el dron `2` casillas hacia el `North` y `2` casillas hacia el `East`.

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
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def move_n_dir(n, dir):
	for i in range(n):
		move(dir)

move_n_dir(2, North)
move_n_dir(2, East)
}}

Cuando veas `def function():`, deberías pensar en ello como una asignación de variable como esta:
`function = create_new_function_object()`
Como con todas las asignaciones, ¡no puedes usar la variable antes de que se le haya asignado un valor!
La instrucción `def` debe ejecutarse antes de cualquier llamada a la función.
Este código lanzará un error:

{{codeexample 
{
    "show_image": false,
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 0,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
func()
def func():
	pass
}}

## Valores de Retorno
Usa la palabra clave `return` para hacer que una función devuelva un valor. 
Por ejemplo, la siguiente función define la operación «o exclusivo». El «o exclusivo» devuelve `True` si un valor es `True` y el otro es `False`:

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
#CODE
def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()
}}

Las [Tuplas](docs/scripting/tuples.md) permiten devolver múltiples valores.

## Argumentos por Defecto
También puedes asignar valores predeterminados que se usarán cuando se omitan los argumentos correspondientes.

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
#CODE
def f(a = False):
	if a:
		do_a_flip()

f()

f(True)
}}

Un argumento que tiene un valor por defecto no puede ser seguido por un argumento que no tiene un valor por defecto.

## Uso Avanzado de Funciones
Las funciones son valores como cualquier otro, y la instrucción `def` actúa como una instrucción de asignación, asignando la función al nombre que le des.
Esto permite hacer cosas como esta:

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
#CODE
def f():
	def d():
		do_a_flip()
	return d

f()()
}}

Aquí, `f()` llama a la función `f`, que define y devuelve una nueva función, `d`. El segundo `()` ejecuta la función devuelta y realiza una voltereta.
(Hacer este tipo de cosas no suele ser buena idea porque cuesta ver lo que está ocurriendo).

Las funciones que toman otras funciones como argumentos te permiten ser muy creativo:

{{codeexample 
{
    "camera_position": {"x": -2, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "fertilizer", "n": 4}],
    "world_size": {"x": 5, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def f(g, arg):
	for _ in range(4):
		g(arg)

f(move, East)
plant(Entities.Tree)
f(use_item, Items.Fertilizer)
}}

---

[Variables](docs/scripting/variables.md)      [Ámbitos de nombres](docs/scripting/scopes.md)      [Tuplas](docs/scripting/tuples.md)      [Import](docs/scripting/import.md)
