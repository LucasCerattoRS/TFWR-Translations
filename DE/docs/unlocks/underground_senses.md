[<- Bergbau](docs/unlocks/mining.md)
---
# Unterirdische Sinne

Statten wir deine Drohne mit einigen Sensoren aus, damit sie sich unter der Erde zurechtfindet.

Du kannst jetzt mit `get_pos_z()` die Höhe der Drohne abfragen. Sie beginnt bei 0 und wird negativ, während die Drohne nach unten fliegt.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "exclude_unlocks": ["watering", "fertilizer"],
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#CODE
move(North)
move(North)
move(East)
dig()
dig()
dig()
print(get_pos_z())
}}

`get_ground_type()` gibt die Art des Bodens unter der Drohne zurück. Du kannst eine Richtung als Argument übergeben – zum Beispiel `get_ground_type(North)` –, um die Bodenart eines benachbarten Feldes abzufragen.

So prüfst du, ob der Block unter der Drohne aus Erde besteht:

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 1
}
#CODE
dig()
if get_ground_type() == Grounds.Dirt:
    do_a_flip()
}}


`get_hardness()` gibt die Härte des Bodenfeldes unter der Drohne zurück. Du kannst eine Richtung als Argument übergeben, etwa `get_hardness(North)`. Je härter ein Feld ist, desto länger dauert es, es abzubauen.

`get_stability()` gibt die Stabilität des Bodenfeldes unter der Drohne zurück. Du kannst eine Richtung als Argument übergeben, etwa `get_stability(North)`. Eine Stabilität von 1 bedeutet, dass der Block einen Höhenunterschied von 1 aushält, bevor er einstürzt.

Beachte, dass die vier Blöcke direkt neben der Drohne unabhängig von ihrer Stabilität entfernt werden, während sich die Drohne nach unten gräbt – außer ein Block erfüllt eine besondere Funktion. Ton, Eisen und Quarz werden von dieser Regel beispielsweise nicht entfernt. Bei mangelnder Stabilität können sie jedoch weiterhin einstürzen.
---

[Bergbau](docs/unlocks/mining.md)      [Sinne](docs/unlocks/senses.md)

[get_pos_z()](functions/get_pos_z)      [get_ground_type()](functions/get_ground_type)      [get_hardness()](functions/get_hardness)      [get_stability()](functions/get_stability)
