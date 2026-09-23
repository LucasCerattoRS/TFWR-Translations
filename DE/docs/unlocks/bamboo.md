[<- Reis](docs/unlocks/rice.md) <right>[Farbige Blöcke ->](docs/unlocks/debug_place.md)
<right>[Pyramiden ->](docs/unlocks/pyramid.md)
---
# Bambus

Bambus ist eine Pflanze, die bis zu 6 Blöcke hoch wachsen kann. Solange sich eine Drohne über ihm befindet, wächst er nicht. Bewege die Drohne nach `plant(Entities.Bamboo)` also unbedingt mit `move` weg. Das Pflanzen von Bambus kostet Reis.

Bambus bildet in einer zufällig bestimmten Höhe Blüten. Mit `measure()` kannst du prüfen, in welcher Höhe er blühen wird. `measure()` beginnt bei 0 zu zählen. Blüht der Bambus also am zweiten Block, gibt `measure()` den Wert 1 zurück:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 1000, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "rice", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
print(measure())
move(East)
}}

Den höchsten Bambusertrag erhältst du, wenn du `harvest()` aufrufst, während sich deine Drohne direkt über der Blüte befindet. Für jeden Block Abstand wird der Ertrag durch acht geteilt.
Wenn sich die Blüte beispielsweise auf Höhe 3 befindet und du den Bambus zwei Blöcke darüber erntest, wird der Ertrag durch 64 geteilt.

Um höher gelegene Blüten zu ernten, fliegst du seitlich in den Bambus hinein, sobald die Drohne die gewünschte Höhe erreicht hat. Der neu freigeschaltete Befehl `place()` hilft dir dabei.

Stapele mit `place(Grounds.Dirt)` Blöcke neben dem Bambus, um nach oben zu gelangen. Fliege dann mit `move()` von der Seite in den Bambus hinein. Beim Aufruf von `harvest()` sollte sich deine Drohne direkt über der Blüte befinden.

`place(Grounds.Dirt)` kostet 1 Block! Du kannst auch andere Böden wie `Grounds.Rock` platzieren, aber keine besonderen Blöcke wie `Grounds.Clay`.

Bambus wächst genau 1 Block pro Sekunde.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 1000, "y": 500},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "block", "n": 100}, {"item": "rice", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "coal"]
}
#SETUP
move(North)
move(East)
#CODE
till()
plant(Entities.Bamboo)
print(measure())
move(East)
place(Grounds.Dirt)
do_a_flip() # kurz warten
do_a_flip()
move(West)
harvest()
}}

---

[Statistiken](docs/stats.md)      [For-Schleife](docs/scripting/for.md)      [Variablen](docs/scripting/variables.md)      [If](docs/scripting/if.md)      [Funktionen](docs/scripting/functions.md)      [Reis](docs/unlocks/rice.md)

[harvest()](functions/harvest)      [plant()](functions/plant)      [move()](functions/move)      [till()](functions/till)      [place()](functions/place)      [measure()](functions/measure)
