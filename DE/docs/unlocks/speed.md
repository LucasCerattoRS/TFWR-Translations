[<- While-Schleife](docs/scripting/while.md) <right>[Erweitern 1 ->](docs/unlocks/expand_1.md)
<right>[Pflanzen ->](docs/unlocks/plant.md)
---
# Geschwindigkeits-Upgrade
Die Ausführungsgeschwindigkeit wurde verdoppelt. Das Problem ist, dass die Drohne jetzt schneller erntet, als das Gras wachsen kann, was zu keiner Ernte führt. Um damit umzugehen, sind jetzt [if](docs/scripting/if.md)-Verzweigungen und die [can_harvest()](functions/can_harvest)-Funktion freigeschaltet.

## Überprüfen vor dem Ernten
Eine `if`-Anweisung führt ihren Codeblock einmal aus, wenn die angegebene Bedingung `True` ist.

Die neue Funktion `can_harvest()` bietet eine bessere Bedingung. `can_harvest()` gibt `True` zurück, wenn die Pflanze unter der Drohne geerntet werden kann, andernfalls `False`.

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
do_a_flip()
#CODE
if can_harvest():
	do_a_flip()
}}

Du kannst dir einen solchen Rückgabewert so vorstellen, als würde der Funktionsaufruf `can_harvest()` bei der Auswertung des `if` durch den zurückgegebenen Wert `True` ersetzt.

Was passiert, wenn der obige Code ausgeführt wird:
- Die `if`-Anweisung wird ausgeführt.
- `can_harvest()` wird aufgerufen.
- `can_harvest()` gibt `True` zurück, weil das Gras ausgewachsen ist.
- Die Anweisung lautet nun `if True:`.
- Die Verzweigung wird ausgeführt, weil der Wert `True` ist.

Wenn das Gras nicht ausgewachsen wäre, würde die Drohne keinen Salto machen.

Jetzt können wir mit `if` verhindern, dass die Drohne zu früh erntet.

---

[If](docs/scripting/if.md)      [While-Schleife](docs/scripting/while.md)

[harvest()](functions/harvest)      [can_harvest()](functions/can_harvest)
