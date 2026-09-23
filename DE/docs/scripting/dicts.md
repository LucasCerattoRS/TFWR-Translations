[<- Listen](docs/scripting/lists.md) <right>[Kosten ->](docs/unlocks/costs.md)
---
# Dictionaries
Dictionaries sind eine Datenstruktur, die es dir ermöglicht, Schlüssel auf Werte abzubilden, so wie ein echtes Wörterbuch Wörter auf ihre Definitionen abbildet, und du kannst sie sehr schnell nachschlagen.

Ein Dictionary kann so erstellt werden:

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
right_of = {North:East, East:South, South:West, West:North}
}}

Der Ausdruck vor dem Doppelpunkt ist der Schlüssel und der Ausdruck nach dem Doppelpunkt ist der Wert, auf den der Schlüssel abbildet.
Das obige Dictionary bildet jede Richtung auf die Richtung rechts davon ab.

Hier ist ein weiteres Dictionary, das die Position der Drohne dem darunterliegenden Objekt zuordnet.
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
x, y = get_pos_x(), get_pos_y()
entity_dict = {(x,y):get_entity_type()}
}}

Der Zugriff auf den Wert, der einem Schlüssel zugeordnet ist, ähnelt dem Zugriff auf ein Element in einer Liste:
`value = dict[key]`

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
right_of = {North:East, East:South, South:West, West:North}
print(right_of[South])
}}

Du kannst ein neues Schlüssel-Wert-Paar zu einem Dictionary hinzufügen, so wie hier:
`dict[key] = value`

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
    "items": [],
    "world_size": {"x": 3, "y": 1},
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
plant(Entities.Bush)
move(East)
plant(Entities.Tree)
move(East)
#CODE
entity_dict = {}
for _ in range(3):
	entity_dict[(get_pos_x(), get_pos_y())] = get_entity_type()
	move(East)
print(entity_dict)
}}

Schlüssel sind einzigartig, daher überschreibt das Hinzufügen eines Schlüssels, der bereits im Dictionary vorhanden ist, den vorherigen Wert.

Verwende `dict.pop(key)`, um ein Schlüssel-Wert-Paar aus `dict` zu entfernen.

`key in dict` wird zu `True` ausgewertet, wenn `key` ein Schlüssel im `dict` ist, und andernfalls zu `False`.
Du kannst also `if key in dict:` verwenden, um zu prüfen, ob `dict` den Schlüssel enthält.

Wenn du ein Dictionary in einer `for`-Schleife verwendest, kannst du über alle seine Schlüssel iterieren:
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
right_of = {North:East, East:South, South:West, West:North}
print(North in right_of)
for key in right_of:
	value = right_of[key]
	print(key, ":", value)
}}

Es gibt keine Garantien bezüglich der Reihenfolge, in der die Schlüssel durchlaufen werden.

Siehe auch [Sets](docs/scripting/sets.md)

---

[Listen](docs/scripting/lists.md)      [Sets](docs/scripting/sets.md)      [Tupel](docs/scripting/tuples.md)      [Kosten](docs/unlocks/costs.md)

[len()](functions/len)
