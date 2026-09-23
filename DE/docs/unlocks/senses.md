[<- Operatoren](docs/scripting/operators.md)
---
# Sinne
Die Drohne kann jetzt sehen!

Die Funktionen `get_pos_x()` und `get_pos_y()` geben die aktuellen x- und y-Koordinaten der Drohne zurück. An der Startposition sind beide `0`. Die x-Koordinate erhöht sich für jedes Feld in Richtung `East` um `1`, die y-Koordinate für jedes Feld in Richtung `North` ebenfalls um `1`.
{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 2, "y": 2},
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
#CODE
print("x =", get_pos_x(), "y =", get_pos_y())
if get_pos_x() == 1 and get_pos_y() == 0:
    do_a_flip()
}}

`num_items(item)` gibt an, wie viele von einem Gegenstand du hast.
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
    "items": [{"item": "hay", "n": 10}],
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
print(num_items(Items.Hay))
}}

`get_entity_type()` und `get_ground_type()` geben den Typ der Entität oder des Bodens an, der sich unter der Drohne befindet.
{{codeexample 
{
    "camera_position": {"x": 0, "y": 1.5, "z": 6},
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
plant(Entities.Bush)
#CODE
print(get_entity_type())
if get_entity_type() == Entities.Bush:
	do_a_flip()

print(get_ground_type())
if get_ground_type() != Grounds.Soil:
	do_a_flip()
}}

Das `None`-Schlüsselwort ist jetzt auch freigeschaltet! `None` ist ein Wert, der darstellt, dass es keinen Wert gibt.
Zum Beispiel wird eine Funktion, die keine `return`-Anweisung hat, tatsächlich `None` zurückgeben.

`get_entity_type()` gibt `None` zurück, wenn sich keine Entität unter der Drohne befindet.


Wenn du herausfinden willst, wie viele von einer bestimmten Freischaltung du hast, verwende die Funktion `num_unlocked(unlock)`.

Zum Beispiel gibt `num_unlocked(Unlocks.Speed)` die Anzahl der Geschwindigkeits-Upgrades zurück, die du hast.

`num_unlocked(Unlocks.Senses)` gibt `1` zurück, wenn die Sinne freigeschaltet sind, und `0`, wenn nicht.

Du kannst `num_unlocked()` auch auf Gegenstände oder Objekte anwenden. Die Funktion gibt `1` zurück, wenn der Gegenstand oder das Objekt freigeschaltet ist, andernfalls `0`.

Achtung: `num_unlocked(Unlocks.Carrots)` gibt zurück, wie oft die Freischaltung freigeschaltet oder verbessert wurde.
`num_unlocked(Items.Carrot)` gibt dagegen nur `0` oder `1` zurück. Dasselbe gilt für andere Pflanzen.

---

[If](docs/scripting/if.md)      [Operatoren](docs/scripting/operators.md)      [Variablen](docs/scripting/variables.md)      [Tupel](docs/scripting/tuples.md)      [Dictionaries](docs/scripting/dicts.md)      [Unterirdische Sinne](docs/unlocks/underground_senses.md)

[get_pos_x()](functions/get_pos_x)      [get_pos_y()](functions/get_pos_y)      [get_entity_type()](functions/get_entity_type)      [get_ground_type()](functions/get_ground_type)      [num_items()](functions/num_items)      [num_unlocked()](functions/num_unlocked)
