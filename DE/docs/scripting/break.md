[<- While-Schleife](docs/scripting/while.md)
---
# Break
`break` ermöglicht es, eine Schleife vorzeitig zu beenden. Wenn die `break`-Anweisung erreicht wird, wird die innerste Schleife sofort verlassen und der Code nach der Schleife ausgeführt.

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
for i in range(10):
	break
print(i)
}}

Dies gibt `0` aus, weil `i` in der ersten Iteration der Schleife `0` ist und dann die `break`-Anweisung die Schleife beendet.

Es funktioniert auch bei `while`-Schleifen.

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
plant(Entities.Tree)
#CODE
while True:
	if can_harvest():
		break
harvest()
}}

Dieser Code führt die `while`-Schleife aus, bis `can_harvest()` `True` ist.
Es hat den gleichen Effekt wie:

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
plant(Entities.Tree)
#CODE
while not can_harvest():
	pass
harvest()
}}

In verschachtelten Schleifen beendet `break` immer die innerste Schleife.

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
for i in range(10):
	for j in range(10):
		break
		print("dies wird nie ausgegeben")
	print("dies wird 10-mal ausgegeben")
}}

---

[While-Schleife](docs/scripting/while.md)      [For-Schleife](docs/scripting/for.md)      [Continue](docs/scripting/continue.md)
