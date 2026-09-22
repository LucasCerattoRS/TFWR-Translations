[<- Bewässerung](docs/unlocks/watering.md)
---
# Sonnenblumen
[Sonnenblumen](objects/sunflower) sammeln die Energie der Sonne. Du kannst diese Energie ernten. 

Das Pflanzen funktioniert genauso wie bei Karotten oder Kürbissen. 

Das Ernten einer ausgewachsenen Sonnenblume liefert Energie.
Wenn mindestens 10 Sonnenblumen auf der Farm sind und du die mit der größten Anzahl an Blütenblättern erntest, bekommst du `8` mal mehr Energie!
Wenn du eine Sonnenblume erntest, während eine andere Sonnenblume mehr Blütenblätter hat, gibt auch die nächste Ernte nur die normale Menge Energie (nicht den 8x Bonus).

`measure()` gibt die Anzahl der Blütenblätter der Sonnenblume unter der Drohne zurück.
Sonnenblumen haben mindestens `7` und höchstens `15` Blütenblätter.
Sonnenblumen können bereits vor dem vollständigen Auswachsen gemessen werden und zählen dann schon für die Grenze von 10 Sonnenblumen.

Mehrere Sonnenblumen können die gleiche Anzahl an Blütenblättern haben, sodass es auch mehrere Sonnenblumen mit der größten Anzahl an Blütenblättern geben kann. In diesem Fall ist es egal, welche davon du erntest.
{{codeexample 
{
    "camera_position": {"x": -1.5, "y": 2, "z": 4},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "inventory_scale": 5,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "carrot", "n": 10}],
    "world_size": {"x": 5, "y": 2},
    "execution_speed": 2,
    "digging_speed": 1,
    "action_ticks": 200,
    "operation_ticks": 1,
    "seed": 4,
    "exclude_unlocks": ["fertilizer", "watering"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
move(North)
for _ in range(5):
    till()
    plant(Entities.Sunflower)
    move(East)
move(North)
do_a_flip()
do_a_flip()
do_a_flip()
do_a_flip()
do_a_flip()
#CODE
for _ in range(5):
    till()
    plant(Entities.Sunflower)
    print(measure())
    move(East)
for _ in range(5):
    while not can_harvest():
        pass
    harvest()
    move(East)
}}

Solange du Energie hast, nutzt die Drohne sie, um doppelt so schnell zu arbeiten.
Sie verbraucht alle 30 Aktionen 1 Energie, beispielsweise bei Bewegungen, beim Ernten oder beim Pflanzen.
Auch die Ausführung anderer Codeanweisungen kann Energie verbrauchen, allerdings deutlich weniger als Drohnenaktionen.

Im Allgemeinen wird alles, was durch Geschwindigkeits-Upgrades beschleunigt wird, auch durch Energie beschleunigt.
Alles, was durch Energie beschleunigt wird, verbraucht auch Energie proportional zur Ausführungszeit, wobei Geschwindigkeits-Upgrades ignoriert werden.
---

[Statistiken](docs/stats.md)      [Listen](docs/scripting/lists.md)      [Dictionaries](docs/scripting/dicts.md)      [Variablen](docs/scripting/variables.md)      [For-Schleife](docs/scripting/for.md)      [If](docs/scripting/if.md)      [Operatoren](docs/scripting/operators.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [measure()](functions/measure)
