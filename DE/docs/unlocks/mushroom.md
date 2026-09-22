[<- Quarz](docs/unlocks/quartz.md) <right>[Dynamit ->](docs/unlocks/dynamite.md)
---
# Pilze

Viele Pilzarten wachsen unterirdisch in Kolonien. Suche beim Graben nach einer Schicht aus `Grounds.Mushroom`. Mit `measure()` kannst du dann den Pilztyp als Zahl ermitteln, beginnend bei `0`.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 6},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": true,
    "autoplay": false,
    "items": [{"item": "hay", "n": 100}, {"item": "iron", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 2,
    "digging_speed": 6,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "dynamite", "iron"]
}

#SETUP
jump(Unlocks.Mushrooms)
#CODE
while get_ground_type() != Grounds.Mushroom:
    dig()
do_a_flip()
print(measure())
}}

Pilze desselben Typs sind gern zusammen, aber etwas zu schüchtern, um übereinander zu wachsen. Schiebe einen Pilzblock auf einen anderen Pilzblock desselben Typs. Beide verschwinden und du erhältst dafür Pilze.

Mit `can_push(direction)` kannst du prüfen, ob sich der Block unter der Drohne schieben lässt und ob in der angegebenen Richtung etwas im Weg ist. `push(direction)` schiebt den Block und gibt zurück, ob das Schieben erfolgreich war.

Blöcke können nicht nach oben geschoben werden. Befindet sich ein anderer Block im Weg, schlägt das Schieben fehl. Werden Blöcke in die Luft geschoben, fallen sie herunter und landen auf dem nächsten Block unter ihnen.

Denke daran, dass du mit `place(Grounds.Dirt)` Blöcke unter der Drohne platzieren kannst. So kannst du Löcher auffüllen, um Blöcke darüberzuschieben.

---

[Statistiken](docs/stats.md)      [Unterirdische Sinne](docs/unlocks/underground_senses.md)      [Dictionaries](docs/scripting/dicts.md)

[move()](functions/move)      [measure()](functions/measure)      [can_push()](functions/can_push)      [push()](functions/push)      [place()](functions/place)      [get_ground_type()](functions/get_ground_type)
