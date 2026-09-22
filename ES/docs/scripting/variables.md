[<- Operadores](docs/scripting/operators.md) <right>[Listas ->](docs/scripting/lists.md)
<right>[Funciones ->](docs/scripting/functions.md)
---
# Variables
Las variables se pueden considerar como contenedores con nombre que pueden almacenar un valor.
El operador `=` se usa para declarar una variable y almacenar un valor en ella.

`nombre_variable = valor`

El lado izquierdo del operador es el nombre de la variable. Puedes darle cualquier nombre válido que quieras.
El lado derecho es una expresión cuyo valor resultante se almacenará en la variable.

Declara una variable llamada `a` y almacena el valor `5` en ella:
`a = 5`
Declara una variable llamada `b` y almacena el valor de retorno de `can_harvest()` en ella:
`b = can_harvest()`

No confundas el operador `=` con el operador `==`. 
El operador `==` comprueba si dos valores son iguales y devuelve `True` o `False`.
El operador `=` asigna el valor de la derecha al nombre de la izquierda.

Después de que se ha asignado una variable, puedes usarla en el código para recuperar el valor que contiene

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
a = 5
for i in range(a):
	do_a_flip()
}}

El bucle anterior se ejecuta 5 veces porque `a` está establecido en `5`.
La `i` del bucle `for` también es una variable. Durante cada iteración, recibe automáticamente el valor actual de la secuencia. No tiene que llamarse `i`; puedes darle cualquier nombre de variable válido.

Las variables también te permiten hacer lo mismo con un bucle while:

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
a = 5
i = 0
while i < a:
	do_a_flip()
	i = i + 1
}}

Esto hace lo mismo que el bucle `for` anterior, pero tenemos que incrementar `i` manualmente.
Para incrementar `i`, le asignamos su valor actual más `1`. Es muy habitual cambiar una variable a partir de su valor anterior.
Se puede abreviar usando estos operadores: `+=, -=, *=, /=, %=`

`i = i + 1` es lo mismo que `i += 1`
`a = a / 3` es lo mismo que `a /= 3`
---

[Operadores](docs/scripting/operators.md)      [Bucle while](docs/scripting/while.md)      [Bucle for](docs/scripting/for.md)      [Funciones](docs/scripting/functions.md)      [Ámbitos de nombres](docs/scripting/scopes.md)
