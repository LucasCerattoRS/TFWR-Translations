[<- Laberintos](docs/unlocks/mazes.md)
---
# Megagranja
Este desbloqueo increíblemente poderoso te da acceso a múltiples drones. 
{{codeexample 
{
    "camera_position": {"x": -3, "y": 2.1, "z": 7},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": true,
    "collapsing": false,
    "autoplay": true,
    "items": [],
    "world_size": {"x": 7, "y": 7},
    "execution_speed": 21,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(North)
move(North)
move(North)
move(East)
move(East)
move(East)
change_hat(Hats.Wizard_Hat)
#CODE
def harvest_spiral(radius):
    for i in range(1, radius, 2):
        harvest()
        move(West)
        for j in range(i):
            harvest()
            move(South)
        for j in range(i+1):
            harvest()
            move(East)
        for j in range(i+1):
            harvest()
            move(North)
        for j in range(i+1):
            harvest()
            move(West)

while True:
    spawn_drone(harvest_spiral, 7)
    do_a_flip()
}}

Como antes, todavía comienzas con un solo dron. Los drones adicionales deben ser generados primero y desaparecerán después de que el programa termine.
Cada dron ejecuta su propio programa por separado. Se pueden generar nuevos drones usando la función `spawn_drone(function)`.

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def drone_function():
    move(East)
    do_a_flip()

spawn_drone(drone_function)
do_a_flip()
}}

Esto genera un nuevo dron en la misma posición que el dron que ejecutó el comando `spawn_drone(function)`. El nuevo dron empieza a ejecutar la función especificada. Cuando termina, desaparece automáticamente, salvo que sea el último dron existente.

Los drones no chocan entre sí. 

Usa `max_drones()` para obtener el número máximo de drones que pueden existir simultáneamente.
Usa `num_drones()` para obtener el número de drones que ya están en la granja.


## Ejemplo:
{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def harvest_column():
    for _ in range(get_world_size()):
        harvest()
        move(North)

while True:
    if spawn_drone(harvest_column):
        move(East)
}}

Esto hará que tu primer dron se mueva horizontalmente y genere más drones. Los drones generados se moverán verticalmente y cosecharán todo a su paso.

Si ya se han generado todos los drones disponibles, `spawn_drone()` no hará nada y devolverá `None`.

Aquí hay otro ejemplo que pasa una dirección diferente a cada dron.
{{codeexample 
{
    "camera_position": {"x": -1, "y": 2, "z": 5},
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
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(North)
move(East)
#CODE
for dir in [North, East, South, West]:
    def task():
        move(dir)
        do_a_flip()
    spawn_drone(task)
}}

## Todos los Drones son Iguales
No hay ningún dron «principal» especial. Todos los drones pueden generar otros drones y todos cuentan para el límite. Todos desaparecen cuando terminan. Si el primer dron acaba su programa antes de tiempo, otro pasa a ser aquel cuya ejecución se visualiza con el resaltado de código. Todos los drones pueden activar puntos de interrupción. Cuando esto ocurre, el resaltado cambia a ese dron.

<spoiler=mostrar pista> 
Mira esta función paralela `for_all`, muy útil: recibe cualquier función y la ejecuta en todas las casillas de la granja usando todos los drones disponibles.

{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2.4, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def for_all(f):
	def row():
		for _ in range(get_world_size()-1):
			f()
			move(East)
		f()
	for _ in range(get_world_size()):
		if not spawn_drone(row):
			row()
		move(North)

for_all(harvest)
}}

Un patrón particularmente útil es generar un dron si hay uno disponible y, de lo contrario, hacerlo tú mismo.

`if not spawn_drone(task):
	task()`
</spoiler>

## Esperar a otro Dron
Usa la función `wait_for(drone)` para esperar a que otro dron termine. Recibes el handle del `drone` cuando lo generas.
`wait_for(drone)` devuelve el valor de retorno de la función que el otro dron estaba ejecutando.

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
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
plant(Entities.Tree)
move(West)
#CODE
def get_entity_type_in_direction(dir):
    move(dir)
    return get_entity_type()

drone = spawn_drone(get_entity_type_in_direction, East)
print(wait_for(drone))
}}

Ten en cuenta que generar drones lleva tiempo, así que no es una buena idea generar un nuevo dron para cada pequeña cosa.

Puedes usar `has_finished(drone)` para ver si el dron ya terminó sin tener que esperar.

## Sin Memoria Compartida
Cada dron tiene su propia memoria y no puede leer o escribir directamente las variables globales de otro dron.

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": false,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
x = 0

def increment():
    global x
    x += 1

wait_for(spawn_drone(increment))
print(x)
}}

Esto imprime `0` porque el nuevo dron incrementó su propia copia de la `x` global, lo cual no afecta a la `x` del primer dron.

## Pasar Argumentos

`spawn_drone()` acepta argumentos opcionales adicionales que se pasarán a la función llamada:

Ten en cuenta que la regla de no compartir memoria sigue aplicándose. Esto significa que la función llamada opera con una copia de los argumentos:

{{codeexample 
{
    "camera_position": {"x": -0.5, "y": 1.5, "z": 4},
    "show_image": false,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": false,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def modify(list):
	list.append('verde')
	print(list)

l = ['rojo']
wait_for(spawn_drone(modify, l))
print(l)
}}

## Condiciones de Carrera
Múltiples drones pueden interactuar con la misma casilla de la granja al mismo tiempo. Si dos drones interactúan con la misma casilla durante el mismo tick, ambas interacciones ocurrirán, pero los resultados pueden diferir según el orden de las interacciones.

Por ejemplo, imagina que los drones `0` y `1` están ambos sobre el mismo árbol que está casi completamente crecido.
El dron `0` llama a
`use_item(Items.Fertilizer)`
El dron `1` llama a
`harvest()`

Si estas acciones ocurren al mismo tiempo, el árbol primero será fertilizado y luego cosechado. En ese caso, recibirás madera de él. Sin embargo, si el dron `1` es ligeramente más rápido, el árbol será cosechado antes de ser fertilizado, y no recibirás la madera.
Esto se llama una "condición de carrera". Es un problema común en la programación paralela, donde el resultado depende del orden en que se realizan las operaciones.

Aquí hay otra situación problemática que puede ocurrir cuando múltiples drones ejecutan el mismo código simultáneamente en la misma posición.
`if get_water() < 0.5:
    use_item(Items.Water)`

Si múltiples drones ejecutan esto simultáneamente, todos ejecutarán la primera línea, lo que los pondrá en el bloque `if`. Luego, todos usarán agua, desperdiciando mucha.
Cuando un dron llega a la segunda línea, puede que `get_water()` ya no sea menor que `0.5` porque otro dron ha regado la casilla mientras tanto.

---

[Funciones](docs/scripting/functions.md)      [Ámbitos de nombres](docs/scripting/scopes.md)      [Simulación](docs/unlocks/simulation.md)

[spawn_drone()](functions/spawn_drone)      [num_drones()](functions/num_drones)      [max_drones()](functions/max_drones)      [wait_for()](functions/wait_for)      [has_finished()](functions/has_finished)
