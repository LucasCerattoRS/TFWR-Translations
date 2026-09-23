[<- Amélioration de Vitesse](docs/unlocks/speed.md)
---
# If
Tu peux utiliser `if`, `elif` et `else` pour exécuter du code de manière conditionnelle.

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
condition1 = False
condition2 = False
condition3 = True

if condition1:
	do_a_flip()
elif condition2:
	harvest()
else:
	do_a_flip()
	harvest()
}}

## Syntaxe
Les `if` te permettent d'exécuter du code seulement si une condition est `True`. C'est comme une boucle `while` qui ne boucle pas.
Le `if` prend une condition tout comme la boucle `while` et exécute le bloc de code du if si la condition s'évalue à `True` :

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
condition = True

if condition:
	do_a_flip()
}}

Tu peux aussi ajouter un `else` après le `if` qui définit le bloc `else` à exécuter si la condition s'évalue à `False`.

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
condition = False

if condition:
	do_a_flip()
else:
	harvest()
}}

`elif` est le diminutif de "else if".

`if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c`

peut être raccourci en :

`if condition1:
	#a
elif condition2:
	#b
else:
	#c`

---

[Boucle while](docs/scripting/while.md)      [Opérateurs](docs/scripting/operators.md)      [Sens](docs/unlocks/senses.md)
