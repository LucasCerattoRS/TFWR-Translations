[<- Erweitern 2](docs/unlocks/expand_2.md)
---
# For-Schleife
Die `for`-Schleife funktioniert wie in Python. (In einigen Sprachen wird sie als foreach-Schleife bezeichnet, nicht zu verwechseln mit der C-artigen for-Schleife, die etwas anderes ist).

`for i in sequence:
	#mache etwas mit i`

Ähnlich wie die `while`-Schleife ruft auch die `for`-Schleife wiederholt einen Codeblock auf. Anstatt basierend auf einer Bedingung zu schleifen, führt sie den Schleifenkörper einmal für jedes Element in einer Sequenz aus.

## Syntax
Eine for-Schleife sieht so aus:

`for variablen_name in sequenz:
	#Codeblock`

`variablen_name` kann ein beliebiger Name deiner Wahl sein. Es ist eine Variable, die das aktuelle Element in der Sequenz speichert. `sequenz` muss ein Wert sein, über den iteriert werden kann, wie ein Zahlenbereich. Der Codeblock wird für jedes Element ausgeführt, wobei der Schleifenvariable dieses Element zugewiesen wird.

## Sequenzen
[Ranges](functions/range)      <unlock=lists>[Listen](docs/scripting/lists.md)      </unlock><unlock=functions>[Tupel](docs/scripting/tuples.md)      </unlock><unlock=dicts>[Dictionaries](docs/scripting/dicts.md)      </unlock><unlock=sets>[Sets](docs/scripting/sets.md)</unlock>

## Beispiel
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
for i in range(5):
    harvest()
}}

Diese Schleife führt den Körper eine feste Anzahl von Malen aus. Es ist im Wesentlichen dasselbe wie das Schreiben von

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
i = 0
harvest()
i = 1
harvest()
i = 2
harvest()
i = 3
harvest()
i = 4
harvest()
}}


---

[While-Schleife](docs/scripting/while.md)      [Break](docs/scripting/break.md)      [Continue](docs/scripting/continue.md)

[range()](functions/range)
