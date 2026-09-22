[<- Bergbau](docs/unlocks/mining.md) <right>[Eisen ->](docs/unlocks/iron.md)
<right>[Springen ->](docs/unlocks/jump.md)
---
# Kohle

Es stellt sich heraus, dass der Boden direkt unter der Oberfläche ein guter Ort ist, um Kohlevorkommen zu finden.

Kohle entsteht zufällig in horizontalen Schichten, die 1 Block dick sind. Die Größe der Schichten wächst proportional zu deiner Weltgröße. Es kann sich also lohnen, sie zu erhöhen, um mehr Kohle zu finden!

Das folgende Programm ist ein guter Ausgangspunkt für die Kohlesuche. Es gräbt nach unten, bis es eine Kohleschicht findet, und gräbt dann östlich und westlich davon weiter, um hoffentlich noch mehr Kohle zu entdecken.

{{codeexample 
{
    "camera_position": {"x": -1, "y": 0, "z": 8},
    "show_image": true,
    "image_size": {"x": 800, "y": 300},
    "show_code": true,
    "show_inventory": true,
    "show_output": false,
    "collapsing": false,
    "autoplay": true,
    "items": [{"item": "hay", "n": 100}, {"item": "wood", "n": 100}],
    "world_size": {"x": 4, "y": 4},
    "execution_speed": 4,
    "digging_speed": 2,
    "action_ticks": 200,
    "operation_ticks": 200,
    "seed": 2
}
#SETUP
move(North)
move(East)
move(East)
#CODE
while get_ground_type() != Grounds.Coal:
    dig()
dig()
move(East)
dig()
move(West)
move(West)
dig()
}}

---

[Statistiken](docs/stats.md)      [Bergbau](docs/unlocks/mining.md)      [Unterirdische Sinne](docs/unlocks/underground_senses.md)

[move()](functions/move)      [get_ground_type()](functions/get_ground_type)      [dig()](functions/dig)
