[<- Pflanzen](docs/unlocks/plant.md) <right>[Debug 2 ->](docs/unlocks/debug2.md)
<right>[Zeitmessung ->](docs/unlocks/timing.md)
---
# Debug
Manchmal funktioniert dein Code einfach nicht und du musst herausfinden, warum. Es gibt ein paar Werkzeuge, die dir dabei helfen.

Das erste ist, das Programm Schritt für Schritt auszuführen.
Du kannst mit dem Button neben dem Ausführen-Button oder durch Setzen eines Haltepunkts in den Schritt-für-Schritt-Modus wechseln.

Haltepunkte können hinzugefügt werden, indem du auf das Haltepunkt-Panel links vom Code klickst.
![|x227](Breakpoints)
Wenn die Ausführung die Zeile erreicht, in der sich der Haltepunkt befindet, wechselt sie automatisch in den Schritt-für-Schritt-Modus.

Wenn du mit der Maus über eine Variable fährst, wird ihr aktueller Wert angezeigt.

Die `print()`-Funktion kann auch sehr nützlich sein. Sie schreibt jeden an sie übergebenen Wert direkt in die Luft.

Beispiele:

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
print(0.24)
}}

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
print(can_harvest())
}}

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
print(get_pos_x(), get_pos_y())
}}

Die `print()`-Funktion gibt den Wert direkt in die Luft und auf die [Ausgabe](docs/output.md)-Seite aus.

Das Schreiben in die Luft kann manchmal etwas langsam sein, wenn du viele Werte ausgeben möchtest.
In diesem Fall kannst du die `quick_print()`-Funktion verwenden, die nur in das Ausgabefenster schreibt.

Das Ausgabefenster protokolliert auch Warnungen und Fehler. Wenn also etwas nicht wie erwartet funktioniert, kann es nützlich sein, das zu überprüfen.

Wenn die Ausführung endet, wird die Ausgabe außerdem in die Datei [output.txt](persistent_data_path/output.txt) im Spielordner geschrieben.

---

[Ausgabe](docs/output.md)      [Kommentare](docs/scripting/comments.md)      [Debug 2](docs/unlocks/debug2.md)      [Farbige Blöcke](docs/unlocks/debug_place.md)      [Simulation](docs/unlocks/simulation.md)

[print()](functions/print)      [quick_print()](functions/quick_print)
