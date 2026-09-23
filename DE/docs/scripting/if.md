[<- Geschwindigkeits-Upgrade](docs/unlocks/speed.md)
---
# If
Du kannst `if`, `elif` und `else` verwenden, um Code bedingt auszuführen.

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

## Syntax
Mit `if`-Anweisungen kannst du Code nur dann ausführen, wenn eine Bedingung `True` ist. Sie ähneln einer `while`-Schleife, die keine Schleife bildet.
Wie eine `while`-Schleife erhält eine `if`-Anweisung eine Bedingung und führt ihren Codeblock aus, wenn diese Bedingung `True` ergibt:

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

Du kannst auch ein `else` nach dem `if` hinzufügen, das einen `else`-Codeblock definiert, der ausgeführt wird, wenn die Bedingung zu `False` ausgewertet wird.

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

`elif` ist die Abkürzung für "else if".

`if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c`

kann verkürzt werden zu:

`if condition1:
	#a
elif condition2:
	#b
else:
	#c`

---

[While-Schleife](docs/scripting/while.md)      [Operatoren](docs/scripting/operators.md)      [Sinne](docs/unlocks/senses.md)
