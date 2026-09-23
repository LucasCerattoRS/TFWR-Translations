[<- Variablen](docs/scripting/variables.md) <right>[Import ->](docs/scripting/import.md)
---
# Funktionen
Benutze das `def`-Schlüsselwort, um eine neue Funktion zu definieren:
`def f(arg1, arg2 = False):
	#Funktionscode`

Du kannst den Aufruf-Operator `()` benutzen, um die Funktion aufzurufen:
`f(42)`

Siehe auch [Geltungsbereiche (Scopes)](docs/scripting/scopes.md), um mehr über lokale und globale Variablen in Funktionen zu erfahren.

## Einführung
Du hast bereits eingebaute Funktionen wie `harvest()` gesehen.
Du kannst auch deine eigenen Funktionen definieren, was es dir ermöglicht, deinen Code modular zu strukturieren. Im Grunde genommen kannst du damit einem Codeblock einen Namen geben, sodass du ihn von überall aufrufen kannst.

## Funktionsdefinitionen
Zum Beispiel könntest du eine Funktion definieren, die die Drohne mehrmals bewegt.

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
def move_n_dir(n, dir):
	for i in range(n):
		move(dir)
}}

Das `def`-Schlüsselwort signalisiert, dass dies eine Funktionsdefinition ist.
`move_n_dir` ist der Name, an den die Funktion gebunden wird. Dies kann jeder gültige Variablenname sein und wird verwendet, um die Funktion aufzurufen.
`n` und `dir` sind Parameter. Das sind Variablen, die die Werte enthalten, die an die Funktion übergeben werden (diese Werte werden auch Argumente genannt). Du kannst einer Funktionsdefinition so viele Parameter hinzufügen, wie du möchtest.
Nach dem `:` kommt der Codeblock, der ausgeführt wird, wenn die Funktion aufgerufen wird.

Der folgende Code bewegt die Drohne dann `2` Felder nach `North` und `2` Felder nach `East`.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 3},
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
def move_n_dir(n, dir):
	for i in range(n):
		move(dir)

move_n_dir(2, North)
move_n_dir(2, East)
}}

Wenn du `def function():` siehst, solltest du es dir wirklich als eine Variablenzuweisung wie diese vorstellen:
`function = create_new_function_object()`
Wie bei allen Zuweisungen kannst du die Variable nicht verwenden, bevor ihr ein Wert zugewiesen wurde!
Die `def`-Anweisung muss vor allen Funktionsaufrufen ausgeführt werden.
Dieser Code wird einen Fehler auslösen:

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
func()
def func():
	pass
}}

## Rückgabewerte
Benutze das `return`-Schlüsselwort, um eine Funktion einen Wert zurückgeben zu lassen.
Zum Beispiel definiert die folgende Funktion die Exklusiv-Oder-Operation. Das Exklusiv-Oder gibt `True` zurück, wenn ein Wert `True` und der andere `False` ist:

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
#CODE
def xor(a, b):
	return a != b

if xor(True, False):
	do_a_flip()
}}

[Tupel](docs/scripting/tuples.md) ermöglichen die Rückgabe mehrerer Werte.

## Standardargumente
Du kannst auch Standardwerte festlegen, die verwendet werden, wenn die entsprechenden Argumente weggelassen werden.

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
#CODE
def f(a = False):
	if a:
		do_a_flip()

f()

f(True)
}}

Einem Argument, das einen Standardwert hat, kann kein Argument folgen, das keinen Standardwert hat.

## Fortgeschrittene Funktionsnutzung
Funktionen sind Werte wie jeder andere Wert auch, und die `def`-Anweisung verhält sich einfach wie eine Zuweisungsanweisung, die die Funktion dem Namen zuweist, den du ihr gibst.
Das ermöglicht Dinge wie diese:

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
#CODE
def f():
	def d():
		do_a_flip()
	return d

f()()
}}

Hier ruft `f()` die Funktion `f` auf, welche eine neue Funktion `d` definiert und zurückgibt. Das zweite `()` führt dann die zurückgegebene Funktion aus und macht einen Salto.
(Solche Dinge zu tun ist normalerweise keine gute Idee, weil es schwer zu durchschauen ist, was passiert)

Funktionen, die andere Funktionen als Argumente entgegennehmen, lassen dich richtig kreativ werden:

{{codeexample 
{
    "camera_position": {"x": -2, "y": 1.5, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": true,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "fertilizer", "n": 4}],
    "world_size": {"x": 5, "y": 1},
    "execution_speed": 1,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 100,
    "seed": 1,
    "exclude_unlocks": ["watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
def f(g, arg):
	for _ in range(4):
		g(arg)

f(move, East)
plant(Entities.Tree)
f(use_item, Items.Fertilizer)
}}

---

[Variablen](docs/scripting/variables.md)      [Namensbereiche (Scopes)](docs/scripting/scopes.md)      [Tupel](docs/scripting/tuples.md)      [Import](docs/scripting/import.md)
