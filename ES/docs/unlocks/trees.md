[<- Zanahorias](docs/unlocks/carrots.md) <right>[Calabazas ->](docs/unlocks/pumpkins.md)
---
# Árboles
Los [árboles](objects/tree) son una mejor manera de conseguir madera que los arbustos. Dan 5 de madera cada uno. Al igual que los arbustos, se pueden plantar en hierba o tierra.

A los árboles les gusta tener algo de espacio y plantarlos uno al lado del otro ralentizará su crecimiento. El tiempo de crecimiento se duplica por cada árbol que esté en una casilla directamente al norte, este, oeste o sur de él. Así que, si plantas árboles en cada casilla, tardarán `2*2*2*2 = 16` veces más en crecer.
{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": false,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 10,
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
for i in range(get_world_size()):
	for j in range(get_world_size()):
		plant(Entities.Tree)
		move(North)
	move(East)
}}

<spoiler=mostrar> 
El operador `%` puede ser útil aquí. El operador `%` devuelve el resto de la división. Los números pares divididos por `2` tienen un resto de `0` y los impares divididos por `2` tienen un resto de `1`.
Así puedes comprobar si un número es par:

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
def is_even(n):
	return n % 2 == 0

print("is_even(0): ", is_even(0))
print("is_even(1): ", is_even(1))
print("is_even(2): ", is_even(2))
print("is_even(5): ", is_even(5))
print("is_even(-1): ", is_even(-1))
print("is_even(x): ", is_even(get_pos_x()))
}}
</spoiler>

---

[Estadísticas](docs/stats.md)      [Operadores](docs/scripting/operators.md)      [If](docs/scripting/if.md)      [Bucle for](docs/scripting/for.md)      [Policultivo](docs/unlocks/polyculture.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)
