[<- Ulepszenie prędkości](docs/unlocks/speed.md)
---
# If
Możesz używać `if`, `elif` i `else`, aby uruchamiać kod warunkowo.

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

## Składnia
Instrukcje `if` pozwalają uruchomić kod tylko wtedy, gdy warunek ma wartość `True`. Są jak pętla `while`, która się nie zapętla.
Instrukcja `if` przyjmuje warunek, tak jak pętla `while`, i wykonuje swój blok kodu, jeśli warunek ma wartość `True`:

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

Możesz także dodać blok `else` po bloku `if`. Blok `else` jest wykonywany, jeśli warunek ma wartość `False`.

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

`elif` to skrót od „else if” (w przeciwnym razie, jeśli).

`if condition1:
	#a
else:
	if condition2:
		#b
	else:
		#c`

można skrócić do:

`if condition1:
	#a
elif condition2:
	#b
else:
	#c`
---

[Pętla While](docs/scripting/while.md)      [Operatory](docs/scripting/operators.md)      [Zmysły](docs/unlocks/senses.md)
