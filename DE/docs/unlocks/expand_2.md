[<- Erweitern 1](docs/unlocks/expand_1.md)
---
# Erweitern 2
Deine Farm hat sich wieder erweitert! Jetzt liegen die Felder nicht mehr in einer schönen Reihe, also musst du einen Weg finden, ein quadratisches Gitter zu durchqueren.

Mit der `while`-Schleife ist das nicht möglich, bis du Sinne und Operatoren freischaltest.
Es ist Zeit, die `for`-Schleife einzuführen.

Du kannst alles über die `for`-Schleife auf der Seite [For-Schleife](docs/scripting/for.md) lesen, aber vorerst benötigst du sie nur, um Code eine feste Anzahl von Malen zu wiederholen.

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
for i in range(5):
	do_a_flip()
}}

`range(n)` erzeugt einen Bereich von Zahlen von `0` bis `n - 1`, der `n` Elemente enthält. Die `for`-Schleife führt ihren Schleifenkörper einmal für jedes Element in der Sequenz aus. In diesem Beispiel wird `do_a_flip()` `5` Mal aufgerufen.

Die Funktion `get_world_size()` ist jetzt auch verfügbar. Sie gibt die Seitenlänge deiner Farm zurück. Auf diese Weise kannst du Code schreiben, der beim nächsten Erweiterungs-Upgrade nicht kaputt geht.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
for i in range(get_world_size()):
	harvest()
	move(North)
}}

Dieses Beispiel erntet eine Spalte der Farm für jede Farmgröße.

Wenn du nicht weiterkommst und versuchst herauszufinden, wie du die Drohne auf der Farm bewegen kannst, sieh dir den Hinweis unten an.
<spoiler=zeige Hinweis>Es gibt natürlich mehrere Möglichkeiten, sich auf der Farm zu bewegen.
Was wir suchen, ist eine Möglichkeit, sie systematisch zu durchqueren, die nicht kaputt geht, wenn die Farm wieder wächst.
Eine systematische Methode, um jede Stelle der Farm zu erreichen, besteht darin, die folgenden beiden Schritte endlos zu wiederholen:

1. Bewege dich nach `North`, bis die Drohne auf die andere Seite wechselt.
2. Bewege dich nach `East`.

`for i in range(get_world_size()):` könnte hilfreich sein, um diese Idee in Code umzusetzen.
</spoiler>
<spoiler=zeige mögliche Lösung>
{{codeexample 
{
    "camera_position": {"x": -1, "y": 1.8, "z": 5},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
do_a_flip()
#CODE
for i in range(get_world_size()):
	for j in range(get_world_size()):
		#mache einen Salto auf jedem Feld
		do_a_flip()
		move(North)
	move(East)
}}
</spoiler>

---

[For-Schleife](docs/scripting/for.md)      [While-Schleife](docs/scripting/while.md)      [Variablen](docs/scripting/variables.md)

[move()](functions/move)      [get_world_size()](functions/get_world_size)
