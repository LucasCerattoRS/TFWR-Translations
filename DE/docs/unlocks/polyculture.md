[<- Kürbisse](docs/unlocks/pumpkins.md)
---
# Polykultur
Du hast vielleicht schon bemerkt, dass Pflanzen manchmal mehr Ertrag bringen, wenn sie zusammen gepflanzt werden.
Gras, Büsche, Bäume und Karotten liefern einen höheren Ertrag, wenn sie den richtigen Pflanzenbegleiter haben. Jede einzelne Pflanze hat eine andere, nicht vorhersagbare Begleitervorliebe. Zum Glück kannst du die Vorliebe der Pflanze unter der Drohne mit `get_companion()` messen. Die Funktion gibt ein Tupel zurück, dessen erstes Element die gewünschte Pflanzenart und dessen zweites Element die gewünschte Position des Begleiters angibt. Der Begleiter muss für den Ertragsbonus nicht vollständig ausgewachsen sein.

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
    "operation_ticks": 20,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer"],
    "starting_chunk": 0,
    "dlc_enabled": false
}
#SETUP
#CODE
plant(Entities.Bush)
plant_type, (x, y) = get_companion()
print(plant_type, (x, y))
move(East)
move(South)
plant(plant_type)
move(West)
move(North)
do_a_flip()
harvest()
}}

Eine Pflanze kann `Entities.Grass`, `Entities.Bush`, `Entities.Tree` oder `Entities.Carrot` als Begleiter bevorzugen. Jede Pflanze wählt zufällig, entscheidet sich aber immer für eine andere Pflanzenart als ihre eigene. Die Position kann mit Ausnahme der Position der Pflanze selbst überall innerhalb von 3 Schritten liegen.

Wenn sich unter der Drohne keine Pflanze mit einer Begleitervorliebe befindet, gibt `get_companion()` `None` zurück.

Bevor die Polykultur zum ersten Mal freigeschaltet wird, beträgt der Ertragsmultiplikator `5`. Mit jeder Verbesserung verdoppelt er sich.

---

[Statistiken](docs/stats.md)      [Tupel](docs/scripting/tuples.md)      [Dictionaries](docs/scripting/dicts.md)      [Sinne](docs/unlocks/senses.md)      [Pflanzen](docs/unlocks/plant.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [get_companion()](functions/get_companion)
