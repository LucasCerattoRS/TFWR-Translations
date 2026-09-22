[<- Eisen](docs/unlocks/iron.md) <right>[Pilze ->](docs/unlocks/mushroom.md)
---
# Quarz

Quarz wächst in nadelförmigen Adern nahe dem unteren Ende der Steinschicht und in der harten Erde darunter. Die Adern bilden senkrechte Säulen, wodurch sie durch bloßes Ausprobieren nur schwer zu finden sind.

Zum Glück können wir unser Eisen zu etwas verbiegen, das einer Wünschelrute ähnelt und mit dem wir diese Quarzadern leichter aufspüren können. Der entsprechende Befehl lautet `prospect_quartz()`.

`prospect_quartz()` funktioniert anders als `prospect_iron()`. Statt die Richtung zum nächstgelegenen Quarzerz zurückzugeben, liefert der Befehl die euklidische Entfernung (3D-Entfernung) zum nächstgelegenen Quarz. Die Ausführung von `prospect_quartz()` kostet 1 Eisen, daher solltest du den Befehl sparsam einsetzen.

Wenn `prospect_quartz()` keinen Quarz in der Nähe findet oder du nicht genug Eisen für die Suche hast, gibt der Befehl `None` zurück.

Mit dem folgenden Code gräbt sich deine Drohne durch die Erde und tief in die Steinschicht. Mit etwas Glück befindet sich dort eine Quarzader in der Nähe. In diesem Fall gibt deine Drohne die Entfernung zu ihr aus.

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
    "items": [{"item": "hay", "n": 100}, {"item": "iron", "n": 100}],
    "world_size": {"x": 3, "y": 3},
    "execution_speed": 8,
    "digging_speed": 16,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 9,
    "exclude_unlocks": ["watering", "fertilizer", "mushrooms", "dynamite"]
}

#CODE
move(East)
move(North)
while get_ground_type() != Grounds.Rock:
    dig()
for i in range(30):
    dig()
do_a_flip()
do_a_flip()
print(prospect_quartz())
}}

---

[Statistiken](docs/stats.md)      [Bergbau](docs/unlocks/mining.md)      [Unterirdische Sinne](docs/unlocks/underground_senses.md)      [Variablen](docs/scripting/variables.md)      [Operatoren](docs/scripting/operators.md)

[move()](functions/move)      [dig()](functions/dig)      [get_ground_type()](functions/get_ground_type)      [prospect_quartz()](functions/prospect_quartz)
