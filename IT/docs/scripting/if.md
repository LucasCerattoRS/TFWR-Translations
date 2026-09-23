[<- Potenziamento Velocità](docs/unlocks/speed.md)
---
# If
Puoi usare `if`, `elif` ed `else` per eseguire il codice in modo condizionale.

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

## Sintassi
Le istruzioni `if` permettono di eseguire il codice solo se una condizione è `True`. Sono come un ciclo `while` che non si ripete.
Un'istruzione `if` accetta una condizione, proprio come un ciclo `while`, ed esegue il proprio blocco di codice se la condizione restituisce `True`:

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

Puoi anche aggiungere un blocco `else` dopo il blocco `if`. Il blocco `else` viene eseguito se la condizione restituisce `False`.

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

`elif` è l'abbreviazione di "else if".

`if condizione1:
	#a
else:
	if condizione2:
		#b
	else:
		#c`

può essere abbreviato in:

`if condizione1:
	#a
elif condizione2:
	#b
else:
	#c`

---

[Ciclo While](docs/scripting/while.md)      [Operatori](docs/scripting/operators.md)      [Sensori](docs/unlocks/senses.md)
